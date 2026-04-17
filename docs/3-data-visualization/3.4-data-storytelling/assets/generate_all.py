"""
Generate all assets for 3.4 Data Storytelling.

Run from docs/:
    uv run python 3-data-visualization/3.4-data-storytelling/assets/generate_all.py

Produces polished PNGs in the same directory as this script.
"""

from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from matplotlib.gridspec import GridSpec
import numpy as np
import seaborn as sns

# ---------------------------------------------------------------------------
# Style constants
# ---------------------------------------------------------------------------
OUT = Path(__file__).resolve().parent  # assets/ directory

BG = "#f8f9fa"
CARD_BG = "#ffffff"
TEXT_DARK = "#1a1a2e"
TEXT_MID = "#555555"
TEXT_LIGHT = "#999999"

# Accent palette (accessible & consistent across all graphics)
RED = "#e74c3c"
BLUE = "#2980b9"
TEAL = "#1abc9c"
ORANGE = "#e67e22"
PURPLE = "#8e44ad"
GREEN = "#27ae60"
GRAY = "#bdc3c7"
DARK_GRAY = "#7f8c8d"
LIGHT_GRAY = "#ecf0f1"

FONT_TITLE = 14
FONT_LABEL = 11
FONT_SMALL = 9
FONT_TINY = 8

plt.rcParams.update(
    {
        "font.family": "sans-serif",
        "font.sans-serif": ["DejaVu Sans", "Helvetica Neue", "Arial"],
        "axes.facecolor": BG,
        "figure.facecolor": "white",
        "axes.edgecolor": "#dddddd",
        "axes.grid": False,
        "xtick.color": TEXT_MID,
        "ytick.color": TEXT_MID,
    }
)


def _save(fig, name):
    fig.savefig(OUT / name, bbox_inches="tight", dpi=200, facecolor="white")
    plt.close(fig)
    print(f"  ✓ {name}")


# ===================================================================
# 1. story_arc.png — Narrative arc curve with labeled stages
# ===================================================================
def gen_story_arc():
    fig, ax = plt.subplots(figsize=(11, 5))
    ax.set_facecolor(BG)

    # Smooth asymmetric arc (peaks ~60 % across)
    x = np.linspace(0, 10, 300)
    y = 2.2 * np.exp(-((x - 6) ** 2) / 7) + 0.15

    # Gradient-colored line
    for i in range(len(x) - 1):
        t = i / len(x)
        c = plt.cm.Blues(0.35 + 0.55 * t)
        ax.plot(
            x[i : i + 2], y[i : i + 2], color=c, linewidth=3.5, solid_capstyle="round"
        )

    # Fill under curve
    ax.fill_between(x, 0, y, alpha=0.06, color=BLUE)

    stages = [
        (0.5, "Hook", "Grab attention\nwith a question\nor surprise", RED),
        (2.8, "Setup", "Establish context\nand background", BLUE),
        (6.0, "Climax", "Key insight —\nthe 'aha' moment", ORANGE),
        (8.2, "Reveal", "Connect dots\nand implications", TEAL),
        (9.8, "Call to\nAction", "Specific\nnext steps", GREEN),
    ]

    for sx, label, desc, color in stages:
        sy = 2.2 * np.exp(-((sx - 6) ** 2) / 7) + 0.15
        ax.plot(
            sx,
            sy,
            "o",
            color=color,
            markersize=11,
            zorder=5,
            markeredgecolor="white",
            markeredgewidth=2,
        )
        ax.annotate(
            label,
            (sx, sy),
            xytext=(0, 18),
            textcoords="offset points",
            ha="center",
            fontweight="bold",
            fontsize=FONT_LABEL,
            color=TEXT_DARK,
        )
        ax.annotate(
            desc,
            (sx, sy),
            xytext=(0, -16),
            textcoords="offset points",
            ha="center",
            fontsize=FONT_TINY,
            color=TEXT_MID,
            linespacing=1.4,
            va="top",
        )

    ax.set_xlim(-0.5, 10.8)
    ax.set_ylim(-0.6, 3.0)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    # Axis labels
    ax.annotate(
        "",
        xy=(10.5, -0.25),
        xytext=(0, -0.25),
        arrowprops=dict(arrowstyle="->", color=DARK_GRAY, lw=1.2),
    )
    ax.text(
        5.2, -0.45, "Story progress", ha="center", fontsize=FONT_SMALL, color=TEXT_MID
    )
    ax.annotate(
        "",
        xy=(-0.2, 2.7),
        xytext=(-0.2, -0.1),
        arrowprops=dict(arrowstyle="->", color=DARK_GRAY, lw=1.2),
    )
    ax.text(
        -0.45,
        1.3,
        "Engagement",
        ha="center",
        fontsize=FONT_SMALL,
        color=TEXT_MID,
        rotation=90,
    )

    ax.set_title(
        "The Narrative Arc in Data Storytelling",
        fontsize=FONT_TITLE,
        fontweight="bold",
        color=TEXT_DARK,
        pad=18,
    )
    _save(fig, "story_arc.png")


# ===================================================================
# 2. visual_hierarchy.png — Three-tier emphasis diagram
# ===================================================================
def gen_visual_hierarchy():
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_facecolor(BG)

    tiers = [
        (
            "Primary — Key Insight",
            95,
            RED,
            "Bold, bright, large: the one thing\nyour audience must see first",
        ),
        (
            "Secondary — Supporting Evidence",
            60,
            BLUE,
            "Medium weight: context that\nexplains and supports the insight",
        ),
        (
            "Background — Reference Data",
            30,
            GRAY,
            "Light, neutral: axes, benchmarks,\ngridlines — don't compete",
        ),
    ]

    for i, (label, width, color, desc) in enumerate(tiers):
        y = 2 - i
        bar = ax.barh(
            y,
            width,
            height=0.6,
            color=color,
            alpha=0.85,
            edgecolor="white",
            linewidth=1.5,
        )
        # Position label proportionally inside each bar
        ax.text(
            width * 0.05,
            y,
            label,
            va="center",
            ha="left",
            fontsize=FONT_LABEL,
            fontweight="bold",
            color="white" if i < 2 else TEXT_DARK,
        )
        # Description text starts after the bar ends
        ax.text(
            width + 3,
            y,
            desc,
            va="center",
            ha="left",
            fontsize=FONT_SMALL,
            color=TEXT_MID,
            linespacing=1.4,
        )

    # Size annotations
    sizes = ["48 pt", "24 pt", "12 pt"]
    for i, s in enumerate(sizes):
        y = 2 - i
        ax.text(
            -8,
            y,
            s,
            va="center",
            ha="center",
            fontsize=FONT_SMALL,
            color=TEXT_MID,
            fontstyle="italic",
        )
    ax.text(
        -8,
        2.6,
        "Size",
        va="center",
        ha="center",
        fontsize=FONT_SMALL,
        fontweight="bold",
        color=TEXT_DARK,
    )

    ax.set_xlim(-15, 135)
    ax.set_ylim(-0.5, 3.2)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    ax.set_title(
        "Visual Hierarchy — Guide the Eye to What Matters",
        fontsize=FONT_TITLE,
        fontweight="bold",
        color=TEXT_DARK,
        pad=16,
    )
    _save(fig, "visual_hierarchy.png")


