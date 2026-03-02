#!/usr/bin/env zsh
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
PROMPT_TOOLS_DIR="$REPO_DIR/lab_prompt_tools"
OUTPUT_DIR="${HOME}/.openclaw/workspace/LRE/self_evolve_runs"
RUN_ID="$(date +%Y%m%d-%H%M%S)"
MODEL="${CODEX_MODEL:-gpt-5.3-codex}"
REASONING="${CODEX_REASONING:-high}"
TOOL_NAME="lre"
FEEDBACK=""
LATEST_OUTPUT_PATH=""
QUERY_FILE=""
PROMPT_FILE="$PROMPT_TOOLS_DIR/lre/lre_self_evolve_prompt.md"
LABEL="lre-self-evolve"
APPLY=0

usage() {
  cat <<'USAGE'
Usage: prompt_lre_self_evolve.sh [options]

Options:
  --tool-name <name>         Tool identity (default: lre)
  --feedback <text>          Required feedback string
  --latest-output <path>     Optional latest result JSON path
  --query-file <path>        Optional query file for auto-heal updates
  --prompt-file <path>       Prompt file override (default: lre_self_evolve_prompt.md)
  --label <name>             Codex runner label (default: lre-self-evolve)
  --apply                    Apply recommended_queries into query-file (dedupe append)
  --output-dir <path>        Output root (default: ~/.openclaw/workspace/LRE/self_evolve_runs)
  --run-id <id>              Run id (default: timestamp)
  --model <name>             Codex model (default: gpt-5.3-codex)
  --reasoning <level>        Codex reasoning (default: high)
  --help
USAGE
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --tool-name) shift; TOOL_NAME="${1:-}";;
    --feedback) shift; FEEDBACK="${1:-}";;
    --latest-output) shift; LATEST_OUTPUT_PATH="${1:-}";;
    --query-file) shift; QUERY_FILE="${1:-}";;
    --prompt-file) shift; PROMPT_FILE="${1:-}";;
    --label) shift; LABEL="${1:-}";;
    --apply) APPLY=1;;
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

if [[ "$APPLY" -eq 1 && -z "$QUERY_FILE" ]]; then
  echo "--apply requires --query-file" >&2
  exit 1
fi

RUN_DIR="${OUTPUT_DIR}/${RUN_ID}"
CODEX_DIR="${RUN_DIR}/codex"
mkdir -p "$RUN_DIR" "$CODEX_DIR"

INPUT_JSON="${RUN_DIR}/self_evolve_input.json"
python3 - "$INPUT_JSON" "$TOOL_NAME" "$FEEDBACK" "$LATEST_OUTPUT_PATH" "$QUERY_FILE" <<'PY'
import json
import pathlib
import sys

out = pathlib.Path(sys.argv[1])
tool_name = sys.argv[2]
feedback = sys.argv[3]
latest_output = sys.argv[4]
query_file = sys.argv[5]

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
    "query_file": query_file,
}
out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
PY

python3 "$PROMPT_TOOLS_DIR/runtime/codex-json-runner.py" \
  --input-json "$INPUT_JSON" \
  --output-dir "$CODEX_DIR" \
  --prompt-file "$PROMPT_FILE" \
  --schema "$PROMPT_TOOLS_DIR/lre/lre_self_evolve_schema.json" \
  --model "$MODEL" \
  --reasoning "$REASONING" \
  --label "$LABEL" \
  --skip-git-check

RESULT_PATH="${CODEX_DIR}/latest-result.json"
if [[ "$APPLY" -eq 1 ]]; then
  python3 - "$RESULT_PATH" "$QUERY_FILE" <<'PY'
import json
import pathlib
import sys

result_path = pathlib.Path(sys.argv[1])
query_path = pathlib.Path(sys.argv[2])

existing = []
if query_path.exists():
    for line in query_path.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        existing.append(s)
seen = {x.lower() for x in existing}

recommended = []
if result_path.exists():
    data = json.loads(result_path.read_text(encoding="utf-8"))
    for q in data.get("recommended_queries", []):
        s = str(q).strip()
        if not s:
            continue
        if s.lower() in seen:
            continue
        seen.add(s.lower())
        recommended.append(s)

if recommended:
    lines = query_path.read_text(encoding="utf-8").splitlines() if query_path.exists() else []
    lines.append("")
    lines.append("# auto-evolve")
    lines.extend(recommended)
    query_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"applied_queries={len(recommended)}")
else:
    print("applied_queries=0")
PY
fi

echo "run_dir=$RUN_DIR"
echo "self_evolve_result=$RESULT_PATH"
echo "self_evolve_prompt=$PROMPT_FILE"
