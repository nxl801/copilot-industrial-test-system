# Public-safe Audit

## Audit goals
- no secrets
- no internal URLs
- no customer names
- no production topology
- no real screenshots / scan bundles / credentials

## Checklist
- [ ] Search for internal hostnames / IPs
- [ ] Replace any example MCP domains with obvious public placeholders such as `*.example`
- [ ] Search for secrets / tokens / env files
- [ ] Search for real customer identifiers
- [ ] Confirm all MCP stubs are demo-safe
- [ ] Confirm README / SECURITY do not overclaim production readiness
- [ ] Confirm demos only use synthetic artifacts
