# Missing Values: Strategies for Incomplete Data

**After this lesson:** You can tell **MCAR**, **MAR**, and **MNAR** apart in plain language, explore missingness patterns in **pandas**, and pick a defensible strategy (drop, impute, or model) for a simple dataset.

## Helpful video

Pandas DataFrames in a quick walkthrough—useful for cleaning and wrangling.

<iframe width="560" height="315" src="https://www.youtube.com/embed/m1_33jhhiLE" title="Learn PANDAS in 5 minutes" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Overview

**Prerequisites:** [Data quality assessment](data-quality.md) and [Pandas](../../1-data-fundamentals/1.5-data-analysis-pandas/README.md) basics (**isna**, indexing). Optional: probability ideas from [Intro Statistics](../../1-data-fundamentals/1.3-intro-statistics/README.md).

> **Time needed:** 60–90 minutes; the code examples are dense—run them in a notebook.

> **Note:** **MCAR** (Missing Completely at Random), **MAR** (Missing at Random), and **MNAR** (Missing Not at Random) describe *why* data might be missing—see the diagram below.

Missing data is one of the most common and challenging issues in data analysis. Understanding the nature of missing values and choosing appropriate handling strategies is crucial for maintaining data integrity and ensuring reliable analysis results.

## Understanding Missing Data Mechanisms

Missing data can occur through different mechanisms, each requiring different handling approaches:

```mermaid
graph TD
    A[Missing Data] --> B[MCAR]
    A --> C[MAR]
    A --> D[MNAR]
    
    B[Missing Completely at Random] --> B1[No systematic pattern]
    B --> B2[True randomness]
    
    C[Missing at Random] --> C1[Pattern exists]
    C --> C2[Explainable by other variables]
    
    D[Missing Not at Random] --> D1[Systematic pattern]
    D --> D2[Related to missing value itself]
```

### Missing Data Mechanisms Explained

1. **Missing Completely at Random (MCAR)**
   - Definition: Missing values occur purely by chance
   - Mathematical: $P(R|X_{complete}) = P(R)$
   - Example: Survey responses lost due to system error
   - Detection: Little's MCAR test
   - Impact: Unbiased estimates possible with complete case analysis

2. **Missing at Random (MAR)**
   - Definition: Missing values depend on observed data
   - Mathematical: $P(R|X_{complete}) = P(R|X_{observed})$
   - Example: Older people more likely to skip income questions
   - Detection: Analyze patterns in observed data
   - Impact: Can be handled with multiple imputation

3. **Missing Not at Random (MNAR)**
   - Definition: Missing values depend on unobserved data
   - Mathematical: $P(R|X_{complete}) \neq P(R|X_{observed})$
   - Example: People with high incomes not reporting income
   - Detection: Requires domain knowledge
   - Impact: Most challenging to handle, may need sensitivity analysis

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight python %}
# no-output
def analyze_missing_mechanism(df):
    """
    Analyze missing data patterns to suggest likely mechanism
    
    Parameters:
    df (pandas.DataFrame): Input dataframe
    
    Returns:
    dict: Analysis results and mechanism suggestions
    """
    from scipy import stats
    
    results = {
        'missing_patterns': {},
        'correlations': {},
        'mechanism_hints': []
    }
    
    # Analyze missing patterns
    missing_patterns = df.isnull().sum() / len(df) * 100
    results['missing_patterns'] = missing_patterns.to_dict()
    
    # Check for relationships between missing values
    missing_corr = df.isnull().corr()
    results['correlations'] = missing_corr.to_dict()
    
    # Perform Little's MCAR test
    # Note: This is a simplified version
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    if len(numeric_cols) >= 2:
        chi2, p_value = stats.chi2_contingency(df[numeric_cols].isnull())[:2]
        results['littles_test'] = {
            'chi2': chi2,
            'p_value': p_value,
            'interpretation': 'MCAR possible' if p_value > 0.05 else 'Not MCAR'
        }
    
    return results
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-12" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Def analyze_missing_mechanism(df):</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–12: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="13-25" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Results = {</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 13–25: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="26-38" data-tint="3">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Perform Little&#x27;s MCAR test</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 26–38: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

## Missing Value Analysis Framework 

### 1. Detection and Visualization

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight python %}
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import missingno as msno

df = pd.read_csv('../_data/ecommerce_data.csv')

def analyze_missing_values(df):
    """Comprehensive missing value analysis"""
    
    # Basic statistics
    missing_stats = pd.DataFrame({
        'Missing Count': df.isnull().sum(),
        'Missing Percentage': (df.isnull().sum() / len(df)) * 100,
        'Data Type': df.dtypes
    })
    
    # Visualizations
    plt.figure(figsize=(15, 8))
    
    # 1. Missing value heatmap
    plt.subplot(2, 2, 1)
    sns.heatmap(df.isnull(), yticklabels=False, cbar=True)
    plt.title('Missing Value Patterns')
    
    # 2. Missing value correlation
    plt.subplot(2, 2, 2)
    msno.matrix(df)
    plt.title('Missing Value Matrix')
    
    # 3. Missing value bar chart
    plt.subplot(2, 2, 3)
    missing_stats['Missing Percentage'].plot(kind='bar')
    plt.title('Missing Value Percentage by Column')
    plt.xticks(rotation=45)
    
    # 4. Missing value correlation heatmap
    plt.subplot(2, 2, 4)
    msno.heatmap(df)
    plt.title('Missing Value Correlation')
    
    plt.tight_layout()
    plt.show()
    
    return missing_stats

