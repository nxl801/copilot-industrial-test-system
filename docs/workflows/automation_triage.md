# Automation Triage Workflow

This workflow defines how testcase candidates are classified into automation, semi-automation, or manual execution paths.

## Summary

Automation triage exists to answer a practical question:

> Which testcases should be automated, which should stay human-guided, and which must remain manual because the risk or context is too high?

For industrial scenarios, automation suitability is not just a tooling question.
It is also a safety and evidence question.

## Classification outcomes

### Auto
A testcase may be classified as `auto` when:
- the steps are deterministic
- the observability points are machine-capturable
- expected results are objective
- the environment is controlled enough for repeatable execution
- no unsafe real-device action is implied by default

### Semi-auto
A testcase should be classified as `semi-auto` when:
- some steps can be automated, but setup or validation still needs human confirmation
- visual confirmation is required
- the environment has partial uncertainty
- a device-side state transition requires operator supervision
- evidence capture can be automated, but the final judgment needs human review

### Manual
A testcase should remain `manual` when:
- the action is safety-sensitive
- the behavior depends on physical context not safely modeled in the template
- the hardware assumptions are incomplete
- the consequence of automation failure is too high
- required observations are not reliably automatable

## Inputs

Required inputs:
- normalized testcase set
- environment assumptions
- safety markings
- required observability
- evidence expectations

Helpful references:
- `schemas/testcase.schema.yaml`
- `schemas/evidence_pack.schema.yaml`

## Decision questions

For each testcase, ask:
1. Are the preconditions reliably reproducible?
2. Are the test steps deterministic enough for automation?
3. Are the expected results objective and machine-checkable?
4. Can the evidence be collected automatically?
5. Does the testcase touch safety-sensitive or motion-sensitive behavior?
6. Does it require real hardware or human judgment?
7. Would a failure mode of the script create unacceptable operational risk?

## Industrial safety defaults

Default to caution.

A testcase should not be promoted to `auto` by default if it involves:
- dangerous motion
- power-stage control
- emergency stop behavior
- STO or interlock behavior
- firmware update flows
- vendor-private register writes with unclear semantics
- irreversible configuration changes

When in doubt, use `semi-auto` or `manual`.

## Typical examples

### Good auto candidates
- login rejection for invalid credentials
- protocol read validation
- unsupported function code rejection
- session timeout verification with objective timestamps
- report or artifact structure validation

### Typical semi-auto candidates
- HMI visual indicator changes requiring operator confirmation
- restart or reconnection flows needing supervised setup
- partial automation with manual bench wiring or fixture changes
- evidence capture where human signoff is still required

### Typical manual candidates
- motor movement verification
- safety relay behavior
- emergency stop chain validation
- unknown real-device write paths
- timing-sensitive scenarios that could affect equipment availability

## Output contract

A triage result should record at least:
- testcase_id
- triage_result: `auto | semi-auto | manual`
- rationale
- blockers or assumptions
- required human approvals if any
- recommended execution path

## Human approval gates

Human approval is required before crossing from triage into execution when:
- real hardware interaction is needed
- safety-sensitive behavior is involved
- a script would change device state in a nontrivial way
- production-like equipment could be affected

## Handoff guidance

After triage:
- `auto` cases may move to script generation templates
- `semi-auto` cases should generate operator-assisted procedures and evidence checklists
- `manual` cases should generate controlled manual test instructions and evidence requirements

## Anti-patterns

Do not:
- classify a testcase as `auto` just because scripting is technically possible
- ignore the difference between observability and true verdict automation
- assume simulator-safe means hardware-safe
- convert high-risk bench actions into scripts without explicit approval and environmental controls

## Practical outcome

A good automation triage workflow creates:
- a realistic automation backlog
- a safe boundary around non-automatable scenarios
- a clearer path from testcase design into scripts, procedures, and evidence packs
