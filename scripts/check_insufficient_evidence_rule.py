#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
needles = ['INSUFFICIENT EVIDENCE']
checked = [ROOT / '.github' / 'copilot-instructions.md'] + list((ROOT / 'profiles').rglob('copilot-instructions.md'))
missing = []
for f in checked:
    if f.exists() and not any(n in f.read_text() for n in needles):
        missing.append(str(f))
if missing:
    print('Missing INSUFFICIENT EVIDENCE rule in:')
    print('\n'.join(missing))
    sys.exit(1)
print('insufficient evidence rule check OK')
