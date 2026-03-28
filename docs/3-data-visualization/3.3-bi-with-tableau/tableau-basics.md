# Tableau Basics: Sample Superstore Guide

**After this lesson:** you can explain the core ideas in “Tableau Basics: Sample Superstore Guide” and reproduce the examples here in your own notebook or environment.

> **Note:** This submodule is **UI-first**. You will follow clicks and shelves in Tableau Desktop rather than writing Python for the main workflow.

## Helpful video

Short Tableau Public install; pair with the written guides in this folder.

<iframe width="560" height="315" src="https://www.youtube.com/embed/lTNWfhmurUg" title="Tableau Public Tutorial Download and Setup" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

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

> **Figure (add screenshot or diagram):** Tableau Desktop start page — the Connect pane on the left listing data source options, with "Sample - Superstore" visible under Saved Data Sources and highlighted for selection.

- In the Connect pane on the left, under **Saved Data Sources**, click **Sample - Superstore**.

2. Preview the data source.

> **Figure (add screenshot or diagram):** Tableau's Data Source tab showing the Sample Superstore connection — the Orders table selected on the left, a scrollable data-grid preview on the right with row count, and the Dimensions/Measures panel showing field data types in green and blue.

- Review the data structure. Dimensions (blue) and measures (green) appear in the pane.
- Scan the first 1,000 rows to confirm fields look reasonable.

3. Open a new worksheet.

> **Figure (add screenshot or diagram):** A blank Tableau worksheet — the Data pane on the left showing Dimensions (blue) and Measures (green) fields, empty Rows and Columns shelves at the top, Marks card on the left, and a white canvas in the center ready for visualization.

- Click **New Worksheet** and familiarize yourself with shelves, marks, and the Data pane.

#### 2. Creating Your First Visualization

Example: **Sales by Category** bar chart.

1. Build the chart.

> **Figure (add screenshot or diagram):** Tableau worksheet mid-drag — the Category field being dragged from the Data pane to the Rows shelf, with Sales already on the Columns shelf and a horizontal bar chart of three categories visible on the canvas.

- Drag **Category** to **Rows**.
- Drag **Sales** to **Columns**. Tableau should show a horizontal bar chart.

2. Customize and refine.

> **Figure (add screenshot or diagram):** Formatted Sales by Category bar chart — bars sorted descending (Technology at top), each bar colored by category, data labels showing exact dollar values on each bar, and the Sort and Color controls in the toolbar highlighted.

- Use **Show Me** if needed.
- Sort bars by sales (descending), add color by category, and add data labels.

3. Format the view.

> **Figure (add screenshot or diagram):** Tableau's Format pane open as a left sidebar — showing Font, Alignment, Shading, and Border tabs for the selected axis element; the axis label font size and color fields visible and editable.

- Adjust axis labels, colors, title, and number formats.

#### 3. Adding Filters and Interactivity

1. Add filters.

> **Figure (add screenshot or diagram):** Tableau worksheet with the Filters shelf showing the Region field dragged in — the Filter dialog open with all four regions (East, West, North, South) listed with checkboxes, and two regions selected.

- Drag **Region** to **Filters**, choose regions, and apply.

2. Create parameters (optional).

> **Figure (add screenshot or diagram):** Tableau's Create Parameter dialog — data type set to String, the "List" radio button selected, and a table of allowed values (e.g. region names) filled in; the parameter name field showing "Select Region" at the top.

- Right-click in the Data pane, choose **Create Parameter**, configure it, and add the control to the view.

3. Use dashboard actions.

> **Figure (add screenshot or diagram):** Tableau's Dashboard Actions dialog — a Filter Action configured with the bar chart as source sheet and the map as target sheet; "Run action on: Select" chosen, and "Clearing the selection will: Show all values" set.

- On a dashboard, add multiple sheets and configure filter or highlight actions.

#### 4. Building a Complete Dashboard

1. Layout.

> **Figure (add screenshot or diagram):** Tableau dashboard editing mode — the Sheets panel on the left listing available worksheets, a bar chart tile dragged onto the top half of the canvas, and a map tile being dragged into the bottom half, with layout sizing handles visible.

- Create a **New Dashboard**, add worksheets, and arrange tiles.

2. Interactivity.

