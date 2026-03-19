#!/usr/bin/env python3
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))
from common_server import serve, default_dispatch


def make(tool):
    return lambda params: default_dispatch('plcctl', tool, params)


TOOLS = {
    'build': make('build'),
    'diff_tags': make('diff_tags'),
    'export_state_machine': make('export_state_machine'),
    'run_simulation': make('run_simulation'),
    'export_alarm_matrix': make('export_alarm_matrix'),
}

serve('plcctl', 8765, TOOLS)
