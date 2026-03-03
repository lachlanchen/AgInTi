#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, Iterable, Optional, Set, Tuple


def parse_env_file(path: Path) -> Dict[str, str]:
    data: Dict[str, str] = {}
    if not path.exists():
        return data
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        data[key.strip()] = value.strip()
    return data


class RunLogger:
    def __init__(self, log_file: Path):
        self.log_file = log_file
        self.log_file.parent.mkdir(parents=True, exist_ok=True)

    def write(self, message: str) -> None:
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        line = f"[{ts}] {message}"
        print(line, flush=True)
        with self.log_file.open("a", encoding="utf-8") as fh:
            fh.write(line + "\n")


def build_arg_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Open DEC login page in Selenium, progress login, and hold for manual verification."
    )
    p.add_argument("--env-file", default="", help="Path to .env file")
    p.add_argument("--url", default="", help="Login URL")
    p.add_argument("--username", default="", help="Login username")
    p.add_argument("--password", default="", help="Login password")
    p.add_argument("--submit", action="store_true", help="Click submit/continue buttons during login flow")
    p.add_argument("--otp-from-mail", action="store_true", help="Try to fetch OTP code from Apple Mail and autofill")
    p.add_argument("--mail-subject-contains", default="", help="Filter Apple Mail OTP search by subject")
    p.add_argument("--mail-sender-contains", default="", help="Filter Apple Mail OTP search by sender")
    p.add_argument("--otp-timeout-seconds", type=int, default=150, help="OTP wait window")
    p.add_argument("--auto-course", action="store_true", help="After login, open course and progress steps automatically")
    p.add_argument("--max-course-steps", type=int, default=80, help="Max auto course actions")
    p.add_argument("--course-click-pause", type=float, default=2.0, help="Pause seconds between auto course actions")
    p.add_argument("--course-stall-retries", type=int, default=6, help="Allow N consecutive no-action stalls before taking recovery action")
    p.add_argument("--course-retry-refresh", type=int, default=2, help="Max page refresh recovery attempts when stuck")
    p.add_argument("--course-retry-wait", type=float, default=3.0, help="Pause before recovery retry when stuck")
    p.add_argument("--auto-course-attempts", type=int, default=1, help="Retry course flow N times if it exits unexpectedly")
    p.add_argument("--headless", action="store_true", help="Run browser in headless mode")
    p.add_argument("--screenshot-dir", default="", help="Directory to store screenshots")
    p.add_argument("--log-file", default="", help="Run log path")
    p.add_argument("--chrome-profile-dir", default="", help="Persistent Chrome profile dir for session/cookie reuse")
    p.add_argument("--fresh-profile", action="store_true", help="Disable profile reuse for this run")
    p.add_argument(
        "--hold-seconds",
        type=int,
        default=0,
        help="Hold browser for N seconds. Default 0 means hold until Ctrl+C.",
    )
    p.add_argument("--window-width", type=int, default=1440)
    p.add_argument("--window-height", type=int, default=980)
    return p


def first_visible_element(driver, by, selectors: Iterable[str]):
    for selector in selectors:
        try:
            element = driver.find_element(by, selector)
            if element.is_displayed() and element.is_enabled():
                return element
        except Exception:
            continue
    return None


def find_in_default_and_frames(driver, by, selectors: Iterable[str]) -> Tuple[Optional[object], str]:
    driver.switch_to.default_content()
    element = first_visible_element(driver, by, selectors)
    if element is not None:
        return element, "default"

    try:
        frames = driver.find_elements("css selector", "iframe,frame")
    except Exception:
        frames = []

    for idx in range(min(len(frames), 15)):
        try:
            driver.switch_to.default_content()
            frames_now = driver.find_elements("css selector", "iframe,frame")
            if idx >= len(frames_now):
                continue
            driver.switch_to.frame(frames_now[idx])
            element = first_visible_element(driver, by, selectors)
            if element is not None:
                return element, f"frame[{idx}]"
        except Exception:
            continue
    driver.switch_to.default_content()
    return None, "none"


def fill_field_wait(driver, by, selectors: Iterable[str], value: str, label: str, timeout: int, logger: RunLogger) -> bool:
    if not value:
        logger.write(f"[warn] empty {label}; skip fill")
        return False
    end = time.time() + timeout
    while time.time() < end:
        element, where = find_in_default_and_frames(driver, by, selectors)
        if element is not None:
            try:
                element.click()
            except Exception:
                pass
            try:
                element.clear()
            except Exception:
                pass
            element.send_keys(value)
            logger.write(f"[ok] filled {label} ({where})")
            driver.switch_to.default_content()
            return True
        time.sleep(0.6)
    logger.write(f"[warn] unable to find {label} field")
    driver.switch_to.default_content()
    return False


def click_first_wait(driver, by, selectors: Iterable[str], label: str, timeout: int, logger: RunLogger) -> bool:
    end = time.time() + timeout
    while time.time() < end:
        element, where = find_in_default_and_frames(driver, by, selectors)
        if element is not None:
            try:
                element.click()
                logger.write(f"[ok] clicked {label} ({where})")
                driver.switch_to.default_content()
                return True
            except Exception:
                pass
        time.sleep(0.4)
    logger.write(f"[warn] unable to click {label}")
    driver.switch_to.default_content()
    return False


def press_enter_on_field(driver, by, selectors: Iterable[str], label: str, logger: RunLogger) -> bool:
    element, where = find_in_default_and_frames(driver, by, selectors)
    if element is None:
        driver.switch_to.default_content()
        logger.write(f"[warn] unable to press Enter on {label}")
        return False
    try:
        element.send_keys("\n")
        logger.write(f"[ok] pressed Enter on {label} ({where})")
        driver.switch_to.default_content()
        return True
    except Exception as exc:
        driver.switch_to.default_content()
        logger.write(f"[warn] Enter key on {label} failed: {exc}")
        return False


def click_text_via_js(driver, text_tokens: Iterable[str], label: str, logger: RunLogger) -> bool:
    js = r"""
const tokens = arguments[0].map(s => String(s).toUpperCase());
const selectors = "button,input[type='submit'],input[type='button'],a,[role='button'],[role='link'],[aria-label],[title],[data-testid]";
const nodes = [];
const seen = new Set();
const maxNodes = 12000;

function collectFromRoot(root) {
  if (!root) return;
  if (nodes.length >= maxNodes) return;
  try {
    const rootNodes = Array.from(root.querySelectorAll(selectors));
    for (const n of rootNodes) {
      if (!n || seen.has(n)) continue;
      seen.add(n);
      nodes.push(n);
      if (nodes.length >= maxNodes) break;
    }
  } catch (e) {}
  try {
    const allNodes = Array.from(root.querySelectorAll("*"));
    for (const n of allNodes) {
      if (nodes.length >= maxNodes) break;
      try {
        if (n && n.shadowRoot) {
          collectFromRoot(n.shadowRoot);
        }
      } catch (e) {}
    }
  } catch (e) {}
  try {
    const frames = Array.from(root.querySelectorAll("iframe,frame"));
    for (const frame of frames) {
      if (nodes.length >= maxNodes) break;
      try {
        if (frame && frame.contentDocument) {
          collectFromRoot(frame.contentDocument);
        }
      } catch (e) {}
    }
  } catch (e) {}
}

function scoreNode(n, raw, tokenMatched) {
  const tag = String((n.tagName || "")).toUpperCase();
  const role = String((n.getAttribute && n.getAttribute("role")) || "").toUpperCase();
  let score = 0;
  if (raw === tokenMatched) score += 12;
  if (raw.startsWith(tokenMatched + " ")) score += 8;
  if (raw.includes(" " + tokenMatched + " ")) score += 6;
  if (raw.includes(tokenMatched)) score += 4;
  if (tag === "BUTTON") score += 6;
  if (tag === "INPUT") score += 5;
  if (role === "BUTTON") score += 5;
  if (tag === "A") score += 2;
  if (raw.includes("QUESTION ") && tokenMatched !== "NEXT QUESTION") score -= 8;
  if (raw.includes("MODULE") && tokenMatched === "NEXT") score -= 6;
  if (raw.length > 120) score -= 3;
  return score;
}

collectFromRoot(document);
let bestNode = null;
let bestScore = -999;

for (const n of nodes) {
  const rawCandidates = [
    n.innerText,
    n.textContent,
    n.value,
    n.getAttribute && n.getAttribute("aria-label"),
    n.getAttribute && n.getAttribute("title"),
  ].map(v => (v || "") + "");
  const raw = rawCandidates.join(" ").toUpperCase().replace(/\\s+/g, " ").trim();
  let style = null;
  try {
    style = window.getComputedStyle(n);
  } catch (e) {}
  const hiddenByStyle = style && (style.visibility === "hidden" || style.display === "none");
  const visible = !(n.offsetWidth === 0 || n.offsetHeight === 0 || hiddenByStyle);
  if (!raw) continue;
  if (!visible) continue;
  const matchedToken = tokens.find(t => raw.includes(t));
  const matched = Boolean(matchedToken);
  if (!matched) continue;
  if (n.disabled === true) continue;
  const ariaDisabled = (n.getAttribute && n.getAttribute("aria-disabled")) || "";
  if (String(ariaDisabled).toLowerCase() === "true") continue;
  const score = scoreNode(n, raw, matchedToken);
  if (score > bestScore) {
    bestNode = n;
    bestScore = score;
  }
}

if (!bestNode) return false;
try {
  bestNode.scrollIntoView({block: "center", inline: "center"});
} catch (e) {}
try {
  bestNode.click();
  return true;
} catch (e) {}
try {
  const evt = new MouseEvent("click", {bubbles: true, cancelable: true, view: window});
  bestNode.dispatchEvent(evt);
  return true;
} catch (e) {}
return false;
"""
    try:
        ok = bool(driver.execute_script(js, list(text_tokens)))
        if ok:
            logger.write(f"[ok] clicked {label} via js text matcher")
            return True
    except Exception as exc:
        logger.write(f"[warn] js click matcher failed for {label}: {exc}")
    logger.write(f"[warn] js click matcher could not find {label}")
    return False


