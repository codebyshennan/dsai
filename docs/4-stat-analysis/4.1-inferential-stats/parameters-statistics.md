# Parameters and Statistics: The Bridge to Understanding Populations

**After this lesson:** you can explain the core ideas in “Parameters and Statistics: The Bridge to Understanding Populations” and reproduce the examples here in your own notebook or environment.

## Overview

**Parameters** describe populations (usually unknown); **statistics** are computed from samples and estimate those parameters. This lesson pulls together notation, point and interval estimates, and properties of estimators—after you have already seen intervals, sampling behavior, and p-values in context.

## Helpful video

StatQuest introduction to confidence intervals.

<iframe width="560" height="315" src="https://www.youtube.com/embed/TqOeMYtOc1w" title="Confidence Intervals, Clearly Explained" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Why this matters

- You will separate **population parameters** (unknown, fixed) from **sample statistics** (computed from data) in every inference task.
- You will read notation (e.g. Greek vs Latin letters) the way textbooks and software reports use it.

## Prerequisites

- All earlier lessons in this submodule: [population vs sample](./population-sample.md), [sampling distributions](./sampling-distributions.md), [confidence intervals](./confidence-intervals.md), and [understanding p-values](./p-values.md).
- Optional: [Module 1.3 statistics](../../1-data-fundamentals/1.3-intro-statistics/README.md) for notation refresh.

> **Note:** This lesson consolidates vocabulary from earlier files in submodule 4.1; skim the headings if you are already comfortable with Greek vs Latin symbols.

## Introduction

Imagine you're a detective trying to understand the average height of all trees in the Amazon rainforest. It's impossible to measure every tree, but you can measure some trees and use that information to make educated guesses about all trees. This is where parameters and statistics come into play!

In statistical inference, we distinguish between parameters and statistics. Parameters are numerical characteristics of a population, while statistics are numerical characteristics of a sample. Understanding this distinction is crucial for making valid inferences about populations based on sample data.

{% include mermaid-diagram.html src="4-stat-analysis/4.1-inferential-stats/diagrams/parameters-statistics-1.mmd" %}

## Definitions

### Parameters

- Fixed, unknown values that describe a population
- Typically denoted by Greek letters (e.g., μ, σ, σ², ρ, π)
- Examples: population mean, population standard deviation, population proportion

### Statistics

- Calculated values from sample data
- Used to estimate population parameters
- Typically denoted by Latin letters (e.g., x̄, s, s², r, p)
- Examples: sample mean, sample standard deviation, sample proportion

### Estimator vs estimate vs statistic

These three words sound interchangeable but mean different things, and the distinction matters once you start reasoning about hypothesis tests and regression:

- **Estimator** — the *rule or formula* you apply to data. Example: "take the arithmetic mean of the sample." An estimator is a function; it has properties like bias and variance regardless of which dataset you feed it.
- **Estimate** — the *single number* the estimator produces on one specific dataset. Example: \\(\bar x = 99.86\\) feet for the sample of 100 trees below. Run the estimator on a different sample and you get a different estimate.
- **Statistic** — any quantity computed from sample data. Every estimate is a statistic, but "statistic" is also the broader umbrella that covers things you would never use as estimators (e.g., the sample minimum, or a test statistic like \\(t\\)).

When the lesson says "the sample mean is unbiased," the subject is the estimator (the rule), not any one estimate. A specific value like \\(\bar x = 99.86\\) is neither biased nor unbiased—it's just a number.

![Parameter-Statistic Relationship](assets/parameter_statistic_diagram.png)
*Figure 1: Visual representation of the relationship between population parameters and sample statistics. Parameters (Greek letters) describe the entire population, while statistics (Latin letters) are calculated from samples to estimate these parameters.*

## Point and Interval Estimates

### Point Estimates

- Single value estimates of population parameters
- Examples:
  - Sample mean (x̄) as an estimate of population mean (μ)
  - Sample proportion (p) as an estimate of population proportion (π)

### Interval Estimates

- Range of values that likely contains the population parameter
- Provides more information than point estimates
- Example: Confidence intervals

