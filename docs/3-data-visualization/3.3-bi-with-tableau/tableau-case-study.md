# Learning Tableau Through a Real Example: SuperStore Analysis

**After this lesson:** you can explain the core ideas in “Learning Tableau Through a Real Example: SuperStore Analysis” and reproduce the examples here in your own notebook or environment.

> **Note:** This tutorial is **UI-first** (Tableau Desktop). Install Tableau or use your course lab; paths to sample data may differ slightly by version and OS.

## Helpful video

Short Tableau Public install; pair with the written guides in this folder.

<iframe width="560" height="315" src="https://www.youtube.com/embed/lTNWfhmurUg" title="Tableau Public Tutorial Download and Setup" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Getting Started

### 1. Opening Tableau and Connecting to Data

1. Launch Tableau Desktop
2. On the start page, under "Connect", select "Sample - Superstore"
   - If not visible, click "Microsoft Excel" and navigate to your Tableau Repository
   - Path: `Documents/My Tableau Repository/Datasources/`
3. Click "Connect" to load the dataset

> **Figure (add screenshot or diagram):** Tableau Desktop start page — Connect pane on the left listing recent and saved data sources, with "Sample - Superstore" highlighted under Saved Data Sources.


### 2. Understanding the Tableau Workspace

The Tableau interface consists of several key areas:

1. **Data Source Tab**
   - Shows connected tables (Orders, People, Returns)
   - Focus on the Orders table for most analyses

2. **Worksheet Area**
   - **Data Pane**: Left side panel
     - Dimensions (blue): Categorical fields (e.g., Category, State)
     - Measures (green): Numerical fields (e.g., Sales, Profit)
   - **Shelves**: Areas for building visualizations
     - Columns shelf
     - Rows shelf
     - Filters shelf
     - Marks card (for colors, labels, etc.)
   - **Canvas**: Main area where charts appear
   - **Show Me**: Panel for chart suggestions

> **Figure (add screenshot or diagram):** The Tableau worksheet interface with key areas annotated: Data pane (left, Dimensions in blue / Measures in green), Rows and Columns shelves (top), Marks card (left-center), Show Me panel (right), and empty canvas in the center.


## Project Overview

In this comprehensive case study, we'll analyze retail data to drive business decisions. By the end of this tutorial, you will create:

- A dynamic sales performance dashboard
- A geographical distribution analysis
- A product profitability analysis
- Interactive filters and drill-downs

> **Figure (add screenshot or diagram):** The completed SuperStore analysis dashboard — a Sales by Category bar chart (top-left), a US state choropleth map colored by Sales (top-right), and a Profit by Sub-Category heat map (bottom) — all with matching color scheme and interactive filter controls.


## Dataset Introduction

We'll utilize the "Sample - Superstore" dataset included with Tableau. This dataset is ideal for learning because:

- It contains clean, pre-formatted data
- It includes realistic business scenarios
- It's readily available in Tableau
- It covers multiple analysis dimensions

> **Figure (add screenshot or diagram):** Tableau's Data Source tab with the Sample Superstore connection — three table icons (Orders, People, Returns) shown on the left with join lines between them, and a row-count preview at the bottom of the data grid.


### Data Structure Overview

The dataset consists of four primary tables:

```yaml
Data Structure:
1. Orders Table:
   Primary Fields:
   - Order ID (Primary Key)
   - Order Date (Date/Time)
   - Ship Date (Date/Time)
   - Ship Mode (String)
   - Customer ID (Foreign Key)
   - Product ID (Foreign Key)
   - Quantity (Integer)
   - Sales (Decimal)
   - Profit (Decimal)
   
   Additional Metadata:
   - Row Count: ~9,000
   - Date Range: 4 years
   - NULL handling: No nulls
   
2. Products Table:
   Primary Fields:
   - Product ID (Primary Key)
   - Category (String)
   - Sub-Category (String)
   - Product Name (String)
   
   Classification:
   - Categories: 3
   - Sub-Categories: 17
   - Products: ~1,500

3. Customers Table:
   Primary Fields:
   - Customer ID (Primary Key)
   - Customer Name (String)
   - Segment (String)
   - Region (String)
   
   Segmentation:
   - Customer Types: 3
   - Regions: 4
   - States: 48

4. Returns Table (Optional):
   Primary Fields:
   - Order ID (Foreign Key)
   - Return Status (Boolean)
   
   Statistics:
   - Return Rate: ~10%
   - Tracking Period: Full dataset
```

