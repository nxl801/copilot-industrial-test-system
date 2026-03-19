# PLC Profile Usage

1. Generate plan with `test-plan-architect`
2. Use `plc-functional-verifier` for read-only sequence and interlock analysis
3. Use `hardware-bench-coordinator` only under explicit human control
4. Emit serialized bench action queues before any real hardware work
