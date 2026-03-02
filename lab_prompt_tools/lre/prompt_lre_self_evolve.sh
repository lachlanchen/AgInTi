#!/usr/bin/env zsh
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
PROMPT_TOOLS_DIR="$REPO_DIR/lab_prompt_tools"
OUTPUT_DIR="${HOME}/.openclaw/workspace/LRE/self_evolve_runs"
RUN_ID="$(date +%Y%m%d-%H%M%S)"
MODEL="${CODEX_MODEL:-gpt-5.3-codex-spark}"
REASONING="${CODEX_REASONING:-high}"
TOOL_NAME="lre"
FEEDBACK=""
LATEST_OUTPUT_PATH=""

usage() {
  cat <<'USAGE'
Usage: prompt_lre_self_evolve.sh [options]

Options:
  --tool-name <name>         Tool identity (default: lre)
  --feedback <text>          Required feedback string
  --latest-output <path>     Optional latest result JSON path
  --output-dir <path>        Output root (default: ~/.openclaw/workspace/LRE/self_evolve_runs)
  --run-id <id>              Run id (default: timestamp)
  --model <name>             Codex model
  --reasoning <level>        Codex reasoning
  --help
USAGE
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --tool-name) shift; TOOL_NAME="${1:-}";;
    --feedback) shift; FEEDBACK="${1:-}";;
    --latest-output) shift; LATEST_OUTPUT_PATH="${1:-}";;
    --output-dir) shift; OUTPUT_DIR="${1:-}";;
    --run-id) shift; RUN_ID="${1:-}";;
    --model) shift; MODEL="${1:-}";;
    --reasoning) shift; REASONING="${1:-}";;
    -h|--help) usage; exit 0;;
    *) echo "Unknown option: $1" >&2; usage; exit 1;;
  esac
  shift
done

if [[ -z "$FEEDBACK" ]]; then
  echo "--feedback is required" >&2
  usage
  exit 1
fi

RUN_DIR="${OUTPUT_DIR}/${RUN_ID}"
CODEx_DIR="${RUN_DIR}/codex"
mkdir -p "$RUN_DIR" "$CODEx_DIR"

INPUT_JSON="${RUN_DIR}/self_evolve_input.json"
python3 - "$INPUT_JSON" "$TOOL_NAME" "$FEEDBACK" "$LATEST_OUTPUT_PATH" <<'PY'
import json
import pathlib
import sys

out = pathlib.Path(sys.argv[1])
tool_name = sys.argv[2]
feedback = sys.argv[3]
latest_output = sys.argv[4]

latest_payload = {}
if latest_output:
    p = pathlib.Path(latest_output)
    if p.exists():
        try:
            latest_payload = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            latest_payload = {"raw_path": str(p)}

payload = {
    "tool_name": tool_name,
    "feedback": feedback,
    "latest_output_path": latest_output,
    "latest_output": latest_payload,
}
out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
PY

python3 "$PROMPT_TOOLS_DIR/runtime/codex-json-runner.py" \
  --input-json "$INPUT_JSON" \
  --output-dir "$CODEx_DIR" \
  --prompt-file "$PROMPT_TOOLS_DIR/lre/lre_self_evolve_prompt.md" \
  --schema "$PROMPT_TOOLS_DIR/lre/lre_self_evolve_schema.json" \
  --model "$MODEL" \
  --reasoning "$REASONING" \
  --label lre-self-evolve \
  --skip-git-check

echo "run_dir=$RUN_DIR"
echo "self_evolve_result=${CODEx_DIR}/latest-result.json"
