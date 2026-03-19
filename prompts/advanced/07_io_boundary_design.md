# Advanced Prompt 07 · AI / DI / DO / HSC 边界测试设计（io-module-verifier）

```text
请针对 ${IO_MODULE_FAMILY} 生成边界测试设计，只做分析，不执行。

覆盖：
- AI: scaling, linearity, min/max, open-wire, short-circuit
- DI: polarity, debounce, delay, pulse loss
- DO: default state, pulse width, fail-safe behavior
- HSC: frequency range, overflow, timestamp, rising/falling edge

输出：
1. stimulus pattern list
2. expected ranges / timing windows / tolerances
3. 最小化 bench test matrix
4. 每条测试需要的 artifact
```