> **Figure (add screenshot or diagram):** Tableau Data Source page with the Orders table selected — the field list on the left showing data types (string, date, integer, decimal) for fields like Order ID, Order Date, Ship Mode, Sales, and Profit; the data grid preview on the right.


## Step-by-Step Visualization Guide

### 1. Creating Your First Chart: Sales by Category

1. Click the "Sheet 1" tab at the bottom
2. In the Data Pane:
   - Drag "Category" to the Rows shelf
   - Drag "Sales" to the Columns shelf
3. Tableau will automatically create a bar chart
4. To enhance:
   - Click on the chart type in the "Show Me" panel to try different visualizations
   - Edit the sheet title (double-click the title above the chart)
   - Add labels by dragging "Sales" to the Label mark

> **Figure (add screenshot or diagram):** Tableau worksheet with Category on the Rows shelf and Sales on the Columns shelf — a horizontal bar chart of three bars (Furniture, Office Supplies, Technology) on the canvas, with the Show Me panel on the right and chart type icons visible.


### 2. Time Series Analysis

#### Line Chart with Multiple Measures

1. Create a new worksheet (click the "+" icon)
2. Basic Setup:
   - Drag "Order Date" to Columns
   - Right-click and select "Month/Year"
   - Drag "Sales" to Rows
   - Drag "Profit" to Rows (dual axis)
3. Customization:
   - Format lines (thickness, style)
   - Add markers for data points
   - Configure dual axis synchronization
   - Add reference lines for averages

> **Figure (add screenshot or diagram):** Tableau dual-axis line chart — Order Date (Month/Year) on Columns and both Sales and Profit on Rows; two lines with different colors, markers at each data point, synchronized dual y-axes, and a right-click "Synchronize Axis" option highlighted.


### 3. Geographic Analysis

#### Creating a Map Visualization

1. Create a new worksheet
2. Basic Setup:
   - Drag "State" to the canvas
   - Tableau will automatically create a map
   - Drag "Sales" to Color
3. Customization:
   - Adjust color gradient
   - Add state labels
   - Configure tooltips
   - Add reference lines

> **Figure (add screenshot or diagram):** Tableau filled map of the United States — State field recognized as a geographic dimension, each state shaded by Sales using a sequential blue gradient; a tooltip open on Texas showing state name and total Sales value.


### 4. Building a Dashboard

1. Click the "New Dashboard" icon
2. Layout Design:
   - Drag your worksheets onto the dashboard canvas
   - Arrange and resize as needed
   - Add a title using the Text object
3. Adding Interactivity:
   - Click on a chart and select "Use as Filter"
   - Add filter controls
   - Configure actions
   - Set up parameters

> **Figure (add screenshot or diagram):** Tableau dashboard canvas in edit mode — three worksheets tiled (bar chart top-left, map top-right, line chart bottom), the Dashboard pane on the left showing the Sheets list, a Text object added as a title banner, and filter controls on the right.


## Advanced Features

### 1. Calculated Fields

1. Creating a Basic Calculation:
   - Right-click in the Data pane
   - Select "Create Calculated Field"
   - Name your calculation (e.g., "Profit Ratio")
   - Enter formula: `SUM([Profit])/SUM([Sales])`
   - Click OK

> **Figure (add screenshot or diagram):** Tableau's Create Calculated Field dialog — field name "Profit Ratio" entered at the top, formula `SUM([Profit])/SUM([Sales])` in the formula bar, and a green checkmark in the bottom-left confirming valid syntax before clicking OK.


### 2. Parameters

1. Creating a Parameter:
   - Right-click in the Data pane
   - Select "Create Parameter"
   - Configure settings (data type, range, etc.)
   - Click OK
2. Using the Parameter:
   - Add parameter control to dashboard
   - Use in calculations or filters

