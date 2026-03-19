# Quickstart

## Prerequisites
- VS Code with GitHub Copilot enabled
- Python 3
- Optional: Node.js / npm for Playwright MCP

## 1. Open the repository
Open the repository root in VS Code.

## 2. Review safety docs
Read:
- `README.md`
- `SECURITY.md`
- `docs/public_release_checklist.md`

## 3. Explore the structure
- shared project skeleton: root
- profile packs: `profiles/hmi`, `profiles/plc`, `profiles/security`
- reusable prompts: `prompts/advanced`

## 4. Run the root demo
```bash
./scripts/demo_run.sh
```

## 5. Run profile demos
```bash
./profiles/hmi/scripts/demo_run.sh
./profiles/plc/scripts/demo_run.sh
./profiles/security/scripts/demo_run.sh
```

## 6. Run validation
```bash
python3 scripts/validate_profile_frontmatter.py
python3 scripts/check_dangerous_tool_exposure.py
python3 scripts/check_insufficient_evidence_rule.py
```

## 7. Pick a profile
- HMI → UI / alarm / screenshot-oriented work
- PLC → sequence / interlock / controlled bench workflow
- Security → IEC 62443 / scan triage / residual risk
