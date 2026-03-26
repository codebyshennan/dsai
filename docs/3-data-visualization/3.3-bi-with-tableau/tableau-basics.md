# Tableau Basics: Sample Superstore Guide

> **Note:** This submodule is **UI-first**. You will follow clicks and shelves in Tableau Desktop rather than writing Python for the main workflow.

## Introduction to Tableau with Sample Superstore

Tableau is a powerful data visualization tool that enables interactive analytics and visualizations. The Sample Superstore dataset is a built-in dataset that simulates a retail business, making it ideal for learning Tableau's features and capabilities. This guide covers:

- Tableau's intuitive visualization interface
- Real-time data analysis without coding
- Interactive dashboard creation
- Advanced visualization techniques

### Prerequisites

1. **Required Components:**
   - Tableau Desktop 2021.1 or newer
   - Basic understanding of data analysis
   - Familiarity with business metrics

2. **System Requirements:**
   - Windows 10/11 or macOS 12+
   - 8GB RAM minimum (16GB recommended)
   - 2GB free disk space
   - Modern multi-core processor

### Getting Started: Step-by-Step Guide

#### 1. Connecting to Sample Superstore

1. Launch Tableau Desktop.

> **Figure (add screenshot or diagram):** Tableau Start Page

- In the Connect pane on the left, under **Saved Data Sources**, click **Sample - Superstore**.

2. Preview the data source.

> **Figure (add screenshot or diagram):** Data Source Tab

- Review the data structure. Dimensions (blue) and measures (green) appear in the pane.
- Scan the first 1,000 rows to confirm fields look reasonable.

3. Open a new worksheet.

> **Figure (add screenshot or diagram):** Blank Worksheet

- Click **New Worksheet** and familiarize yourself with shelves, marks, and the Data pane.

#### 2. Creating Your First Visualization

Example: **Sales by Category** bar chart.

1. Build the chart.

> **Figure (add screenshot or diagram):** Drag and Drop Fields

- Drag **Category** to **Rows**.
- Drag **Sales** to **Columns**. Tableau should show a horizontal bar chart.

2. Customize and refine.

> **Figure (add screenshot or diagram):** Chart Formatting

- Use **Show Me** if needed.
- Sort bars by sales (descending), add color by category, and add data labels.

3. Format the view.

> **Figure (add screenshot or diagram):** Format Pane

- Adjust axis labels, colors, title, and number formats.

#### 3. Adding Filters and Interactivity

1. Add filters.

> **Figure (add screenshot or diagram):** Filter Shelf

- Drag **Region** to **Filters**, choose regions, and apply.

2. Create parameters (optional).

> **Figure (add screenshot or diagram):** Parameter Creation

- Right-click in the Data pane, choose **Create Parameter**, configure it, and add the control to the view.

3. Use dashboard actions.

> **Figure (add screenshot or diagram):** Dashboard Actions

- On a dashboard, add multiple sheets and configure filter or highlight actions.

#### 4. Building a Complete Dashboard

1. Layout.

> **Figure (add screenshot or diagram):** Dashboard Workspace

- Create a **New Dashboard**, add worksheets, and arrange tiles.

2. Interactivity.

> **Figure (add screenshot or diagram):** Dashboard Interactivity

- Add filters, actions, parameter controls, and navigation as needed.

3. Final polish.

> **Figure (add screenshot or diagram):** Final Dashboard

- Add legends, align colors, adjust spacing, and tune tooltips.

### Common Visualization Examples

#### 1. Sales Analysis Dashboard

1. Sales trend.

> **Figure (add screenshot or diagram):** Line Chart

- **Order Date** (Month) on **Columns**, **Sales** on **Rows**. Add a trend line and format dates.

2. Geographic map.

> **Figure (add screenshot or diagram):** Map View

- **State** on the map, **Sales** on **Color**, labels and tooltips as needed.

3. Category breakdown.

> **Figure (add screenshot or diagram):** Bar Chart

- **Category** on **Rows**, **Sales** on **Columns**, sort and add percentage labels if useful.

#### 2. Profit Analysis Dashboard

1. Profit by sub-category.

> **Figure (add screenshot or diagram):** Heat Map

