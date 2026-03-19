# Advanced Prompt 09 · Nessus / Burp / Defensics triage（vuln-scan-triage）

```text
请对 ${SCAN_DIR} 下的 Nessus、Burp、Defensics 结果做统一 triage。

要求：
- 按 host / service / endpoint / protocol / CWE / root cause 去重
- 标出 reachability、auth precondition、network segmentation
- 区分 confirmed / likely / needs verification / false positive
- 优先按工业影响排序，不只按 CVSS

输出：
1. normalized findings
2. duplicates removed
3. compensating controls
4. fix queue
5. retest plan
6. 需要人工确认的项
```
