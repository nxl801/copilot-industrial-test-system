# HMI Example Flow

## Example requirement fragment

```text
4.2.1 Engineering settings shall be protected by authentication.
4.2.2 Unauthorized users shall not be able to modify engineering parameters.
4.2.3 The system shall return to the login page after session timeout.
```

## Recommended sequence

1. requirement extraction and normalization
2. `prompts/protocols/hmi/requirement_to_testcases.md`
3. `docs/workflows/automation_triage.md`
4. HMI-oriented script generation or operator-assisted procedure generation
5. evidence pack generation
6. report generation

## Good automation candidates

- login page transition
- engineering settings access control
- session-timeout redirect to login

## Default non-auto candidates

- subjective display-quality judgments
- touch-feel or usability-only evaluations
- scenarios tightly coupled to real physical device behavior without safe lab context
