"""Generate example plots for matplotlib-basics.md and annotations-and-highlighting.md"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

OUT = "/Users/wongshennan/Documents/personal/career/work/skillsunion/dsai/tamkeen/docs/3-data-visualization/3.1-intro-data-viz/assets"

# ── matplotlib-basics: pyplot example ─────────────────────────────────────────
fig = plt.figure(figsize=(8, 5))
plt.plot([1, 2, 3], [1, 2, 3], 'ro-', linewidth=2, markersize=8)
plt.title('Pyplot Interface')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True, alpha=0.4)
plt.tight_layout()
fig.savefig(f"{OUT}/matplotlib_basics_pyplot.png", dpi=150, bbox_inches='tight')
plt.close(fig)
print("saved matplotlib_basics_pyplot.png")

# ── matplotlib-basics: object-oriented example ────────────────────────────────
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot([1, 2, 3], [1, 2, 3], 'bo-', linewidth=2, markersize=8)
ax.set_title('Object-Oriented Interface')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.grid(True, alpha=0.4)
fig.tight_layout()
fig.savefig(f"{OUT}/matplotlib_basics_oo.png", dpi=150, bbox_inches='tight')
plt.close(fig)
print("saved matplotlib_basics_oo.png")

# ── matplotlib-basics: multi-series line plot ─────────────────────────────────
x = np.linspace(0, 4 * np.pi, 200)
y1 = np.sin(x)
y2 = np.cos(x)

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x, y1, color='#3498db', label='Series 1 (sin)', linewidth=2)
ax.plot(x, y2, color='#e74c3c', label='Series 2 (cos)', linewidth=2)
ax.set_title('Multi-Series Line Plot')
ax.set_xlabel('Time')
ax.set_ylabel('Value')
ax.grid(True, linestyle=':', alpha=0.7)
ax.legend()
fig.tight_layout()
fig.savefig(f"{OUT}/matplotlib_basics_line.png", dpi=150, bbox_inches='tight')
plt.close(fig)
print("saved matplotlib_basics_line.png")

# ── matplotlib-basics: scatter plot with color + size ─────────────────────────
rng = np.random.default_rng(42)
n = 80
x = rng.standard_normal(n)
y = x * 0.6 + rng.standard_normal(n) * 0.8
colors = rng.uniform(0, 1, n)
sizes = rng.uniform(40, 200, n)

fig, ax = plt.subplots(figsize=(8, 5))
scatter = ax.scatter(x, y, c=colors, s=sizes, alpha=0.6, cmap='viridis')
plt.colorbar(scatter, ax=ax, label='Value')
ax.set_title('Scatter Plot with Color and Size Encoding')
ax.set_xlabel('X Variable')
ax.set_ylabel('Y Variable')
fig.tight_layout()
fig.savefig(f"{OUT}/matplotlib_basics_scatter.png", dpi=150, bbox_inches='tight')
plt.close(fig)
print("saved matplotlib_basics_scatter.png")

# ── matplotlib-basics: bar chart with error bars ─────────────────────────────
categories = ['A', 'B', 'C', 'D', 'E']
values = [1200, 950, 1450, 800, 1100]
errors = [80, 60, 110, 55, 75]

fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(categories, values, yerr=errors, capsize=5,
              color='#2ecc71', alpha=0.8)
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2., height + 30,
            f'{height:,.0f}', ha='center', va='bottom', fontsize=10)
ax.set_title('Bar Chart with Error Bars')
ax.set_xlabel('Categories')
ax.set_ylabel('Values')
ax.set_ylim(0, max(values) * 1.25)
fig.tight_layout()
fig.savefig(f"{OUT}/matplotlib_basics_bar.png", dpi=150, bbox_inches='tight')
plt.close(fig)
print("saved matplotlib_basics_bar.png")

# ── annotations: direct label + reference line + shaded range ─────────────────
x = np.arange(1, 7)
y = np.array([15, 18, 17, 25, 23, 24])
target = 20
peak_idx = y.argmax()

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(x, y, color="#2c7fb8", linewidth=2, marker='o')

ax.annotate(
    "Campaign launch peak",
    xy=(x[peak_idx], y[peak_idx]),
    xytext=(x[peak_idx] + 0.3, y[peak_idx] + 2),
    arrowprops={"arrowstyle": "->", "color": "#444"},
    fontsize=11
)
ax.axhline(y=target, color="#d95f0e", linestyle="--", linewidth=1.5, label="Target")
ax.axhspan(19, 21, color="#fee8c8", alpha=0.5, label="Target range")
ax.legend()
ax.set_title("Direct label + reference line + shaded range")
ax.set_xlabel("Month")
ax.set_ylabel("Value")
fig.tight_layout()
fig.savefig(f"{OUT}/annotations_line_annotated.png", dpi=150, bbox_inches='tight')
plt.close(fig)
print("saved annotations_line_annotated.png")

# ── annotations: selective color emphasis ────────────────────────────────────
x = np.arange(1, 7)
y = np.array([15, 18, 17, 25, 23, 24])
peak_idx = y.argmax()
colors = ["#bdbdbd"] * len(y)
colors[peak_idx] = "#e34a33"

fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(x, y, color=colors)
ax.set_title("Selective Color Emphasis — one bar highlighted")
ax.set_xlabel("Month")
ax.set_ylabel("Value")
fig.tight_layout()
fig.savefig(f"{OUT}/annotations_selective_color.png", dpi=150, bbox_inches='tight')
plt.close(fig)
print("saved annotations_selective_color.png")

# ── annotations: annotated bar chart (horizontal) ────────────────────────────
categories = ["Support", "Sales", "Ops", "Finance", "HR"]
values = [82, 96, 71, 68, 64]

fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.barh(categories, values, color="#d9d9d9")
bars[1].set_color("#3182bd")
ax.annotate(
    "Highest satisfaction",
    xy=(values[1], 1),
    xytext=(values[1] + 2, 1),
    va="center", fontsize=11
)
ax.set_xlim(0, 115)
ax.set_title("Annotated Bar Chart — highlight the top category")
ax.set_xlabel("Satisfaction score")
fig.tight_layout()
fig.savefig(f"{OUT}/annotations_bar_highlighted.png", dpi=150, bbox_inches='tight')
plt.close(fig)
print("saved annotations_bar_highlighted.png")

# ── annotations: time series with axvline ────────────────────────────────────
dates = pd.date_range("2025-01-01", periods=6, freq="ME")
traffic = [120, 128, 130, 165, 172, 176]

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(dates, traffic, marker="o", linewidth=2, color="#2b8cbe")
event_date = dates[3]
ax.axvline(event_date, color="#636363", linestyle="--")
ax.annotate(
    "Homepage redesign",
    xy=(event_date, traffic[3]),
    xytext=(dates[1], 178),
    arrowprops={"arrowstyle": "->"},
    fontsize=11
)
ax.set_title("Time Series — annotated event")
ax.set_xlabel("Date")
ax.set_ylabel("Traffic")
fig.autofmt_xdate()
fig.tight_layout()
fig.savefig(f"{OUT}/annotations_timeseries.png", dpi=150, bbox_inches='tight')
plt.close(fig)
print("saved annotations_timeseries.png")

print("All done.")