![Confidence Intervals](assets/confidence_interval_diagram.png)
*Figure 2: Visualization of confidence intervals. The red line represents our point estimate, while the blue shaded area shows the range where we're confident the true parameter lies.*

## Properties of Good Estimators

A good estimator should possess the following properties:

1. **Unbiasedness**
   - The expected value of the estimator equals the parameter being estimated
   - Example: Sample mean is an unbiased estimator of population mean

2. **Efficiency**
   - Among unbiased estimators, the one with the smallest variance is most efficient
   - Example: Sample mean is more efficient than sample median for normal distributions

3. **Consistency**
   - As sample size increases, the estimator converges to the parameter value
   - Example: Sample mean becomes more accurate as sample size increases

![Estimator Properties](assets/estimator_properties_diagram.png)
*Figure 3: Visual comparison of different estimator properties. The top panel shows unbiased vs biased estimators, the middle panel demonstrates efficiency, and the bottom panel illustrates consistency.*

## From Sample to Population: Making the Connection

### Point Estimates: Our Best Single Guess

A point estimate is like taking your best shot at the true value:

**Simulated forest: μ vs one \\(\bar x\\)**

**Purpose:** Ground notation—population mean vs sample mean—on a synthetic finite “forest” and a single draw of 100 trees.

**Walkthrough:** `population` is stand-in census; `choice` with replacement mimics IID sampling from a large population; prints report |μ̂ − μ| for one realization.

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight python %}
import numpy as np
np.random.seed(42)  # For reproducibility

# Simulate a population of tree heights (in feet)
population = np.random.normal(loc=100, scale=15, size=10000)
population_mean = np.mean(population)

# Take a sample and calculate point estimate
sample = np.random.choice(population, size=100)
sample_mean = np.mean(sample)

print(f"Tree Height Analysis")
print(f"Population mean (μ): {population_mean:.2f} feet")
print(f"Sample mean (x̄): {sample_mean:.2f} feet")
print(f"Difference: {abs(population_mean - sample_mean):.2f} feet")
{% endhighlight %}
```
Tree Height Analysis
Population mean (μ): 99.97 feet
Sample mean (x̄): 99.86 feet
Difference: 0.11 feet
```


</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-7" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Population setup</span>
    </div>
    <div class="code-callout__body">
      <p>Simulate 10,000 tree heights from N(100, 15²) to represent the population parameter μ—in practice this value would be unknown.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="9-15" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Point estimate</span>
    </div>
    <div class="code-callout__body">
      <p>Draw 100 heights from the population and compare the sample mean to μ to show how close a single statistic gets to the true parameter.</p>
    </div>
  </div>
</aside>
</div>

![Tree Height Analysis](assets/tree_height_analysis.png)
*Figure 4: Comparison of population and sample distributions for tree heights. The red dashed lines indicate the means, and the blue shaded area shows the 95% confidence interval.*

### Interval Estimates: Being Realistic About Uncertainty

Instead of a single guess, we provide a range where we believe the true value lies:

**t-interval continuing the same sample**

**Purpose:** Turn the previous lesson’s `sample` and `sample_mean` into a textbook t-based CI using sample SD and \\(n-1\\) degrees of freedom.

**Walkthrough:** `stats.t.ppf` at \\((1+0.95)/2\\) gives two-sided critical t; margin is \\(t_{df} \cdot s/\sqrt{n}\\); relies on `sample` still in memory from the prior cell.

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight python %}
from scipy import stats

# Calculate 95% confidence interval
confidence_level = 0.95
sample_std = np.std(sample, ddof=1)  # ddof=1 for sample standard deviation
sample_size = len(sample)

# Calculate margin of error
# (1 + confidence_level) / 2 = 0.975: two-sided, upper tail at α/2.
margin_of_error = stats.t.ppf((1 + confidence_level) / 2, sample_size - 1) * \
                 (sample_std / np.sqrt(sample_size))

ci_lower = sample_mean - margin_of_error
ci_upper = sample_mean + margin_of_error

