"""Tiny JSON-RPC 2.0 server — pure protocol, no MCP yet.

Listens on http://localhost:8000 and supports two methods: 'echo' and 'add'.
Demonstrates: requests, responses, notifications, and standard error codes.
"""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


# ═══════════════════════════════════════════════════════════
# 1) The METHODS this server knows how to run
# ═══════════════════════════════════════════════════════════

def method_echo(params):
    """Returns whatever was passed in."""
    return {"you_sent": params}


def method_add(params):
    """Adds two numbers a + b."""
    return params["a"] + params["b"]


METHODS = {
    "echo": method_echo,
    "add": method_add,
}


# ═══════════════════════════════════════════════════════════
# 2) The JSON-RPC HANDLER (the brain of the server)
# ═══════════════════════════════════════════════════════════

class JsonRpcHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # --- Read the raw request body ---
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length).decode("utf-8")
        print(f"\n📨 RECEIVED: {body}")

        # --- Try to parse JSON. Bad JSON → error -32700 ---
        try:
            req = json.loads(body)
        except json.JSONDecodeError:
            return self._respond({
                "jsonrpc": "2.0", "id": None,
                "error": {"code": -32700, "message": "Parse error"}
            })

        method = req.get("method")
        params = req.get("params", {})
        msg_id = req.get("id")   # None means this is a NOTIFICATION

        # --- Notification branch (no id = no response) ---
        if msg_id is None:
            print(f"   ↳ This was a NOTIFICATION (no response will be sent)")
            if method in METHODS:
                METHODS[method](params)  # silently run
            self.send_response(204)  # 204 = No Content
            self.end_headers()
            return

        # --- Request branch: unknown method → error -32601 ---
        if method not in METHODS:
            return self._respond({
                "jsonrpc": "2.0", "id": msg_id,
                "error": {"code": -32601, "message": f"Method not found: {method}"}
            })

        # --- Request branch: run the method, return result ---
        try:
            result = METHODS[method](params)
            self._respond({"jsonrpc": "2.0", "id": msg_id, "result": result})
        except Exception as e:
            self._respond({
                "jsonrpc": "2.0", "id": msg_id,
                "error": {"code": -32603, "message": f"Internal error: {e}"}
            })

    def _respond(self, obj):
        body = json.dumps(obj).encode("utf-8")
        print(f"📤 SENDING:  {body.decode()}")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *_):
        # Suppress noisy default HTTP logs — we print our own
        pass


# ═══════════════════════════════════════════════════════════
# 3) START THE SERVER
# ═══════════════════════════════════════════════════════════

if __name__ == "__main__":
    PORT = 8000
    print(f"🚀 JSON-RPC server running at http://localhost:{PORT}")
    print(f"   Press Ctrl+C to stop.\n")
    HTTPServer(("localhost", PORT), JsonRpcHandler).serve_forever()
