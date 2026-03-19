---
name: scan-result-triage
description: Normalize Nessus, Burp Suite and Defensics outputs into actionable findings with deduplication, reachability and industrial impact assessment. Use when prompts mention scan, Nessus, Burp, Defensics, CVE, CWE or fuzzing.
user-invocable: false
---
# Scan Result Triage

1. Import and normalize findings by target, protocol, root cause and CWE.
2. Deduplicate across tools and repeated runs.
3. Evaluate reachability, exploit preconditions and compensating controls.
4. Prioritize by industrial impact, not CVSS alone.
5. Output actionable fix queue with repro evidence and retest criteria.
