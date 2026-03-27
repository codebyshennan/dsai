# Exploratory Data Analysis Assignment

**After this lesson:** You produce a short EDA report (notebook or slides) with distributions, key relationships, and clear limitations—grounded in the [EDA README](README.md) workflow.

## Helpful video

Summarizing distributions with percentiles—common in exploratory analysis.

<iframe width="560" height="315" src="https://www.youtube.com/embed/IFKQLDmRK0Y" title="Quantiles and Percentiles, Clearly Explained" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Overview

**Prerequisites:** [Distributions](distributions.md), [relationships](relationships.md), and [time series](time-series.md) readings (or parallel skimming). [Wrangling (Module 2.2)](../2.2-data-wrangling/README.md) should be done or in progress.

> **Time needed:** Often 6–10 hours including polish.

## Why this matters

EDA deliverables should read like **evidence**, not a gallery of plots: each figure should answer a stated question, and the write-up should name **limitations** (time window, selection bias, missing fields) alongside conclusions.

In this assignment, you perform exploratory data analysis on a realistic e-commerce-style dataset. You apply the workflow from the readings to uncover patterns, relationships, and trends—and to document what you cannot claim from the data alone.

## Dataset Description

You'll be working with an e-commerce dataset containing:

- Customer transactions
- Product information
- Temporal data
- Customer demographics
- Sales metrics

## Setup

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight python %}
# Required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from statsmodels.tsa.seasonal import seasonal_decompose

# Load the dataset
df = pd.read_csv('../_data/ecommerce_data.csv')
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-10" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Required libraries</span>
    </div>
    <div class="code-callout__body">
      <p><strong>Required libraries</strong> — lines 1-10 in the highlighted code. Identify what this band does: DDL (table/column definitions), row changes (<code>INSERT</code>/<code>UPDATE</code>/<code>DELETE</code>), or a <code>SELECT</code> pipeline—then read joins and predicates in snippet order.</p>
    </div>
  </div>
</aside>
</div>

## Tasks

### 1. Data Distribution Analysis (25 points)

a) Numeric Variables (15 points)

- Analyze the distribution of sales amounts
- Examine customer spending patterns
- Study product pricing distributions
- Identify and handle outliers
- Transform skewed distributions if necessary

b) Categorical Variables (10 points)

- Analyze product category distributions
- Examine customer demographics
- Study geographical distributions
- Create meaningful visualizations for each

### 2. Relationship Analysis (25 points)

a) Numeric Relationships (10 points)

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight python %}
# Example structure
def analyze_numeric_relationships(data):
    """
    Analyze relationships between numeric variables
    """
    # Your code here
    return analysis_results
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-7" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Example structure</span>
    </div>
    <div class="code-callout__body">
      <p><strong>Example structure</strong> — lines 1-7 in the highlighted code. Identify what this band does: DDL (table/column definitions), row changes (<code>INSERT</code>/<code>UPDATE</code>/<code>DELETE</code>), or a <code>SELECT</code> pipeline—then read joins and predicates in snippet order.</p>
    </div>
  </div>
</aside>
</div>

b) Categorical Relationships (10 points)

- Cross-tabulations of categories
- Chi-square tests of independence
- Visualization of category relationships

c) Mixed Variable Analysis (5 points)

- Compare numeric variables across categories
- Analyze variance between groups
- Create box plots and violin plots

### 3. Time Series Analysis (25 points)

a) Temporal Patterns (10 points)

- Daily sales patterns
- Weekly trends
- Monthly seasonality
- Year-over-year growth

b) Decomposition (10 points)

- Trend analysis
- Seasonal patterns
- Residual analysis
- Moving averages

c) Anomaly Detection (5 points)

- Identify unusual patterns
- Detect seasonal anomalies
- Flag suspicious transactions

### 4. Advanced Analysis (15 points)

