# Statistical Tests: Your Data Analysis Toolkit

**After this lesson:** you can explain the core ideas in “Statistical Tests: Your Data Analysis Toolkit” and reproduce the examples here in your own notebook or environment.

## Overview

This lesson is a **selector map**: given your outcome type (numeric vs counts vs paired), number of groups, and rough assumptions, you pick a test that matches the data-generating story. [Hypothesis formulation](./hypothesis-formulation.md) gave you \\(H_0\\) and \\(H_1\\); here you attach a concrete test statistic and null distribution. The next lessons apply the same logic in product-style [A/B testing](./ab-testing.md) and in [reporting](./results-analysis.md).

## Why this matters

- Choosing the **wrong test** wastes time and can mislead stakeholders.
- You will map data types and study design to common tests and know when to seek non-parametric alternatives.

## Prerequisites

- [Hypothesis formulation](./hypothesis-formulation.md) and [Experimental design](./experimental-design.md).
- [A/B testing](./ab-testing.md) comes next in this submodule; you do not need it to choose tests here.

> **Important:** Pick the test before you analyze; note if you adjust after seeing the data.

## Introduction

Statistical tests are essential tools for analyzing data. They help you determine whether observed patterns, differences, or relationships in your data are likely to be real or just due to random chance. By using the right statistical test, you can make informed, evidence-based decisions rather than relying on intuition alone.

### Video Tutorial: Statistical Tests Explained

<div class="video-embed">
<iframe width="560" height="315" src="https://www.youtube.com/embed/NF5_btOaCig" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

*StatQuest: Using Linear Models for t-tests and ANOVA, Clearly Explained!!! by Josh Starmer*

<div class="video-embed">
<iframe width="560" height="315" src="https://www.youtube.com/embed/7_cs1YlZoug" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

*Chi-Square Tests: Crash Course Statistics #29*

## How to Choose the Right Statistical Test

Choosing the correct test depends on your research question, the type of data you have, and the assumptions your data meets. Use the decision tree below to guide your choice:

{% include mermaid-diagram.html src="4-stat-analysis/4.2-hypotheses-testing/diagrams/statistical-tests-1.mmd" %}

> **Figure (add screenshot or diagram):** Full statistical test decision tree poster — numeric vs categorical, parametric vs non-parametric, one-sample vs two-sample vs k-sample branches.

- **Numerical data (means):** Use t-tests or ANOVA.
- **Categorical data (counts/frequencies):** Use chi-square tests.
- **Relationships between variables:** Use correlation or regression tests.

## Overview of Common Statistical Tests

### 1. T-Tests: Comparing Means

**When to use:**

- Comparing the means of two groups (e.g., test vs. control).
- Data should be approximately normally distributed.

**Types:**

- **One-sample t-test:** Compare sample mean to a known value.
- **Independent t-test:** Compare means of two independent groups.
- **Paired t-test:** Compare means from the same group at different times.

**Assumptions:**

- Data are continuous and approximately normal.
- Groups have similar variances (for independent t-test).
- Observations are independent (except for paired t-test).

**Example:**

**Independent two-sample t-test with effect size**

**Purpose:** Run a classic independent-groups t-test on small numeric arrays, compute a simple standardized mean difference (using the control SD), and return a single human-readable verdict at \\(\alpha = 0.05\\).

**Walkthrough:** `stats.ttest_ind` produces `t_stat` and `p_value`; the effect size line mirrors Cohen-style scaling; the returned dict keeps statistics and a printable `explanation` string.

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight python %}
# Self-contained example: Independent t-test
import numpy as np
from scipy import stats

# Example data: two groups
control_data = np.array([8, 9, 7, 10, 9])
treatment_data = np.array([12, 11, 13, 12, 14])

