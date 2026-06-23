# 🛠️ Day 3 Mini-Project — Build a Tiny JSON-RPC Echo Server

This is where Day 3 gets **real**. You'll run an actual server you can talk to. **No MCP yet — pure JSON-RPC.** Once you see this work, MCP servers (Day 6) will feel like a small step up.

---

## 🎬 What you're building

A tiny Python HTTP server that speaks JSON-RPC 2.0. It supports:

- 🔁 `echo` — sends back whatever you give it
- ➕ `add` — adds two numbers
- 🚫 Unknown methods → returns `-32601` error
- 📣 Notifications → silently runs, no response

**~80 lines of code. No `pip install` needed.** Just built-in Python.

Plus a test client to fire 4 messages and see all 3 message types in action.

---

## 📦 The code is already here

You don't have to write the code from scratch — but you DO have to **read it carefully** and **run it yourself**. The point is to see a real JSON-RPC server work, end to end.

| File | What it is |
|------|------------|
| [`echo-server/server.py`](echo-server/server.py) | The JSON-RPC server |
| [`echo-server/test_client.py`](echo-server/test_client.py) | Test client that fires 4 messages |

### 📖 Read the code first

Open both files. Read them slowly. Look for:

1. **In `server.py`:** Find the line that decides "is this a notification?" *(Hint: it's an `if msg_id is None` check — the exact rule from sub-topic 3.2!)*
2. **In `server.py`:** Find where the error code `-32601` gets returned. What method-related condition triggers it?
3. **In `test_client.py`:** Identify which test is a notification (no id) and which 3 are requests.

If you can answer those 3 questions by reading the code, you're ready to run it.

---

## ▶️ How to run (2 terminals)

### Terminal 1 — start the server
```bash
cd echo-server
python server.py
```

You should see:
```
🚀 JSON-RPC server running at http://localhost:8000
   Press Ctrl+C to stop.
```

**Leave that terminal open.**

### Terminal 2 — run the test client (open a NEW terminal)
```bash
cd echo-server
python test_client.py
```

---

## 🔮 What you should see

### Server terminal — 4 incoming messages:
```
📨 RECEIVED: {"jsonrpc": "2.0", "id": 1, "method": "echo", "params": {"hi": "world"}}
📤 SENDING:  {"jsonrpc": "2.0", "id": 1, "result": {"you_sent": {"hi": "world"}}}

📨 RECEIVED: {"jsonrpc": "2.0", "id": 2, "method": "add", "params": {"a": 5, "b": 7}}
📤 SENDING:  {"jsonrpc": "2.0", "id": 2, "result": 12}

📨 RECEIVED: {"jsonrpc": "2.0", "id": 3, "method": "divide", "params": {"a": 10, "b": 2}}
📤 SENDING:  {"jsonrpc": "2.0", "id": 3, "error": {"code": -32601, "message": "Method not found: divide"}}

📨 RECEIVED: {"jsonrpc": "2.0", "method": "echo", "params": {"silent": "this won't get a reply"}}
   ↳ This was a NOTIFICATION (no response will be sent)
```

### What to NOTICE in the output

1. **id pairing** — every request's id (`1`, `2`, `3`) comes back in its response. Live proof of sub-topic 3.3.
2. **`add` returns `12`** — your protocol parser handled the math seamlessly.
3. **`divide` returns `-32601`** — your real first error code, live!
4. **Test 4 (notification)** — server says *"This was a NOTIFICATION"* and the client gets *"(no body)"*. The "no id = no reply" rule, proven.

---

## 🧪 Tweak it yourself (optional)

Once it works, try:
- **Add a `subtract` method** — copy `method_add`, change the body, add it to `METHODS`
- **Make `add` fail when given strings** — see what error code surfaces (it'll trigger -32603)
- **Add a 5th test** with an empty `params` — what happens?

Modifying real code is where MCP becomes second nature. 💪

---

## 📖 If you want a written walkthrough

See [`05-example-echo-server.md`](05-example-echo-server.md) — line-by-line code explanation.

---

## ✅ When done

Once you've run it and watched the output:
- Take a screenshot or note what you saw
- Move on to [`04-quiz.md`](04-quiz.md)

🎯 **This is your first working server in the course.** Pause and feel that win. You went from *"what's MCP?"* on Day 1 to *"I built a server that speaks the protocol underneath MCP"* on Day 3. The foundation is real.
