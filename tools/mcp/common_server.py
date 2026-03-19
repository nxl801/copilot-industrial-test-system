#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import datetime, timezone
import json
import sys


def now_iso():
    return datetime.now(timezone.utc).isoformat()


def default_dispatch(server_name, tool, params):
    return {
        'ok': True,
        'server': server_name,
        'tool': tool,
        'timestamp': now_iso(),
        'inputs': params,
        'artifacts': [],
        'warnings': ['stub implementation: replace with real backend integration'],
        'result': {
            'echo': params,
            'message': f'{server_name}.{tool} executed in stub mode'
        }
    }


def make_handler(server_name, tools_map):
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, format, *args):
            return

        def _send(self, payload, code=200):
            data = json.dumps(payload, ensure_ascii=False, indent=2).encode()
            self.send_response(code)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.send_header('Content-Length', str(len(data)))
            self.end_headers()
            self.wfile.write(data)

        def do_GET(self):
            self._send({
                'ok': True,
                'server': server_name,
                'timestamp': now_iso(),
                'status': 'ready',
                'tools': sorted(tools_map.keys()),
            })

        def do_POST(self):
            length = int(self.headers.get('Content-Length', '0'))
            raw = self.rfile.read(length).decode() if length else '{}'
            try:
                req = json.loads(raw)
            except Exception:
                self._send({'ok': False, 'error': 'invalid_json', 'raw': raw}, 400)
                return

            tool = req.get('tool')
            params = req.get('params', {})
            if not tool:
                self._send({
                    'ok': False,
                    'error': 'missing_tool',
                    'server': server_name,
                    'availableTools': sorted(tools_map.keys()),
                }, 400)
                return

            fn = tools_map.get(tool)
            if not fn:
                self._send({
                    'ok': False,
                    'error': 'unknown_tool',
                    'server': server_name,
                    'tool': tool,
                    'availableTools': sorted(tools_map.keys()),
                }, 404)
                return

            try:
                result = fn(params)
                self._send(result, 200)
            except Exception as e:
                self._send({
                    'ok': False,
                    'server': server_name,
                    'tool': tool,
                    'error': 'tool_execution_failed',
                    'message': str(e),
                }, 500)
    return Handler


def serve(server_name, port, tools_map):
    HTTPServer(('127.0.0.1', port), make_handler(server_name, tools_map)).serve_forever()


if __name__ == '__main__':
    print('Import common_server.py from a concrete MCP stub server.')