def perform_ttest(control_data, treatment_data, alpha=0.05):
    """Perform an independent t-test and explain the results."""
    t_stat, p_value = stats.ttest_ind(control_data, treatment_data)
    effect_size = (np.mean(treatment_data) - np.mean(control_data)) / np.std(control_data)
    explanation = (
        f"T-statistic: {t_stat:.2f}, P-value: {p_value:.3f}. "
        f"Effect size: {effect_size:.2f}. "
        f"{'Significant difference' if p_value < alpha else 'No significant difference'} "
        f"between group means at alpha={alpha}."
    )
    return {
        't_statistic': t_stat,
        'p_value': p_value,
        'effect_size': effect_size,
        'significant': p_value < alpha,
        'explanation': explanation
    }

result = perform_ttest(control_data, treatment_data)
print(result['explanation'])
# Sample output:
# T-statistic: -4.47, P-value: 0.002. Effect size: 3.00. Significant difference between group means at alpha=0.05.
{% endhighlight %}

</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-7" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Setup and data</span>
    </div>
    <div class="code-callout__body">
      <p>Import NumPy and SciPy, then define two small control and treatment arrays to feed the t-test function.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="9-12" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">T-test and effect size</span>
    </div>
    <div class="code-callout__body">
      <p>Run <code>stats.ttest_ind</code> for t and p, then compute a Cohen-style standardized mean difference using the control SD.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="13-25" data-tint="3">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Explanation string</span>
    </div>
    <div class="code-callout__body">
      <p>Format a human-readable summary combining the test statistic, p-value, effect size, and significance verdict at the chosen alpha.</p>
    </div>
  </div>
</aside>
</div>

```
T-statistic: -5.27, P-value: 0.001. Effect size: 3.73. Significant difference between group means at alpha=0.05.
```

### 2. ANOVA: Comparing More Than Two Groups

**When to use:**

- Comparing means across three or more groups.
- Data should be approximately normally distributed.

**Assumptions:**

- Data are continuous and approximately normal.
- Groups have similar variances.
- Observations are independent.

**Example:**

**One-way ANOVA with eta-squared**

**Purpose:** Compare means of three or more groups with `f_oneway`, summarize how much variance sits between groups (\\(\eta^2\\)), and state whether any mean differs at the chosen \\(\alpha\\).

**Walkthrough:** `stats.f_oneway(*groups)` for F and p; \\(\eta^2\\) uses between-group and total sum of squares; the function mirrors the t-test helper pattern (stats + explanation string).

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight python %}
# Self-contained example: One-way ANOVA
from scipy import stats
import numpy as np

# Example data: three groups
group1 = np.array([5, 6, 7, 5, 6])
group2 = np.array([8, 9, 7, 8, 9])
group3 = np.array([10, 11, 12, 10, 11])

def perform_anova(*groups, alpha=0.05):
    """Perform one-way ANOVA and explain the results."""
    f_stat, p_value = stats.f_oneway(*groups)
    group_means = [np.mean(g) for g in groups]
    grand_mean = np.mean(np.concatenate(groups))
    ss_between = sum(len(g) * (np.mean(g) - grand_mean)**2 for g in groups)
    ss_total = sum(sum((x - grand_mean)**2 for x in g) for g in groups)
    eta_squared = ss_between / ss_total
    explanation = (
        f"F-statistic: {f_stat:.2f}, P-value: {p_value:.3f}. "
        f"Effect size (eta-squared): {eta_squared:.2f}. "
        f"{'At least one group mean is significantly different' if p_value < alpha else 'No significant difference between group means'} "
        f"at alpha={alpha}."
    )
    return {
        'f_statistic': f_stat,
        'p_value': p_value,
        'effect_size': eta_squared,
        'significant': p_value < alpha,
        'explanation': explanation
    }

result = perform_anova(group1, group2, group3)
print(result['explanation'])
# Sample output:
# F-statistic: 44.00, P-value: 0.000. Effect size (eta-squared): 0.88. At least one group mean is significantly different at alpha=0.05.
{% endhighlight %}

