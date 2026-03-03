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
RUN_ID="$(date +%Y%m%d-%H%M%S)"
OUTPUT_ROOT="${HOME}/.openclaw/workspace/AgInTi/career_tool_builder_runs"
LABEL="career-tool-builder"

usage() {
  cat <<'USAGE'
Usage: prompt_career_tool_builder.sh [options]

Options:
  --objective <text>       Required objective statement
  --issue-log-file <path>  Optional issue log text file
  --target-root <path>     Output tool root target (default: AgInTi/AutoAppDev/CareerOps)
  --model <name>           Codex model (default: gpt-5.3-codex)
  --reasoning <level>      Codex reasoning (default: medium)
  --run-id <id>            Run id override
  --output-root <path>     Builder run root
  --label <name>           Codex run label
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
CODEX_DIR="$RUN_DIR/codex"
mkdir -p "$RUN_DIR" "$CODEX_DIR"

INPUT_JSON="$RUN_DIR/input.json"
python3 - "$INPUT_JSON" "$OBJECTIVE" "$TARGET_ROOT" "$ISSUE_LOG_FILE" <<'PY'
import json
import pathlib
import sys

out = pathlib.Path(sys.argv[1])
objective = sys.argv[2]
target_root = sys.argv[3]
issue_log_file = sys.argv[4]

issue_log_text = ""
if issue_log_file:
    p = pathlib.Path(issue_log_file).expanduser()
    if p.exists() and p.is_file():
        issue_log_text = p.read_text(encoding="utf-8")

payload = {
    "objective": objective,
    "target_root": target_root,
    "issue_log_text": issue_log_text,
    "existing_runtime_tools": [
        "lab_prompt_tools/runtime/codex-json-runner.py",
        "lab_prompt_tools/runtime/codex-noninteractive.sh",
        "lab_prompt_tools/websearch/prompt_web_search_immersive.sh",
    ],
}
out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
PY

python3 "$PROMPT_TOOLS_DIR/runtime/codex-json-runner.py" \
  --input-json "$INPUT_JSON" \
  --output-dir "$CODEX_DIR" \
  --prompt-file "$SCRIPT_DIR/prompt_career_tool_builder.md" \
  --schema "$SCRIPT_DIR/career_tool_builder_schema.json" \
  --model "$MODEL" \
  --reasoning "$REASONING" \
  --label "$LABEL" \
  --skip-git-check

echo "run_dir=$RUN_DIR"
echo "builder_result=$CODEX_DIR/latest-result.json"