# ===================================================================
# 3. color_schemes.png — Sequential / Categorical / Diverging / Accessible
# ===================================================================
def gen_color_schemes():
    fig, axes = plt.subplots(4, 1, figsize=(10, 8))
    fig.subplots_adjust(hspace=0.55)

    schemes = [
        (
            "Sequential — ordered data (low → high)",
            sns.color_palette("Blues", 7),
            "Use when values have a natural order:\nintensity, concentration, magnitude",
        ),
        (
            "Categorical — distinct groups",
            [BLUE, ORANGE, GREEN, RED, PURPLE, "#e84393", DARK_GRAY],
            "Use for unordered categories:\nproducts, regions, teams (max 6–8)",
        ),
        (
            "Diverging — positive / negative from center",
            sns.color_palette("RdBu", 7),
            "Use when values span a meaningful midpoint:\nprofit/loss, above/below target",
        ),
        (
            "Accessible — color-blind friendly",
            [
                "#0077BB",
                "#33BBEE",
                "#009988",
                "#EE7733",
                "#CC3311",
                "#EE3377",
                "#BBBBBB",
            ],
            "Avoid red-green only distinctions;\nuse blue-orange or add patterns",
        ),
    ]

    for ax, (title, colors, desc) in zip(axes, schemes):
        ax.set_facecolor(BG)
        n = len(colors)
        for i, c in enumerate(colors):
            rect = FancyBboxPatch(
                (i * 1.2, 0),
                1.0,
                1.0,
                boxstyle="round,pad=0.05",
                facecolor=c,
                edgecolor="white",
                linewidth=2,
            )
            ax.add_patch(rect)
        ax.set_xlim(-0.3, n * 1.2 + 0.3)
        ax.set_ylim(-0.8, 1.6)
        ax.text(
            n * 0.6,
            1.3,
            title,
            ha="center",
            fontsize=FONT_LABEL,
            fontweight="bold",
            color=TEXT_DARK,
        )
        ax.text(
            n * 1.2 + 0.5,
            0.5,
            desc,
            ha="left",
            va="center",
            fontsize=FONT_TINY,
            color=TEXT_MID,
            linespacing=1.5,
        )
        ax.set_xticks([])
        ax.set_yticks([])
        for spine in ax.spines.values():
            spine.set_visible(False)

    fig.suptitle(
        "Color Schemes for Data Storytelling",
        fontsize=FONT_TITLE,
        fontweight="bold",
        color=TEXT_DARK,
        y=0.98,
    )
    _save(fig, "color_schemes.png")


# ===================================================================
# 4. story_structure.png — Classic Arc vs SCR side-by-side
# ===================================================================
def gen_story_structure():
    fig = plt.figure(figsize=(12, 6.5))
    gs = GridSpec(1, 2, figure=fig, width_ratios=[1.2, 1], wspace=0.35)

    # --- Classic Arc (left) ---
    ax1 = fig.add_subplot(gs[0])
    ax1.set_facecolor(BG)

    x = np.linspace(0, 10, 200)
    y = 2.0 * np.exp(-((x - 5.5) ** 2) / 6) + 0.1
    for i in range(len(x) - 1):
        t = i / len(x)
        ax1.plot(
            x[i : i + 2],
            y[i : i + 2],
            color=plt.cm.Blues(0.3 + 0.6 * t),
            linewidth=3,
            solid_capstyle="round",
        )
    ax1.fill_between(x, 0, y, alpha=0.05, color=BLUE)

    pts = [
        (1.0, "Hook"),
        (3.0, "Setup"),
        (5.5, "Journey"),
        (7.5, "Reveal"),
        (9.5, "Action"),
    ]
    colors = [RED, BLUE, ORANGE, TEAL, GREEN]
    for (px, label), c in zip(pts, colors):
        py = 2.0 * np.exp(-((px - 5.5) ** 2) / 6) + 0.1
        ax1.plot(
            px,
            py,
            "o",
            color=c,
            markersize=9,
            zorder=5,
            markeredgecolor="white",
            markeredgewidth=1.5,
        )
        ax1.annotate(
            label,
            (px, py),
            xytext=(0, 14),
            textcoords="offset points",
            ha="center",
            fontweight="bold",
            fontsize=FONT_SMALL,
            color=TEXT_DARK,
        )

    ax1.set_xlim(-0.2, 10.5)
    ax1.set_ylim(-0.2, 2.8)
    ax1.set_xticks([])
    ax1.set_yticks([])
    for s in ax1.spines.values():
        s.set_visible(False)
    ax1.set_title(
        "Classic Narrative Arc", fontsize=12, fontweight="bold", color=TEXT_DARK, pad=12
    )
    ax1.text(
        5.2,
        -0.15,
        "Best for: longer presentations (20+ min)",
        ha="center",
        fontsize=FONT_TINY,
        color=TEXT_LIGHT,
    )

    # --- SCR (right) ---
    ax2 = fig.add_subplot(gs[1])
    ax2.set_facecolor(BG)

    scr = [
        ("Situation", "What is true today?", BLUE),
        ("Complication", "What changed or challenges us?", ORANGE),
        ("Resolution", "What we should do about it", GREEN),
    ]
    for i, (label, desc, color) in enumerate(scr):
        y = 2 - i
        rect = FancyBboxPatch(
            (0.3, y - 0.3),
            4.2,
            0.55,
            boxstyle="round,pad=0.12",
            facecolor=color,
            alpha=0.15,
            edgecolor=color,
            linewidth=1.5,
        )
        ax2.add_patch(rect)
        ax2.text(
            0.5,
            y,
            label,
            va="center",
            fontweight="bold",
            fontsize=FONT_LABEL,
            color=color,
        )
        ax2.text(0.5, y - 0.18, desc, va="center", fontsize=FONT_TINY, color=TEXT_MID)
        if i < 2:
            ax2.annotate(
                "",
                xy=(2.4, y - 0.35),
                xytext=(2.4, y - 0.5),
                arrowprops=dict(arrowstyle="->", color=DARK_GRAY, lw=1.2),
            )

    ax2.set_xlim(0, 5)
    ax2.set_ylim(-0.6, 2.8)
    ax2.set_xticks([])
    ax2.set_yticks([])
    for s in ax2.spines.values():
        s.set_visible(False)
    ax2.set_title(
        "SCR Framework", fontsize=12, fontweight="bold", color=TEXT_DARK, pad=12
    )
    ax2.text(
        2.5,
        -0.45,
        "Best for: executive briefings (5 min)",
        ha="center",
        fontsize=FONT_TINY,
        color=TEXT_LIGHT,
    )

    fig.suptitle(
        "Story Structure Frameworks",
        fontsize=FONT_TITLE,
        fontweight="bold",
        color=TEXT_DARK,
        y=1.01,
    )
    _save(fig, "story_structure.png")


