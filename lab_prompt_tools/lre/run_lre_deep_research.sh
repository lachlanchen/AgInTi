#!/usr/bin/env zsh
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
PROMPT_TOOLS_DIR="$REPO_DIR/lab_prompt_tools"
OUTPUT_ROOT="${HOME}/.openclaw/workspace/LRE"
RUN_ID="$(date +%Y%m%d-%H%M%S)"
MODEL="${CODEX_MODEL:-gpt-5.3-codex}"
REASONING="${CODEX_REASONING:-high}"
SKIP_WEBSEARCH=0
SEND_EMAIL=1
TO_ADDR="${LRE_EMAIL_TO:-lachchen@qq.com}"
FROM_ADDR="${LRE_EMAIL_FROM:-lachlan.miao.chen@gmail.com}"

usage() {
  cat <<'USAGE'
Usage: run_lre_deep_research.sh [options]

Run full LRE cycle:
1) profile research
2) books research
3) investment research
4) ideas research
5) single-copy notes update
6) autoappdev autoreadme + autowebsite update (AgInTi/LRE/LazyLearn/LazyEarn/IDEAS)
7) email send

Options:
  --output-root <path>    Base output root
  --run-id <id>           Run id (shared across all stages)
  --model <name>          Codex model (default: gpt-5.3-codex)
  --reasoning <level>     Codex reasoning (default: high)
  --skip-websearch        Skip all websearch calls
  --no-send-email         Draft only (do not send)
  --to <email>            Email recipient (default: lachchen@qq.com)
  --from <email>          Email sender
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
    --no-send-email) SEND_EMAIL=0;;
    --to) shift; TO_ADDR="${1:-}";;
    --from) shift; FROM_ADDR="${1:-}";;
    -h|--help) usage; exit 0;;
    *) echo "Unknown option: $1" >&2; usage; exit 1;;
  esac
  shift
done

COMMON_ARGS=(
  --run-id "$RUN_ID"
  --model "$MODEL"
  --reasoning "$REASONING"
)
if [[ "$SKIP_WEBSEARCH" -eq 1 ]]; then
  COMMON_ARGS+=(--skip-websearch)
fi

LOG_DIR="${OUTPUT_ROOT}/logs/${RUN_ID}"
mkdir -p "$LOG_DIR"

"$SCRIPT_DIR/prompt_lre_profile_research.sh" \
  --output-dir "${OUTPUT_ROOT}/profile_runs" \
  "${COMMON_ARGS[@]}" \
  >"${LOG_DIR}/01_profile.log" 2>&1
PROFILE_JSON="${OUTPUT_ROOT}/profile_runs/${RUN_ID}/codex/latest-result.json"
PROFILE_MD="${OUTPUT_ROOT}/profile_runs/${RUN_ID}/profile.md"
PROFILE_SELF_HEAL_JSON="${OUTPUT_ROOT}/profile_runs/${RUN_ID}/profile_self_heal_result.json"
PROFILE_SELF_HEAL_LOG="${OUTPUT_ROOT}/profile_runs/${RUN_ID}/profile_self_heal.log"

"$SCRIPT_DIR/prompt_lre_book_finder.sh" \
  --output-dir "${OUTPUT_ROOT}/book_runs" \
  --profile-json "$PROFILE_JSON" \
  "${COMMON_ARGS[@]}" \
  >"${LOG_DIR}/02_books.log" 2>&1
BOOKS_JSON="${OUTPUT_ROOT}/book_runs/${RUN_ID}/codex/latest-result.json"
BOOKS_MD="${OUTPUT_ROOT}/book_runs/${RUN_ID}/books.md"
BOOKS_SELF_HEAL_JSON="${OUTPUT_ROOT}/book_runs/${RUN_ID}/books_self_heal_result.json"
BOOKS_SELF_HEAL_LOG="${OUTPUT_ROOT}/book_runs/${RUN_ID}/books_self_heal.log"

"$SCRIPT_DIR/prompt_lre_investment_finder.sh" \
  --output-dir "${OUTPUT_ROOT}/investment_runs" \
  --profile-json "$PROFILE_JSON" \
  "${COMMON_ARGS[@]}" \
  >"${LOG_DIR}/03_investments.log" 2>&1