def click_text_main_pane_via_js(driver, text_tokens: Iterable[str], label: str, logger: RunLogger) -> bool:
    js = r"""
const tokens = arguments[0].map(s => String(s).toUpperCase());
const selectors = "button,input[type='submit'],input[type='button'],a,[role='button'],[role='link'],[aria-label],[title],[data-testid]";
const seen = new Set();
const nodes = [];

function collectFrom(root) {
  if (!root) return;
  try {
    for (const n of Array.from(root.querySelectorAll(selectors))) {
      if (!n || seen.has(n)) continue;
      seen.add(n);
      nodes.push(n);
    }
  } catch (e) {}
  try {
    for (const n of Array.from(root.querySelectorAll("*"))) {
      try {
        if (n && n.shadowRoot) collectFrom(n.shadowRoot);
      } catch (e) {}
    }
  } catch (e) {}
  try {
    for (const f of Array.from(root.querySelectorAll("iframe,frame"))) {
      try {
        if (f && f.contentDocument) collectFrom(f.contentDocument);
      } catch (e) {}
    }
  } catch (e) {}
}

function nearSidebar(node) {
  let cur = node;
  for (let i = 0; i < 8 && cur; i++) {
    const id = String(cur.id || "").toUpperCase();
    const cls = String(cur.className || "").toUpperCase();
    const role = String((cur.getAttribute && cur.getAttribute("role")) || "").toUpperCase();
    const tag = String(cur.tagName || "").toUpperCase();
    if (
      role === "NAVIGATION" ||
      tag === "NAV" ||
      cls.includes("SIDEBAR") ||
      cls.includes("LESSON") ||
      cls.includes("MODULE") ||
      cls.includes("MENU") ||
      id.includes("SIDEBAR") ||
      id.includes("NAV")
    ) {
      return true;
    }
    cur = cur.parentElement;
  }
  return false;
}

function scoreNode(node, raw, matchedToken) {
  const rect = node.getBoundingClientRect();
  const tag = String((node.tagName || "")).toUpperCase();
  const role = String((node.getAttribute && node.getAttribute("role")) || "").toUpperCase();
  let score = 0;
  if (raw === matchedToken) score += 20;
  if (raw.startsWith(matchedToken + " ")) score += 10;
  if (raw.includes(" " + matchedToken + " ")) score += 8;
  if (tag === "BUTTON") score += 8;
  if (tag === "INPUT") score += 6;
  if (role === "BUTTON") score += 6;
  if (rect.width >= 80) score += 2;
  if (rect.height >= 28) score += 2;
  const centerX = rect.left + (rect.width / 2);
  const mainPaneThreshold = Math.max(360, window.innerWidth * 0.32);
  if (centerX < mainPaneThreshold) score -= 20;
  if (nearSidebar(node)) score -= 25;
  return score;
}

collectFrom(document);
let bestNode = null;
let bestScore = -999;
for (const n of nodes) {
  const rawCandidates = [
    n.innerText,
    n.textContent,
    n.value,
    n.getAttribute && n.getAttribute("aria-label"),
    n.getAttribute && n.getAttribute("title"),
  ].map(v => (v || "") + "");
  const raw = rawCandidates.join(" ").toUpperCase().replace(/\s+/g, " ").trim();
  if (!raw) continue;
  const matchedToken = tokens.find(t => raw.includes(t));
  if (!matchedToken) continue;
  if (n.disabled === true) continue;
  const ariaDisabled = String((n.getAttribute && n.getAttribute("aria-disabled")) || "").toLowerCase();
  if (ariaDisabled === "true") continue;
  let style = null;
  try { style = window.getComputedStyle(n); } catch (e) {}
  const hidden = style && (style.visibility === "hidden" || style.display === "none" || style.opacity === "0");
  if (hidden) continue;
  if (n.offsetWidth === 0 || n.offsetHeight === 0) continue;
  const score = scoreNode(n, raw, matchedToken);
  if (score > bestScore) {
    bestScore = score;
    bestNode = n;
  }
}
if (!bestNode) return false;
try { bestNode.scrollIntoView({block: "center", inline: "center"}); } catch (e) {}
try { bestNode.click(); return true; } catch (e) {}
try {
  const evt = new MouseEvent("click", {bubbles: true, cancelable: true, view: window});
  bestNode.dispatchEvent(evt);
  return true;
} catch (e) {}
return false;
"""
    try:
        ok = bool(driver.execute_script(js, list(text_tokens)))
        if ok:
            logger.write(f"[ok] clicked {label} via main-pane js matcher")
            return True
    except Exception as exc:
        logger.write(f"[warn] main-pane js click matcher failed for {label}: {exc}")
    logger.write(f"[warn] main-pane js click matcher could not find {label}")
    return False


def pick_question_answer(driver, logger: RunLogger) -> bool:
    js = r"""
const questions = ["QUESTION", "CHOOSE ONLY ONE", "CHOOSE ALL THAT APPLY", "SELECT THE CORRECT", "MULTIPLE CHOICE"];
const questionStopWords = ["A", "AN", "AND", "ARE", "AS", "AT", "THE", "THIS", "THAT", "THEN", "WHEN", "WHERE", "WITH", "WHAT", "WHICH", "WHETHER", "HOW", "WHY", "WHEN", "FROM", "FOR", "FOR", "IN", "IS", "ON", "OF", "OR", "TO", "IF", "BE", "HAS", "HAVE", "HAD", "WAS", "WERE"];
const optionLeadRegex = /^[A-E]\b/;

function forceClickNode(node) {
  try {
    node.focus();
  } catch (e) {}
  try {
    node.click();
    return true;
  } catch (e) {}
  try {
    const mdown = new MouseEvent("mousedown", {bubbles: true, cancelable: true, view: window});
    node.dispatchEvent(mdown);
    const mup = new MouseEvent("mouseup", {bubbles: true, cancelable: true, view: window});
    node.dispatchEvent(mup);
    const click = new MouseEvent("click", {bubbles: true, cancelable: true, view: window});
    node.dispatchEvent(click);
    const change = new Event("change", {bubbles: true, cancelable: true});
    node.dispatchEvent(change);
    return true;
  } catch (e) {}
  return false;
}

function nearestClickable(node) {
  let cur = node;
  for (let i = 0; i < 6 && cur; i++) {
    const tag = String((cur.tagName || "").toUpperCase());
    const role = String(cur.getAttribute && cur.getAttribute("role")).toUpperCase();
    if (
      tag === "BUTTON" ||
      tag === "A" ||
      tag === "LABEL" ||
      tag === "INPUT" ||
      tag === "LI" ||
      tag === "SPAN" ||
      tag === "DIV" ||
      role === "BUTTON" ||
      role === "RADIO" ||
      role === "CHECKBOX" ||
      (cur.getAttribute && (cur.getAttribute("onclick") || cur.getAttribute("data-action")))
    ) {
      return cur;
    }
    cur = cur.parentElement;
  }
  return node;
}

function textOf(node) {
  return String((node && (node.innerText || node.textContent || node.value)) || "").replace(/\s+/g, " ").trim();
}

function getAllNodes() {
  const nodes = [];
  const seen = new Set();
  const maxNodes = 25000;
  function collect(root) {
    if (!root || nodes.length >= maxNodes) return;
    try {
      const all = Array.from(root.querySelectorAll("*"));
      for (const n of all) {
        if (nodes.length >= maxNodes) break;
        if (!n || seen.has(n)) continue;
        seen.add(n);
        nodes.push(n);
        try {
          if (n.shadowRoot) collect(n.shadowRoot);
        } catch (e) {}
      }
    } catch (e) {}
    try {
      const frames = Array.from(root.querySelectorAll("iframe,frame"));
      for (const f of frames) {
        if (nodes.length >= maxNodes) break;
        try {
          if (f && f.contentDocument) collect(f.contentDocument);
        } catch (e) {}
      }
    } catch (e) {}
  }
  collect(document);
  return nodes;
}

function isVisible(node) {
  if (!node) return false;
  try {
    const style = window.getComputedStyle(node);
    if (style.visibility === "hidden" || style.display === "none" || style.opacity === "0") return false;
  } catch (e) {}
  if (node.offsetWidth === 0 && node.offsetHeight === 0) return false;
  return true;
}

function confirmButtonEnabled(allNodes) {
  for (const n of allNodes) {
    const upper = textOf(n).toUpperCase();
    if (!upper || !upper.includes("CONFIRM")) continue;
    if (!isVisible(n)) continue;
    if (n.disabled === true) continue;
    const ariaDisabled = String((n.getAttribute && n.getAttribute("aria-disabled")) || "").toLowerCase();
    if (ariaDisabled === "true") continue;
    const cls = String(n.className || "").toUpperCase();
    if (cls.includes("DISABLED")) continue;
    return true;
  }
  return false;
}

function hasQuestionSignal(el) {
  if (!el || !el.textContent) return false;
  const upper = String(el.textContent).toUpperCase();
  return questions.some(q => upper.includes(q));
}

function parseQuestionContext() {
  const lines = String(document.body.innerText || "").split(/[\r\n]+/).map(s => String(s || "").trim()).filter(Boolean);
  const result = [];
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i].toUpperCase();
    if (!line.includes("QUESTION")) {
      continue;
    }
    for (let j = i + 1; j < lines.length && j < i + 12; j++) {
      const candidate = String(lines[j]).trim();
      if (!candidate) continue;
      if (candidate.toUpperCase().includes("CHOOSE ONLY")) break;
      if (candidate.length > 160) continue;
      result.push(candidate);
      if (result.length >= 2) break;
    }
    if (result.length > 0) break;
  }
  return result.join(" ");
}

function answerHintsForContext(context) {
  const upperContext = String(context || "").toUpperCase();
  const ruleSets = [
    {
      keywords: ["PERSONALISATION", "RETAIL", "INDUSTRY"],
      hints: ["CUSTOM", "RECOMMENDATION", "RECOMMEND", "PRODUCT"],
    },
  ];
  for (const item of ruleSets) {
    const ok = item.keywords.every((k) => upperContext.includes(k));
    if (ok) return item.hints;
  }
  return [];
}

function scoreText(text, context) {
  const upperText = (text || "").toUpperCase();
  const qContext = String(context || "").toUpperCase();
  let score = 0;
  const hintTerms = qContext
    .replace(/[^A-Z0-9 ]/g, " ")
    .split(/\s+/)
    .filter(w => w.length > 2 && !questionStopWords.includes(w));
  if (hintTerms.length === 0) return 0;
  for (const token of hintTerms) {
    if (upperText.includes(token)) score += 1;
  }
  const strongHints = [
    "CUSTOM", "RECOMMEND", "PERSONAL", "ANALYZ", "AI", "AUTOM", "DATA", "IMAGE", "TEXT", "PROMPT",
  ];
  for (const hint of strongHints) {
    if (upperText.includes(hint)) score += 2;
  }
  return score;
}

const radioSelectors = 'input[type="radio"], input[type="checkbox"], [role="radio"], [role="option"]';
const questionContext = parseQuestionContext();
const knownAnswerHints = answerHintsForContext(questionContext);
const allNodes = getAllNodes();
const radios = allNodes.filter((n) => {
  try {
    return n.matches && n.matches(radioSelectors);
  } catch (e) {
    return false;
  }
});
if (radios.length > 0) {
  let bestRadio = null;
  let bestScore = -1;
  for (const r of radios) {
    const labelNode = document.querySelector(`[for="${r.id}"]`) || r.closest('label') || r.closest('[role="button"]');
    const text = String((labelNode && (labelNode.innerText || labelNode.textContent)) || r.value || "").toUpperCase();
    const visible = r.offsetParent !== null && !r.disabled;
    if (!visible) continue;
    if (knownAnswerHints.length > 0 && knownAnswerHints.some((h) => text.includes(h))) {
      bestRadio = r;
      bestScore = 999;
      break;
    }
    const optionScore = scoreText(text, questionContext);
    if (optionScore > bestScore) {
      bestScore = optionScore;
      bestRadio = r;
    }
    if (!r.checked) {
      if (!bestRadio) {
        bestRadio = r;
      }
    }
  }
  if (bestRadio) {
    try {
      if (forceClickNode(nearestClickable(bestRadio))) {
        if (confirmButtonEnabled(allNodes)) return true;
      }
    } catch (e) {}
  }
}

const candidates = [];
for (const node of allNodes) {
  if (!isVisible(node)) continue;
  const text = textOf(node);
  if (!text || text.length < 2 || text.length > 180) continue;
  const upper = text.toUpperCase();
  if (!hasQuestionSignal(document.body)) continue;
  if (upper.includes("CONFIRM") || upper.includes("NEXT QUESTION")) continue;
  const looksLikeOption = optionLeadRegex.test(upper) || knownAnswerHints.some((h) => upper.includes(h));
  if (!looksLikeOption) continue;
  const score = scoreText(upper, questionContext) + (optionLeadRegex.test(upper) ? 2 : 0);
  candidates.push({node, score});
}
candidates.sort((a, b) => b.score - a.score);

for (const item of candidates.slice(0, 18)) {
  const n = item.node;
  try {
    n.scrollIntoView({block: "center", inline: "center"});
  } catch (e) {}
  if (!forceClickNode(nearestClickable(n))) continue;
  if (confirmButtonEnabled(allNodes)) return true;
}

for (const item of candidates.slice(0, 18)) {
  const n = item.node;
  if (!forceClickNode(n)) continue;
  if (confirmButtonEnabled(allNodes)) return true;
}

return candidates.length > 0;
"""
    try:
        selected = bool(driver.execute_script(js))
        if selected:
            logger.write("[ok] selected a quiz option candidate")
            return True
    except Exception as exc:
        logger.write(f"[warn] quiz answer selector failed: {exc}")
    return False


