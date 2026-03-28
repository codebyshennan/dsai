"""Generate educational diagrams for the Naive Bayes module."""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Wedge
from sklearn.datasets import make_classification
from sklearn.naive_bayes import GaussianNB
from pathlib import Path

OUT = Path(__file__).parent
SEED = 42

plt.rcParams.update({
    "font.family": "sans-serif",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "figure.dpi": 120,
})

# ── 1. bayes_theorem_venn.png ──────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(7, 5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 7)
ax.axis("off")
ax.set_title("Bayes' Theorem: Updating Beliefs with Evidence",
             fontsize=12, fontweight="bold", pad=10)

# Sample space rectangle
rect = mpatches.FancyBboxPatch((0.3, 0.5), 9.4, 5.8,
                                boxstyle="round,pad=0.1",
                                fc="#f7f7f7", ec="#aaa", lw=1.5)
ax.add_patch(rect)
ax.text(0.65, 5.95, "Sample Space  Ω", fontsize=9, color="#666")

# Circle A (prior)
circA = plt.Circle((3.8, 3.2), 1.9, fc="#6baed6", ec="#2171b5", lw=1.5, alpha=0.55)
ax.add_patch(circA)
ax.text(2.2, 3.2, "A\n(Prior\nevent)", ha="center", fontsize=10, color="#084594")

# Circle B (evidence)
circB = plt.Circle((6.2, 3.2), 1.9, fc="#fd8d3c", ec="#d94801", lw=1.5, alpha=0.55)
ax.add_patch(circB)
ax.text(7.7, 3.2, "B\n(Evidence)", ha="center", fontsize=10, color="#7f2704")

# Intersection label
ax.text(5.0, 3.2, "A ∩ B", ha="center", fontsize=10, fontweight="bold", color="#333")

# Formula
ax.text(5.0, 0.95,
        r"$P(A|B) = \dfrac{P(B|A)\cdot P(A)}{P(B)}$",
        ha="center", fontsize=12, color="#333")

# Annotation arrows
ax.annotate("P(A|B): probability\nof A given B occurred",
            xy=(4.7, 3.7), xytext=(1.2, 5.3),
            fontsize=8, color="#333",
            arrowprops=dict(arrowstyle="-|>", color="#888", lw=1))

plt.tight_layout()
plt.savefig(OUT / "bayes_theorem_venn.png", bbox_inches="tight")
plt.close()
print("Saved bayes_theorem_venn.png")

# ── 2. conditional_probability.png ────────────────────────────────────────────
data = {
    "Email is Spam": [15, 85],
    "Email is Ham": [5, 95],
}
words = ["Contains\n'FREE'", "No\n'FREE'"]
categories = list(data.keys())

fig, ax = plt.subplots(figsize=(7, 4))
x = np.arange(len(categories))
width = 0.35

bars1 = ax.bar(x - width / 2, [data[c][0] for c in categories], width,
               label=words[0], color="#e8967a", alpha=0.85)
bars2 = ax.bar(x + width / 2, [data[c][1] for c in categories], width,
               label=words[1], color="#6baed6", alpha=0.85)

ax.set_ylabel("Count (out of 100)")
ax.set_title("P(Word | Class): Conditional Probability Example\n'FREE' in subject line",
             fontweight="bold")
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()

for bar in list(bars1) + list(bars2):
    h = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, h + 1, f"{h}%",
            ha="center", va="bottom", fontsize=9)

plt.tight_layout()
plt.savefig(OUT / "conditional_probability.png", bbox_inches="tight")
plt.close()
print("Saved conditional_probability.png")

# ── 3. gaussian_nb.png ────────────────────────────────────────────────────────
rng = np.random.default_rng(SEED)
x_range = np.linspace(-4, 8, 500)

mu0, sigma0 = 1.0, 1.2
mu1, sigma1 = 4.5, 1.0

