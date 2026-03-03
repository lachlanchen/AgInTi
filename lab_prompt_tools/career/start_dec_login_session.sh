#!/usr/bin/env zsh
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ENV_FILE="${ENV_FILE:-$SCRIPT_DIR/.env}"
VENV_DIR="${VENV_DIR:-$SCRIPT_DIR/.venv}"
PY_BIN="$VENV_DIR/bin/python3"

if [[ ! -x "$PY_BIN" ]]; then
  python3 -m venv "$VENV_DIR"
  "$PY_BIN" -m pip install --quiet --upgrade pip
fi

if ! "$PY_BIN" - <<'PY' >/dev/null 2>&1
import selenium
import webdriver_manager
PY
then
  "$PY_BIN" -m pip install --quiet --upgrade pip
  "$PY_BIN" -m pip install --quiet selenium webdriver-manager
fi

if [[ -f "$ENV_FILE" ]]; then
  exec "$PY_BIN" "$SCRIPT_DIR/selenium_login_bootstrap.py" --env-file "$ENV_FILE" "$@"
fi

exec "$PY_BIN" "$SCRIPT_DIR/selenium_login_bootstrap.py" "$@"
