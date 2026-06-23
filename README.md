# 🎓 10-Day MCP Mastery Plan

> My self-taught journey through the **Model Context Protocol (MCP)** — I'm [@muhammadanask880](https://github.com/muhammadanask880), and I'm building this course day-by-day as I learn, so anyone can follow the same path.

[![Status](https://img.shields.io/badge/status-in%20progress-blue)]()
[![Day 3](https://img.shields.io/badge/Day%203-complete-brightgreen)]()

---

## 📖 What is this?

A **complete 10-day curriculum** that takes a total beginner from *"what is MCP?"* to **shipping their own working MCP server** in production.

Every day follows the same rhythm:
- 🎯 Clear learning objectives
- 📚 Concept explanations (analogy → definition → diagram → code → real-world example)
- 🧪 Hands-on practice
- 🛠️ A mini-project that combines the day's concepts
- 📝 A 5-question quiz
- 🔁 Recap and tomorrow's preview

## 👤 Who is this for?

- **Solo builders** who want to ship AI agents that actually do things
- **Developers** new to MCP who want a structured path instead of jumping between scattered docs
- **Anyone** curious about how AI assistants like Claude, ChatGPT, and Cursor talk to the rest of the world

No prior MCP knowledge required. Basic comfort with reading code is enough.

---

## 🚀 How to use this course

You have three solid options — pick whichever fits your budget and style:

### Option A — Free, with web Claude
1. Clone or download this repo.
2. Open the current day's folder (start with [`day-01/`](day-01/)).
3. Read the `README.md` in that folder. It tells you exactly how to study that day.
4. When stuck, open https://claude.ai (free tier works fine) and ask.

### Option B — With Claude Code (paid CLI, more powerful)
1. Clone the repo into a working folder.
2. Run `claude` in that folder.
3. Tell Claude Code: *"You are my MCP tutor. Read MCP_COURSE_PLAN.md and start Day X."*
4. Claude Code can read files, run servers, and write code with you in real time.

### Option C — Any other LLM (Gemini, ChatGPT, etc.)
The lesson content is plain Markdown. Paste a day's `01-lessons.md` into any LLM and learn from there. Self-evaluation instructions in each day's README work with any model.

---

## 🗺️ The 10-Day Plan

See [MCP_COURSE_PLAN.md](MCP_COURSE_PLAN.md) for the full table. Quick view:

| Day | Topic | Status |
|-----|-------|--------|
| [01](day-01/) | What MCP Is & Why It Exists | ✅ Complete |
| [02](day-02/) | MCP Architecture (Hosts, Clients, Servers, Transports) | ✅ Complete |
| [03](day-03/) | JSON-RPC: The Language Underneath | ✅ Complete |
| 04 | Tools (Deep Dive) | 🚧 Coming |
| 05 | Resources + Prompts | ⬜ |
| 06 | Initialization Handshake & First Real Server | ⬜ |
| 07 | MCP Clients + Plugging Into Claude | ⬜ |
| 08 | Security, Auth, Permissions, Sandboxing | ⬜ |
| 09 | Errors, Logging, Debugging + Advanced | ⬜ |
| 10 | Publishing + Capstone | ⬜ |

New days are published as the author completes them. Star the repo to get notified.

---

## 🧠 The "self-evaluate" pattern

At the end of every day's quiz, do this:

> Open your favorite LLM (Claude, Gemini, GPT). Paste in:
> 1. The day's `01-lessons.md`
> 2. The day's `04-quiz.md`
> 3. Your own answers
>
> Ask: *"Here is the course content, here are the quiz questions, and here are my answers. Please grade me out of 5 and tell me what I missed."*

This turns any AI into your personal tutor and works for free. 🎯

---

## 📂 Repo structure

```
MCP-Course/
├── README.md                ← this file
├── MCP_COURSE_PLAN.md       ← the 10-day overview
├── day-01/                  ← Day 1 (complete)
│   ├── README.md            ← how to study this day
│   ├── 01-lessons.md
│   ├── 02-practice.md
│   ├── 03-mini-project.md
│   ├── 04-quiz.md
│   └── 05-example-memo.md
├── day-02/                  ← Day 2 (complete)
│   ├── README.md
│   ├── 01-lessons.md
│   ├── 02-practice.md
│   ├── 03-mini-project.md
│   ├── 04-quiz.md
│   └── 05-example-architectures.md
├── day-03/                  ← Day 3 (complete — with runnable code!)
│   ├── README.md
│   ├── 01-lessons.md
│   ├── 02-practice.md
│   ├── 03-mini-project.md
│   ├── 04-quiz.md
│   ├── 05-example-echo-server.md
│   └── echo-server/         ← runnable Python JSON-RPC server
│       ├── server.py
│       └── test_client.py
└── day-04/  (coming)
    └── ...
```

Every day folder follows the same shape. Predictable for learners.

---

## 🤝 Contributing / Feedback

Spot an error? Have a better analogy? Open an issue or a PR. This is a learning resource — improvements welcome.

## 📜 License

MIT — use it, fork it, teach with it, build on it.

---

*Built while learning, taught while building.*
