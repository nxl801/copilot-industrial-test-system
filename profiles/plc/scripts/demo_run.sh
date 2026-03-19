#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
cp reports/demo/plc_demo_report.md reports/demo/plc_demo_report_copy.md
printf '{"status":"ok","profile":"plc"}\n' > scripts/output/demo_run.json
echo "PLC demo completed"
