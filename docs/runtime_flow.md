# Runtime Flow

## 1. Plan
- 输入变更范围、版本、模块、环境
- 使用 `test-plan-architect`
- 输出：`plans/<release>.md`

## 2. Orchestrate
- 使用 `industrial-test-orchestrator`
- 并行派发只读分析
- 把真实工位动作收敛成串行队列

## 3. Analyze
- PLC / HMI / Motion / IO / Security 各自输出 findings + evidence needs
- 漏扫走 `vuln-scan-triage`

## 4. Execute Bench
- 仅 `hardware-bench-coordinator` 可驱动真实工位
- 通过 hooks 验证 lock 与 artifact

## 5. Synthesize
- 使用 `evidence-synthesizer`
- 输出：`reports/release_test_summary_template.md` 的实例化版本

## 6. Review
- 人工审核 residual risk / blockers / retest items
- 生成最终 Go / No-Go / Conditional Go 判定
