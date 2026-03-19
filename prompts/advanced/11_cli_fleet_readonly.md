# Advanced Prompt 11 · CLI `/fleet` 只读批处理

```text
/fleet Analysis-only for build ${BUILD_ID}.

1. Use @plc-functional-verifier to analyze PLC sequence, interlocks, alarms, timers, counters, and HSC edge cases.
2. Use @hmi-e2e-verifier to derive HMI regression cases, screenshot checkpoints, and role/permission risks.
3. Use @motion-drive-verifier to compare parameter changes and propose trace-based checks.
4. Use @security-62443-assessor to map changed features to threat model and IEC 62443-4-2 evidence.
5. Use @vuln-scan-triage to normalize Nessus, Burp, and Defensics findings.
6. Use @evidence-synthesizer to merge all outputs into artifacts/reports/${BUILD_ID}-summary.md.

Constraints:
- Do not call any bench, PLC download, motion, or power tools.
- Any need for real hardware must be converted into a serialized action queue only.
- If evidence is missing, write INSUFFICIENT EVIDENCE instead of PASS.
```
