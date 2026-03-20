#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

mkdir -p scripts/output artifacts/security/raw artifacts/evidence/bench_output artifacts/findings reports

cat > artifacts/security/raw/burp_sample.json <<'JSON'
[
  {"target":"plc-web-ui","protocol":"https","cwe":"CWE-798","summary":"Default credential still enabled"}
]
JSON

python3 tools/mcp/labctl/server.py >/tmp/copilot_labctl.log 2>&1 &
LABCTL_PID=$!
python3 tools/mcp/scanparse/server.py >/tmp/copilot_scanparse.log 2>&1 &
SCAN_PID=$!
trap 'kill $LABCTL_PID $SCAN_PID 2>/dev/null || true' EXIT
sleep 1

curl -s -X POST http://127.0.0.1:8761/ -H 'content-type: application/json' -d '{"tool":"reserve_bench","params":{"station_id":"bench-a01","operator":"demo"}}' > scripts/output/reserve_bench.json
curl -s -X POST http://127.0.0.1:8761/ -H 'content-type: application/json' -d '{"tool":"start_capture","params":{"channels":["log","trace"]}}' > scripts/output/start_capture.json
curl -s -X POST http://127.0.0.1:8761/ -H 'content-type: application/json' -d '{"tool":"read_alarm_log","params":{"station_id":"bench-a01"}}' > scripts/output/read_alarm_log.json
curl -s -X POST http://127.0.0.1:8762/ -H 'content-type: application/json' -d '{"tool":"import_burp","params":{"path":"artifacts/security/raw/burp_sample.json"}}' > scripts/output/import_burp.json
curl -s -X POST http://127.0.0.1:8762/ -H 'content-type: application/json' -d '{"tool":"deduplicate_findings","params":{"paths":["artifacts/security/raw/burp_sample.json"]}}' > scripts/output/deduplicate_findings.json

cp reports/release-3.8.12-test-summary.md reports/demo_release_report.md

echo "Demo run completed"
echo "Outputs:"
find scripts/output artifacts/evidence/bench_output artifacts/findings reports -maxdepth 2 | sort
