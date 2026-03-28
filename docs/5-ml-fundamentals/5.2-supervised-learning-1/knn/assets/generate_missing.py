"""Generate missing KNN diagram assets."""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from pathlib import Path

OUT = Path(__file__).parent
SEED = 42

plt.rcParams.update({
    "font.family": "sans-serif",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "figure.dpi": 120,
})

X, y = make_classification(
    n_samples=200, n_features=2, n_informative=2, n_redundant=0,
    n_clusters_per_class=1, random_state=SEED
)

# ── 1. knn_decision_boundary.png ──────────────────────────────────────────────
h = 0.05
xx, yy = np.meshgrid(
    np.arange(X[:, 0].min() - 0.6, X[:, 0].max() + 0.6, h),
    np.arange(X[:, 1].min() - 0.6, X[:, 1].max() + 0.6, h),
)
grid = np.c_[xx.ravel(), yy.ravel()]

knn = KNeighborsClassifier(n_neighbors=5).fit(X, y)
Z = knn.predict(grid).reshape(xx.shape)

fig, ax = plt.subplots(figsize=(6, 5))
ax.contourf(xx, yy, Z, alpha=0.2, cmap="RdBu")
ax.contour(xx, yy, Z, linewidths=1.5, colors="#555")
ax.scatter(X[y == 0, 0], X[y == 0, 1], c="#e8967a", edgecolors="white",
           linewidths=0.5, s=40, label="Class 0", zorder=3)
ax.scatter(X[y == 1, 0], X[y == 1, 1], c="#6baed6", edgecolors="white",
           linewidths=0.5, s=40, label="Class 1", zorder=3)
ax.set_title("KNN Decision Boundary (k = 5)", fontweight="bold")
ax.set_xlabel("Feature 1")
ax.set_ylabel("Feature 2")
ax.legend()
plt.tight_layout()
plt.savefig(OUT / "knn_decision_boundary.png", bbox_inches="tight")
plt.close()
print("Saved knn_decision_boundary.png")

# ── 2. 4-advanced_fig_1.png — k vs cross-validated accuracy ──────────────────
k_range = range(1, 31)
X_cv, y_cv = make_classification(
    n_samples=400, n_features=10, n_informative=6, random_state=SEED
)
scores = [
    cross_val_score(KNeighborsClassifier(n_neighbors=k), X_cv, y_cv,
                    cv=5, scoring="accuracy").mean()
    for k in k_range
]
best_k = list(k_range)[np.argmax(scores)]

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(k_range, scores, color="#6baed6", lw=2, marker="o", markersize=4)
ax.axvline(best_k, ls="--", color="#e8967a", lw=1.5,
           label=f"Best k = {best_k}")
ax.scatter([best_k], [max(scores)], color="#e8967a", s=80, zorder=5)
ax.set_xlabel("k (number of neighbours)")
ax.set_ylabel("5-fold CV Accuracy")
ax.set_title("Choosing k: Accuracy vs Number of Neighbours", fontweight="bold")
ax.legend()
plt.tight_layout()
plt.savefig(OUT / "4-advanced_fig_1.png", bbox_inches="tight")
plt.close()
print("Saved 4-advanced_fig_1.png")

# ── 3. 4-advanced_fig_2.png — uniform vs distance weighting ──────────────────
h2 = 0.04
xx2, yy2 = np.meshgrid(
    np.arange(X[:, 0].min() - 0.6, X[:, 0].max() + 0.6, h2),
    np.arange(X[:, 1].min() - 0.6, X[:, 1].max() + 0.6, h2),
)
grid2 = np.c_[xx2.ravel(), yy2.ravel()]

fig, axes = plt.subplots(1, 2, figsize=(10, 4), sharey=True)
for ax, weights, title in zip(
    axes,
    ["uniform", "distance"],
    ["Uniform weights\n(majority vote)", "Distance weights\n(closer = more influence)"]
):
    model = KNeighborsClassifier(n_neighbors=7, weights=weights).fit(X, y)
    Z2 = model.predict(grid2).reshape(xx2.shape)
    ax.contourf(xx2, yy2, Z2, alpha=0.2, cmap="RdBu")
    ax.contour(xx2, yy2, Z2, linewidths=1.2, colors="#555")
    ax.scatter(X[y == 0, 0], X[y == 0, 1], c="#e8967a", edgecolors="white",
               linewidths=0.5, s=30, label="Class 0")
    ax.scatter(X[y == 1, 0], X[y == 1, 1], c="#6baed6", edgecolors="white",
               linewidths=0.5, s=30, label="Class 1")
    ax.set_title(title, fontweight="bold")
    ax.set_xlabel("Feature 1")

axes[0].set_ylabel("Feature 2")
axes[0].legend(fontsize=8)
fig.suptitle("KNN Weighting Strategies (k = 7)", fontsize=12, fontweight="bold")
plt.tight_layout()
plt.savefig(OUT / "4-advanced_fig_2.png", bbox_inches="tight")
plt.close()
print("Saved 4-advanced_fig_2.png")

print("\nAll KNN missing assets generated.")
