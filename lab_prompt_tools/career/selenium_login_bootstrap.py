#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, Iterable, Optional, Tuple


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
    p.add_argument("--headless", action="store_true", help="Run browser in headless mode")
    p.add_argument("--screenshot-dir", default="", help="Directory to store screenshots")
    p.add_argument("--log-file", default="", help="Run log path")
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
const nodes = Array.from(document.querySelectorAll("button,input[type='submit'],input[type='button'],a,[role='button']"));
for (const n of nodes) {
  const raw = ((n.innerText || n.textContent || n.value || "") + "").toUpperCase();
  if (!raw) continue;
  const matched = tokens.some(t => raw.includes(t));
  if (!matched) continue;
  try {
    n.click();
    return true;
  } catch (e) {}
}
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


def main() -> int:
    args = build_arg_parser().parse_args()
    cfg = resolve_config(args)
    screenshot_dir, log_file = make_run_paths(args)
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
    options.add_experimental_option("detach", True)
    if args.headless:
        options.add_argument("--headless=new")

    driver = None
    try:
        driver = webdriver.Chrome(options=options)
    except Exception as exc:
        message = str(exc)
        needs_fallback = "session not created" in message.lower() or "chromedriver" in message.lower()
        if not needs_fallback:
            raise
        try:
            from selenium.webdriver.chrome.service import Service as ChromeService
            from webdriver_manager.chrome import ChromeDriverManager

            logger.write("[warn] default chromedriver failed; trying webdriver-manager fallback")
            service = ChromeService(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)
        except Exception as inner:
            logger.write(f"[error] webdriver-manager fallback failed: {inner}")
            raise exc

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

    user_ok = fill_field_wait(driver, By.CSS_SELECTOR, username_selectors, cfg["username"], "username", 30, logger)
    take_shot(driver, screenshot_dir, "username_attempted", logger)
    if not user_ok:
        logger.write("[error] username field not resolved")
        hold_session(args.hold_seconds, logger)
        return 1

    pwd_ok = fill_field_wait(driver, By.CSS_SELECTOR, password_selectors, cfg["password"], "password", 6, logger)
    if not pwd_ok and args.submit:
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

    try:
        hold_session(args.hold_seconds, logger)
    except KeyboardInterrupt:
        logger.write("[info] closing bootstrap session")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
