# MCP Server Contracts

## 1. labctl

### Purpose
统一封装真实工位相关动作，确保所有高风险物理操作均通过单一受控接口执行。

### Suggested Tools
- `reserve_bench(station_id, operator, ttl_minutes)`
- `release_bench(lock_id)`
- `power_cycle(station_id, profile)`
- `download_firmware(station_id, target, package_path)`
- `start_capture(station_id, channels)`
- `stop_capture(capture_id)`
- `set_io_pattern(station_id, module, pattern)`
- `read_alarm_log(station_id, since_ts)`
- `screenshot_panel(station_id, panel_id)`
- `send_panel_input(station_id, action, value)`

### Safety Rules
- No bench lock => deny
- Missing E-stop / STO readiness => deny
- Physical actions must be serialized per station

## 2. plcctl

### Purpose
处理 PLC 程序与逻辑分析相关的静态 / 仿真能力。

### Suggested Tools
- `build(project_path)`
- `diff_tags(old_export, new_export)`
- `export_state_machine(project_path)`
- `run_simulation(project_path, scenario)`
- `export_alarm_matrix(project_path)`

## 3. motionctl

### Purpose
统一处理伺服 / 变频器参数、trace、fault history 等能力。

### Suggested Tools
- `compare_parameters(before, after)`
- `read_trace(station_id, axis_id, window)`
- `export_fault_history(station_id, drive_id)`
- `run_profile(station_id, axis_id, profile_name)`

### Safety Rules
- Real motion requires bench coordinator approval
- Unsafe profile / missing limits => deny

## 4. scanparse

### Purpose
导入并归一化 Nessus / Burp / Defensics 等扫描结果。

### Suggested Tools
- `import_nessus(path)`
- `import_burp(path)`
- `import_defensics(path)`
- `deduplicate_findings(paths)`
- `rank_industrial_impact(findings)`

## 5. testmgmt

### Purpose
连接测试管理系统，沉淀 case / result / artifact / defect。

### Suggested Tools
- `create_case(title, component, priority)`
- `update_result(case_id, result, notes)`
- `attach_artifact(entity_id, path, type)`
- `create_defect_stub(summary, severity, evidence_paths)`

## Common Return Shape

建议所有 MCP tool 返回统一结构：

```json
{
  "ok": true,
  "tool": "reserve_bench",
  "timestamp": "2026-03-19T12:00:00+08:00",
  "inputs": {},
  "artifacts": [],
  "warnings": [],
  "result": {}
}
```
