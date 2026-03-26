# 3.3 Business Intelligence with Tableau

## Overview

This submodule is **UI-first**: you will connect data and build views in **Tableau** (and related lessons may reference **Looker Studio** or **Power BI**) with drag-and-drop analytics instead of Python scripts.

> **Note:** Perception and chart-choice principles still apply; see [3.1 visualization principles](../3.1-intro-data-viz/visualization-principles.md) when you are unsure which visual to use.

> **Time needed:** Plan several hours across the case studies and practice labs if you have access to the tools.

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

#### Advanced Analytics

```sql
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
```

### 4. Dashboard Design

#### Layout Patterns

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

#### Interactive Elements

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

### Week 1: Foundation

```yaml
Day 1-2:
  - Tableau interface
  - Data connection
  - Basic charts
  - Simple calculations

Day 3-4:
  - Filtering
  - Sorting
  - Grouping
  - Basic dashboards

Day 5:
  - Practice exercises
  - Review
  - Q&A session
```

### Week 2: Advanced Features

```yaml
Day 1-2:
  - Complex calculations
  - LOD expressions
  - Advanced charts
  - Custom SQL

Day 3-4:
  - Dashboard actions
  - Parameters
  - Sets
  - Analytics

Day 5:
  - Advanced exercises
  - Performance tuning
  - Best practices
```

### Week 3: Real-World Applications

```yaml
Day 1-2:
  - Sales analytics
  - Financial reporting
  - Marketing dashboards
  - Operations KPIs

Day 3-4:
  - Server deployment
  - Security setup
  - Maintenance
  - Optimization

Day 5:
  - Final project
  - Presentation
  - Feedback
  - Next steps
```

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
