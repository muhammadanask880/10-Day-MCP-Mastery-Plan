# 📚 Day 3 — Lessons

Four sub-topics. Read them in order. Don't rush.

---

## 3.1 — What JSON-RPC 2.0 Is

### ☕ Karak chai analogy

A busy chai stall in Karama. Customers order, cashier writes on tiny pads:

```
   ┌──────────────────┐
   │  Order #47       │
   │  Item: Karak     │
   │  Size: Large     │
   │  Sugar: Medium   │
   └──────────────────┘
```

Barista replies with another slip:
```
   ┌──────────────────┐
   │  Order #47       │
   │  Status: READY   │
   │  Time: 2 min     │
   └──────────────────┘
```

**Every slip has the same shape.** That's why 50 customers + 5 baristas don't get confused. JSON-RPC is the **strict, agreed-on format** for software messages. Same idea.

### 🛠️ Technical definition

> **JSON-RPC 2.0** = A lightweight, stateless **Remote Procedure Call** protocol using **JSON** as the message format.

Three terms decoded:

- **Remote Procedure Call (RPC):** *"Hey, run this function over there, and tell me the result."* Like calling Domino's — you don't make the pizza, they do.
- **JSON:** Plain-text data using `{}`, `[]`, and `"keys": values`. Human-readable, language-agnostic.
- **2.0:** The version released in 2010 — the one everyone uses today.

### 💻 Example exchange

**Client sends:**
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "calculator.add",
  "params": { "a": 5, "b": 3 }
}
```

**Server replies:**
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": 8
}
```

That's JSON-RPC at its purest. Notice:
- Both messages declare `"jsonrpc": "2.0"`
- Both have matching `"id": 1` — pairs request with response
- Request has `method` + `params`. Response has `result`.

### 🤖 MCP uses JSON-RPC 2.0

Every MCP message you'll ever see is just JSON-RPC. MCP defines *which methods exist* (`tools/list`, `tools/call`, `initialize`...), but the wire format is plain JSON-RPC. **Know JSON-RPC = know MCP's syntax.** 🎯

---

## 3.2 — The Three Message Types

### 💬 WhatsApp analogy

You send your friend 3 different kinds of messages:

| Type | WhatsApp example | Reply expected? |
|------|-----------------|-----------------|
| **Request** | *"Are you free Thursday at 3pm?"* | ✅ Yes |
| **Response** | *"Yes, Thursday at 3 works."* | (it IS the reply) |
| **Notification** | *"FYI I'm logging off."* | ❌ No |

JSON-RPC has exactly these three kinds. Same idea, software version.

### 🛠️ The 3 types, formally

| Type | Has `id`? | Has `method`? | Has `result`/`error`? |
|------|-----------|---------------|----------------------|
| **Request** | ✅ | ✅ | ❌ |
| **Response** | ✅ (matches request) | ❌ | ✅ (one or the other) |
| **Notification** | ❌ **NO** | ✅ | ❌ |

### 🕵️ The sneaky one — the Notification

> **A "request" without an `id` is NOT a request — it's a notification.**

Side by side:

```json
// REQUEST — has id, expects reply
{ "jsonrpc": "2.0", "id": 1, "method": "send", "params": {...} }

// NOTIFICATION — NO id, NO reply
{ "jsonrpc": "2.0",          "method": "log",  "params": {...} }
```

Miss the missing id, and your code **hangs forever** waiting for a reply that's never coming. The `id` IS the only difference. 🔍

### 🌍 In MCP

- `tools/call` → **Request** (need result back)
- `notifications/initialized` → **Notification** ("I'm ready", no reply needed)
- `notifications/progress` → **Notification** ("30% done", no reply needed)
- `notifications/cancelled` → **Notification** ("I'm killing request #7")

---

## 3.3 — Every Field, Explained

### 📝 Bank slip analogy

A bank transfer slip has fields with clear jobs: form version, slip number, action, details, success/error box. JSON-RPC has the same 6 fields.

### The 6 fields

| Field | Job | Required? |
|-------|-----|-----------|
| `jsonrpc` | Declares protocol version — always `"2.0"` | ✅ Always |
| `id` | Pairs request ↔ response (number or string) | Request/Response only |
| `method` | The "verb" — what function to call | Requests/Notifications |
| `params` | The inputs (object or array) | Optional |
| `result` | Successful answer | Success responses only |
| `error` | Failure info (code, message, data) | Failed responses only |

### ⚠️ The strict rule

> **A response has EITHER `result` OR `error`. NEVER both.**

