# Repo Profiles

## HMI Repo

### Keep
- test-plan-architect
- industrial-test-orchestrator
- hmi-e2e-verifier
- security-62443-assessor
- vuln-scan-triage
- evidence-synthesizer

### Drop by default
- plc-functional-verifier
- motion-drive-verifier
- io-module-verifier
- hardware-bench-coordinator (unless there is a real panel / IPC bench)

### Add dirs
- ui-map/
- alarm-catalog/
- fixtures/
- artifacts/screenshots/
- artifacts/traces/
- artifacts/reports/

## PLC / Logic Repo

### Keep
- test-plan-architect
- industrial-test-orchestrator
- plc-functional-verifier
- io-module-verifier
- motion-drive-verifier (if servo/VFD controlled)
- hardware-bench-coordinator
- evidence-synthesizer
- security-62443-assessor (if network exposed)

### Drop by default
- hmi-e2e-verifier

### Add dirs
- sim/
- tagmaps/
- alarm-matrix/
- bench/
- artifacts/plc/
- artifacts/motion/
- artifacts/io/
- artifacts/reports/

## Security Repo

### Keep
- test-plan-architect
- industrial-test-orchestrator
- security-62443-assessor
- vuln-scan-triage
- evidence-synthesizer

### Drop by default
- hardware-bench-coordinator
- plc-functional-verifier
- hmi-e2e-verifier
- motion-drive-verifier
- io-module-verifier

### Add dirs
- scans/nessus/
- scans/burp/
- scans/defensics/
- threat-model/
- evidence/62443/
- reports/