> **Figure (add screenshot or diagram):** Tableau's Create Parameter dialog for a dynamic filter — data type String, "List" selected, allowed values table showing region names (East, West, North, South), and "Show Parameter Control" checkbox visible at the bottom.


## Tips and Best Practices

1. **Data Organization**
   - Keep related visualizations together
   - Use consistent color schemes
   - Maintain clear labeling

2. **Performance**
   - Use extracts for large datasets
   - Limit the number of marks
   - Optimize calculations

3. **User Experience**
   - Add clear instructions
   - Include tooltips
   - Test on different screen sizes

## Saving and Sharing

1. Save your workbook:
   - File > Save As
   - Choose location and name
   - Select file type (.twb or .twbx)

2. Sharing options:
   - Publish to Tableau Public
   - Export as PDF/image
   - Share on Tableau Server

> **Figure (add screenshot or diagram):** Tableau's File > Save As dialog alongside the Publish to Tableau Public dialog — showing the two sharing paths: saving locally as .twb or .twbx and publishing online with a public profile URL.


## Tableau Prep Builder

### 1. Data Preparation

1. Launching Tableau Prep:
   - Open Tableau Prep Builder
   - Click "Connect to Data"
   - Select your data source

2. Common Transformations:
   - Clean and shape data
   - Join multiple data sources
   - Aggregate data
   - Create calculated fields
   - Handle null values
   - Pivot/unpivot data

> **Figure (add screenshot or diagram):** Tableau Prep Builder's Flow canvas — a data source Input step on the left connected by an arrow to a Clean step in the center (showing profile bars and null counts per column), connected to an Output step on the right.


### 2. Flow Management

1. Creating a Flow:
   - Add input step
   - Add cleaning steps
   - Add output step
   - Configure refresh settings

2. Advanced Features:
   - Schedule flows
   - Monitor flow performance
   - Handle errors
   - Create reusable flows

> **Figure (add screenshot or diagram):** Tableau Prep Builder's scheduled flow configuration screen — run frequency options (daily/weekly), a mini-diagram of the flow's steps, and a green "Last run succeeded" status badge with timestamp.


## Advanced Calculations

### 1. Table Calculations

```tableau
// Running Total
RUNNING_SUM(SUM([Sales]))

// Percent of Total
SUM([Sales]) / TOTAL(SUM([Sales]))

// Moving Average
WINDOW_AVG(SUM([Sales]), -2, 0)

// Rank
RANK(SUM([Sales]), 'desc')
```

### 2. Level of Detail (LOD) Expressions

```tableau
// Fixed LOD
{FIXED [Category] : SUM([Sales])}

// Include LOD
{INCLUDE [Region] : AVG([Profit])}

// Exclude LOD
{EXCLUDE [Sub-Category] : SUM([Quantity])}
```

## Advanced Visualizations

### 1. Custom Visualizations

1. Creating Custom Shapes:
   - Design shapes in external tools
   - Import to Tableau
   - Map to data
   - Configure display options

2. Advanced Chart Types:
   - Waterfall charts
   - Box and whisker plots
   - Gantt charts
   - Bullet graphs
   - Radar charts

> **Figure (add screenshot or diagram):** Tableau advanced chart gallery — a waterfall chart (top-left), a bullet graph showing actual vs target (top-right), a box and whisker plot (bottom-left), and a Gantt chart for scheduling (bottom-right), all built using standard Tableau shelves.


### 2. Advanced Mapping

1. Custom Geocoding:
   - Import custom geocodes
   - Create custom territories
   - Configure map layers
   - Add custom backgrounds

2. Spatial Analysis:
   - Create buffers
   - Calculate distances
   - Perform spatial joins
   - Create density maps

> **Figure (add screenshot or diagram):** Tableau map with advanced geographic layers — a density heatmap overlay showing order concentration by ZIP code, a custom sales territory polygon drawn in orange, and a distance buffer circle around a distribution center.


## Tableau Server Features

### 1. Content Management

1. Publishing Content:
   - Publish workbooks
   - Set permissions
   - Configure schedules
   - Manage extracts

