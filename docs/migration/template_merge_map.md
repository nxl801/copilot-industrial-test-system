# Template Fusion Map

Branch: `chore/repo-fusion-plan`

## Summary

This document maps reusable assets from `industrial-copilot-template` into the target public repository `copilot-industrial-test-system`.

Recommended strategy:
- keep `copilot-industrial-test-system` as the canonical repository skeleton
- import high-value generation and governance assets from `industrial-copilot-template`
- avoid dual standards for naming, schema, agent roles, or artifact layout

## Target scope

- source repo: `industrial-copilot-template`
- target repo: `copilot-industrial-test-system`
- objective: merge method assets and testing intelligence into the public-safe orchestration skeleton

## Migration categories

### A. Migrate directly

| Source asset | Why it matters | Target location | Action | Risk note |
|---|---|---|---|---|
| `governance/dedup-rules.md` | Strong testcase dedup rules after parallel generation | `docs/governance/dedup_rules.md` | Port with terminology aligned to target repo | Low |
| `governance/testcase-naming.md` | Stable testcase naming convention | `docs/governance/testcase_naming.md` | Port and extend for profiles / security cases | Low |
| `templates/requirement.schema.yaml` | Requirement normalization contract | `schemas/requirement.schema.yaml` | Import and adapt to public repo schema style | Low |
| `templates/testcase.schema.yaml` | Testcase output contract | `schemas/testcase.schema.yaml` | Import and align field names with target prompts | Low |
| `templates/evidence-pack.schema.yaml` | Evidence packaging contract | `schemas/evidence_pack.schema.yaml` | Import and align to current report flow | Low |
| `templates/coverage-matrix.template.yaml` | Traceability and coverage audit base | `schemas/coverage_matrix.template.yaml` | Import as starter matrix template | Low |
| `templates/test-report.template.md` | Shared reporting baseline | `reports/templates/test_report_template.md` | Port into target report template system | Low |
| `subagent-task-templates/*.md` | Good decomposition patterns for testcase parallelism | `prompts/subagent/` | Port with naming cleanup | Low |

### B. Migrate after refactor

| Source asset | Why it matters | Target location | Refactor needed | Risk note |
|---|---|---|---|---|
| Spec -> requirement -> testcase workflow from `README.md` and prompt set | Gives the target repo a full engineering chain, not just orchestration | `docs/workflows/spec_to_requirement_to_testcase.md` | Recast as stage-based workflow with explicit review gates | Medium |
| `.github/copilot/agents/*.agent.md` | Valuable role definitions | `.github/agents/` or `docs/agents/` | Normalize to one canonical role system and one output contract per agent | Medium |
| Protocol-specific prompt packs for HMI / PLC / Modbus / OPC UA | High-value domain knowledge | `prompts/protocols/` and `profiles/` | Split domain knowledge from task instructions and output contract | Medium |
| Automation triage flow | Bridges testcase design to scriptability | `docs/workflows/automation_triage.md` | Align with bench-safety constraints in target repo | Medium |
| Script generation prompts and templates | Useful for quick starts | `templates/scripts/` and `prompts/script_generation/` | Keep demo-safe defaults and avoid unsafe real-device assumptions | Medium |
| `governance/parallel-generation-playbook.md` | Good operator guidance for parallel generation | `docs/workflows/parallel_generation.md` | Rewrite around target repo orchestration model and validation scripts | Medium |

### C. Do not merge directly

| Source asset type | Why not merge directly | Recommended handling |
|---|---|---|
| Project-private assumptions embedded in prompts | Weakens public template neutrality | Extract to examples or leave out |
| Free-form long prompts mixing domain rules, workflow, and output format | Hard to maintain and validate | Decompose into knowledge + task + schema |
| Any workflow that implies direct bench action by default | Conflicts with demo-safe posture | Keep only as guarded future extension |
| Duplicate role names with different meanings | Creates operational ambiguity | Keep one canonical naming system |
| Any example that looks production-realistic without explicit safety disclaimers | Increases misuse risk | Convert to synthetic/demo-safe example only |

## Canonical design decisions

1. `copilot-industrial-test-system` remains the primary skeleton.
2. One naming system only.
3. One schema family only.
4. One role taxonomy only.
5. Old assets are imported as capability packs, not as a second repository structure.

## Proposed target structure

```text
copilot-industrial-test-system/
├─ docs/
│  ├─ governance/
│  │  ├─ dedup_rules.md
│  │  ├─ testcase_naming.md
│  │  └─ review_gates.md
│  ├─ migration/
│  │  └─ template_merge_map.md
│  └─ workflows/
│     ├─ spec_to_requirement_to_testcase.md
│     ├─ parallel_generation.md
│     └─ automation_triage.md
├─ prompts/
│  ├─ protocols/
│  │  ├─ hmi/
│  │  ├─ plc/
│  │  ├─ modbus/
│  │  └─ opcua/
│  ├─ subagent/
│  └─ script_generation/
├─ schemas/
│  ├─ requirement.schema.yaml
│  ├─ testcase.schema.yaml
│  ├─ evidence_pack.schema.yaml
│  └─ coverage_matrix.template.yaml
├─ reports/
│  └─ templates/
└─ profiles/
   ├─ hmi/
   ├─ plc/
   └─ security/
```

## Recommended execution order

### Phase 1: low-risk, high-value
1. import naming rule
2. import dedup rule
3. import requirement / testcase / evidence / coverage schemas
4. import subagent task templates
5. add migration note into repo docs

### Phase 2: workflow uplift
6. add spec -> requirement -> testcase workflow doc
7. add parallel generation workflow doc
8. add automation triage workflow doc
9. align target prompts to the new workflow chain

### Phase 3: protocol capability packs
10. extract Modbus prompt pack
11. extract OPC UA prompt pack
12. extract HMI / PLC specializations
13. align profile packs and examples

### Phase 4: agent normalization
14. map old agent roles to canonical target roles
15. unify output contracts
16. add validation checks where possible

## Acceptance criteria

A fusion pass is considered successful when:
- the target repo has one clear workflow from spec to report
- naming and dedup rules are explicit and reusable
- schemas exist for requirement, testcase, evidence, and coverage
- protocol-specific assets are discoverable without duplicating repository structure
- the public-safe posture remains intact
