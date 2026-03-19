# 实施计划

## 已完成

- 方案全文抓取并归档
- Obsidian 落库
- 项目骨架初始化
- `.github/copilot-instructions.md`
- 10 个 agent 模板
- 6 个 skill 模板
- `.vscode/settings.json`
- `.vscode/mcp.json`
- hooks / findings 脚本占位

## 下一阶段

1. 把 agent 与 skill 按产品线再细化一层（HMI / PLC / Drive / IO / Security）
2. 设计真实 MCP server 契约：`labctl`, `plcctl`, `motionctl`, `scanparse`, `testmgmt`
3. 生成示例 `plans/release-3.8.12.md`
4. 生成示例 `/fleet` 批处理 prompt
5. 补充工位锁、证据校验、finding 归一化脚本的真实实现
6. 视需要补一个 `prompts/` 目录，沉淀可直接复用的 Copilot 提示词模板
