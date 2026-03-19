# Release 3.8.12 Test Summary

## Summary
- Release / Build: 3.8.12
- Product Family: HMI / PLC / Servo / Drive / IO
- Station / Environment: lab / bench-a01
- Overall Verdict: Conditional Go

## Scope
- PLC 顺控与 HSC
- HMI 报警与配方
- Servo 回零与过载恢复
- IEC 62443-4-2 证据映射
- Nessus / Burp / Defensics finding triage

## Assumptions
- 当前结果为演示闭环样例，不代表真实实验室执行结论
- Bench 操作日志为串行执行模板数据

## Parallel Findings
### PLC
- 状态机主流程可生成回归用例
- HSC 边界场景需要补一轮 overflow 与 edge-loss 复测

### HMI
- 登录、导航、报警确认流已形成用例模板
- 配方回写与越界提示仍需真实界面截图证据

### Motion / Drive
- 参数差异分析模板已具备
- 回零 trace 与 fault history 仍需真实采集

### IO
- AI/DI/DO/HSC 边界测试模板已建立
- 仍需真实 stimulus pattern 与 tolerance 数据

### Security
- 已形成 IEC 62443-4-2 evidence mapping 思路
- 默认口令 / 调试接口 / 会话超时等仍需真实证据支持

## Serialized Bench Actions
| Timestamp | Station | Action | Expected | Actual | Artifact |
|---|---|---|---|---|---|
| 2026-03-19T12:35:00+08:00 | bench-a01 | collect-baseline | baseline logs and params captured | placeholder | artifacts/evidence/baseline_capture.md |

## Findings
| ID | Severity | Domain | Summary | Evidence | Owner | Status |
|---|---|---|---|---|---|---|
| F-001 | High | Security | Maintenance endpoint default credential still enabled | artifacts/evidence/security/default_credential_check.md | Security | Open |
| F-002 | Medium | PLC | HSC overflow regression cases not yet validated on bench | artifacts/evidence/plc/state_machine_diff.md | PLC | Retest |

## Evidence Index
| Artifact Path | Type | Description |
|---|---|---|
| artifacts/evidence/plc/state_machine_diff.md | markdown | PLC 状态机差异分析 |
| artifacts/evidence/hmi/login_alarm_flow.png | screenshot | HMI 登录与报警确认流程截图 |
| artifacts/evidence/motion/axis1_trace.csv | trace | Axis1 回零 trace |
| artifacts/evidence/security/62443_matrix.md | matrix | IEC 62443-4-2 requirement/evidence mapping |

## Residual Risk
- 默认口令相关问题若真实存在，将直接影响 release 结论
- HSC 与 motion 相关边界场景尚未完成真实 bench 验证

## Retest Items
- HSC overflow / edge-loss
- HMI 配方越界提示截图
- Servo 回零 trace 实测
- Maintenance endpoint default credential check

## Recommendation
- 作为模板演示，本项目已具备从 plan -> findings -> evidence -> report 的闭环骨架
- 进入真实发布评估前，需接入真实 MCP 后端并完成实验室执行
