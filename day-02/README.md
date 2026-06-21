# 📅 Day 2 — MCP Architecture

> *"Yesterday you learned WHY MCP exists. Today we open the hood and see HOW it actually works."*

---

## 🎯 What you'll be able to do by the end of today

1. Name the **three main parts** of any MCP setup (host, client, server) and explain what each does
2. Understand the **three transports** MCP uses (stdio, HTTP, SSE) and when to pick which
3. Identify the **trust boundary** in an MCP setup — and why it matters for security
4. Draw an architecture diagram for any MCP system you can think of

---

## 📂 Files in this folder

| File | Purpose |
|------|---------|
| [`01-lessons.md`](01-lessons.md) | The 5 sub-topics — read this first |
| [`02-practice.md`](02-practice.md) | Hands-on: draw the architecture for a Claude Desktop setup |
| [`03-mini-project.md`](03-mini-project.md) | Design a fully autonomous WhatsApp lead responder |
| [`04-quiz.md`](04-quiz.md) | 5 questions to lock the knowledge in |
| [`05-example-architectures.md`](05-example-architectures.md) | Two worked examples — basic + advanced (autonomous cloud) |

---

## 📚 How to study Day 2 (do these in order)

### Step 1 — Read the lessons
Open [`01-lessons.md`](01-lessons.md). Read it slowly. Don't speed-read. Each sub-topic has an **analogy first** — really picture the analogy before moving to the definition.

### Step 2 — When you're stuck, ask an AI
- 💬 **Claude (free)** — https://claude.ai
- 💬 **Gemini (free)** — https://gemini.google.com
- 💬 **ChatGPT (free)** — https://chatgpt.com
- 💻 **Claude Code (paid CLI)** — best for learning while building

**How to ask well:** copy the paragraph you don't understand and say:
> *"I'm learning MCP architecture. Explain this paragraph to me like I'm 10, with a fresh analogy."*

### Step 3 — Do the practice
Open [`02-practice.md`](02-practice.md). Draw the architecture yourself. The act of drawing forces concepts to stick. Use [draw.io](https://app.diagrams.net/), Excalidraw, or even paper.

### Step 4 — Do the mini-project
Open [`03-mini-project.md`](03-mini-project.md). Design a **fully autonomous WhatsApp lead responder**. This is harder than the practice — it combines architecture choices with real-world product thinking.

### Step 5 — Take the quiz
Open [`04-quiz.md`](04-quiz.md). Answer all 5 questions in your own words.

### Step 6 — Self-evaluate with any AI 🎯

Same magic step as Day 1. Open any AI and paste:

> *"I am studying a self-paced MCP course. Below is (1) the lesson content for Day 2, (2) the quiz questions, and (3) my own answers. Please grade each out of 1 (total /5), tell me what I missed, suggest one better phrasing for any weak answer, and end with one curiosity question for Day 3.*
>
> *=== LESSON CONTENT ===*
> *[paste contents of 01-lessons.md]*
>
> *=== QUIZ QUESTIONS ===*
> *[paste contents of 04-quiz.md]*
>
> *=== MY ANSWERS ===*
> *[paste your answers here]*"

---

## 🧠 The single sentence to carry forward

> *Transport depends on whether client and server are on the **same machine** — not on whether things are "local" or "cloud."*

If you remember nothing else from today, remember that. It will save you from architecture mistakes for years.

---

## ⏭️ Next up

When Day 2 feels solid, move to `../day-03/` (coming soon — **JSON-RPC**, the actual language the messages use).

Between sessions, chew on this curiosity prompt:
> *"You've seen JSON in tool calls already. Why JSON? Why not just plain text? (Hint: machines reading messages.)"*

That's the perfect on-ramp to Day 3. 🚀