# ===================================================================
# 5. layout_examples.png — Dashboard / Report / Presentation layouts
# ===================================================================
def gen_layout_examples():
    fig, axes = plt.subplots(1, 3, figsize=(14, 5))
    fig.subplots_adjust(wspace=0.3)

    layouts = [
        (
            "Dashboard Layout",
            [
                (0.05, 0.65, 0.9, 0.3, RED, "KPI Cards", 0.18),
                (0.05, 0.15, 0.42, 0.45, BLUE, "Main Chart", 0.12),
                (0.53, 0.15, 0.42, 0.45, TEAL, "Detail Table", 0.12),
                (0.05, 0.02, 0.9, 0.08, LIGHT_GRAY, "Filters", 0.08),
            ],
            "Real-time monitoring;\nKPIs top, detail below",
        ),
        (
            "Report Layout",
            [
                (0.05, 0.82, 0.9, 0.13, RED, "Executive Summary", 0.12),
                (0.05, 0.35, 0.9, 0.42, BLUE, "Analysis & Charts", 0.12),
                (0.05, 0.12, 0.9, 0.18, TEAL, "Methodology", 0.10),
                (0.05, 0.02, 0.9, 0.06, LIGHT_GRAY, "Sources", 0.07),
            ],
            "Formal documentation;\nconclusion first, detail below",
        ),
        (
            "Presentation Layout",
            [
                (0.05, 0.75, 0.9, 0.2, RED, "Headline Insight", 0.12),
                (0.05, 0.25, 0.9, 0.45, BLUE, "One Chart, One Message", 0.12),
                (0.05, 0.02, 0.9, 0.18, GREEN, "Call to Action", 0.10),
            ],
            "Storytelling flow;\nhook → evidence → action",
        ),
    ]

    for ax, (title, blocks, desc) in zip(axes, layouts):
        ax.set_facecolor(BG)
        for bx, by, bw, bh, color, label, fs in blocks:
            rect = FancyBboxPatch(
                (bx, by),
                bw,
                bh,
                boxstyle="round,pad=0.02",
                facecolor=color,
                alpha=0.15,
                edgecolor=color,
                linewidth=1.2,
            )
            ax.add_patch(rect)
            ax.text(
                bx + bw / 2,
                by + bh / 2,
                label,
                ha="center",
                va="center",
                fontsize=fs * 100,
                fontweight="bold",
                color=color,
                alpha=0.8,
            )

        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_xticks([])
        ax.set_yticks([])
        for s in ax.spines.values():
            s.set_visible(False)
        ax.set_title(title, fontsize=11, fontweight="bold", color=TEXT_DARK, pad=10)
        ax.text(
            0.5,
            -0.08,
            desc,
            ha="center",
            fontsize=FONT_TINY,
            color=TEXT_MID,
            linespacing=1.4,
        )

    fig.suptitle(
        "Common Data Presentation Layouts",
        fontsize=FONT_TITLE,
        fontweight="bold",
        color=TEXT_DARK,
        y=1.02,
    )
    _save(fig, "layout_examples.png")


# ===================================================================
# 6. narrative_arc.png — Detailed arc with zones
# ===================================================================
def gen_narrative_arc():
    fig, ax = plt.subplots(figsize=(12, 5.5))
    ax.set_facecolor(BG)

    x = np.linspace(0, 12, 400)
    y = 2.0 * np.exp(-((x - 7) ** 2) / 9) + 0.2

    # Zone backgrounds
    zones = [
        (0, 3.5, "#e8f4fd", "Context"),
        (3.5, 8.5, "#fef5e7", "Tension"),
        (8.5, 12, "#eafaf1", "Resolution"),
    ]
    for x0, x1, zc, zlabel in zones:
        ax.axvspan(x0, x1, color=zc, alpha=0.5, zorder=0)
        ax.text(
            (x0 + x1) / 2,
            2.6,
            zlabel,
            ha="center",
            fontsize=FONT_SMALL,
            color=TEXT_LIGHT,
            fontstyle="italic",
        )

    # Main curve
    for i in range(len(x) - 1):
        t = i / len(x)
        ax.plot(
            x[i : i + 2],
            y[i : i + 2],
            color=plt.cm.viridis(0.2 + 0.6 * t),
            linewidth=3.5,
            solid_capstyle="round",
        )

    stages = [
        (1.0, "Hook", "Surprising fact\nor bold question", RED),
        (3.0, "Setup", "Background the\naudience needs", BLUE),
        (5.5, "Journey", "Guided discovery\nthrough data", ORANGE),
        (7.0, "Climax", "The key\ninsight", "#d35400"),
        (9.0, "Reveal", "Implications\nand evidence", TEAL),
        (11.0, "Call to\nAction", "Specific\nnext steps", GREEN),
    ]
    for sx, label, desc, color in stages:
        sy = 2.0 * np.exp(-((sx - 7) ** 2) / 9) + 0.2
        ax.plot(
            sx,
            sy,
            "o",
            color=color,
            markersize=10,
            zorder=5,
            markeredgecolor="white",
            markeredgewidth=2,
        )
        ax.annotate(
            label,
            (sx, sy),
            xytext=(0, 16),
            textcoords="offset points",
            ha="center",
            fontweight="bold",
            fontsize=10,
            color=TEXT_DARK,
        )
        ax.annotate(
            desc,
            (sx, sy),
            xytext=(0, -14),
            textcoords="offset points",
            ha="center",
            fontsize=FONT_TINY,
            color=TEXT_MID,
            linespacing=1.3,
            va="top",
        )

    ax.set_xlim(-0.3, 12.5)
    ax.set_ylim(-0.5, 3.0)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    ax.annotate(
        "",
        xy=(12.2, -0.2),
        xytext=(0, -0.2),
        arrowprops=dict(arrowstyle="->", color=DARK_GRAY, lw=1),
    )
    ax.text(
        6,
        -0.4,
        "Presentation timeline",
        ha="center",
        fontsize=FONT_SMALL,
        color=TEXT_MID,
    )

    ax.set_title(
        "The Narrative Arc — Structuring a Data Presentation",
        fontsize=FONT_TITLE,
        fontweight="bold",
        color=TEXT_DARK,
        pad=16,
    )
    _save(fig, "narrative_arc.png")


# ===================================================================
# 7. visualization_decision_tree.png — Flowchart for chart selection
# ===================================================================
def gen_visualization_decision_tree():
    fig, ax = plt.subplots(figsize=(12, 7))
    ax.set_facecolor(BG)

    def _box(ax, x, y, w, h, text, color, fontsize=FONT_SMALL):
        rect = FancyBboxPatch(
            (x - w / 2, y - h / 2),
            w,
            h,
            boxstyle="round,pad=0.15",
            facecolor=color,
            alpha=0.15,
            edgecolor=color,
            linewidth=1.5,
        )
        ax.add_patch(rect)
        ax.text(
            x,
            y,
            text,
            ha="center",
            va="center",
            fontsize=fontsize,
            fontweight="bold",
            color=color,
        )

    def _arrow(ax, x1, y1, x2, y2, label=""):
        ax.annotate(
            "",
            xy=(x2, y2 + 0.25),
            xytext=(x1, y1 - 0.25),
            arrowprops=dict(
                arrowstyle="-|>", color=DARK_GRAY, lw=1.2, connectionstyle="arc3,rad=0"
            ),
        )
        if label:
            mx, my = (x1 + x2) / 2, (y1 + y2) / 2
            ax.text(
                mx + 0.15,
                my,
                label,
                fontsize=FONT_TINY,
                color=TEXT_MID,
                ha="left",
                va="center",
            )

    # Root
    _box(ax, 5, 6, 3.5, 0.5, "What comparison are\nyou trying to make?", TEXT_DARK, 11)

    # Level 2
    goals = [
        (1.5, 4.5, "Compare\ncategories", BLUE),
        (4, 4.5, "Trend\nover time", ORANGE),
        (6.5, 4.5, "Distribution\n& spread", TEAL),
        (9, 4.5, "Relationship\nbetween vars", PURPLE),
    ]
    for gx, gy, label, color in goals:
        _box(ax, gx, gy, 1.8, 0.5, label, color)
        _arrow(ax, 5, 6, gx, gy)

    # Level 3
    charts = [
        (0.5, 2.8, "Bar chart", BLUE),
        (2.5, 2.8, "Grouped /\nstacked bar", BLUE),
        (4, 2.8, "Line chart", ORANGE),
        (5.8, 2.8, "Histogram", TEAL),
        (7.5, 2.8, "Box plot", TEAL),
        (9, 2.8, "Scatter plot", PURPLE),
    ]
    for cx, cy, label, color in charts:
        _box(ax, cx, cy, 1.6, 0.45, label, color, FONT_SMALL)

    # Connect level 2 → 3
    _arrow(ax, 1.5, 4.5, 0.5, 2.8)
    _arrow(ax, 1.5, 4.5, 2.5, 2.8)
    _arrow(ax, 4, 4.5, 4, 2.8)
    _arrow(ax, 6.5, 4.5, 5.8, 2.8)
    _arrow(ax, 6.5, 4.5, 7.5, 2.8)
    _arrow(ax, 9, 4.5, 9, 2.8)

    # Tips at bottom
    tips = [
        (0.5, 1.8, "Few categories;\nhorizontal if\nlong labels"),
        (2.5, 1.8, "Multiple series;\ncompare parts"),
        (4, 1.8, "Continuous time;\nsmooth or stepped"),
        (5.8, 1.8, "Shape of\nvalue distribution"),
        (7.5, 1.8, "Quartiles, outliers,\nand spread"),
        (9, 1.8, "Correlation;\nadd trend line"),
    ]
    for tx, ty, tip in tips:
        ax.text(
            tx,
            ty,
            tip,
            ha="center",
            va="top",
            fontsize=7,
            color=TEXT_LIGHT,
            linespacing=1.3,
        )

    ax.set_xlim(-0.5, 10.5)
    ax.set_ylim(1.2, 6.8)
    ax.set_xticks([])
    ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)

    ax.set_title(
        "Visualization Decision Tree — Start with the Question",
        fontsize=FONT_TITLE,
        fontweight="bold",
        color=TEXT_DARK,
        pad=14,
    )
    _save(fig, "visualization_decision_tree.png")


