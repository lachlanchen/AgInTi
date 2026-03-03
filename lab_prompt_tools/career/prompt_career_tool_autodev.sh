#!/usr/bin/env zsh
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
PROMPT_TOOLS_DIR="$REPO_DIR/lab_prompt_tools"

OBJECTIVE=""
ISSUE_LOG_FILE=""
TARGET_ROOT="$REPO_DIR/AutoAppDev/CareerOps"
MODEL="${CODEX_MODEL:-gpt-5.3-codex}"
REASONING="${CODEX_REASONING:-medium}"
SAFETY="${CODEX_SAFETY:-danger-full-access}"
APPROVAL="${CODEX_APPROVAL:-never}"
RUN_ID="$(date +%Y%m%d-%H%M%S)"
OUTPUT_ROOT="${HOME}/.openclaw/workspace/AgInTi/career_autodev_runs"
LABEL="career-tool-autodev"

usage() {
  cat <<'USAGE'
Usage: prompt_career_tool_autodev.sh [options]

Runs two phases:
1) builder: create structured plan JSON
2) autodev: apply/fix scripts under target root using Codex non-interactive run

Options:
  --objective <text>       Required objective statement
  --issue-log-file <path>  Optional issue log text file
  --target-root <path>     Tool target root (default: AgInTi/AutoAppDev/CareerOps)
  --model <name>           Codex model (default: gpt-5.3-codex)
  --reasoning <level>      Codex reasoning (default: medium)
  --safety <mode>          Codex safety mode (default: danger-full-access)
  --approval <policy>      Codex approval policy (default: never)
  --run-id <id>            Run id override
  --output-root <path>     Run output root
  --label <name>           Label prefix
  -h, --help               Show help
USAGE
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --objective) shift; OBJECTIVE="${1:-}" ;;
    --issue-log-file) shift; ISSUE_LOG_FILE="${1:-}" ;;
    --target-root) shift; TARGET_ROOT="${1:-}" ;;
    --model) shift; MODEL="${1:-}" ;;
    --reasoning) shift; REASONING="${1:-}" ;;
    --safety) shift; SAFETY="${1:-}" ;;
    --approval) shift; APPROVAL="${1:-}" ;;
    --run-id) shift; RUN_ID="${1:-}" ;;
    --output-root) shift; OUTPUT_ROOT="${1:-}" ;;
    --label) shift; LABEL="${1:-}" ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown option: $1" >&2; usage >&2; exit 1 ;;
  esac
  shift
done

if [[ -z "$OBJECTIVE" ]]; then
  echo "--objective is required" >&2
  usage >&2
  exit 1
fi

RUN_DIR="$OUTPUT_ROOT/$RUN_ID"
mkdir -p "$RUN_DIR"

BUILDER_LOG="$RUN_DIR/builder.log"
EXTRA_BUILDER_ARGS=()
if [[ -n "$ISSUE_LOG_FILE" ]]; then
  EXTRA_BUILDER_ARGS+=(--issue-log-file "$ISSUE_LOG_FILE")
fi

"$SCRIPT_DIR/prompt_career_tool_builder.sh" \
  --objective "$OBJECTIVE" \
  --target-root "$TARGET_ROOT" \
  --model "$MODEL" \
  --reasoning "$REASONING" \
  --run-id "$RUN_ID-builder" \
  --output-root "$RUN_DIR" \
  --label "$LABEL-builder" \
  "${EXTRA_BUILDER_ARGS[@]}" \
  > "$BUILDER_LOG"

BUILDER_RESULT="$(python3 - "$BUILDER_LOG" <<'PY'
import pathlib
import re
import sys

log = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")
m = re.search(r"builder_result=(.+)", log)
if not m:
    raise SystemExit(1)
print(m.group(1).strip())
PY
)"

AUTODEV_PROMPT_PATH="$RUN_DIR/autodev_prompt.txt"
python3 - "$AUTODEV_PROMPT_PATH" "$SCRIPT_DIR/career_autodev_apply_prompt.md" "$OBJECTIVE" "$TARGET_ROOT" "$BUILDER_RESULT" "$ISSUE_LOG_FILE" <<'PY'
import json
import pathlib
import sys

out_path = pathlib.Path(sys.argv[1])
template_path = pathlib.Path(sys.argv[2])
objective = sys.argv[3]
target_root = sys.argv[4]
builder_result_path = pathlib.Path(sys.argv[5])
issue_log_file = sys.argv[6]

template = template_path.read_text(encoding="utf-8")
builder_json = {}
if builder_result_path.exists():
    builder_json = json.loads(builder_result_path.read_text(encoding="utf-8"))

issue_log_text = ""
if issue_log_file:
    p = pathlib.Path(issue_log_file).expanduser()
    if p.exists() and p.is_file():
        issue_log_text = p.read_text(encoding="utf-8")

prompt = (
    template
    + "\n\n=== objective ===\n"
    + objective
    + "\n\n=== target_root ===\n"
    + target_root
    + "\n\n=== issue_log_text ===\n"
    + (issue_log_text or "(empty)")
    + "\n\n=== builder_plan_json ===\n"
    + json.dumps(builder_json, ensure_ascii=False, indent=2)
)
out_path.write_text(prompt, encoding="utf-8")
PY

AUTODEV_RESPONSE="$RUN_DIR/autodev_response.md"
"$PROMPT_TOOLS_DIR/runtime/codex-noninteractive.sh" \
  --model "$MODEL" \
  --reasoning "$REASONING" \
  --safety "$SAFETY" \
  --approval "$APPROVAL" \
  --skip-git-check \
  --prompt "$(cat "$AUTODEV_PROMPT_PATH")" \
  > "$AUTODEV_RESPONSE"

echo "run_dir=$RUN_DIR"
echo "builder_result=$BUILDER_RESULT"
echo "autodev_prompt=$AUTODEV_PROMPT_PATH"
echo "autodev_response=$AUTODEV_RESPONSE"
