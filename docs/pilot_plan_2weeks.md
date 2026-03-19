# 2-Week Pilot Plan

## Team
- 1 Copilot / repo owner
- 1 domain expert (HMI or PLC)
- 1 bench owner or security owner
- optional 1 extra part-time member

## Milestones
- Day 1: M0 environment ready
- Day 2: M1 frontmatter stabilized
- Day 3-4: M2 read-only analysis working
- Day 5: M3 report template working
- Day 6-7: M4 CLI `/fleet` analysis-only parallelism
- Day 8: M5 bench dry-run
- Day 9-10: M6 single-bench controlled validation
- Day 11-12: M7 security triage working
- Day 13: M8 end-to-end demo
- Day 14: M9 go / no-go

## Acceptance Gates
- At least 8/10 core prompts produce usable structure on first run
- `/fleet` touches real bench tools exactly 0 times
- 100% of pass/fail/gap lines include artifact path
- No-evidence items must be marked `INSUFFICIENT EVIDENCE`
- Bench pilot limited to 1 bench, 1 product family, 1 build flow
