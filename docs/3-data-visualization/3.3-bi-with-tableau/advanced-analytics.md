# Taking Your Tableau Skills to the Next Level

**After this lesson:** you can explain the core ideas in “Taking Your Tableau Skills to the Next Level” and reproduce the examples here in your own notebook or environment.

> **Note:** This lesson is **UI-first** (Tableau Desktop or comparable). You should already know worksheets, filters, and simple calculations from [Tableau basics](tableau-basics.md).

## Helpful video

Short Tableau Public install; pair with the written guides in this folder.

<iframe width="560" height="315" src="https://www.youtube.com/embed/lTNWfhmurUg" title="Tableau Public Tutorial Download and Setup" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Introduction: Beyond the Basics

Now that you're comfortable with basic charts and dashboards, let's explore some powerful features that will make your visualizations even better! Think of this as upgrading from a basic calculator to a scientific calculator - more buttons, but so much more you can do!

## 1. Table Calculations: Making Your Numbers Smarter

### What Are Table Calculations?

Think of them as Excel formulas that work across your entire visualization. They help you:

- Compare values over time
- Calculate growth rates
- Rank and analyze performance

### Common Table Calculations (With Real Examples!)

#### Running Total (Like a Growing Bank Balance)

**Purpose:** Express a cumulative sum of sales along the visualization’s sort order (often date).

**Walkthrough:** `RUNNING_SUM` is Tableau’s formula language; UI steps in the comment describe Quick Table Calc.

```sql
-- Shows how sales add up over time
Running Total = RUNNING_SUM(SUM([Sales]))

Example Use:
1. Create a line chart of sales
2. Add running total:
   - Right-click the Sales pill
   - Quick Table Calculation
   - Running Total
```

#### Growth Rate (Like Calculating Interest)

**Purpose:** Compute period-over-period percent change using `LOOKUP` to read the previous mark’s value.

**Walkthrough:** `-1` in `LOOKUP` means one step back along the partition; denominator is prior period sales.

```sql
-- Shows how much something grew
Growth = 
([Sales] - LOOKUP([Sales], -1)) / 
LOOKUP([Sales], -1)

Example Use:
1. Create a bar chart of monthly sales
2. Add growth rate:
   - Right-click the Sales pill
   - Quick Table Calculation
   - Percent Difference
```

#### Moving Average (Smoothing Out the Bumps)

**Purpose:** Smooth a noisy series with a trailing window average (here three periods including current).

**Walkthrough:** `WINDOW_AVG` with `-2` to `0` averages current and two prior periods along the partition.

```sql
-- Averages last 3 periods to smooth trends
Moving Avg = 
WINDOW_AVG(SUM([Sales]), -2, 0)

Example Use:
1. Create a line chart
2. Add moving average:
   - Analytics pane
   - Drag 'Moving Average'
   - Choose 3 periods
```

## 2. Level of Detail (LOD) Expressions: The Secret Sauce

### What Are LOD Expressions?

Think of them as a way to look at your data from different angles at the same time. Like having multiple magnifying glasses!

### Types of LOD (With Examples)

#### FIXED: Look at Specific Things

**Purpose:** Compute a per-customer aggregate (here average sales) that ignores other dimensions on the sheet unless blended.

**Walkthrough:** `{FIXED [Customer Name] : ...}` pins the grain to customer; compare to table totals with `TOTAL()` or reference lines.

```sql
-- Find average order value per customer
{FIXED [Customer Name] : 
    AVG([Sales])}

Real-World Use:
1. Find big spenders
2. Compare to overall average
3. Identify VIP customers
```

#### INCLUDE: Add Extra Detail

**Purpose:** Add a dimension to the LOD grain beyond what the view already groups by—here product within each region context.

**Walkthrough:** `INCLUDE` increases detail relative to the view; use when the view is coarser than the aggregation you need.

```sql
-- Sales by product within each region
{INCLUDE [Product]: 
    SUM([Sales])}

When to Use:
1. Comparing product performance
2. Finding regional favorites
3. Spotting trends
```

#### EXCLUDE: Remove Some Detail

**Purpose:** Compute an aggregate at a coarser level by stripping a dimension from the LOD (e.g. company average without region).

**Walkthrough:** `EXCLUDE [Region]` removes region from the inner aggregation; compare to per-region marks.

```sql
-- Overall average excluding regions
{EXCLUDE [Region]: 
    AVG([Sales])}

Perfect For:
1. Company-wide metrics
2. Removing seasonal effects
3. Overall trends
```

## 3. Advanced Charts: Making Your Data Beautiful

### Combo Charts (Two Charts in One!)

**Purpose:** Combine bar and line (or other mark types) on shared time or category axes with dual axes when scales differ.

**Walkthrough:** Dual axis aligns two measures; synchronize or not depending on whether scales are comparable.

```yaml
Steps to Create:
1. Start with a bar chart
2. Drag second measure to right axis
3. Right-click → Dual Axis
4. Change mark types for each measure

Example:
- Bars for Sales
- Line for Profit
```

### Custom Charts (Be Creative!)

**Purpose:** Suggest chart types beyond defaults (dumbbell, bullet, waterfall) for comparisons and part-to-whole stories.

