# 📐 Example — Walk-through of the Echo Server

> ⚠️ **Run the code first.** This document explains WHY the code looks the way it does — it's most useful after you've seen the server work.

---

## 🎯 What this server proves

By running [`echo-server/server.py`](echo-server/server.py) + [`echo-server/test_client.py`](echo-server/test_client.py), you prove ALL of Day 3 in live code:

| Day 3 concept | How the example proves it |
|---|---|
| JSON-RPC has 3 message types | Test 1, 2 are REQUESTS. Test 3 triggers an ERROR RESPONSE. Test 4 is a NOTIFICATION. All 3 types covered. |
| Notifications have no `id` | Test 4 has no id → server prints *"This was a NOTIFICATION"* and sends no body back |
| Responses use `result` OR `error`, never both | Test 1/2 use `result`. Test 3 uses `error`. Never both. |
| `id` pairs request ↔ response | Every reply quotes back the same `id` you sent |
| Standard error code `-32601` means "method not found" | Test 3 calls `divide`, which doesn't exist → `-32601` returned |

---

## 🔍 Code walk-through — `server.py`

### Block 1 — The methods this server knows

```python
def method_echo(params):
    return {"you_sent": params}

def method_add(params):
    return params["a"] + params["b"]

METHODS = {
    "echo": method_echo,
    "add": method_add,
}
```

A dictionary mapping **method names** (strings) to **Python functions**. Adding a new method is as easy as defining a function and adding it here. This is also exactly how MCP servers organize their tools (Day 4). 🎯

### Block 2 — Parsing the incoming JSON

```python
length = int(self.headers.get("Content-Length", 0))
body = self.rfile.read(length).decode("utf-8")
try:
    req = json.loads(body)
except json.JSONDecodeError:
    return self._respond({
        "jsonrpc": "2.0", "id": None,
        "error": {"code": -32700, "message": "Parse error"}
    })
```

Read the HTTP body, parse JSON. If JSON itself is malformed → return error **`-32700` (Parse error)**. Sub-topic 3.3 had this code in the table. Here it is in real code. 🔧

### Block 3 — Decide: is it a Notification or a Request?

```python
msg_id = req.get("id")   # None means this is a NOTIFICATION

if msg_id is None:
    if method in METHODS:
        METHODS[method](params)  # silently run
    self.send_response(204)  # 204 = No Content
    self.end_headers()
    return
```

**This is THE classifying line.** No id = notification = run silently, send no body. The exact rule from Sub-topic 3.2, in 4 lines of Python. ✅

### Block 4 — Method not found?

```python
if method not in METHODS:
    return self._respond({
        "jsonrpc": "2.0", "id": msg_id,
        "error": {"code": -32601, "message": f"Method not found: {method}"}
    })
```

If the requested method isn't in our dictionary → return **`-32601`**. Test 3 (`divide`) hits this exact branch.

### Block 5 — Run the method, return result

```python
try:
    result = METHODS[method](params)
    self._respond({"jsonrpc": "2.0", "id": msg_id, "result": result})
except Exception as e:
    self._respond({
        "jsonrpc": "2.0", "id": msg_id,
        "error": {"code": -32603, "message": f"Internal error: {e}"}
    })
```

Call the function, wrap the result in a JSON-RPC response. If anything throws → `-32603` (Internal error). This is what production-grade error handling looks like — minus a couple of niceties. 🛡️

---

## 🔍 Code walk-through — `test_client.py`

Four tests, demonstrating every message type:

| Test | Message type | What it proves |
|------|-------------|----------------|
| 1 | REQUEST (id=1, method=echo) | Basic request → success response |
| 2 | REQUEST (id=2, method=add) | Multiple in-flight requests, paired by id |
| 3 | REQUEST (id=3, method=divide) | Unknown method → error -32601 |
| 4 | NOTIFICATION (no id) | Server runs silently, returns nothing |

The test client uses Python's built-in `urllib` — no third-party libraries needed.

---

## 🎯 The big takeaways

1. **JSON-RPC is dead-simple.** ~80 lines of Python and you have a working spec-compliant server.
2. **The "no id = notification" rule is enforced by 4 lines of code.** That's the entire rule.
3. **Error codes are just numbers.** Server picks one based on what went wrong, client checks it. No magic.
4. **MCP is built on this.** Day 6 will literally take this pattern and add MCP-specific method names. You're 80% of the way there already.

---

## 🛠️ Try modifying it

The best learning happens when you break things on purpose:

1. **Add a `subtract` method** — 5 lines of code
2. **Make `add` throw an error** when given strings — see -32603 happen live
3. **Add an `id` to test 4** — watch it become a real request with a real response
4. **Remove the `if msg_id is None:` block** — notifications now try to send responses → broken behavior. See the consequence.

Each tweak teaches you something the docs never will.

---

## ⏭️ What's next

Day 4 (Tools) takes this exact pattern and adds:
- **Method names from MCP** (`tools/list`, `tools/call`)
- **Input schemas** so the LLM knows what params to send
- **Structured return content** (text, images, etc.)

But the message-passing engine? Same as what's in `server.py`. **You already built the hard part.** 🎯
