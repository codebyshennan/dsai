# Hypothesis Formulation: Asking the Right Scientific Questions

**After this lesson:** you can explain the core ideas in “Hypothesis Formulation: Asking the Right Scientific Questions” and reproduce the examples here in your own notebook or environment.

## Overview

A hypothesis ties a **decision** to a **testable claim**: what would the world look like if nothing interesting were happening (null), and what pattern would convince you otherwise (alternative)? Clear wording prevents “significant” results that no one can act on. This lesson follows [experimental design](./experimental-design.md) and feeds directly into [statistical tests](./statistical-tests.md).

## Why this matters

- Clear **null** and **alternative** hypotheses keep your analysis aligned with the decision you need to make.
- You will avoid vague claims that cannot be tested with data.

## Prerequisites

- [Experimental design](./experimental-design.md).
- [Understanding p-values](../4.1-inferential-stats/p-values.md) for null/alternative language.

> **Warning:** Do not choose your hypotheses after peeking at the data.

## 1. Introduction

A hypothesis is your scientific roadmap—it guides your investigation and helps you reach meaningful conclusions. Whether you're testing a new drug, optimizing a website, or studying customer behavior, well-formulated hypotheses are essential for discovery and sound decision-making.

### Video Tutorial: Hypothesis Testing Explained

<div class="video-embed">
<iframe width="560" height="315" src="https://www.youtube.com/embed/0oc49DyA3hU" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

*StatQuest: Hypothesis Testing and The Null Hypothesis, Clearly Explained!!! by Josh Starmer*

<div class="video-embed">
<iframe width="560" height="315" src="https://www.youtube.com/embed/5koKb5B_YWo" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

*StatQuest: Alternative Hypotheses: Main Ideas!!! by Josh Starmer*

## 2. The Anatomy of a Hypothesis

### Null Hypothesis (H₀)

- The default position: no effect, no difference, or no relationship.
- Example: "There is no difference in recovery time between the new and old treatments."
- Mathematical form:

\[
H_0: \mu_1 = \mu_2
\]

### Alternative Hypothesis (H₁ or Hₐ)

- What you hope to support: there is an effect, difference, or relationship.
- Example: "The new treatment reduces recovery time compared to the old treatment."
- Mathematical form:

\[
H_1: \mu_1 \neq \mu_2
\]

![Null vs Alternative Distribution](assets/null_vs_alternative.png)

## 3. The Three Pillars of Good Hypotheses

### 1. Specific and Clear

A good hypothesis is precise and unambiguous.

**Bad:** "The treatment might work better."

**Good:** "The new treatment reduces recovery time by at least 2 days."

**One-sided test for a minimum improvement**

**Purpose:** Encode a *directional* hypothesis (“at least 2 days better”) as a one-sample-style contrast against `min_improvement` using a pooled SE, so the p-value reads off the right tail only.

**Walkthrough:** Effect is `mean(control) - mean(treatment)`; `pooled_std` and `se` build a two-sample t standard error; `stats.t.cdf` with `1 -` gives a one-tailed p-value vs `min_improvement`.

```python
def test_specific_hypothesis(control_data, treatment_data, min_improvement=2):
    """
    H₀: treatment_effect ≤ min_improvement
    H₁: treatment_effect > min_improvement
    """
    effect = np.mean(control_data) - np.mean(treatment_data)
    n1, n2 = len(control_data), len(treatment_data)
    pooled_std = np.sqrt(((n1-1)*np.var(control_data) + (n2-1)*np.var(treatment_data)) / (n1+n2-2))
    se = pooled_std * np.sqrt(1/n1 + 1/n2)
    t_stat = (effect - min_improvement) / se
    p_value = 1 - stats.t.cdf(t_stat, df=n1+n2-2)
    return {'effect_size': effect, 't_statistic': t_stat, 'p_value': p_value, 'significant': p_value < 0.05}

# Example usage:
import numpy as np
from scipy import stats
control = np.array([12, 11, 13, 12, 14])
treatment = np.array([9, 10, 8, 9, 10])
result = test_specific_hypothesis(control, treatment, min_improvement=2)
print(result)
# Sample output:
# {'effect_size': 3.0, 't_statistic': 2.683, 'p_value': 0.012, 'significant': True}
```

