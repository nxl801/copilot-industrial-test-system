# HMI Capability Pack

This pack defines how the repository should approach HMI-oriented requirement extraction, testcase generation, automation triage, and evidence capture.

## Purpose

Use this pack when the target scope includes:
- login and session behavior
- UI navigation and state transitions
- role-based access restrictions
- operator-visible alarms or status changes
- form validation and configuration entry
- screenshot-oriented evidence collection

## Source lineage

This pack is derived from reusable assets in `industrial-copilot-template`, especially:
- HMI spec-to-testcase prompting
- HMI testcase-to-Playwright generation patterns
- HMI login flow examples

## Recommended workflow position

Use this pack after:
1. source intake
2. requirement extraction
3. requirement normalization

Then apply it during:
- testcase derivation
- parallel specialist generation
- automation triage
- evidence definition

## Core testcase angles

Typical HMI coverage should consider:
- valid and invalid login behavior
- role-based page or action visibility
- input validation and boundary conditions
- timeout and session expiration
- alarm or indicator visibility
- navigation consistency
- evidence screenshots and logs

## Suggested evidence

Common evidence types:
- screenshots
- UI event logs
- browser console or network logs when relevant
- exported configuration snapshots
- operator notes for visually verified outcomes

## Safety and boundary notes

Do not assume that visual pass criteria can always be judged automatically.
If a state change is operator-visible but not objectively machine-checkable, default toward semi-auto classification.
Avoid generating flows that imply dangerous device control through the HMI without explicit approval and environment context.

## Example outputs this pack should support

- normalized HMI requirements
- HMI-focused testcase drafts
- Playwright skeleton candidates for safe UI flows
- evidence pack requirements for screenshot and log capture

## Related repository paths

- `docs/workflows/spec_to_requirement_to_testcase.md`
- `docs/workflows/parallel_generation.md`
- `docs/workflows/automation_triage.md`
- `schemas/testcase.schema.yaml`
- `schemas/evidence_pack.schema.yaml`