# Example usage
missing_analysis = analyze_missing_values(df)
print("\nMissing Value Statistics:")
print(missing_analysis)
{% endhighlight %}

![missing-values](assets/missing-values_fig_1.png)

![missing-values](assets/missing-values_fig_2.png)

![missing-values](assets/missing-values_fig_3.png)

```

Missing Value Statistics:
             Missing Count  Missing Percentage Data Type
customer_id              0                 0.0     int64
product_id               0                 0.0     int64
order_date               0                 0.0       str
amount                   8                16.0   float64
quantity                 0                 0.0   float64
category                 0                 0.0       str
rating                   5                10.0   float64
```

</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-12" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Import pandas as pd</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–12: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="13-24" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">&#x27;Missing Percentage&#x27;: (df.isnull().sum() / le…</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 13–24: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="25-36" data-tint="3">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">2. Missing value correlation</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 25–36: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="37-49" data-tint="4">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Plt.subplot(2, 2, 4)</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 37–49: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

## Imputation Strategies Decision Tree

```mermaid
graph TD
    A[Missing Values] --> B{Data Type?}
    B -->|Numeric| C{Missing Pattern?}
    B -->|Categorical| D{Cardinality?}
    
    C -->|MCAR| C1[Mean/Median]
    C -->|MAR| C2[KNN/MICE]
    C -->|MNAR| C3[Custom Rules]
    
    D -->|Low| D1[Mode]
    D -->|High| D2[ML-based]
    D -->|Time Series| D3[Forward/Backward Fill]
```

## Advanced Imputation Techniques

### 1. Statistical Imputation

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight python %}
class StatisticalImputer:
    """Advanced statistical imputation methods"""
    
    def __init__(self, strategy='mean'):
        self.strategy = strategy
        self.statistics = {}
    
    def fit(self, df):
        """Calculate statistics for imputation"""
        for column in df.select_dtypes(include=[np.number]):
            if self.strategy == 'mean':
                self.statistics[column] = df[column].mean()
            elif self.strategy == 'median':
                self.statistics[column] = df[column].median()
            elif self.strategy == 'weighted_mean':
                # Weighted mean based on correlation
                correlations = df[column].corr(df.drop(columns=[column]))
                weights = correlations.abs() / correlations.abs().sum()
                self.statistics[column] = (df[column] * weights).sum()
    
    def transform(self, df):
        """Apply imputation"""
        df_imputed = df.copy()
        for column, value in self.statistics.items():
            df_imputed[column].fillna(value, inplace=True)
        return df_imputed
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-13" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Class StatisticalImputer:</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–13: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="14-26" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Self.statistics[column] = df[column].median()</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 14–26: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

### 2. Machine Learning Imputation

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight python %}
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier

class MLImputer:
    """Machine learning based imputation"""
    
    def __init__(self, categorical_features=None):
        self.categorical_features = categorical_features or []
        self.models = {}
    
    def fit_transform(self, df):
        df_imputed = df.copy()
        
        for column in df.columns:
            if df[column].isnull().any():
                # Prepare training data
                known_data = df[~df[column].isnull()].copy()
                missing_data = df[df[column].isnull()].copy()
                
                # Select features for prediction
                features = [f for f in df.columns if f != column]
                
                # Handle categorical features
                if column in self.categorical_features:
                    model = RandomForestClassifier(n_estimators=100)
                else:
                    model = RandomForestRegressor(n_estimators=100)
                
                # Train model
                model.fit(
                    known_data[features].fillna(0),
                    known_data[column]
                )
                
                # Predict missing values
                predictions = model.predict(
                    missing_data[features].fillna(0)
                )
                
                # Fill missing values
                df_imputed.loc[df[column].isnull(), column] = predictions
                
                self.models[column] = model
        
        return df_imputed
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-14" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">From sklearn.ensemble import RandomForestRegr…</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–14: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="15-29" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Prepare training data</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 15–29: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="30-44" data-tint="3">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Known_data[features].fillna(0),</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 30–44: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

### 3. Multiple Imputation

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight python %}
# no-output
def multiple_imputation(df, n_imputations=5):
    """Multiple imputation with uncertainty estimation"""
    
    imputed_datasets = []
    
    for i in range(n_imputations):
        # Create imputer with different random state
        imputer = IterativeImputer(
            estimator=RandomForestRegressor(),
            random_state=i,
            max_iter=10
        )
        
        # Impute values
        imputed_data = imputer.fit_transform(df)
        imputed_df = pd.DataFrame(imputed_data, columns=df.columns)
        
        imputed_datasets.append(imputed_df)
    
    # Calculate statistics across imputations
    combined_stats = {}
    for column in df.columns:
        values = np.array([df[column].values for df in imputed_datasets])
        combined_stats[column] = {
            'mean': np.mean(values, axis=0),
            'std': np.std(values, axis=0),
            'ci_lower': np.percentile(values, 2.5, axis=0),
            'ci_upper': np.percentile(values, 97.5, axis=0)
        }
    
    return imputed_datasets, combined_stats
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-10" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Def multiple_imputation(df, n_imputations=5):</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–10: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="11-20" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Max_iter=10</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 11–20: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="21-31" data-tint="3">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Combined_stats = {}</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 21–31: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

