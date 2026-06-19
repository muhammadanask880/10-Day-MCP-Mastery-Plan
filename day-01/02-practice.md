# 🧪 Day 1 Practice — Explore a Real MCP Server

**Time needed:** 5–10 minutes
**Goal:** Get today's concepts out of your head and into the real world by looking at an actual MCP server.

---

## 📋 Your task

Open this page in your browser:

🔗 **https://github.com/modelcontextprotocol/servers**

This is the official collection of example MCP servers. Pick **ONE** that interests you most. Beginner-friendly options:

| Server | What it does | Good if you care about |
|--------|--------------|------------------------|
| `filesystem` | Read/write files in a folder | Local file workflows |
| `fetch` | Fetch web pages | Web scraping |
| `brave-search` | Search the web | Research agents |
| `postgres` | Query a database (read-only) | Data analysis |
| `sqlite` | Same, for tiny local DBs | Embedded apps |
| `slack` | Read/post Slack messages | Team automation |
| `google-drive` | Read Google Drive files | Document workflows |

---

## 🎯 What to look for (don't just skim)

While reading your chosen server's README, answer these in your own words:

1. **What does this server do** in one sentence?
2. **What tools does it expose?** (look for a section listing tools)
3. **How is it installed?** (usually `npx`, `pip`, or `docker`)
4. **Who would use this** in a real project?

Spend **5–10 minutes max**. Don't try to understand every line — just absorb the *shape* of a real MCP server.

---

## 📝 Write down your findings

Create a file `my-practice-notes.md` in this folder with:

```markdown
# Day 1 Practice — Server I Explored

**Server:** ____________
**Link:** ____________

## 1. What it does
[one sentence]

## 2. Tools it exposes
- tool_name_1
- tool_name_2
- ...

## 3. How to install
[the command from the README]

## 4. Who would use it
[real-world use case]

## 5. One thing I didn't understand
[a concept or word — we'll revisit it later]
```

---

## 💡 Tip — what to notice

As you read, look for:

- **Tool names follow a pattern** — usually `{service}_{verb}_{thing}` (e.g., `slack_post_message`, `postgres_query`).
- **Servers often require secrets** — API keys, tokens, OAuth scopes. This sets up Day 8 (security).
- **The install command tells you the "transport"** — `npx` means local stdio (Day 2 material!).

Done? Move on to [`03-mini-project.md`](03-mini-project.md).