# ===================================================================
# 8. story_creation_process.png — 10-step pipeline
# ===================================================================
def gen_story_creation_process():
    fig, ax = plt.subplots(figsize=(15, 4.5))
    ax.set_facecolor(BG)

    steps = [
        ("Collect\nData", BLUE),
        ("Analyze\nPatterns", BLUE),
        ("Extract\nInsights", ORANGE),
        ("Choose\nFramework", ORANGE),
        ("Build\nVisuals", TEAL),
        ("Peer\nReview", GREEN),
        ("Refine &\nCut", GREEN),
        ("Polish\nDesign", PURPLE),
        ("Present", RED),
        ("Measure\nImpact", RED),
    ]

    n = len(steps)
    for i, (label, color) in enumerate(steps):
        x = i * 1.4 + 0.5
        rect = FancyBboxPatch(
            (x - 0.5, 0.3),
            1.0,
            1.2,
            boxstyle="round,pad=0.15",
            facecolor=color,
            alpha=0.12,
            edgecolor=color,
            linewidth=1.5,
        )
        ax.add_patch(rect)
        ax.text(
            x,
            0.9,
            label,
            ha="center",
            va="center",
            fontsize=FONT_SMALL,
            fontweight="bold",
            color=color,
            linespacing=1.3,
        )
        ax.text(
            x,
            0.15,
            str(i + 1),
            ha="center",
            fontsize=FONT_TINY,
            color=TEXT_LIGHT,
            fontweight="bold",
        )

        if i < n - 1:
            ax.annotate(
                "",
                xy=(x + 0.7, 0.9),
                xytext=(x + 0.55, 0.9),
                arrowprops=dict(arrowstyle="-|>", color=DARK_GRAY, lw=1.0),
            )

    # Phase labels
    phases = [
        (0, 2, "Understand", BLUE),
        (2, 4, "Structure", ORANGE),
        (4, 6, "Build", TEAL),
        (6, 8, "Validate", GREEN),
        (8, 10, "Deliver", RED),
    ]
    # Removed phase labels to keep it clean - the colors already group them

    ax.set_xlim(-0.3, n * 1.25 + 0.3)
    ax.set_ylim(-0.1, 2.0)
    ax.set_xticks([])
    ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)

    ax.set_title(
        "The Story Creation Process — From Data to Decision",
        fontsize=FONT_TITLE,
        fontweight="bold",
        color=TEXT_DARK,
        pad=14,
    )
    _save(fig, "story_creation_process.png")


# ===================================================================
# 9. color_palette_guide.png — Palette samples with usage guidance
# ===================================================================
def gen_color_palette_guide():
    # Same as color_schemes but with slightly different layout for narrative-techniques
    fig, axes = plt.subplots(4, 1, figsize=(10, 7.5))
    fig.subplots_adjust(hspace=0.6)

    palettes = [
        (
            "Sequential",
            sns.color_palette("Blues", 8),
            "Ordered data: light = low, dark = high",
        ),
        (
            "Categorical",
            [BLUE, ORANGE, GREEN, RED, PURPLE, TEAL, "#e84393", DARK_GRAY],
            "Distinct groups: max 6–8 hues, no implied order",
        ),
        (
            "Diverging",
            sns.color_palette("RdBu", 9),
            "Two extremes: red ← neutral → blue (e.g. profit / loss)",
        ),
        (
            "Accessible",
            [
                "#0077BB",
                "#33BBEE",
                "#009988",
                "#EE7733",
                "#CC3311",
                "#EE3377",
                "#BBBBBB",
                "#000000",
            ],
            "Color-blind safe: avoid red-green only; use shape + color",
        ),
    ]

    for ax, (title, colors, usage) in zip(axes, palettes):
        ax.set_facecolor(BG)
        for i, c in enumerate(colors):
            rect = FancyBboxPatch(
                (i * 1.1, 0),
                0.9,
                0.9,
                boxstyle="round,pad=0.04",
                facecolor=c,
                edgecolor="white",
                linewidth=2,
            )
            ax.add_patch(rect)
        ax.set_xlim(-0.3, len(colors) * 1.1 + 0.3)
        ax.set_ylim(-0.5, 1.5)
        ax.text(
            len(colors) * 0.55,
            1.2,
            title,
            ha="center",
            fontsize=FONT_LABEL,
            fontweight="bold",
            color=TEXT_DARK,
        )
        ax.text(
            len(colors) * 0.55,
            -0.3,
            usage,
            ha="center",
            fontsize=FONT_SMALL,
            color=TEXT_MID,
        )
        ax.set_xticks([])
        ax.set_yticks([])
        for s in ax.spines.values():
            s.set_visible(False)

    fig.suptitle(
        "Color Palette Guide",
        fontsize=FONT_TITLE,
        fontweight="bold",
        color=TEXT_DARK,
        y=0.99,
    )
    _save(fig, "color_palette_guide.png")


# ===================================================================
# 10. quality_checklist.png — Visual QA checklist
# ===================================================================
def gen_quality_checklist():
    fig, ax = plt.subplots(figsize=(11, 8))
    ax.set_facecolor(BG)

    items = [
        ("Clear main message", "Can you say the insight in one sentence?", GREEN),
        ("Logical flow", "Does each section lead naturally to the next?", BLUE),
        ("Appropriate visuals", "Does every chart support the main message?", BLUE),
        ("Consistent styling", "Same fonts, colors, and layout throughout?", TEAL),
        (
            "Accessible design",
            "Can someone with color blindness read every chart?",
            TEAL,
        ),
        ("Actionable insights", "Are next steps specific enough to act on?", ORANGE),
        ("Engaging narrative", "Would you want to listen to this?", ORANGE),
        ("Proper context", "Benchmarks or comparisons that give numbers meaning?", RED),
        ("Clear call to action", "Does the audience know what to do, by when?", RED),
        ("Impact measurement", "How will you know if the recommendation worked?", RED),
    ]

    for i, (label, desc, color) in enumerate(items):
        y = 9.5 - i
        # Checkbox
        rect = FancyBboxPatch(
            (0.3, y - 0.25),
            0.4,
            0.4,
            boxstyle="round,pad=0.05",
            facecolor="white",
            edgecolor=color,
            linewidth=1.5,
        )
        ax.add_patch(rect)
        # Checkmark
        ax.text(
            0.5,
            y - 0.05,
            "✓",
            ha="center",
            va="center",
            fontsize=14,
            color=color,
            fontweight="bold",
        )
        # Label
        ax.text(
            1.0,
            y + 0.05,
            label,
            va="center",
            fontsize=12,
            fontweight="bold",
            color=TEXT_DARK,
        )
        ax.text(1.0, y - 0.25, desc, va="center", fontsize=10, color=TEXT_MID)

    ax.set_xlim(0, 11)
    ax.set_ylim(-0.5, 10.5)
    ax.set_xticks([])
    ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)

    ax.set_title(
        "Data Story Quality Checklist",
        fontsize=FONT_TITLE,
        fontweight="bold",
        color=TEXT_DARK,
        pad=14,
    )
    _save(fig, "quality_checklist.png")


