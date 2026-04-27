"""Generate small (160x80) thumbnail PNGs for the CLT 'population shape' table.

Each thumbnail shows the rough shape of a population distribution so learners
can match the row description in the table to a visual cue.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

OUT = Path(__file__).parent
SIZE = (1.8, 0.9)  # inches → ~ 160x80 px at 90 dpi
DPI = 110


def _styled_axes():
    fig, ax = plt.subplots(figsize=SIZE)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ("top", "right", "left"):
        ax.spines[spine].set_visible(False)
    ax.spines["bottom"].set_color("#888")
    return fig, ax


def save(fig, name):
    fig.tight_layout(pad=0.1)
    fig.savefig(OUT / f"shape_{name}.png", dpi=DPI, transparent=True)
    plt.close(fig)


def normal():
    x = np.linspace(-4, 4, 200)
    y = stats.norm.pdf(x)
    fig, ax = _styled_axes()
    ax.fill_between(x, y, color="#4f7cac", alpha=0.7)
    ax.plot(x, y, color="#27496d", lw=1.2)
    save(fig, "normal")


def uniform():
    x = np.linspace(-1.2, 1.2, 200)
    y = np.where(np.abs(x) <= 1, 0.5, 0)
    fig, ax = _styled_axes()
    ax.fill_between(x, y, color="#7aa874", alpha=0.7)
    ax.plot(x, y, color="#3d5a45", lw=1.2)
    ax.set_ylim(0, 0.7)
    save(fig, "uniform")


def mild_skew():
    x = np.linspace(0, 8, 300)
    y = stats.gamma.pdf(x, a=4, scale=0.7)
    fig, ax = _styled_axes()
    ax.fill_between(x, y, color="#e0a458", alpha=0.7)
    ax.plot(x, y, color="#a36f1d", lw=1.2)
    save(fig, "mild_skew")


def strong_skew():
    x = np.linspace(0, 6, 300)
    y = stats.expon.pdf(x, scale=0.8)
    fig, ax = _styled_axes()
    ax.fill_between(x, y, color="#c0625b", alpha=0.7)
    ax.plot(x, y, color="#7c2a26", lw=1.2)
    save(fig, "strong_skew")


def binomial_extreme():
    n, p = 20, 0.08
    k = np.arange(0, 12)
    pmf = stats.binom.pmf(k, n, p)
    fig, ax = _styled_axes()
    ax.bar(k, pmf, width=0.8, color="#8e6fb0", alpha=0.85, edgecolor="#4a3168")
    save(fig, "binomial_extreme")


if __name__ == "__main__":
    normal()
    uniform()
    mild_skew()
    strong_skew()
    binomial_extreme()
    print("Wrote shape_*.png to", OUT)
