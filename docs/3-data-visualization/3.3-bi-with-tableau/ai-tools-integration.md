# Using AI Tools with Tableau

**After this lesson:** you can use Claude Desktop or ChatGPT as an AI pair partner while building Tableau dashboards — writing calculated fields faster, debugging LOD expressions, generating practice data, and getting chart recommendations without leaving your workflow.

Tableau's calculation language is powerful, but debugging a formula can eat 30 minutes. This guide shows you two ways to set up AI assistance, from zero-setup copy-paste to a full MCP integration where Claude can talk directly to your Tableau workbooks.

| Problem you have | Use this workflow | Time saved |
|-----------------|-------------------|------------|
| Can't write a calculated field | Workflow 1: Calculated Fields | 5–15 min |
| LOD expression keeps erroring | Workflow 2: LOD Debugging | 10–20 min |
| Need realistic test data | Workflow 3: Sample Data | 10 min |
| CSV has messy data | Workflow 4: Python Prep | 20–30 min |
| Unsure which chart to use | Workflow 5: Chart Recommendations | 5 min |

---

## Setup Options

There are two ways to connect AI tools to Tableau. Start with Option A (no setup needed), and upgrade to Option B if you want Claude to query your live workbooks and data sources.

| | Option A: Copy-paste | Option B: Claude Desktop + MCP |
|---|---|---|
| **Setup time** | Zero | ~10 minutes |
| **Works with** | Claude Desktop, ChatGPT, any AI chat | Claude Desktop only |
| **What AI can access** | Only what you paste | Your Tableau Server / Cloud workbooks, data sources, and views directly |
| **Best for** | Quick formula help, one-off questions | Iterative dashboard work, querying live workbooks |

---

## Option A: Copy-Paste (No Setup)

Open Claude or ChatGPT in a browser tab or window alongside Tableau Desktop. Paste your question, formula, or error message directly into the chat. No configuration required.