> **Figure (add screenshot or diagram):** Completed Tableau dashboard showing interactive filtering in action — one category bar selected (highlighted) on the bar chart, the map automatically updated to show only that category's states, and a Region filter control visible on the right side.

- Add filters, actions, parameter controls, and navigation as needed.

3. Final polish.

> **Figure (add screenshot or diagram):** Polished Tableau dashboard with a branded title banner at the top, a Sales by Category bar chart (top-left), a US state choropleth map (top-right), consistent color legend, and a tooltip visible on a hovered state showing Sales and Profit values.

- Add legends, align colors, adjust spacing, and tune tooltips.

### Common Visualization Examples

#### 1. Sales Analysis Dashboard

1. Sales trend.

> **Figure (add screenshot or diagram):** Tableau line chart with Order Date (Month/Year) on Columns and Sales on Rows — a smooth blue trend line with a lighter 95% confidence band overlay, and formatted month/year tick labels on the x-axis.

- **Order Date** (Month) on **Columns**, **Sales** on **Rows**. Add a trend line and format dates.

2. Geographic map.

> **Figure (add screenshot or diagram):** Tableau filled map of the United States — each state shaded by Sales using a blue color gradient (light blue = low, dark blue = high), state labels visible, and a tooltip open on California showing State name and total Sales.

- **State** on the map, **Sales** on **Color**, labels and tooltips as needed.

3. Category breakdown.

> **Figure (add screenshot or diagram):** Tableau horizontal bar chart with Category on Rows and Sales on Columns, sorted descending, with percentage-of-total labels on each bar (e.g. "Technology 36%") and matching category colors.

- **Category** on **Rows**, **Sales** on **Columns**, sort and add percentage labels if useful.

#### 2. Profit Analysis Dashboard

1. Profit by sub-category.

> **Figure (add screenshot or diagram):** Tableau text/heat map with Sub-Category on Columns and Category on Rows — cells colored by Profit using a diverging red-blue palette (red = loss, blue = profit), with Profit values shown as text labels inside each cell.

- **Sub-Category** on **Columns**, **Category** on **Rows**, **Profit** on **Color**.

2. Discount impact.

> **Figure (add screenshot or diagram):** Tableau scatter plot of Discount (x-axis) vs Profit Ratio (y-axis) — individual orders as dots clustered near low discount on the left, with a downward-sloping red trend line and a shaded 95% confidence band showing the negative relationship.

- **Discount** on one axis, **Profit Ratio** on the other; add a trend line or bins.

3. Regional performance.

> **Figure (add screenshot or diagram):** Tableau map with US regions shaded by Profit using a diverging palette — a tooltip open on the South region showing Region name, total Sales, and total Profit; a reference line annotation marking the average profit threshold.

- **Region** on the map, **Profit** on **Color**, reference lines and tooltips as needed.

### Advanced Features

#### 1. Calculated Fields

1. Profit ratio.

> **Figure (add screenshot or diagram):** Tableau's Create Calculated Field dialog — the field named "Profit Ratio" with the formula `SUM([Profit])/SUM([Sales])` typed in the formula bar; a green checkmark in the lower-left confirming the syntax is valid.

- Formula: `SUM([Profit])/SUM([Sales])`
- Right-click in the Data pane, **Create Calculated Field**, enter the formula, and name the field.

2. Year-over-year growth.

> **Figure (add screenshot or diagram):** Tableau's Edit Table Calculation dialog for year-over-year growth — "Compute Using: Table (across)" selected, the formula visible at the top, and the result formatted as a percentage in the underlying view.

- Example: `(SUM([Sales]) - LOOKUP(SUM([Sales]), -1))/ABS(LOOKUP(SUM([Sales]), -1))`
- Set up as a table calculation and format as a percentage.

#### 2. Level of Detail Expressions

1. Fixed LOD.

> **Figure (add screenshot or diagram):** Tableau's Calculated Field dialog showing a FIXED LOD expression: `{FIXED [Category] : SUM([Sales])}` — the scope keyword highlighted and the aggregate function visible, with the field named "Category Total Sales".

- Example: `{FIXED [Category] : SUM([Sales])}`
- Create a calculated field, enter the LOD expression, apply to the view.

2. Include LOD.

> **Figure (add screenshot or diagram):** Tableau worksheet with an INCLUDE LOD field added to the Color mark — the view showing average profit colored by region while the level of detail is finer than the view's row/column structure.

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