# ===================================================================
# 11. before_after_example.png — Summary before/after comparison
# ===================================================================
def gen_before_after():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5))
    fig.subplots_adjust(wspace=0.35)

    np.random.seed(42)
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    values = [42, 45, 38, 51, 48, 55]

    # --- BAD version ---
    ax1.set_facecolor("#fff5f5")
    bad_colors = ["#e74c3c", "#f39c12", "#2ecc71", "#3498db", "#9b59b6", "#e91e63"]
    bars = ax1.bar(months, values, color=bad_colors, edgecolor="black", linewidth=0.5)
    ax1.set_title("Revenue by Month", fontsize=11, color=TEXT_MID)
    ax1.set_ylabel("Revenue ($K)")
    ax1.grid(True, alpha=0.3)
    # Add unnecessary elements
    ax1.legend(["Revenue"], loc="upper left", fontsize=8)
    for bar, v in zip(bars, values):
        ax1.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.5,
            str(v),
            ha="center",
            fontsize=8,
            color=TEXT_MID,
        )

    # Big red X
    ax1.text(
        0.5,
        0.5,
        "✗",
        transform=ax1.transAxes,
        fontsize=60,
        color=RED,
        alpha=0.15,
        ha="center",
        va="center",
        fontweight="bold",
    )

    ax1.text(
        0.5,
        -0.18,
        "Random colors · No insight · Descriptive title",
        transform=ax1.transAxes,
        ha="center",
        fontsize=FONT_TINY,
        color=RED,
    )

    # --- GOOD version ---
    ax2.set_facecolor("#f0faf5")
    bar_colors = [GRAY] * 6
    bar_colors[3] = GREEN  # Highlight April (the high)
    bar_colors[2] = RED  # Highlight March (the dip)
    bars = ax2.bar(months, values, color=bar_colors, edgecolor="white", linewidth=1)
    ax2.set_title(
        "Revenue Dipped in March Before Recovering 34% in April",
        fontsize=11,
        fontweight="bold",
        color=TEXT_DARK,
    )
    ax2.set_ylabel("Revenue ($K)")
    for s in ["top", "right"]:
        ax2.spines[s].set_visible(False)

    # Annotate the story
    ax2.annotate(
        "Dip: $38K\n(staffing gap)",
        xy=(2, 38),
        xytext=(0.5, 52),
        fontsize=FONT_SMALL,
        color=RED,
        arrowprops=dict(arrowstyle="->", color=RED, lw=1.2),
        ha="center",
    )
    ax2.annotate(
        "Recovery: $51K\n(new hire effect)",
        xy=(3, 51),
        xytext=(4.5, 58),
        fontsize=FONT_SMALL,
        color=GREEN,
        arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.2),
        ha="center",
    )

    # Checkmark
    ax2.text(
        0.5,
        0.5,
        "✓",
        transform=ax2.transAxes,
        fontsize=60,
        color=GREEN,
        alpha=0.12,
        ha="center",
        va="center",
        fontweight="bold",
    )

    ax2.text(
        0.5,
        -0.18,
        "Semantic color · Insight title · Annotations tell the story",
        transform=ax2.transAxes,
        ha="center",
        fontsize=FONT_TINY,
        color=GREEN,
    )

    fig.suptitle(
        "Before & After: The Same Data, Two Stories",
        fontsize=FONT_TITLE,
        fontweight="bold",
        color=TEXT_DARK,
        y=1.01,
    )
    _save(fig, "before_after_example.png")


# ===================================================================
# 12–16. Case study BAD/GOOD pairs
# ===================================================================


def _bad_watermark(ax):
    ax.text(
        0.5,
        0.5,
        "✗",
        transform=ax.transAxes,
        fontsize=80,
        color=RED,
        alpha=0.08,
        ha="center",
        va="center",
        fontweight="bold",
    )


def _good_watermark(ax):
    ax.text(
        0.5,
        0.5,
        "✓",
        transform=ax.transAxes,
        fontsize=80,
        color=GREEN,
        alpha=0.08,
        ha="center",
        va="center",
        fontweight="bold",
    )


# --- Case Study 1: Dashboard ---
def gen_cs1_dashboard():
    np.random.seed(42)
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    sales = [98, 105, 92, 115, 108, 120]
    customers = [2100, 2250, 2050, 2400, 2300, 2500]
    basket = [46.7, 46.7, 44.9, 47.9, 47.0, 48.0]

    # --- BAD ---
    fig, axes = plt.subplots(2, 3, figsize=(14, 7))
    fig.suptitle(
        "Store Performance Dashboard — Before",
        fontsize=13,
        fontweight="bold",
        color=RED,
        y=1.01,
    )
    colors_random = ["#e74c3c", "#f39c12", "#2ecc71", "#3498db", "#9b59b6", "#e91e63"]

    for i, ax in enumerate(axes.flat):
        ax.set_facecolor("#fafafa")
        metric_names = ["Sales", "Customers", "Basket", "Returns", "Shrinkage", "Labor"]
        vals = np.random.normal(50, 15, 6)
        ax.bar(months, vals, color=colors_random)
        ax.set_title(metric_names[i], fontsize=9)
        ax.tick_params(labelsize=7)
        _bad_watermark(ax)

    fig.text(
        0.5,
        -0.02,
        "Problems: too many metrics · inconsistent colors · no hierarchy · no context",
        ha="center",
        fontsize=FONT_SMALL,
        color=RED,
    )
    _save(fig, "bad_dashboard.png")

    # --- GOOD ---
    fig = plt.figure(figsize=(14, 7))
    gs = GridSpec(2, 3, figure=fig, hspace=0.4, wspace=0.3)
    fig.suptitle(
        "Store Performance Dashboard — After",
        fontsize=13,
        fontweight="bold",
        color=GREEN,
        y=1.01,
    )

    # KPI cards across top
    kpis = [
        (
            "Daily Sales",
            f"${sales[-1]}K",
            f"↑ {((sales[-1]-sales[-2])/sales[-2]*100):.0f}%",
            GREEN,
        ),
        (
            "Customer Count",
            f"{customers[-1]:,}",
            f"↑ {((customers[-1]-customers[-2])/customers[-2]*100):.0f}%",
            GREEN,
        ),
        ("Avg. Basket", f"${basket[-1]:.1f}", f"↑ ${basket[-1]-basket[-2]:.1f}", BLUE),
    ]
    for i, (title, val, delta, color) in enumerate(kpis):
        ax = fig.add_subplot(gs[0, i])
        ax.set_facecolor("white")
        ax.text(
            0.5,
            0.7,
            val,
            ha="center",
            va="center",
            fontsize=22,
            fontweight="bold",
            color=TEXT_DARK,
            transform=ax.transAxes,
        )
        ax.text(
            0.5,
            0.4,
            delta,
            ha="center",
            va="center",
            fontsize=12,
            color=color,
            transform=ax.transAxes,
        )
        ax.text(
            0.5,
            0.15,
            title,
            ha="center",
            va="center",
            fontsize=10,
            color=TEXT_MID,
            transform=ax.transAxes,
        )
        for s in ax.spines.values():
            s.set_linewidth(0.5)
            s.set_color("#eeeeee")
        ax.set_xticks([])
        ax.set_yticks([])

    # Trend chart
    ax_trend = fig.add_subplot(gs[1, :2])
    ax_trend.set_facecolor("white")
    ax_trend.plot(months, sales, color=BLUE, linewidth=2.5, marker="o", markersize=6)
    ax_trend.fill_between(months, sales, alpha=0.08, color=BLUE)
    ax_trend.set_title(
        "Monthly Sales Trend ($K)", fontsize=10, fontweight="bold", color=TEXT_DARK
    )
    ax_trend.set_ylabel("Sales ($K)", fontsize=9)
    for s in ["top", "right"]:
        ax_trend.spines[s].set_visible(False)

    # Target comparison
    ax_target = fig.add_subplot(gs[1, 2])
    ax_target.set_facecolor("white")
    targets = [100, 100, 100, 110, 110, 110]
    x_pos = range(len(months))
    ax_target.bar(
        x_pos,
        sales,
        color=[GREEN if s >= t else RED for s, t in zip(sales, targets)],
        width=0.6,
        alpha=0.8,
    )
    ax_target.plot(
        x_pos,
        targets,
        color=TEXT_DARK,
        linewidth=1.5,
        linestyle="--",
        label="Target",
        marker="",
    )
    ax_target.set_xticks(x_pos)
    ax_target.set_xticklabels(months, fontsize=8)
    ax_target.set_title("vs Target", fontsize=10, fontweight="bold", color=TEXT_DARK)
    ax_target.legend(fontsize=8)
    for s in ["top", "right"]:
        ax_target.spines[s].set_visible(False)

    _good_watermark(ax_trend)
    fig.text(
        0.5,
        -0.02,
        "Improvements: 3 focused KPIs · semantic color · clear hierarchy · trend context",
        ha="center",
        fontsize=FONT_SMALL,
        color=GREEN,
    )
    _save(fig, "good_dashboard.png")


