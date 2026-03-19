---
name: hmi-regression-evidence
description: Build reproducible HMI regression tests and screenshot evidence for login, alarms, recipes, trends and command interlocks. Use when prompts mention HMI, screen, alarm, recipe, trend, operator station or panel.
user-invocable: false
---
# HMI Regression Evidence

1. Map each user flow to page path, role, preconditions and expected UI state.
2. Require screenshots for every failed state and every critical confirmation page.
3. Validate stale bindings, refresh timing, localization and alarm acknowledgement flow.
4. For command pages, verify command interlocks against equipment state.
5. Output screenshot list, repro steps and evidence file naming.
