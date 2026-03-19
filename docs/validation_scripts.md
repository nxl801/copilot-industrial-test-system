# Validation Scripts

- `scripts/validate_profile_frontmatter.py`
  - 检查 profile agents 是否缺少 `name` / `description` / `tools`
- `scripts/check_dangerous_tool_exposure.py`
  - 检查非 bench agent 是否错误暴露 `labctl/*` / `plcctl/*` / `motionctl/*`
- `scripts/check_insufficient_evidence_rule.py`
  - 检查主项目与各 profile 的 `copilot-instructions.md` 是否包含 `INSUFFICIENT EVIDENCE` 规则
