#!/usr/bin/env zsh
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
PROMPT_TOOLS_DIR="$REPO_DIR/lab_prompt_tools"
OUTPUT_DIR="${HOME}/.openclaw/workspace/LRE/autoappdev/readme_runs"
RUN_ID="$(date +%Y%m%d-%H%M%S)"
MODEL="${CODEX_MODEL:-gpt-5.3-codex}"
REASONING="${CODEX_REASONING:-high}"
REPO_PATH=""
REPO_NAME=""
CONTEXT_FILE=""

usage() {
  cat <<'USAGE'
Usage: prompt_lre_repo_autoreadme.sh [options]

Options:
  --repo-path <path>      Target repo path (required)
  --repo-name <name>      Repo display name (default: basename of repo path)
  --context-file <path>   Context markdown file (optional)
  --output-dir <path>     Output root (default: ~/.openclaw/workspace/LRE/autoappdev/readme_runs)
  --run-id <id>           Run id (default: timestamp)
  --model <name>          Codex model (default: gpt-5.3-codex)
  --reasoning <level>     Codex reasoning (default: high)
  --help
USAGE
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --repo-path) shift; REPO_PATH="${1:-}";;
    --repo-name) shift; REPO_NAME="${1:-}";;
    --context-file) shift; CONTEXT_FILE="${1:-}";;
    --output-dir) shift; OUTPUT_DIR="${1:-}";;
    --run-id) shift; RUN_ID="${1:-}";;
    --model) shift; MODEL="${1:-}";;
    --reasoning) shift; REASONING="${1:-}";;
    -h|--help) usage; exit 0;;
    *) echo "Unknown option: $1" >&2; usage; exit 1;;
  esac
  shift
done

if [[ -z "$REPO_PATH" ]]; then
  echo "--repo-path is required" >&2
  exit 1
fi
if [[ -z "$REPO_NAME" ]]; then
  REPO_NAME="$(basename "$REPO_PATH")"
fi

RUN_DIR="${OUTPUT_DIR}/${RUN_ID}_${REPO_NAME}"
CODEX_DIR="${RUN_DIR}/codex"
mkdir -p "$RUN_DIR" "$CODEX_DIR"

INPUT_JSON="${RUN_DIR}/autoreadme_input.json"
python3 - "$INPUT_JSON" "$REPO_PATH" "$REPO_NAME" "$CONTEXT_FILE" <<'PY'
import json
import pathlib
import sys

out = pathlib.Path(sys.argv[1])
repo_path = pathlib.Path(sys.argv[2]).expanduser()
repo_name = sys.argv[3]
context_file = pathlib.Path(sys.argv[4]).expanduser() if sys.argv[4] else None
readme_path = repo_path / "README.md"

context_text = ""
if context_file and context_file.exists():
    context_text = context_file.read_text(encoding="utf-8")

readme_text = ""
if readme_path.exists():
    readme_text = readme_path.read_text(encoding="utf-8")

top_entries = []
if repo_path.exists():
    for p in sorted(repo_path.iterdir()):
        top_entries.append(p.name + ("/" if p.is_dir() else ""))

payload = {
    "repo_name": repo_name,
    "repo_path": str(repo_path),
    "top_level_entries": top_entries,
    "existing_readme_path": str(readme_path),
    "existing_readme_markdown": readme_text,
    "lre_context_markdown": context_text,
}
out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
PY

python3 "$PROMPT_TOOLS_DIR/runtime/codex-json-runner.py" \
  --input-json "$INPUT_JSON" \
  --output-dir "$CODEX_DIR" \
  --prompt-file "$PROMPT_TOOLS_DIR/lre/lre_repo_readme_prompt.md" \
  --schema "$PROMPT_TOOLS_DIR/lre/lre_repo_readme_schema.json" \
  --model "$MODEL" \
  --reasoning "$REASONING" \
  --label "lre-autoreadme-${REPO_NAME}" \
  --skip-git-check

README_PATH="${REPO_PATH}/README.md"
python3 - "$CODEX_DIR/latest-result.json" "$README_PATH" <<'PY'
import json
import pathlib
import sys

result_path = pathlib.Path(sys.argv[1])
readme_path = pathlib.Path(sys.argv[2])
data = json.loads(result_path.read_text(encoding="utf-8")) if result_path.exists() else {}
content = data.get("readme_markdown", "").strip()
if not content:
    content = "# README\n\nAutoREADME generated empty content.\n"
readme_path.write_text(content + "\n", encoding="utf-8")
PY

echo "run_dir=$RUN_DIR"
echo "repo_path=$REPO_PATH"
echo "readme_path=$README_PATH"
echo "autoreadme_result=${CODEX_DIR}/latest-result.json"
