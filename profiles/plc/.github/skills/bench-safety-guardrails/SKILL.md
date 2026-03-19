---
name: bench-safety-guardrails
description: Safety guardrails for tasks involving real benches, PLC download, power cycle, force IO, servo enable, or motion.
user-invocable: false
---

# Bench Safety Guardrails

1. Confirm bench lock, station id, build id, and hardware revision.
2. Verify E-stop / STO / safe state / rollback path before physical action.
3. Never run physical actions in parallel on the same bench.
