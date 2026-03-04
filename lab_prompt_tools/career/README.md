# Career Agent Tools

This module is a dedicated prompt-tool stack for:

- finishing online courses (with manual login checkpoints)
- maintaining a LinkedIn profile/workflow
- auto-generating and auto-repairing dedicated scripts for those tasks

## Files

- `start_dec_login_session.sh`
- `selenium_login_bootstrap.py`
- `prompt_career_tool_builder.sh`
- `prompt_career_tool_builder.md`
- `career_tool_builder_schema.json`
- `prompt_career_tool_autodev.sh`
- `career_autodev_apply_prompt.md`
- `.env` (ignored)
- `env.example`

## Runtime reuse

This module reuses existing shared runners:

- `lab_prompt_tools/runtime/codex-json-runner.py`
- `lab_prompt_tools/runtime/codex-noninteractive.sh`

## Quick start

1. Start manual login bootstrap:

```bash
/Users/lachlan/Local/Clawbot/AgInTi/lab_prompt_tools/career/start_dec_login_session.sh
```

2. Build a tool plan:

```bash
/Users/lachlan/Local/Clawbot/AgInTi/lab_prompt_tools/career/prompt_career_tool_builder.sh \
  --objective "Finish DEC online course and keep LinkedIn updated weekly"
```

3. Run autodev (plan + apply/fix):

```bash
/Users/lachlan/Local/Clawbot/AgInTi/lab_prompt_tools/career/prompt_career_tool_autodev.sh \
  --objective "Finish DEC online course and maintain LinkedIn"
```

## Logic map (HKU DEC course agent)

```mermaid
flowchart TD
  A[Human runs start_dec_login_session.sh] --> B[Bootstrap venv + selenium deps]
  B --> C[Run selenium_login_bootstrap.py]
  C --> D[Load config from .env or CLI flags]
  D --> E{Already logged in?}
  E -- yes --> F[Open course dashboard]
  E -- no --> G[Fill username/password]
  G --> H[Manual checkpoint for verification and OTP]
  H --> F
  F --> I[Auto-course loop]
  I --> J[Detect page state and question markers]
  J --> K[Pick answer via precise/reasoned mapping]
  K --> L[Click confirm/next using main-pane JS/xpath fallbacks]
  L --> M{Progress detected?}
  M -- yes --> I
  M -- no --> N[Stall handling: retry, refresh, no-action guard]
  N --> I
  I --> O{Completion marker found?}
  O -- yes --> P[Result: completed]
  O -- no --> Q[Result: incomplete + logs for repair]
  P --> R[Write screenshots + bootstrap.log in sessions/<run-id>/]
  Q --> R
```

```mermaid
flowchart LR
  U[Human objective] --> V[prompt_career_tool_builder.sh]
  V --> W[JSON plan via prompt_career_tool_builder.md + schema]
  W --> X[prompt_career_tool_autodev.sh]
  X --> Y[Apply/fix tools via career_autodev_apply_prompt.md]
  Y --> Z[Run bootstrap again with updated logic]
  Z --> AA[sessions/ screenshots + bootstrap.log]
  AA --> AB[Shadow-self diagnosis inputs]
  AB --> X
```