print(f"\nConfidence Interval Analysis")
print(f"{confidence_level*100}% Confidence Interval:")
print(f"({ci_lower:.2f}, {ci_upper:.2f}) feet")
print(f"Interpretation: across repeated samples, {confidence_level*100}% of intervals")
print(f"built this way would capture the true mean; this one is ({ci_lower:.2f}, {ci_upper:.2f}) feet")
{% endhighlight %}
```

Confidence Interval Analysis
95.0% Confidence Interval:
(96.90, 102.82) feet
Interpretation: across repeated samples, 95.0% of intervals
built this way would capture the true mean; this one is (96.90, 102.82) feet
```


</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-7" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Margin of error</span>
    </div>
    <div class="code-callout__body">
      <p>Compute the t critical value for n−1 degrees of freedom and multiply by the standard error (s/√n) to get the margin of error for a 95% interval.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="9-19" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Interval bounds</span>
    </div>
    <div class="code-callout__body">
      <p>Subtract and add the margin of error from the sample mean to form the interval, then print a plain-language interpretation of what 95% confidence means.</p>
    </div>
  </div>
</aside>
</div>

## What Makes a Good Estimator?

### 1. Unbiasedness: Hitting the Target on Average

An unbiased estimator's expected value equals the population parameter:

**Monte Carlo average of \\(\bar x\\)**

**Purpose:** Show empirically that the mean of many sample means tracks \\(\mu\\)—the computational face of unbiasedness for the sample mean.

**Walkthrough:** Loop draws fresh n=100 samples with replacement; `mean_of_means` should hug `population_mean` from the earlier simulation block.

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight python %}
# Demonstrate unbiasedness of sample mean
n_simulations = 1000
sample_means = []

for _ in range(n_simulations):
    sample = np.random.choice(population, size=100)
    sample_means.append(np.mean(sample))

mean_of_means = np.mean(sample_means)

print(f"\nUnbiasedness Analysis")
print(f"True population mean: {population_mean:.2f}")
print(f"Average of {n_simulations} sample means: {mean_of_means:.2f}")
print(f"Difference: {abs(population_mean - mean_of_means):.2f}")
{% endhighlight %}
```

Unbiasedness Analysis
True population mean: 99.97
Average of 1000 sample means: 99.94
Difference: 0.03
```


</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-8" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Monte Carlo simulation</span>
    </div>
    <div class="code-callout__body">
      <p>Draw 1,000 independent samples of size 100 and record each mean to build an empirical picture of the sampling distribution.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="10-14" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Verify unbiasedness</span>
    </div>
    <div class="code-callout__body">
      <p>Compute the mean of 1,000 sample means and compare to μ—the tiny difference confirms the sample mean is an unbiased estimator.</p>
    </div>
  </div>
</aside>
</div>

![Unbiasedness Demonstration](assets/unbiasedness_demonstration.png)
*Figure 5: Distribution of sample means around the population mean. The green dashed line shows the mean of sample means, which is very close to the true population mean (red dashed line).*

### 2. Efficiency: Minimal Variance

An efficient estimator has less variability in its estimates:

**Mean vs 10% trimmed mean on the same draw**

**Purpose:** Illustrate two competing location estimators on identical data—under normality the plain mean is BLUE; trimming trades bias/variance when tails are heavy.

**Walkthrough:** `stats.trim_mean(data, 0.1)` drops the lowest/highest 10% before averaging; compare numeric closeness for teaching, not a formal efficiency calculation.

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight python %}
def compare_estimators(data):
    """Compare mean estimators"""
    # Regular mean
    mean1 = np.mean(data)
    # Trimmed mean (less efficient for normal data)
    mean2 = stats.trim_mean(data, 0.1)

    return mean1, mean2

# Compare estimators
regular_mean, trimmed_mean = compare_estimators(sample)
print(f"\nEfficiency Analysis")
print(f"Regular mean: {regular_mean:.2f}")
print(f"Trimmed mean: {trimmed_mean:.2f}")
{% endhighlight %}
```

Efficiency Analysis
Regular mean: 99.80
Trimmed mean: 99.71
```


