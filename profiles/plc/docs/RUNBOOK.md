# PLC Profile RUNBOOK

## Purpose
用于 PLC / 控制逻辑 / 联动工位相关仓库的 Copilot 多智能体协作规范。

## Bench Approval Flow
1. 先由 `test-plan-architect` 和 `plc-functional-verifier` 完成只读分析。
2. 若需要真实工位动作，只能形成 serialized action queue。
3. 只有人在明确切换到 `hardware-bench-coordinator` 后，才允许进入 bench 流程。
4. bench lock、station id、安全状态、回滚路径缺任一项时，输出 `BLOCKED`。
5. 所有 bench 动作必须记录 artifact path。

## Hard Rules
- 禁止把 bench 动作交给 `/fleet`
- 禁止无 lock 执行真实动作
- 没有证据不能输出 PASS
