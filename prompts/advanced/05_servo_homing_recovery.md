# Advanced Prompt 05 · 伺服回零与故障恢复（motion-drive-verifier）

```text
请对 ${AXIS_NAME} 的伺服逻辑做只读验证。

重点：
- servo enable 条件
- homing / re-homing / interrupted homing
- positive / negative limits
- following error、encoder fault、comm loss、overload 后的恢复逻辑
- parameter drift after firmware/config changes

约束：
- 不执行真实运动
- 只输出 trace checks、fault-history checks、required bench actions

输出：
1. homing risk points
2. fault recovery cases
3. parameter diff hotspots
4. required artifacts
5. bench action queue（如果确实需要）
```