</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-8" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Two estimators</span>
    </div>
    <div class="code-callout__body">
      <p>Compute the plain mean and a 10%-trimmed mean on the same data—the trimmed version drops the extreme 10% from each tail before averaging.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="10-14" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Efficiency comparison</span>
    </div>
    <div class="code-callout__body">
      <p>Print both estimates side by side; for normal data the plain mean is more efficient (lower variance), while the trimmed mean becomes competitive with heavy tails.</p>
    </div>
  </div>
</aside>
</div>

![Efficiency Comparison](assets/efficiency_comparison.png)
*Figure 6: Comparison of regular mean (red) and trimmed mean (green) estimators. The regular mean is more efficient for normally distributed data.*

### 3. Consistency: Getting Better with More Data

A consistent estimator converges to the true value as sample size increases:

**One \\(\bar x\\) per n on a ladder of sizes**

**Purpose:** Print how |x̄ − μ| shrinks as `size` grows—visual consistency narrative without a formal limit proof.

**Walkthrough:** Same `population` array as before; independent draws per row—differences step down on average as n increases.

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight python %}
# Demonstrate consistency with increasing sample sizes
sample_sizes = [10, 100, 1000, 5000]
results = []

for size in sample_sizes:
    sample = np.random.choice(population, size=size)
    sample_mean = np.mean(sample)
    results.append(sample_mean)

print(f"\nConsistency Analysis")
print(f"True population mean: {population_mean:.2f}")
for size, result in zip(sample_sizes, results):
    print(f"Sample size {size:4d}: {result:.2f} (Diff: {abs(result - population_mean):.2f})")
{% endhighlight %}
```

Consistency Analysis
True population mean: 99.97
Sample size   10: 105.13 (Diff: 5.17)
Sample size  100: 101.35 (Diff: 1.38)
Sample size 1000: 100.18 (Diff: 0.21)
Sample size 5000: 99.81 (Diff: 0.16)
```


</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-8" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Size ladder</span>
    </div>
    <div class="code-callout__body">
      <p>Draw one independent sample at each of four sizes (10, 100, 1000, 5000) and record the resulting sample mean.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="10-13" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Convergence printout</span>
    </div>
    <div class="code-callout__body">
      <p>Print the absolute difference between each sample mean and μ—it should generally shrink as n grows, illustrating consistency numerically.</p>
    </div>
  </div>
</aside>
</div>

![Consistency Demonstration](assets/consistency_demonstration.png)
*Figure 7: Demonstration of consistency. As sample size increases, the sample mean (blue line) converges to the true population mean (red dashed line).*

## Real-World Applications

### 1. Quality Control in Manufacturing

**One-shot manufacturing sample → t CI**

**Purpose:** Package sample mean, sample SD, and `stats.t.interval` into a dict return—pattern matches how you’d log QC telemetry in code.

**Walkthrough:** Gaussian sample around target 100; `stats.sem` implicit inside `t.interval` via `scale` argument; function body stays side-effect free.

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight python %}
import numpy as np
from scipy import stats

def quality_control_example():
    # Simulate production measurements
    population_mean = 100  # Target value
    population_std = 2
    sample_size = 30

    # Generate sample
    sample = np.random.normal(population_mean, population_std, sample_size)

    # Calculate statistics
    sample_mean = np.mean(sample)
    sample_std = np.std(sample, ddof=1)

    # Calculate 95% confidence interval
    ci = stats.t.interval(0.95, len(sample)-1,
                         loc=sample_mean,
                         scale=stats.sem(sample))

    return {
        'sample_mean': sample_mean,
        'sample_std': sample_std,
        'confidence_interval': ci
    }
{% endhighlight %}

<figure>
<img src="assets/parameters-statistics_fig_1.png" alt="parameters-statistics" />
<figcaption>Figure 1: Generated visualization</figcaption>
</figure>


