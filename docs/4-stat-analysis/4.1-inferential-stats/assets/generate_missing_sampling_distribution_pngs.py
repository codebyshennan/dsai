"""Generate the three sampling-distribution illustrations that the lesson
references but never wrote: quality_control.png, polling_results.png,
sampling_game.png.

Run:
    uv run python docs/4-stat-analysis/4.1-inferential-stats/assets/generate_missing_sampling_distribution_pngs.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

OUT = Path(__file__).parent
np.random.seed(42)


def quality_control():
    target = 100
    tolerance = 2
    measurements = np.random.normal(100.5, 1.5, 30)
    mean = np.mean(measurements)
    se = stats.sem(measurements)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(measurements, bins=15, alpha=0.7, label="Measurements", color="#4f7cac")
    ax.axvline(mean, color="red", linestyle="--", label=f"Sample Mean ({mean:.2f})")
    ax.axvline(target, color="green", linestyle=":", label=f"Target ({target})")
    ax.axvline(target + tolerance, color="orange", linestyle=":", label="Tolerance ±2")
    ax.axvline(target - tolerance, color="orange", linestyle=":")
    ymax = ax.get_ylim()[1]
    ax.fill_between(
        [target - tolerance, target + tolerance],
        [0, 0],
        [ymax, ymax],
        color="orange",
        alpha=0.15,
    )
    ax.set_title(f"Quality Control Measurements (SE = {se:.2f})")
    ax.set_xlabel("Measurement Value")
    ax.set_ylabel("Frequency")
    ax.legend(loc="upper left", fontsize=9)
    fig.tight_layout()
    fig.savefig(OUT / "quality_control.png", dpi=120)
    plt.close(fig)


def polling_results():
    true_support = 0.52
    sample_size = 1000
    n_polls = 100
    poll_results = [
        np.mean(np.random.binomial(1, true_support, sample_size))
        for _ in range(n_polls)
    ]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(poll_results, bins=20, alpha=0.7, label="Poll Results", color="#7aa874")
    ax.axvline(
        true_support,
        color="red",
        linestyle="--",
        label=f"True Support ({true_support:.0%})",
    )
    ax.axvline(
        np.mean(poll_results),
        color="blue",
        linestyle=":",
        label=f"Mean of polls ({np.mean(poll_results):.1%})",
    )
    ax.set_title(f"Distribution of {n_polls} Polls (n = {sample_size:,} each)")
    ax.set_xlabel("Support Proportion")
    ax.set_ylabel("Frequency")
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUT / "polling_results.png", dpi=120)
    plt.close(fig)


def sampling_game():
    true_mean = 100
    true_std = 15
    sample_size = 30
    population = np.random.normal(true_mean, true_std, 10000)
    sample = np.random.choice(population, size=sample_size)
    sample_mean = np.mean(sample)
    se = np.std(sample, ddof=1) / np.sqrt(sample_size)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(
        population,
        bins=50,
        alpha=0.3,
        label="Population (N=10,000)",
        color="#888",
    )
    ax.hist(
        sample,
        bins=15,
        alpha=0.7,
        label=f"Sample (n={sample_size})",
        color="#4f7cac",
    )
    ax.axvline(true_mean, color="red", linestyle="--", label=f"True Mean ({true_mean})")
    ax.axvline(
        sample_mean,
        color="blue",
        linestyle=":",
        label=f"Sample Mean ({sample_mean:.1f})",
    )
    ymax = ax.get_ylim()[1]
    ax.fill_between(
        [sample_mean - 1.96 * se, sample_mean + 1.96 * se],
        [0, 0],
        [ymax, ymax],
        color="blue",
        alpha=0.15,
        label="Approx. 95% CI",
    )
    ax.set_title("The Sampling Game: One Draw, One Interval")
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUT / "sampling_game.png", dpi=120)
    plt.close(fig)


if __name__ == "__main__":
    quality_control()
    polling_results()
    sampling_game()
    print("Wrote quality_control.png, polling_results.png, sampling_game.png")
