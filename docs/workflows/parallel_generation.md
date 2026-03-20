# Parallel Testcase Generation Workflow

This workflow describes how to split testcase generation into multiple focused lanes, then merge the outputs into one reviewed set.

## Summary

Parallel generation is recommended when the source material mixes multiple testing concerns, such as:
- nominal functionality
- negative and boundary behavior
- recovery and robustness
- security and permission checks
- observability and evidence expectations

The purpose is not just speed.
The main benefit is improved coverage quality.

## Recommended split dimensions

Default split for medium-complexity industrial specifications:
- functional
- negative-boundary
- recovery-robustness
- security-permission
- observability-evidence

Optional additional specialists when needed:
- HMI specialist
- PLC specialist
- Modbus specialist
- OPC UA specialist

## Inputs

Parallel generation should start only after:
- source intake is complete
- requirements have been extracted
- requirements have been normalized

Required artifacts:
- normalized requirement list
- scope notes
- exclusions
- known assumptions
- naming and dedup rules

## Output expectations per lane

Each lane should produce:
- testcase drafts
- explicit requirement references
- known assumptions
- unresolved questions
- evidence expectations when relevant

Draft IDs are allowed during this phase, but final IDs must be normalized later.

## Lane guidance

### Functional lane
Focus on:
- nominal success path coverage
- expected operator flow
- required system behavior under valid inputs

### Negative-boundary lane
Focus on:
- invalid input rejection
- unsupported operations
- out-of-range values
- malformed requests
- protocol exceptions

### Recovery-robustness lane
Focus on:
- reconnect behavior
- session recovery
- restart persistence
- degraded state handling
- timeout and retry behavior

### Security-permission lane
Focus on:
- authentication checks
- authorization failures
- role-based restrictions
- session expiration
- protocol or API misuse rejection

### Observability-evidence lane
Focus on:
- logging expectations
- alerts and audit records
- operator-visible indicators
- artifact capture requirements
- evidence sufficiency for pass/fail decisions

## Aggregation step

After lane outputs are produced, merge them into one combined candidate set.

At this stage:
- preserve original lane attribution if useful
- do not renumber immediately if review is still ongoing
- capture unresolved conflicts explicitly

## Coverage audit step

The coverage auditor should evaluate:
- whether each requirement is covered
- whether positive / negative / boundary / recovery / security / observability angles exist where relevant
- whether there are duplicate candidates
- whether evidence expectations are sufficient
- whether any requirement is still uncovered

Reference artifact:
- `schemas/coverage_matrix.template.yaml`

## Dedup and normalization

Use:
- `docs/governance/dedup_rules.md`
- `docs/governance/testcase_naming.md`

Rules:
- merge only materially equivalent cases
- preserve an audit trail for removed duplicates
- normalize final testcase IDs only after merge decisions are stable

## Human review gates

Escalate for human review when:
- two lanes disagree on expected behavior
- requirements appear internally inconsistent
- a candidate testcase may imply unsafe physical action
- a testcase seems to require real hardware but source context is incomplete
- lane outputs reveal unclear ownership of a protocol assumption

## Suggested artifacts

A healthy parallel-generation run should produce:
- combined testcase draft set
- coverage matrix
- duplicate decision log
- gap list
- follow-up recommendations

## Follow-up actions

Typical follow-up outcomes:
- run another focused lane for uncovered areas
- request clarification on ambiguous requirements
- move stable cases into automation triage
- hold unsafe or unclear cases for human review

## Anti-patterns

Do not:
- treat parallel generation as a license for uncontrolled testcase sprawl
- merge aggressively just to reduce count
- skip observability and evidence thinking
- let specialist lanes invent product behavior not supported by source material
- hide uncovered requirements because the generated set looks large