INVEST_JSON="${OUTPUT_ROOT}/investment_runs/${RUN_ID}/codex/latest-result.json"
INVEST_MD="${OUTPUT_ROOT}/investment_runs/${RUN_ID}/investments.md"
INVEST_SELF_HEAL_JSON="${OUTPUT_ROOT}/investment_runs/${RUN_ID}/invest_self_heal_result.json"
INVEST_SELF_HEAL_LOG="${OUTPUT_ROOT}/investment_runs/${RUN_ID}/invest_self_heal.log"

"$SCRIPT_DIR/prompt_lre_ideas_finder.sh" \
  --output-dir "${OUTPUT_ROOT}/ideas_runs" \
  --profile-json "$PROFILE_JSON" \
  "${COMMON_ARGS[@]}" \
  >"${LOG_DIR}/04_ideas.log" 2>&1
IDEAS_JSON="${OUTPUT_ROOT}/ideas_runs/${RUN_ID}/codex/latest-result.json"
IDEAS_MD="${OUTPUT_ROOT}/ideas_runs/${RUN_ID}/ideas.md"
IDEAS_SELF_HEAL_JSON="${OUTPUT_ROOT}/ideas_runs/${RUN_ID}/ideas_self_heal_result.json"
IDEAS_SELF_HEAL_LOG="${OUTPUT_ROOT}/ideas_runs/${RUN_ID}/ideas_self_heal.log"

REPORT_DIR="${OUTPUT_ROOT}/reports"
mkdir -p "$REPORT_DIR"
REPORT_MD="${REPORT_DIR}/lre_single_copy.md"

python3 - "$PROFILE_MD" "$BOOKS_MD" "$INVEST_MD" "$IDEAS_MD" "$REPORT_MD" "$RUN_ID" >"${LOG_DIR}/05_report_build.log" 2>&1 <<'PY'
import pathlib
import sys

profile_md = pathlib.Path(sys.argv[1])
books_md = pathlib.Path(sys.argv[2])
invest_md = pathlib.Path(sys.argv[3])
ideas_md = pathlib.Path(sys.argv[4])
report_md = pathlib.Path(sys.argv[5])
run_id = sys.argv[6]

parts = [
    f"# LRE Deep Research (Single Copy)\n\nRun ID: {run_id}\n",
    "## Profile\n",
    profile_md.read_text(encoding="utf-8") if profile_md.exists() else "_missing_\n",
    "\n## Books\n",
    books_md.read_text(encoding="utf-8") if books_md.exists() else "_missing_\n",
    "\n## Investments\n",
    invest_md.read_text(encoding="utf-8") if invest_md.exists() else "_missing_\n",
    "\n## Research Ideas\n",
    ideas_md.read_text(encoding="utf-8") if ideas_md.exists() else "_missing_\n",
]
report_md.write_text("\n".join(parts), encoding="utf-8")
PY

