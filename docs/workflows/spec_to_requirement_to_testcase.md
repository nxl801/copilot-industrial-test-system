# Spec -> Requirement -> Testcase Workflow

This workflow defines the canonical engineering chain for turning industrial product specifications into reviewable testcase assets.

## Summary

Goal:
- extract testable requirements from source material
- normalize them into a stable requirement structure
- derive traceable testcases
- preserve review gates before automation or execution decisions

This workflow is intended for:
- HMI scenarios
- PLC scenarios
- industrial protocol scenarios such as Modbus and OPC UA
- security and evidence-oriented test planning

## Inputs

Typical source inputs:
- product specifications
- interface definitions
- protocol behavior descriptions
- acceptance criteria
- safety constraints
- known environment assumptions

## Outputs

The workflow should produce:
- normalized requirement records
- testcase records
- traceability references
- identified ambiguities
- a list of missing information that needs human clarification

## Stage 1 - source intake

Objective:
- collect the relevant source material before any testcase generation

Required actions:
- identify document source and version
- identify product or protocol scope
- identify environment assumptions
- identify safety-sensitive areas

Minimum recorded fields:
- source document name
- source revision if known
- target product or subsystem
- protocol or interface scope
- known exclusions

## Stage 2 - requirement extraction

Objective:
- convert raw spec statements into discrete, testable requirements

Good extraction behavior:
- one requirement per distinct intent
- retain source section traceability
- preserve uncertainty instead of guessing
- separate normative requirement text from analyst interpretation

Expected output shape:
- `requirement_id`
- `source_section`
- `requirement_summary`
- `requirement_text`
- `category`
- `observability`
- `needs_clarification`
- `ambiguity_reason`
- `notes_for_testing`
- `inferred_assumptions`

Review gate:
- if a requirement is too ambiguous to test responsibly, mark it for clarification instead of inventing behavior

## Stage 3 - requirement normalization

Objective:
- make extracted requirements structurally consistent before testcase generation

Normalization checks:
- duplicate requirements merged or cross-referenced
- vague language flagged
- category assigned consistently
- observability expectations recorded
- assumptions separated from requirements

Typical categories:
- interface_communication
- authentication
- authorization
- configuration
- recovery
- logging
- safety
- performance

## Stage 4 - testcase derivation

Objective:
- derive one or more testcases from each normalized requirement

Design principles:
- preserve traceability to the originating requirement
- cover nominal, negative, boundary, recovery, permission, and observability angles where relevant
- distinguish what is expected from what is merely inferred
- keep unsafe real-device assumptions out of generic templates

Expected testcase shape:
- `testcase_id`
- `requirement_id`
- `product_type`
- `module`
- `testcase_title`
- `objective`
- `preconditions`
- `test_steps`
- `expected_result`
- `priority`
- `required_observability`
- `evidence_needed`
- `safety_sensitive`
- `requires_real_hardware`
- `requires_visual_confirmation`
- `traceability`

## Stage 5 - quality review

Objective:
- review testcase quality before any automation triage or script generation

Review checklist:
- is every testcase tied to a requirement?
- are expected results observable?
- are evidence expectations explicit?
- are safety-sensitive cases marked?
- are assumptions called out clearly?
- are duplicate candidates visible?

Key references:
- `docs/governance/testcase_naming.md`
- `docs/governance/dedup_rules.md`
- `schemas/requirement.schema.yaml`
- `schemas/testcase.schema.yaml`

## Stage 6 - handoff to downstream workflows

After testcase derivation and review, the output can flow into:
- parallel generation expansion
- automation triage
- evidence pack generation
- report generation

## Human review gates

Human clarification is required when:
- a requirement statement is ambiguous
- the source conflicts internally
- safety-sensitive behavior is underspecified
- a testcase would imply real bench action by default
- protocol or device semantics are unknown

## Anti-patterns

Do not:
- jump directly from raw spec to script generation
- hide ambiguity in natural language prose
- treat inferred assumptions as confirmed behavior
- collapse multiple requirement intents into one testcase without justification
- optimize for testcase count instead of evidence quality

## Practical outcome

A good run of this workflow should leave the repository with:
- a stable requirement layer
- a stable testcase layer
- explicit traceability
- explicit uncertainty
- a clean handoff into coverage audit and automation triage
