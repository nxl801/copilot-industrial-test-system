# Fusion Progress - `chore/repo-fusion-plan`

## Summary

This document tracks what has already landed on the fusion branch and what remains for a reviewable first-phase merge.

## Completed in this branch

### Planning layer
- added `docs/migration/template_merge_map.md`
- added `docs/migration/initial_fusion_backlog.md`

### Governance layer
- added `docs/governance/testcase_naming.md`
- added `docs/governance/dedup_rules.md`

### Schema layer
- added `schemas/requirement.schema.yaml`
- added `schemas/testcase.schema.yaml`
- added `schemas/evidence_pack.schema.yaml`
- added `schemas/coverage_matrix.template.yaml`

### Workflow layer
- added `docs/workflows/spec_to_requirement_to_testcase.md`
- added `docs/workflows/parallel_generation.md`
- added `docs/workflows/automation_triage.md`

### Capability-pack layer
- added `prompts/protocols/hmi/README.md`
- added `prompts/protocols/plc/README.md`
- added `prompts/protocols/modbus/README.md`
- added `prompts/protocols/opcua/README.md`
- deepened Modbus with prompt contracts and example flow
- deepened OPC UA with prompt contracts and example flow

### Entrypoint layer
- updated `README.md`
- updated `ROADMAP.md`

## Current shape of the branch

The branch now provides:
- a documented fusion strategy
- canonical testcase governance starters
- starter schemas for requirement, testcase, evidence, and coverage
- workflow docs for the main engineering chain
- protocol capability-pack skeletons for four domains
- deeper prompt contracts for Modbus and OPC UA
- surfaced repository entrypoints for the fusion track

## What remains for first-phase review

Recommended remaining items before PR merge:
1. optionally link new docs from `QUICKSTART.md` or a dedicated docs index
2. optionally add HMI / PLC deeper prompt contracts for symmetry
3. decide whether README.zh-CN should mirror the new fusion track
4. create a review-oriented PR description

## What should stay out of phase 1

- direct bench-control integration
- production-realistic execution examples
- risky automation flows
- duplicated role systems
- private project assumptions

## Review recommendation

This branch is already reviewable as a first-phase documentation and structure fusion PR.
The next logical merge after this one would be:
- deeper HMI / PLC capability packs
- canonical role map
- reusable example/template linkage
