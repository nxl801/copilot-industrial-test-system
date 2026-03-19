# Prompt 06 · Copilot CLI /fleet 批处理

```text
/fleet 根据 plans/release-3.8.12.md 执行以下并行任务：
1. Use @plc-functional-verifier to derive regression cases for PLC sequence, interlocks, alarms and HSC edge cases.
2. Use @hmi-e2e-verifier to generate HMI regression cases and screenshot evidence checklist.
3. Use @motion-drive-verifier to compare motion/drive parameters and produce trace-based checks.
4. Use @security-62443-assessor to map changed features to threat model and IEC62443 evidence gaps.
5. Use @vuln-scan-triage to normalize Nessus, Burp and Defensics findings from artifacts/security/.
6. Use @evidence-synthesizer to merge all outputs into reports/release-3.8.12-test-summary.md.
Do not execute physical bench actions in parallel. Any real bench action must be emitted as a serialized queue for @hardware-bench-coordinator only.
```
