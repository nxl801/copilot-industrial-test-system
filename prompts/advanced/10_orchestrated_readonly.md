# Advanced Prompt 10 · 总控并行分析（industrial-test-orchestrator）

```text
针对 build ${BUILD_ID}，请只做并行只读分析，不执行真实工位动作。

范围：
- PLC 顺控与 HSC
- HMI 报警与配方
- 伺服回零与故障恢复
- IEC 62443-4-2 证据映射
- scan triage

要求：
- 使用合适的只读 subagents 并行分析
- 不要调用 hardware-bench-coordinator
- 如果某项必须上 bench，只输出 serialized action queue

最终输出：
- parallel findings
- cross-module conflicts
- required bench actions
- evidence gaps
- go / no-go / conditional go
```
