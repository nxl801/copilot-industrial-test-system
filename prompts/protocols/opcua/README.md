# OPC UA Capability Pack

This pack defines how the repository should approach OPC UA-oriented requirement extraction, testcase generation, automation triage, and evidence capture.

## Purpose

Use this pack when the target scope includes:
- endpoint connectivity
- browse and read behavior
- unauthorized write rejection
- session lifecycle handling
- authentication and authorization checks
- namespace and node access behavior
- auditability and evidence expectations

## Source lineage

This pack is derived from reusable assets in `industrial-copilot-template`, especially:
- OPC UA requirement-to-testcase prompting
- OPC UA testcase-to-pytest generation patterns
- browse / read flow examples

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

Typical OPC UA coverage should consider:
- endpoint discovery
- secure session establishment
- browse and read behavior
- unauthorized write rejection
- role or permission restrictions
- session timeout and expiration
- reconnect and recovery behavior
- audit log or event generation
- protocol observability and client-side evidence

## Suggested evidence

Common evidence types:
- client request and response traces
- endpoint and session metadata
- server-side logs where available
- security event records
- state snapshots relevant to the accessed node set

## Safety and boundary notes

Do not assume write permissions.
Do not infer namespace semantics when the source material is incomplete.
If node mutability or privilege scope is unclear, keep the testcase read-first and mark the write path for clarification.

## Example outputs this pack should support

- normalized OPC UA requirements
- OPC UA-focused testcase drafts
- safe script skeleton candidates
- evidence pack requirements for access and session validation

## Related repository paths

- `docs/workflows/spec_to_requirement_to_testcase.md`
- `docs/workflows/parallel_generation.md`
- `docs/workflows/automation_triage.md`
- `schemas/testcase.schema.yaml`
- `schemas/evidence_pack.schema.yaml`
