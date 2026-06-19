# 🎓 10-Day MCP Mastery Plan

> A complete journey from "what is MCP?" to shipping your own MCP server.
> Tailored for a solo builder in the GCC market — focus on things you can actually ship (WhatsApp agents, property scrapers, support bots) on free-tier infrastructure.

---

## 📅 Full Plan at a Glance

| Day | Topic | Sub-topics | Practice | Mini-project |
|-----|-------|------------|----------|--------------|
| **1** | **What MCP Is & Why It Exists** | 1.1 The "M×N problem" before MCP · 1.2 What MCP stands for · 1.3 Analogy: the USB-C port for AI · 1.4 Who made it & where it fits | Read 1 real MCP server's README and identify what it does | Write a 1-page "Why MCP matters for my project" memo |
| **2** | **MCP Architecture** | 2.1 Hosts (Claude Desktop, Claude Code, IDEs) · 2.2 Clients · 2.3 Servers · 2.4 Transports: stdio, HTTP, SSE · 2.5 The trust boundary | Draw the architecture for a Claude Desktop ↔ weather server setup | Build an ASCII architecture diagram for a future WhatsApp-MCP idea |
| **3** | **JSON-RPC: The Language Underneath** | 3.1 What JSON-RPC 2.0 is · 3.2 Requests, responses, notifications · 3.3 IDs, methods, params, results, errors · 3.4 Reading raw MCP traffic | Hand-write 3 JSON-RPC messages on paper | Build a tiny JSON-RPC echo server (no MCP yet) |
| **4** | **Primitive #1: Tools (Deep Dive)** | 4.1 What a tool is · 4.2 `tools/list` and `tools/call` · 4.3 Input schemas (JSON Schema basics) · 4.4 Return shapes · 4.5 When the model decides to call a tool | Write input schemas for 3 imagined tools | Build a `calculator` MCP server with 4 tools |
| **5** | **Primitives #2 & #3: Resources + Prompts** | 5.1 Resources vs Tools (read-only data) · 5.2 URIs and `resources/list` · 5.3 Prompts as reusable templates · 5.4 When to pick which primitive | Convert a "tool" into a "resource" and explain why | Build a `notes` server with resources (your saved notes) + a prompt template |
| **6** | **Initialization Handshake & First Real Server** | 6.1 The `initialize` message · 6.2 Capability negotiation · 6.3 Server lifecycle (start → ready → shutdown) · 6.4 Building a full server end-to-end | Step through a real handshake byte-by-byte | Build a `property-scraper-lite` MCP server (mock data) |
| **7** | **MCP Clients + Plugging Into Claude** | 7.1 What a client really does · 7.2 Connecting a server to Claude Desktop (config file) · 7.3 Connecting to Claude Code · 7.4 Testing with MCP Inspector | Wire your Day 6 server into Claude Desktop & chat with it | Add your scraper server to Claude Code and use it in a real task |
| **8** | **Security, Auth, Permissions, Sandboxing** | 8.1 The trust model · 8.2 Why "tools can do anything" is scary · 8.3 OAuth flows for remote servers · 8.4 Secret handling · 8.5 Input validation & prompt injection | Audit your Day 6 server for 3 security holes and fix them | Add API-key auth to a remote-style MCP server |
| **9** | **Errors, Logging, Debugging + Advanced Features** | 9.1 JSON-RPC error codes · 9.2 Logging without breaking stdio · 9.3 Debugging with Inspector · 9.4 Sampling (server asks model) · 9.5 Roots, progress notifications, cancellation | Break your server 3 ways on purpose, then fix each | Add progress notifications + cancellation to your scraper |
| **10** | **Publishing + Capstone** | 10.1 Packaging (npm/pip/uv) · 10.2 README essentials · 10.3 Sharing & discoverability · 10.4 **Capstone**: design + build + ship a useful MCP server | Publish a tiny test package | **Capstone**: a real MCP server you'd actually use (e.g., WhatsApp message drafter, Dubai property listing scraper, or GCC customer-support knowledge base) |

---

## 🧭 How Each Day Runs

Every day follows the same rhythm so it stays predictable:

1. 🎯 **Objectives** — what you'll be able to do by end of day
2. 📚 **Concepts** — explained with analogy → definition → diagram → code → real-world example
3. 🧪 **Hands-on practice** — at least one exercise you do yourself
4. 🛠️ **Mini-project** — combines everything from the day
5. 📝 **5-question quiz** — locks knowledge in
6. 🔁 **Recap + tomorrow's preview**

## 🛠️ Tools You'll Need (we'll install when needed)
- Python 3.10+ **or** Node.js 18+ (we'll pick on Day 4)
- A code editor (VS Code works great)
- Claude Desktop and/or Claude Code (you already have Claude Code)
- The MCP Inspector (a debugging UI — we'll meet it on Day 7)

## 🎯 What You'll Be Able to Do at the End
- Explain MCP to another developer in 60 seconds
- Read raw MCP traffic and understand it
- Build, test, secure, and publish your own MCP servers
- Ship at least one MCP server connected to real workflows in your business