# --- Case Study 2: Customer Journey / Funnel ---
def gen_cs2_journey():
    stages = ["Sign Up", "Verify Email", "Complete Profile", "Create Playlist", "Share"]
    counts = [10000, 8200, 6500, 3900, 2100]
    pcts = [100, 82, 65, 39, 21]

    # --- BAD ---
    fig, ax = plt.subplots(figsize=(11, 5))
    ax.set_facecolor("#fafafa")
    ax.bar(stages, counts, color=[GRAY] * 5, edgecolor="black", linewidth=0.3)
    ax.set_title("User Onboarding Steps", fontsize=11, color=TEXT_MID)
    ax.set_ylabel("Users")
    _bad_watermark(ax)
    fig.text(
        0.5,
        -0.02,
        "Problems: no drop-off rates · no color coding · no flow arrows · descriptive title",
        ha="center",
        fontsize=FONT_SMALL,
        color=RED,
    )
    fig.suptitle(
        "Customer Journey — Before", fontsize=13, fontweight="bold", color=RED, y=1.02
    )
    _save(fig, "bad_journey.png")

    # --- GOOD ---
    fig, ax = plt.subplots(figsize=(12, 5.5))
    ax.set_facecolor(BG)

    colors_funnel = [GREEN, GREEN, ORANGE, RED, ORANGE]
    bar_widths = [c / 10000 * 6 for c in counts]

    for i, (stage, count, pct, color, bw) in enumerate(
        zip(stages, counts, pcts, colors_funnel, bar_widths)
    ):
        x = i * 2.2
        rect = FancyBboxPatch(
            (x + (6 - bw) / 2 / 2.5, 0.5),
            bw / 2.5 + 0.4,
            2.5,
            boxstyle="round,pad=0.12",
            facecolor=color,
            alpha=0.18,
            edgecolor=color,
            linewidth=1.5,
        )
        ax.add_patch(rect)

        ax.text(
            x + 1.1,
            2.2,
            stage,
            ha="center",
            va="center",
            fontsize=FONT_SMALL,
            fontweight="bold",
            color=TEXT_DARK,
        )
        ax.text(
            x + 1.1,
            1.6,
            f"{count:,} users",
            ha="center",
            fontsize=FONT_SMALL,
            color=TEXT_MID,
        )
        ax.text(
            x + 1.1,
            1.1,
            f"{pct}%",
            ha="center",
            fontsize=14,
            fontweight="bold",
            color=color,
        )

        if i < len(stages) - 1:
            drop = pcts[i] - pcts[i + 1]
            ax.annotate(
                "",
                xy=(x + 2.0, 1.6),
                xytext=(x + 1.7, 1.6),
                arrowprops=dict(arrowstyle="-|>", color=DARK_GRAY, lw=1.2),
            )
            ax.text(
                x + 1.85,
                1.2,
                f"−{drop}%",
                ha="center",
                fontsize=FONT_TINY,
                color=RED,
                fontweight="bold",
            )

    # Callout for worst step
    ax.annotate(
        "40% drop-off here!\nSimplify this step",
        xy=(6.6, 0.7),
        xytext=(8.5, 0.3),
        fontsize=FONT_SMALL,
        color=RED,
        fontweight="bold",
        arrowprops=dict(arrowstyle="->", color=RED, lw=1.5),
        bbox=dict(
            boxstyle="round,pad=0.3", facecolor="#ffeaea", edgecolor=RED, linewidth=1
        ),
    )

    ax.set_xlim(-0.5, 11.5)
    ax.set_ylim(-0.3, 3.5)
    ax.set_xticks([])
    ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_title(
        "User Onboarding Funnel — 40% Drop-off at Playlist Creation",
        fontsize=12,
        fontweight="bold",
        color=TEXT_DARK,
        pad=12,
    )
    fig.suptitle(
        "Customer Journey — After", fontsize=13, fontweight="bold", color=GREEN, y=1.03
    )
    fig.text(
        0.5,
        -0.02,
        "Improvements: visual flow · drop-off rates · semantic color · actionable callout",
        ha="center",
        fontsize=FONT_SMALL,
        color=GREEN,
    )
    _save(fig, "good_journey.png")


# --- Case Study 3: Marketing Campaign ---
def gen_cs3_campaign():
    channels = ["Paid Search", "Email", "Social Media", "Display", "Referral"]
    roas = [4.1, 3.2, 1.8, 1.2, 2.5]
    spend = [150, 80, 120, 100, 50]

    # --- BAD ---
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_facecolor("#fafafa")
    x_pos = range(len(channels))
    ax.bar(
        [x - 0.2 for x in x_pos],
        roas,
        width=0.35,
        label="ROAS",
        color=GRAY,
        edgecolor="black",
        linewidth=0.3,
    )
    ax.bar(
        [x + 0.2 for x in x_pos],
        [s / 50 for s in spend],
        width=0.35,
        label="Spend (÷50)",
        color=DARK_GRAY,
        edgecolor="black",
        linewidth=0.3,
    )
    ax.set_xticks(x_pos)
    ax.set_xticklabels(channels, fontsize=8)
    ax.set_title("Q3 Marketing Results", fontsize=11, color=TEXT_MID)
    ax.legend()
    _bad_watermark(ax)
    fig.suptitle(
        "Marketing Campaign — Before", fontsize=13, fontweight="bold", color=RED, y=1.02
    )
    fig.text(
        0.5,
        -0.02,
        "Problems: mixed metrics · no ranking · no context · no recommendation",
        ha="center",
        fontsize=FONT_SMALL,
        color=RED,
    )
    _save(fig, "bad_campaign.png")

    # --- GOOD ---
    fig, ax = plt.subplots(figsize=(10, 5.5))
    ax.set_facecolor(BG)

    sorted_idx = np.argsort(roas)[::-1]
    sorted_channels = [channels[i] for i in sorted_idx]
    sorted_roas = [roas[i] for i in sorted_idx]

    bar_colors = [
        BLUE if r >= 3.0 else (ORANGE if r >= 2.0 else RED) for r in sorted_roas
    ]
    bars = ax.barh(
        range(len(sorted_channels)),
        sorted_roas,
        color=bar_colors,
        height=0.55,
        edgecolor="white",
        linewidth=1,
    )

    for i, (bar, val) in enumerate(zip(bars, sorted_roas)):
        ax.text(
            bar.get_width() + 0.08,
            bar.get_y() + bar.get_height() / 2,
            f"{val:.1f}x",
            va="center",
            fontsize=FONT_LABEL,
            fontweight="bold",
            color=TEXT_DARK,
        )

    ax.set_yticks(range(len(sorted_channels)))
    ax.set_yticklabels(sorted_channels, fontsize=FONT_LABEL)
    ax.set_xlabel("ROAS (Return on Ad Spend)", fontsize=FONT_SMALL)
    ax.axvline(x=2.0, color=DARK_GRAY, linestyle="--", linewidth=1, alpha=0.5)
    ax.text(2.05, -0.6, "Break-even", fontsize=FONT_TINY, color=TEXT_LIGHT)

    for s in ["top", "right"]:
        ax.spines[s].set_visible(False)

    ax.set_title(
        "Paid Search Delivers 4.1x ROAS — Shift Budget from Display",
        fontsize=12,
        fontweight="bold",
        color=TEXT_DARK,
        pad=12,
    )
    fig.suptitle(
        "Marketing Campaign — After",
        fontsize=13,
        fontweight="bold",
        color=GREEN,
        y=1.03,
    )
    fig.text(
        0.5,
        -0.02,
        "Improvements: single metric · sorted ranking · semantic color · insight title",
        ha="center",
        fontsize=FONT_SMALL,
        color=GREEN,
    )
    _save(fig, "good_campaign.png")


