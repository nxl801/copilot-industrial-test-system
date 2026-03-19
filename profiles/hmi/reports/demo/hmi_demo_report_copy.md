# HMI Demo Report

## Summary
- Build: demo-hmi-001
- Scope: login, alarm flow, recipe page, command interlock
- Verdict: Conditional Go

## Findings
| ID | Severity | Page/Flow | Summary | Evidence |
|---|---|---|---|---|
| HMI-001 | Medium | Login | Role matrix needs explicit screenshot evidence | artifacts/evidence/demo/login_role_matrix.md |
| HMI-002 | High | Alarm Ack | Alarm acknowledgement permission flow needs manual verification | artifacts/evidence/demo/alarm_ack_flow.md |

## Evidence
- artifacts/evidence/demo/login_role_matrix.md
- artifacts/evidence/demo/alarm_ack_flow.md
- artifacts/evidence/demo/screenshot_index.md

## Gaps / Blockers
- Real screenshot set not yet captured
- Recipe boundary input needs UI replay evidence
