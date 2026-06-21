# 🛠️ Day 2 Mini-Project — Design a Fully Autonomous WhatsApp Lead Responder

This is where Day 2 becomes a **real product blueprint**. You'll design the architecture for a SaaS that **actually replies to leads automatically** — no human in the chat.

---

## 📋 The product idea

> **Autonomous WhatsApp Lead Responder for Property Agents**
>
> An agent (let's call her **Sara**) signs up. She:
> 1. Adds her WhatsApp Business number to the system
> 2. Uploads her property listings
> 3. Sets reply rules (e.g., "auto-reply property inquiries, escalate price negotiations")
> 4. Goes to sleep
>
> When a lead messages Sara's number at 3 AM, the system:
> - Reads the message
> - Looks up matching properties
> - Drafts a reply in Sara's writing style (using her past conversations as reference)
> - Sends the reply automatically — **NO human approval needed for routine cases**
> - Logs everything for Sara to review in the morning
>
> Sara only interacts with the system to **configure** it, not to operate it.

---

## 🎨 Your task

Design the architecture. Use draw.io, Excalidraw, ASCII, or paper.

You must show and label:

1. ✅ Where the **app (host)** runs
2. ✅ Where the **MCP servers** run
3. ✅ How **incoming WhatsApp messages** reach your system (hint: webhooks)
4. ✅ The **3 MCP servers** you'd need:
   - WhatsApp send/receive
   - Listings database
   - Conversation history (so AI can mimic Sara's style)
5. ✅ A **Rule Engine** (replaces the per-message Permission Layer for autonomous flow)
6. ✅ The **transports** between client and each server
7. ✅ Sara's **admin UI** (where she manages numbers, listings, rules)

---

## 🧠 The tricky bits to think through

### 🌐 Local vs Cloud — which fits "autonomous"?

| | Local on Sara's laptop | Cloud hosted |
|---|---|---|
| Webhook works? | ❌ Needs ngrok tunnel, fragile | ✅ Public URL, reliable |
| Replies at 3 AM? | ❌ Laptop closed = no reply | ✅ Server runs 24/7 |
| Multiple agents? | ❌ One install per agent | ✅ Many agents, one system |
| SaaS-able? | ❌ | ✅ |

**Autonomous + webhook-driven = needs cloud.** Local just doesn't fit this use case.

### 🔌 Transports — what's the rule?

> Same machine → stdio. Different machines → HTTP.

For a smart SaaS design: put **everything on the same cloud machine** (web app + MCP servers) and use **stdio** between them. Fast, free, secure.

### 🛡️ Permission layer changes shape

Old design: ask Sara before every action.
New design: **Rule Engine** — Sara sets rules ONCE, the engine enforces them on every message. Trust shifts from per-action to per-policy.

Example rules Sara might set:
- ✅ Auto-reply property inquiries
- ✅ Auto-share listing photos
- ⚠️ Flag price negotiations for Sara to review
- ❌ Never share Sara's personal phone number

---

## 💡 Optional: Add notification flow

For bonus points, show how the system **notifies Sara** if a message needs her attention (e.g., a price negotiation triggers a flag). Email? SMS to her real number? In-app notification?

---

## ✅ When done

Save your architecture diagram as `my-autonomous-design.png` (or `.md`) in this folder.

Compare your design against [`05-example-architectures.md`](05-example-architectures.md) — the second example shows a worked-out autonomous cloud architecture. **Don't peek until you've tried yours first.**

---

## 🎯 Why this exercise matters

You're designing a real, sellable SaaS product. The architecture you sketch here is essentially what companies like Botpress, Twilio Studio, and Chatbase charge serious money for. Your edge: GCC-specific, Arabic-aware, real-estate-focused.

When you reach **Day 10 (Capstone)**, this exact design becomes your roadmap. 🎯

Done? Move on to [`04-quiz.md`](04-quiz.md).
