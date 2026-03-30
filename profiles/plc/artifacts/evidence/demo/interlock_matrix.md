# Interlock Matrix (Demo) — 反应釜控制系统

> 本矩阵定义反应釜控制系统的联锁/允许/禁止条件。  
> 所有 Inhibit 类型条目为安全级，任何一项触发即强制禁止对应动作。

| # | Interlock ID | 类型 | Condition | Action | Expected | Status |
|---|---|---|---|---|---|---|
| 1 | IL-MOTOR-001 | Permissive | Safety_OK = TRUE AND Mode = AUTO | Motor enable allowed | allowed | demo |
| 2 | IL-PUMP-001 | Permissive | Tank_Level within [Low_Limit, High_Limit] | Pump start allowed | allowed | demo |
| 3 | IL-AGIT-001 | **Inhibit** | Mode = AUTO_RUNNING AND **Drain_Valve = OPEN** | **Agitator start INHIBITED; if running → immediate STOP** | inhibited | demo |
| 4 | IL-AGIT-002 | **Inhibit** | Safety_OK = FALSE | ALL motors inhibited (including agitator) | inhibited | demo |
| 5 | IL-DRAIN-001 | **Inhibit (反向)** | Agitator_Running = TRUE | **Drain valve OPEN inhibited** (对称互锁) | inhibited | demo |
| 6 | IL-ESTOP-001 | Safety Chain | E-Stop_Active = TRUE | ALL outputs de-energized; retentive latch EStop_Flag | emergency | demo |

## 规则说明
- **Permissive**: 必须满足才允许动作执行（AND 逻辑）
- **Inhibit**: 任意一项为 TRUE 即绝对禁止动作（OR 逻辑）
- **Safety Chain**: 最高优先级，直接切断所有输出
- 第 3 项（IL-AGIT-001）与第 5 项（IL-DRAIN-001）构成对称互锁：排污阀开 ↔ 搅拌运行 互斥
