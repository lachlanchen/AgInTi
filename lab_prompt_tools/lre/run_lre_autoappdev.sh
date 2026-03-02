#!/usr/bin/env zsh
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
OUTPUT_DIR="${HOME}/.openclaw/workspace/LRE/autoappdev"
RUN_ID="$(date +%Y%m%d-%H%M%S)"
MODEL="${CODEX_MODEL:-gpt-5.3-codex}"
REASONING="${CODEX_REASONING:-high}"
CONTEXT_FILE=""

usage() {
  cat <<'USAGE'
Usage: run_lre_autoappdev.sh [options]

Options:
  --context-file <path>   Shared context markdown file (optional)
  --output-dir <path>     Output root (default: ~/.openclaw/workspace/LRE/autoappdev)
  --run-id <id>           Run id (default: timestamp)
  --model <name>          Codex model (default: gpt-5.3-codex)
  --reasoning <level>     Codex reasoning (default: high)
  --help
USAGE
}

while [[ $# -gt 0 ]]; do
  case "$1" in
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

LOG_DIR="${OUTPUT_DIR}/logs/${RUN_ID}"
mkdir -p "$LOG_DIR"

declare -a repos=(
  "AgInTi|$REPO_DIR"
  "LifeReverseEngineering|$REPO_DIR/LifeReverseEngineering"
  "LazyLearn|$REPO_DIR/LifeReverseEngineering/learn"
  "LazyEarn|$REPO_DIR/LifeReverseEngineering/earn"
  "IDEAS|$REPO_DIR/LifeReverseEngineering/IDEAS"
)

for spec in "${repos[@]}"; do
  name="${spec%%|*}"
  path="${spec#*|}"
  safe_name="${name:l}"

  "$SCRIPT_DIR/prompt_lre_repo_autoreadme.sh" \
    --repo-path "$path" \
    --repo-name "$name" \
    --context-file "$CONTEXT_FILE" \
    --run-id "$RUN_ID" \
    --model "$MODEL" \
    --reasoning "$REASONING" \
    >"${LOG_DIR}/${safe_name}_autoreadme.log" 2>&1

  "$SCRIPT_DIR/prompt_lre_repo_autowebsite.sh" \
    --repo-path "$path" \
    --repo-name "$name" \
    --context-file "$CONTEXT_FILE" \
    --run-id "$RUN_ID" \
    --model "$MODEL" \
    --reasoning "$REASONING" \
    >"${LOG_DIR}/${safe_name}_autowebsite.log" 2>&1
done

echo "run_id=$RUN_ID"
echo "autoappdev_logs=$LOG_DIR"
