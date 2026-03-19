# Advanced Prompt 04 · PLC 掉电恢复与 HSC 边界（plc-functional-verifier）

```text
请基于当前 PLC 代码与配置，做“掉电恢复 + HSC 边界条件”专项分析。

重点：
- 上电初始化顺序
- retentive 变量是否会导致错误恢复
- HSC 是否存在 overflow、edge loss、window timing 问题
- timer / counter / latch 是否存在竞态或异常复位
- 报警与计数值是否可能在电源波动后不一致

约束：
- 只做静态与仿真分析
- 任何需要真实工位动作的内容，只输出 serialized action queue

输出：
- 风险矩阵
- 必测边界用例
- 需要 bench 验证的最小动作集
```
