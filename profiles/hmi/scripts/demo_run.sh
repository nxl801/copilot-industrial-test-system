#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
cp reports/demo/hmi_demo_report.md reports/demo/hmi_demo_report_copy.md
printf '{"status":"ok","profile":"hmi"}\n' > scripts/output/demo_run.json
echo "HMI demo completed"
