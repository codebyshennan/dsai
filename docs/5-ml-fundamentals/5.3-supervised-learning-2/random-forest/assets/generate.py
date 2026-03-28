"""Generate educational diagrams for the Random Forest module."""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from pathlib import Path

OUT = Path(__file__).parent
SEED = 42
rng = np.random.default_rng(SEED)

plt.rcParams.update({
    "font.family": "sans-serif",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "figure.dpi": 120,
})

# ── 1. decision_tree_boundary.png ─────────────────────────────────────────────
X, y = make_classification(
    n_samples=300, n_features=2, n_informative=2, n_redundant=0,
    n_clusters_per_class=1, random_state=SEED
)

xx, yy = np.meshgrid(
    np.linspace(X[:, 0].min() - 0.5, X[:, 0].max() + 0.5, 300),
    np.linspace(X[:, 1].min() - 0.5, X[:, 1].max() + 0.5, 300),
)
grid = np.c_[xx.ravel(), yy.ravel()]

dt = DecisionTreeClassifier(max_depth=5, random_state=SEED).fit(X, y)
rf = RandomForestClassifier(n_estimators=100, random_state=SEED).fit(X, y)

fig, axes = plt.subplots(1, 2, figsize=(10, 4), sharey=True)
titles = ["Single Decision Tree", "Random Forest (100 trees)"]
models = [dt, rf]
colors = ["#e8967a", "#6baed6"]

for ax, model, title, color in zip(axes, models, titles, colors):
    Z = model.predict(grid).reshape(xx.shape)
    ax.contourf(xx, yy, Z, alpha=0.25, cmap="RdBu")
    ax.contour(xx, yy, Z, linewidths=1.2, colors=color)
    ax.scatter(X[y == 0, 0], X[y == 0, 1], c="#e8967a", edgecolors="white",
               linewidths=0.5, s=30, label="Class 0")
    ax.scatter(X[y == 1, 0], X[y == 1, 1], c="#6baed6", edgecolors="white",
               linewidths=0.5, s=30, label="Class 1")
    ax.set_title(title, fontweight="bold")
    ax.set_xlabel("Feature 1")

axes[0].set_ylabel("Feature 2")
axes[0].legend(loc="upper right", fontsize=8)
fig.suptitle("Decision Boundary Comparison", fontsize=13, fontweight="bold")
plt.tight_layout()
plt.savefig(OUT / "decision_tree_boundary.png", bbox_inches="tight")
plt.close()
print("Saved decision_tree_boundary.png")

# ── 2. feature_importance.png ─────────────────────────────────────────────────
X2, y2 = make_classification(
    n_samples=500, n_features=8, n_informative=5, n_redundant=2,
    random_state=SEED
)
feature_names = [
    "Age", "Income", "Score", "Duration",
    "Frequency", "Recency", "Tenure", "Calls"
]

rf2 = RandomForestClassifier(n_estimators=200, random_state=SEED).fit(X2, y2)
importances = rf2.feature_importances_
order = np.argsort(importances)

fig, ax = plt.subplots(figsize=(7, 4))
bars = ax.barh(
    [feature_names[i] for i in order],
    importances[order],
    color=["#6baed6" if i >= len(order) - 3 else "#c6dbef" for i in range(len(order))]
)
ax.set_xlabel("Mean Decrease in Impurity")
ax.set_title("Feature Importances — Random Forest", fontweight="bold")
ax.axvline(1 / len(feature_names), ls="--", color="gray", lw=1, label="Uniform baseline")
ax.legend(fontsize=8)
plt.tight_layout()
plt.savefig(OUT / "feature_importance.png", bbox_inches="tight")
plt.close()
print("Saved feature_importance.png")

# ── 3. ensemble_prediction.png ────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 4))
ax.set_xlim(0, 10)
ax.set_ylim(0, 5)
ax.axis("off")
ax.set_title("How Random Forest Makes a Prediction", fontsize=13, fontweight="bold", pad=14)

tree_votes = ["Class A", "Class B", "Class A", "Class A", "Class B"]
tree_colors = ["#6baed6" if v == "Class A" else "#e8967a" for v in tree_votes]

for i, (vote, color) in enumerate(zip(tree_votes, tree_colors)):
    x = 0.5 + i * 1.4
    box = FancyBboxPatch((x, 2.6), 1.1, 1.5, boxstyle="round,pad=0.05",
                          fc=color, ec="white", lw=1.5, alpha=0.85)
    ax.add_patch(box)
    ax.text(x + 0.55, 3.35, f"Tree {i+1}", ha="center", va="center",
            fontsize=8, fontweight="bold", color="white")
    ax.text(x + 0.55, 2.9, vote, ha="center", va="center",
            fontsize=8, color="white")
    ax.annotate("", xy=(4.7, 1.8), xytext=(x + 0.55, 2.6),
                arrowprops=dict(arrowstyle="-|>", color="gray", lw=1.2))

# Majority vote box
vote_box = FancyBboxPatch((3.85, 0.8), 1.7, 1.0, boxstyle="round,pad=0.08",
                           fc="#2ca25f", ec="white", lw=2)
ax.add_patch(vote_box)
ax.text(4.7, 1.3, "Majority Vote\n→ Class A (3/5)", ha="center", va="center",
        fontsize=9, fontweight="bold", color="white")

plt.tight_layout()
plt.savefig(OUT / "ensemble_prediction.png", bbox_inches="tight")
plt.close()
print("Saved ensemble_prediction.png")

# ── 4. bias_variance.png ──────────────────────────────────────────────────────
n_estimators_range = list(range(1, 101, 5))

X3, y3 = make_classification(n_samples=600, n_features=10, n_informative=6,
                              random_state=SEED)
X_train, X_test = X3[:400], X3[400:]
y_train, y_test = y3[:400], y3[400:]

train_errors, test_errors = [], []
for n in n_estimators_range:
    model = RandomForestClassifier(n_estimators=n, random_state=SEED)
    model.fit(X_train, y_train)
    train_errors.append(1 - model.score(X_train, y_train))
    test_errors.append(1 - model.score(X_test, y_test))

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(n_estimators_range, train_errors, label="Training error",
        color="#e8967a", lw=2)
ax.plot(n_estimators_range, test_errors, label="Test error (generalisation)",
        color="#6baed6", lw=2)
ax.fill_between(n_estimators_range, train_errors, test_errors,
                alpha=0.15, color="#6baed6", label="Variance gap")
ax.set_xlabel("Number of Trees")
ax.set_ylabel("Error Rate")
ax.set_title("Bias-Variance Tradeoff as Forest Grows", fontweight="bold")
ax.legend()
ax.set_ylim(bottom=0)
plt.tight_layout()
plt.savefig(OUT / "bias_variance.png", bbox_inches="tight")
plt.close()
print("Saved bias_variance.png")

print("\nAll random-forest assets generated.")
