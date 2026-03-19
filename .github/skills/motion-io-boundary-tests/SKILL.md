---
name: motion-io-boundary-tests
description: Boundary and timing tests for servo, drive, analog/digital IO and high-speed counters. Use when prompts mention homing, limits, trace, scaling, polarity, debounce, overflow, pulse or frequency.
user-invocable: false
---
# Motion and IO Boundary Tests

1. Enumerate min / max / nominal / invalid inputs.
2. Define expected timing window, tolerance and stop condition.
3. Verify fault handling, restart behavior and parameter drift.
4. For HSC and pulse signals, include overflow and edge-loss scenarios.
5. Output stimulus patterns, expected ranges and required trace/log artifacts.
