#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
cp reports/demo/security_demo_report.md reports/demo/security_demo_report_copy.md
printf '{"status":"ok","profile":"security"}\n' > scripts/output/demo_run.json
echo "Security demo completed"
