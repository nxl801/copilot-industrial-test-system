# Initial Fusion Backlog

Branch: `chore/repo-fusion-plan`

## Goal

Create a practical first wave of repository fusion work that can be finished incrementally without destabilizing the public-facing skeleton.

## Backlog

### P0 - establish canonical governance and schema layer

#### P0.1 Add testcase naming rule
- source: `industrial-copilot-template/governance/testcase-naming.md`
- target: `docs/governance/testcase_naming.md`
- deliverable:
  - naming spec committed
  - examples for HMI / PLC / Modbus / OPC UA / Security
- acceptance:
  - human readers can assign IDs consistently
  - future prompt packs can cite one canonical naming document

#### P0.2 Add testcase dedup rule
- source: `industrial-copilot-template/governance/dedup-rules.md`
- target: `docs/governance/dedup_rules.md`
- deliverable:
  - merge / non-merge criteria
  - required audit record for removed duplicates
- acceptance:
  - parallel generation outputs can be normalized consistently

#### P0.3 Import schema starters
- source:
  - `templates/requirement.schema.yaml`
  - `templates/testcase.schema.yaml`
  - `templates/evidence-pack.schema.yaml`
  - `templates/coverage-matrix.template.yaml`
- target: `schemas/`
- deliverable:
  - starter schema set with target-repo naming and comments
- acceptance:
  - all major artifacts have a documented structure
  - prompts and reports can reference the same schema family

#### P0.4 Add migration overview doc
- source: this fusion planning work
- target: `docs/migration/template_merge_map.md`
- deliverable:
  - source-to-target mapping
  - phased merge plan
- acceptance:
  - contributors can understand what is being merged and why

### P1 - add the missing engineering workflow chain

#### P1.1 Add spec -> requirement -> testcase workflow doc
- source: old repo README and prompt chain
- target: `docs/workflows/spec_to_requirement_to_testcase.md`
- deliverable:
  - stage-by-stage flow
  - required inputs and outputs
  - review gates
- acceptance:
  - target repo no longer reads as orchestration-only

#### P1.2 Add parallel generation workflow
- source:
  - `subagent-task-templates/*.md`
  - `governance/parallel-generation-playbook.md`
- target: `docs/workflows/parallel_generation.md`
- deliverable:
  - recommended split dimensions
  - aggregation and audit rules
- acceptance:
  - contributors can reproduce parallel testcase generation safely

#### P1.3 Add automation triage workflow
- source: old repo process definition
- target: `docs/workflows/automation_triage.md`
- deliverable:
  - auto / semi-auto / manual decision logic
  - safety caveats for industrial scenarios
- acceptance:
  - script generation is clearly gated and bounded

### P2 - extract reusable capability packs

#### P2.1 Add Modbus prompt pack
- source: old repo Modbus prompt set and templates
- target: `prompts/protocols/modbus/`
- acceptance:
  - prompt assets are protocol-specific and reusable
  - no unsafe device assumptions are baked in

#### P2.2 Add OPC UA prompt pack
- source: old repo OPC UA prompt set and templates
- target: `prompts/protocols/opcua/`
- acceptance:
  - prompt assets are reusable and public-safe

#### P2.3 Add HMI / PLC specialization packs
- source: old repo HMI / PLC prompt set
- target: `prompts/protocols/hmi/` and `prompts/protocols/plc/`
- acceptance:
  - specialization prompts are separated from generic orchestration prompts

### P3 - normalize role system

#### P3.1 Map old roles to canonical roles
- likely canonical target roles:
  - orchestrator
  - spec_analyst
  - requirement_extractor
  - testcase_designer
  - coverage_auditor
  - automation_triage
  - evidence_curator
- deliverable:
  - one role map document
  - one output contract per role
- acceptance:
  - no duplicate role names with conflicting responsibilities

#### P3.2 Align prompts and docs to the canonical role map
- deliverable:
  - references updated across docs and prompt packs
- acceptance:
  - repo terminology is consistent end to end

## Suggested working order for the next 1-3 days

### Day 1
- complete P0.1
- complete P0.2
- complete P0.3
- open a draft PR

### Day 2
- complete P1.1
- complete P1.2
- complete P1.3
- update README / roadmap references if needed

### Day 3
- start P2.1 and P2.2
- draft P3.1 role map
- identify examples to convert into demo-safe assets

## Out of scope for the first pass

- bench control integration
- production-realistic execution examples
- automatic device write flows
- private customer assumptions
- dual role systems kept for compatibility

## Definition of done for this branch

This branch is ready for review when:
- governance docs exist in the target repo
- starter schemas exist in the target repo
- fusion strategy is documented
- the missing workflow chain is documented
- follow-up capability extraction tasks are explicit and sequenced
