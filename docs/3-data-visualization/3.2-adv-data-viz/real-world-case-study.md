# Real-World Visualization Case Study

**After this lesson:** you can move from a vague business question to a cleaned dataset, a set of exploratory charts, and a polished final visualization with a clear recommendation.

> **Note:** This lesson is workflow-first. It connects [data prep](../3.1-intro-data-viz/data-prep-for-visualization.md), [annotation](../3.1-intro-data-viz/annotations-and-highlighting.md), [Seaborn guide](seaborn-guide.md), and [Plotly guide](plotly-guide.md) into one realistic analysis sequence.

## Scenario

You work for an e-commerce company. The growth team asks:

> "Why did conversion improve in Q2, and which channels should we invest in next?"

You have session-level marketing data with:

- `date`
- `channel`
- `device`
- `sessions`
- `orders`
- `revenue`

Your job is not just to make charts. Your job is to answer the question with evidence.

## Step 1: Define the decision

Break the request into smaller chartable questions:

1. Did conversion really improve over time?
2. Which channels contributed most?
3. Was the lift broad-based or concentrated in one device or channel?
4. Is the recommendation about volume, efficiency, or both?

That prevents random chart production.

## Step 2: Prepare the data

**Purpose:** Create chart-ready metrics at the right granularity.

**Walkthrough:** Aggregate by week and channel, then compute conversion rate and revenue per session.

```python
import pandas as pd

df = pd.read_csv("marketing_performance.csv")
df["date"] = pd.to_datetime(df["date"])

weekly_channel = (
    df.assign(week=df["date"].dt.to_period("W").dt.start_time)
      .groupby(["week", "channel"], as_index=False)
      .agg(
          sessions=("sessions", "sum"),
          orders=("orders", "sum"),
          revenue=("revenue", "sum")
      )
)

weekly_channel["conversion_rate"] = (
    weekly_channel["orders"] / weekly_channel["sessions"]
)
weekly_channel["revenue_per_session"] = (
    weekly_channel["revenue"] / weekly_channel["sessions"]
)
```

## Step 3: Start with exploratory charts

Use a small set of charts with distinct purposes.

### Chart 1: Overall trend

Question: Did conversion improve over time?

```python
overall_weekly = (
    weekly_channel
    .groupby("week", as_index=False)
    .agg(
        sessions=("sessions", "sum"),
        orders=("orders", "sum")
    )
)
overall_weekly["conversion_rate"] = (
    overall_weekly["orders"] / overall_weekly["sessions"]
)
```

This should usually be a line chart.

### Chart 2: Channel comparison

Question: Which channels are strongest on efficiency?

```python
channel_summary = (
    weekly_channel
    .groupby("channel", as_index=False)
    .agg(
        sessions=("sessions", "sum"),
        orders=("orders", "sum"),
        revenue=("revenue", "sum")
    )
)
channel_summary["conversion_rate"] = (
    channel_summary["orders"] / channel_summary["sessions"]
)
channel_summary["revenue_per_session"] = (
    channel_summary["revenue"] / channel_summary["sessions"]
)
```

This could be:

- a sorted bar chart for `conversion_rate`
- a scatter plot of `sessions` vs `revenue_per_session`
- a heatmap by `channel` and `device`

### Chart 3: Segment breakdown

Question: Was the improvement consistent across devices?

This is a good place for Seaborn facets or grouped lines.

## Step 4: Identify the actual takeaway

Suppose your exploratory work shows:

- total conversion improved after week 14
- paid search drove the largest session growth
- email had the highest conversion efficiency
- mobile improved more than desktop after a checkout redesign

That gives you the skeleton of the final story:

1. conversion improved in Q2
2. paid search increased volume
3. email remained the most efficient
4. the mobile redesign likely contributed to the lift

## Step 5: Build the final visuals

A good final deliverable usually uses fewer charts than the exploration phase.

### Final chart set

1. One annotated line chart for overall conversion by week.
2. One sorted bar chart for channel conversion rate or revenue per session.
3. One segmented view showing mobile vs desktop before and after the redesign.

That is usually enough. More charts are not automatically more persuasive.

## Example final chart

**Purpose:** Create an executive-ready line chart that shows the trend and marks the redesign event.

**Walkthrough:** Highlight the signal, annotate the event, and keep the styling restrained.

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(11, 5))
ax.plot(
    overall_weekly["week"],
    overall_weekly["conversion_rate"],
    color="#2b8cbe",
    linewidth=2.5
)

redesign_date = pd.Timestamp("2025-04-07")
ax.axvline(redesign_date, color="#636363", linestyle="--", linewidth=1.5)
ax.annotate(
    "Mobile checkout redesign",
    xy=(redesign_date, overall_weekly["conversion_rate"].max()),
    xytext=(redesign_date, overall_weekly["conversion_rate"].max() * 1.05),
    ha="left",
    fontsize=11
)

ax.set_title("Weekly Conversion Rate Increased After Q2 Redesign")
ax.set_xlabel("Week")
ax.set_ylabel("Conversion Rate")
ax.grid(True, alpha=0.3)
```

## Plotly version for stakeholder exploration

When the audience wants to inspect channels interactively, a Plotly chart can complement the static final chart.

```python
import plotly.express as px

fig = px.line(
    weekly_channel,
    x="week",
    y="conversion_rate",
    color="channel",
    title="Weekly Conversion Rate by Channel"
)
fig.update_layout(hovermode="x unified")
fig.show()
```

## How to write the recommendation

Your final recommendation should connect evidence to action:

- "Increase paid search budget carefully because it drove session growth, but monitor efficiency."
- "Protect email because it remains the highest-converting channel."
- "Prioritize mobile optimization because the strongest conversion lift appeared after the redesign."

That is better than simply saying "conversion went up."

## Common failure modes

- Starting with a chart type instead of a business question.
- Using too many exploratory charts in the final deck.
- Mixing volume and rate metrics without explaining the difference.
- Showing channel performance without normalizing for traffic scale.
- Presenting a correlation as proof of causation.

## A reusable project template

For any real visualization task:

1. Define the decision.
2. Prepare the data at the right level.
3. Explore with several chart types.
4. Choose the 2-3 charts that best support the conclusion.
5. Annotate the final charts.
6. Write a recommendation in plain language.

## Practice prompts

1. Rework this case study using customer support data instead of marketing data.
2. Create a final chart set for sales performance by region.
3. Replace one static chart with an interactive Plotly version and explain when each is better.
4. Write a one-paragraph recommendation based on three charts only.

## Next steps

1. Use [3.4 Data storytelling](../3.4-data-storytelling/README.md) to turn case-study evidence into a polished narrative.
2. Use the [module assignment](../_assignments/module-assignment.md) if you want a fuller end-to-end practice task.
3. Revisit [Annotations and highlighting](../3.1-intro-data-viz/annotations-and-highlighting.md) if your final charts still require too much verbal explanation.