**Walkthrough:** Each type maps to a Tableau recipe (often dual-axis or Gantt-style marks); look up the official tutorial for your version.

```yaml
Try These Cool Ideas:
1. Dumbbell Charts:
   - Compare two points in time
   - Show before/after
   - Highlight changes

2. Bullet Charts:
   - Show targets vs actual
   - Add color bands
   - Highlight performance

3. Waterfall Charts:
   - Show how values build up
   - Track additions/subtractions
   - Visualize flow
```

## 4. Making It Interactive: Bringing Your Dashboard to Life

### Parameters (Let Users Choose!)

**Purpose:** Let viewers change thresholds, N, or dates through a control without editing the workbook.

**Walkthrough:** Parameter is a workbook object; calculated fields reference it with `[Parameter Name]`.

```yaml
Create a Parameter:
1. Right-click in Data pane
2. Create Parameter
3. Choose type (number, date, list)
4. Add to your visualization

Example Uses:
- Top N selector
- Date range picker
- Threshold setter
```

### Actions (Make Things Happen!)

**Purpose:** Link sheets—filter, highlight, or navigate—so dashboards feel like one connected app.

**Walkthrough:** Define source sheet, action type, and target; test with multi-select and clearing.

```yaml
Types of Actions:
1. Filter Actions:
   - Click map → filter table
   - Select bar → highlight related
   
2. Highlight Actions:
   - Hover → highlight connected
   - Click → emphasize related
   
3. URL Actions:
   - Click → open webpage
   - Link to details
   - Connect to docs
```

## 5. Best Practices for Advanced Analytics

### Performance Tips

**Purpose:** Reduce query load and calculation cost so large dashboards stay responsive.

**Walkthrough:** Extracts trade freshness for speed; simplify calcs; push filters and date bounds early.

```yaml
Speed Up Your Dashboard:
1. Use Extracts Instead of Live:
   - Faster performance
   - Work offline
   - Schedule updates

2. Optimize Calculations:
   - Use built-in functions
   - Minimize complexity
   - Pre-aggregate when possible

3. Filter Efficiently:
   - Use context filters
   - Apply filters early
   - Limit date ranges
```

### Design for Understanding

**Purpose:** Reinforce narrative, guidance, and visual hygiene on advanced vizzes—not only performance.

**Walkthrough:** Reference lines and annotations answer “compared to what?”; tooltips carry definitions.

```yaml
Make It Clear:
1. Add Context:
   - Reference lines
   - Annotations
   - Clear titles

2. Guide Users:
   - Instructions
   - Tool tips
   - Legend explanations

3. Keep It Clean:
   - Remove clutter
   - Use consistent colors
   - Clear hierarchy
```

## Practice Exercises to Try

**Note:** Exercise IDs 1–3 below are open-ended lab prompts—build them in Tableau (or your course sandbox); no starter workbook is bundled here.

1. **Customer Analysis Dashboard:**

   ```yaml
   Create These Charts:
   1. Customer lifetime value
   2. Purchase frequency
   3. Regional comparison
   ```

2. **Financial Performance:**

   ```yaml
   Build These Metrics:
   1. Year-over-year growth
   2. Profit margins
   3. Cost breakdown
   ```

3. **Inventory Analysis:**

   ```yaml
   Analyze These Aspects:
   1. Stock turnover
   2. Popular products
   3. Seasonal patterns
   ```

## Need Help?

- Tableau Help: [help.tableau.com](https://help.tableau.com)
- Community: [community.tableau.com](https://community.tableau.com)
- Video Tutorials: [Tableau YouTube](https://www.youtube.com/user/tableausoftware)

## Gotchas

- **`FIXED` LODs ignore dimension filters but not context filters** — a `{FIXED [Customer Name] : AVG([Sales])}` expression ignores any Region or Category filter you've added to the view, so the customer average won't change when the viewer filters. Promote filters to context filters (right-click → Add to Context) if you need the LOD to respect them.
- **Table calculations like `RUNNING_SUM` recalculate when the viewer sorts the view** — the running total is computed along the current sort order, not the data order. If a stakeholder clicks a column header to re-sort, the running total changes silently and shows a different number for the same row. Lock the sort or add a note explaining this dependency.
- **Parameters don't filter data automatically — they only feed calculations** — creating a parameter and adding it to the dashboard does nothing until a calculated field or filter references `[Parameter Name]`. Learners often add a parameter control and wonder why the view doesn't change; the parameter needs a corresponding formula that uses it.
- **`LOOKUP([Sales], -1)` for growth rate returns NULL for the first period** — because there is no prior period to look back to, the first row always shows NULL for percent difference. If your chart has many periods this is invisible, but for short date ranges (e.g., 3 months) NULL on the first bar can make it disappear or show as zero depending on how Tableau handles nulls in the mark type.
- **Combo chart axes are not synchronised by default even when they appear to overlap** — when you create a dual axis with Sales (thousands) and Profit Ratio (0–1), the y-axis scales are independent. Tableau does not warn you. Always right-click the secondary axis and inspect the scale range before publishing, otherwise the overlap is visually meaningless.

Remember:

- Start with simple calculations
- Build complexity gradually
- Practice with sample data
- Don't be afraid to experiment!
