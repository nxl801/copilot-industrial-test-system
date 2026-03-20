# PLC Capability Pack

This pack defines how the repository should approach PLC-oriented requirement extraction, testcase generation, automation triage, and evidence capture.

## Purpose

Use this pack when the target scope includes:
- PLC communication behavior
- sequence or interlock logic verification planning
- parameter validation
- restart and recovery behavior
- permission or role constraints around PLC access
- evidence collection tied to controller state and logs

## Source lineage

This pack is derived from reusable assets in `industrial-copilot-template`, especially:
- PLC protocol requirement extraction patterns
- PLC testcase-to-pytest generation patterns
- PLC-Modbus flow examples

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

Typical PLC coverage should consider:
- communication success and rejection paths
- state transition logic
- restart persistence or recovery behavior
- parameter boundary validation
- interlock-related conditions
- logging and diagnostics
- evidence traceability to the originating requirement

## Suggested evidence

Common evidence types:
- protocol traces
- PLC diagnostics or event logs
- state snapshots
- parameter export or before/after comparison
- operator confirmation notes when hardware context matters

## Safety and boundary notes

Do not assume that real PLC writes are safe in a generic template.
Avoid generating direct control logic execution flows without explicit environment and approval context.
When safety logic or physical outputs are involved, bias toward manual or supervised paths.

## Example outputs this pack should support

- normalized PLC requirements
- PLC-focused testcase drafts
- safe script skeleton candidates for communication-oriented checks
- evidence pack requirements for controller and log validation

## Related repository paths

- `docs/workflows/spec_to_requirement_to_testcase.md`
- `docs/workflows/parallel_generation.md`
- `docs/workflows/automation_triage.md`
- `schemas/testcase.schema.yaml`
- `schemas/evidence_pack.schema.yaml`