</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="4-11" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">QC sample</span>
    </div>
    <div class="code-callout__body">
      <p>Draw 30 production measurements from N(100, 2²) simulating a manufacturing process with a known target value.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="13-22" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">t-interval</span>
    </div>
    <div class="code-callout__body">
      <p>Use <code>stats.t.interval</code> with <code>stats.sem</code> as the scale parameter to produce a 95% CI—a one-line alternative to the manual ppf × SE formula.</p>
    </div>
  </div>
</aside>
</div>

![Quality Control Analysis](assets/quality_control_analysis.png)
*Figure 8: Quality control measurements with target value (red), sample mean (green), and 95% confidence interval (blue).*

### 2. A/B Testing in Tech

**Bernoulli arms and normal-approx CI on \\(\hat p_T - \hat p_C\\)**

**Purpose:** Estimate lift between two conversion rates and attach an asymptotic CI—common quick-and-dirty reporting path (check assumptions in production).

**Walkthrough:** Independent Bernoulli vectors; `diff_std` uses separate-factor SE formula; `stats.norm.interval` treats the difference as normal—OK for large n.

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight python %}
def ab_testing_example():
    # Simulate conversion rates
    control_rate = 0.1
    treatment_rate = 0.12
    sample_size = 1000

    # Generate samples
    control = np.random.binomial(1, control_rate, sample_size)
    treatment = np.random.binomial(1, treatment_rate, sample_size)

    # Calculate statistics
    control_mean = np.mean(control)
    treatment_mean = np.mean(treatment)

    # Calculate difference and confidence interval
    diff = treatment_mean - control_mean
    diff_std = np.sqrt(control_mean*(1-control_mean)/sample_size +
                      treatment_mean*(1-treatment_mean)/sample_size)
    ci = stats.norm.interval(0.95, loc=diff, scale=diff_std)

    return {
        'control_rate': control_mean,
        'treatment_rate': treatment_mean,
        'difference': diff,
        'confidence_interval': ci
    }
{% endhighlight %}

<figure>
<img src="assets/parameters-statistics_fig_1.png" alt="parameters-statistics" />
<figcaption>Figure 1: Generated visualization</figcaption>
</figure>


</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-11" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Bernoulli arms</span>
    </div>
    <div class="code-callout__body">
      <p>Simulate binary conversion events for 1,000 users in each arm using Bernoulli draws at 10% and 12% rates.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="13-21" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Lift and CI</span>
    </div>
    <div class="code-callout__body">
      <p>Compute the difference in observed rates, build a normal-approx SE for the difference, and use <code>stats.norm.interval</code> to produce a 95% CI for the lift.</p>
    </div>
  </div>
</aside>
</div>

![A/B Testing Results](assets/ab_testing_results.png)
*Figure 9: A/B test results showing conversion rates for control and treatment groups with error bars.*

## Practice Questions

1. A company measures the battery life of 100 phones and finds a mean of 12 hours. Is this a parameter or a statistic? Why?
2. How would increasing sample size affect the width of a confidence interval? Explain using the margin of error formula.
3. Design a sampling strategy for estimating the average time users spend on a social media app. What statistics would you use?
4. If you had to choose between an unbiased estimator with high variance and a slightly biased estimator with low variance, which would you pick? Why?
5. How could you use bootstrapping to assess the reliability of your sample statistics?

## Key Takeaways

1. Parameters describe populations, statistics describe samples
2. Sample statistics help us estimate unknown population parameters
3. Larger samples generally provide more precise estimates
4. Good estimators are unbiased, efficient, and consistent
5. Confidence intervals provide a range of plausible values for population parameters
6. Real-world applications include quality control, A/B testing, and market research

## Gotchas

