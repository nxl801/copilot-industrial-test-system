# Demo Run Guide

## Purpose
一键演示这套项目的最小闭环：
- 启动 MCP stub
- 执行 bench 相关 stub 动作
- 导入扫描样例
- 归一化 findings
- 生成演示报告副本

## Command

```bash
cd data/openclaw_cowork/copilot-industrial-test-system
./scripts/demo_run.sh
```

## Expected Outputs

- `scripts/output/*.json`
- `artifacts/evidence/bench_output/*.json`
- `artifacts/findings/*.json`
- `reports/demo_release_report.md`

## Notes
- 当前为 stub 演示，不连接真实实验室环境
- 后续可将 `labctl` 与 `scanparse` 替换为真实后端