## Performance Impact Analysis

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight python %}
def analyze_imputation_impact(original_df, imputed_df, target_col):
    """Analyze impact of imputation on model performance"""
    
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_squared_error, r2_score
    
    results = {}
    
    # Split data
    X_orig = original_df.drop(columns=[target_col])
    y_orig = original_df[target_col]
    
    X_imp = imputed_df.drop(columns=[target_col])
    y_imp = imputed_df[target_col]
    
    # Train models
    models = {
        'original': RandomForestRegressor(n_estimators=100),
        'imputed': RandomForestRegressor(n_estimators=100)
    }
    
    for name, model in models.items():
        X = X_orig if name == 'original' else X_imp
        y = y_orig if name == 'original' else y_imp
        
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        
        results[name] = {
            'mse': mean_squared_error(y_test, y_pred),
            'r2': r2_score(y_test, y_pred)
        }
    
    return results
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-12" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Def analyze_imputation_impact(original_df, im…</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–12: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="13-25" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">X_imp = imputed_df.drop(columns=[target_col])</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 13–25: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="26-38" data-tint="3">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">X_train, X_test, y_train, y_test = train_test…</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 26–38: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

## Best Practices and Common Pitfalls

### 1. Data Understanding

- Always investigate why data is missing
- Consider domain knowledge
- Document assumptions

### 2. Method Selection

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight python %}
def select_imputation_method(df, column):
    """Select appropriate imputation method"""
    
    missing_rate = df[column].isnull().mean()
    data_type = df[column].dtype
    unique_ratio = df[column].nunique() / len(df)
    
    if missing_rate > 0.5:
        return "Consider dropping column"
    
    if pd.api.types.is_numeric_dtype(data_type):
        if missing_rate < 0.1:
            return "Mean/Median imputation"
        else:
            return "KNN/MICE imputation"
    
    if pd.api.types.is_categorical_dtype(data_type):
        if unique_ratio < 0.05:
            return "Mode imputation"
        else:
            return "ML-based imputation"
    
    return "Custom imputation needed"
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-11" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Def select_imputation_method(df, column):</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–11: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="12-23" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">If missing_rate &lt; 0.1:</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 12–23: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

### 3. Validation

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight python %}
def validate_imputation(original_df, imputed_df):
    """Validate imputation results"""
    
    validations = []
    
    # Check value ranges
    for column in original_df.columns:
        if pd.api.types.is_numeric_dtype(original_df[column]):
            orig_range = original_df[column].describe()
            imp_range = imputed_df[column].describe()
            
            validations.append({
                'column': column,
                'check': 'range',
                'original': [orig_range['min'], orig_range['max']],
                'imputed': [imp_range['min'], imp_range['max']]
            })
    
    # Check correlations
    orig_corr = original_df.corr()
    imp_corr = imputed_df.corr()
    
    correlation_diff = (orig_corr - imp_corr).abs().max().max()
    validations.append({
        'check': 'correlation_preservation',
        'max_difference': correlation_diff
    })
    
    return validations
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-14" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Def validate_imputation(original_df, imputed_…</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–14: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="15-29" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">&#x27;original&#x27;: [orig_range[&#x27;min&#x27;], orig_range[&#x27;m…</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 15–29: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

## Practice Exercise: E-commerce Missing Data

Scenario: You have an e-commerce dataset with missing customer and transaction data.

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight python %}
# no-output
# Load and prepare data
df = pd.read_csv('../_data/ecommerce_data.csv')

# 1. Analyze missing patterns
missing_analysis = analyze_missing_values(df)

# 2. Apply appropriate imputation
numeric_imputer = StatisticalImputer(strategy='weighted_mean')
categorical_imputer = MLImputer(
    categorical_features=['category', 'customer_segment']
)

# 3. Validate results
validation_results = validate_imputation(df, imputed_df)

# 4. Document findings
imputation_report = {
    'missing_analysis': missing_analysis,
    'imputation_methods': {
        'numeric': 'weighted_mean',
        'categorical': 'ml_based'
    },
    'validation_results': validation_results
}
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-12" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Load and prepare data</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–12: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="13-24" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">3. Validate results</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 13–24: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

Remember: "The quality of your imputation directly impacts the reliability of your analysis!"

## Next steps

- [Outliers](outliers.md) — extreme values that interact with missingness
- [Transformations](transformations.md) — scaling and encoding after cleaning
- [Exploratory Data Analysis (Module 2.3)](../2.3-eda/README.md) — validate patterns after imputation
- [Module README](README.md) — assignments and notebook