def pick_question_answer_precise(driver, logger: RunLogger) -> bool:
    page_upper = safe_page_text(driver, logger)
    page_upper = (
        page_upper.replace("‑", "-")
        .replace("–", "-")
        .replace("—", "-")
        .replace("’", "'")
    )
    targets: list[str] = []
    if "WHAT IS AI PRIMARILY DEFINED AS" in page_upper:
        targets = [
            "A TECHNIQUE THAT ENABLES COMPUTERS TO MIMIC HUMAN INTELLIGENCE",
            "SIMULATION OF HUMAN INTELLIGENCE",
            "TASKS THAT NORMALLY REQUIRE HUMAN INTELLIGENCE",
            "MACHINES PERFORMING TASKS THAT REQUIRE HUMAN INTELLIGENCE",
        ]
    elif "SUBSET OF AI THAT FOCUSES ON CREATING NEW CONTENT" in page_upper:
        targets = [
            "GENERATIVE AI",
            "A TYPE OF AI THAT CREATES NEW CONTENT",
        ]
    elif "MAIN PURPOSE OF SUPERVISED LEARNING" in page_upper:
        targets = [
            "TO PREDICT OUTCOMES BASED ON INPUT DATA WITH KNOWN ANSWERS",
            "LEARN FROM LABELED DATA",
            "PREDICT OUTCOMES FROM LABELED DATA",
            "TRAIN ON LABELED DATA",
        ]
    elif "APPLICATIONS OF AI IN PERSONALISATION" in page_upper and "RETAIL" in page_upper:
        targets = ["CUSTOMISED PRODUCT RECOMMENDATIONS", "CUSTOMIZED PRODUCT RECOMMENDATIONS"]
    elif "BENEFIT OF USING AI FOR INCLUSIVITY IN CUSTOMER SERVICE" in page_upper:
        targets = ["SUPPORTING USERS IN MULTIPLE LANGUAGES"]
    elif "COMMON CHALLENGE ASSOCIATED WITH AI" in page_upper and "DECISION-MAKING TRANSPARENCY" in page_upper:
        targets = ["LACK OF TRANSPARENCY AND EXPLAINABILITY"]
    elif (
        "CREATING AN ENGAGING BLOG POST ON SUSTAINABLE TRAVEL" in page_upper
        and "WHICH PROMPT WOULD BE THE MOST EFFECTIVE" in page_upper
    ):
        targets = [
            "CREATE A BLOG POST ON ECO-FRIENDLY TRAVEL FOR UNIVERSITY STUDENTS, WITH COST-SAVING TIPS AND DESTINATION RECOMMENDATIONS",
        ]
    elif (
        "CREATING AN ENGAGING BLOG POST ON SUSTAINABLE TRAVEL" in page_upper
        and "OUTPUT IS TOO GENERIC" in page_upper
        and "LACKS PRACTICAL RECOMMENDATIONS" in page_upper
    ):
        targets = [
            "PROVIDE SPECIFIC TRAVEL TIPS, COST-SAVING STRATEGIES, AND RECOMMENDED DESTINATIONS FOR STUDENTS",
        ]
    elif (
        "WRITING A VIDEO SCRIPT ON RENEWABLE ENERGY" in page_upper
        and "MORE LIKELY TO PRODUCE THE BEST RESULTS" in page_upper
    ):
        targets = [
            "DRAFT A SCRIPT FOR AN EDUCATIONAL VIDEO ON RENEWABLE ENERGY, INCLUDING PRACTICAL EXAMPLES OF HOW ALTERNATIVE ENERGY SOURCES AND HOW THEY FUNCTION",
        ]
    elif (
        "WRITING A VIDEO SCRIPT ON RENEWABLE ENERGY" in page_upper
        and "TOO TECHNICAL FOR STUDENTS TO UNDERSTAND" in page_upper
    ):
        targets = [
            "SIMPLIFY THE LANGUAGE AND USE RELATABLE EXAMPLES FOR STUDENTS",
        ]
    elif (
        "DRAFTING A SOCIAL MEDIA CAMPAIGN" in page_upper
        and "LEAST EFFECTIVE" in page_upper
    ):
        targets = [
            "LIST KEY TIPS ABOUT SUSTAINABLE LIVING AND WHY IT IS IMPORTANT",
        ]
    elif (
        "DRAFT A RESEARCH REPORT ABOUT THE IMPACT OF AI ON WORKFORCE PRODUCTIVITY IN THE TECH INDUSTRY" in page_upper
        and "LEAST EFFECTIVE" in page_upper
    ):
        targets = [
            "EXPLAIN HOW AI IS USED IN THE TECH INDUSTRY WITH KEY EXAMPLES",
        ]
    elif "KEY ETHICAL CONCERN WHEN USING AI IN ACADEMIC SETTINGS" in page_upper:
        targets = [
            "PLAGIARISM AND MISREPRESENTATION OF WORK",
        ]
    elif (
        "LEVEL OF AI USE IS CHARACTERISED BY CLEAR VIOLATIONS OF ACADEMIC INTEGRITY" in page_upper
        or "LEVEL OF AI USE IS CHARACTERIZED BY CLEAR VIOLATIONS OF ACADEMIC INTEGRITY" in page_upper
    ):
        targets = [
            "LEVEL 1: PROHIBITED AI USE",
        ]
    elif "WHAT DOES THE 'E' IN THE LEAD FRAMEWORK STAND FOR" in page_upper:
        targets = [
            "ETHICAL & TRANSPARENT",
            "ETHICAL AND TRANSPARENT",
        ]
    elif "BEST PRACTICE FOR ENSURING HONESTY IN ACADEMIC WORK WHEN USING AI" in page_upper:
        targets = [
            "ACKNOWLEDGE THE USE OF AI WHERE REQUIRED BY ACADEMIC POLICIES",
        ]
    elif "WHY IS IT IMPORTANT TO VERIFY AI-GENERATED CONTENT BEFORE USING IT" in page_upper:
        targets = [
            "AI-GENERATED CONTENT MAY CONTAIN MISINFORMATION OR INACCURACIES",
        ]
    elif "MAIN DIFFERENCE BETWEEN AI-DEPENDENT AND AI-AUGMENTED PROFESSIONALS" in page_upper:
        targets = [
            "AI-DEPENDENT PROFESSIONALS LET AI TAKE OVER THEIR WORK WITHOUT CRITICAL OVERSIGHT",
        ]
    elif "KEY SKILL FOR THRIVING IN AN AI-DRIVEN WORKFORCE" in page_upper:
        targets = [
            "AI LITERACY AND CRITICAL THINKING",
        ]
    elif "HOW DO AI-AUGMENTED PROFESSIONALS UTILISE AI IN THEIR WORKFLOWS" in page_upper:
        targets = [
            "THEY INTEGRATE AI TO ENHANCE THEIR CAPABILITIES WHILE MAINTAINING HUMAN CREATIVITY",
        ]

    if not targets:
        return False

    js = r"""
const phrases = arguments[0].map(s => String(s).toUpperCase());
const selectors = "li,button,div,label,span,p,[role='radio'],[role='option']";

function textOf(node) {
  return String((node && (node.innerText || node.textContent || node.value)) || "").replace(/\s+/g, " ").trim();
}
function isVisible(node) {
  if (!node) return false;
  try {
    const style = window.getComputedStyle(node);
    if (style.visibility === "hidden" || style.display === "none" || style.opacity === "0") return false;
  } catch (e) {}
  if (node.offsetWidth === 0 && node.offsetHeight === 0) return false;
  return true;
}
function isSidebarNode(node) {
  let cur = node;
  for (let i = 0; i < 8 && cur; i++) {
    const role = String((cur.getAttribute && cur.getAttribute("role")) || "").toUpperCase();
    const tag = String(cur.tagName || "").toUpperCase();
    const cls = String(cur.className || "").toUpperCase();
    if (
      role === "NAVIGATION" ||
      tag === "NAV" ||
      cls.includes("SIDEBAR") ||
      cls.includes("LESSON") ||
      cls.includes("MODULE") ||
      cls.includes("MENU")
    ) {
      return true;
    }
    cur = cur.parentElement;
  }
  return false;
}
function nearestClickable(node) {
  let cur = node;
  for (let i = 0; i < 6 && cur; i++) {
    const tag = String((cur.tagName || "").toUpperCase());
    const role = String((cur.getAttribute && cur.getAttribute("role")) || "").toUpperCase();
    if (
      tag === "BUTTON" || tag === "A" || tag === "LABEL" || tag === "INPUT" || tag === "LI" ||
      role === "BUTTON" || role === "RADIO" || role === "OPTION" || role === "CHECKBOX"
    ) {
      return cur;
    }
    cur = cur.parentElement;
  }
  return node;
}
function forceClick(node) {
  try { node.scrollIntoView({block: "center", inline: "center"}); } catch (e) {}
  try { node.focus(); } catch (e) {}
  try { node.click(); return true; } catch (e) {}
  try {
    const evt = new MouseEvent("click", {bubbles: true, cancelable: true, view: window});
    node.dispatchEvent(evt);
    return true;
  } catch (e) {}
  return false;
}

let best = null;
let bestScore = -999;
for (const node of Array.from(document.querySelectorAll(selectors))) {
  if (!isVisible(node)) continue;
  if (isSidebarNode(node)) continue;
  const rect = node.getBoundingClientRect();
  if ((rect.left + (rect.width / 2)) < Math.max(360, window.innerWidth * 0.32)) continue;
  const upper = textOf(node).toUpperCase();
  if (!upper || upper.length > 200) continue;
  const phrase = phrases.find((p) => upper.includes(p));
  if (!phrase) continue;
  let score = 0;
  if (upper === phrase) score += 20;
  if (upper.startsWith(phrase)) score += 12;
  if (upper.includes(phrase)) score += 8;
  if (String(node.tagName || "").toUpperCase() === "LABEL") score += 4;
  if (String((node.getAttribute && node.getAttribute("role")) || "").toUpperCase() === "RADIO") score += 4;
  if (score > bestScore) {
    bestScore = score;
    best = node;
  }
}
if (!best) return false;
return forceClick(nearestClickable(best));
"""
    try:
        selected = bool(driver.execute_script(js, targets))
        if selected:
            logger.write("[ok] selected quiz option by precise question mapping")
            return True
    except Exception as exc:
        logger.write(f"[warn] precise quiz selector failed: {exc}")
    return False


