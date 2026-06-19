# Example Memo — For Inspiration Only

> ⚠️ **Don't copy this. Read it, then close the file and write your own.** The whole point of the mini-project is the thinking, not the output.

This is a real memo written by [@muhammadanask880](https://github.com/muhammadanask880) (a solo builder in the GCC market) on Day 1 of his MCP journey.

---

# Why MCP Matters for My Business
*Day 1 reflection — 2026-06-19*

## 1. The pain I used to face (or would have faced) without MCP

If I built a Slack automation today and tomorrow my client said *"switch to ChatGPT,"* I'd have to rewrite every single tool integration from scratch. For 5 tools × 2 LLMs, that's 10 implementations instead of 5. Multiply by every new LLM that drops next year, and the work compounds — but I'm still one person. That's the M×N problem in my world.

## 2. What MCP changes for me as a solo builder

I build my tools once as an MCP server. Switching from Claude to ChatGPT becomes a config edit, not a code rewrite. My time moves from **plumbing to product** — better tools, better prompts, faster shipping.

## 3. One project idea I could build using MCP

**`dubizzle-scout`** — an MCP server that scrapes Dubai property listings (Dubizzle/Bayut) and lets the AI organize them. One MCP server, multiple tools inside it:

- `search_listings(area, max_price, bedrooms)`
- `get_listing_details(url)`
- `save_to_notebook(listing, notebook_name)`

The AI (Claude or ChatGPT) orchestrates these tools to do the actual work — find new 2BHK listings in Marina under 100k AED/year, pull details, save them to a notebook. Plus optionally draft a WhatsApp reply to the landlord.

## 4. Which MCP server(s) would I plug into for that idea?

- **Postgres MCP server** (read-only) — store/query already-scraped listings. The read-only design protects data from accidental writes by the AI.
- **Google Sheets MCP server** (custom build) — list available sheets, read contents, find the relevant sheet, write/update rows. Useful for clients who live in spreadsheets.
- **`dubizzle-scout` server** — the scraping logic itself.
- **Future: WhatsApp BSP wrapper** (Wati / 360dialog) — for sending landlord outreach. Capstone candidate.

## 5. My one-sentence pitch for MCP to a non-technical client

> *"We build the smart parts once; whichever AI you prefer — Claude, ChatGPT, or whatever comes next — it just plugs in. No rewrite, no vendor lock-in, no surprise bills."*

---

## 🧠 What's strong about this memo

1. **Real numbers** — "5 tools × 2 LLMs = 10 implementations". Not vague.
2. **A specific project name** — `dubizzle-scout`. Easier to imagine.
3. **The phrase "plumbing to product"** — punchy and memorable.
4. **The client pitch uses no jargon** — "no vendor lock-in, no surprise bills" lands in business meetings.

Now go write yours. 💪
