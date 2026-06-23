# 📝 Day 3 Quiz — 5 Questions

Answer all 5 in your own words. **Don't peek at the lessons until you've tried.**

---

### Question 1
Name the **three types** of JSON-RPC messages and what makes each one different.

---

### Question 2
A **notification** is missing one specific field that every request has. **Which field**, and what does its absence mean for the receiver?

---

### Question 3
What does error code **`-32601`** mean? Give the standard meaning + when you'd see it.

---

### Question 4 — Scenario
Your client sends 3 requests one after another in 10 milliseconds. The server returns 3 responses, but in a **different order** than the requests went out.

**How does the client know which response belongs to which request?**

---

### Question 5 — Bug spotting
A teammate shows you this server response. **What's wrong with it** in one sentence?

```json
{
  "jsonrpc": "2.0",
  "id": 5,
  "result": { "value": 42 },
  "error": { "code": -32603, "message": "Something went wrong" }
}
```

---

## 🎯 Self-evaluation prompt

Copy this into Claude/Gemini/GPT:

> *"I am studying a self-paced MCP course. Below is (1) the lesson content for Day 3, (2) the quiz questions, and (3) my own answers. Please:*
> *— Grade each answer out of 1 (so total out of 5).*
> *— Tell me clearly what I missed or got partially right.*
> *— Suggest one better way to phrase any weak answer.*
> *— End with one curiosity question to take into Day 4.*
>
> *=== LESSON CONTENT === [paste 01-lessons.md]*
> *=== QUIZ === [paste this file]*
> *=== MY ANSWERS === [paste your answers]*"

---

## 🏆 Passing bar

- **5/5** → Excellent. JSON-RPC is locked in.
- **4/5** → Strong pass. Re-read the one you missed and move on.
- **3/5** → Re-read `01-lessons.md` for the two weakest spots before Day 4.
- **≤2/5** → Pause. Take a break. The 3-message-types distinction is the foundation; everything else builds on it. Worth re-reading fresh tomorrow.
