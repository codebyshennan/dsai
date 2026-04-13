# Business Intelligence with Tableau

**After this submodule:** you can use the lessons linked below and complete the exercises that match **3.3 Business Intelligence with Tableau** in your course schedule.

## Helpful video

Short Tableau Public install; pair with the written guides in this folder.

<iframe width="560" height="315" src="https://www.youtube.com/embed/lTNWfhmurUg" title="Tableau Public Tutorial Download and Setup" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Overview

This submodule is **UI-first**: you will connect data and build views in **Tableau** (and related lessons may reference **Looker Studio** or **Power BI**) with drag-and-drop analytics instead of Python scripts.

> **Note:** Perception and chart-choice principles still apply; see [3.1 visualization principles](../3.1-intro-data-viz/visualization-principles.md) when you are unsure which visual to use.

> **Time needed:** Plan several hours across the case studies and practice labs if you have access to the tools.

**Submodule map**

**Purpose:** Show how BI lessons move from connecting data, to building views, to dashboards and stories.

**Walkthrough:** Reference diagram only.

```yaml
Module Structure:
┌─────────────────────────┐
│ Data Connection       │ → Source Integration
├─────────────────────────┤
│ Visual Analytics     │ → Chart Creation
├─────────────────────────┤
│ Dashboard Design     │ → Story Building
└─────────────────────────┘
```

## Prerequisites

- [3.1 Intro to data visualization](../3.1-intro-data-viz/README.md) and basic comfort with spreadsheets or SQL-style fields (dimensions vs measures).
- Tableau Desktop or a comparable lab environment (your instructor may specify Tableau Public or server access).

## Why Tableau?

### 1. Intuitive Design

```yaml
Key Features:
  Drag-and-Drop:
    - Visual field mapping
    - Instant chart creation
    - Dynamic filtering
    
  Visual Analytics:
    - Automatic insights
    - Statistical summaries
    - Trend analysis
    
  Rapid Development:
    - Quick prototyping
    - Instant feedback
    - Easy iteration
```

### 2. Enterprise Power

```yaml
Capabilities:
  Data Handling:
    - Live connections
    - Data extracts
    - Incremental updates
    
  Security:
    - Row-level security
    - User authentication
    - Data encryption
    
  Scalability:
    - Big data ready
    - Server deployment
    - Cloud integration
```

## Core concepts

### 1. Data Architecture

```
Data Pipeline:
┌─────────────┐    ┌─────────────┐    ┌───────────────┐
│ Data Source │ →  │   Extract   │ →  │ Visualization │
└─────────────┘    └─────────────┘    └───────────────┘
     Raw Data         Processing         Presentation
```

#### Connection Types

```yaml
Live Connection:
  Pros:
    - Real-time updates
    - No storage needed
    - Latest data always
  Cons:
    - Network dependent
    - Can be slower
    - Server load

Extract:
  Pros:
    - Fast performance
    - Offline access
    - Reduced load
  Cons:
    - Point-in-time
    - Storage needed
    - Manual/scheduled refresh
```

> **Ask AI (Claude or ChatGPT)**
>
> "I'm connecting Tableau to a [describe your data source, e.g. 'MySQL database with 5 million rows updated hourly']. Should I use a live connection or an extract? What are the trade-offs for my specific situation?"

### 2. Visual Grammar

#### Basic Charts

```yaml
Chart Selection:
  Comparison:
    - Bar charts (categories)
    - Line charts (time)
    - Bullet charts (targets)
    
  Distribution:
    - Histograms (frequency)
    - Box plots (statistics)
    - Heat maps (density)
    
  Composition:
    - Pie charts (parts)
    - Tree maps (hierarchy)
    - Stacked bars (parts over time)
    
  Relationship:
    - Scatter plots (correlation)
    - Bubble charts (3 variables)
    - Connected scatter (paths)
```

> **Ask AI (Claude or ChatGPT)**
>
> "I want to show [describe your goal, e.g. 'how monthly revenue has changed across 4 product categories over the past 2 years']. What chart type should I use in Tableau, and how do I set it up — which fields go on Rows, Columns, and Marks?"

#### Visual Best Practices

```yaml
Design Principles:
  Color Usage:
    - Sequential: Ordered data
    - Diverging: Mid-point data
    - Categorical: Distinct groups
    
  Layout:
    - Grid alignment
    - Visual hierarchy
    - White space
    
  Typography:
    - Clear hierarchy
    - Consistent fonts
    - Readable sizes
```

### 3. Calculations

#### Basic Formulas

```sql
-- Year-over-Year Growth
YOY_Growth = 
([Sales] - LOOKUP([Sales], -1)) / 
LOOKUP([Sales], -1)

-- Moving Average
Moving_Avg = 
WINDOW_AVG([Value], -3, 0)

-- Running Total
Running_Sum = 
RUNNING_SUM(SUM([Sales]))
```

> **Ask AI (Claude or ChatGPT)**
>
> "Write a Tableau calculated field that [describe what you need, e.g. ‘calculates the 3-month moving average of profit, expressed as a percentage of the category total’]. My data has these fields: [list your field names]."

