# Demo Closed Loop

本项目已具备一个演示性质的闭环：

1. `plans/release-3.8.12.md`
   - 定义范围、并行分析、串行工位动作、证据需求

2. `artifacts/findings/sample_normalized_findings.json`
   - 作为漏洞扫描归一化样例输入

3. `artifacts/evidence/*`
   - 作为 evidence 占位与映射样例

4. `reports/release-3.8.12-test-summary.md`
   - 作为最终汇总报告样例

## 演示价值
- 展示 Copilot 多 agent 如何组织测试任务
- 展示 evidence-driven 报告结构
- 展示 MCP 工具层与 bench 串行执行如何衔接

## 下一步
- 用真实实验室输出替换样例 artifact
- 让 MCP stub 接真实系统
- 把 `evidence-synthesizer` 结果自动写入 `reports/`
