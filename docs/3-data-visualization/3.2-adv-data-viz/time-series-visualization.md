# Time Series Visualization

**After this lesson:** you can prepare and plot time-based data clearly, choose suitable time intervals, and annotate trends, seasonality, and events without misleading the viewer.

> **Note:** Time series charts are common in analytics work, but easy to misuse. Build on [Matplotlib basics](../3.1-intro-data-viz/matplotlib-basics.md), then apply the richer styling and interactivity from [Seaborn guide](seaborn-guide.md) and [Plotly guide](plotly-guide.md).

## Helpful video

Context for plotting libraries and communication goals in advanced viz.

<iframe width="560" height="315" src="https://www.youtube.com/embed/RBSUwFGa6Fk" title="What is Data Science?" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Why time series needs its own lesson

Time adds structure that category charts do not have:

- order matters
- gaps matter
- aggregation choices matter
- seasonality can hide or exaggerate trends

A poor time chart can create fake spikes, hide missing periods, or compare partial months against full ones.

## Start with clean dates

**Purpose:** Convert string dates into real datetimes, sort them, and derive useful periods like week or month.

**Walkthrough:** `to_datetime` enables resampling, rolling averages, and time-based grouping.

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

traffic = pd.read_csv("traffic.csv")
traffic["date"] = pd.to_datetime(traffic["date"])
traffic = traffic.sort_values("date")
```

## Choose the right time grain

Your chart should match the decision being made.

- **Hourly or daily:** operational monitoring
- **Weekly:** smoother trend tracking
- **Monthly or quarterly:** business reporting

```python
weekly = (
    traffic
    .set_index("date")
    .resample("W")
    .agg(visits=("visits", "sum"))
    .reset_index()
)
```

If you compare time periods, make sure they are comparable:

- do not compare a partial current month to complete prior months
- use the same timezone where relevant
- explain missing periods instead of silently filling them

## Basic time series patterns

### 1. Trend line

**Purpose:** Show how a metric changes over time.

**Walkthrough:** Keep the line simple, label axes clearly, and avoid too many overlapping series.

```python
fig, ax = plt.subplots(figsize=(11, 5))
ax.plot(weekly["date"], weekly["visits"], color="#2b8cbe", linewidth=2)
ax.set_title("Weekly Website Visits")
ax.set_xlabel("Week")
ax.set_ylabel("Visits")
ax.grid(True, alpha=0.3)
```

### 2. Rolling average

**Purpose:** Reduce short-term noise so the longer-term pattern is easier to see.

**Walkthrough:** A rolling mean smooths local fluctuations but should not replace the original series entirely when the raw variation matters.

```python
weekly["rolling_4w"] = weekly["visits"].rolling(window=4, min_periods=1).mean()

fig, ax = plt.subplots(figsize=(11, 5))
ax.plot(weekly["date"], weekly["visits"], color="#9ecae1", linewidth=1.5, label="Weekly visits")
ax.plot(weekly["date"], weekly["rolling_4w"], color="#08519c", linewidth=2.5, label="4-week rolling average")
ax.legend()
```

### 3. Multiple series

Use multiple lines only when the comparison is manageable. If there are too many categories, use small multiples instead.

```python
sns.lineplot(
    data=channel_weekly,
    x="date",
    y="visits",
    hue="channel"
)
```

## Small multiples for clarity

**Purpose:** Compare several time series without stacking too many lines on one axes.

**Walkthrough:** `relplot(..., col=...)` creates one panel per group while preserving a common visual structure.

```python
sns.relplot(
    data=channel_weekly,
    kind="line",
    x="date",
    y="visits",
    col="channel",
    col_wrap=2,
    height=3.5,
    facet_kws={"sharey": False}
)
```

## Annotating events

Event markers often matter more than individual values.

```python
launch_date = pd.Timestamp("2025-04-15")

fig, ax = plt.subplots(figsize=(11, 5))
ax.plot(weekly["date"], weekly["visits"], color="#2b8cbe", linewidth=2)
ax.axvline(launch_date, color="#636363", linestyle="--", linewidth=1.5)
ax.annotate(
    "Campaign launch",
    xy=(launch_date, weekly["visits"].max()),
    xytext=(launch_date, weekly["visits"].max() * 1.08),
    ha="left"
)
```

## Plotly for time exploration

Plotly is useful when stakeholders need hover details, zooming, and interactive range selection.

**Purpose:** Build an interactive time chart with a range slider.

**Walkthrough:** `px.line` handles the series; `update_xaxes(rangeslider_visible=True)` adds a built-in explorer control.

```python
import plotly.express as px

fig = px.line(
    weekly,
    x="date",
    y="visits",
    title="Weekly Website Visits"
)
fig.update_xaxes(rangeslider_visible=True)
fig.show()
```

## Common mistakes

- Comparing incomplete periods to complete ones.
- Connecting points across missing dates without checking whether the gap is meaningful.
- Using too many overlapping series in one chart.
- Adding a second y-axis when normalization or separate panels would be clearer.
- Over-smoothing the data and hiding important volatility.

## A practical checklist

Before publishing a time chart, check:

1. Are the dates parsed and sorted?
2. Is the aggregation level appropriate for the question?
3. Are incomplete periods excluded or clearly labeled?
4. Would a rolling average help, and if so, is the raw series still visible?
5. Are key events marked directly on the chart?

## Practice prompts

1. Turn daily sales into weekly and monthly charts and compare readability.
2. Add a rolling average to a noisy time series.
3. Replace a cluttered multi-line chart with small multiples.
4. Mark an intervention date and explain the post-event pattern.

## Next steps

1. Use [Plotly guide](plotly-guide.md) for richer interactive time exploration.
2. Use [Real-world case study](real-world-case-study.md) to combine time trends with category and distribution views in one workflow.
3. Use [3.4 Data storytelling](../3.4-data-storytelling/README.md) when you need to turn a time-based analysis into a stakeholder narrative.
