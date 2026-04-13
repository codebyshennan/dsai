# Using AI Tools with Tableau

**After this lesson:** you can use Claude Desktop or ChatGPT as an AI pair partner while building Tableau dashboards — writing calculated fields faster, debugging LOD expressions, generating practice data, and getting chart recommendations without leaving your workflow.

Tableau's calculation language is powerful, but debugging a formula can eat 30 minutes. This guide shows you how to use Claude or ChatGPT as a pair partner — paste your question, get working syntax back, verify it in Tableau. No special setup needed.

| Problem you have | Use this workflow | Time saved |
|-----------------|-------------------|------------|
| Can't write a calculated field | Workflow 1: Calculated Fields | 5–15 min |
| LOD expression keeps erroring | Workflow 2: LOD Debugging | 10–20 min |
| Need realistic test data | Workflow 3: Sample Data | 10 min |
| CSV has messy data | Workflow 4: Python Prep | 20–30 min |
| Unsure which chart to use | Workflow 5: Chart Recommendations | 5 min |

## Which AI tool should I use?

You don't need a special integration. Any conversational AI assistant works:

| Tool | How to access |
|------|--------------|
| **Claude Desktop** | [claude.ai](https://claude.ai) — desktop app or web |
| **ChatGPT** | [chatgpt.com](https://chatgpt.com) — web or desktop app |

Open either tool in a browser tab or window next to Tableau Desktop. You can paste errors, formula fragments, or plain-English questions directly into the chat.

**Why pair AI with Tableau?**

- Write and debug calculated fields and LOD expressions without memorising every function
- Generate realistic sample datasets when you don't have real data to hand
- Prepare and clean data in Python/pandas before connecting to Tableau
- Get instant chart-type recommendations given your data shape and goal
- Explain Tableau errors in plain language

## Practical workflows

### Workflow 1: Write a calculated field

Tableau's calculation language is expressive but the syntax is easy to get wrong. Describe what you need and paste the result into **Create Calculated Field**.

![Tableau Create Calculated Field dialog showing a Profit Ratio formula](assets/tableau_calculated_field.png)

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

![Tableau LOD expression editor showing a FIXED expression and context filter](assets/tableau_lod.png)

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

- [Claude Code documentation](https://docs.anthropic.com/en/docs/claude-code)
- [Tableau calculated fields reference](https://help.tableau.com/current/pro/desktop/en-us/calculations_calculatedfields_create.htm)
- [Tableau LOD expressions](https://help.tableau.com/current/pro/desktop/en-us/calculations_calculatedfields_lod.htm)
