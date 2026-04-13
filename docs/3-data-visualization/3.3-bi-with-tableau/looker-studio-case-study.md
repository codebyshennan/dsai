# Learning Looker Studio Through a Real Example: SuperStore Analysis

You have monthly sales data sitting in a Google Sheet. Your manager wants a live dashboard they can filter by region and date — by tomorrow. Here is how to build one in 30 minutes with zero code, using Google's free Looker Studio tool.

**After this lesson:** you can explain the core ideas in “Learning Looker Studio Through a Real Example: SuperStore Analysis” and reproduce the examples here in your own notebook or environment.

> **Note:** This tutorial is **UI-first** (Looker Studio in the browser). You need a Google account and permission to connect a Google Sheet or similar source.

## Helpful video

<!-- TODO: embed specific Google Looker Studio intro video here -->

Watch the official [Google Looker Studio Getting Started guide](https://lookerstudio.google.com/navigation/reporting) before continuing.

## Key Terms

Before diving in, get familiar with these words — you will see them throughout the interface.

| Term | Definition | Example |
|------|-----------|---------|
| **Dimension** | A categorical field used to group or label data | `Category` (Furniture, Technology, Office Supplies) |
| **Metric** | A numeric field that gets aggregated (summed, averaged, counted) | `Sales` totalled per category |
| **Filter** | A rule that limits which rows appear in a chart or page | Show only orders where `Region = West` |
| **Slicer** | An interactive filter control that viewers can click to filter the whole page | A dropdown letting users pick a year |
| **Data Source** | A connected dataset that powers one or more charts | A Google Sheet named "Superstore Orders" |
| **Canvas** | The main drag-and-drop area where you place charts and text | The white page you see when you open a report |
| **Connector** | The bridge that links Looker Studio to an external data system | The "Google Sheets" connector |

## Getting Started

### 1. Opening Looker Studio and Connecting to Data

1. Go to [Looker Studio](https://lookerstudio.google.com/)
2. Click "Create" and select "Report"
3. Choose your data source:
   - For this example, we'll use Google Sheets
   - Upload the Superstore dataset to Google Sheets
   - Select the sheet as your data source
4. Click "Add" to connect the data

![Looker Studio start page](assets/looker_start_page.png)


### 2. Understanding the Looker Studio Workspace

{% include mermaid-diagram.html src="3-data-visualization/3.3-bi-with-tableau/diagrams/looker-studio-case-study-1.mmd" %}

![Looker Studio workspace](assets/looker_workspace.png)

The Looker Studio interface consists of several key areas:

1. **Canvas**
   - Main area for creating visualizations
   - Multiple pages for different analyses
   - Responsive layout options

2. **Toolbar**
   - Add components
   - Format options
   - Theme settings
   - View controls

3. **Properties Panel**
   - Data configuration
   - Style options
   - Interaction settings
   - Advanced options

4. **Data Panel**
   - Available fields
   - Calculated fields
   - Data source settings
   - Filter controls

![Looker Studio interface toolbar and properties panel](assets/looker_workspace.png)


## Project Overview

In this comprehensive case study, we'll analyze retail data to drive business decisions. By the end of this tutorial, you will create:

- A dynamic sales performance dashboard
- A geographical distribution analysis
- A product profitability analysis
- Interactive filters and controls

![Completed SuperStore dashboard](assets/looker_dashboard.png)


## Dataset Introduction

We'll utilize the "Sample - Superstore" dataset adapted for Looker Studio. This dataset is ideal for learning because:

- It contains clean, pre-formatted data
- It includes realistic business scenarios
- It's easy to import into Google Sheets
- It covers multiple analysis dimensions

![Superstore data source connector](assets/looker_data_source.png)


### Data Structure Overview

The dataset consists of four primary tables. The **Orders** table is the heart of the data — it records every transaction (~9,000 rows over 4 years) including the sale amount, profit, shipping mode, and the dates an order was placed and shipped. The **Products** table tells you what was sold, organising ~1,500 products into 3 categories (Furniture, Technology, Office Supplies) and 17 sub-categories. The **Customers** table tells you who bought it: each customer belongs to one of 3 segments (Consumer, Corporate, Home Office) and maps to one of 4 US regions. Finally, the **Returns** table is optional but useful — it flags the roughly 10% of orders that were returned, which you can blend in to calculate a clean "net sales" figure.

![Data source field configuration](assets/looker_data_source.png)


## Step-by-Step Visualization Guide

### 1. Creating Your First Chart: Sales by Category

1. Click "Add a chart" in the toolbar
2. Select "Bar chart" from the chart types
3. In the Properties panel:
   - Set "Category" as the Dimension
   - Set "Sales" as the Metric
4. To enhance:
   - Add data labels
   - Customize colors
   - Add a title
   - Configure tooltips

![First bar chart by category](assets/looker_first_chart.png)


### 2. Time Series Analysis

#### Line Chart with Multiple Metrics

1. Add a new page (click "+" at bottom)
2. Select "Time series" chart
3. Basic Setup:
   - Set "Order Date" as Dimension
   - Add "Sales" as Metric
   - Click "Add metric" and add "Profit"
4. Customization:
   - Format lines and markers
   - Add reference lines
   - Configure date range
   - Add trend lines

![Time series chart with multiple metrics](assets/looker_timeseries.png)


### 3. Geographic Analysis

#### Creating a Map Visualization

1. Add a new page
2. Select "Geo map" from chart types
3. Basic Setup:
   - Set "State" as Location dimension
   - Set "Sales" as Color metric
   - Set "Profit" as Size metric
4. Customization:
   - Adjust color scale
   - Add region labels
   - Configure tooltips
   - Set zoom level

![Geo map of US sales by state](assets/looker_map.png)


### 4. Building a Dashboard

1. Arrange your visualizations on the canvas
2. Add a title using the Text tool
3. Adding Interactivity:
   - Add filter controls
   - Set up date range controls
   - Configure cross-filtering
   - Add navigation between pages

![Dashboard canvas with charts and filter controls](assets/looker_dashboard.png)


## Advanced Features

### 1. Calculated Fields

1. Basic Calculations:

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
-- Profit Ratio
Profit Ratio = Profit / Sales

-- Sales Growth
Sales Growth =
(SELECT SUM(Sales)
 WHERE Order Date >= DATE_SUB(CURRENT_DATE(), INTERVAL 1 MONTH))
/
(SELECT SUM(Sales)
 WHERE Order Date >= DATE_SUB(CURRENT_DATE(), INTERVAL 2 MONTH))
- 1

-- Customer Segment
Customer Segment =
CASE
  WHEN SUM(Sales) > 10000 THEN "High Value"
  WHEN SUM(Sales) > 5000 THEN "Medium Value"
  ELSE "Low Value"
END
{% endhighlight %}

</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-2" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Profit Ratio</span>
    </div>
    <div class="code-callout__body">
      <p>A simple division field; Looker Studio evaluates this per-row before aggregation.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="4-11" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Sales Growth</span>
    </div>
    <div class="code-callout__body">
      <p>Divides this month's total by last month's using subqueries with <code>DATE_SUB</code>, then subtracts 1 to get a percentage change.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="13-19" data-tint="3">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Customer Segmentation</span>
    </div>
    <div class="code-callout__body">
      <p>A <code>CASE</code> expression buckets customers into High, Medium, or Low value tiers based on their aggregated sales.</p>
    </div>
  </div>
</aside>
</div>

2. Advanced Functions:

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
-- Moving Average (3-month)
Moving Average =
AVG(Sales) OVER (
  ORDER BY Order Date
  ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
)

-- Running Total
Running Total =
SUM(Sales) OVER (
  ORDER BY Order Date
  ROWS UNBOUNDED PRECEDING
)

-- Percent of Total
Percent of Total =
SUM(Sales) /
(SELECT SUM(Sales) FROM Orders)
{% endhighlight %}

</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-6" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Moving Average</span>
    </div>
    <div class="code-callout__body">
      <p><code>ROWS BETWEEN 2 PRECEDING AND CURRENT ROW</code> creates a 3-period window that slides forward with each date, smoothing volatility.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="8-13" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Running Total</span>
    </div>
    <div class="code-callout__body">
      <p><code>ROWS UNBOUNDED PRECEDING</code> starts from the first row of the partition, accumulating sales into a running sum.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="15-18" data-tint="3">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Percent of Total</span>
    </div>
    <div class="code-callout__body">
      <p>Divides each row's sales by the grand total from a subquery, giving each row its share of overall revenue.</p>
    </div>
  </div>
</aside>
</div>

![Calculated field editor with Profit Ratio formula](assets/looker_calculations.png)


### 2. Parameters and Controls

1. Interactive Controls:
   - Dropdown lists
   - Date range selectors
   - Sliders
   - Checkboxes
   - Radio buttons

2. Parameter Configuration:

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
-- Dynamic Threshold Parameter
Threshold Parameter =
CASE
  WHEN @threshold = "High" THEN 10000
  WHEN @threshold = "Medium" THEN 5000
  ELSE 1000
END

-- Dynamic Date Range
Date Range Filter =
CASE
  WHEN @date_range = "Last 30 Days"
    THEN Order Date >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
  WHEN @date_range = "Last 90 Days"
    THEN Order Date >= DATE_SUB(CURRENT_DATE(), INTERVAL 90 DAY)
  ELSE TRUE
END
{% endhighlight %}

</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-7" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Threshold Parameter</span>
    </div>
    <div class="code-callout__body">
      <p><code>@threshold</code> references a Looker Studio parameter control; the <code>CASE</code> maps the viewer's selection to a numeric value.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="9-17" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Dynamic Date Filter</span>
    </div>
    <div class="code-callout__body">
      <p><code>@date_range</code> lets viewers pick a window; <code>DATE_SUB</code> computes the cutoff date dynamically, returning a boolean filter condition.</p>
    </div>
  </div>
</aside>
</div>

![Filter controls: date range, dropdown, and slider](assets/looker_controls.png)


## Data Blending and Integration

### 1. Advanced Data Blending

1. Multi-Source Blending:
   - Combine Google Sheets with BigQuery
   - Blend with Google Analytics data
   - Integrate with CRM data
   - Connect to external databases

2. Blend Configuration:

```sql
-- Example of a complex blend
SELECT 
  o.OrderID,
  o.Sales,
  p.Category,
  c.Segment,
  r.ReturnStatus
FROM Orders o
LEFT JOIN Products p ON o.ProductID = p.ProductID
LEFT JOIN Customers c ON o.CustomerID = c.CustomerID
LEFT JOIN Returns r ON o.OrderID = r.OrderID
```

![Data blending dialog with join configuration](assets/looker_blending.png)


### 2. Data Source Management

1. Connection Types:
   - Google Sheets
   - BigQuery
   - Google Analytics
   - MySQL
   - PostgreSQL
   - CSV files
   - Custom connectors

2. Data Refresh Options:
   - Manual refresh
   - Scheduled refresh
   - Real-time updates
   - Incremental refresh

![Data source management panel with refresh options](assets/looker_source_mgmt.png)


## Advanced Visualizations

### 1. Modern Chart Types

1. Scorecards:
   - Smart scorecards with AI insights
   - KPI comparisons
   - Trend indicators
   - Conditional formatting

2. Advanced Charts:
   - Waterfall charts
   - Bullet graphs
   - Radar charts
   - Heat maps
   - Tree maps
   - Sankey diagrams

![Advanced chart types gallery](assets/looker_advanced_charts.png)


### 2. Interactive Features

1. Drill-Down Capabilities:
   - Hierarchical navigation
   - Cross-filtering
   - Detail-on-demand
   - Interactive tooltips

2. Dynamic Formatting:
   - Conditional colors
   - Dynamic labels
   - Responsive layouts
   - Mobile optimization

![Cross-filter drill-down interactivity](assets/looker_interactivity.png)


## Collaboration and Sharing

### 1. Team Collaboration

1. Real-Time Editing:
   - Multiple editors
   - Version history
   - Comments and annotations
   - Change tracking

2. Access Control:
   - User roles
   - Permission levels
   - Group access
   - Audit logs

![Share dialog with collaborator roles](assets/looker_collaboration.png)


### 2. Advanced Sharing Options

1. Distribution Methods:
   - Shareable links
   - Email subscriptions
   - PDF exports
   - Embedded dashboards
   - Mobile access

2. Scheduling and Automation:
   - Scheduled reports
   - Automated alerts
   - Data-driven triggers
   - Custom notifications

![Advanced sharing and embedding options](assets/looker_sharing.png)


## Performance Optimization

### 1. Data Optimization

1. Query Optimization:
   - Use appropriate data types
   - Implement caching
   - Optimize calculations
   - Limit data volume

2. Performance Monitoring:
   - Query execution times
   - Resource usage
   - Cache hit rates
   - Refresh performance

![Report performance panel with query times and cache hits](assets/looker_performance.png)


### 2. Dashboard Optimization

1. Best Practices:
   - Limit visualizations per page
   - Use efficient chart types
   - Optimize filters
   - Implement pagination

2. Mobile Optimization:
   - Responsive layouts
   - Touch-friendly controls
   - Mobile-specific views
   - Offline capabilities

![Mobile preview with responsive layout optimization](assets/looker_optimization.png)


## AI and Automation

### 1. Smart Features

1. AI-Powered Insights:
   - Automated recommendations
   - Anomaly detection
   - Trend analysis
   - Predictive metrics

2. Automation Tools:
   - Smart alerts
   - Automated reports
   - Data-driven actions
   - Scheduled tasks

![AI-powered insights panel with anomaly detection](assets/looker_ai.png)


## Next Steps

1. Explore Looker Studio templates
2. Learn advanced SQL for calculated fields
3. Practice with different data sources
4. Join the Looker Studio community
5. Explore Looker Studio extensions
6. Learn about data governance
7. Master AI-powered features
8. Implement advanced automation

## Gotchas

- **Data blending in Looker Studio is a left join by default and silently drops unmatched rows** — when you blend a Google Sheet with a BigQuery source, only rows where the join key matches both sources appear in the chart. Missing rows produce no warning. Always verify row counts before and after blending with a scorecard showing record count.
- **Calculated fields that use `SUM()` are evaluated per-row before aggregation unless you explicitly aggregate** — `Profit / Sales` computes a ratio at row level and then Looker Studio averages those ratios, which is different from `SUM(Profit) / SUM(Sales)`. Use the latter form for accurate margin or rate calculations.
- **Date range controls only filter charts that are connected to the same data source** — if your dashboard blends two sources, a date control wired to source A won't filter charts backed by source B. You need a separate date control for each distinct source, or reconfigure blending so both charts share one source.
- **`@parameter` syntax for parameter references is only valid inside calculated fields, not in native filter widgets** — learners often try to write a filter condition using a parameter name directly in the filter dialog and get no result. Parameters must be consumed inside a `CASE` or conditional calculated field, which then drives the chart or filter.
- **Scheduled email reports always send the cached snapshot, not a live query** — if your data refreshes every hour but your scheduled report runs at 6 AM, recipients get whatever the cache held at 6 AM, which may be hours stale. Set the data source refresh schedule to run just before the report time.

Remember: Practice makes perfect! Try recreating these visualizations and experiment with different options to build your Looker Studio skills.
