# HMI Profile RUNBOOK

## Purpose
用于 HMI / Web UI / panel 相关仓库的 Copilot 多智能体协作规范。

## Rules
- 默认只做只读分析、截图设计、证据索引。
- 不直接触发真实 bench 动作。
- 若需要设备侧验证，只输出 serialized action queue。
- 没有证据时写 `INSUFFICIENT EVIDENCE`。