**Captured output (example):** Numeric types may print as `np.float64`; check `significant` and that `effect_size` exceeds your stated minimum.

```
{'effect_size': np.float64(3.200000000000001), 't_statistic': np.float64(2.121320343559645), 'p_value': np.float64(0.03334399999999982), 'significant': np.True_}
```

### 2. Measurable

Your hypothesis should involve quantifiable variables.

**Descriptive metrics + one-sample t-test vs a target**

**Purpose:** Tie a verbal hypothesis (“satisfaction above 4”) to concrete summaries (mean, median, proportion ≥ 4) and a `ttest_1samp` against the benchmark.

**Walkthrough:** `metrics` dict holds everything you might report in a dashboard; `ttest_1samp(ratings, target_score)` tests the mean against the reference value (two-sided by default).

```python
def measure_customer_satisfaction(ratings, target_score=4.0):
    """
    H₀: Mean satisfaction ≤ target_score
    H₁: Mean satisfaction > target_score
    """
    metrics = {
        'mean_score': np.mean(ratings),
        'median_score': np.median(ratings),
        'std_dev': np.std(ratings),
        'satisfaction_rate': np.mean(ratings >= 4),
        'sample_size': len(ratings)
    }
    t_stat, p_value = stats.ttest_1samp(ratings, target_score)
    # Visualization (example)
    # plt.figure(figsize=(10, 5))
    # ... (visualization code omitted for brevity)
    return {**metrics, 't_statistic': t_stat, 'p_value': p_value}

# Example usage:
import numpy as np
from scipy import stats
ratings = np.array([5, 4, 4, 3, 5, 4, 3, 4, 5, 4])
result = measure_customer_satisfaction(ratings, target_score=4.0)
print(result)
# Sample output:
# {'mean_score': 4.2, 'median_score': 4.0, 'std_dev': 0.748, 'satisfaction_rate': 0.8, 'sample_size': 10, 't_statistic': 0.845, 'p_value': 0.420}
```

**Captured output (example):** With a mean only slightly above 4, the two-sided p-value may be large—failing to reject does *not* prove the mean equals the target.

```
{'mean_score': np.float64(4.1), 'median_score': np.float64(4.0), 'std_dev': np.float64(0.7000000000000001), 'satisfaction_rate': np.float64(0.8), 'sample_size': 10, 't_statistic': np.float64(0.42857142857142705), 'p_value': np.float64(0.6783097418055807)}
```

### 3. Falsifiable

A hypothesis must be testable and possible to prove wrong.

**Falsifiable vs vague statements**

**Purpose:** Contrast a rule that returns a Boolean from data (`test_mean_effect`) with a placeholder that cannot yield a test statistic—emphasizing why “falsifiable” matters operationally.

**Walkthrough:** `test_mean_effect` uses `ttest_1samp` and an arbitrary threshold; `vague_statement` deliberately avoids quantitative rejection rules.

```python
def demonstrate_falsifiability():
    """
    Show the importance of falsifiable hypotheses
    """
    def test_mean_effect(data, threshold):
        """H₀: mean ≤ threshold"""
        t_stat, p_value = stats.ttest_1samp(data, threshold)
        return p_value < 0.05
    def vague_statement(data):
        return "Statement too vague to test statistically"
    np.random.seed(42)
    data = np.random.normal(loc=10, scale=2, size=100)
    return {
        'falsifiable_result': test_mean_effect(data, 9.5),
        'non_falsifiable': vague_statement(data)
    }

# Example usage:
import numpy as np
from scipy import stats
result = demonstrate_falsifiability()
print(result)
# Sample output:
# {'falsifiable_result': True, 'non_falsifiable': 'Statement too vague to test statistically'}
```

**Captured output (example):** With these draws, the one-sided “mean > 9.5” check may or may not fire; the vague branch always returns the same string.

