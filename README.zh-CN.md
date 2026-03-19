# copilot-industrial-test-system（中文说明）

[![Release](https://img.shields.io/github/v/release/nxl801/copilot-industrial-test-system)](https://github.com/nxl801/copilot-industrial-test-system/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Repo Status](https://img.shields.io/badge/status-demo--safe-blue)](./SECURITY.md)

这是一个面向**工业自动化测试场景**的 GitHub Copilot 多智能体模板仓库，适合用来构建和演示以下能力：

- HMI 回归测试与证据整理
- PLC 顺控 / 联锁 / HSC 等逻辑分析
- 伺服 / 变频器 / IO 边界场景分析
- IEC 62443-4-2 证据映射
- Nessus / Burp / Defensics 等扫描结果归一化与 triage
- GitHub Copilot custom agents、skills、MCP、CLI `/fleet` 的协同使用

## 这个仓库提供什么

仓库内包含：
- 一套完整的多智能体项目骨架
- HMI / PLC / Security 三套精简 profile
- 可直接复用的高级 prompts
- demo-safe 的 MCP stub 与最小演示闭环
- 报告模板、证据模板、RUNBOOK、校验脚本
- 面向 public repo 的发布文档和打包说明

## 适用场景

适合以下工作：
- 工业自动化产品测试流程的 AI 化试点
- GitHub Copilot 多 agent 工作流设计
- 工业测试证据结构与报告模板沉淀
- 安全验证 / 漏扫 triage / 62443 映射的协同模板化

## 安全边界

这个仓库默认采取保守策略：
- **默认不开放真实工位动作**
- **默认禁止无证据 PASS**
- **所有 demo 都使用合成/占位工件**
- **任何真实 bench 集成都应由人工审批 + 服务端策略保护**

也就是说：
> 这是一个模板仓库和演示仓库，不是现成可直接上生产的实验室控制系统。

## 仓库结构

- `.github/`：共享 Copilot instructions、agents、skills
- `.vscode/`：VS Code 设置与 MCP 配置
- `prompts/`：可复用 prompt 包
- `plans/`：示例计划
- `reports/`：共享报告模板
- `tools/mcp/`：demo-safe MCP stub
- `profiles/`：HMI / PLC / Security 三套瘦身包
- `artifacts/`：示例 evidence / findings / logs
- `scripts/`：demo 与校验脚本
- `docs/`：打包、发布、验证、演进文档

## 快速开始

### 1）先看文档
建议先读：
- `README.md`
- `README.zh-CN.md`
- `QUICKSTART.md`
- `SECURITY.md`

### 2）运行根级 demo
```bash
./scripts/demo_run.sh
```

### 3）运行 profile demo
```bash
./profiles/hmi/scripts/demo_run.sh
./profiles/plc/scripts/demo_run.sh
./profiles/security/scripts/demo_run.sh
```

### 4）运行校验脚本
```bash
python3 scripts/validate_profile_frontmatter.py
python3 scripts/check_dangerous_tool_exposure.py
python3 scripts/check_insufficient_evidence_rule.py
```

## 三套 profile 怎么选

### HMI profile
适合：
- 登录 / 导航 / 报警 / 配方 / 趋势 / 权限
- 截图证据、页面流、回归清单

### PLC profile
适合：
- 顺控、联锁、启动默认值、定时器/计数器/HSC
- bench action queue
- 串行工位动作审批流

### Security profile
适合：
- IEC 62443-4-2 映射
- threat model
- 扫描结果归一化
- residual risk 与 retest plan

## 发布到自己仓库时建议先看
- `docs/public_release_checklist.md`
- `docs/profile_packaging_guide.md`
- `docs/github_release_prep.md`
- `docs/demo_quickstart.md`

## 当前状态
当前仓库已经具备：
- public-ready 文档
- 最小可运行 demo
- profile 打包结构
- 校验脚本
- 首版 release

如果你要把它继续演化成真实团队内部使用版本，建议优先做：
1. 接入真实 MCP 服务端
2. 把危险动作策略放到服务端
3. 引入真实但脱敏后的 evidence schema
4. 为 profile 增加 CI 校验

## English
For the English version, see:
- `README.md`
