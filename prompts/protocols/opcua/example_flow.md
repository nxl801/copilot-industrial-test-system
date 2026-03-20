# OPC UA Example Flow

## Example requirement fragment

```text
5.1.1 The server shall expose the configured endpoint.
5.1.2 The client shall be able to browse the configured namespace.
5.1.3 Authenticated users may read process variables according to role permissions.
5.1.4 Invalid or unauthorized write operations shall be rejected.
```

## Recommended sequence

1. requirement extraction and normalization
2. `prompts/protocols/opcua/requirement_to_testcases.md`
3. `docs/workflows/automation_triage.md`
4. `prompts/protocols/opcua/testcase_to_pytest.md`
5. evidence pack generation
6. report generation

## Good automation candidates

- endpoint discovery
- browse path validation
- node read verification
- role-based read or write rejection
- reconnect and session timeout behavior

## Default non-auto candidates

- write operations that may trigger hazardous outputs
- control writes with unclear node semantics
- scenarios that rely on unverified privilege assumptions
