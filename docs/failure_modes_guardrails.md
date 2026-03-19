# Failure Modes and Guardrails

## Real bench misfire
- Missing `tools` in agent frontmatter -> reject in review/CI
- Bench agent auto-invoked by another agent -> use `user-invocable: true` + `disable-model-invocation: true`
- `/fleet` tries hardware actions -> do not expose `labctl/*`, `plcctl/*`, `motionctl/*` in CLI session
- Bench lock only enforced by prompt -> add hook or server-side lock validation

## Evidence-free PASS
- Missing evidence path -> output `INSUFFICIENT EVIDENCE`
- Missing build id / hw revision / timestamp -> block report
- Triage overclaims -> split into confirmed / likely / needs verification / false positive / compensating control

## Agent / model drift
- Generic agent naming -> use strong semantic names
- Too many subagents -> phase-2 `agents:` whitelist
- Windows MCP sandbox assumption -> do server-side allowlist instead
- Hardcoded API keys -> use env vars / input variables
