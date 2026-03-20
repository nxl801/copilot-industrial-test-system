# Testcase Dedup Rules

This document defines the canonical duplicate-handling rules for testcase sets produced by parallel generation or iterative refinement.

## Summary

Merge testcases only when they are materially equivalent.

## Merge only when all are materially equivalent

- same requirement intent
- same primary objective
- same preconditions or equivalent starting state
- same expected result
- same risk significance

## Prefer keeping the testcase that has

1. clearer traceability
2. more explicit observability
3. more precise failure expectation
4. better evidence requirements

## Do not merge if any of these differ materially

- one case is positive and another is negative
- one case is boundary-focused and the other is nominal
- one case is recovery-focused and the other is not
- one case requires real hardware and the other does not
- one case is safety-sensitive and the other is not
- one case validates audit or logging while the other does not

## Required audit record

For every removed duplicate, record:
- removed testcase id
- kept testcase id
- reason for merge

## Practical review guidance

When duplicate handling is uncertain:
- prefer keeping both candidates temporarily
- mark the ambiguity in the coverage audit output
- defer final merge until a human reviewer or coverage auditor resolves it

Do not merge aggressively just to reduce testcase count.
The goal is higher signal quality, not smaller output.

## Expected outputs

Coverage and normalization outputs should preserve:
- duplicate decisions
- retained canonical testcase ID
- rationale for removal
- any remaining coverage risk introduced by the merge
