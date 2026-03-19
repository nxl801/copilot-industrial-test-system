#!/usr/bin/env python3
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))
from common_server import serve, default_dispatch


def make(tool):
    return lambda params: default_dispatch('motionctl', tool, params)


TOOLS = {
    'compare_parameters': make('compare_parameters'),
    'read_trace': make('read_trace'),
    'export_fault_history': make('export_fault_history'),
    'run_profile': make('run_profile'),
}

serve('motionctl', 8764, TOOLS)
