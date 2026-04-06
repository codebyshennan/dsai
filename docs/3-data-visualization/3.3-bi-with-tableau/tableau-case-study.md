# Learning Tableau Through a Real Example: SuperStore Analysis

**After this lesson:** you can explain the core ideas in "Learning Tableau Through a Real Example: SuperStore Analysis" and reproduce the examples here in your own notebook or environment.

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

![Tableau Desktop start page](assets/tableau_start_page.png)


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

![Tableau worksheet interface with annotated areas](assets/tableau_workspace.png)

> **Ask AI (Claude or ChatGPT)**
>
> "In Tableau, I have a field called [field name] that shows up as a Measure (green) but I want to use it as a Dimension (blue) — for example, a numeric order ID I want to group by. How do I change it, and when should I do this?"


## Project Overview

In this comprehensive case study, we'll analyze retail data to drive business decisions. By the end of this tutorial, you will create:

- A dynamic sales performance dashboard
- A geographical distribution analysis
- A product profitability analysis
- Interactive filters and drill-downs

![Completed SuperStore analysis dashboard](assets/tableau_final_dashboard.png)


## Dataset Introduction

We'll utilize the "Sample - Superstore" dataset included with Tableau. This dataset is ideal for learning because:

- It contains clean, pre-formatted data
- It includes realistic business scenarios
- It's readily available in Tableau
- It covers multiple analysis dimensions

![Tableau Data Source tab with table join preview](assets/tableau_data_source.png)


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

![Tableau Data Source page with Orders table field list](assets/tableau_data_source.png)


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

![Tableau first chart — Sales by Category bar chart](assets/tableau_first_chart.png)


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

![Tableau dual-axis line chart with Sales and Profit](assets/tableau_line_chart.png)


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

![Tableau filled map of US states colored by Sales](assets/tableau_map.png)


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

![Tableau dashboard canvas in edit mode](assets/tableau_dashboard_workspace.png)


## Advanced Features

### 1. Calculated Fields

1. Creating a Basic Calculation:
   - Right-click in the Data pane
   - Select "Create Calculated Field"
   - Name your calculation (e.g., "Profit Ratio")
   - Enter formula: `SUM([Profit])/SUM([Sales])`
   - Click OK

![Tableau Create Calculated Field dialog for Profit Ratio](assets/tableau_calculated_field.png)


### 2. Parameters

1. Creating a Parameter:
   - Right-click in the Data pane
   - Select "Create Parameter"
   - Configure settings (data type, range, etc.)
   - Click OK
2. Using the Parameter:
   - Add parameter control to dashboard
   - Use in calculations or filters

![Tableau Create Parameter dialog](assets/tableau_parameter.png)


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

![Tableau Save As and Publish to Tableau Public dialogs](assets/tableau_collaboration.png)


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

![Tableau Prep Builder Flow canvas with input, clean, and output steps](assets/tableau_prep.png)


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

![Tableau Prep Builder scheduled flow configuration](assets/tableau_flow.png)


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

![Tableau advanced chart gallery — waterfall, bullet, box plot, Gantt](assets/tableau_custom_viz.png)


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

![Tableau map with density overlay and custom territory polygon](assets/tableau_advanced_map.png)


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

![Tableau Server content management UI with project folders](assets/tableau_content_mgmt.png)


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

![Tableau Server subscription setup dialog](assets/tableau_collaboration.png)


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

![Tableau Extract refresh configuration dialog](assets/tableau_extract.png)


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

![Tableau Performance Recorder results with flame chart](assets/tableau_performance.png)


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

![Tableau User Filters dialog for row-level security](assets/tableau_security.png)


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

![Tableau Server Admin Activity Log view](assets/tableau_governance.png)


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

![Tableau dashboard in mobile layout mode](assets/tableau_mobile.png)


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

![Tableau dashboard desktop vs mobile layout comparison](assets/tableau_mobile_app.png)


## Next Steps

1. Explore Tableau Public
2. Join the Tableau Community
3. Get Tableau Certified
4. Learn Tableau Server administration
5. Explore Tableau extensions
6. Practice with real-world datasets

## Gotchas

- **"Use as Filter" on a dashboard sheet filters all other sheets by default, including ones you didn't intend** — when you enable a chart as a filter, it acts on every compatible sheet on the dashboard unless you configure a targeted filter action. Go to Dashboard → Actions to restrict the source and target sheets explicitly.
- **Dual-axis charts require synchronised axes or the chart visually lies** — if Sales is in the thousands and Profit is in the hundreds, an unsynchronised dual axis makes the two lines appear to track each other closely when they may not. Right-click the secondary axis and choose "Synchronize Axis" or use separate panels to avoid misleading comparisons.
- **Table calculations like `RUNNING_SUM` depend on the sort order of the view, not the data** — if a viewer reorders the table by clicking a column header, the running total recomputes along the new sort order, producing a completely different result. Always label running total charts with the sort assumption or lock the view.
- **Tableau Prep flows do not automatically re-run when source data changes** — a Prep flow is a manual or scheduled operation, not a live query. If you clean your data in Prep and then update the source file, the downstream Tableau workbook still shows the old cleaned data until you re-run the flow and refresh the extract.
- **Saving as `.twb` (not `.twbx`) leaves data behind** — a `.twb` file is just XML; it references the data source path but does not embed the data. When you share a `.twb` with a colleague who doesn't have access to the same data path, the workbook opens empty. Use `.twbx` to bundle the extract for portability.

Remember: Practice makes perfect! Try recreating these visualizations and experiment with different options to build your Tableau skills.
