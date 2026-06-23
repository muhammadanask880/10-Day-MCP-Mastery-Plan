# 🧪 Day 3 Practice — Hand-Write 3 JSON-RPC Messages

**Time:** 10–15 minutes
**Goal:** Move from *reading* JSON-RPC to *writing* it. JSON syntax is unforgiving — writing forces precision into your muscle memory.

---

## ✍️ Your task

Write these 3 messages in a text file (or on paper). No editor magic — type each character.

### Message 1 — A REQUEST

A JSON-RPC request that:
- Calls a calculator server's `multiply` method
- Params: `a = 7`, `b = 6`
- Uses id `42`

### Message 2 — A NOTIFICATION

A JSON-RPC notification that:
- Cancels request `42`
- Method: `notifications/cancelled`
- Param: `requestId: 42`

### Message 3 — An ERROR RESPONSE

The server's error response saying *"Method not found"* for a request that had id `99`.
Hint: the standard error code starts with `-326…`

---

## 📋 Checklist (apply to each message)

- ✅ `"jsonrpc": "2.0"` present
- ✅ Notification: **NO `id`**. Request/Response: **HAS `id`**
- ✅ Quotes around keys AND string values
- ✅ Commas between fields, NOT after the last one
- ✅ Curly braces balanced (count opens vs closes)
- ✅ Error code is a **number**, not a string (no quotes around `-32601`)
- ✅ Error responses use **`error`** field, NOT `params`

---

## 💡 Cheat sheet (only if stuck)

```jsonl
REQUEST:       { "jsonrpc": "2.0", "id": N, "method": "...", "params": {...} }
NOTIFICATION:  { "jsonrpc": "2.0",          "method": "...", "params": {...} }
ERROR RESP:    { "jsonrpc": "2.0", "id": N, "error":  { "code": -N, "message": "..." } }
```

---

## 🎯 Self-evaluate

Paste your 3 messages into Claude/Gemini/GPT with this prompt:

> *"I'm learning JSON-RPC 2.0. Check these 3 messages for: (1) valid JSON syntax, (2) correct structure (request/notification/error response), (3) proper field usage. For each one, tell me what's right and what's wrong."*

---

## 🧠 The lesson

JSON is **brutally strict**. One missing brace, one stray quote, one string-where-a-number-should-be → whole message rejected.

**You'll never write JSON-RPC by hand in real life** — you'll use an SDK that handles the syntax. Today's practice is just so you can **read raw messages** when debugging real servers. 🔍

Done? Move on to [`03-mini-project.md`](03-mini-project.md) — you'll run a real JSON-RPC server.
