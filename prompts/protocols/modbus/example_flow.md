# Modbus Example Flow

## Example requirement fragment

```text
4.2.3 The controller shall reject unsupported Modbus function codes and log an error event.
4.2.4 Invalid write requests shall not alter retained parameters.
4.2.5 Requests targeting an illegal address shall return the appropriate exception response.
```

## Recommended sequence

1. requirement extraction and normalization
2. `prompts/protocols/modbus/requirement_to_testcases.md`
3. `docs/workflows/automation_triage.md`
4. `prompts/protocols/modbus/testcase_to_pytest.md`
5. evidence pack generation
6. report generation

## Good automation candidates

- unsupported function code rejection
- illegal address exception response
- invalid write request does not alter retained value
- timeout and reconnect behavior at the protocol layer

## Default non-auto candidates

- anything that could directly drive hazardous outputs
- write flows coupled to real machine movement
- scenarios with unknown vendor-private register meaning