a) Customer Segmentation

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight python %}
# no-output
def segment_customers(data):
    """
    Segment customers based on behavior
    """
    # Calculate RFM metrics
    recency = # Calculate recency
    frequency = # Calculate frequency
    monetary = # Calculate monetary value
    
    # Perform clustering
    # Your code here
    
    return segments
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-13" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Def segment_customers(data):</span>
    </div>
    <div class="code-callout__body">
      <p><strong>Def segment_customers(data):</strong> — lines 1-13. Walk this block top to bottom: imports, inputs, then the transformation or plot that uses them.</p>
    </div>
  </div>
</aside>
</div>

b) Product Analysis

- Analyze product affinities
- Study category performance
- Identify top performers

c) Geographic Analysis

- Regional sales patterns
- Location-based trends
- Market penetration analysis

### 5. Documentation and Presentation (10 points)

a) Analysis Report

- Executive summary
- Key findings
- Methodology description
- Recommendations

b) Visualizations

- Clear and informative plots
- Proper labeling
- Consistent styling
- Interactive elements (optional)

## Deliverables

1. Jupyter Notebook containing:
   - All analysis code
   - Visualizations
   - Markdown explanations
   - Results interpretation

2. Summary Report (PDF) including:
   - Methodology overview
   - Key findings
   - Business recommendations
   - Future analysis suggestions

3. Presentation Slides:
   - Key visualizations
   - Main insights
   - Actionable recommendations

## Evaluation Criteria

- Code quality and organization (20%)
- Analysis depth and accuracy (30%)
- Visualization effectiveness (20%)
- Insights and interpretation (20%)
- Documentation clarity (10%)

## Solution Template

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight python %}
# 1. Initial Setup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Load and prepare data
def load_and_prepare_data():
    """
    Load and prepare the dataset for analysis
    """
    # Load data
    df = pd.read_csv('../_data/ecommerce_data.csv')
    
    # Basic cleaning
    df['date'] = pd.to_datetime(df['date'])
    
    # Handle missing values
    # Your code here
    
    return df

# 2. Distribution Analysis
def analyze_distributions(data):
    """
    Analyze and visualize distributions
    """
    # Numeric distributions
    numeric_cols = data.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        plt.figure(figsize=(10, 6))
        sns.histplot(data[col], kde=True)
        plt.title(f'Distribution of {col}')
        plt.show()
        
        # Calculate statistics
        print(f"\nStatistics for {col}:")
        print(data[col].describe())
    
    # Categorical distributions
    categorical_cols = data.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        plt.figure(figsize=(10, 6))
        data[col].value_counts().plot(kind='bar')
        plt.title(f'Distribution of {col}')
        plt.xticks(rotation=45)
        plt.show()

# 3. Relationship Analysis
def analyze_relationships(data):
    """
    Analyze relationships between variables
    """
    # Correlation matrix
    numeric_data = data.select_dtypes(include=[np.number])
    correlation_matrix = numeric_data.corr()
    
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.show()
    
    # Categorical relationships
    # Your code here

# 4. Time Series Analysis
def analyze_time_series(data):
    """
    Perform time series analysis
    """
    # Set date as index
    data = data.set_index('date')
    
    # Daily patterns
    daily_sales = data.resample('D')['sales'].sum()
    
    # Plot trends
    plt.figure(figsize=(15, 5))
    daily_sales.plot()
    plt.title('Daily Sales Trend')
    plt.show()
    
    # Decomposition
    # Your code here

# 5. Generate Report
def generate_report(data, analysis_results):
    """
    Generate analysis report
    """
    report = {
        'summary_statistics': data.describe(),
        'correlation_analysis': analysis_results['correlations'],
        'time_series_patterns': analysis_results['temporal_patterns'],
        'key_findings': analysis_results['findings']
    }
    
    return report

