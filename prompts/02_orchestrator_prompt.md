# Prompt 02 · 调度子代理执行任务

```text
根据测试计划，请开始调度以下任务：
1. 并行执行以下只读分析任务：
   - 使用 @plc-functional-verifier 执行 PLC 程序逻辑、状态机、报警与时序分析。
   - 使用 @hmi-e2e-verifier 执行 HMI 的回归测试，包括登录、导航、报警与操作联锁。
   - 使用 @motion-drive-verifier 执行伺服与变频器的参数验证和运动行为分析。
   - 使用 @security-62443-assessor 执行 IEC 62443-4-2 安全评估，覆盖威胁建模、账户/认证、日志、更新完整性等验证。

2. 串行执行硬件操作任务：
   - 使用 @hardware-bench-coordinator 完成上电、固件下载、force IO 操作等串行硬件任务，确保不与其他任务并行执行。

3. 汇总结果并生成报告：
   - 使用 @evidence-synthesizer 汇总所有子代理的输出，生成最终的测试报告，包含缺陷列表、证据路径、Go/No-Go 判定。

请执行上述操作，并确保每个子代理在执行时都符合安全前置条件，如工位锁、E-stop、安全状态等。
```
