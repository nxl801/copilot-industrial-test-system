---
name: bench-safety-guardrails
description: Safety guardrails for any task involving real benches, PLC download, power cycle, force IO, servo enable, motion run, STO or emergency-stop tests. Auto-load when prompts mention bench, station, power cycle, motion, commissioning, download, force IO, servo or drive.
user-invocable: false
---
# Bench Safety Guardrails

1. Confirm bench lock, station id, build id, hardware revision.
2. Verify E-stop / STO / safe state / rollback path before any physical action.
3. Prefer simulation, replay, diff and log analysis before real bench actions.
4. Never run physical actions in parallel on the same bench.
5. Record timestamp, action, expected result, actual result and artifact path.
6. Stop and request human review if any safety precondition is missing.
