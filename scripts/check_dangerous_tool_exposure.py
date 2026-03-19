#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1] / 'profiles'
forbidden = ['labctl/*', 'plcctl/*', 'motionctl/*']
violations = []
for f in ROOT.rglob('*.agent.md'):
    text = f.read_text()
    if 'hardware-bench-coordinator.agent.md' in str(f):
        continue
    for tool in forbidden:
        if tool in text:
            violations.append(f'{f}: forbidden tool exposure {tool}')

if violations:
    print('\n'.join(violations))
    sys.exit(1)
print('dangerous tool exposure check OK')
