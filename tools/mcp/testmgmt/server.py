#!/usr/bin/env python3
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))
from common_server import serve, default_dispatch


def make(tool):
    return lambda params: default_dispatch('testmgmt', tool, params)


TOOLS = {
    'create_case': make('create_case'),
    'update_result': make('update_result'),
    'attach_artifact': make('attach_artifact'),
    'create_defect_stub': make('create_defect_stub'),
}

serve('testmgmt', 8763, TOOLS)
