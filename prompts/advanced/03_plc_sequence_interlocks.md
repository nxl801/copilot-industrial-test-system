# Advanced Prompt 03 · PLC 顺控与联锁分析（plc-functional-verifier）

```text
请对 ${MODULE_PATH} 下的 PLC 逻辑做只读验证，不下载程序、不 force IO。

重点：
- mode 切换：manual / auto / maintenance / remote
- 状态机进入条件、退出条件、异常跳转
- permissives / interlocks / inhibits
- alarm trigger / reset / timeout
- startup defaults / power-loss recovery / retentive data

输出格式：
1. state machine summary
2. permissives / inhibits matrix
3. 可能遗漏的负向测试
4. suspected defects
5. 需要采集的 tags / traces / logs
```
