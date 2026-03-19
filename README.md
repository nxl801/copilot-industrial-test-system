# copilot-industrial-test-system

A public-ready template repository for building GitHub Copilot multi-agent workflows for industrial automation testing.

It provides:
- a full multi-agent project skeleton
- HMI / PLC / Security profile packs
- advanced prompt packs
- MCP stub servers and demo-safe examples
- report, evidence, and validation templates
- minimal runnable demos

## What this repo is for

This repository is designed to help teams prototype and operationalize GitHub Copilot custom agents, skills, MCP-backed tools, and CLI `/fleet` workflows for industrial automation test scenarios such as:
- HMI regression and evidence capture
- PLC sequence / interlock analysis
- servo / VFD / IO boundary analysis
- IEC 62443-4-2 evidence mapping
- scan normalization and vulnerability triage

## Safety stance

This repository is intentionally conservative:
- real bench actions are disabled by default
- dangerous tool exposure should be validated
- evidence-free PASS is forbidden
- demos use synthetic / placeholder artifacts

## Repository layout

- `.github/` — shared Copilot instructions, agents, skills
- `.vscode/` — VS Code settings and MCP configuration
- `prompts/` — reusable prompt packs
- `plans/` — sample plans
- `reports/` — shared report templates
- `tools/mcp/` — demo-safe MCP stubs
- `profiles/` — HMI / PLC / Security slim packs
- `artifacts/` — example evidence / findings / logs
- `scripts/` — validation and demo helpers
- `docs/` — rollout, packaging, validation, and public release docs

## Quick start

1. Read `QUICKSTART.md`
2. Run the root demo:
   ```bash
   ./scripts/demo_run.sh
   ```
3. Run a profile demo:
   ```bash
   ./profiles/hmi/scripts/demo_run.sh
   ./profiles/plc/scripts/demo_run.sh
   ./profiles/security/scripts/demo_run.sh
   ```
4. Validate the repository:
   ```bash
   python3 scripts/validate_profile_frontmatter.py
   python3 scripts/check_dangerous_tool_exposure.py
   python3 scripts/check_insufficient_evidence_rule.py
   ```

## Public publishing note

Before publishing publicly, review:
- `docs/public_release_checklist.md`
- `docs/profile_packaging_guide.md`
- `SECURITY.md`

## Status

This repository is a template and demo pack, not a production lab controller.
Any real bench integration should be added behind explicit human approval and server-side policy.