- **Swapping Greek and Latin notation in code comments** — writing `mu` when you mean `x_bar` (or vice versa) is not just cosmetic; it signals a conceptual confusion between the unknown population parameter and the computed sample statistic. Parameters are fixed but unknown; statistics are noisy estimates that change with every new sample.
- **Using `np.std(data)` to compute the sample SD for a confidence interval** — NumPy's default is `ddof=0` (population formula), which underestimates the variance for samples. Use `np.std(data, ddof=1)` or `scipy.stats.sem(data)` wherever you need the sample standard deviation.
- **Believing a biased estimator is always worse** — a biased estimator with lower variance can produce estimates closer to the truth (lower MSE) than an unbiased one with high variance. The lesson's trimmed mean example illustrates this: trimming biases the mean slightly but reduces variance when outliers are present.
- **Forgetting that consistency is a large-sample property** — a consistent estimator is not guaranteed to be close to the parameter for small n; it only converges as n → ∞. Drawing a single sample of size 10 and observing that x̄ ≈ μ does not demonstrate consistency.
- **Ignoring the finite population correction factor** — when you sample more than about 5–10% of a finite population *without* replacement, the standard error formula `σ/√n` overstates variability. Apply the FPC multiplier `√((N−n)/(N−1))` to get an accurate SE.
- **Treating x̄ as the population mean** — software often prints the sample mean prominently; it is easy to start writing "the average is 12.3" when the correct statement is "the sample estimate of the average is 12.3, with uncertainty." This distinction matters every time you communicate results.

## Additional Resources

