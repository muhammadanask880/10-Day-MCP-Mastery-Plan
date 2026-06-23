"""Tiny test client — fires 4 messages at the JSON-RPC server and prints replies.

Run the server first (in another terminal):  python server.py
Then run this:                                python test_client.py
"""

import json
import urllib.request
import urllib.error

URL = "http://localhost:8000"


def send(message):
    """Send a JSON-RPC message and print whatever comes back."""
    raw = json.dumps(message)
    print(f"\n→ Sending:  {raw}")
    data = raw.encode("utf-8")
    req = urllib.request.Request(
        URL, data=data, headers={"Content-Type": "application/json"}
    )
    try:
        with urllib.request.urlopen(req) as response:
            body = response.read().decode("utf-8")
            if body:
                print(f"← Received: {body}")
            else:
                print(f"← (no body — was that a notification?)")
    except urllib.error.HTTPError as e:
        print(f"← HTTP error: {e.code}")
    except urllib.error.URLError as e:
        print(f"← Connection failed: {e.reason} (is the server running?)")


# ═══════════════════════════════════════════════════════════
# TEST 1 — a normal REQUEST (id present)
# ═══════════════════════════════════════════════════════════
send({
    "jsonrpc": "2.0",
    "id": 1,
    "method": "echo",
    "params": {"hi": "world"}
})

# ═══════════════════════════════════════════════════════════
# TEST 2 — another REQUEST, math this time
# ═══════════════════════════════════════════════════════════
send({
    "jsonrpc": "2.0",
    "id": 2,
    "method": "add",
    "params": {"a": 5, "b": 7}
})

# ═══════════════════════════════════════════════════════════
# TEST 3 — unknown method, expect error -32601
# ═══════════════════════════════════════════════════════════
send({
    "jsonrpc": "2.0",
    "id": 3,
    "method": "divide",      # we never defined this!
    "params": {"a": 10, "b": 2}
})

# ═══════════════════════════════════════════════════════════
# TEST 4 — a NOTIFICATION (no id) — expect empty body back
# ═══════════════════════════════════════════════════════════
send({
    "jsonrpc": "2.0",
    "method": "echo",
    "params": {"silent": "this won't get a reply"}
})

print("\n✅ All 4 tests done.")
