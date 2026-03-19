# Advanced Prompt 02 · HMI 报警与权限专项（hmi-e2e-verifier）

```text
请审查 HMI 的报警与权限逻辑，只做只读分析。

输入上下文：
- alarm catalog: ${ALARM_FILE}
- UI map: ${UI_MAP}
- recent changes: ${CHANGE_SCOPE}

请重点检查：
- 报警是否分级显示
- 报警确认是否受角色控制
- 已清除 / 未确认 / 历史报警的状态流转
- 参数页是否存在越权写入风险
- HMI 命令是否可能在设备不满足联锁时仍可点击

输出：
- 风险点列表
- 复现步骤草案
- 建议截图点
- 需要 PLC / 设备侧补充验证的点
```
