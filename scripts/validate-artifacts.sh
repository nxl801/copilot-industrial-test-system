#!/usr/bin/env bash
set -euo pipefail

ARTIFACT_DIR="${ARTIFACT_DIR:-./artifacts}"

if [[ ! -d "$ARTIFACT_DIR" ]]; then
  echo "DENY: artifact directory missing: $ARTIFACT_DIR" >&2
  exit 2
fi

echo "Artifact validation placeholder OK: $ARTIFACT_DIR"