</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-8" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Three-group data</span>
    </div>
    <div class="code-callout__body">
      <p>Define three clearly separated groups (means ~6, 8, 11) as toy examples for the ANOVA function.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="10-17" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">F-test and eta-squared</span>
    </div>
    <div class="code-callout__body">
      <p>Run <code>f_oneway</code> then compute eta-squared (between-group SS / total SS) as a proportion-of-variance effect size.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="18-30" data-tint="3">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Result dict</span>
    </div>
    <div class="code-callout__body">
      <p>Bundle F, p, eta-squared, significance flag, and a formatted explanation string for display or downstream reporting.</p>
    </div>
  </div>
</aside>
</div>

```
F-statistic: 44.67, P-value: 0.000. Effect size (eta-squared): 0.88. At least one group mean is significantly different at alpha=0.05.
```

### 3. Chi-Square Tests: Analyzing Categorical Data

**When to use:**

- Testing if observed frequencies differ from expected frequencies (goodness of fit).
- Testing if two categorical variables are independent (contingency table).

**Assumptions:**

- Data are counts/frequencies (not means).
- Observations are independent.
- Expected frequency in each cell should be at least 5.

**Example:**

**Chi-square: goodness-of-fit vs independence**

**Purpose:** See how one function can dispatch to `chisquare` (goodness of fit) or `chi2_contingency` (tables), and attach a simple effect-size label (Cramer’s V is computed here for illustration).

**Walkthrough:** When `expected` is passed, the contingency path runs; `chisquare` is used when testing counts against a uniform or custom expected pattern; the returned dict includes `test_type` for reporting.

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight python %}
# Self-contained example: Chi-square test (goodness of fit)
import numpy as np
from scipy import stats

# Example observed frequencies (e.g., dice rolls)
observed = np.array([18, 22, 20, 15, 17, 18])
# Expected frequencies (fair dice)
expected = np.array([18.33, 18.33, 18.33, 18.33, 18.33, 18.33])

def perform_chi_square(observed, expected=None, alpha=0.05):
    """Perform chi-square test and explain the results."""
    if expected is None:
        # Goodness of fit test
        chi2, p_value = stats.chisquare(observed)
        test_type = 'Goodness of fit'
    else:
        # Test of independence (contingency table)
        chi2, p_value, _, _ = stats.chi2_contingency(observed)
        test_type = 'Test of independence'
    n = np.sum(observed)
    min_dim = min(np.array(observed).shape) - 1
    cramer_v = np.sqrt(chi2 / (n * min_dim)) if min_dim > 0 else np.nan
    explanation = (
        f"Chi-square: {chi2:.2f}, P-value: {p_value:.3f}. "
        f"Effect size (Cramer's V): {cramer_v:.2f}. "
        f"{'Significant association' if p_value < alpha else 'No significant association'} "
        f"at alpha={alpha}."
    )
    return {
        'chi2_statistic': chi2,
        'p_value': p_value,
        'effect_size': cramer_v,
        'significant': p_value < alpha,
        'test_type': test_type,
        'explanation': explanation
    }

result = perform_chi_square(observed, expected)
print(result['explanation'])
# Sample output:
# Chi-square: 1.18, P-value: 0.946. Effect size (Cramer's V): 0.20. No significant association at alpha=0.05.
{% endhighlight %}

</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-9" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Data setup</span>
    </div>
    <div class="code-callout__body">
      <p>Define observed dice-roll counts and uniform expected counts for a goodness-of-fit scenario.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="11-22" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Test dispatch</span>
    </div>
    <div class="code-callout__body">
      <p>Branch on whether <code>expected</code> is provided: use <code>chisquare</code> for goodness of fit or <code>chi2_contingency</code> for independence testing.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="23-35" data-tint="3">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Cramer's V and result</span>
    </div>
    <div class="code-callout__body">
      <p>Compute Cramer's V as a normalized effect size and bundle everything into a result dict with a plain-text explanation.</p>
    </div>
  </div>
