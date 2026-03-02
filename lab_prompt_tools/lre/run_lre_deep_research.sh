#!/usr/bin/env zsh
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
OUTPUT_ROOT="${HOME}/.openclaw/workspace/LRE"
RUN_ID="$(date +%Y%m%d-%H%M%S)"
MODEL="${CODEX_MODEL:-gpt-5.3-codex-spark}"
REASONING="${CODEX_REASONING:-high}"
SKIP_WEBSEARCH=0

usage() {
  cat <<'USAGE'
Usage: run_lre_deep_research.sh [options]

Run full LRE cycle:
1) profile research
2) book finder
3) investment finder

Options:
  --output-root <path>    Base output root
  --run-id <id>           Run id (shared across all stages)
  --model <name>          Codex model
  --reasoning <level>     Codex reasoning
  --skip-websearch        Skip all websearch calls
  --help
USAGE
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --output-root) shift; OUTPUT_ROOT="${1:-}";;
    --run-id) shift; RUN_ID="${1:-}";;
    --model) shift; MODEL="${1:-}";;
    --reasoning) shift; REASONING="${1:-}";;
    --skip-websearch) SKIP_WEBSEARCH=1;;
    -h|--help) usage; exit 0;;
    *) echo "Unknown option: $1" >&2; usage; exit 1;;
  esac
  shift
done

PROFILE_ARGS=(
  --output-dir "${OUTPUT_ROOT}/profile_runs"
  --run-id "$RUN_ID"
  --model "$MODEL"
  --reasoning "$REASONING"
)
BOOK_ARGS=(
  --output-dir "${OUTPUT_ROOT}/book_runs"
  --run-id "$RUN_ID"
  --model "$MODEL"
  --reasoning "$REASONING"
)
INVEST_ARGS=(
  --output-dir "${OUTPUT_ROOT}/investment_runs"
  --run-id "$RUN_ID"
  --model "$MODEL"
  --reasoning "$REASONING"
)

if [[ "$SKIP_WEBSEARCH" -eq 1 ]]; then
  PROFILE_ARGS+=(--skip-websearch)
  BOOK_ARGS+=(--skip-websearch)
  INVEST_ARGS+=(--skip-websearch)
fi

"$SCRIPT_DIR/prompt_lre_profile_research.sh" "${PROFILE_ARGS[@]}"
PROFILE_JSON="${OUTPUT_ROOT}/profile_runs/${RUN_ID}/codex/latest-result.json"

"$SCRIPT_DIR/prompt_lre_book_finder.sh" \
  "${BOOK_ARGS[@]}" \
  --profile-json "$PROFILE_JSON"

"$SCRIPT_DIR/prompt_lre_investment_finder.sh" \
  "${INVEST_ARGS[@]}" \
  --profile-json "$PROFILE_JSON"

echo "lre_run_id=$RUN_ID"
echo "profile=${OUTPUT_ROOT}/profile_runs/${RUN_ID}/codex/latest-result.json"
echo "books=${OUTPUT_ROOT}/book_runs/${RUN_ID}/codex/latest-result.json"
echo "investments=${OUTPUT_ROOT}/investment_runs/${RUN_ID}/codex/latest-result.json"
