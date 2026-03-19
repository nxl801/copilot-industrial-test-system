# Frontmatter Stability Guide

## Day-1 稳妥字段

优先使用：
- `name`
- `description`
- `tools`
- `user-invocable`
- `disable-model-invocation`
- 可选 `model`

## 原则

- 主 agent 若要调 subagent，`tools` 必须包含 `agent`
- 不要省略 `tools`，否则默认打开所有可用工具
- `argument-hint` 与 `handoffs` 更适合 VS Code 本地交互，不要把它们当成跨表面必需逻辑
- `agents` 白名单放到 phase-2 再启用
- `hooks` 有价值，但 day-1 不要把它当唯一护栏

## 推荐 bench agent 策略

```md
---
name: hardware-bench-coordinator
description: Human-invoked bench coordinator for serialized real-bench actions only.
tools: ['labctl/*', 'search']
user-invocable: true
disable-model-invocation: true
---
```

这样可以降低被其他 agent 自动调用的风险。