#### Advanced Analytics

**Purpose:** Illustrate built-in forecasting, clustering, and statistical test functions—availability varies by Tableau version.

**Walkthrough:** Treat as signatures to look up in current docs; clustering and t-test need appropriate data prep.

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
-- Forecasting
FORECAST_INDICATOR(
    SUM([Sales]), 6, 'manual',
    0.95, 'multiplicative'
)

-- Clustering
KMEANS(
    [Dimension1], [Dimension2],
    3, 'euclidean'
)

-- Statistical Testing
T_TEST(
    [Group1], [Group2],
    'two-tail', 0.95
)
{% endhighlight %}

</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-5" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Forecasting</span>
    </div>
    <div class="code-callout__body">
      <p><code>FORECAST_INDICATOR</code> with <code>'multiplicative'</code> seasonality and 95% confidence interval forecasts 6 periods ahead from the aggregated sales measure.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="7-12" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">K-Means Clustering</span>
    </div>
    <div class="code-callout__body">
      <p><code>KMEANS</code> partitions records into 3 clusters using Euclidean distance on two dimensions—requires Tableau's Analytics model.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="14-17" data-tint="3">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Statistical Test</span>
    </div>
    <div class="code-callout__body">
      <p><code>T_TEST</code> runs a two-tailed t-test between two groups at the 95% confidence level to test for significant differences in means.</p>
    </div>
  </div>
</aside>
</div>

### 4. Dashboard Design

#### Layout Patterns

**Purpose:** Show two common grid sketches—KPI band + main chart vs filter rail + detail—for planning wireframes.

**Walkthrough:** ASCII only; translate to Tableau containers and floating/layout when building.

```
1. Executive Dashboard
┌──────────┬──────────┬──────────┐
│  KPI 1   │   KPI 2  │   KPI 3  │
├──────────┴──────────┴──────────┤
│      Main Visualization        │
├──────────┬──────────┬──────────┤
│ Detail 1 │ Detail 2 │ Detail 3 │
└──────────┴──────────┴──────────┘

2. Analysis Dashboard
┌─────────┬─────────────────┐
│ Filters │    Overview     │
├─────────┤                 │
│ Metrics │                 │
├─────────┼─────────────────┤
│ Details │   Drill-Down    │
└─────────┴─────────────────┘
```

> **Ask AI (Claude or ChatGPT)**
>
> "I'm designing a Tableau dashboard for [describe your audience and goal, e.g. 'a weekly sales review for a regional manager who wants to spot underperforming territories quickly']. Suggest a layout: which KPIs to show at the top, what the main chart should be, and what filters to include."

#### Interactive Elements

**Purpose:** Checklist of filter widgets, dashboard actions, and parameter types you can combine for interactivity.

**Walkthrough:** Pair with [advanced-analytics](advanced-analytics.md) actions section for behavior details.

```yaml
Filter Types:
  - Single value
  - Multiple values
  - Range
  - Relative date
  - Top N

Action Types:
  - Filter
  - Highlight
  - URL
  - Set value
  - Parameter

Parameters:
  - Numeric
  - String
  - Date
  - Boolean
```

## Learning path

This submodule runs over **two sessions**.

### Session 1: Tableau foundations

- Read [Tableau basics](tableau-basics.md) — interface, connecting Sample Superstore, first charts, calculated fields, LOD
- Read [Advanced analytics](advanced-analytics.md) — table calculations, LOD types, combo charts, parameters, actions
- Explore the [AI tools integration](ai-tools-integration.md) guide to use Claude or ChatGPT as a pair partner while building

### Session 2: Case studies and comparison

- Work through the [Tableau case study](tableau-case-study.md) — end-to-end Superstore dashboard
- Compare tools: [Looker Studio case study](looker-studio-case-study.md) and [Power BI case study](powerbi-case-study.md)
- Complete the [module assignment](../_assignments/module-assignment.md)

## Using AI Tools with Tableau

See [ai-tools-integration.md](ai-tools-integration.md) for a practical guide on using Claude Desktop or ChatGPT as an AI pair partner: writing calculated fields, debugging LOD expressions, generating sample data, and preparing data in Python before connecting to Tableau.

## Assignment

Use the [module assignment](../_assignments/module-assignment.md) when you are ready for the graded work.

## Resources

### Documentation

* [Tableau Help](https://help.tableau.com)
* [Knowledge Base](https://kb.tableau.com)
* [Community Forums](https://community.tableau.com)
* [Video Library](https://www.tableau.com/learn/training)

### Learning Materials

* [Sample Workbooks](https://public.tableau.com/gallery)
* [Best Practices](https://www.tableau.com/learn/whitepapers)
* [Tips & Tricks](https://www.tableau.com/learn/tutorials)
* [Blog](https://www.tableau.com/blog)

Remember: The key to mastering Tableau is practice and experimentation. Start with simple visualizations, then gradually add complexity as you become more comfortable with the tool.