2. Content Organization:
   - Create projects
   - Set up folders
   - Configure permissions
   - Manage subscriptions

> **Figure (add screenshot or diagram):** Tableau Server / Tableau Cloud content management UI — Projects pane on the left with a folder hierarchy, workbooks listed in the center grid with thumbnail previews, and a Permissions settings panel open on the right.


### 2. Collaboration Features

1. Sharing Options:
   - Create subscriptions
   - Set up alerts
   - Share dashboards
   - Configure mobile access

2. Version Control:
   - Track changes
   - Restore versions
   - Compare versions
   - Manage conflicts

> **Figure (add screenshot or diagram):** Tableau Server subscription setup dialog — recipient email addresses entered, schedule frequency set to "Weekly on Monday 8 AM", and the attachment format toggle showing PDF or image options.


## Performance Optimization

### 1. Extract Optimization

1. Creating Extracts:
   - Configure refresh schedule
   - Set up incremental refresh
   - Optimize for performance
   - Monitor extract size

2. Best Practices:
   - Filter data early
   - Aggregate when possible
   - Use appropriate data types
   - Monitor performance

> **Figure (add screenshot or diagram):** Tableau's Extract refresh configuration dialog — Full vs Incremental refresh toggle, schedule frequency options (daily/weekly), estimated extract size shown in MB, and last refresh timestamp.


### 2. Dashboard Optimization

1. Performance Tips:
   - Limit number of views
   - Use appropriate chart types
   - Optimize calculations
   - Configure caching

2. Monitoring:
   - Use Performance Recorder
   - Check query performance
   - Monitor resource usage
   - Analyze bottlenecks

> **Figure (add screenshot or diagram):** Tableau Performance Recorder results view — a flame chart of timed events (query execution, rendering, layout) with the slowest steps highlighted in red and a total load time summary at the top.


## Security and Governance

### 1. Row-Level Security

1. Implementing RLS:
   - Create user filters
   - Set up data source filters
   - Configure permissions
   - Test security rules

2. Advanced Security:
   - User-based filters
   - Project-based access
   - Time-based restrictions
   - Custom security rules

> **Figure (add screenshot or diagram):** Tableau's User Filters dialog for row-level security — a mapping table listing usernames in the left column and their allowed Region values in the right column; a "Match to current user" checkbox at the bottom.


### 2. Data Governance

1. Compliance Features:
   - Audit logs
   - Usage tracking
   - Data lineage
   - Compliance reports

2. Monitoring:
   - Usage statistics
   - Performance metrics
   - Security logs
   - Compliance tracking

> **Figure (add screenshot or diagram):** Tableau Server Admin's Activity Log view — a table of usage events (view, publish, download) with columns for timestamp, username, action type, and content name; filterable by date range and event type.


## Tableau Mobile

### 1. Mobile Optimization

1. Dashboard Design:
   - Create mobile layouts
   - Optimize for touch
   - Configure device detection
   - Test on multiple devices

2. Mobile Features:
   - Offline access
   - Push notifications
   - Mobile-specific filters
   - Touch interactions

> **Figure (add screenshot or diagram):** Tableau dashboard in mobile layout mode — a single KPI card (Sales total) at the top, a compact bar chart below, and touch-friendly filter buttons at the bottom; the Device Preview dropdown at the top showing "Phone" selected.


### 2. Mobile App Features

1. App Capabilities:
   - View dashboards
   - Interact with data
   - Receive alerts
   - Share insights

2. Best Practices:
   - Design for small screens
   - Optimize performance
   - Simplify interactions
   - Test thoroughly

> **Figure (add screenshot or diagram):** Side-by-side comparison of a Tableau dashboard in desktop layout (left, wide multi-column) and the auto-optimized mobile layout (right, narrow single-column with stacked charts), showing how Tableau reflows tiles for the phone screen.


## Next Steps

1. Explore Tableau Public
2. Join the Tableau Community
3. Get Tableau Certified
4. Learn Tableau Server administration
5. Explore Tableau extensions
6. Practice with real-world datasets

Remember: Practice makes perfect! Try recreating these visualizations and experiment with different options to build your Tableau skills.