def pick_question_answer_reasoned(driver, logger: RunLogger) -> bool:
    js = r"""
function upper(s) {
  return String(s || "").toUpperCase();
}
function isVisible(node) {
  if (!node) return false;
  try {
    const style = window.getComputedStyle(node);
    if (style.visibility === "hidden" || style.display === "none" || style.opacity === "0") return false;
  } catch (e) {}
  if (node.offsetWidth === 0 && node.offsetHeight === 0) return false;
  return true;
}
function isSidebar(node) {
  let cur = node;
  for (let i = 0; i < 8 && cur; i++) {
    const role = upper(cur.getAttribute && cur.getAttribute("role"));
    const tag = upper(cur.tagName || "");
    const cls = upper(cur.className || "");
    if (
      role === "NAVIGATION" ||
      tag === "NAV" ||
      cls.includes("SIDEBAR") ||
      cls.includes("LESSON") ||
      cls.includes("MODULE") ||
      cls.includes("MENU")
    ) return true;
    cur = cur.parentElement;
  }
  return false;
}
function nearestClickable(node) {
  let cur = node;
  for (let i = 0; i < 6 && cur; i++) {
    const tag = upper(cur.tagName || "");
    const role = upper((cur.getAttribute && cur.getAttribute("role")) || "");
    if (
      tag === "BUTTON" || tag === "A" || tag === "LABEL" || tag === "INPUT" || tag === "LI" ||
      role === "BUTTON" || role === "RADIO" || role === "OPTION" || role === "CHECKBOX"
    ) return cur;
    cur = cur.parentElement;
  }
  return node;
}
function clickNode(node) {
  try { node.scrollIntoView({block: "center", inline: "center"}); } catch (e) {}
  try { node.focus(); } catch (e) {}
  try { node.click(); return true; } catch (e) {}
  try {
    const evt = new MouseEvent("click", {bubbles: true, cancelable: true, view: window});
    node.dispatchEvent(evt);
    return true;
  } catch (e) {}
  return false;
}

const pageText = upper((document.body && document.body.innerText) || "");
const leastMode = pageText.includes("LEAST EFFECTIVE") || pageText.includes("LEAST APPROPRIATE") || pageText.includes("LEAST HELPFUL");
const bestMode = pageText.includes("MOST EFFECTIVE") || pageText.includes("BEST") || pageText.includes("MOST APPROPRIATE");

const selectors = "li,button,div,label,span,[role='radio'],[role='option']";
const options = [];
for (const node of Array.from(document.querySelectorAll(selectors))) {
  if (!isVisible(node)) continue;
  if (isSidebar(node)) continue;
  const rect = node.getBoundingClientRect();
  if ((rect.left + (rect.width / 2)) < Math.max(360, window.innerWidth * 0.32)) continue;
  const txt = String((node.innerText || node.textContent || "")).replace(/\s+/g, " ").trim();
  const t = upper(txt);
  if (!t || t.length < 6 || t.length > 450) continue;
  if (!/^[A-E]\b/.test(t)) continue;
  options.push({node, text: t});
}
if (options.length === 0) return false;

const questionKey = (() => {
  const lines = pageText.split(/\n+/).map(s => String(s || "").trim()).filter(Boolean);
  for (let i = 0; i < lines.length; i++) {
    if (lines[i].includes("QUESTION ") && lines[i].includes(" OF ")) {
      const chunk = [];
      for (let j = i + 1; j < Math.min(lines.length, i + 12); j++) {
        const cur = lines[j];
        if (cur.includes("CHOOSE ONLY") || cur.includes("KNOWLEDGE CHECK")) break;
        if (cur.length < 4) continue;
        chunk.push(cur);
        if (chunk.length >= 2) break;
      }
      return chunk.join(" ").slice(0, 180);
    }
  }
  return pageText.slice(0, 180);
})();
if (!window.__oc_question_attempts) window.__oc_question_attempts = {};
const priorAttempts = Number(window.__oc_question_attempts[questionKey] || 0);
window.__oc_question_attempts[questionKey] = priorAttempts + 1;

function specificityScore(t) {
  let score = 0;
  const words = t.split(/\s+/).filter(Boolean).length;
  score += Math.min(words, 60) * 0.6;
  if (/\b\d+\b/.test(t)) score += 3;
  const strong = [
    "STUDENT", "YOUNG ADULT", "AUDIENCE", "FORMAT", "STRUCTURE", "STEP-BY-STEP",
    "INCLUDE", "EXAMPLE", "EVIDENCE", "SOURCE", "TONE", "WORD", "LENGTH",
    "BLOG", "SCRIPT", "REPORT", "BULLET", "SECTIONS", "ACTIONABLE", "CLEAR",
  ];
  for (const k of strong) {
    if (t.includes(k)) score += 1.6;
  }
  const weak = [
    "WRITE SOMETHING", "ANYTHING", "GENERAL", "WHATEVER", "RANDOM", "JUST WRITE",
    "WITHOUT DETAILS", "NO NEED", "DONT CARE", "ABOUT AI", "ABOUT THIS TOPIC",
  ];
  for (const k of weak) {
    if (t.includes(k)) score -= 5;
  }
  return score;
}

const ranked = options.map((opt) => ({...opt, score: specificityScore(opt.text)}));
if (leastMode) {
  ranked.sort((a, b) => a.score - b.score);
} else {
  ranked.sort((a, b) => b.score - a.score);
}
const pickIndex = Math.min(priorAttempts, Math.max(0, ranked.length - 1));
const best = ranked[pickIndex] || ranked[0] || null;
if (!best) return false;
return clickNode(nearestClickable(best.node));
"""
    try:
        selected = bool(driver.execute_script(js))
        if selected:
            logger.write("[ok] selected quiz option by reasoned heuristic")
            return True
    except Exception as exc:
        logger.write(f"[warn] reasoned quiz selector failed: {exc}")
    return False


