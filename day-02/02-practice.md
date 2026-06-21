# 🧪 Day 2 Practice — Draw the Architecture

**Time:** 5–15 minutes
**Goal:** Take everything you learned today and **draw it yourself**. Drawing forces concepts into visual memory.

---

## 📋 Your task

Draw the full architecture for this scenario:

> *You're using **Claude Desktop**. You've configured it with a **weather MCP server** (runs locally via `npx`) and a **Postgres MCP server** (runs locally via `npx`).*

Your drawing must show and label:

1. ✅ The **host** (which one?)
2. ✅ The **Chat UI** inside the host
3. ✅ The **LLM connection** (which model?)
4. ✅ How many **clients**? Label each
5. ✅ The **Permission Layer**
6. ✅ The two **servers** (outside the host)
7. ✅ Which **transport** each server uses
8. ✅ Draw the **trust boundary** clearly (a wall, dashed line, anything)

---

## 🛠️ Tools to use

Pick whatever feels comfortable:

- 🎨 **[draw.io](https://app.diagrams.net/)** — free, browser-based, great for boxes & arrows
- ✏️ **[Excalidraw](https://excalidraw.com/)** — clean, hand-drawn feel, free
- 📝 **ASCII art** — type into a `.md` file (like the diagrams in this course)
- 📄 **Pencil & paper** — totally fine

---

## 🧠 Hints (only peek if stuck)

<details>
<summary>Hint 1 — what host?</summary>

The scenario says "Claude Desktop." That's your host. One big outer box labeled "Claude Desktop HOST".
</details>

<details>
<summary>Hint 2 — how many clients?</summary>

Two servers → two clients. The 1:1 rule from sub-topic 2.2.
</details>

<details>
<summary>Hint 3 — what transport?</summary>

Both servers run via `npx` on the same laptop as Claude Desktop → same machine → **stdio** for both.
</details>

---

## ✅ When done

Save your drawing as `my-practice-architecture.png` (or `.md` if ASCII) in this folder.

**Bonus:** add **two annotations** to your diagram:
- ➡️ One showing where the permission layer would catch a risky outbound call (e.g., *"AI tries to DELETE rows → permission asks user"*)
- ⬅️ One showing where the host would treat server output as untrusted (e.g., *"server returns prompt-injection text → host doesn't blindly act on it"*)

These two annotations show you understand the **bidirectional trust boundary**. Adding them = senior-level thinking.

---

## 📚 Need an example for inspiration?

See [`05-example-architectures.md`](05-example-architectures.md) for two worked examples (a basic one and an advanced autonomous cloud one).

Done? Move on to [`03-mini-project.md`](03-mini-project.md).
