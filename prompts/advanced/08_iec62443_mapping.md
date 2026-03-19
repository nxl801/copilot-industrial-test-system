# Advanced Prompt 08 · IEC 62443-4-2 证据映射（security-62443-assessor）

```text
请对 ${PRODUCT_NAME} / build ${BUILD_ID} 做 IEC 62443-4-2 证据映射。

输入：
- docs folder: ${DOCS_PATH}
- configs: ${CONFIG_PATH}
- scan bundle: ${SCAN_BUNDLE}
- known interfaces: ${INTERFACE_LIST}

要求：
- 先做 threat model 摘要
- 再做 requirement -> evidence mapping
- 没有证据的项必须标记为 MISSING EVIDENCE
- 不要把部分覆盖写成 fully covered

输出：
1. attack surface
2. trust boundaries
3. requirement / evidence / status table
4. gaps
5. residual risk
6. mandatory retests
```
