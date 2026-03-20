# PLC Example Flow

## Example requirement fragment

```text
4.2.3 The controller shall reject unsupported Modbus function codes and log an error event.
4.2.4 Invalid write requests shall not alter retained parameters.
```

## Recommended sequence

1. requirement extraction and normalization
2. `prompts/protocols/plc/requirement_to_testcases.md`
3. `docs/workflows/automation_triage.md`
4. PLC-oriented script generation or operator-assisted procedure generation
5. evidence pack generation
6. report generation

## Good automation candidates

- protocol request and response validation
- unsupported function code rejection
- parameter write validity checks in safe contexts
- diagnostic log verification

## Default non-auto candidates

- real hazardous outputs
- motion-related actions
- live process interactions coupled to production equipment
