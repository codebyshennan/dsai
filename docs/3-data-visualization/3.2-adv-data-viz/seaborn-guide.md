# Mastering Statistical Visualization with Seaborn

**After this lesson:** you can explain the core ideas in “Mastering Statistical Visualization with Seaborn” and reproduce the examples here in your own notebook or environment.

> **Note:** This lesson is **code-first**. You should understand [Matplotlib basics](../3.1-intro-data-viz/matplotlib-basics.md) and [visualization principles](../3.1-intro-data-viz/visualization-principles.md) first so you can interpret what Seaborn is doing.

## Introduction

Seaborn is your statistical visualization powerhouse - think of it as Matplotlib with a PhD in Statistics. It's designed to make complex statistical visualizations both beautiful and informative, while requiring minimal code.

### Video Tutorial: Seaborn Data Visualization

<div class="video-embed">
<iframe width="560" height="315" src="https://www.youtube.com/embed/6GUZXDef2U0" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

*Seaborn Tutorial - Data Visualization in Python*

**Seaborn at a glance**

**Purpose:** Summarize why Seaborn is used on top of Matplotlib for statistical plots and tidy data.

**Walkthrough:** Not executable code—a schematic of strengths (defaults, stats, pandas integration).

```yaml
Key Advantages:
┌─────────────────────────┐
│ Beautiful Defaults     │ → Professional look out-of-the-box
├─────────────────────────┤
│ Statistical Power      │ → Built-in statistical computations
├─────────────────────────┤
│ Pandas Integration     │ → Seamless data handling
└─────────────────────────┘
```

## Getting Started

### Professional Setup

**Purpose:** Import Seaborn and Matplotlib and set global theme, palette, font scale, and `rcParams` for figure size and label sizes.

**Walkthrough:** `sns.set_theme` wraps style + palette + font; `plt.rcParams.update` aligns Matplotlib defaults with the same look.

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set professional defaults
def setup_plotting_defaults():
    """Configure professional plotting defaults"""
    sns.set_theme(
        style="whitegrid",          # Clean, professional grid
        palette="deep",             # Professional color palette
        font="sans-serif",          # Modern font
        font_scale=1.1             # Slightly larger text
    )
    
    # Figure aesthetics
    plt.rcParams.update({
        'figure.figsize': (10, 6),
        'figure.dpi': 100,
        'axes.labelsize': 12,
        'axes.titlesize': 14,
        'xtick.labelsize': 10,
        'ytick.labelsize': 10
    })

setup_plotting_defaults()
```

### Data Loading & Inspection

**Purpose:** Load a built-in Seaborn dataset and return both the frame and a small dict of diagnostics (shape, dtypes, nulls, `describe`).

**Walkthrough:** `sns.load_dataset` ships sample CSVs; the dict pattern is handy for teaching EDA before plotting.

```python
def load_and_inspect_data(dataset_name="tips"):
    """Load and provide quick data overview"""
    # Load dataset
    data = sns.load_dataset(dataset_name)
    
    # Quick inspection
    summary = {
        "Shape": data.shape,
        "Columns": data.columns.tolist(),
        "Data Types": data.dtypes,
        "Missing Values": data.isnull().sum(),
        "Numeric Summary": data.describe()
    }
    
    return data, summary

# Example usage
tips, tips_summary = load_and_inspect_data("tips")
```

## Distribution Analysis

### 1. Single Variable Distributions

**Purpose:** Compare four views of one numeric column—histogram+KDE, box, violin, and ECDF—on one canvas.

**Walkthrough:** `histplot`/`boxplot`/`violinplot`/`ecdfplot` share `data=` and `x=` or `y=`; `GridSpec` lays out four axes.

```python
def plot_distribution_suite(data, variable):
    """Create comprehensive distribution analysis"""
    # Create figure
    fig = plt.figure(figsize=(15, 10))
    gs = fig.add_gridspec(2, 2, hspace=0.3, wspace=0.3)
    
    # Histogram with KDE
    ax1 = fig.add_subplot(gs[0, 0])
    sns.histplot(
        data=data,
        x=variable,
        kde=True,
        ax=ax1,
        palette="deep"
    )
    ax1.set_title(f'Distribution of {variable}')
    
    # Box plot
    ax2 = fig.add_subplot(gs[0, 1])
    sns.boxplot(
        data=data,
        y=variable,
        ax=ax2,
        color='skyblue'
    )
    ax2.set_title(f'Box Plot of {variable}')
    
    # Violin plot
    ax3 = fig.add_subplot(gs[1, 0])
    sns.violinplot(
        data=data,
        y=variable,
        ax=ax3,
        color='lightgreen'
    )
    ax3.set_title(f'Violin Plot of {variable}')
    
    # ECDF
    ax4 = fig.add_subplot(gs[1, 1])
    sns.ecdfplot(
        data=data,
        x=variable,
        ax=ax4,
        color='coral'
    )
    ax4.set_title(f'Empirical CDF of {variable}')
    
    plt.tight_layout()
    return fig

