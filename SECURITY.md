# Security Policy

## Scope
This repository contains templates, prompt packs, MCP stubs, and demo-safe examples for industrial automation testing workflows.
It is not intended to directly control production or safety-critical systems.

## Security expectations
- Do not commit secrets, tokens, internal URLs, customer identifiers, or private scan bundles
- Keep real bench actions disabled by default
- Require explicit human approval for any integration that can affect hardware state
- Prefer server-side allowlists and policy enforcement for dangerous MCP tools

## Reporting
If you identify a risky default, dangerous tool exposure, or a workflow that could unintentionally enable unsafe hardware actions, open a security issue or contact the maintainers privately before broad disclosure.