def pick_alternate_question_answer(driver, logger: RunLogger) -> bool:
    js = r"""
const selectors = "li,button,div,label,span,[role='radio'],[role='option'],input[type='radio']";

function isVisible(node) {
  if (!node) return false;
  try {
    const style = window.getComputedStyle(node);
    if (style.visibility === "hidden" || style.display === "none" || style.opacity === "0") return false;
  } catch (e) {}
  if (node.offsetWidth === 0 && node.offsetHeight === 0) return false;
  return true;
}
function isSidebar(node) {
  let cur = node;
  for (let i = 0; i < 8 && cur; i++) {
    const role = String((cur.getAttribute && cur.getAttribute("role")) || "").toUpperCase();
    const tag = String(cur.tagName || "").toUpperCase();
    const cls = String(cur.className || "").toUpperCase();
    if (
      role === "NAVIGATION" ||
      tag === "NAV" ||
      cls.includes("SIDEBAR") ||
      cls.includes("LESSON") ||
      cls.includes("MODULE") ||
      cls.includes("MENU")
    ) return true;
    cur = cur.parentElement;
  }
  return false;
}
function isSelected(node) {
  const ariaChecked = String((node.getAttribute && node.getAttribute("aria-checked")) || "").toLowerCase();
  const ariaSelected = String((node.getAttribute && node.getAttribute("aria-selected")) || "").toLowerCase();
  if (ariaChecked === "true" || ariaSelected === "true") return true;
  if (String(node.tagName || "").toUpperCase() === "INPUT") {
    try { if (node.checked) return true; } catch (e) {}
  }
  const cls = String(node.className || "").toUpperCase();
  if (cls.includes("SELECTED") || cls.includes("ACTIVE")) return true;
  return false;
}
function isIncorrect(node) {
  const text = String((node.innerText || node.textContent || "")).toUpperCase();
  const cls = String(node.className || "").toUpperCase();
  return (
    cls.includes("INCORRECT") ||
    cls.includes("WRONG") ||
    text.includes("THIS ANSWER IS INCORRECT")
  );
}
function textOf(node) {
  return String((node && (node.innerText || node.textContent || node.value)) || "").replace(/\s+/g, " ").trim();
}
function nearestClickable(node) {
  let cur = node;
  for (let i = 0; i < 6 && cur; i++) {
    const tag = String((cur.tagName || "").toUpperCase());
    const role = String((cur.getAttribute && cur.getAttribute("role")) || "").toUpperCase();
    if (
      tag === "BUTTON" || tag === "A" || tag === "LABEL" || tag === "INPUT" || tag === "LI" ||
      role === "BUTTON" || role === "RADIO" || role === "OPTION" || role === "CHECKBOX"
    ) return cur;
    cur = cur.parentElement;
  }
  return node;
}
function clickNode(node) {
  try { node.scrollIntoView({block: "center", inline: "center"}); } catch (e) {}
  try { node.focus(); } catch (e) {}
  try { node.click(); return true; } catch (e) {}
  try {
    const evt = new MouseEvent("click", {bubbles: true, cancelable: true, view: window});
    node.dispatchEvent(evt);
    return true;
  } catch (e) {}
  return false;
}

let candidates = [];
for (const node of Array.from(document.querySelectorAll(selectors))) {
  if (!isVisible(node)) continue;
  if (isSidebar(node)) continue;
  const rect = node.getBoundingClientRect();
  if ((rect.left + (rect.width / 2)) < Math.max(360, window.innerWidth * 0.32)) continue;
  const txt = textOf(node).toUpperCase();
  if (!txt || txt.length < 2 || txt.length > 220) continue;
  if (!(txt.match(/^[A-E]\b/) || txt.includes("RECOMMEND") || txt.includes("LEARN") || txt.includes("TRANSPARENC") || txt.includes("EXPLAIN"))) continue;
  if (isIncorrect(node)) continue;
  const selected = isSelected(node) ? 1 : 0;
  candidates.push({node, selected});
}

candidates.sort((a, b) => a.selected - b.selected);
for (const item of candidates) {
  if (item.selected === 1) continue;
  if (clickNode(nearestClickable(item.node))) return true;
}
return false;
"""
    try:
        selected = bool(driver.execute_script(js))
        if selected:
            logger.write("[ok] selected alternate quiz option candidate")
            return True
    except Exception as exc:
        logger.write(f"[warn] alternate quiz selector failed: {exc}")
    return False


def take_action_from_snapshot(
    driver,
    by,
    action_xpath: Iterable[str],
    action_tokens: Iterable[str],
    fallback_tokens: Iterable[str],
    screenshot_dir: Path,
    logger: RunLogger,
    step: int,
    adaptive_level: int = 0,
    disable_precise_for: Optional[Set[str]] = None,
) -> bool:
    page_upper = safe_page_text(driver, logger)
    state = detect_course_state(page_upper)
    logger.write(f"[info] course-state={state} step={step}")

    if state == "reflective_question":
        clicked_skip = click_text_main_pane_via_js(
            driver,
            ["SKIP QUESTION"],
            f"reflective-skip(main-pane-js)-{step}",
            logger,
        )
        if clicked_skip:
            time.sleep(0.5)
        clicked_confirm = click_text_main_pane_via_js(
            driver,
            ["CONFIRM", "SUBMIT"],
            f"reflective-confirm(main-pane-js)-{step}",
            logger,
        )
        if clicked_confirm:
            return True
        return click_text_main_pane_via_js(
            driver,
            ["CONTINUE", "NEXT"],
            f"reflective-continue(main-pane-js)-{step}",
            logger,
        )

    if state == "portal_products":
        clicked_dash = click_text_main_pane_via_js(
            driver,
            ["MY DASHBOARD", "DASHBOARD"],
            f"portal-back-dashboard(main-pane-js)-{step}",
            logger,
        )
        if clicked_dash:
            return True
        return click_text_via_js(
            driver,
            ["MY DASHBOARD", "DASHBOARD"],
            f"portal-back-dashboard(js)-{step}",
            logger,
        )

    if state == "survey_completed":
        return click_text_main_pane_via_js(
            driver,
            ["CONTINUE", "NEXT"],
            f"survey-continue(main-pane-js)-{step}",
            logger,
        )

    if state == "knowledge_check_failed":
        return click_text_main_pane_via_js(
            driver,
            ["RETAKE QUIZ"],
            f"retake-quiz(main-pane-js)-{step}",
            logger,
        )

    if state == "knowledge_check_passed":
        return click_text_main_pane_via_js(
            driver,
            ["CONTINUE", "NEXT", "MARK AS COMPLETE"],
            f"passed-continue(main-pane-js)-{step}",
            logger,
        )

    if state == "knowledge_check_entry":
        return click_text_main_pane_via_js(
            driver,
            ["START QUIZ", "TAKE QUIZ", "BEGIN QUIZ", "KNOWLEDGE CHECK"],
            f"knowledge-check-entry(main-pane-js)-{step}",
            logger,
        )

    if state == "knowledge_check_feedback":
        if "THIS ANSWER IS INCORRECT" in page_upper:
            reselection = pick_alternate_question_answer(driver, logger)
            if reselection:
                clicked_reconfirm = click_text_main_pane_via_js(
                    driver,
                    ["CONFIRM", "SUBMIT", "CHECK ANSWER"],
                    f"knowledge-check-reconfirm(main-pane-js)-{step}",
                    logger,
                )
                if clicked_reconfirm:
                    return True
        return click_text_main_pane_via_js(
            driver,
            ["NEXT", "CONTINUE"],
            f"knowledge-check-feedback(main-pane-js)-{step}",
            logger,
        )

    if state in {"reflective_prompt", "video_or_reading"}:
        clicked = click_text_main_pane_via_js(
            driver,
            ["CONTINUE", "MARK AS COMPLETE", "NEXT", "START", "RESUME"],
            f"prompt-progress(main-pane-js)-{step}",
            logger,
        )
        if clicked:
            return True

    selected = False
    if state == "knowledge_check_question":
        prompt = extract_question_prompt(page_upper)
        if prompt:
            logger.write(f"[info] question-prompt={prompt}")
        prompt_key = normalize_question_key(prompt)
        precise_disabled = bool(prompt_key and disable_precise_for and prompt_key in disable_precise_for)
        if precise_disabled:
            logger.write("[self-heal] precise mapping disabled for repeated-stall question")
        if not precise_disabled and adaptive_level < 2:
            selected = pick_question_answer_precise(driver, logger)
        if not selected:
            selected = pick_question_answer_reasoned(driver, logger)
        if not selected and adaptive_level >= 1:
            selected = pick_alternate_question_answer(driver, logger)
        if not selected:
            selected = pick_question_answer(driver, logger)
    if selected:
        clicked_confirm = click_text_main_pane_via_js(
            driver,
            ["CONFIRM", "SUBMIT", "NEXT QUESTION", "CHECK ANSWER"],
            f"quiz-confirm(main-pane-js)-{step}",
            logger,
        )
        if clicked_confirm:
            return True
        confirm_xpath = [
            "//button[contains(translate(normalize-space(.),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'CONFIRM')]",
            "//a[contains(translate(normalize-space(.),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'CONFIRM')]",
            "//*[@role='button' and contains(translate(normalize-space(.),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'CONFIRM')]",
            "//*[contains(translate(normalize-space(.),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'CONFIRM')]",
            "//button[contains(translate(normalize-space(.),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'SUBMIT')]",
            "//a[contains(translate(normalize-space(.),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'SUBMIT')]",
            "//button[contains(translate(normalize-space(.),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'NEXT QUESTION')]",
            "//a[contains(translate(normalize-space(.),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'NEXT QUESTION')]",
        ]
        clicked_confirm = click_first_wait(driver, by, confirm_xpath, f"quiz-confirm(xpath)-{step}", 2, logger)
        if not clicked_confirm:
            clicked_confirm = click_text_via_js(
                driver,
                ["CONFIRM", "SUBMIT", "NEXT QUESTION", "CHECK ANSWER"],
                f"quiz-confirm(js)-{step}",
                logger,
            )
        if clicked_confirm:
            return True
        if state == "knowledge_check_question":
            return False
    clicked = click_text_main_pane_via_js(
        driver,
        action_tokens,
        f"course-action(main-pane-js)-{step}",
        logger,
    )
    if clicked:
        return True
    clicked = click_first_wait(driver, by, action_xpath, f"course-action(xpath)-{step}", 3, logger)
    if clicked:
        return True
    clicked = click_text_via_js(
        driver,
        action_tokens,
        f"course-action(js)-{step}",
        logger,
    )
    if clicked:
        return True
    return click_text_via_js(
        driver,
        fallback_tokens,
        f"course-action-fallback(js)-{step}",
        logger,
    )