# maintain single-copy updates in target repos (overwrite, do not append)
{
  mkdir -p "$REPO_DIR/LifeReverseEngineering/notes"
  cp "$REPORT_MD" "$REPO_DIR/LifeReverseEngineering/notes/lre_single_copy.md"

  mkdir -p "$REPO_DIR/LifeReverseEngineering/learn/notes"
  cp "$BOOKS_MD" "$REPO_DIR/LifeReverseEngineering/learn/notes/lre_books_latest.md"
  mkdir -p "$REPO_DIR/LifeReverseEngineering/learn/tools/lre"
  cp "$BOOKS_SELF_HEAL_JSON" "$REPO_DIR/LifeReverseEngineering/learn/tools/lre/books_self_heal_latest.json"
  cp "$BOOKS_SELF_HEAL_LOG" "$REPO_DIR/LifeReverseEngineering/learn/tools/lre/books_self_heal_latest.log"

  mkdir -p "$REPO_DIR/LifeReverseEngineering/earn/notes"
  cp "$INVEST_MD" "$REPO_DIR/LifeReverseEngineering/earn/notes/lre_investments_latest.md"
  mkdir -p "$REPO_DIR/LifeReverseEngineering/earn/tools/lre"
  cp "$INVEST_SELF_HEAL_JSON" "$REPO_DIR/LifeReverseEngineering/earn/tools/lre/investments_self_heal_latest.json"
  cp "$INVEST_SELF_HEAL_LOG" "$REPO_DIR/LifeReverseEngineering/earn/tools/lre/investments_self_heal_latest.log"

  mkdir -p "$REPO_DIR/LifeReverseEngineering/IDEAS/notes"
  cp "$IDEAS_MD" "$REPO_DIR/LifeReverseEngineering/IDEAS/notes/lre_research_ideas_latest.md"
  mkdir -p "$REPO_DIR/LifeReverseEngineering/IDEAS/tools/lre"
  cp "$IDEAS_SELF_HEAL_JSON" "$REPO_DIR/LifeReverseEngineering/IDEAS/tools/lre/ideas_self_heal_latest.json"
  cp "$IDEAS_SELF_HEAL_LOG" "$REPO_DIR/LifeReverseEngineering/IDEAS/tools/lre/ideas_self_heal_latest.log"

  mkdir -p "$REPO_DIR/LifeReverseEngineering/tools/lre"
  cp "$PROFILE_SELF_HEAL_JSON" "$REPO_DIR/LifeReverseEngineering/tools/lre/profile_self_heal_latest.json"
  cp "$PROFILE_SELF_HEAL_LOG" "$REPO_DIR/LifeReverseEngineering/tools/lre/profile_self_heal_latest.log"
} >"${LOG_DIR}/06_repo_sync.log" 2>&1

"$SCRIPT_DIR/run_lre_autoappdev.sh" \
  --context-file "$REPORT_MD" \
  --run-id "$RUN_ID" \
  --model "$MODEL" \
  --reasoning "$REASONING" \
  >"${LOG_DIR}/07_autoappdev.log" 2>&1

EMAIL_INSTRUCTION="${REPORT_DIR}/email_instruction_${RUN_ID}.txt"
cat > "$EMAIL_INSTRUCTION" <<EOF
Create a polished HTML email for today's Life Reverse Engineering deep research.

Requirements:
- Chinese-first narrative, concise English labels.
- Include four sections: Profile, Books, Investments, Research Ideas.
- Keep it concise but complete.
- Subject must include: [LRE] Deep Research Update
- Do not invent facts outside the provided markdown.

Markdown report:
$(cat "$REPORT_MD")
EOF

EMAIL_LOG="${REPORT_DIR}/email_${RUN_ID}.log"
if [[ "$SEND_EMAIL" -eq 1 ]]; then
  cat "$EMAIL_INSTRUCTION" | python3 "$PROMPT_TOOLS_DIR/runtime/codex-email-cli.py" \
    --to "$TO_ADDR" \
    --from "$FROM_ADDR" \
    --model "$MODEL" \
    --reasoning "$REASONING" \
    --prompt-tools-dir "$PROMPT_TOOLS_DIR/runtime" \
    --skip-git-check \
    --send \
    >"$EMAIL_LOG" 2>&1
else
  cat "$EMAIL_INSTRUCTION" | python3 "$PROMPT_TOOLS_DIR/runtime/codex-email-cli.py" \
    --to "$TO_ADDR" \
    --from "$FROM_ADDR" \
    --model "$MODEL" \
    --reasoning "$REASONING" \
    --prompt-tools-dir "$PROMPT_TOOLS_DIR/runtime" \
    --skip-git-check \
    >"$EMAIL_LOG" 2>&1
fi

echo "lre_run_id=$RUN_ID"
echo "profile=$PROFILE_JSON"
echo "books=$BOOKS_JSON"
echo "investments=$INVEST_JSON"
echo "ideas=$IDEAS_JSON"
echo "report=$REPORT_MD"
echo "email_log=$EMAIL_LOG"
echo "logs_dir=$LOG_DIR"
echo "autoappdev_log=${LOG_DIR}/07_autoappdev.log"
