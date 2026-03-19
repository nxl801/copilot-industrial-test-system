# Advanced Prompt 01 · HMI 冒烟回归（hmi-e2e-verifier）

```text
针对 build ${BUILD_ID} 对 HMI 做一次只读回归设计与证据清单生成。

范围：
- 登录 / 注销
- 角色权限：operator / engineer / admin
- 报警列表、报警确认、历史报警
- 配方查看与下发
- 关键操作页的命令按钮与联锁显示

约束：
- 只做分析和测试设计，不执行真实工位动作。
- 如果需要浏览器自动化，只输出推荐的 Playwright case 列表与截图点。

输出：
1. 页面流与角色矩阵
2. 高风险回归用例（按优先级排序）
3. 每条用例需要的前置条件、输入、预期、截图点
4. evidence checklist
5. gaps / blockers
```