| Tool | Where to open |
|------|--------------|
| **Claude** | [claude.ai](https://claude.ai) — web or install the Claude Desktop app |
| **ChatGPT** | [chatgpt.com](https://chatgpt.com) — web or the ChatGPT desktop app |

> **Tip:** Paste your exact field names from the Data pane — AI gives much better output when it knows whether your field is called `[Revenue]` or `[Sales]`.

Skip straight to [Practical workflows](#practical-workflows) to start using this now.

---

## Option B: Claude Desktop + Tableau MCP Integration

The [Model Context Protocol (MCP)](https://modelcontextprotocol.io) lets Claude Desktop connect directly to external tools. Tableau's official MCP server lets Claude query your Tableau Server or Tableau Cloud workbooks, data sources, and views without you having to copy-paste anything.

### What you can do with the integration

- Ask Claude "What workbooks do I have?" and get a list back
- Paste a view name and ask Claude to describe the data schema
- Let Claude pull a data source's field list automatically when you ask for a formula — no manual copying

### Prerequisites

- **Claude Desktop** installed ([download here](https://claude.ai/download))
- Access to **Tableau Server** or **Tableau Cloud** (the MCP server uses the Tableau REST API, which is not available in Tableau Public)
- A **Personal Access Token (PAT)** from your Tableau site

> **Tableau Public users:** Tableau Public does not expose the REST API, so Option B is not available. Use Option A (copy-paste) instead.

### Step 1 — Create a Personal Access Token in Tableau

1. Sign in to Tableau Server or Tableau Cloud.
2. Click your profile icon (top right) → **My Account Settings**.
3. Scroll to **Personal Access Tokens** → click **Create new token**.
4. Give it a name (e.g. `claude-mcp`) and copy the **token secret** — you will not see it again.

### Step 2 — Install the Tableau MCP server

The Tableau MCP server is published as an npm package. Run the following once from your terminal to verify Node.js is installed and working:

```bash
node --version   # should be v18 or later
npx --version
```

If you don't have Node.js, install it from [nodejs.org](https://nodejs.org) (LTS version).

### Step 3 — Configure Claude Desktop

Open the Claude Desktop configuration file. On macOS:

```bash
open ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

If the file does not exist, create it. Add the Tableau server block inside `mcpServers` — replace the placeholder values with your actual credentials:

```json
{
  "mcpServers": {
    "tableau": {
      "command": "npx",
      "args": ["-y", "@salesforce/mcp-server-tableau"],
      "env": {
        "TABLEAU_SERVER_URL": "https://your-tableau-server.com",
        "TABLEAU_SITE_ID": "your-site-id",
        "TABLEAU_TOKEN_NAME": "claude-mcp",
        "TABLEAU_TOKEN_VALUE": "your-token-secret-here"
      }
    }
  }
}
```

> **Finding your values:**
> - `TABLEAU_SERVER_URL` — the base URL you use to sign in, e.g. `https://10ax.online.tableau.com`
> - `TABLEAU_SITE_ID` — found in the URL after `/site/` when signed in; leave as `""` for the default site
> - `TABLEAU_TOKEN_NAME` — the name you gave the PAT in Step 1
> - `TABLEAU_TOKEN_VALUE` — the secret you copied in Step 1

### Step 4 — Restart Claude Desktop and verify

Quit and reopen Claude Desktop. You should see a hammer icon (🔨) in the chat input bar, indicating MCP tools are active.

Test the connection by typing:

```
List my Tableau workbooks.
```

Claude should return a list of workbooks from your site. If you get an error, double-check your server URL and token values in the config file.

> **Package name note:** Tableau's MCP tooling is actively developed. If `@salesforce/mcp-server-tableau` is not found, check the current package name at the [Tableau Developer documentation](https://developer.salesforce.com/docs/tableau) or the [Salesforce MCP GitHub](https://github.com/salesforce/mcp).

---

## ChatGPT Setup

ChatGPT does not yet support MCP-based integrations with Tableau. Use the copy-paste workflow (Option A) alongside the following tips to get the most out of it.

### Using ChatGPT effectively with Tableau

**Upload your data schema:** Export a small CSV sample from your Tableau data source (right-click a data source → **View Data** → **Export**). Attach the CSV to ChatGPT so it can see your exact field names without you listing them manually.

**Use the Data Analyst mode:** In ChatGPT, select **GPT-4o** and attach a CSV. ChatGPT can run Python internally to verify that a formula or aggregation gives the right output before you paste it into Tableau.

**Paste error messages directly:** Tableau's error text is often cryptic. Copy the full error (including the formula that caused it) and paste it into ChatGPT — it will usually identify the problem and offer a corrected version.

---

## Practical Workflows

The prompts below work with both Option A (copy-paste) and Option B (MCP). With Option B, you can skip the step where you manually describe your fields — Claude can read them from the connected workbook.

### Workflow 1: Write a calculated field

Tableau's calculation language is expressive but the syntax is easy to get wrong. Describe what you need and paste the result into **Create Calculated Field**.

**Example prompt:**

```
I'm working in Tableau with an Orders table that has Sales, Profit, and Discount fields.
Write a calculated field that returns the net margin as a percentage, formatted for display.
```

**Claude's output** (paste directly into Tableau):

```
SUM([Profit]) / SUM([Sales])
```

Format the field as **Percentage** via the field's default number format. For a label-ready string version:

```
STR(ROUND(SUM([Profit]) / SUM([Sales]) * 100, 1)) + "%"
```

---

### Workflow 2: Debug an LOD expression

LOD (Level of Detail) expressions are powerful but frequently produce unexpected totals. Paste the broken expression plus a description of what it should do.

**Example prompt:**

```
This Tableau LOD expression returns wrong numbers when I add a Region filter:
{FIXED [Customer ID] : MIN([Order Date])}
I want it to show each customer's first order date, filtered by the current Region selection.
```

Claude will explain why `FIXED` ignores dimension filters and show you how to add a **context filter** or rewrite it using `INCLUDE`:

```
{INCLUDE [Region] : MIN([Order Date])}
```

---

### Workflow 3: Generate a sample dataset

Use Claude to create CSV data when you want to practice a specific chart type without waiting for real data.

**Example prompt:**

```
Generate a CSV with 50 rows of fictional retail sales data suitable for Tableau practice.
Include: Order ID, Order Date (2023–2024), Region (East/West/North/South),
Category (Furniture/Technology/Office Supplies), Sales (numeric), Profit (numeric).
```

Save the output as `sample_sales.csv` and connect via **Text File** in Tableau's Connect pane.

---

### Workflow 4: Prepare data with Python before connecting

Tableau works best with clean, wide-format data. Ask Claude to write a pandas script to reshape or clean your source file.

**Example prompt:**

```
I have a CSV with columns: date, product, region, revenue.
Some revenue values are empty strings instead of NaN.
Write a pandas script that cleans the data and pivots it so each region
becomes its own column, ready to connect in Tableau.
```

Run the script, save the output, then connect Tableau to the cleaned file.

---

### Workflow 5: Choose the right chart type

Describe your data and analytical question; Claude recommends a Tableau chart type and the shelf configuration.

**Example prompt:**

```
I want to show how profit margin has changed month-over-month for three product categories.
What chart type should I use in Tableau, and how do I set it up?
```

**Sample AI response:**

> **Recommended chart type:** Multi-line chart (one line per category)
>
> **Shelf configuration:**
> - **Columns:** `Order Date` (set to continuous Month/Year)
> - **Rows:** Your profit margin calculated field, e.g. `SUM([Profit]) / SUM([Sales])`
> - **Color:** `Category` (drag to the Color mark — Tableau will draw one line per category)
> - **Marks:** Line
>
> **To set it up:**
> 1. Create the calculated field `SUM([Profit]) / SUM([Sales])` and format it as Percentage.
> 2. Drag `Order Date` to Columns, right-click → **Month** (continuous, not discrete).
> 3. Drag your calculated field to Rows.
> 4. Drag `Category` to the Color mark card.
>
> **Verify the result:** You should see three coloured lines trending over time. Check that the Y-axis range is sensible (e.g. -10% to 30%) and that the lines diverge or converge in ways that match what you'd expect from the raw numbers. If all three lines overlap exactly, double-check that `Category` landed on Color (not Rows or Columns).

---

## Debugging checklist

Before assuming AI gave you a bad formula, work through these:

- [ ] **Formula copied with surrounding explanation text** → paste only the formula line(s) into Tableau's calculated field editor; strip any plain-English sentences Claude added around it
- [ ] **Field names don't match your Data pane** → your prompt used generic names (e.g. `[Revenue]`) but your field is called `[Sales]`; re-prompt with your exact field names, or do a find-and-replace in the formula before pasting
- [ ] **Calculated field result looks wrong on the view** → Claude's formula may be correct in isolation but aggregate differently with multiple dimensions present; drag the field onto a fresh sheet with only one dimension and compare against a known total
- [ ] **`FIXED` LOD ignores your filter** → `FIXED` expressions bypass dimension filters by design; right-click the filter pill in the Filters shelf → **Add to Context**, then re-test; alternatively re-prompt Claude asking for a version using `INCLUDE` instead
- [ ] **Working offline and Claude is unavailable** → use a formula you saved from a previous session in a local notes file; the Tableau calculated field reference at `help.tableau.com` also covers all functions without needing a connection

## Additional resources

- [Claude Desktop download](https://claude.ai/download)
- [Model Context Protocol documentation](https://modelcontextprotocol.io)
- [Tableau Developer documentation](https://developer.salesforce.com/docs/tableau)
- [Tableau Personal Access Tokens](https://help.tableau.com/current/server/en-us/security_personal_access_tokens.htm)
- [Tableau calculated fields reference](https://help.tableau.com/current/pro/desktop/en-us/calculations_calculatedfields_create.htm)
- [Tableau LOD expressions](https://help.tableau.com/current/pro/desktop/en-us/calculations_calculatedfields_lod.htm)