</aside>
</div>

```
Chi-square: 0.00, P-value: 1.000. Effect size (Cramer's V): 0.00. No significant association at alpha=0.05.
```

### 4. Correlation Tests: Measuring Relationships

**When to use:**

- Assessing the strength and direction of the relationship between two continuous variables.

**Types:**

- **Pearson correlation:** Measures linear relationships (requires normality).
- **Spearman correlation:** Measures monotonic relationships (non-parametric).

**Assumptions:**

- Data are continuous (for Pearson).
- Observations are independent.
- Relationship is linear (for Pearson).

**Example:**

**Pearson and Spearman correlation with significance**

**Purpose:** Compare a parametric linear association (`pearsonr`) with a rank-based monotonic measure (`spearmanr`) on the same pairs, and interpret each against \\(\alpha\\).

**Walkthrough:** The `method` flag switches APIs; both return correlation and two-sided p-value; two calls illustrate that strength and significance can differ slightly by metric.

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight python %}
# Self-contained example: Correlation test (Pearson and Spearman)
from scipy import stats
import numpy as np

# Example data
x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([2, 4, 5, 4, 5, 7])

def perform_correlation(x, y, method='pearson', alpha=0.05):
    """Perform correlation test and explain the results."""
    if method == 'pearson':
        corr, p_value = stats.pearsonr(x, y)
        method_name = 'Pearson'
    elif method == 'spearman':
        corr, p_value = stats.spearmanr(x, y)
        method_name = 'Spearman'
    else:
        raise ValueError('method must be "pearson" or "spearman"')
    explanation = (
        f"{method_name} correlation: {corr:.2f}, P-value: {p_value:.3f}. "
        f"{'Significant correlation' if p_value < alpha else 'No significant correlation'} "
        f"at alpha={alpha}."
    )
    return {
        'correlation': corr,
        'p_value': p_value,
        'significant': p_value < alpha,
        'method': method_name,
        'explanation': explanation
    }

result = perform_correlation(x, y, method='pearson')
print(result['explanation'])
result = perform_correlation(x, y, method='spearman')
print(result['explanation'])
# Sample output:
# Pearson correlation: 0.89, P-value: 0.018. Significant correlation at alpha=0.05.
# Spearman correlation: 0.94, P-value: 0.005. Significant correlation at alpha=0.05.
{% endhighlight %}

</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-7" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Setup and data</span>
    </div>
    <div class="code-callout__body">
      <p>Import SciPy and NumPy, then define toy x and y arrays with a near-monotonic relationship to make both correlation tests clearly significant.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="9-30" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Unified correlation function</span>
    </div>
    <div class="code-callout__body">
      <p>Dispatch to <code>pearsonr</code> or <code>spearmanr</code> based on the <code>method</code> flag, build a plain-English explanation string, and return a structured result dict.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="32-38" data-tint="3">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Compare both metrics</span>
    </div>
    <div class="code-callout__body">
      <p>Call the function twice—once for Pearson, once for Spearman—and print the explanation strings side by side to show how the two measures can give slightly different results.</p>
    </div>
  </div>
</aside>
</div>

```
Pearson correlation: 0.88, P-value: 0.021. Significant correlation at alpha=0.05.
Spearman correlation: 0.85, P-value: 0.031. Significant correlation at alpha=0.05.
```

## Effect Size, Power, and Confidence Intervals

- **Effect Size:** Quantifies the magnitude of a difference or relationship. Large effect sizes are more likely to be practically significant.
- **Statistical Power:** The probability that a test will detect an effect if there is one. Higher power reduces the risk of false negatives. Plan your sample size to achieve adequate power (commonly 0.8 or higher).
- **Confidence Intervals:** Provide a range of plausible values for your estimate (e.g., mean difference, correlation). Narrow intervals indicate more precise estimates.

**Visuals:**

