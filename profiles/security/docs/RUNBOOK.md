# Security Profile RUNBOOK

## Purpose
用于 IEC 62443 / 漏扫 triage / threat model / 安全证据汇总仓库的 Copilot 多智能体协作规范。

## Rules
- 只做 threat model、evidence mapping、scan normalization、residual risk 和 retest planning。
- 不调用真实 bench 工具。
- findings 必须区分 confirmed / likely / needs verification / false positive / compensating control。
- 没有 evidence path 时，输出 `INSUFFICIENT EVIDENCE`。
