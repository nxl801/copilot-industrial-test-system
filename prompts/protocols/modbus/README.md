# Modbus Capability Pack

This pack defines how the repository should approach Modbus-oriented requirement extraction, testcase generation, automation triage, and evidence capture.

## Purpose

Use this pack when the target scope includes:
- Modbus TCP or RTU behavior
- request / response validation
- illegal function code handling
- illegal data address or value handling
- exception response behavior
- connection or reconnect robustness
- protocol observability and packet evidence

## Source lineage

This pack is derived from reusable assets in `industrial-copilot-template`, especially:
- Modbus requirement-to-testcase prompting
- Modbus testcase-to-pytest generation patterns
- Modbus invalid request flow examples

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

Typical Modbus coverage should consider:
- supported function behavior
- unsupported function code rejection
- invalid register or coil addressing
- out-of-range values
- malformed request handling
- timeout and reconnect behavior
- permission or write restriction behavior where applicable
- protocol-level observability
- diagnostic logging expectations

## Suggested evidence

Common evidence types:
- request packet capture
- response packet capture
- exception code capture
- controller or gateway logs
- state snapshot after the test

## Safety and boundary notes

Do not assume vendor-private register semantics.
Do not generate write-heavy or state-changing flows without clear scope and approval.
When device write behavior is uncertain, prefer:
- read-oriented checks
- simulator-safe examples
- TODO markers for human confirmation

## Example outputs this pack should support

- normalized Modbus requirements
- Modbus-focused testcase drafts
- pytest skeleton candidates for safe cases
- evidence pack requirements for protocol verification

## Related repository paths

- `docs/workflows/spec_to_requirement_to_testcase.md`
- `docs/workflows/parallel_generation.md`
- `docs/workflows/automation_triage.md`
- `schemas/testcase.schema.yaml`
- `schemas/evidence_pack.schema.yaml`
