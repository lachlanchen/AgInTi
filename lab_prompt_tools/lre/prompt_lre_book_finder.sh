#!/usr/bin/env zsh
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
PROMPT_TOOLS_DIR="$REPO_DIR/lab_prompt_tools"
OUTPUT_DIR="${HOME}/.openclaw/workspace/LRE/book_runs"
RUN_ID="$(date +%Y%m%d-%H%M%S)"
MODEL="${CODEX_MODEL:-gpt-5.3-codex-spark}"
REASONING="${CODEX_REASONING:-high}"
PROFILE_JSON=""
SKIP_WEBSEARCH=0

QUERIES=(
  "best books systems thinking founder decision making"
  "best books on emotional discipline and self mastery"
  "books for strategic execution and focus"
  "shadow work books for ambitious leaders"
  "books creativity research and product innovation"
)

usage() {
  cat <<'USAGE'
Usage: prompt_lre_book_finder.sh [options]

Options:
  --profile-json <path>  Profile JSON (optional; can use latest from profile runs)
  --output-dir <path>    Output root (default: ~/.openclaw/workspace/LRE/book_runs)
  --run-id <id>          Run id (default: timestamp)
  --model <name>         Codex model
  --reasoning <level>    Codex reasoning
  --skip-websearch       Skip websearch stage
  --help
USAGE
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --profile-json) shift; PROFILE_JSON="${1:-}";;
    --output-dir) shift; OUTPUT_DIR="${1:-}";;
    --run-id) shift; RUN_ID="${1:-}";;
    --model) shift; MODEL="${1:-}";;
    --reasoning) shift; REASONING="${1:-}";;
    --skip-websearch) SKIP_WEBSEARCH=1;;
    -h|--help) usage; exit 0;;
    *) echo "Unknown option: $1" >&2; usage; exit 1;;
  esac
  shift
done

if [[ -z "$PROFILE_JSON" ]]; then
  PROFILE_JSON="${HOME}/.openclaw/workspace/LRE/profile_runs/latest/latest-result.json"
fi

RUN_DIR="${OUTPUT_DIR}/${RUN_ID}"
WEB_DIR="${RUN_DIR}/websearch"
CODEx_DIR="${RUN_DIR}/codex"
mkdir -p "$WEB_DIR" "$CODEx_DIR"

if [[ "$SKIP_WEBSEARCH" -eq 0 ]]; then
  i=1
  for q in "${QUERIES[@]}"; do
    "$PROMPT_TOOLS_DIR/websearch/prompt_web_search_batch.sh" \
      --query "$q" \
      --kind auto \
      --top-results 5 \
      --output-dir "$WEB_DIR" \
      --run-id "books-${i}" \
      --no-codex || true
    i=$((i + 1))
  done
fi

INPUT_JSON="${RUN_DIR}/books_input.json"
python3 - "$INPUT_JSON" "$PROFILE_JSON" "$WEB_DIR" <<'PY'
import json
import pathlib
import sys

out = pathlib.Path(sys.argv[1])
profile_path = pathlib.Path(sys.argv[2])
web_dir = pathlib.Path(sys.argv[3])

profile = {}
if profile_path.exists():
    try:
        profile = json.loads(profile_path.read_text(encoding="utf-8"))
    except Exception:
        profile = {"raw_profile_path": str(profile_path)}

artifacts = [str(p) for p in sorted(web_dir.rglob("search_batch_result.json"))]
payload = {
    "profile": profile,
    "profile_path": str(profile_path),
    "websearch_artifacts": artifacts,
}
out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
PY

python3 "$PROMPT_TOOLS_DIR/runtime/codex-json-runner.py" \
  --input-json "$INPUT_JSON" \
  --output-dir "$CODEx_DIR" \
  --prompt-file "$PROMPT_TOOLS_DIR/lre/lre_books_prompt.md" \
  --schema "$PROMPT_TOOLS_DIR/lre/lre_books_schema.json" \
  --model "$MODEL" \
  --reasoning "$REASONING" \
  --label lre-books \
  --skip-git-check

echo "run_dir=$RUN_DIR"
echo "books_result=${CODEx_DIR}/latest-result.json"
