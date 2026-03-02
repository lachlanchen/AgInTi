#!/usr/bin/env zsh
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
PROMPT_TOOLS_DIR="$REPO_DIR/lab_prompt_tools"
OUTPUT_DIR="${HOME}/.openclaw/workspace/LRE/profile_runs"
RUN_ID="$(date +%Y%m%d-%H%M%S)"
MODEL="${CODEX_MODEL:-gpt-5.3-codex-spark}"
REASONING="${CODEX_REASONING:-high}"
SKIP_WEBSEARCH=0

LINKS=(
  "https://scholar.google.com/citations?user=Kdqr_AcAAAAJ&hl=en&authuser=1"
  "https://www.linkedin.com/in/lazyingart/"
  "https://github.com/lachlanchen"
  "https://github.com/lachlanchen?tab=repositories"
  "https://lazying.art"
)

QUERIES=(
  "lachlanchen github repositories ai automation"
  "lazyingart linkedin profile product strategy"
  "lazying art portfolio projects research"
  "lachlan chen scholar publications"
  "ai automation founder growth pattern strengths weaknesses"
)

usage() {
  cat <<'USAGE'
Usage: prompt_lre_profile_research.sh [options]

Options:
  --output-dir <path>   Output root (default: ~/.openclaw/workspace/LRE/profile_runs)
  --run-id <id>         Run id (default: timestamp)
  --model <name>        Codex model (default: gpt-5.3-codex-spark)
  --reasoning <level>   Reasoning level (default: high)
  --skip-websearch      Skip websearch stage and only run synthesis
  --help
USAGE
}

while [[ $# -gt 0 ]]; do
  case "$1" in
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
      --run-id "profile-${i}" \
      --no-codex || true
    i=$((i + 1))
  done
fi

INPUT_JSON="${RUN_DIR}/profile_input.json"
python3 - "$INPUT_JSON" "$WEB_DIR" <<'PY'
import json
import pathlib
import sys

out = pathlib.Path(sys.argv[1])
web_dir = pathlib.Path(sys.argv[2])
links = [
    "https://scholar.google.com/citations?user=Kdqr_AcAAAAJ&hl=en&authuser=1",
    "https://www.linkedin.com/in/lazyingart/",
    "https://github.com/lachlanchen",
    "https://github.com/lachlanchen?tab=repositories",
    "https://lazying.art",
]
artifacts = [str(p) for p in sorted(web_dir.rglob("search_batch_result.json"))]
payload = {
    "profile_links": links,
    "websearch_artifacts": artifacts,
}
out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
PY

python3 "$PROMPT_TOOLS_DIR/runtime/codex-json-runner.py" \
  --input-json "$INPUT_JSON" \
  --output-dir "$CODEx_DIR" \
  --prompt-file "$PROMPT_TOOLS_DIR/lre/lre_profile_prompt.md" \
  --schema "$PROMPT_TOOLS_DIR/lre/lre_profile_schema.json" \
  --model "$MODEL" \
  --reasoning "$REASONING" \
  --label lre-profile \
  --skip-git-check

echo "run_dir=$RUN_DIR"
echo "profile_result=${CODEx_DIR}/latest-result.json"