# Example usage
dist_fig = plot_distribution_suite(tips, "total_bill")
```


![seaborn-guide](assets/seaborn-guide_fig_1.png)

**Output:**
> **Figure (add screenshot or diagram):** Distribution Suite
### 2. Categorical Distributions

**Purpose:** Show how a numeric outcome varies across a category using box, violin, strip, and swarm plots.

**Walkthrough:** Categorical encodings use `x=` for the grouping column and `y=` for the measurement; swarm can be slow on large *n*.

```python
def plot_categorical_analysis(data, cat_var, num_var):
    """Create comprehensive categorical analysis"""
    # Create figure
    fig = plt.figure(figsize=(15, 10))
    gs = fig.add_gridspec(2, 2, hspace=0.3, wspace=0.3)
    
    # Box plot
    ax1 = fig.add_subplot(gs[0, 0])
    sns.boxplot(
        data=data,
        x=cat_var,
        y=num_var,
        ax=ax1
    )
    ax1.set_title(f'{num_var} by {cat_var} (Box Plot)')
    
    # Violin plot
    ax2 = fig.add_subplot(gs[0, 1])
    sns.violinplot(
        data=data,
        x=cat_var,
        y=num_var,
        ax=ax2
    )
    ax2.set_title(f'{num_var} by {cat_var} (Violin Plot)')
    
    # Strip plot
    ax3 = fig.add_subplot(gs[1, 0])
    sns.stripplot(
        data=data,
        x=cat_var,
        y=num_var,
        ax=ax3,
        alpha=0.5,
        jitter=0.2
    )
    ax3.set_title(f'{num_var} by {cat_var} (Strip Plot)')
    
    # Swarm plot
    ax4 = fig.add_subplot(gs[1, 1])
    sns.swarmplot(
        data=data,
        x=cat_var,
        y=num_var,
        ax=ax4
    )
    ax4.set_title(f'{num_var} by {cat_var} (Swarm Plot)')
    
    plt.tight_layout()
    return fig

# Example usage
cat_fig = plot_categorical_analysis(tips, "day", "total_bill")
```


![seaborn-guide](assets/seaborn-guide_fig_2.png)

**Output:**
> **Figure (add screenshot or diagram):** Categorical Analysis

## Relationship Analysis

### 1. Scatter Plot Suite

**Purpose:** Explore bivariate relationship with scatter, regression line, residuals, and hexbin density in one figure.

**Walkthrough:** `regplot` fits OLS; `residplot` shows errors; `hexbin` handles overlap—watch `kde`/`regplot` defaults for large data.

```python
def create_scatter_analysis(data, x_var, y_var, hue_var=None):
    """Create comprehensive scatter plot analysis"""
    # Create figure
    fig = plt.figure(figsize=(15, 10))
    gs = fig.add_gridspec(2, 2, hspace=0.3, wspace=0.3)
    
    # Basic scatter
    ax1 = fig.add_subplot(gs[0, 0])
    sns.scatterplot(
        data=data,
        x=x_var,
        y=y_var,
        hue=hue_var,
        ax=ax1
    )
    ax1.set_title('Basic Scatter Plot')
    
    # With regression line
    ax2 = fig.add_subplot(gs[0, 1])
    sns.regplot(
        data=data,
        x=x_var,
        y=y_var,
        ax=ax2,
        scatter_kws={'alpha':0.5},
        line_kws={'color': 'red'}
    )
    ax2.set_title('Scatter with Regression')
    
    # Residual plot
    ax3 = fig.add_subplot(gs[1, 0])
    sns.residplot(
        data=data,
        x=x_var,
        y=y_var,
        ax=ax3,
        scatter_kws={'alpha':0.5}
    )
    ax3.set_title('Residual Plot')
    
    # Hex bin for density
    ax4 = fig.add_subplot(gs[1, 1])
    sns.hexbin(
        data=data,
        x=x_var,
        y=y_var,
        ax=ax4,
        gridsize=20,
        cmap='YlOrRd'
    )
    ax4.set_title('Hexbin Density Plot')
    
    plt.tight_layout()
    return fig

# Example usage
scatter_fig = create_scatter_analysis(tips, "total_bill", "tip", "time")
```

**Output:**
> **Figure (add screenshot or diagram):** Scatter Analysis
### 2. Complex Relationships

**Purpose:** Combine `PairGrid` (same y vs x with hue) and `FacetGrid` (small multiples by category) for multivariate views.

**Walkthrough:** `PairGrid.map` applies a plotting function row-wise; `FacetGrid.map_dataframe` passes column names to `scatterplot`.

```python
def analyze_complex_relationships(data, x_var, y_var, cat_vars):
    """Analyze relationships with categorical variables"""
    # Create pair grid
    g = sns.PairGrid(
        data,
        x_vars=[x_var],
        y_vars=[y_var],
        hue=cat_vars[0],
        height=8
    )
    
    # Add different plots
    g.map(sns.scatterplot, alpha=0.7)
    g.add_legend()
    
    # Create facet grid
    g2 = sns.FacetGrid(
        data,
        col=cat_vars[0],
        row=cat_vars[1] if len(cat_vars) > 1 else None,
        height=4,
        aspect=1.5
    )
    
    # Add plot layers
    g2.map_dataframe(sns.scatterplot, x_var, y_var)
    g2.add_legend()
    
    return g, g2

