#!/usr/bin/env zsh
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
PROMPT_TOOLS_DIR="$REPO_DIR/lab_prompt_tools"
OUTPUT_DIR="${HOME}/.openclaw/workspace/LRE/investment_runs"
RUN_ID="$(date +%Y%m%d-%H%M%S)"
MODEL="${CODEX_MODEL:-gpt-5.3-codex}"
REASONING="${CODEX_REASONING:-high}"
PROFILE_JSON=""
SKIP_WEBSEARCH=0
AUTO_HEAL=1
QUERY_FILE="${SCRIPT_DIR}/investment_queries.txt"
SELF_EVOLVE_PROMPT_FILE="${SCRIPT_DIR}/lre_self_evolve_investments_prompt.md"

usage() {
  cat <<'USAGE'
Usage: prompt_lre_investment_finder.sh [options]

Options:
  --profile-json <path>   Profile JSON (default: ~/.openclaw/workspace/LRE/profile_runs/latest/latest-result.json)
  --output-dir <path>     Output root (default: ~/.openclaw/workspace/LRE/investment_runs)
  --run-id <id>           Run id (default: timestamp)
  --model <name>          Codex model (default: gpt-5.3-codex)
  --reasoning <level>     Codex reasoning (default: high)
  --query-file <path>     Query file (default: lre/investment_queries.txt)
  --self-evolve-prompt <path>  Self-evolve prompt (default: lre_self_evolve_investments_prompt.md)
  --skip-websearch        Skip websearch stage
  --no-auto-heal          Disable self-heal query evolution
  --help
USAGE
}

load_queries() {
  local file="$1"
  local -a out=()
  while IFS= read -r line || [[ -n "$line" ]]; do
    line="${line#"${line%%[![:space:]]*}"}"
    line="${line%"${line##*[![:space:]]}"}"
    [[ -z "$line" ]] && continue
    [[ "$line" == \#* ]] && continue
    out+=("$line")
  done < "$file"
  printf "%s\n" "${out[@]}"
}

run_queries() {
  local prefix="$1"
  shift
  local -a queries=("$@")
  local i=1
  for q in "${queries[@]}"; do
    "$PROMPT_TOOLS_DIR/websearch/prompt_web_search_immersive.sh" \
      --query "$q" \
      --engine "google-news" \
      --results 8 \
      --open-top-results 5 \
      --summarize-open-url \
      --scroll-steps 4 \
      --scroll-pause 1.0 \
      --no-auto-attach \
      --output-dir "$WEB_DIR" \
      --run-id "${prefix}-${i}" \
      >"$WEB_DIR/${prefix}-${i}.log" 2>&1 || true
    i=$((i + 1))
  done
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --profile-json) shift; PROFILE_JSON="${1:-}";;
    --output-dir) shift; OUTPUT_DIR="${1:-}";;
    --run-id) shift; RUN_ID="${1:-}";;
    --model) shift; MODEL="${1:-}";;
    --reasoning) shift; REASONING="${1:-}";;
    --query-file) shift; QUERY_FILE="${1:-}";;
    --self-evolve-prompt) shift; SELF_EVOLVE_PROMPT_FILE="${1:-}";;
    --skip-websearch) SKIP_WEBSEARCH=1;;
    --no-auto-heal) AUTO_HEAL=0;;
    -h|--help) usage; exit 0;;
    *) echo "Unknown option: $1" >&2; usage; exit 1;;
  esac
  shift
done

if [[ -z "$PROFILE_JSON" ]]; then
  PROFILE_JSON="${HOME}/.openclaw/workspace/LRE/profile_runs/latest/latest-result.json"
fi
if [[ ! -f "$QUERY_FILE" ]]; then
  echo "Missing query file: $QUERY_FILE" >&2
  exit 1
fi

