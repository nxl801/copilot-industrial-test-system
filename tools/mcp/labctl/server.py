#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime, timezone
import json
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))
from common_server import serve

ROOT = Path(__file__).resolve().parents[3]
ART = ROOT / 'artifacts' / 'evidence' / 'bench_output'
ART.mkdir(parents=True, exist_ok=True)


def now():
    return datetime.now(timezone.utc).isoformat()


def write_artifact(name, payload):
    path = ART / name
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2))
    return str(path.relative_to(ROOT))


def reserve_bench(params):
    lock = {
        'station_id': params.get('station_id', 'bench-a01'),
        'operator': params.get('operator', 'copilot'),
        'ttl_minutes': params.get('ttl_minutes', 30),
        'locked_at': now(),
        'lock_id': f"lock-{params.get('station_id', 'bench-a01')}",
    }
    art = write_artifact('reserve_bench.json', lock)
    return {'ok': True, 'server': 'labctl', 'tool': 'reserve_bench', 'timestamp': now(), 'inputs': params, 'artifacts': [art], 'warnings': ['stub mode'], 'result': lock}


def release_bench(params):
    result = {'released': True, 'lock_id': params.get('lock_id', 'lock-bench-a01')}
    art = write_artifact('release_bench.json', result)
    return {'ok': True, 'server': 'labctl', 'tool': 'release_bench', 'timestamp': now(), 'inputs': params, 'artifacts': [art], 'warnings': ['stub mode'], 'result': result}


def power_cycle(params):
    result = {'station_id': params.get('station_id', 'bench-a01'), 'profile': params.get('profile', 'default'), 'status': 'cycled'}
    art = write_artifact('power_cycle.json', result)
    return {'ok': True, 'server': 'labctl', 'tool': 'power_cycle', 'timestamp': now(), 'inputs': params, 'artifacts': [art], 'warnings': ['stub mode'], 'result': result}


def start_capture(params):
    result = {'capture_id': 'capture-001', 'channels': params.get('channels', ['log', 'trace']), 'status': 'started'}
    art = write_artifact('start_capture.json', result)
    return {'ok': True, 'server': 'labctl', 'tool': 'start_capture', 'timestamp': now(), 'inputs': params, 'artifacts': [art], 'warnings': ['stub mode'], 'result': result}


def read_alarm_log(params):
    result = {'station_id': params.get('station_id', 'bench-a01'), 'alarms': [{'code': 'A-101', 'level': 'warning', 'message': 'Demo alarm log entry'}]}
    art = write_artifact('alarm_log.json', result)
    return {'ok': True, 'server': 'labctl', 'tool': 'read_alarm_log', 'timestamp': now(), 'inputs': params, 'artifacts': [art], 'warnings': ['stub mode'], 'result': result}


def passthrough(tool):
    return lambda params: {'ok': True, 'server': 'labctl', 'tool': tool, 'timestamp': now(), 'inputs': params, 'artifacts': [], 'warnings': ['stub mode'], 'result': {'message': f'{tool} not yet implemented'}}


TOOLS = {
    'reserve_bench': reserve_bench,
    'release_bench': release_bench,
    'power_cycle': power_cycle,
    'download_firmware': passthrough('download_firmware'),
    'start_capture': start_capture,
    'stop_capture': passthrough('stop_capture'),
    'set_io_pattern': passthrough('set_io_pattern'),
    'read_alarm_log': read_alarm_log,
    'screenshot_panel': passthrough('screenshot_panel'),
    'send_panel_input': passthrough('send_panel_input'),
}

serve('labctl', 8761, TOOLS)
