# Contributing

## Principles
- Keep demos safe by default
- Do not add real credentials, customer data, or production topology
- Prefer synthetic or placeholder artifacts in public branches
- Preserve the rule: no evidence -> `INSUFFICIENT EVIDENCE`

## Suggested workflow
1. Fork or branch
2. Make focused changes
3. Run validation scripts
4. Update docs when behavior changes
5. Open a PR with scope, rationale, and safety notes

## Before submitting
Run:
```bash
python3 scripts/validate_profile_frontmatter.py
python3 scripts/check_dangerous_tool_exposure.py
python3 scripts/check_insufficient_evidence_rule.py
```