def extract_question_marker(page_text: str) -> str:
    match = re.search(r"QUESTION\s+(\d+)\s+OF\s+(\d+)", page_text)
    if not match:
        return ""
    return f"{match.group(1)}/{match.group(2)}"


def detect_course_state(page_upper: str) -> str:
    if "PRODUCTS" in page_upper and "NO RESULTS WERE FOUND" in page_upper:
        return "portal_products"
    if "REFLECTIVE PROMPT" in page_upper and "SKIP QUESTION" in page_upper:
        return "reflective_question"
    if "FAILED THIS QUIZ" in page_upper and "RETAKE QUIZ" in page_upper:
        return "knowledge_check_failed"
    if "PASSED THIS QUIZ" in page_upper and "SCORE" in page_upper:
        return "knowledge_check_passed"
    if "THIS ANSWER IS INCORRECT" in page_upper or "THIS ANSWER IS CORRECT" in page_upper:
        return "knowledge_check_feedback"
    if "QUESTION " in page_upper and " OF " in page_upper and "KNOWLEDGE CHECK" in page_upper:
        return "knowledge_check_question"
    if "SURVEY COMPLETED" in page_upper:
        return "survey_completed"
    if "KNOWLEDGE CHECK" in page_upper and (
        "START QUIZ" in page_upper or "TAKE QUIZ" in page_upper or "BEGIN QUIZ" in page_upper
    ):
        return "knowledge_check_entry"
    if "REFLECTIVE PROMPT" in page_upper:
        return "reflective_prompt"
    if "VIDEO" in page_upper and "MIN" in page_upper:
        return "video_or_reading"
    return "generic"


def extract_question_prompt(page_upper: str) -> str:
    lines = [ln.strip() for ln in page_upper.splitlines() if ln.strip()]
    if not lines:
        return ""
    for idx, ln in enumerate(lines):
        if "QUESTION " in ln and " OF " in ln:
            collected: list[str] = []
            for j in range(idx + 1, min(len(lines), idx + 12)):
                cur = lines[j]
                if "CHOOSE ONLY" in cur or "KNOWLEDGE CHECK" in cur:
                    break
                if len(cur) < 3:
                    continue
                collected.append(cur)
                if len(collected) >= 3:
                    break
            return " ".join(collected)[:220]
    return ""


def normalize_question_key(prompt: str) -> str:
    key = (
        (prompt or "")
        .replace("‑", "-")
        .replace("–", "-")
        .replace("—", "-")
        .replace("’", "'")
        .strip()
        .upper()
    )
    key = re.sub(r"\s+", " ", key)
    return key[:220]


def has_completion_marker(page_text: str) -> bool:
    return any(
        token in page_text
        for token in [
            "YOU HAVE COMPLETED",
            "COURSE COMPLETED",
            "COURSE COMPLETION",
            "CONGRATULATIONS",
            "CERTIFICATE",
            "THANK YOU FOR COMPLETING",
        ]
    )


def page_signature(driver, logger: RunLogger) -> str:
    try:
        page_source = driver.page_source or ""
    except Exception as exc:
        logger.write(f"[warn] failed reading page source for progress tracking: {exc}")
        page_source = ""
    try:
        title = driver.title or ""
    except Exception:
        title = ""
    try:
        url = driver.current_url or ""
    except Exception:
        url = ""
    snippet = page_source[:800].replace("\n", " ")
    return f"{title}|{url}|{len(page_source)}|{snippet}"


def looks_like_logged_in(driver, by, selectors: Iterable[str], logger: RunLogger) -> bool:
    hints = [
        "SIGN OUT",
        "LOG OUT",
        "MY COURSES",
        "DASHBOARD",
        "COURSES",
    ]
    try:
        page_upper = (driver.page_source or "").upper()
    except Exception:
        page_upper = ""
    if any(token in page_upper for token in hints):
        logger.write("[info] detected dashboard/login-session context from page text")
        return True
    login_hint = any(
        token in page_upper
        for token in ["LOG IN", "LOGIN", "SIGN IN", "USERNAME", "PASSWORD"]
    )
    if login_hint:
        logger.write("[info] detected login prompt by page text")
        return False
    element, _ = find_in_default_and_frames(driver, by, selectors)
    if element is not None:
        logger.write("[info] visible username field detected; login flow still needed")
        return False
    logger.write("[info] no visible username field and no explicit login text; assuming signed-in session")
    return True


def safe_page_text(driver, logger: RunLogger) -> str:
    try:
        text = driver.execute_script("return (document && document.body && document.body.innerText) ? document.body.innerText : ''")
        if isinstance(text, str) and text.strip():
            return text.upper()
    except Exception:
        pass
    try:
        return (driver.page_source or "").upper()
    except Exception as exc:
        logger.write(f"[warn] failed reading page text/source: {exc}")
        return ""


def is_session_dead_error(exc: Exception) -> bool:
    message = str(exc).lower()
    return any(token in message for token in ["invalid session id", "no such window", "target window already closed"])


def cleanup_profile_locks(profile_dir: Path, logger: RunLogger) -> None:
    if not profile_dir.exists():
        return
    lock_names = {"SingletonLock", "SingletonCookie", "SingletonSocket", "SingletonService"}
    for lock_name in lock_names:
        for path in profile_dir.rglob(lock_name):
            try:
                if path.is_file():
                    path.unlink()
                    logger.write(f"[warn] removed stale chrome lock {path}")
            except Exception as exc:
                logger.write(f"[warn] failed remove lock {path}: {exc}")


def resolve_config(args: argparse.Namespace) -> Dict[str, str]:
    env: Dict[str, str] = {}
    env_file = Path(args.env_file).expanduser() if args.env_file else None
    if env_file is not None:
        env = parse_env_file(env_file)
    return {
        "url": args.url or env.get("DEC_LOGIN_URL", ""),
        "username": args.username or env.get("DEC_USERNAME", ""),
        "password": args.password or env.get("DEC_PASSWORD", ""),
        "subject_filter": args.mail_subject_contains or env.get("DEC_MAIL_SUBJECT_CONTAINS", ""),
        "sender_filter": args.mail_sender_contains or env.get("DEC_MAIL_SENDER_CONTAINS", ""),
    }


def hold_session(seconds: int, logger: RunLogger) -> None:
    if seconds > 0:
        logger.write(f"[info] holding browser for {seconds}s")
        time.sleep(seconds)
        return
    logger.write("[info] browser is open. Finish login / verification manually.")
    logger.write("[info] press Ctrl+C in this terminal when done.")
    while True:
        time.sleep(2)


def is_driver_alive(driver, logger: RunLogger) -> bool:
    try:
        driver.current_url
        driver.title
        return True
    except Exception as exc:
        logger.write(f"[warn] webdriver session check failed: {exc}")
        return False


def build_chrome_driver(
    webdriver,
    logger: RunLogger,
    options,
    args,
    profile_dir: Path,
) -> object:
    def make_fallback_options() -> object:
        cloned = webdriver.ChromeOptions()
        for arg in getattr(options, "arguments", []):
            if str(arg).startswith("--user-data-dir="):
                continue
            if str(arg).startswith("--profile-directory="):
                continue
            cloned.add_argument(arg)
        alt_profile = profile_dir.parent / f"chrome_profile_fallback_{int(time.time())}"
        alt_profile.mkdir(parents=True, exist_ok=True)
        cloned.add_argument(f"--user-data-dir={alt_profile}")
        cloned.add_argument("--profile-directory=Default")
        logger.write(f"[warn] using fallback chrome profile: {alt_profile}")
        return cloned

    driver = None
    try:
        driver = webdriver.Chrome(options=options)
    except Exception as exc:
        message = str(exc).lower()
        if not args.fresh_profile and "session not created" in message:
            cleanup_profile_locks(profile_dir, logger)
            try:
                logger.write("[warn] retrying Chrome start after cleaning stale profile locks")
                driver = webdriver.Chrome(options=options)
            except Exception:
                pass
        if driver is not None:
            logger.write("[info] chrome driver start recovered after lock cleanup")
            return driver

        needs_fallback = "session not created" in message or "chromedriver" in message
        if not needs_fallback:
            raise

        try:
            from selenium.webdriver.chrome.service import Service as ChromeService
            from webdriver_manager.chrome import ChromeDriverManager

            logger.write("[warn] default chromedriver failed; trying webdriver-manager fallback")
            driver_binary = ChromeDriverManager().install()
            service = ChromeService(driver_binary)
            try:
                return webdriver.Chrome(service=service, options=options)
            except Exception as inner:
                logger.write(f"[warn] webdriver-manager launch with persistent profile failed: {inner}")
                fallback_options = make_fallback_options()
                return webdriver.Chrome(service=service, options=fallback_options)
        except Exception as inner:
            logger.write(f"[error] webdriver-manager fallback failed: {inner}")
            raise

    return driver


def make_run_paths(args: argparse.Namespace) -> Tuple[Path, Path]:
    script_dir = Path(__file__).resolve().parent
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    if args.screenshot_dir:
        screenshot_dir = Path(args.screenshot_dir).expanduser().resolve()
    else:
        screenshot_dir = (script_dir / "sessions" / stamp).resolve()
    screenshot_dir.mkdir(parents=True, exist_ok=True)
    if args.log_file:
        log_file = Path(args.log_file).expanduser().resolve()
    else:
        log_file = screenshot_dir / "bootstrap.log"
    return screenshot_dir, log_file


def take_shot(driver, screenshot_dir: Path, name: str, logger: RunLogger) -> Path:
    stamp = datetime.now().strftime("%H%M%S")
    path = screenshot_dir / f"{stamp}_{name}.png"
    try:
        driver.save_screenshot(str(path))
        logger.write(f"[shot] {path}")
    except Exception as exc:
        logger.write(f"[warn] screenshot failed ({name}): {exc}")
    return path


