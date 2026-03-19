# Industrial Automation Test Rules

- 所有输出都必须记录：product family、firmware/build id、hardware revision、station id、timestamp。
- 同一真实工位视为独占资源；任何硬件动作前必须先拿到 bench lock。
- 优先 simulation、log replay、config diff、scan parsing，再做真实工位动作。
- 同一工位禁止并行执行：上电/下电、固件下载、force IO、驱动使能、运动命令。
- 每个缺陷都必须包含：expected、actual、repro steps、evidence path、suspected owner。
- 安全结论必须写清：evidence、gap、residual risk、retest action；没有证据就不要声称满足 IEC 62443-4-2。
- 任何涉及 motion / STO / emergency stop / power electronics 的测试，若安全前提不完整，停止并请求人工确认。
- Never execute real bench actions unless the active agent is hardware-bench-coordinator.
- In any /fleet or CLI analysis task, do not use labctl/*, plcctl/*, motionctl/*.
- If evidence is missing, output INSUFFICIENT EVIDENCE instead of PASS.
- Every conclusion must include artifact path, build id, hardware revision, and timestamp.
- Any request involving power cycle, download, force IO, servo enable, motion, STO, or E-stop must become a serialized action queue first.
