# Prompt 05 · 证据汇总与报告生成

```text
使用 @evidence-synthesizer 汇总所有子代理的结果并生成报告：
1. 合并 PLC、HMI、伺服/变频器、IO 模块和安全验证的分析结果，保持 requirement -> test -> result -> artifact -> defect 的可追溯性。
2. 生成一个统一的 Markdown 格式的测试报告，包含以下内容：
   - 测试范围和假设
   - 并行执行的分析结果
   - 串行硬件操作的执行情况
   - 风险/阻塞项
   - 证据路径和修复计划
   - Go / No-Go / Conditional Go 判定
```