- **Sub-Category** on **Columns**, **Category** on **Rows**, **Profit** on **Color**.

2. Discount impact.

> **Figure (add screenshot or diagram):** Scatter Plot

- **Discount** on one axis, **Profit Ratio** on the other; add a trend line or bins.

3. Regional performance.

> **Figure (add screenshot or diagram):** Map with Indicators

- **Region** on the map, **Profit** on **Color**, reference lines and tooltips as needed.

### Advanced Features

#### 1. Calculated Fields

1. Profit ratio.

> **Figure (add screenshot or diagram):** Calculation Editor

- Formula: `SUM([Profit])/SUM([Sales])`
- Right-click in the Data pane, **Create Calculated Field**, enter the formula, and name the field.

2. Year-over-year growth.

> **Figure (add screenshot or diagram):** Table Calculation

- Example: `(SUM([Sales]) - LOOKUP(SUM([Sales]), -1))/ABS(LOOKUP(SUM([Sales]), -1))`
- Set up as a table calculation and format as a percentage.

#### 2. Level of Detail Expressions

1. Fixed LOD.

> **Figure (add screenshot or diagram):** LOD Editor

- Example: `{FIXED [Category] : SUM([Sales])}`
- Create a calculated field, enter the LOD expression, apply to the view.

2. Include LOD.

> **Figure (add screenshot or diagram):** LOD in View

- Example: `{INCLUDE [Region] : AVG([Profit])}`
- Add to the view and format as needed.

### Best Practices for High-Performance Visualizations

#### 1. Data Source Optimization

```yaml
Optimization Steps:
1. Data Preparation:
   - Clean and prepare data before analysis
   - Use appropriate data types
   - Remove unnecessary fields
   - Create data extracts for better performance

2. Query Optimization:
   - Use appropriate filters
   - Implement efficient calculations
   - Optimize data extracts
   - Monitor query performance

3. Resource Management:
   - Monitor memory usage
   - Optimize view complexity
   - Configure refresh intervals
   - Manage dashboard size
```

#### 2. Dashboard Design Optimization

```yaml
Design Best Practices:
1. Layout Optimization:
   - Use efficient dashboard layouts
   - Implement appropriate sizing
   - Optimize view placement
   - Balance information density

2. Performance Considerations:
   - Limit number of views
   - Use appropriate chart types
   - Implement efficient filters
   - Monitor dashboard performance

3. User Experience:
   - Create intuitive navigation
   - Implement clear labeling
   - Use consistent formatting
   - Provide helpful tooltips
```

#### 3. Visualization Best Practices

```yaml
Visualization Guidelines:
1. Chart Selection:
   - Choose appropriate chart types
   - Consider data relationships
   - Optimize for readability
   - Use consistent styling

2. Color Usage:
   - Implement meaningful color schemes
   - Use color for emphasis
   - Consider color blindness
   - Maintain consistency

3. Interactivity:
   - Add appropriate filters
   - Implement dashboard actions
   - Create parameter controls
   - Enable drill-down capabilities
```

## Next steps

- Continue with [Tableau case study](tableau-case-study.md) or [advanced analytics](advanced-analytics.md).
- See the submodule overview in [README](README.md) and the [module assignment](../_assignments/module-assignment.md) when you are ready for a graded exercise.

### Additional Resources

**Tableau Resources:**

- [Tableau Documentation](https://help.tableau.com/current/guides/get-started-tutorial/en-us/get-started-tutorial-home.htm)
- [Tableau Public Gallery](https://public.tableau.com/app/discover)
- [Tableau Community](https://community.tableau.com/s/)

**Support Channels:**

- Tableau Technical Support
- Community Forums
- Knowledge Base
- Training Resources

### Implementation Checklist

1. **Initial Setup:**
   - Install Tableau Desktop
   - Connect to Sample Superstore
   - Create initial worksheets
   - Test basic visualizations

2. **Performance Optimization:**
   - Configure data extracts
   - Optimize calculations
   - Implement efficient filters
   - Monitor performance

3. **Maintenance:**
   - Regular performance testing
   - Update visualizations
   - Monitor usage patterns
   - Document changes

4. **Security:**
   - Implement user permissions
   - Configure data access
   - Monitor usage
   - Maintain audit logs
