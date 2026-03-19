#!/usr/bin/env bash
set -euo pipefail

LOCK_FILE="${BENCH_LOCK_FILE:-./artifacts/bench.lock}"

if [[ ! -f "$LOCK_FILE" ]]; then
  echo "DENY: missing bench lock at $LOCK_FILE" >&2
  exit 2
fi

echo "ALLOW: bench lock present at $LOCK_FILE"