- ![Effect Sizes](assets/effect_sizes.png)
- ![Power Analysis](assets/power_analysis.png)
- ![Confidence Intervals](assets/confidence_intervals.png)

## Common Mistakes to Avoid

1. **Choosing the Wrong Test:** Match your test to your data type and research question.
2. **Ignoring Assumptions:** Always check if your data meet the test's assumptions (normality, equal variances, independence, etc.).
3. **Multiple Testing Without Correction:** Adjust for multiple comparisons to avoid inflated false positive rates.
4. **Overlooking Effect Size:** Statistical significance does not always mean practical importance.
5. **Insufficient Sample Size:** Underpowered studies may miss real effects.
6. **Misinterpreting P-values:** A small p-value does not prove a hypothesis; it just suggests the data are unlikely under the null.

## Best Practices

### Planning

- Define a clear research question and hypotheses.
- Choose the appropriate test before collecting data.
- Calculate required sample size (power analysis).
- Pre-register your analysis plan if possible.

### Execution

- Collect data carefully and consistently.
- Check data quality and handle missing values appropriately.
- Document all procedures and decisions.

### Analysis

- Use the correct statistical test for your data and question.
- Check and report test assumptions.
- Report effect sizes and confidence intervals, not just p-values.

### Reporting

- Clearly state your hypotheses and which tests you used.
- Include test statistics, p-values, effect sizes, and confidence intervals.
- Use visualizations to support your findings.
- Discuss limitations and practical significance.

## Gotchas

- **Using `ttest_ind` for paired data** — if the same subjects are measured twice (before/after, left/right eye), using the independent t-test ignores the within-subject correlation and inflates the p-value. Use `scipy.stats.ttest_rel` for paired designs; the lesson's `ttest_ind` example is only correct when observations in the two groups are genuinely independent.
- **Running ANOVA and concluding which groups differ** — `f_oneway` only tells you that *at least one* group mean is different; it does not say which pair. Following up with Tukey HSD or Bonferroni-corrected pairwise t-tests is required, and each extra comparison must be reported as part of the multiple-testing burden.
- **Chi-square test on cells with expected counts below 5** — `chi2_contingency` can return misleading p-values when the expected frequency in any cell is small (< 5). The test's asymptotic approximation breaks down; switch to Fisher's exact test (`scipy.stats.fisher_exact`) for 2×2 tables or aggregate sparse categories before proceeding.
- **Passing raw category *labels* instead of counts to `chisquare`** — `scipy.stats.chisquare(observed, expected)` expects numeric *frequency arrays*, not category names or raw rows. A common silent error is passing a list of strings or a 2D array when the function expects a 1D count vector.
- **Conflating Pearson r significance with Pearson r magnitude** — `pearsonr` returns a p-value that is strongly influenced by sample size; with n=1000 even r=0.05 will be "significant" at α=0.05. Always report the correlation coefficient alongside the p-value, and remember that r² (the coefficient of determination) is what tells you how much variance is explained.
- **Choosing Pearson when the relationship is monotonic but not linear** — if your scatter plot shows a clear but curved pattern, Pearson r will understate the association because it only captures linear relationships. Use Spearman's rank correlation (`spearmanr`) for monotonic relationships, or visualize first with a scatter plot before committing to a method.

## Next steps

- Continue to [A/B testing](./ab-testing.md), then [Results analysis](./results-analysis.md).

## Additional Resources

- [Statistical Tests Guide](https://www.statisticshowto.com/probability-and-statistics/statistical-tests/)
- [Effect Size Calculator](https://www.statstest.com/effect-size/)
- [Multiple Testing Correction](https://www.statstest.com/bonferroni/)
- Books:
  - "Statistics in Plain English" by Timothy C. Urdan
  - "Discovering Statistics Using Python" by Andy Field
- Software:
  - Python's scipy.stats
  - statsmodels
  - pingouin for advanced tests

---

Remember: Statistical tests are like tools in a toolbox—choose the right one for your data and question, and always interpret results in context!