RUN_DIR="${OUTPUT_DIR}/${RUN_ID}"
WEB_DIR="${RUN_DIR}/websearch"
CODEX_DIR="${RUN_DIR}/codex"
SELF_HEAL_LOG="${RUN_DIR}/invest_self_heal.log"
SELF_HEAL_RESULT="${RUN_DIR}/invest_self_heal_result.json"
mkdir -p "$WEB_DIR" "$CODEX_DIR"

if [[ "$SKIP_WEBSEARCH" -eq 0 ]]; then
  QUERIES=("${(@f)$(load_queries "$QUERY_FILE")}")
  run_queries "invest" "${QUERIES[@]}"

  STATS_JSON="${WEB_DIR}/websearch_stats.json"
  python3 - "$WEB_DIR" "$STATS_JSON" <<'PY'
import json, pathlib, sys
web_dir = pathlib.Path(sys.argv[1])
out = pathlib.Path(sys.argv[2])
files = sorted(web_dir.rglob("query-*.json"))
success = 0
for f in files:
    try:
        data = json.loads(f.read_text(encoding="utf-8"))
    except Exception:
        continue
    if int(data.get("opened_count", 0) or 0) > 0:
        success += 1
stats = {"json_files": len(files), "success_files": success, "weak_signal": success < max(2, len(files) // 2 if files else 1)}
out.write_text(json.dumps(stats, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(stats))
PY

  if [[ "$AUTO_HEAL" -eq 1 ]]; then
    WEAK_SIGNAL="$(python3 - "$STATS_JSON" <<'PY'
import json, pathlib, sys
data = json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"))
print("1" if data.get("weak_signal") else "0")
PY
)"
    if [[ "$WEAK_SIGNAL" == "1" ]]; then
      HEAL_RUN_ID="${RUN_ID}-invest-heal"
      HEAL_RESULT_PATH="${HOME}/.openclaw/workspace/LRE/self_evolve_runs/${HEAL_RUN_ID}/codex/latest-result.json"
      "$SCRIPT_DIR/prompt_lre_self_evolve.sh" \
        --tool-name "lre-investment-websearch" \
        --feedback "Investment/news search signal weak. Improve with concise macro/theme/risk-oriented queries." \
        --query-file "$QUERY_FILE" \
        --prompt-file "$SELF_EVOLVE_PROMPT_FILE" \
        --label "lre-invest-heal" \
        --apply \
        --model "$MODEL" \
        --reasoning "$REASONING" \
        --run-id "$HEAL_RUN_ID" \
        --output-dir "${HOME}/.openclaw/workspace/LRE/self_evolve_runs" \
        >"$SELF_HEAL_LOG" 2>&1 || true
      if [[ -f "$HEAL_RESULT_PATH" ]]; then
        cp "$HEAL_RESULT_PATH" "$SELF_HEAL_RESULT"
      else
        cat > "$SELF_HEAL_RESULT" <<EOF
{"status":"failed","reason":"missing_self_evolve_result","expected":"$HEAL_RESULT_PATH"}
EOF
      fi
      QUERIES=("${(@f)$(load_queries "$QUERY_FILE")}")
      run_queries "invest-heal" "${QUERIES[@]:0:4}"
    else
      HEAL_RUN_ID="${RUN_ID}-invest-review"
      HEAL_RESULT_PATH="${HOME}/.openclaw/workspace/LRE/self_evolve_runs/${HEAL_RUN_ID}/codex/latest-result.json"
      "$SCRIPT_DIR/prompt_lre_self_evolve.sh" \
        --tool-name "lre-investment-websearch" \
        --feedback "Signal is strong. Propose incremental tool/prompt improvements to keep investment search quality improving." \
        --query-file "$QUERY_FILE" \
        --prompt-file "$SELF_EVOLVE_PROMPT_FILE" \
        --label "lre-invest-review" \
        --model "$MODEL" \
        --reasoning "$REASONING" \
        --run-id "$HEAL_RUN_ID" \
        --output-dir "${HOME}/.openclaw/workspace/LRE/self_evolve_runs" \
        >"$SELF_HEAL_LOG" 2>&1 || true
      if [[ -f "$HEAL_RESULT_PATH" ]]; then
        cp "$HEAL_RESULT_PATH" "$SELF_HEAL_RESULT"
      else
        cat > "$SELF_HEAL_RESULT" <<EOF
{"status":"failed","reason":"missing_self_evolve_result","expected":"$HEAL_RESULT_PATH"}
EOF
      fi
    fi
  else
    echo "self-heal skipped: auto-heal disabled" > "$SELF_HEAL_LOG"
    cat > "$SELF_HEAL_RESULT" <<'EOF'
{"status":"skipped","reason":"auto_heal_disabled"}
EOF
  fi
else
  echo "self-heal skipped: websearch skipped" > "$SELF_HEAL_LOG"
  cat > "$SELF_HEAL_RESULT" <<'EOF'
{"status":"skipped","reason":"websearch_skipped"}
EOF
fi

INPUT_JSON="${RUN_DIR}/investments_input.json"
python3 - "$INPUT_JSON" "$PROFILE_JSON" "$WEB_DIR" <<'PY'
import json, pathlib, sys
out = pathlib.Path(sys.argv[1])
profile_path = pathlib.Path(sys.argv[2])
web_dir = pathlib.Path(sys.argv[3])
profile = {}
if profile_path.exists():
    try:
        profile = json.loads(profile_path.read_text(encoding="utf-8"))
    except Exception:
        profile = {"raw_profile_path": str(profile_path)}
artifacts = [str(p) for p in sorted(web_dir.rglob("query-*.json"))]
payload = {"profile": profile, "profile_path": str(profile_path), "websearch_artifacts": artifacts}
out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
PY

python3 "$PROMPT_TOOLS_DIR/runtime/codex-json-runner.py" \
  --input-json "$INPUT_JSON" \
  --output-dir "$CODEX_DIR" \
  --prompt-file "$PROMPT_TOOLS_DIR/lre/lre_investments_prompt.md" \
  --schema "$PROMPT_TOOLS_DIR/lre/lre_investments_schema.json" \
  --model "$MODEL" \
  --reasoning "$REASONING" \
  --label lre-investments \
  --skip-git-check

INVEST_MD="${RUN_DIR}/investments.md"
python3 - "$CODEX_DIR/latest-result.json" "$INVEST_MD" <<'PY'
import json, pathlib, sys
src = pathlib.Path(sys.argv[1]); dst = pathlib.Path(sys.argv[2])
data = json.loads(src.read_text(encoding="utf-8")) if src.exists() else {}
lines = ["# LRE Investments", "", f"Summary: {data.get('summary', '')}", "", "## High Conviction"]
for item in data.get("high_conviction", []):
    lines.append(f"- {item.get('theme','')}")
    lines.append(f"  - Thesis: {item.get('thesis','')}")
    lines.append(f"  - Profile fit: {item.get('profile_fit','')}")
    risks = item.get("risks", [])
    if risks:
        lines.append(f"  - Risks: {', '.join(risks)}")
lines += ["", "## Watchlist"]
for x in data.get("watchlist", []):
    lines.append(f"- {x}")
lines += ["", "## Avoid For Now"]
for x in data.get("avoid_for_now", []):
    lines.append(f"- {x}")
dst.write_text("\n".join(lines) + "\n", encoding="utf-8")
PY

LATEST_DIR="${OUTPUT_DIR}/latest"
mkdir -p "$LATEST_DIR"
cp "$CODEX_DIR/latest-result.json" "$LATEST_DIR/latest-result.json"
cp "$INVEST_MD" "$LATEST_DIR/investments.md"

echo "run_dir=$RUN_DIR"
echo "investments_result=${CODEX_DIR}/latest-result.json"
echo "investments_markdown=$INVEST_MD"
echo "investments_self_heal_log=$SELF_HEAL_LOG"
echo "investments_self_heal_result=$SELF_HEAL_RESULT"
