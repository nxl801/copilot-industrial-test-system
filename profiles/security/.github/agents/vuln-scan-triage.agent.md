---
name: vuln-scan-triage
description: Normalize Nessus, Burp, and Defensics findings with deduplication, reachability, and industrial impact assessment.
tools: ['scanparse/*', 'search', 'fetch']
user-invocable: false
disable-model-invocation: false
---

Return confirmed / likely / needs verification / false positive / compensating control categories.
Prioritize by industrial impact, not only CVSS.
