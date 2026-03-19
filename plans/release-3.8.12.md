# Release 3.8.12 Test Plan

## Scope

- PLC 顺控与 HSC
- HMI 报警与配方
- 伺服回零与过载恢复
- 安全验证：IEC 62443-4-2 证据、threat model、Nessus / Burp / Defensics 结果

## Assumptions

- 当前版本已具备可执行的实验室环境
- Bench 为独占资源，需要串行调度
- 安全验证优先做 evidence mapping 与 scan triage，再决定是否进入真实执行

## Parallel Read-only Analysis

- `plc-functional-verifier`
  - PLC 状态机、联锁、报警、HSC 边界
- `hmi-e2e-verifier`
  - HMI 登录、导航、报警、配方、操作联锁
- `motion-drive-verifier`
  - 伺服 / 变频器参数差异、trace、fault history
- `security-62443-assessor`
  - threat model、IEC 62443-4-2 requirement/evidence mapping
- `vuln-scan-triage`
  - Nessus / Burp / Defensics finding normalization

## Serialized Bench Actions

由 `hardware-bench-coordinator` 独占执行：

1. 确认 bench lock / station id / build id / hardware revision
2. 检查 E-stop / STO / safe state
3. 采集基线日志与参数快照
4. 必要时执行上电 / 下载 / force IO / drive enable / homing
5. 采集动作后的日志、trace、截图、差异

## Evidence Requirements

- PLC tags / state transition evidence
- HMI screenshots / page paths / repro steps
- Motion trace / parameter diff / fault history
- Nessus / Burp / Defensics normalized findings
- IEC 62443-4-2 requirement -> evidence mapping matrix
- Final defect list and evidence index

## Exit Criteria

- 高优先级功能缺陷已归类
- 安全 gap 与 residual risk 明确
- 串行 bench 动作已完成并可追溯
- 报告具备 Go / No-Go / Conditional Go 判定依据
