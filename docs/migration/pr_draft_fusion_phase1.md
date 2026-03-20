# PR Draft - Fusion Phase 1

## Title

`docs: add first-phase fusion layer from industrial-copilot-template`

## Summary

This PR introduces the first structured fusion layer from `industrial-copilot-template` into `copilot-industrial-test-system`.

The goal is not to merge two repository shapes wholesale.
Instead, this PR keeps the current public-safe repository skeleton as the canonical base, then imports the most reusable testing-method assets:
- testcase governance
- starter schemas
- workflow chain documentation
- protocol capability-pack scaffolding
- deeper Modbus and OPC UA prompt contracts

## Why

The target repository already had a strong public-safe orchestration skeleton.
What it lacked was a fuller testing-engineering chain from:
- spec
- requirement
- testcase
- coverage audit
- automation triage
- evidence

This PR starts closing that gap without weakening the repository's safety posture.

## Included changes

### Planning and migration docs
- add source-to-target fusion map
- add initial fusion backlog
- add branch progress tracking

### Governance
- add canonical testcase naming rules
- add canonical dedup rules

### Schemas
- add starter schemas for:
  - requirement
  - testcase
  - evidence pack
  - coverage matrix

### Workflows
- add docs for:
  - spec -> requirement -> testcase
  - parallel testcase generation
  - automation triage

### Capability packs
- add HMI / PLC / Modbus / OPC UA capability-pack READMEs
- deepen HMI with:
  - requirement-to-testcases prompt contract
  - example flow
- deepen PLC with:
  - requirement-to-testcases prompt contract
  - example flow
- deepen Modbus with:
  - requirement-to-testcases prompt contract
  - testcase-to-pytest prompt contract
  - example flow
- deepen OPC UA with:
  - requirement-to-testcases prompt contract
  - testcase-to-pytest prompt contract
  - example flow

### Entrypoints
- update README to surface fusion additions
- update ROADMAP to reflect the new fusion track

## Explicit non-goals

This PR does not:
- add direct bench control
- add risky real-device automation examples
- claim production readiness
- merge old and new role taxonomies side by side
- import private or customer-specific assumptions

## Review focus

Please review for:
1. clarity of the canonical repository direction
2. consistency between governance, schema, and workflow docs
3. public-safe framing of protocol capability packs
4. whether Modbus and OPC UA are deep enough for a first-phase merge
5. whether HMI / PLC should stay README-only in this phase

## Follow-up candidates

- deepen HMI and PLC capability packs
- add canonical role map and output contracts
- connect capability packs to reusable examples and script templates
- mirror key fusion additions in `README.zh-CN.md`