# Example usage
pair_g, facet_g = analyze_complex_relationships(
    tips, "total_bill", "tip", ["time", "day"]
)
```


![seaborn-guide](assets/seaborn-guide_fig_3.png)


![seaborn-guide](assets/seaborn-guide_fig_4.png)


![seaborn-guide](assets/seaborn-guide_fig_5.png)

**Output - Pair Grid:**
> **Figure (add screenshot or diagram):** Pair Plot
**Output - Facet Grid:**
> **Figure (add screenshot or diagram):** Facet Grid
## Matrix Visualizations

### 1. Correlation Analysis

**Purpose:** Numeric correlation matrix as a labeled heatmap and as a clustered heatmap to reveal variable groups.

**Walkthrough:** `select_dtypes` keeps numeric columns; `heatmap` vs `clustermap`—second reorders rows/columns by similarity.

```python
def create_correlation_analysis(data, method='pearson'):
    """Create comprehensive correlation analysis"""
    # Compute correlations
    corr = data.select_dtypes(include=[np.number]).corr(method=method)
    
    # Create figure
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))
    
    # Heatmap
    sns.heatmap(
        corr,
        annot=True,
        cmap='coolwarm',
        center=0,
        ax=ax1,
        fmt='.2f'
    )
    ax1.set_title('Correlation Heatmap')
    
    # Clustermap
    sns.clustermap(
        corr,
        annot=True,
        cmap='coolwarm',
        center=0,
        fmt='.2f',
        figsize=(10, 10)
    )
    
    return fig

# Example usage
corr_fig = create_correlation_analysis(tips)
```


![seaborn-guide](assets/seaborn-guide_fig_6.png)


![seaborn-guide](assets/seaborn-guide_fig_7.png)

**Output - Heatmap:**
> **Figure (add screenshot or diagram):** Correlation Heatmap
**Output - Clustermap:**
> **Figure (add screenshot or diagram):** Clustermap
### Additional Visualization Examples

**Bar Plot with Error Bars:**
> **Figure (add screenshot or diagram):** Bar Plot
**Count Plot:**
> **Figure (add screenshot or diagram):** Count Plot
**Joint Plot:**
> **Figure (add screenshot or diagram):** Joint Plot
**Time Series Heatmap:**
> **Figure (add screenshot or diagram):** Flights Heatmap
**Line Plot:**
> **Figure (add screenshot or diagram):** Line Plot
## Best Practices

### 1. Style Management

**Purpose:** Switch Seaborn themes for slides (`presentation`), papers (`paper`), or notebooks (`notebook`) from one function.

**Walkthrough:** Dict holds kwargs for `sns.set_theme`; unknown keys fall back to `notebook`.

```python
def set_plot_style(style_type='presentation'):
    """Set plot style based on context"""
    styles = {
        'presentation': {
            'style': 'whitegrid',
            'palette': 'deep',
            'font_scale': 1.2,
            'figure.figsize': (12, 8)
        },
        'paper': {
            'style': 'ticks',
            'palette': 'colorblind',
            'font_scale': 0.8,
            'figure.figsize': (8, 6)
        },
        'notebook': {
            'style': 'darkgrid',
            'palette': 'muted',
            'font_scale': 1.0,
            'figure.figsize': (10, 6)
        }
    }
    
    style = styles.get(style_type, styles['notebook'])
    sns.set_theme(**style)
    return style

# Example usage
style = set_plot_style('presentation')
```

### 2. Export Settings

**Purpose:** Write the same figure to PDF, PNG, and SVG with tight bounding boxes for documents and web.

**Walkthrough:** Loop over extensions; `savefig` on the Matplotlib `Figure` returned by Seaborn plotting functions.

```python
def save_publication_quality(fig, filename, dpi=300):
    """Save figure in publication quality"""
    # Save in multiple formats
    formats = {
        'pdf': {'bbox_inches': 'tight'},
        'png': {'dpi': dpi, 'bbox_inches': 'tight'},
        'svg': {'bbox_inches': 'tight'}
    }
    
    for fmt, settings in formats.items():
        fig.savefig(f'{filename}.{fmt}', **settings)

# Example usage
save_publication_quality(scatter_fig, 'scatter_analysis')
```

Remember:

- Start with data exploration
- Choose appropriate visualizations
- Keep it simple but informative
- Consider your audience
- Use consistent styling
- Save high-quality outputs

## Next steps

- Continue with [Interactive visualization with Plotly](plotly-guide.md).
- Review the [3.2 Advanced data visualization](README.md) overview and the [module assignment](../_assignments/module-assignment.md) when assigned.