```
{'falsifiable_result': np.False_, 'non_falsifiable': 'Statement too vague to test statistically'}
```

## 4. Types of Hypotheses

### Simple vs. Composite

- **Simple:** Tests an exact value (e.g., H₀: μ = 100)
- **Composite:** Tests a range (e.g., H₀: 95 ≤ μ ≤ 105)

**Simple null vs composite range check**

**Purpose:** Show one workflow that tests \(H_0: \mu = 100\) with `ttest_1samp`, and a separate *interval* check that implements “is the sample mean inside [95, 105]?” as a descriptive composite screen.

**Walkthrough:** `simple_test.pvalue` comes from SciPy’s two-sided t-test vs 100; `composite_result` is a plain Python range check on \(\bar x\), not a formal LRT.

```python
def demonstrate_hypothesis_types(data):
    simple_test = stats.ttest_1samp(data, 100)
    mean = np.mean(data)
    composite_result = 95 <= mean <= 105
    return {'simple_p_value': simple_test.pvalue, 'composite_result': composite_result}

# Example usage:
import numpy as np
from scipy import stats
data = np.array([98, 102, 100, 97, 103])
result = demonstrate_hypothesis_types(data)
print(result)
# Sample output:
# {'simple_p_value': 0.682, 'composite_result': True}
```

**Captured output (example):** A p-value of 1.0 for the toy data means the sample mean equals the tested null exactly in this construction; interpret composite flags separately from the p-value.

```
{'simple_p_value': np.float64(1.0), 'composite_result': np.True_}
```

### Directional vs. Non-directional

- **Directional (one-tailed):** Specifies the direction of effect (e.g., H₁: μ₁ > μ₂)
- **Non-directional (two-tailed):** Only specifies there is an effect (e.g., H₁: μ₁ ≠ μ₂)

**Visual:**
![Hypothesis Testing Flowchart](assets/hypothesis_testing_flowchart.png)

## 5. Effect Size, Power, and Confidence Intervals

- **Effect Size:** Shows the magnitude of the difference or relationship. Important for practical significance.
- **Statistical Power:** The probability your test will detect a true effect. Plan your sample size accordingly.
- **Confidence Intervals:** Indicate the precision of your estimate.

**Visuals:**

- ![Effect Sizes](assets/effect_sizes.png)
- ![Power Analysis](assets/power_analysis.png)
- ![Confidence Intervals](assets/confidence_intervals.png)

## 6. Common Mistakes to Avoid

1. **Vague or ambiguous statements**
2. **Untestable (non-falsifiable) claims**
3. **Multiple hypotheses without correction**
4. **Ignoring practical significance**
5. **Confirmation bias**
6. **Ignoring test assumptions**
7. **Formulating hypotheses after seeing the data**

## 7. Best Practices

### Formulation

- Start with a clear research question
- Write both null and alternative hypotheses
- Ensure measurability and falsifiability
- Consider practical significance

### Testing

- Choose appropriate statistical tests
- Calculate required sample size
- Plan for multiple testing and corrections
- Document assumptions

### Interpretation

- Consider both statistical and practical significance
- Report effect sizes and confidence intervals
- Be cautious about causation

### Documentation

- Pre-register hypotheses
- Document any changes
- Report all tests conducted
- Share data and code

## Next steps

- Continue to [Statistical tests](./statistical-tests.md), then [A/B testing](./ab-testing.md) and [Results analysis](./results-analysis.md).

## 8. Additional Resources

- [Statistical Hypothesis Testing Guide](https://www.statisticshowto.com/probability-and-statistics/hypothesis-testing/)
- [Multiple Testing Calculator](https://www.statstest.com/bonferroni/)
- [P-value Misconceptions](https://www.nature.com/articles/nmeth.3288)
- Books:
  - "The Art of Scientific Investigation" by W.I.B. Beveridge
  - "Research Design" by John W. Creswell
- Software:
  - Python's statsmodels
  - R's hypothesis tests
  - G*Power for power analysis

---

Remember: A well-formulated hypothesis is half the battle won!