- [Interactive Sampling Distribution Simulator](https://seeing-theory.brown.edu/sampling-distributions/index.html)
- [Confidence Interval Calculator](https://www.mathsisfun.com/data/confidence-interval-calculator.html)
- [Statistical Estimation Tutorial](https://www.khanacademy.org/math/statistics-probability/sampling-distributions-library)

Remember: The journey from sample to population is like building a bridge. The better your sampling and estimation, the more reliable your inference.

## Next steps

- Start [Hypothesis testing (module 4.2)](../4.2-hypotheses-testing/README.md) with [Experimental design](../4.2-hypotheses-testing/experimental-design.md).

## Common Questions and Answers

### Q: Why can't we just measure the entire population?

A: Measuring entire populations is often impractical due to:

- Cost constraints
- Time limitations
- Physical impossibility
- Destructive testing requirements

### Q: How do we know if our sample is representative?

A: We ensure representativeness through:

- Random sampling
- Adequate sample size
- Checking for sampling bias
- Stratification when necessary

### Q: What's the difference between standard deviation and standard error?

A:

- Standard deviation: Measures variability in the population
- Standard error: Measures variability of the sample mean

## Practice Problems

1. A sample of 50 students has an average height of 170cm with a standard deviation of 10cm. Calculate a 95% confidence interval for the population mean height.

2. In a survey of 200 customers, 120 reported satisfaction with a product. Calculate a 90% confidence interval for the population proportion of satisfied customers.

3. Two samples of 30 each show means of 100 and 105 with standard deviations of 5. Test if the difference is statistically significant.

## Additional Resources

1. [Statistical Inference Course](https://www.coursera.org/learn/statistical-inference)
2. [Introduction to Statistical Learning](https://www.statlearning.com/)
3. [OpenIntro Statistics](https://www.openintro.org/book/os/)

## Sampling Distributions: The Foundation of Inference

### What is a Sampling Distribution?

A sampling distribution is the distribution of a statistic (like the mean) across all possible samples of a given size from a population. It's crucial because it tells us how our sample statistics would vary if we were to take many samples.

**Empirical sampling distribution with seaborn KDE**

**Purpose:** Histogram/KDE of many x̄ values with a vertical line at μ—needs `matplotlib`/`seaborn` imported in the notebook environment running this snippet.

**Walkthrough:** Double loop unnecessary—inner draws `sample_size` with replacement; returns dict comparing population mean to mean/SD of simulated x̄’s.

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight python %}
def demonstrate_sampling_distribution():
    # Generate population data
    np.random.seed(42)
    population = np.random.normal(100, 15, 10000)

    # Take multiple samples and calculate means
    n_samples = 1000
    sample_size = 30
    sample_means = []

    for _ in range(n_samples):
        sample = np.random.choice(population, sample_size)
        sample_means.append(np.mean(sample))

    # Plot sampling distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(sample_means, kde=True)
    plt.axvline(np.mean(population), color='red', linestyle='--',
                label='Population Mean')
    plt.title('Sampling Distribution of the Mean')
    plt.xlabel('Sample Mean')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()

    return {
        'population_mean': np.mean(population),
        'sampling_dist_mean': np.mean(sample_means),
        'sampling_dist_std': np.std(sample_means)
    }
{% endhighlight %}

<figure>
<img src="assets/parameters-statistics_fig_1.png" alt="parameters-statistics" />
<figcaption>Figure 1: Generated visualization</figcaption>
</figure>


</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="2-3" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Population setup</span>
    </div>
    <div class="code-callout__body">
      <p>Generate a synthetic normal population of 10,000 values as the reference distribution for repeated sampling.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="5-13" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Collect sample means</span>
    </div>
    <div class="code-callout__body">
      <p>Draw 1,000 samples of size 30 with replacement and store each mean to build the empirical sampling distribution.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="15-24" data-tint="3">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">KDE histogram</span>
    </div>
    <div class="code-callout__body">
      <p>Plot the sampling distribution with a seaborn KDE overlay and mark the true population mean as a reference line.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="26-30" data-tint="4">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Summary statistics</span>
    </div>
    <div class="code-callout__body">
      <p>Return population mean alongside the mean and SD of simulated sample means for easy comparison in a notebook.</p>
    </div>
  </div>
</aside>
</div>

### Central Limit Theorem

The Central Limit Theorem (CLT) states that:

- For large enough sample sizes, the sampling distribution of the mean will be approximately normal
- The mean of the sampling distribution equals the population mean
- The standard deviation of the sampling distribution (standard error) equals σ/√n

**Skewed population: CLT at three n values**

**Purpose:** Side-by-side KDE/histograms of x̄ for small, medium, and large n from an exponential population—normality emerges for the *mean*, not the raw data.

**Walkthrough:** Exponential draws; nested loops fill `sample_means` per panel; axis titles show n.

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight python %}
def demonstrate_clt():
    # Generate non-normal population
    np.random.seed(42)
    population = np.random.exponential(scale=2, size=10000)

    # Different sample sizes
    sample_sizes = [5, 30, 100]
    n_samples = 1000

    # Plot sampling distributions
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    for i, size in enumerate(sample_sizes):
        sample_means = []
        for _ in range(n_samples):
            sample = np.random.choice(population, size)
            sample_means.append(np.mean(sample))

        sns.histplot(sample_means, kde=True, ax=axes[i])
        axes[i].set_title(f'n = {size}')
        axes[i].set_xlabel('Sample Mean')

    plt.tight_layout()
    plt.show()
{% endhighlight %}

<figure>
<img src="assets/parameters-statistics_fig_1.png" alt="parameters-statistics" />
<figcaption>Figure 1: Generated visualization</figcaption>
</figure>


</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="2-3" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Skewed population</span>
    </div>
    <div class="code-callout__body">
      <p>Use an exponential distribution as the population to show CLT working on a non-normal base.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="5-7" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Sample size ladder</span>
    </div>
    <div class="code-callout__body">
      <p>Try three sample sizes (5, 30, 100) to visualise how normality of the sampling distribution emerges as n grows.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="9-22" data-tint="3">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Three-panel KDE</span>
    </div>
    <div class="code-callout__body">
      <p>Collect 1,000 means per size and plot each distribution in its own axis; the rightmost panel should appear most bell-shaped.</p>
    </div>
  </div>
</aside>
</div>

### Standard Error

The standard error (SE) measures the precision of our sample statistic:

**Manual SEM and t-interval**

**Purpose:** Show SE as `s/√n` with `ddof=1`, then feed that scalar into `stats.t.interval` as the scale—mirrors the hand formula for μ.

**Walkthrough:** Single random normal sample; return dict bundles point estimate, SE, and CI tuple.

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight python %}
def calculate_standard_error():
    # Example data
    sample = np.random.normal(100, 15, 30)

    # Calculate standard error of the mean
    se = np.std(sample, ddof=1) / np.sqrt(len(sample))

    # Calculate 95% confidence interval
    ci = stats.t.interval(0.95, len(sample)-1,
                         loc=np.mean(sample),
                         scale=se)

    return {
        'sample_mean': np.mean(sample),
        'standard_error': se,
        'confidence_interval': ci
    }
{% endhighlight %}

</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-6" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">SE formula</span>
    </div>
    <div class="code-callout__body">
      <p>Compute the standard error as s/√n using <code>ddof=1</code> for the unbiased sample standard deviation—this is the precision measure for the sample mean.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="8-16" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">t-interval output</span>
    </div>
    <div class="code-callout__body">
      <p>Feed the SE into <code>stats.t.interval</code> as the scale parameter and bundle mean, SE, and CI into a single return dict for easy inspection.</p>
    </div>
  </div>
</aside>
</div>

### Practical Implications

1. **Sample Size Determination**
   - Larger samples lead to smaller standard errors
   - The relationship is not linear (√n in denominator)

2. **Confidence Intervals**
   - Standard error is crucial for calculating confidence intervals
   - Smaller SE leads to narrower intervals

3. **Hypothesis Testing**
   - Sampling distributions form the basis of hypothesis tests
   - They help determine the probability of observing our sample statistic

## Common Misconceptions

1. **Sample Size vs. Population Size**
   - The precision of estimates depends on sample size, not population size
   - A sample of 1000 is equally precise whether the population is 10,000 or 10 million

2. **Normal Distribution Assumption**
   - CLT applies to the sampling distribution, not necessarily the population
   - Even with non-normal populations, sample means tend to be normal

3. **Standard Error vs. Standard Deviation**
   - Standard deviation describes variability in the population
   - Standard error describes variability in the sample statistic

## Advanced Topics

### Bootstrapping

A resampling technique to estimate sampling distributions:

**Nonparametric bootstrap CI for the mean**

**Purpose:** Resample rows with replacement to build an empirical distribution of x̄ and take percentile bounds—distribution-free alternative when parametric assumptions hesitate.

**Walkthrough:** Inner loop draws `len(sample)` picks with replacement; `np.percentile` on bootstrap means gives equal-tail 95% interval.

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight python %}
def bootstrap_example():
    # Original sample
    sample = np.random.normal(100, 15, 30)

    # Bootstrap
    n_bootstrap = 1000
    bootstrap_means = []

    for _ in range(n_bootstrap):
        bootstrap_sample = np.random.choice(sample, len(sample), replace=True)
        bootstrap_means.append(np.mean(bootstrap_sample))

    # Calculate bootstrap confidence interval
    ci = np.percentile(bootstrap_means, [2.5, 97.5])

    return {
        'original_mean': np.mean(sample),
        'bootstrap_mean': np.mean(bootstrap_means),
        'bootstrap_ci': ci
    }
{% endhighlight %}

</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-11" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Bootstrap loop</span>
    </div>
    <div class="code-callout__body">
      <p>Draw 1,000 resamples with replacement from the original 30-item sample, each the same size as the original, and record the mean of each resample.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="13-19" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Percentile CI</span>
    </div>
    <div class="code-callout__body">
      <p>Take the 2.5th and 97.5th percentiles of the bootstrap means to form a distribution-free 95% CI that requires no normality assumption.</p>
    </div>
  </div>
</aside>
</div>

### Finite Population Correction

When sampling without replacement from a finite population:

**Finite population correction factor**

**Purpose:** Show the √(N−n)/(N−1) multiplier that shrinks variance when sampling without replacement from small frames—often omitted in “infinite population” approximations.

**Walkthrough:** Pure scalar math; multiply estimated SE by `fpc` when applying formulas that assumed WR sampling.

```python
def finite_population_correction():
    population_size = 1000
    sample_size = 100
    
    # Calculate correction factor
    fpc = np.sqrt((population_size - sample_size) / (population_size - 1))
    
    return fpc
```


<figure>
<img src="assets/parameters-statistics_fig_1.png" alt="parameters-statistics" />
<figcaption>Figure 1: Generated visualization</figcaption>
</figure>