pdf0 = (1 / (sigma0 * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x_range - mu0) / sigma0) ** 2)
pdf1 = (1 / (sigma1 * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x_range - mu1) / sigma1) ** 2)

fig, ax = plt.subplots(figsize=(7, 4))
ax.fill_between(x_range, pdf0, alpha=0.35, color="#e8967a", label="Class 0 (negative)")
ax.fill_between(x_range, pdf1, alpha=0.35, color="#6baed6", label="Class 1 (positive)")
ax.plot(x_range, pdf0, color="#c94040", lw=2)
ax.plot(x_range, pdf1, color="#2171b5", lw=2)

# Decision boundary (where pdf0 == pdf1 approximately)
decision_x = (mu0 + mu1) / 2 + (sigma0 ** 2 - sigma1 ** 2) / (2 * (mu0 - mu1) + 1e-9)
ax.axvline(decision_x, ls="--", color="#444", lw=1.5, label=f"Decision boundary ≈ {decision_x:.1f}")

ax.set_xlabel("Feature value")
ax.set_ylabel("Probability density")
ax.set_title("Gaussian Naive Bayes: Feature Distributions per Class", fontweight="bold")
ax.legend()
plt.tight_layout()
plt.savefig(OUT / "gaussian_nb.png", bbox_inches="tight")
plt.close()
print("Saved gaussian_nb.png")

# ── 4. multinomial_feature_counts.png ─────────────────────────────────────────
words_list = ["buy", "free", "offer", "meeting", "agenda", "report"]
spam_counts = [42, 61, 38, 3, 1, 5]
ham_counts = [4, 7, 5, 48, 52, 55]

x = np.arange(len(words_list))
width = 0.38

fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(x - width / 2, spam_counts, width, label="Spam", color="#e8967a", alpha=0.85)
ax.bar(x + width / 2, ham_counts, width, label="Ham (not spam)", color="#6baed6", alpha=0.85)
ax.set_xticks(x)
ax.set_xticklabels(words_list)
ax.set_ylabel("Word frequency (per 100 emails)")
ax.set_title("Multinomial NB: Word Frequencies by Class", fontweight="bold")
ax.legend()
plt.tight_layout()
plt.savefig(OUT / "multinomial_feature_counts.png", bbox_inches="tight")
plt.close()
print("Saved multinomial_feature_counts.png")

# ── 5. nb_decision_boundary.png ───────────────────────────────────────────────
X, y = make_classification(
    n_samples=300, n_features=2, n_informative=2, n_redundant=0,
    n_clusters_per_class=1, random_state=SEED
)

h = 0.05
xx, yy = np.meshgrid(
    np.arange(X[:, 0].min() - 0.6, X[:, 0].max() + 0.6, h),
    np.arange(X[:, 1].min() - 0.6, X[:, 1].max() + 0.6, h),
)
gnb = GaussianNB().fit(X, y)
Z = gnb.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

fig, ax = plt.subplots(figsize=(6, 5))
ax.contourf(xx, yy, Z, alpha=0.2, cmap="RdBu")
ax.contour(xx, yy, Z, linewidths=1.5, colors="#444")
ax.scatter(X[y == 0, 0], X[y == 0, 1], c="#e8967a", edgecolors="white",
           linewidths=0.5, s=35, label="Class 0", zorder=3)
ax.scatter(X[y == 1, 0], X[y == 1, 1], c="#6baed6", edgecolors="white",
           linewidths=0.5, s=35, label="Class 1", zorder=3)
ax.set_title("Gaussian NB Decision Boundary", fontweight="bold")
ax.set_xlabel("Feature 1")
ax.set_ylabel("Feature 2")
ax.legend()
plt.tight_layout()
plt.savefig(OUT / "nb_decision_boundary.png", bbox_inches="tight")
plt.close()
print("Saved nb_decision_boundary.png")

print("\nAll Naive Bayes assets generated.")