# --- Case Study 4: Financial Report ---
def gen_cs4_financial():
    quarters = ["Q1'23", "Q2'23", "Q3'23", "Q4'23", "Q1'24", "Q2'24", "Q3'24", "Q4'24"]
    revenue = [18.0, 20.0, 21.5, 22.0, 21.0, 23.0, 24.5, 26.0]
    margin = [16.0, 17.0, 17.2, 17.5, 17.0, 17.8, 18.0, 18.5]

    # --- BAD ---
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_facecolor("#fafafa")
    cell_text = []
    metrics = [
        "Revenue ($B)",
        "COGS ($B)",
        "Gross Margin (%)",
        "R&D ($B)",
        "SG&A ($B)",
        "EBIT ($B)",
        "Net Income ($B)",
        "EPS ($)",
    ]
    for m in metrics:
        row = [f"{np.random.normal(5, 2):.1f}" for _ in quarters]
        cell_text.append(row)

    table = ax.table(
        cellText=cell_text,
        rowLabels=metrics,
        colLabels=quarters,
        loc="center",
        cellLoc="center",
    )
    table.auto_set_font_size(False)
    table.set_fontsize(7)
    table.scale(1.0, 1.3)
    ax.set_title("Quarterly Financial Summary", fontsize=11, color=TEXT_MID)
    ax.axis("off")
    _bad_watermark(ax)
    fig.suptitle(
        "Financial Report — Before", fontsize=13, fontweight="bold", color=RED, y=0.98
    )
    fig.text(
        0.5,
        0.02,
        "Problems: data overload · no charts · no context · no trend visible",
        ha="center",
        fontsize=FONT_SMALL,
        color=RED,
    )
    _save(fig, "bad_financial.png")

    # --- GOOD ---
    fig = plt.figure(figsize=(14, 6))
    gs = GridSpec(1, 3, figure=fig, width_ratios=[1, 1.5, 1], wspace=0.3)
    fig.suptitle(
        "Financial Report — After", fontsize=13, fontweight="bold", color=GREEN, y=1.02
    )

    # KPI cards
    ax_kpi = fig.add_subplot(gs[0])
    ax_kpi.set_facecolor("white")
    kpis = [
        (
            "Revenue",
            f"${revenue[-1]:.0f}B",
            f"↑ {((revenue[-1]-revenue[-5])/revenue[-5]*100):.0f}% YoY",
            GREEN,
        ),
        (
            "Gross Margin",
            f"{margin[-1]:.1f}%",
            f"↑ {margin[-1]-margin[-5]:.1f}pp YoY",
            GREEN,
        ),
        ("Free Cash Flow", "$2.1B", "↑ 18% YoY", BLUE),
    ]
    for i, (title, val, delta, color) in enumerate(kpis):
        y = 0.8 - i * 0.3
        ax_kpi.text(
            0.1,
            y,
            val,
            fontsize=18,
            fontweight="bold",
            color=TEXT_DARK,
            transform=ax_kpi.transAxes,
        )
        ax_kpi.text(
            0.1, y - 0.08, delta, fontsize=10, color=color, transform=ax_kpi.transAxes
        )
        ax_kpi.text(
            0.1, y - 0.15, title, fontsize=9, color=TEXT_MID, transform=ax_kpi.transAxes
        )
    ax_kpi.set_xticks([])
    ax_kpi.set_yticks([])
    for s in ax_kpi.spines.values():
        s.set_linewidth(0.5)
        s.set_color("#eee")
    ax_kpi.set_title(
        "Key Metrics", fontsize=10, fontweight="bold", color=TEXT_DARK, pad=10
    )

    # Trend line
    ax_trend = fig.add_subplot(gs[1])
    ax_trend.set_facecolor("white")
    ax_trend.plot(
        quarters, revenue, color=BLUE, linewidth=2.5, marker="o", markersize=5
    )
    ax_trend.fill_between(quarters, revenue, alpha=0.06, color=BLUE)
    ax_trend.plot(quarters[-1], revenue[-1], "o", color=RED, markersize=10, zorder=5)
    ax_trend.annotate(
        f"${revenue[-1]:.0f}B",
        xy=(7, revenue[-1]),
        xytext=(5.5, revenue[-1] + 1.5),
        fontsize=FONT_LABEL,
        fontweight="bold",
        color=RED,
        arrowprops=dict(arrowstyle="->", color=RED, lw=1.2),
    )
    ax_trend.set_title(
        "Revenue Trend ($B)", fontsize=10, fontweight="bold", color=TEXT_DARK, pad=10
    )
    ax_trend.set_ylabel("$B", fontsize=9)
    ax_trend.tick_params(labelsize=8, rotation=45)
    for s in ["top", "right"]:
        ax_trend.spines[s].set_visible(False)

    # YoY comparison
    ax_yoy = fig.add_subplot(gs[2])
    ax_yoy.set_facecolor("white")
    q3_years = ["Q3'22", "Q3'23", "Q3'24"]
    q3_rev = [19.5, 21.5, 24.5]
    bar_colors_yoy = [GRAY, GRAY, BLUE]
    ax_yoy.bar(
        q3_years,
        q3_rev,
        color=bar_colors_yoy,
        width=0.5,
        edgecolor="white",
        linewidth=1,
    )
    for x, v in zip(range(3), q3_rev):
        ax_yoy.text(
            x,
            v + 0.3,
            f"${v:.1f}B",
            ha="center",
            fontsize=FONT_SMALL,
            fontweight="bold",
            color=TEXT_DARK,
        )
    ax_yoy.set_title(
        "Q3 Year-over-Year", fontsize=10, fontweight="bold", color=TEXT_DARK, pad=10
    )
    ax_yoy.set_ylim(0, 28)
    for s in ["top", "right"]:
        ax_yoy.spines[s].set_visible(False)

    fig.text(
        0.5,
        -0.02,
        "Improvements: 3 focused KPIs · trend visualization · YoY context · current quarter highlighted",
        ha="center",
        fontsize=FONT_SMALL,
        color=GREEN,
    )
    _save(fig, "good_financial.png")


