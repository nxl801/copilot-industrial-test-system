#!/usr/bin/env python3
from pathlib import Path
import json
import sys

src = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("artifacts/raw_findings.json")
dst = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("artifacts/normalized_findings.json")

data = []
if src.exists():
    try:
        data = json.loads(src.read_text())
    except Exception:
        data = []

dst.parent.mkdir(parents=True, exist_ok=True)
dst.write_text(json.dumps({"source": str(src), "items": data}, ensure_ascii=False, indent=2))
print(dst)
