# Copilot Usage Guide

## 推荐使用顺序

1. 先用 `test-plan-architect` 生成计划
2. 再交给 `industrial-test-orchestrator` 分拆并行分析与串行工位动作
3. 需要安全验证时，显式调用 `security-62443-assessor`
4. 需要报告时，统一调用 `evidence-synthesizer`
5. `/fleet` 只在 plan 明确后用于后台并行批处理

## 最小工作流

### Step 1 · 生成计划
- 使用：`prompts/01_test_plan_prompt.md`

### Step 2 · 调度子代理
- 使用：`prompts/02_orchestrator_prompt.md`

### Step 3 · 安全扫描与 62443 评估
- 使用：`prompts/03_security_triage_prompt.md`

### Step 4 · 工位动作
- 使用：`prompts/04_bench_execution_prompt.md`

### Step 5 · 证据与报告
- 使用：`prompts/05_evidence_report_prompt.md`

### Step 6 · 后台批处理
- 使用：`prompts/06_cli_fleet_prompt.md`

## 注意事项

- CLI `/fleet` 不要直接碰真实工位
- 真实工位动作必须串行并挂在 `hardware-bench-coordinator`
- 所有结论都要绑定 artifact path
- 无证据不宣称满足 IEC 62443-4-2
