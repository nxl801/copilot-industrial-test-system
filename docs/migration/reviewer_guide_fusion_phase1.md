# Reviewer Guide - Fusion Phase 1

Use this guide to review `chore/repo-fusion-plan` quickly and in the intended order.

## What this PR is

This is a **phase-1 documentation and structure fusion PR**.

It brings reusable testing-method assets from `industrial-copilot-template` into `copilot-industrial-test-system` while keeping the current public-safe repository skeleton as the canonical base.

## What this PR is not

This PR does **not**:
- add direct bench control
- add risky real-device automation flows
- introduce production-ready execution claims
- merge two repository structures wholesale
- import private customer assumptions

## Fastest review order

If you want the fastest useful review, read in this order:

### 1. Direction and scope
- `docs/migration/template_merge_map.md`
- `docs/migration/pr_draft_fusion_phase1.md`

Review question:
- Is the repository direction clear: new repo as canonical skeleton, old repo as capability source?

### 2. Governance and artifact contract
- `docs/governance/testcase_naming.md`
- `docs/governance/dedup_rules.md`
- `schemas/requirement.schema.yaml`
- `schemas/testcase.schema.yaml`
- `schemas/evidence_pack.schema.yaml`
- `schemas/coverage_matrix.template.yaml`

Review question:
- Do naming, dedup, and starter schemas form a coherent baseline for testcase engineering?

### 3. Workflow chain
- `docs/workflows/spec_to_requirement_to_testcase.md`
- `docs/workflows/parallel_generation.md`
- `docs/workflows/automation_triage.md`

Review question:
- Does the repo now have a credible engineering chain from spec to testcase to triage?

### 4. Capability-pack layer
- `prompts/protocols/hmi/README.md`
- `prompts/protocols/plc/README.md`
- `prompts/protocols/modbus/README.md`
- `prompts/protocols/opcua/README.md`
- `prompts/protocols/hmi/requirement_to_testcases.md`
- `prompts/protocols/plc/requirement_to_testcases.md`
- `prompts/protocols/modbus/requirement_to_testcases.md`
- `prompts/protocols/modbus/testcase_to_pytest.md`
- `prompts/protocols/opcua/requirement_to_testcases.md`
- `prompts/protocols/opcua/testcase_to_pytest.md`

Review question:
- Are the protocol packs useful, scoped, and still public-safe?

### 5. Entrypoint surfacing
- `README.md`
- `ROADMAP.md`

Review question:
- Can a new contributor discover this fusion track from the repo entrypoints?

## Suggested review focus

Prioritize these decisions:
1. Is phase-1 scope appropriately limited?
2. Is the public-safe posture preserved?
3. Are the workflow and schema additions genuinely reusable?
4. Is Modbus / OPC UA deep enough for phase 1?
5. Is HMI / PLC symmetry sufficient for this phase?

## Suggested defer list

These are reasonable follow-ups and do not need to block this PR:
- deeper HMI capability pack contracts
- deeper PLC script-generation contracts
- canonical agent-role map
- README.zh-CN parity update
- tighter example/template linking

## One-line reviewer summary

Treat this PR as: **"establish the fusion foundation, not finish the fusion."**