# Main execution
if __name__ == "__main__":
    # Load data
    df = load_and_prepare_data()
    
    # Perform analyses
    analyze_distributions(df)
    analyze_relationships(df)
    analyze_time_series(df)
    
    # Generate report
    results = {
        'correlations': None,  # Add your results
        'temporal_patterns': None,  # Add your results
        'findings': []  # Add your findings
    }
    
    report = generate_report(df, results)
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-19" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">1. Initial Setup</span>
    </div>
    <div class="code-callout__body">
      <p><strong>1. Initial Setup</strong> — lines 1-19 in the highlighted code. Identify what this band does: DDL (table/column definitions), row changes (<code>INSERT</code>/<code>UPDATE</code>/<code>DELETE</code>), or a <code>SELECT</code> pipeline—then read joins and predicates in snippet order.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="20-39" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Your code here</span>
    </div>
    <div class="code-callout__body">
      <p><strong>Your code here</strong> — lines 20-39 in the highlighted code. Identify what this band does: DDL (table/column definitions), row changes (<code>INSERT</code>/<code>UPDATE</code>/<code>DELETE</code>), or a <code>SELECT</code> pipeline—then read joins and predicates in snippet order.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="40-59" data-tint="3">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Categorical distributions</span>
    </div>
    <div class="code-callout__body">
      <p><strong>Categorical distributions</strong> — lines 40-59 in the highlighted code. Identify what this band does: DDL (table/column definitions), row changes (<code>INSERT</code>/<code>UPDATE</code>/<code>DELETE</code>), or a <code>SELECT</code> pipeline—then read joins and predicates in snippet order.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="60-78" data-tint="4">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Sns.heatmap(correlation_matrix, annot=True, c…</span>
    </div>
    <div class="code-callout__body">
      <p><strong>Sns.heatmap(correlation_matrix, annot=True, c…</strong> — lines 60-78 in the highlighted code. Identify what this band does: DDL (table/column definitions), row changes (<code>INSERT</code>/<code>UPDATE</code>/<code>DELETE</code>), or a <code>SELECT</code> pipeline—then read joins and predicates in snippet order.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="79-98" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Plt.figure(figsize=(15, 5))</span>
    </div>
    <div class="code-callout__body">
      <p><strong>Plt.figure(figsize=(15, 5))</strong> — lines 79-98 in the highlighted code. Identify what this band does: DDL (table/column definitions), row changes (<code>INSERT</code>/<code>UPDATE</code>/<code>DELETE</code>), or a <code>SELECT</code> pipeline—then read joins and predicates in snippet order.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="99-118" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Return report</span>
    </div>
    <div class="code-callout__body">
      <p><strong>Return report</strong> — lines 99-118 in the highlighted code. Identify what this band does: DDL (table/column definitions), row changes (<code>INSERT</code>/<code>UPDATE</code>/<code>DELETE</code>), or a <code>SELECT</code> pipeline—then read joins and predicates in snippet order.</p>
    </div>
  </div>
</aside>
</div>

## Tips for Success

1. **Start with Questions**
   - Define analysis objectives
   - Form hypotheses
   - Plan visualization strategy
   - Consider business context

2. **Be Systematic**
   - Follow a structured approach
   - Document your process
   - Validate findings
   - Cross-check results

3. **Focus on Insights**
   - Look beyond basic statistics
   - Consider business implications
   - Identify actionable findings
   - Provide clear recommendations

4. **Create Clear Visualizations**
   - Choose appropriate plots
   - Use consistent styling
   - Add proper labels
   - Include explanations

## Bonus Challenges

1. **Advanced Visualization**
   - Create interactive plots
   - Build a dashboard
   - Implement custom visualizations
   - Add animation

2. **Statistical Analysis**
   - Hypothesis testing
   - Confidence intervals
   - Effect size calculations
   - Power analysis

3. **Machine Learning Integration**
   - Clustering analysis
   - Anomaly detection
   - Pattern recognition
   - Predictive modeling

Good luck! Remember to focus on generating actionable insights from your analysis!
