# Testcase Naming Convention

This document defines the canonical testcase naming rule for `copilot-industrial-test-system`.

## Summary

Use this format:

```text
<DOMAIN>_<AREA>_TC_<NNN>
```

Examples:
- `HMI_AUTH_TC_001`
- `PLC_COM_TC_012`
- `MODBUS_NEG_TC_003`
- `OPCUA_SESS_TC_005`
- `SECURITY_TLS_TC_004`

## Field meanings

- `DOMAIN`
  - product, protocol, or capability domain
  - examples: `HMI`, `PLC`, `MODBUS`, `OPCUA`, `SECURITY`
- `AREA`
  - primary concern or validation area
  - examples: `AUTH`, `COM`, `CFG`, `SAFE`, `REC`, `LOG`, `UI`, `SESS`, `TLS`, `PERM`
- `TC`
  - fixed literal marker for testcase
- `NNN`
  - zero-padded sequence number within the domain-area scope

## Naming rules

1. Keep IDs stable once published into reports or evidence packs.
2. Prefer the dominant validation concern for `AREA`; do not encode every attribute into the ID.
3. Use uppercase snake-style segments.
4. Renumber only during the merge and normalization phase, not during early drafting.
5. The final merged set should be renumbered consistently by the orchestrator or coverage auditor.

## Drafting rule for parallel generation

Subagents may use temporary IDs while drafting.

Recommended temporary forms:
- `PLC_COM_DRAFT_FUNC_01`
- `MODBUS_NEG_DRAFT_03`
- `SECURITY_TLS_DRAFT_02`

Before final publication, draft IDs must be normalized into the canonical `*_TC_*` format.

## Domain examples

### HMI
- `HMI_UI_TC_001`
- `HMI_AUTH_TC_002`

### PLC
- `PLC_COM_TC_001`
- `PLC_SAFE_TC_002`

### Modbus
- `MODBUS_NEG_TC_001`
- `MODBUS_REC_TC_002`

### OPC UA
- `OPCUA_SESS_TC_001`
- `OPCUA_PERM_TC_002`

### Security
- `SECURITY_TLS_TC_001`
- `SECURITY_AUTH_TC_002`

## Related artifacts

This naming convention should be referenced by:
- testcase schemas
- coverage audit workflows
- report templates
- prompt packs that generate or normalize testcase IDs
