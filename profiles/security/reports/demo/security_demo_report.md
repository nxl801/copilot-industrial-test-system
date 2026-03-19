# Security Demo Report

## Summary
- Build: demo-sec-001
- Scope: IEC 62443 mapping, scan normalization, residual risk
- Verdict: Conditional Go

## Threat Model Summary
- Assets: controller web UI, maintenance endpoint, engineering workstation path
- Interfaces: HTTPS, maintenance service, update package path
- Trust boundaries: operator LAN, engineering zone, update source

## Findings
| ID | Severity | Category | Summary | Evidence |
|---|---|---|---|---|
| SEC-001 | High | Auth | Default credential verification remains open | artifacts/findings/demo/normalized_findings.json |
| SEC-002 | Medium | Evidence | Session timeout evidence missing | artifacts/evidence/demo/62443_matrix.md |

## Residual Risk
- Missing session timeout validation
- Maintenance endpoint still pending verification
