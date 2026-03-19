# Advanced Prompt 06 · 变频器参数差异与 fault history（motion-drive-verifier）

```text
请比较 ${OLD_PARAM_SET} 与 ${NEW_PARAM_SET}，并结合 ${FAULT_HISTORY_FILE} 做 VFD 风险分析。

重点：
- accel / decel / torque / current / freq limits
- trip / warning thresholds
- startup behavior after parameter changes
- communication timeout and fallback mode
- reset / restart semantics after faults

输出：
- 参数差异中最可能影响功能或安全的项
- 需要补测的 fault scenarios
- 高优先级 bench checks
- evidence needed
```