def fetch_mail_text(subject_filter: str, sender_filter: str) -> str:
    script = r'''
on run argv
  set subjectNeed to item 1 of argv
  set senderNeed to item 2 of argv
  set outText to ""
  tell application "Mail"
    set msgList to messages of inbox
    set msgCount to count msgList
    if msgCount > 40 then set msgCount to 40
    repeat with i from 1 to msgCount
      set m to item i of msgList
      try
        set s to subject of m as text
      on error
        set s to ""
      end try
      try
        set snd to sender of m as text
      on error
        set snd to ""
      end try
      if (subjectNeed is "" or s contains subjectNeed) and (senderNeed is "" or snd contains senderNeed) then
        try
          set c to content of m as text
        on error
          set c to ""
        end try
        set outText to outText & return & "###MSG###" & return & s & return & snd & return & c
      end if
    end repeat
  end tell
  return outText
end run
'''.strip()
    proc = subprocess.run(
        ["osascript", "-", subject_filter, sender_filter],
        input=script,
        text=True,
        capture_output=True,
        check=False,
    )
    if proc.returncode != 0:
        return ""
    return proc.stdout or ""


def extract_otp_code(text: str) -> str:
    matches = re.findall(r"\b(\d{4,8})\b", text)
    if not matches:
        return ""
    return matches[0]


def try_fill_otp(
    driver,
    by,
    otp_selectors: Iterable[str],
    submit_selectors: Iterable[str],
    cfg: Dict[str, str],
    timeout: int,
    screenshot_dir: Path,
    logger: RunLogger,
) -> bool:
    end = time.time() + timeout
    while time.time() < end:
        otp_el, where = find_in_default_and_frames(driver, by, otp_selectors)
        if otp_el is not None:
            logger.write(f"[info] OTP field found ({where}), fetching code from Mail")
            mail_text = fetch_mail_text(cfg["subject_filter"], cfg["sender_filter"])
            code = extract_otp_code(mail_text)
            if not code:
                logger.write("[warn] OTP code not found in filtered Mail scan yet")
                take_shot(driver, screenshot_dir, "otp_waiting_no_code", logger)
                time.sleep(6)
                continue
            try:
                otp_el.click()
            except Exception:
                pass
            try:
                otp_el.clear()
            except Exception:
                pass
            otp_el.send_keys(code)
            logger.write(f"[ok] filled OTP code ({where})")
            take_shot(driver, screenshot_dir, "otp_filled", logger)
            click_first_wait(driver, by, submit_selectors, "otp submit", 6, logger)
            driver.switch_to.default_content()
            return True
        time.sleep(1.0)
    logger.write("[info] OTP field not detected in wait window")
    return False


def run_course_progression(
    driver,
    by,
    screenshot_dir: Path,
    logger: RunLogger,
    max_steps: int,
    pause_sec: float,
    stall_retries: int,
    retry_refresh: int,
    retry_wait: float,
) -> bool:
    logger.write(f"[info] starting course auto-run (max_steps={max_steps})")
    take_shot(driver, screenshot_dir, "course_dashboard", logger)

    action_tokens = [
        "NEXT",
        "CONTINUE",
        "MARK AS COMPLETE",
        "COMPLETE",
        "SUBMIT",
        "FINISH",
        "START",
        "RESUME",
        "BEGIN",
        "NEXT MODULE",
        "GET STARTED",
        "START EXAM",
        "BEGIN EXAM",
        "TAKE EXAM",
        "START QUIZ",
        "TAKE QUIZ",
        "I AGREE",
        "AGREE",
        "ACCEPT",
        "CONTINUE LEARNING",
    ]

    fallback_tokens = [
        "CONFIRM",
        "SUBMIT",
        "NEXT QUESTION",
        "NEXT",
        "CONTINUE",
        "OK",
        "BEGIN",
    ]

    open_tokens = [
        "RESUME COURSE",
        "START COURSE",
        "VIEW MORE COURSES",
        "CONTINUE COURSE",
        "GO TO COURSE",
        "VIEW COURSE",
        "OPEN COURSE",
    ]

    open_course_xpath = [
        "//a[contains(translate(normalize-space(.),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'RESUME COURSE')]",
        "//button[contains(translate(normalize-space(.),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'RESUME COURSE')]",
        "//a[contains(translate(normalize-space(.),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'START COURSE')]",
        "//button[contains(translate(normalize-space(.),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'START COURSE')]",
        "//a[contains(translate(normalize-space(.),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'VIEW MORE COURSES')]",
    ]
    opened = click_first_wait(driver, by, open_course_xpath, "open course(xpath)", 8, logger)
    if not opened:
        opened = click_text_via_js(
            driver, open_tokens, "open course(js)", logger
        )
    if not opened:
        logger.write("[warn] could not open course entry from dashboard")
        return False

    time.sleep(max(0.5, pause_sec))
    take_shot(driver, screenshot_dir, "course_opened", logger)
    stall_count = 0
    refresh_count = 0
    attempts_without_progress = 0
    last_question_marker = ""
    adaptive_level = 0
    repeated_question_counts: Dict[str, int] = {}
    disable_precise_for: Set[str] = set()

    action_xpath = [
        "//button[contains(translate(normalize-space(.),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'CONFIRM')]",
        "//a[contains(translate(normalize-space(.),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'CONFIRM')]",
        "//button[contains(translate(normalize-space(.),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'NEXT QUESTION')]",
        "//a[contains(translate(normalize-space(.),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'NEXT QUESTION')]",
        "//button[contains(translate(normalize-space(.),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'NEXT')]",
        "//a[contains(translate(normalize-space(.),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'NEXT')]",
        "//button[contains(translate(normalize-space(.),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'CONTINUE')]",
        "//a[contains(translate(normalize-space(.),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'CONTINUE')]",
        "//button[contains(translate(normalize-space(.),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'MARK AS COMPLETE')]",
        "//button[contains(translate(normalize-space(.),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'COMPLETE')]",
        "//button[contains(translate(normalize-space(.),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'SUBMIT')]",
        "//button[contains(translate(normalize-space(.),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'FINISH')]",
        "//a[contains(translate(normalize-space(.),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'RESUME')]",
        "//button[contains(translate(normalize-space(.),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'LET'S START')]",
        "//button[contains(translate(normalize-space(.),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'GET STARTED')]",
        "//button[contains(translate(normalize-space(.),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'START EXAM')]",
        "//button[contains(translate(normalize-space(.),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'BEGIN EXAM')]",
        "//button[contains(translate(normalize-space(.),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'TAKE EXAM')]",
        "//button[contains(translate(normalize-space(.),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'START QUIZ')]",
        "//button[contains(translate(normalize-space(.),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'TAKE QUIZ')]",
    ]

    for step in range(max_steps):
        time.sleep(max(0.5, pause_sec))
        take_shot(driver, screenshot_dir, f"course_step_{step:03d}", logger)
        before_signature = page_signature(driver, logger)
        before_upper = safe_page_text(driver, logger)
        before_q = extract_question_marker(before_upper)
        before_state = detect_course_state(before_upper)
        before_prompt = extract_question_prompt(before_upper) if before_state == "knowledge_check_question" else ""
        before_prompt_key = normalize_question_key(before_prompt)
        if before_prompt_key:
            repeated_question_counts[before_prompt_key] = repeated_question_counts.get(before_prompt_key, 0) + 1
            if repeated_question_counts[before_prompt_key] >= 4:
                if before_prompt_key not in disable_precise_for:
                    disable_precise_for.add(before_prompt_key)
                    adaptive_level = max(adaptive_level, 1)
                    logger.write("[self-heal] repeated question detected; switching to adaptive mode")

        try:
            clicked = take_action_from_snapshot(
                driver,
                by,
                action_xpath,
                action_tokens,
                fallback_tokens,
                screenshot_dir,
                logger,
                step,
                adaptive_level,
                disable_precise_for,
            )
        except Exception as exc:
            logger.write(f"[warn] click flow error at step={step}: {exc}")
            if is_session_dead_error(exc):
                logger.write("[warn] session appears dead; aborting this attempt for restart")
                return False
            clicked = False

        page_upper = safe_page_text(driver, logger)
        if clicked:
            time.sleep(max(0.8, min(2.5, pause_sec)))
            page_upper = safe_page_text(driver, logger)
        after_q = extract_question_marker(page_upper)
        after_state = detect_course_state(page_upper)
        after_signature = page_signature(driver, logger)
        progressed = after_signature != before_signature
        if not progressed and before_q and after_q and before_q != after_q:
            progressed = True
        if not progressed and clicked and before_state == "knowledge_check_question":
            progressed = True
        if after_q and after_q != last_question_marker:
            logger.write(f"[info] quiz marker moved to {after_q}")
            last_question_marker = after_q
        if not progressed:
            attempts_without_progress += 1
            logger.write(f"[warn] no page-change detected at step={step}; no-progress count={attempts_without_progress}")
            if before_state == "knowledge_check_question" and before_prompt_key:
                adaptive_level = min(3, adaptive_level + 1)
                disable_precise_for.add(before_prompt_key)
                logger.write(f"[self-heal] stall on question; escalating adaptive_level={adaptive_level}")
        else:
            attempts_without_progress = 0

        if after_state == "knowledge_check_failed":
            adaptive_level = min(3, adaptive_level + 1)
            logger.write(f"[self-heal] quiz failed; escalating adaptive_level={adaptive_level}")

        try:
            if not clicked:
                stale = driver.execute_script("return document.readyState === 'complete'")
            else:
                stale = False
        except Exception as exc:
            logger.write(f"[warn] page stability check failed at step={step}: {exc}")
            if is_session_dead_error(exc):
                logger.write("[warn] session appears dead at stability check; aborting this attempt for restart")
                return False
            stale = True
        if stale and refresh_count < retry_refresh:
            refresh_count += 1
            logger.write(f"[warn] detected unstable session state at step={step}; refreshing ({refresh_count}/{retry_refresh})")
            try:
                driver.refresh()
            except Exception as exc:
                logger.write(f"[error] refresh failed at step={step}: {exc}")
                if is_session_dead_error(exc):
                    logger.write("[warn] refresh failed due dead session; aborting this attempt for restart")
                    return False
                return False
            time.sleep(max(pause_sec, retry_wait))
            continue

        if has_completion_marker(page_upper):
            logger.write("[info] detected completion-like marker in page source")
            take_shot(driver, screenshot_dir, "course_completion_marker", logger)
            return True

        if not clicked or not progressed:
            stall_count += 1
            logger.write(f"[info] no actionable progress at step={step}; stopping course auto-run")
            take_shot(driver, screenshot_dir, f"course_no_action_{step:03d}", logger)
            if stall_count >= stall_retries:
                if stall_count == stall_retries and refresh_count < retry_refresh:
                    refresh_count += 1
                    logger.write(f"[warn] repeated no-action detected; refreshing to recover ({refresh_count}/{retry_refresh})")
                    try:
                        driver.refresh()
                    except Exception as exc:
                        logger.write(f"[error] refresh failed during stall recovery: {exc}")
                        if is_session_dead_error(exc):
                            logger.write("[warn] refresh failed due dead session; aborting this attempt for restart")
                            return False
                        return False
                    stall_count = 0
                    time.sleep(max(pause_sec, retry_wait))
                    continue
                logger.write(f"[warn] no-action stalled after {stall_count} attempts; keeping log for manual review")
                return False
        else:
            stall_count = 0

    logger.write("[info] reached max_course_steps without explicit completion marker")
    return False