# --- Case Study 5: Product Usage ---
def gen_cs5_usage():
    features = ["Search", "Continue\nWatching", "Browse", "My List", "Downloads"]
    usage = [2400, 1800, 1200, 400, 90]

    # --- BAD ---
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_facecolor("#fafafa")
    for i, (f, u) in enumerate(zip(features, usage)):
        ax.text(
            0.1,
            0.85 - i * 0.17,
            f"{i+1}. {f.replace(chr(10), ' ')}: {u}K weekly users",
            fontsize=11,
            color=TEXT_MID,
            transform=ax.transAxes,
        )
    ax.set_title("Feature Usage Data", fontsize=11, color=TEXT_MID)
    ax.set_xticks([])
    ax.set_yticks([])
    _bad_watermark(ax)
    fig.suptitle(
        "Product Usage — Before", fontsize=13, fontweight="bold", color=RED, y=1.02
    )
    fig.text(
        0.5,
        -0.02,
        "Problems: plain list · no chart · no ranking visible · no insight",
        ha="center",
        fontsize=FONT_SMALL,
        color=RED,
    )
    _save(fig, "bad_usage.png")

    # --- GOOD ---
    fig, ax = plt.subplots(figsize=(10, 5.5))
    ax.set_facecolor(BG)

    sorted_idx = np.argsort(usage)
    s_features = [features[i].replace("\n", " ") for i in sorted_idx]
    s_usage = [usage[i] for i in sorted_idx]

    bar_colors_usage = [GRAY] * len(s_features)
    bar_colors_usage[-1] = BLUE  # Top feature
    bar_colors_usage[-2] = TEAL  # Second
    bar_colors_usage[0] = RED  # Lowest — deprioritize?

    bars = ax.barh(
        range(len(s_features)),
        s_usage,
        color=bar_colors_usage,
        height=0.55,
        edgecolor="white",
        linewidth=1,
    )

    for i, (bar, val) in enumerate(zip(bars, s_usage)):
        label = f"{val:,}K" if val >= 1000 else f"{val}K"
        ax.text(
            bar.get_width() + 30,
            bar.get_y() + bar.get_height() / 2,
            label,
            va="center",
            fontsize=FONT_LABEL,
            color=TEXT_DARK,
        )

    ax.set_yticks(range(len(s_features)))
    ax.set_yticklabels(s_features, fontsize=FONT_LABEL)
    ax.set_xlabel("Weekly Active Users (K)", fontsize=FONT_SMALL)
    for s in ["top", "right"]:
        ax.spines[s].set_visible(False)

    ax.set_title(
        "Search Dominates Usage — Downloads May Need Promotion or Removal",
        fontsize=12,
        fontweight="bold",
        color=TEXT_DARK,
        pad=12,
    )
    fig.suptitle(
        "Product Usage — After", fontsize=13, fontweight="bold", color=GREEN, y=1.03
    )
    fig.text(
        0.5,
        -0.02,
        "Improvements: sorted bar · semantic color (invest vs deprioritize) · insight title",
        ha="center",
        fontsize=FONT_SMALL,
        color=GREEN,
    )
    _save(fig, "good_usage.png")


# ===================================================================
# Placeholder stubs — these generate simple labeled placeholders
# for images referenced in case-studies.md sub-breakdowns
# ===================================================================
def _placeholder(name, title, color=GRAY):
    """Generate a minimal placeholder for case study detail images."""
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.set_facecolor(BG)
    ax.text(
        0.5,
        0.5,
        title,
        ha="center",
        va="center",
        fontsize=FONT_LABEL,
        color=color,
        fontweight="bold",
        transform=ax.transAxes,
        wrap=True,
    )
    ax.set_xticks([])
    ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)
    _save(fig, name)


def gen_placeholders():
    """Generate detail-view placeholders referenced in case-studies.md."""
    details = [
        # CS1 dashboard
        ("bad_dashboard_metrics.png", "BAD: 20+ metrics at equal weight", RED),
        ("bad_dashboard_colors.png", "BAD: Random colors, no semantic meaning", RED),
        ("bad_dashboard_hierarchy.png", "BAD: All elements same visual weight", RED),
        (
            "good_dashboard_metrics.png",
            "GOOD: 3 focused KPI cards with sparklines",
            GREEN,
        ),
        ("good_dashboard_colors.png", "GOOD: Semantic color (green/red/gray)", GREEN),
        ("good_dashboard_hierarchy.png", "GOOD: Three visual tiers by size", GREEN),
        # CS2 journey
        ("bad_journey_text.png", "BAD: Key stats buried in paragraphs", RED),
        ("bad_journey_metrics.png", "BAD: Funnel without percentage labels", RED),
        ("bad_journey_flow.png", "BAD: Steps as bullets, no visual flow", RED),
        ("good_journey_flow.png", "GOOD: Flow diagram with icons and arrows", GREEN),
        ("good_journey_metrics.png", "GOOD: Each step shows users + drop-off", GREEN),
        ("good_journey_insights.png", "GOOD: Callout box with recommendations", GREEN),
        # CS3 campaign
        ("bad_campaign_data.png", "BAD: Dense table, no sorting or highlights", RED),
        ("bad_campaign_story.png", "BAD: Impressions chart with no narrative", RED),
        ("bad_campaign_context.png", "BAD: ROAS without prior-period comparison", RED),
        (
            "good_campaign_narrative.png",
            "GOOD: Objective → Results → Recommendations",
            GREEN,
        ),
        (
            "good_campaign_comparisons.png",
            "GOOD: ROAS by channel, sorted descending",
            GREEN,
        ),
        ("good_campaign_roi.png", "GOOD: ROI + CAC scorecard with indicators", GREEN),
        # CS4 financial
        ("bad_financial_numbers.png", "BAD: 80 cells of numbers, no highlights", RED),
        ("bad_financial_visuals.png", "BAD: Bullet points describing trends", RED),
        ("bad_financial_context.png", "BAD: Net income with no YoY comparison", RED),
        (
            "good_financial_metrics.png",
            "GOOD: 3 large KPI cards with YoY deltas",
            GREEN,
        ),
        (
            "good_financial_trends.png",
            "GOOD: 8-quarter line chart, current highlighted",
            GREEN,
        ),
        (
            "good_financial_comparison.png",
            "GOOD: Q3 grouped bars across 3 years",
            GREEN,
        ),
        # CS5 usage
        ("bad_usage_data.png", "BAD: Raw event table, 200 rows × 12 columns", RED),
        ("bad_usage_visuals.png", "BAD: Features as numbered list, no chart", RED),
        ("bad_usage_patterns.png", "BAD: DAU line chart, no annotations", RED),
        ("good_usage_flow.png", "GOOD: Sankey diagram of navigation paths", GREEN),
        ("good_usage_features.png", "GOOD: Features ranked, top 3 highlighted", GREEN),
        ("good_usage_patterns.png", "GOOD: Heatmap of sessions by hour × day", GREEN),
    ]
    for name, title, color in details:
        _placeholder(name, title, color)


# ===================================================================
# Main
# ===================================================================
def main():
    print("Generating 3.4 Data Storytelling assets...")
    print(f"Output: {OUT}\n")

    # Diagrams & concepts
    gen_story_arc()
    gen_visual_hierarchy()
    gen_color_schemes()
    gen_story_structure()
    gen_layout_examples()
    gen_narrative_arc()
    gen_visualization_decision_tree()
    gen_story_creation_process()
    gen_color_palette_guide()
    gen_quality_checklist()
    gen_before_after()

    # Case study main pairs
    gen_cs1_dashboard()
    gen_cs2_journey()
    gen_cs3_campaign()
    gen_cs4_financial()
    gen_cs5_usage()

    # Case study detail placeholders
    gen_placeholders()

    print(f"\nDone — {len(list(OUT.glob('*.png')))} PNGs in {OUT}")


if __name__ == "__main__":
    main()
