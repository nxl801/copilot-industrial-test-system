#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1] / 'profiles'
required = ['name:', 'description:', 'tools:']
errors = []
for f in ROOT.rglob('*.agent.md'):
    text = f.read_text()
    if not text.startswith('---'):
        errors.append(f'{f}: missing frontmatter start')
        continue
    frontmatter = text.split('---', 2)[1]
    for key in required:
        if key not in frontmatter:
            errors.append(f'{f}: missing {key}')

if errors:
    print('\n'.join(errors))
    sys.exit(1)
print('frontmatter validation OK')