def main() -> int:
    args = build_arg_parser().parse_args()
    cfg = resolve_config(args)
    screenshot_dir, log_file = make_run_paths(args)
    script_dir = Path(__file__).resolve().parent
    logger = RunLogger(log_file)
    logger.write(f"[info] run_paths screenshots={screenshot_dir} log={log_file}")
    if not cfg["url"]:
        print("Missing login URL. Set --url or DEC_LOGIN_URL in .env.", file=sys.stderr)
        return 1

    try:
        from selenium import webdriver
        from selenium.webdriver.common.by import By
    except Exception:
        print("selenium is not installed. Run: python3 -m pip install --user selenium", file=sys.stderr)
        return 1

    options = webdriver.ChromeOptions()
    options.add_argument(f"--window-size={args.window_width},{args.window_height}")
    options.add_argument("--remote-debugging-port=0")
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--no-first-run")
    options.add_argument("--no-default-browser-check")
    if args.headless:
        options.add_argument("--headless=new")
    profile_dir = (
        Path(args.chrome_profile_dir).expanduser().resolve()
        if args.chrome_profile_dir
        else (script_dir / "cache" / "chrome_profile").resolve()
    )
    if not args.fresh_profile:
        profile_dir.mkdir(parents=True, exist_ok=True)
        options.add_argument(f"--user-data-dir={profile_dir}")
        options.add_argument("--profile-directory=Default")
        logger.write(f"[info] using persistent chrome profile: {profile_dir}")
    else:
        logger.write("[info] fresh-profile mode enabled; cookie/session reuse disabled")

    driver = None
    try:
        driver = build_chrome_driver(webdriver, logger, options, args, profile_dir)
    except Exception as exc:
        logger.write(f"[error] failed to start Chrome: {exc}")
        return 1

    if driver is None:
        logger.write("[error] failed to create webdriver session")
        return 1
    logger.write(f"[info] opening {cfg['url']}")
    driver.get(cfg["url"])
    time.sleep(2.5)
    take_shot(driver, screenshot_dir, "loaded", logger)

    username_selectors = [
        "input[type='email']",
        "input[name='email']",
        "input[id='email']",
        "input[name='username']",
        "input[id='username']",
        "input[name*='user']",
        "input[id*='user']",
        "input[type='text']",
    ]
    password_selectors = [
        "input[type='password']",
        "input[name='password']",
        "input[id='password']",
        "input[name*='pass']",
        "input[id*='pass']",
    ]
    otp_selectors = [
        "input[autocomplete='one-time-code']",
        "input[name*='otp']",
        "input[id*='otp']",
        "input[name*='code']",
        "input[id*='code']",
        "input[inputmode='numeric']",
    ]
    submit_selectors = [
        "button[type='submit']",
        "input[type='submit']",
        "button[name='next']",
        "button[id*='next']",
        "button[name*='continue']",
        "button[id*='continue']",
        "button[name='login']",
        "button[id*='login']",
        "button[id*='sign']",
    ]
    submit_xpath_selectors = [
        "//button[contains(translate(normalize-space(.),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'LOG IN')]",
        "//button[contains(translate(normalize-space(.),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'LOGIN')]",
        "//button[contains(translate(normalize-space(.),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'SIGN IN')]",
        "//button[contains(translate(normalize-space(.),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'CONTINUE')]",
        "//button[contains(translate(normalize-space(.),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'NEXT')]",
        "//input[@type='button' and contains(translate(@value,'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'LOG IN')]",
        "//input[@type='submit' and contains(translate(@value,'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'LOG IN')]",
    ]
    post_submit_continue_xpath = [
        "//button[contains(translate(normalize-space(.),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'CONTINUE')]",
        "//a[contains(translate(normalize-space(.),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'CONTINUE')]",
        "//input[@type='submit' and contains(translate(@value,'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'CONTINUE')]",
    ]
    stay_signed_in_yes_xpath = [
        "//button[normalize-space(.)='Yes']",
        "//input[@type='submit' and translate(@value,'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ')='YES']",
        "//button[contains(translate(normalize-space(.),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'YES')]",
    ]

    logged_in = looks_like_logged_in(driver, By.CSS_SELECTOR, username_selectors, logger)
    if not logged_in and args.submit:
        user_ok = fill_field_wait(driver, By.CSS_SELECTOR, username_selectors, cfg["username"], "username", 30, logger)
        take_shot(driver, screenshot_dir, "username_attempted", logger)
        if not user_ok:
            logger.write("[error] username field not resolved")
            hold_session(args.hold_seconds, logger)
            return 1

        pwd_ok = fill_field_wait(driver, By.CSS_SELECTOR, password_selectors, cfg["password"], "password", 6, logger)
        if not pwd_ok:
            clicked = click_first_wait(driver, By.CSS_SELECTOR, submit_selectors, "continue/next(css)", 6, logger)
            if not clicked:
                clicked = click_first_wait(driver, By.XPATH, submit_xpath_selectors, "continue/next(xpath)", 6, logger)
            if not clicked:
                press_enter_on_field(driver, By.CSS_SELECTOR, username_selectors, "username", logger)
            time.sleep(1.2)
            take_shot(driver, screenshot_dir, "after_next_click", logger)
            pwd_ok = fill_field_wait(driver, By.CSS_SELECTOR, password_selectors, cfg["password"], "password", 45, logger)
        take_shot(driver, screenshot_dir, "password_attempted", logger)

        if args.submit:
            submitted = click_first_wait(driver, By.CSS_SELECTOR, submit_selectors, "submit(css)", 8, logger)
            if not submitted:
                submitted = click_first_wait(driver, By.XPATH, submit_xpath_selectors, "submit(xpath)", 8, logger)
            if not submitted and not pwd_ok:
                press_enter_on_field(driver, By.CSS_SELECTOR, username_selectors, "username", logger)
            elif not submitted and pwd_ok:
                press_enter_on_field(driver, By.CSS_SELECTOR, password_selectors, "password", logger)
            time.sleep(1.0)
            take_shot(driver, screenshot_dir, "after_submit", logger)
            clicked_trust_continue = click_first_wait(driver, By.XPATH, post_submit_continue_xpath, "post-submit continue", 6, logger)
            if not clicked_trust_continue:
                clicked_trust_continue = click_text_via_js(driver, ["CONTINUE", "PROCEED", "ALLOW"], "post-submit continue", logger)
            if clicked_trust_continue:
                time.sleep(1.0)
                take_shot(driver, screenshot_dir, "after_trust_continue", logger)
            clicked_stay_signed_yes = click_first_wait(driver, By.XPATH, stay_signed_in_yes_xpath, "stay-signed-in yes", 6, logger)
            if not clicked_stay_signed_yes:
                clicked_stay_signed_yes = click_text_via_js(driver, ["YES", "KEEP ME SIGNED IN"], "stay-signed-in yes", logger)
            if clicked_stay_signed_yes:
                time.sleep(1.0)
                take_shot(driver, screenshot_dir, "after_stay_signed_in_yes", logger)
    elif logged_in:
        logger.write("[info] logged_in detected; skipping username/password flow")

    if args.otp_from_mail:
        try_fill_otp(
            driver,
            By.CSS_SELECTOR,
            otp_selectors,
            submit_selectors,
            cfg,
            args.otp_timeout_seconds,
            screenshot_dir,
            logger,
        )
        take_shot(driver, screenshot_dir, "after_otp_attempt", logger)

    if args.auto_course:
        completed = False
        total_attempts = max(1, args.auto_course_attempts)
        if total_attempts > 1:
            logger.write("[info] single-session mode enabled: retries will reuse same browser window")
        for attempt in range(total_attempts):
            logger.write(f"[info] auto-course attempt {attempt + 1}/{total_attempts}")
            if not is_driver_alive(driver, logger):
                logger.write("[error] webdriver session lost; stopping retries to avoid spawning a new window")
                break
            completed = run_course_progression(
                driver,
                By.XPATH,
                screenshot_dir,
                logger,
                args.max_course_steps,
                args.course_click_pause,
                args.course_stall_retries,
                args.course_retry_refresh,
                args.course_retry_wait,
            )
            if completed:
                break
            if attempt + 1 < total_attempts:
                logger.write("[warn] auto-course attempt failed; retrying in current window")
                time.sleep(2)
        logger.write(f"[info] auto course result: {'completed' if completed else 'incomplete'}")
        take_shot(driver, screenshot_dir, "after_auto_course", logger)

    try:
        hold_session(args.hold_seconds, logger)
    except KeyboardInterrupt:
        logger.write("[info] closing bootstrap session")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
