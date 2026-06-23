# 📅 Day 3 — JSON-RPC: The Language Underneath MCP

> *"Day 2 was abstract (architecture). Day 3 is concrete — we look at the actual messages flying between client and server."*

---

## 🎯 What you'll be able to do by the end of today

1. Explain **what JSON-RPC 2.0 is** and why MCP chose it
2. Tell the **3 types of JSON-RPC messages** apart (Request, Response, Notification)
3. Identify every **field in a JSON-RPC message** (`id`, `method`, `params`, `result`, `error`)
4. **Read raw MCP traffic** byte-by-byte without freaking out
5. Run (and understand!) a **working JSON-RPC server** in Python

---

## 📂 Files in this folder

| File | Purpose |
|------|---------|
| [`01-lessons.md`](01-lessons.md) | The 4 sub-topics — read this first |
| [`02-practice.md`](02-practice.md) | Hand-write 3 JSON-RPC messages |
| [`03-mini-project.md`](03-mini-project.md) | Build a tiny JSON-RPC echo server in Python |
| [`04-quiz.md`](04-quiz.md) | 5 questions to lock the knowledge in |
| [`05-example-echo-server.md`](05-example-echo-server.md) | Walk-through of the worked example |
| [`echo-server/server.py`](echo-server/server.py) | Working JSON-RPC server (~80 lines) |
| [`echo-server/test_client.py`](echo-server/test_client.py) | Test client that fires 4 messages |

---

## 📚 How to study Day 3 (do these in order)

### Step 1 — Read the lessons
Open [`01-lessons.md`](01-lessons.md). Read slowly. Each sub-topic builds on the last.

### Step 2 — When stuck, ask any AI
- 💬 **Claude (free)** — https://claude.ai
- 💬 **Gemini (free)** — https://gemini.google.com
- 💬 **ChatGPT (free)** — https://chatgpt.com

How to ask well:
> *"Explain this JSON-RPC concept to me with a fresh analogy. I'm learning the protocol from scratch."*

### Step 3 — Do the practice
Open [`02-practice.md`](02-practice.md). Hand-write 3 JSON-RPC messages. JSON's syntax is unforgiving — writing forces precision.

### Step 4 — Do the mini-project
Open [`03-mini-project.md`](03-mini-project.md). You'll **run a working JSON-RPC server** in 2 terminals and watch the traffic. Real code, real running, real "aha." 🛠️

### Step 5 — Take the quiz
Open [`04-quiz.md`](04-quiz.md). Answer all 5 questions in your own words.

### Step 6 — Self-evaluate with any AI

Paste this prompt into Claude/Gemini/GPT:

> *"I am studying a self-paced MCP course. Below is (1) the lesson content for Day 3, (2) the quiz questions, and (3) my answers. Please grade each out of 1 (total /5), tell me what I missed, suggest a better phrasing for any weak answer, and end with one curiosity question for Day 4.*
>
> *=== LESSON CONTENT === [paste 01-lessons.md]*
> *=== QUIZ === [paste 04-quiz.md]*
> *=== MY ANSWERS === [paste your answers]*"

---

## 🧠 The single sentence to carry forward

> *MCP is JSON-RPC 2.0 with specific method names. Once you can read JSON-RPC, you can read MCP — there's no magic.*

---

## ⏭️ Next up

When Day 3 feels solid, head to `../day-04/` (coming soon — **Tools deep dive**, your first MCP primitive).

Between sessions, chew on this:
> *"You built an `add` method on your echo server. To turn that into an MCP tool, what extra information would you need to give the AI so it knows WHEN to call it?"*

That's your on-ramp to Day 4. 🚀
