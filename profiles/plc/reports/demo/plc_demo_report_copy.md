# PLC Demo Report

## Summary
- Build: demo-plc-001
- Scope: sequence logic, interlocks, startup defaults, HSC edge cases
- Verdict: Conditional Go

## Findings
| ID | Severity | Logic Area | Summary | Evidence |
|---|---|---|---|---|
| PLC-001 | High | Interlock | One interlock branch lacks explicit recovery note in evidence pack | artifacts/evidence/demo/interlock_matrix.md |
| PLC-002 | Medium | HSC | Overflow and edge-loss cases still require bench validation | artifacts/evidence/demo/hsc_boundary.md |

## Required Bench Actions
| Step | Preconditions | Action Queue | Artifact |
|---|---|---|---|
| 1 | lock + safe state | collect startup trace only | artifacts/logs/demo/serialized_bench_actions.csv |

## Gaps / Risks
- Bench validation still pending for HSC edge cases
- Startup recovery evidence is template-level only
