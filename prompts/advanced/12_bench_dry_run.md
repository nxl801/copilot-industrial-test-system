# Advanced Prompt 12 · bench dry-run（hardware-bench-coordinator）

```text
先做 dry-run，不执行真实动作。

目标：
为 ${STATION_ID} 上的 ${PRODUCT_NAME} / build ${BUILD_ID} 生成最小化 serialized action queue，用于验证：
- 上电后初始化
- PLC 与 IO 通讯状态
- 伺服 enable 前置条件
- 报警读取
- 日志采集

约束：
- 不调用任何执行型工具
- 如果 bench lock、安全状态、回滚路径缺失，立即输出 BLOCKED
- 输出应包含：preconditions、step-by-step queue、stop conditions、artifacts to collect、rollback notes
```
