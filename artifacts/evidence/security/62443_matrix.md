# IEC 62443-4-2 Requirement / Evidence Matrix

| Requirement Area | Status | Evidence | Notes |
|---|---|---|---|
| Account / Auth | Partial | artifacts/evidence/security/default_credential_check.md | 默认口令检查未闭环 |
| Session / Timeout | Missing | - | 需补会话超时抓包与 UI 行为 |
| Logging / Audit | Partial | artifacts/evidence/logging/audit_placeholder.md | 需真实审计日志 |
| Update / Integrity | Missing | - | 需补升级包签名 / 校验链路 |
| Protocol Exposure | Partial | artifacts/findings/sample_normalized_findings.json | 需结合真实端口与服务枚举 |
