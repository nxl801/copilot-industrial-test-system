# PR Ready Checklist - Fusion Phase 1

Use this checklist before opening the PR for `chore/repo-fusion-plan`.

## Scope check
- [ ] This PR is documentation-and-structure focused
- [ ] No direct bench-control behavior was added
- [ ] No risky real-device automation examples were added
- [ ] No private customer assumptions were imported

## Content check
- [ ] Migration docs are present
- [ ] Governance docs are present
- [ ] Starter schemas are present
- [ ] Workflow chain docs are present
- [ ] Capability-pack docs are present for HMI / PLC / Modbus / OPC UA
- [ ] Modbus and OPC UA include prompt contracts and example flows
- [ ] HMI and PLC include minimum symmetry-layer assets

## Repository entrypoint check
- [ ] `README.md` references the fusion track
- [ ] `ROADMAP.md` references the fusion track
- [ ] Decide whether `README.zh-CN.md` should be updated in this PR or a follow-up PR

## Review framing
- [ ] Reviewers are told this is phase 1, not full convergence
- [ ] Non-goals are explicit in the PR body
- [ ] Follow-up items are listed clearly