Think of the bank slip — either the transfer succeeded, or it didn't. There's no "succeeded with errors." Same here.

### 💻 Success vs failure side-by-side

**Success response:**
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": { "listings": [...] }
}
```

**Failure response:**
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "error": {
    "code": -32602,
    "message": "Invalid params: 'area' must be a real city",
    "data": { "field": "area", "value": "Mars" }
  }
}
```

### 🔢 Standard error codes

| Code | Meaning |
|------|---------|
| `-32700` | Parse error (malformed JSON) |
| `-32600` | Invalid Request (wrong shape) |
| `-32601` | **Method not found** (typo'd a function name?) |
| `-32602` | Invalid params (wrong types) |
| `-32603` | Internal error (server crashed) |

Custom codes from servers are allowed too. We'll dig deeper on Day 9.

### 📊 The decision tree

```
   Is there an "id"?
        │
   ┌────┴────┐
   YES       NO
   │         │
   │         └──► NOTIFICATION
   │
   Is there a "method"?
        │
   ┌────┴────┐
   YES       NO
   │         │
   │         └──► RESPONSE
   │              ├─ has "result"? → SUCCESS
   │              └─ has "error"?  → FAILURE
   │
   └──► REQUEST
```

5 seconds to classify any JSON-RPC message. 🎯

---

## 3.4 — Reading Raw MCP Traffic

You can now read real MCP traffic. Here's a typical session — read each line, classify the message:

```jsonl
// ─── 1. CONNECTION OPENS ───
→ { "jsonrpc": "2.0", "id": 0, "method": "initialize", "params": {...} }
   💬 CLIENT: "Hi, are we compatible?" (REQUEST, id=0)

← { "jsonrpc": "2.0", "id": 0, "result": { "serverInfo": {...} } }
   💬 SERVER: "Yes — I'm weather-server v1.0." (RESPONSE to id=0)

→ { "jsonrpc": "2.0", "method": "notifications/initialized" }
   💬 CLIENT: "Cool, I'm ready." (NOTIFICATION — no id, no reply)

// ─── 2. CLIENT ASKS WHAT TOOLS EXIST ───
→ { "jsonrpc": "2.0", "id": 1, "method": "tools/list" }
   💬 CLIENT: "Show me your menu." (REQUEST, id=1)

← { "jsonrpc": "2.0", "id": 1, "result": { "tools": [...] } }
   💬 SERVER: "Here's my menu: 1 tool — get_weather." (RESPONSE to id=1)

// ─── 3. CLIENT CALLS A TOOL — with progressToken ───
→ { "jsonrpc": "2.0", "id": 2, "method": "tools/call",
    "params": { "name": "get_weather", "arguments": {...},
                "_meta": { "progressToken": "p1" } } }
   💬 CLIENT: "Call get_weather for Dubai." (REQUEST, id=2, with progress token "p1")

// ─── 4. SERVER STREAMS PROGRESS (notifications, paired by progressToken) ───
← { "jsonrpc": "2.0", "method": "notifications/progress",
    "params": { "progressToken": "p1", "progress": 30 } }
   💬 SERVER: "30% done..." (NOTIFICATION, tagged p1)

← { "jsonrpc": "2.0", "method": "notifications/progress",
    "params": { "progressToken": "p1", "progress": 70 } }
   💬 SERVER: "70% done..." (NOTIFICATION, tagged p1)

// ─── 5. SERVER RETURNS FINAL RESULT (paired by id) ───
← { "jsonrpc": "2.0", "id": 2, "result": { "content": [...] } }
   💬 SERVER: "Done — Dubai is 38°C and sunny." (RESPONSE to id=2)
```

### Two pairing mechanisms

| Pairing | Mechanism | Used for |
|---------|-----------|----------|
| **Request ↔ Response** | matching `id` | The final answer |
| **Request ↔ Progress notifications** | matching `progressToken` | Updates DURING a long operation |

Same idea (correlation), different fields (because notifications have no `id`).

---

## 🔁 Day 3 recap

```
✅ 3.1  What JSON-RPC is        → Restaurant slip analogy + RPC defined
✅ 3.2  3 message types         → Request, Response, Notification
✅ 3.3  Every field             → jsonrpc, id, method, params, result, error
✅ 3.4  Reading raw traffic     → Full MCP session decoded
```

**One sentence to remember:**
> *MCP is JSON-RPC 2.0 with specific method names. Once you can read JSON-RPC, you can read MCP — there's no magic.*

Next: [`02-practice.md`](02-practice.md) — hand-write 3 messages.
