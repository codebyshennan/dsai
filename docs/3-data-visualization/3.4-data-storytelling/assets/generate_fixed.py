"""Regenerate case study figures to match markdown caption descriptions exactly."""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np

plt.rcParams.update({"figure.facecolor": "white", "font.family": "DejaVu Sans"})

G = "#2ecc71"  # good green
Y = "#f39c12"  # warn yellow
R = "#e74c3c"  # bad red
GR = "#95a5a6"  # neutral gray
BL = "#2980b9"  # blue
DK = "#2c3e50"  # dark

WALMART = "#004C91"
SPOTIFY = "#1DB954"
AIRBNB = "#FF5A5F"
ATEAL = "#00A699"
TESLA = "#E31937"
NETFLIX = "#E50914"


def kpi_card(
    fig, x, y, w, h, label, value, delta, positive, spark, color=WALMART, bg="#eef3fb"
):
    rect = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.005",
        facecolor=bg,
        edgecolor=color,
        linewidth=1.5,
        transform=fig.transFigure,
        clip_on=False,
    )
    fig.add_artist(rect)
    c = G if positive else R
    arr = "▲" if positive else "▼"
    fig.text(
        x + w / 2,
        y + h - 0.012,
        label,
        ha="center",
        va="top",
        fontsize=8,
        color="#555",
        transform=fig.transFigure,
    )
    fig.text(
        x + w / 2,
        y + h * 0.52,
        value,
        ha="center",
        va="center",
        fontsize=13,
        fontweight="bold",
        color=color,
        transform=fig.transFigure,
    )
    fig.text(
        x + w / 2,
        y + h * 0.22,
        f"{arr} {delta}",
        ha="center",
        va="center",
        fontsize=8,
        color=c,
        transform=fig.transFigure,
    )
    ax = fig.add_axes([x + 0.008, y + 0.008, w - 0.016, 0.038])
    ax.plot(spark, color=color, linewidth=1.5)
    ax.fill_between(range(len(spark)), spark, alpha=0.2, color=color)
    ax.axis("off")


# ── DASHBOARD ──────────────────────────────────────────────────────────────────


def bad_dashboard():
    fig = plt.figure(figsize=(14, 8))
    fig.suptitle("Store Performance Dashboard — All 20 KPIs", fontsize=12, y=0.98)
    random_colors = [
        "red",
        "blue",
        "green",
        "purple",
        "orange",
        "cyan",
        "magenta",
        "brown",
        "pink",
        "gray",
        "olive",
        "teal",
        "navy",
        "coral",
        "khaki",
        "salmon",
        "lime",
        "turquoise",
        "gold",
        "violet",
    ]
    names = [
        "Total Sales",
        "Gross Margin",
        "Net Income",
        "EBITDA",
        "Rev/SqFt",
        "Inv Turns",
        "Shrinkage%",
        "Staff Cost",
        "Mktg ROI",
        "Returns%",
        "Customers",
        "Basket Size",
        "NPS",
        "Brand Idx",
        "Foot Traffic",
        "Loyalty Mbr",
        "E-comm%",
        "Avg Disc",
        "OOS Rate",
        "Units/Hr",
    ]
    np.random.seed(7)
    gs = fig.add_gridspec(4, 5, hspace=0.65, wspace=0.55)
    for i, (name, col) in enumerate(zip(names, random_colors)):
        r, c = divmod(i, 5)
        ax = fig.add_subplot(gs[r, c])
        ax.bar(range(6), np.random.normal(100, 25, 6), color=col, width=0.8)
        ax.set_title(name, fontsize=6, pad=2)
        ax.set_xticks([])
        ax.tick_params(labelsize=4)
    plt.savefig("bad_dashboard.png", bbox_inches="tight", dpi=150)
    plt.close()


def good_dashboard():
    fig = plt.figure(figsize=(14, 8), facecolor="white")
    fig.patch.set_linewidth(1.5)
    fig.patch.set_edgecolor("#e0e0e0")
    fig.text(
        0.5,
        0.97,
        "Store Performance Dashboard",
        ha="center",
        va="top",
        fontsize=16,
        fontweight="bold",
        color=WALMART,
    )
    fig.text(
        0.5,
        0.935,
        "Week of Jan 15 · Target: Q1 +5% Growth",
        ha="center",
        va="top",
        fontsize=9,
        color="#666",
    )

    sparks = [
        [820, 810, 835, 840, 830, 847],
        [11800, 11900, 12100, 12200, 12300, 12450],
        [66, 65, 67, 67.5, 67.8, 68.1],
        [24.8, 24.6, 24.5, 24.3, 24.2, 24.1],
        [96.5, 96.8, 97, 97.3, 97.5, 97.8],
    ]
    kpis = [
        ("Daily Sales", "$847K", "+8.2%", True),
        ("Customer Count", "12,450", "+5.1%", True),
        ("Avg Basket", "$68.10", "+2.9%", True),
        ("Gross Margin", "24.1%", "-0.3%", False),
        ("In-Stock Rate", "97.8%", "+1.2%", True),
    ]
    cw, gap, sx, cy, ch = 0.155, 0.038, 0.025, 0.675, 0.19
    for i, ((lbl, val, dlt, pos), sp) in enumerate(zip(kpis, sparks)):
        kpi_card(fig, sx + i * (cw + gap), cy, cw, ch, lbl, val, dlt, pos, sp)

    # Main bar: monthly sales vs target with semantic color
    ax1 = fig.add_axes([0.04, 0.27, 0.55, 0.33])
    months = ["Aug", "Sep", "Oct", "Nov", "Dec", "Jan"]
    actual = [780, 810, 825, 920, 890, 847]
    target = [800, 800, 820, 850, 870, 820]
    bar_cols = [G if a >= t else R for a, t in zip(actual, target)]
    ax1.bar(months, actual, color=bar_cols, width=0.5, alpha=0.85, zorder=3)
    ax1.plot(months, target, "o--", color=GR, linewidth=1.5, markersize=5, zorder=4)
    ax1.set_title(
        "Monthly Sales vs Target ($K)", fontweight="bold", color=WALMART, fontsize=10
    )
    ax1.set_ylabel("Sales ($K)", fontsize=9)
    handles = [
        mpatches.Patch(color=G, label="Above Target"),
        mpatches.Patch(color=R, label="Below Target"),
        plt.Line2D([0], [0], color=GR, linestyle="--", label="Target"),
    ]
    ax1.legend(handles=handles, fontsize=8, loc="upper left")
    ax1.grid(axis="y", alpha=0.15, color="#e0e0e0")
    ax1.spines["top"].set_visible(False)
    ax1.spines["right"].set_visible(False)

    # Secondary: dept breakdown
    ax2 = fig.add_axes([0.63, 0.27, 0.34, 0.33])
    depts = ["Grocery", "Apparel", "Electronics", "Home", "Beauty"]
    vals = [38, 22, 18, 13, 9]
    ax2.barh(depts, vals, color=WALMART, alpha=0.8)
    for i, v in enumerate(vals):
        ax2.text(v + 0.4, i, f"{v}%", va="center", fontsize=9)
    ax2.set_title("Revenue Mix (%)", fontweight="bold", color=WALMART, fontsize=10)
    ax2.set_xlim(0, 48)
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_visible(False)
    ax2.grid(axis="x", alpha=0.15, color="#e0e0e0")

    # Bottom: detail table stub
    ax3 = fig.add_axes([0.04, 0.04, 0.93, 0.18])
    ax3.axis("off")
    cols = ["Store Region", "Sales $K", "vs Target", "vs LW", "NPS"]
    rows = [
        ["North", "$287K", "+6%", "+3%", "78"],
        ["South", "$264K", "-2%", "+1%", "71"],
        ["East", "$185K", "+12%", "+8%", "82"],
        ["West", "$111K", "+5%", "+2%", "75"],
    ]
    tbl = ax3.table(cellText=rows, colLabels=cols, loc="center", cellLoc="center")
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(9)
    tbl.scale(1, 1.3)
    for (r, c), cell in tbl.get_celld().items():
        if r == 0:
            cell.set_facecolor(WALMART)
            cell.set_text_props(color="white", fontweight="bold")
        elif r % 2 == 0:
            cell.set_facecolor("#f0f4ff")
    ax3.set_title(
        "Supporting Detail (scroll for more)", fontsize=9, color="#666", pad=2
    )

    plt.savefig("good_dashboard.png", bbox_inches="tight", dpi=150)
    plt.close()


def bad_dashboard_metrics():
    """20+ numeric tiles all given equal visual weight."""
    fig, ax = plt.subplots(figsize=(12, 7))
    ax.axis("off")
    fig.patch.set_facecolor("white")
    ax.set_title("Store KPIs — Weekly Summary", fontsize=13, pad=12)

    names = [
        "Total Sales",
        "Net Sales",
        "Gross Margin",
        "Net Income",
        "EBITDA",
        "Rev/SqFt",
        "Inv Turnover",
        "Shrinkage",
        "Staff Cost",
        "Mktg Spend",
        "Cust Count",
        "Basket Size",
        "NPS Score",
        "Returns%",
        "Brand Index",
        "Loyalty Mbrs",
        "E-comm%",
        "Avg Disc",
        "OOS Rate",
        "Units/Hr",
        "Capex",
        "Working Cap",
    ]
    vals = [
        "$847K",
        "$823K",
        "24.1%",
        "$142K",
        "$198K",
        "$58",
        "4.2x",
        "1.8%",
        "$312K",
        "$67K",
        "12,450",
        "$68.10",
        "76",
        "3.2%",
        "82",
        "156K",
        "18%",
        "12%",
        "2.1%",
        "94",
        "$45K",
        "$234K",
    ]
    np.random.seed(3)
    cols_per_row = 6
    for i, (n, v) in enumerate(zip(names, vals)):
        row, col = divmod(i, cols_per_row)
        x = 0.04 + col * 0.16
        y = 0.82 - row * 0.17
        rect = FancyBboxPatch(
            (x, y),
            0.14,
            0.14,
            boxstyle="round,pad=0.01",
            facecolor="#e8e8e8",
            edgecolor="#aaa",
            linewidth=1,
            transform=fig.transFigure,
            clip_on=False,
        )
        fig.add_artist(rect)
        fig.text(
            x + 0.07,
            y + 0.10,
            n,
            ha="center",
            va="center",
            fontsize=7,
            color="#555",
            transform=fig.transFigure,
        )
        fig.text(
            x + 0.07,
            y + 0.05,
            v,
            ha="center",
            va="center",
            fontsize=11,
            fontweight="bold",
            color="#222",
            transform=fig.transFigure,
        )

    plt.savefig("bad_dashboard_metrics.png", bbox_inches="tight", dpi=150)
    plt.close()


def good_dashboard_metrics():
    """Three large KPI cards with bold numbers and sparklines."""
    fig = plt.figure(figsize=(12, 5), facecolor="white")
    fig.text(
        0.5,
        0.97,
        "Primary KPIs — Top Row",
        ha="center",
        va="top",
        fontsize=13,
        fontweight="bold",
        color=WALMART,
    )
    sparks = [
        [820, 810, 835, 840, 830, 847],
        [11800, 11900, 12100, 12200, 12300, 12450],
        [66, 65, 67, 67.5, 67.8, 68.1],
    ]
    kpis = [
        ("Daily Sales", "$847K", "+8.2%", True),
        ("Customer Count", "12,450", "+5.1%", True),
        ("Avg Basket", "$68.10", "+2.9%", True),
    ]
    for i, ((lbl, val, dlt, pos), sp) in enumerate(zip(kpis, sparks)):
        kpi_card(fig, 0.05 + i * 0.32, 0.12, 0.27, 0.72, lbl, val, dlt, pos, sp)
    fig.text(
        0.5,
        0.04,
        "Each card: bold value · trend arrow · 6-week sparkline",
        ha="center",
        fontsize=9,
        color="#666",
        style="italic",
    )
    plt.savefig("good_dashboard_metrics.png", bbox_inches="tight", dpi=150)
    plt.close()


def bad_dashboard_colors():
    """Bar chart with random colors — no semantic meaning."""
    fig, ax = plt.subplots(figsize=(10, 5))
    categories = ["North", "South", "East", "West", "Online", "Wholesale"]
    vals = [287, 264, 185, 111, 143, 98]
    random_colors = ["red", "blue", "green", "purple", "orange", "cyan"]
    bars = ax.bar(categories, vals, color=random_colors, width=0.6)
    ax.set_title("Regional Sales ($K) — Color has no meaning", fontsize=12)
    ax.set_ylabel("Sales ($K)")
    for bar, v in zip(bars, vals):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 3,
            f"${v}K",
            ha="center",
            fontsize=9,
        )
    ax.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.savefig("bad_dashboard_colors.png", bbox_inches="tight", dpi=150)
    plt.close()


def good_dashboard_colors():
    """Bar chart: green=above target, red=below target, gray=on-target."""
    fig, ax = plt.subplots(figsize=(10, 5))
    categories = ["North", "South", "East", "West", "Online", "Wholesale"]
    actual = [287, 264, 185, 111, 143, 98]
    targets = [270, 270, 200, 110, 130, 105]
    status = ["above", "below", "below", "on", "above", "below"]
    cmap = {"above": G, "below": R, "on": GR}
    bar_c = [cmap[s] for s in status]
    bars = ax.bar(categories, actual, color=bar_c, width=0.6, alpha=0.88)
    ax.plot(
        range(len(categories)),
        targets,
        "o--",
        color="#333",
        linewidth=1.5,
        markersize=6,
        label="Target",
        zorder=5,
    )
    ax.set_title(
        "Regional Sales vs Target — Semantic Color", fontsize=12, fontweight="bold"
    )
    ax.set_ylabel("Sales ($K)")
    for bar, v in zip(bars, actual):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 2,
            f"${v}K",
            ha="center",
            fontsize=9,
        )
    handles = [
        mpatches.Patch(color=G, label="Above target"),
        mpatches.Patch(color=R, label="Below target"),
        mpatches.Patch(color=GR, label="On target"),
        plt.Line2D([0], [0], color="#333", linestyle="--", marker="o", label="Target"),
    ]
    ax.legend(handles=handles, fontsize=9, loc="upper right")
    ax.grid(axis="y", alpha=0.3)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.tight_layout()
    plt.savefig("good_dashboard_colors.png", bbox_inches="tight", dpi=150)
    plt.close()


def bad_dashboard_hierarchy():
    """All elements use the same font size and weight — nothing stands out."""
    fig = plt.figure(figsize=(12, 7), facecolor="white")
    np.random.seed(5)
    # 9 equal-sized panels, all same styling
    for i in range(9):
        r, c = divmod(i, 3)
        ax = fig.add_axes([0.06 + c * 0.32, 0.68 - r * 0.32, 0.28, 0.24])
        ax.bar(
            ["A", "B", "C", "D"], np.random.normal(100, 15, 4), color="#888", width=0.6
        )
        ax.set_title(f"Metric {i+1}", fontsize=10)
        ax.tick_params(labelsize=9)
    fig.suptitle("Dashboard — All Elements Equal Visual Weight", fontsize=10)
    plt.savefig("bad_dashboard_hierarchy.png", bbox_inches="tight", dpi=150)
    plt.close()


def good_dashboard_hierarchy():
    """Three visual tiers: large primary KPIs, medium secondary charts, small detail table."""
    fig = plt.figure(figsize=(14, 8), facecolor="white")
    fig.text(
        0.5,
        0.97,
        "Visual Hierarchy: Three Tiers",
        ha="center",
        va="top",
        fontsize=14,
        fontweight="bold",
        color=WALMART,
    )
    fig.text(
        0.02,
        0.91,
        "TIER 1 — Primary KPIs (largest, most prominent)",
        fontsize=9,
        color=WALMART,
        style="italic",
    )
    # Tier 1: 3 big KPI cards
    for i, (lbl, val, dlt, pos) in enumerate(
        [
            ("Daily Sales", "$847K", "+8%", True),
            ("Customers", "12,450", "+5%", True),
            ("Avg Basket", "$68", "+3%", True),
        ]
    ):
        kpi_card(
            fig,
            0.04 + i * 0.32,
            0.68,
            0.27,
            0.20,
            lbl,
            val,
            dlt,
            pos,
            [100, 102, 104, 103, 106, 108],
        )

    fig.text(
        0.02,
        0.63,
        "TIER 2 — Secondary metrics (medium, supporting)",
        fontsize=9,
        color="#555",
        style="italic",
    )
    # Tier 2: 2 medium charts
    for i, title in enumerate(["Monthly Trend", "Dept Mix"]):
        ax = fig.add_axes([0.04 + i * 0.50, 0.38, 0.42, 0.22])
        ax.bar(
            ["A", "B", "C", "D", "E", "F"],
            np.random.default_rng(i).normal(100, 15, 6),
            color=WALMART,
            alpha=0.7,
            width=0.6,
        )
        ax.set_title(title, fontsize=10, color=WALMART)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.grid(axis="y", alpha=0.3)

    fig.text(
        0.02,
        0.35,
        "TIER 3 — Detail table (small, supplementary)",
        fontsize=9,
        color="#888",
        style="italic",
    )
    # Tier 3: small table
    ax3 = fig.add_axes([0.04, 0.04, 0.93, 0.28])
    ax3.axis("off")
    rows = [
        ["North", "$287K", "+6%", "78"],
        ["South", "$264K", "-2%", "71"],
        ["East", "$185K", "+12%", "82"],
        ["West", "$111K", "+5%", "75"],
    ]
    tbl = ax3.table(
        cellText=rows,
        colLabels=["Region", "Sales", "vs Target", "NPS"],
        loc="center",
        cellLoc="center",
    )
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(8)
    tbl.scale(1, 1.2)
    for (r, c), cell in tbl.get_celld().items():
        if r == 0:
            cell.set_facecolor(WALMART)
            cell.set_text_props(color="white")
        elif r % 2 == 0:
            cell.set_facecolor("#f7f9ff")
    plt.savefig("good_dashboard_hierarchy.png", bbox_inches="tight", dpi=150)
    plt.close()


# ── JOURNEY ──────────────────────────────────────────────────────────────────


def bad_journey():
    """Text-heavy, no visual flow — numbers buried in prose."""
    fig, ax = plt.subplots(figsize=(12, 7))
    ax.axis("off")
    fig.patch.set_facecolor("white")
    text = (
        "Onboarding Analysis — Spotify New User Flow\n\n"
        "This report examines the onboarding experience for new Spotify users during Q3.\n"
        "Users who signed up during the period were observed over a 7-day window. "
        "Approximately 100,000 users signed up. A large proportion completed profile creation. "
        "After the profile step, users were asked about music preferences. A significant drop "
        "was noted here though exact figures are still being verified across data sources.\n\n"
        "Users who completed preferences were more likely to search for music. However "
        "the search feature was not always intuitive. Some users found it quickly while "
        "others did not engage with the search functionality at all during their first session.\n\n"
        "Playlist creation is a key activation milestone. The data suggests that around "
        "40% of users who reached the playlist step did not complete it. There are several "
        "hypotheses for this including UX friction and unclear value proposition.\n\n"
        "Regular usage was defined as returning within 7 days. Users who created playlists "
        "were more likely to return. The onboarding completion rate requires further review.\n\n"
        "Recommendation: Consider improving the onboarding experience to reduce drop-off."
    )
    ax.text(
        0.05,
        0.95,
        text,
        va="top",
        ha="left",
        fontsize=10,
        color="#222",
        transform=ax.transAxes,
        wrap=True,
        bbox=dict(boxstyle="round", facecolor="#f9f9f9", edgecolor="#ccc"),
    )
    ax.set_title("Onboarding Drop-off Analysis", fontsize=13, pad=10)
    plt.tight_layout()
    plt.savefig("bad_journey.png", bbox_inches="tight", dpi=150)
    plt.close()


def bad_journey_text():
    """Five paragraphs of text — critical 40% drop-off buried mid-paragraph."""
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.axis("off")
    fig.patch.set_facecolor("white")
    paragraphs = [
        "1. Sign-Up Performance\n"
        "During the quarter we observed a total of 100,000 new account registrations. "
        "The sign-up flow itself showed strong completion with most users completing email "
        "verification within the first session. No major issues were identified at this stage.",
        "2. Profile Creation Step\n"
        "Following sign-up users were directed to create their profile including display name "
        "and avatar. Of the original cohort approximately 85,000 users completed this step. "
        "This represents a 15% drop which is within expected range for onboarding flows.",
        "3. Music Preference Selection\n"
        "Users then selected their preferred genres and artists. This step saw continued drop-off "
        "with around 70,000 users completing preferences. Feedback indicates some users found "
        "the genre selection screen overwhelming with too many options presented simultaneously.",
        "4. First Search and Playlist Creation\n"
        "The data shows that of users who completed preferences only about 55,000 proceeded to "
        "search for music. More critically the step from search to actual playlist creation "
        "saw a 40% drop-off meaning only roughly 33,000 users created their first playlist. "
        "This is a significant loss in the funnel and merits investigation.",
        "5. Summary\n"
        "Overall onboarding completion is below target. Further analysis is needed to understand "
        "root causes of drop-off at each stage. A/B tests may help identify improvements.",
    ]
    y = 0.97
    for para in paragraphs:
        ax.text(
            0.03,
            y,
            para,
            va="top",
            ha="left",
            fontsize=9.5,
            color="#222",
            transform=ax.transAxes,
        )
        y -= 0.19
    ax.set_title("Onboarding Analysis Report", fontsize=13, pad=10)
    plt.tight_layout()
    plt.savefig("bad_journey_text.png", bbox_inches="tight", dpi=150)
    plt.close()


def bad_journey_metrics():
    """Funnel chart WITHOUT percentage labels — viewer can't read drop-off magnitude."""
    fig, ax = plt.subplots(figsize=(10, 6))
    steps = [
        "Sign Up",
        "Profile",
        "Preferences",
        "Search",
        "Create Playlist",
        "Regular Use",
    ]
    users = [100, 85, 70, 55, 33, 28]
    widths = [u * 0.9 for u in users]
    colors = ["#5b8dee"] * len(steps)
    for i, (step, w) in enumerate(zip(steps, widths)):
        y = len(steps) - i - 1
        ax.barh(
            y,
            w,
            height=0.6,
            left=(100 - w) / 2,
            color=colors[i],
            edgecolor="white",
            linewidth=2,
        )
        ax.text(
            50,
            y,
            step,
            ha="center",
            va="center",
            fontsize=10,
            color="white",
            fontweight="bold",
        )
        # NO percentage labels — that's the bad example
    ax.set_xlim(0, 105)
    ax.set_yticks([])
    ax.set_xticks([])
    ax.spines[:].set_visible(False)
    ax.set_title("User Onboarding Funnel", fontsize=12)
    fig.text(
        0.5,
        0.02,
        "← No completion rates shown — viewer cannot measure drop-off severity",
        ha="center",
        fontsize=9,
        color="#999",
        style="italic",
    )
    plt.tight_layout()
    plt.savefig("bad_journey_metrics.png", bbox_inches="tight", dpi=150)
    plt.close()


def bad_journey_flow():
    """Bullet list of steps — no arrows, no visual progression."""
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.axis("off")
    fig.patch.set_facecolor("white")
    ax.set_title("Onboarding Steps", fontsize=14, pad=12)
    steps = [
        "• Step 1: User signs up with email or social login",
        "• Step 2: User creates their profile (name, photo)",
        "• Step 3: User selects music preferences (genres/artists)",
        "• Step 4: User searches for music",
        "• Step 5: User creates first playlist",
        "• Step 6: User becomes a regular listener",
    ]
    for i, step in enumerate(steps):
        ax.text(
            0.1,
            0.82 - i * 0.12,
            step,
            va="top",
            ha="left",
            fontsize=12,
            transform=ax.transAxes,
            color="#222",
        )
    fig.text(
        0.5,
        0.03,
        "← Disconnected bullets — no arrows, no drop-off data, no visual progression",
        ha="center",
        fontsize=9,
        color="#999",
        style="italic",
    )
    plt.savefig("bad_journey_flow.png", bbox_inches="tight", dpi=150)
    plt.close()


def good_journey():
    """Visual funnel: 5 steps, completion %, color-coded green/yellow/red by health."""
    fig, ax = plt.subplots(figsize=(10, 7))
    steps = [
        "Sign Up",
        "Profile",
        "Preferences",
        "Search",
        "Create Playlist",
        "Regular Use",
    ]
    users = [100, 85, 70, 55, 33, 28]
    health = ["good", "good", "good", "warn", "bad", "warn"]
    cmap = {"good": G, "warn": Y, "bad": R}
    for i, (step, u, h) in enumerate(zip(steps, users, health)):
        y = len(steps) - i - 1
        w = u * 0.88
        left = (100 - w) / 2
        ax.barh(
            y,
            w,
            height=0.65,
            left=left,
            color=cmap[h],
            edgecolor="white",
            linewidth=2,
            alpha=0.88,
        )
        ax.text(
            50,
            y + 0.02,
            f"{step}",
            ha="center",
            va="center",
            fontsize=10,
            color="white",
            fontweight="bold",
        )
        ax.text(
            50,
            y - 0.25,
            f"{u}% completion",
            ha="center",
            va="center",
            fontsize=9,
            color="#333",
        )
        if i > 0:
            drop = users[i - 1] - u
            ax.text(
                104,
                y,
                f"−{drop}%",
                va="center",
                ha="left",
                fontsize=9,
                color=cmap[h],
                fontweight="bold",
            )
    ax.set_xlim(0, 115)
    ax.set_yticks([])
    ax.set_xticks([])
    ax.spines[:].set_visible(False)
    ax.set_title(
        "Spotify Onboarding Funnel — Completion & Health",
        fontsize=12,
        fontweight="bold",
    )
    handles = [
        mpatches.Patch(color=G, label="On target (>65%)"),
        mpatches.Patch(color=Y, label="Watch (<65%)"),
        mpatches.Patch(color=R, label="Critical (<50%)"),
    ]
    ax.legend(handles=handles, loc="lower right", fontsize=9)
    plt.tight_layout()
    plt.savefig("good_journey.png", bbox_inches="tight", dpi=150)
    plt.close()


def good_journey_flow():
    """Flow diagram: step boxes with icons, arrows, conversion rates."""
    fig, ax = plt.subplots(figsize=(14, 5))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 5)
    ax.axis("off")
    ax.set_title(
        "User Onboarding Flow — Visual Progression",
        fontsize=13,
        fontweight="bold",
        pad=10,
    )

    steps = [
        ("Sign Up", "✉", "100%", G),
        ("Profile", "◉", "85%", G),
        ("Preferences", "♪", "70%", G),
        ("Search", "⊙", "55%", Y),
        ("Create Playlist", "≡", "33%", R),
    ]
    box_w, box_h = 2.0, 1.6
    xs = [0.5, 3.0, 5.5, 8.0, 10.5]

    for i, (step, icon, pct, color) in enumerate(steps):
        x = xs[i]
        rect = FancyBboxPatch(
            (x, 1.7),
            box_w,
            box_h,
            boxstyle="round,pad=0.1",
            facecolor=color,
            edgecolor="white",
            linewidth=2,
            alpha=0.85,
        )
        ax.add_patch(rect)
        ax.text(
            x + box_w / 2,
            1.7 + box_h * 0.70,
            icon,
            ha="center",
            va="center",
            fontsize=18,
        )
        ax.text(
            x + box_w / 2,
            1.7 + box_h * 0.35,
            step,
            ha="center",
            va="center",
            fontsize=9,
            color="white",
            fontweight="bold",
        )
        ax.text(
            x + box_w / 2,
            1.3,
            pct,
            ha="center",
            va="center",
            fontsize=11,
            color=color,
            fontweight="bold",
        )
        ax.text(
            x + box_w / 2,
            0.9,
            "completion",
            ha="center",
            va="center",
            fontsize=8,
            color="#555",
        )
        if i < len(steps) - 1:
            ax.annotate(
                "",
                xy=(xs[i + 1] - 0.05, 2.5),
                xytext=(x + box_w + 0.05, 2.5),
                arrowprops=dict(arrowstyle="->", color="#666", lw=2.0),
            )
            drop_labels = ["", "-15%", "-15%", "-15%", "-40%"]
            if drop_labels[i + 1]:
                dcol = R if drop_labels[i + 1] == "-40%" else Y
                ax.text(
                    (x + box_w + xs[i + 1]) / 2,
                    2.1,
                    drop_labels[i + 1],
                    ha="center",
                    va="center",
                    fontsize=9,
                    color=dcol,
                    fontweight="bold",
                )
    plt.tight_layout()
    plt.savefig("good_journey_flow.png", bbox_inches="tight", dpi=150)
    plt.close()


def good_journey_metrics():
    """Each step: users entering, completing, and drop-off rate in bold."""
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.axis("off")
    ax.set_title(
        "Onboarding Funnel — Users In / Out / Drop-off per Step", fontsize=12, pad=10
    )
    fig.patch.set_facecolor("white")

    steps = ["Sign Up", "Profile", "Prefs", "Search", "Playlist"]
    into_ = [100000, 100000, 85000, 70000, 55000]
    compl = [100000, 85000, 70000, 55000, 33000]
    drops = [0, 15, 15, 15, 40]

    cols = ["Step", "Users In", "Users Completed", "Drop-off %"]
    cell_data = [
        [s, f"{i:,}", f"{c:,}", f"{d}%"]
        for s, i, c, d in zip(steps, into_, compl, drops)
    ]
    tbl = ax.table(cellText=cell_data, colLabels=cols, loc="center", cellLoc="center")
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(11)
    tbl.scale(1.5, 2.2)
    for (r, c), cell in tbl.get_celld().items():
        if r == 0:
            cell.set_facecolor("#2c3e50")
            cell.set_text_props(color="white", fontweight="bold")
        elif c == 3 and r > 0:
            val = drops[r - 1]
            cell.set_facecolor(R if val >= 30 else Y if val >= 10 else G)
            cell.set_text_props(color="white", fontweight="bold")
        elif r % 2 == 0:
            cell.set_facecolor("#f5f5f5")
    plt.savefig("good_journey_metrics.png", bbox_inches="tight", dpi=150)
    plt.close()


def good_journey_insights():
    """Funnel with callout box beside worst-performing step."""
    fig, axes = plt.subplots(
        1, 2, figsize=(14, 6), gridspec_kw={"width_ratios": [1.6, 1]}
    )
    ax = axes[0]
    steps = [
        "Sign Up",
        "Profile",
        "Preferences",
        "Search",
        "Create Playlist",
        "Regular Use",
    ]
    users = [100, 85, 70, 55, 33, 28]
    health = ["good", "good", "good", "warn", "bad", "warn"]
    cmap = {"good": G, "warn": Y, "bad": R}
    for i, (step, u, h) in enumerate(zip(steps, users, health)):
        y = len(steps) - i - 1
        w = u * 0.88
        c = cmap[h]
        lw = 3 if h == "bad" else 1
        ax.barh(
            y,
            w,
            height=0.65,
            left=(100 - w) / 2,
            color=c,
            edgecolor="white" if h != "bad" else "#c0392b",
            linewidth=lw,
            alpha=0.88,
        )
        ax.text(
            50,
            y,
            f"{step}  ({u}%)",
            ha="center",
            va="center",
            fontsize=9.5,
            color="white",
            fontweight="bold",
        )
        if i > 0:
            ax.text(
                92,
                y,
                f"−{users[i-1]-u}%",
                va="center",
                ha="left",
                fontsize=9,
                color=cmap[h],
                fontweight="bold",
            )
    ax.set_xlim(0, 108)
    ax.set_yticks([])
    ax.set_xticks([])
    ax.spines[:].set_visible(False)
    ax.set_title("Onboarding Funnel", fontsize=11, fontweight="bold")

    # Callout panel
    ax2 = axes[1]
    ax2.axis("off")
    ax2.set_facecolor("#fff5f5")
    ax2.set_title(
        "⚠ Critical Drop-off: Create Playlist (−40%)",
        fontsize=10,
        color=R,
        fontweight="bold",
        pad=8,
    )
    recs = [
        "1. Auto-generate a starter playlist\n   on sign-up (reduce friction)",
        "2. Reduce required fields from 5\n   to 2 at playlist creation",
        "3. Send 24-hour reminder email\n   to users who haven't created\n   a playlist yet",
    ]
    for i, rec in enumerate(recs):
        ax2.text(
            0.07,
            0.78 - i * 0.28,
            rec,
            va="top",
            ha="left",
            fontsize=10,
            transform=ax2.transAxes,
            color="#333",
            bbox=dict(boxstyle="round,pad=0.4", facecolor="white", edgecolor="#f5c6cb"),
        )

    plt.tight_layout()
    plt.savefig("good_journey_insights.png", bbox_inches="tight", dpi=150)
    plt.close()


# ── CAMPAIGN ─────────────────────────────────────────────────────────────────


def bad_campaign():
    """Raw data table — 8 columns, all channels at equal weight, no highlights."""
    fig, ax = plt.subplots(figsize=(13, 7))
    ax.axis("off")
    ax.set_title(
        "Q3 Campaign Performance — All Channels & Metrics", fontsize=12, pad=10
    )
    channels = [
        "Facebook",
        "Instagram",
        "Google Ads",
        "Email",
        "Organic",
        "Affiliates",
        "YouTube",
        "Twitter",
        "Pinterest",
        "LinkedIn",
        "Snapchat",
        "TikTok",
        "Display",
        "Native",
        "Podcast",
        "Radio",
        "TV",
        "OOH",
        "Direct Mail",
        "SMS",
    ]
    cols = [
        "Channel",
        "Impressions",
        "Clicks",
        "CTR%",
        "CPA($)",
        "Spend($)",
        "Conv",
        "ROAS",
    ]
    np.random.seed(1)
    rows = [
        [
            ch,
            f"{int(np.random.uniform(10,500))}K",
            f"{int(np.random.uniform(500,20000)):,}",
            f"{np.random.uniform(0.5,8):.1f}%",
            f"${np.random.uniform(10,150):.0f}",
            f"${np.random.uniform(5,200):.0f}K",
            f"{int(np.random.uniform(50,2000)):,}",
            f"{np.random.uniform(0.5,5):.1f}x",
        ]
        for ch in channels
    ]
    tbl = ax.table(cellText=rows, colLabels=cols, loc="center", cellLoc="center")
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(7.5)
    tbl.scale(1, 1.1)
    for (r, c), cell in tbl.get_celld().items():
        if r == 0:
            cell.set_facecolor("#ddd")
            cell.set_text_props(fontweight="bold")
    plt.savefig("bad_campaign.png", bbox_inches="tight", dpi=150)
    plt.close()


def bad_campaign_data():
    """Dense table — no sorting, color, or highlights, all channels equal weight."""
    fig, ax = plt.subplots(figsize=(11, 6))
    ax.axis("off")
    ax.set_title("Marketing Data Export — Channel × Metric Matrix", fontsize=11, pad=8)
    channels = [
        "Facebook",
        "Instagram",
        "Google",
        "Email",
        "Organic",
        "Affiliates",
        "YouTube",
        "Twitter",
    ]
    metrics = [
        "Impressions",
        "Clicks",
        "CTR",
        "CPA",
        "Spend",
        "Conv",
        "ROAS",
        "CPM",
        "Reach",
        "Freq",
    ]
    np.random.seed(9)
    data = [[f"{np.random.uniform(1,500):.1f}" for _ in metrics] for _ in channels]
    tbl = ax.table(
        cellText=data,
        rowLabels=channels,
        colLabels=metrics,
        loc="center",
        cellLoc="center",
    )
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(8)
    tbl.scale(1.2, 1.4)
    for (r, c), cell in tbl.get_celld().items():
        if r == 0 or c == -1:
            cell.set_facecolor("#e0e0e0")
            cell.set_text_props(fontweight="bold")
    plt.savefig("bad_campaign_data.png", bbox_inches="tight", dpi=150)
    plt.close()


def bad_campaign_story():
    """Bar chart titled 'Q3 Marketing Results' — impressions only, no revenue link."""
    fig, ax = plt.subplots(figsize=(10, 5))
    channels = ["Facebook", "Instagram", "Google", "Email", "Organic"]
    impressions = [480, 320, 210, 95, 65]
    ax.bar(channels, impressions, color=BL, width=0.55)
    ax.set_title("Q3 Marketing Results — Impressions by Channel", fontsize=12)
    ax.set_ylabel("Impressions (thousands)")
    for i, v in enumerate(impressions):
        ax.text(i, v + 5, f"{v}K", ha="center", fontsize=9)
    ax.grid(axis="y", alpha=0.3)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    fig.text(
        0.5,
        0.01,
        "← No revenue, no ROAS, no objective stated — data without a story",
        ha="center",
        fontsize=9,
        color="#999",
        style="italic",
    )
    plt.tight_layout()
    plt.savefig("bad_campaign_story.png", bbox_inches="tight", dpi=150)
    plt.close()


def bad_campaign_context():
    """ROAS values shown without prior-period comparison or benchmark."""
    fig, ax = plt.subplots(figsize=(10, 5))
    channels = ["Facebook", "Instagram", "Google", "Email", "Organic"]
    roas = [2.3, 1.8, 4.1, 3.2, 5.0]
    ax.bar(channels, roas, color="#5dade2", width=0.55)
    ax.set_title("Channel ROAS — Q3 2024", fontsize=12)
    ax.set_ylabel("ROAS (x)")
    for i, v in enumerate(roas):
        ax.text(i, v + 0.05, f"{v}x", ha="center", fontsize=10)
    ax.grid(axis="y", alpha=0.3)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    fig.text(
        0.5,
        0.01,
        "← No Q2 comparison, no benchmark — is 2.3x good or bad?",
        ha="center",
        fontsize=9,
        color="#999",
        style="italic",
    )
    plt.tight_layout()
    plt.savefig("bad_campaign_context.png", bbox_inches="tight", dpi=150)
    plt.close()


def good_campaign():
    """Campaign report: narrative headline, ROAS comparison chart, YoY annotations, recommendation."""
    fig = plt.figure(figsize=(14, 8), facecolor="white")
    # Headline
    fig.text(
        0.5,
        0.95,
        "Paid Search delivered 4.1x ROAS, outperforming Social by 60%",
        ha="center",
        va="top",
        fontsize=14,
        fontweight="bold",
        color=AIRBNB,
    )
    fig.text(
        0.5,
        0.905,
        "Q3 2024 · Total Spend: $500K · Objective: Maximize bookings at ROAS ≥ 2.5x",
        ha="center",
        va="top",
        fontsize=10,
        color="#555",
    )

    # Main: horizontal ROAS bar chart sorted desc
    ax1 = fig.add_axes([0.04, 0.42, 0.56, 0.42])
    channels = [
        "Paid Search",
        "Organic SEO",
        "Email",
        "Facebook",
        "Instagram",
        "Display",
    ]
    roas = [4.1, 5.0, 3.2, 2.3, 1.8, 1.2]
    roas_q2 = [3.5, 4.8, 3.0, 2.5, 2.0, 1.4]
    idx = np.argsort(roas)
    ch_s, r_s, r2_s = (
        [channels[i] for i in idx],
        [roas[i] for i in idx],
        [roas_q2[i] for i in idx],
    )
    bar_c = [G if r >= 2.5 else R for r in r_s]
    bars = ax1.barh(ch_s, r_s, color=bar_c, height=0.5, alpha=0.85)
    ax1.axvline(2.5, color="#333", linestyle="--", linewidth=1.5, label="Target 2.5x")
    for i, (r, r2) in enumerate(zip(r_s, r2_s)):
        delta = r - r2
        arrow = "▲" if delta >= 0 else "▼"
        col = G if delta >= 0 else R
        ax1.text(
            r + 0.05,
            i,
            f"{r}x  {arrow}{abs(delta):.1f} vs Q2",
            va="center",
            fontsize=9,
            color=col,
        )
    ax1.set_title(
        "ROAS by Channel vs Target (sorted)",
        fontsize=10,
        fontweight="bold",
        color=AIRBNB,
    )
    ax1.set_xlabel("ROAS (x)")
    ax1.set_xlim(0, 7)
    handles = [
        mpatches.Patch(color=G, label="Above 2.5x target"),
        mpatches.Patch(color=R, label="Below 2.5x target"),
        plt.Line2D([0], [0], color="#333", linestyle="--", label="Target 2.5x"),
    ]
    ax1.legend(handles=handles, fontsize=8, loc="lower right")
    ax1.spines["top"].set_visible(False)
    ax1.spines["right"].set_visible(False)

    # Recommendation box
    ax2 = fig.add_axes([0.64, 0.42, 0.33, 0.42])
    ax2.axis("off")
    ax2.set_facecolor("#fff9f0")
    ax2.set_title(
        "Recommendation", fontsize=11, fontweight="bold", color="#e67e22", pad=6
    )
    recs = [
        "→ Reallocate 30% of Instagram\n   budget to Paid Search\n   (Est. +$42K revenue)",
        "→ Scale Email to $80K spend\n   (high ROAS, low saturation)",
        "→ Pause Display in Q4\n   (ROAS below break-even)",
    ]
    for i, r in enumerate(recs):
        ax2.text(
            0.07,
            0.82 - i * 0.30,
            r,
            va="top",
            ha="left",
            fontsize=10,
            transform=ax2.transAxes,
            color="#333",
            bbox=dict(boxstyle="round,pad=0.4", facecolor="white", edgecolor="#f5cba7"),
        )

    # Spend vs ROAS scatter
    ax3 = fig.add_axes([0.04, 0.06, 0.93, 0.30])
    spend = [120, 80, 70, 150, 50, 30]
    sc = ax3.scatter(
        spend, roas, s=200, c=[G if r >= 2.5 else R for r in roas], zorder=5, alpha=0.9
    )
    for i, ch in enumerate(channels):
        ax3.annotate(
            ch,
            (spend[i], roas[i]),
            xytext=(5, 5),
            textcoords="offset points",
            fontsize=9,
        )
    ax3.axhline(2.5, color="#333", linestyle="--", linewidth=1.2, label="Target 2.5x")
    ax3.set_xlabel("Q3 Spend ($K)", fontsize=10)
    ax3.set_ylabel("ROAS (x)", fontsize=10)
    ax3.set_title(
        "Spend vs Efficiency — bubble = channel", fontsize=10, fontweight="bold"
    )
    ax3.legend(fontsize=9)
    ax3.grid(alpha=0.3)
    ax3.spines["top"].set_visible(False)
    ax3.spines["right"].set_visible(False)

    plt.savefig("good_campaign.png", bbox_inches="tight", dpi=150)
    plt.close()


def good_campaign_narrative():
    """Three clearly labelled sections: Objective, Results, Recommendations."""
    fig = plt.figure(figsize=(13, 8), facecolor="white")
    sections = [
        (
            "OBJECTIVE",
            "#2c3e50",
            "Maximize Q3 bookings across all channels\nwith a minimum ROAS target of 2.5x.\nTotal budget: $500K",
        ),
        (
            "RESULTS",
            AIRBNB,
            "Paid Search: 4.1x ROAS ✓\nEmail: 3.2x ROAS ✓\nFacebook: 2.3x ROAS ✗\nInstagram: 1.8x ROAS ✗\nDisplay: 1.2x ROAS ✗",
        ),
        (
            "RECOMMENDATIONS",
            "#27ae60",
            "1. Shift 30% of Social budget → Paid Search\n2. Scale Email to $80K spend\n3. Pause Display in Q4\nDecision needed: Oct 1 budget review",
        ),
    ]
    for i, (title, color, body) in enumerate(sections):
        x = 0.04 + i * 0.33
        rect = FancyBboxPatch(
            (x, 0.08),
            0.29,
            0.84,
            boxstyle="round,pad=0.01",
            facecolor="white",
            edgecolor=color,
            linewidth=3,
            transform=fig.transFigure,
            clip_on=False,
        )
        fig.add_artist(rect)
        # Section header band
        header = FancyBboxPatch(
            (x, 0.82),
            0.29,
            0.10,
            boxstyle="round,pad=0.005",
            facecolor=color,
            edgecolor=color,
            linewidth=0,
            transform=fig.transFigure,
            clip_on=False,
        )
        fig.add_artist(header)
        fig.text(
            x + 0.145,
            0.87,
            title,
            ha="center",
            va="center",
            fontsize=13,
            fontweight="bold",
            color="white",
            transform=fig.transFigure,
        )
        fig.text(
            x + 0.145,
            0.60,
            body,
            ha="center",
            va="center",
            fontsize=10,
            color="#333",
            transform=fig.transFigure,
            multialignment="center",
            linespacing=1.6,
        )
    fig.text(
        0.5,
        0.02,
        "Clear narrative structure: context → evidence → action",
        ha="center",
        fontsize=9,
        color="#666",
        style="italic",
    )
    plt.savefig("good_campaign_narrative.png", bbox_inches="tight", dpi=150)
    plt.close()


def good_campaign_comparisons():
    """Horizontal bar chart, ROAS sorted descending, shared scale."""
    fig, ax = plt.subplots(figsize=(10, 6))
    channels = [
        "Organic SEO",
        "Paid Search",
        "Email",
        "Facebook",
        "Instagram",
        "Display",
    ]
    roas = [5.0, 4.1, 3.2, 2.3, 1.8, 1.2]
    idx = np.argsort(roas)
    ch_s = [channels[i] for i in idx]
    r_s = [roas[i] for i in idx]
    bar_c = [G if r >= 2.5 else R for r in r_s]
    bars = ax.barh(ch_s, r_s, color=bar_c, height=0.5, alpha=0.88)
    ax.axvline(2.5, color="#333", linestyle="--", linewidth=1.5)
    ax.text(2.55, -0.6, "Target 2.5x", fontsize=9, color="#333")
    for i, r in enumerate(r_s):
        ax.text(
            r + 0.06,
            i,
            f"{r}x",
            va="center",
            fontsize=10,
            fontweight="bold",
            color=G if r >= 2.5 else R,
        )
    ax.set_title(
        "ROAS by Channel — sorted descending, shared scale",
        fontsize=12,
        fontweight="bold",
        color=AIRBNB,
    )
    ax.set_xlabel("ROAS (Return on Ad Spend)")
    ax.set_xlim(0, 6.5)
    handles = [
        mpatches.Patch(color=G, label="Above 2.5x target"),
        mpatches.Patch(color=R, label="Below 2.5x target"),
    ]
    ax.legend(handles=handles, fontsize=9, loc="lower right")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis="x", alpha=0.3)
    plt.tight_layout()
    plt.savefig("good_campaign_comparisons.png", bbox_inches="tight", dpi=150)
    plt.close()


def good_campaign_roi():
    """Scorecard: ROI and CAC per channel, green/red indicators."""
    fig, ax = plt.subplots(figsize=(11, 6))
    ax.axis("off")
    ax.set_title(
        "Channel ROI & Customer Acquisition Cost Scorecard",
        fontsize=12,
        fontweight="bold",
        pad=10,
    )
    channels = [
        "Paid Search",
        "Organic SEO",
        "Email",
        "Facebook",
        "Instagram",
        "Display",
    ]
    roi = [4.1, 5.0, 3.2, 2.3, 1.8, 1.2]
    cac = [24, 18, 32, 68, 85, 140]
    target_roi, target_cac = 2.5, 60

    cols = ["Channel", "ROAS", "vs Target", "CAC ($)", "vs CAC Target", "Action"]
    rows = []
    for ch, r, c in zip(channels, roi, cac):
        roi_ok = r >= target_roi
        cac_ok = c <= target_cac
        action = (
            "Scale ↑" if roi_ok and cac_ok else ("Pause ✗" if not roi_ok else "Watch →")
        )
        rows.append(
            [
                ch,
                f"{r}x",
                "✓" if roi_ok else "✗",
                f"${c}",
                "✓" if cac_ok else "✗",
                action,
            ]
        )

    tbl = ax.table(cellText=rows, colLabels=cols, loc="center", cellLoc="center")
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(10)
    tbl.scale(1.4, 2.0)
    for (r, c), cell in tbl.get_celld().items():
        if r == 0:
            cell.set_facecolor("#2c3e50")
            cell.set_text_props(color="white", fontweight="bold")
        elif r > 0:
            if c == 2:
                cell.set_facecolor(G if rows[r - 1][2] == "✓" else R)
                cell.set_text_props(color="white", fontweight="bold", fontsize=12)
            elif c == 4:
                cell.set_facecolor(G if rows[r - 1][4] == "✓" else R)
                cell.set_text_props(color="white", fontweight="bold", fontsize=12)
            elif c == 5:
                val = rows[r - 1][5]
                cell.set_facecolor(G if "Scale" in val else R if "Pause" in val else Y)
                cell.set_text_props(color="white", fontweight="bold")
            elif r % 2 == 0:
                cell.set_facecolor("#f9f9f9")
    plt.savefig("good_campaign_roi.png", bbox_inches="tight", dpi=150)
    plt.close()


# ── FINANCIAL ────────────────────────────────────────────────────────────────


def bad_financial():
    """Dense financial table — 10 columns × 8 quarters, no highlights."""
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.axis("off")
    ax.set_title(
        "Tesla Financial Performance — Raw Data (all metrics, all quarters)",
        fontsize=11,
        pad=8,
    )
    qs = ["Q1'21", "Q2'21", "Q3'21", "Q4'21", "Q1'22", "Q2'22", "Q3'22", "Q4'22"]
    cols = [
        "Quarter",
        "Revenue",
        "COGS",
        "Gross Profit",
        "R&D",
        "SG&A",
        "EBIT",
        "Net Income",
        "EPS",
        "FCF",
        "Capex",
    ]
    np.random.seed(2)
    rows = [[q] + [f"${np.random.uniform(2,25):.1f}B" for _ in range(10)] for q in qs]
    tbl = ax.table(cellText=rows, colLabels=cols, loc="center", cellLoc="center")
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(7)
    tbl.scale(1, 1.5)
    for (r, c), cell in tbl.get_celld().items():
        if r == 0:
            cell.set_facecolor("#ccc")
            cell.set_text_props(fontweight="bold", fontsize=6.5)
    plt.savefig("bad_financial.png", bbox_inches="tight", dpi=150)
    plt.close()


def bad_financial_numbers():
    """P&L table 10×8 = 80 cells, size-10 font, no shading or highlights."""
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.axis("off")
    ax.set_title("Quarterly P&L — All Metrics", fontsize=11, pad=8)
    qs = ["Q1'22", "Q2'22", "Q3'22", "Q4'22", "Q1'23", "Q2'23", "Q3'23", "Q4'23"]
    metrics = [
        "Revenue",
        "COGS",
        "Gross Profit",
        "R&D",
        "SG&A",
        "EBIT",
        "Net Income",
        "FCF",
        "Capex",
        "EPS",
    ]
    np.random.seed(11)
    data = [[f"{np.random.uniform(1,25):.1f}" for _ in qs] for _ in metrics]
    tbl = ax.table(
        cellText=data, rowLabels=metrics, colLabels=qs, loc="center", cellLoc="center"
    )
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(8)
    tbl.scale(1.1, 1.35)
    for (r, c), cell in tbl.get_celld().items():
        if r == 0 or c == -1:
            cell.set_facecolor("#e0e0e0")
            cell.set_text_props(fontweight="bold", fontsize=7.5)
    plt.savefig("bad_financial_numbers.png", bbox_inches="tight", dpi=150)
    plt.close()


def bad_financial_visuals():
    """Bullet points describing revenue — trends buried in prose, no charts."""
    fig, ax = plt.subplots(figsize=(11, 7))
    ax.axis("off")
    fig.patch.set_facecolor("white")
    ax.set_title("Q4 2022 Financial Highlights", fontsize=14, pad=12)
    bullets = [
        "• Revenue grew 12% year-over-year reaching $24.3B, up from $21.5B in Q3 2022.",
        "• Gross margin declined to 23.8% from 32.9% in Q1 2022 reflecting higher input\n"
        "  costs and production ramp expenses at new factories in Texas and Berlin.",
        "• EBIT came in at $3.9B representing an EBIT margin of approximately 16%\n"
        "  compared to 14.8% in the year-ago period.",
        "• Free cash flow was $1.4B, lower than the $3.3B generated in Q4 2021 primarily\n"
        "  due to elevated capex of $1.9B related to gigafactory expansion.",
        "• Net income was $3.7B or $1.07 per diluted share versus $2.3B or $0.68 in Q4 2021.",
    ]
    for i, b in enumerate(bullets):
        ax.text(
            0.05,
            0.83 - i * 0.16,
            b,
            va="top",
            ha="left",
            fontsize=11,
            transform=ax.transAxes,
            color="#222",
            linespacing=1.5,
        )
    fig.text(
        0.5,
        0.03,
        "← Trends buried in prose — a line chart would show this instantly",
        ha="center",
        fontsize=9,
        color="#999",
        style="italic",
    )
    plt.savefig("bad_financial_visuals.png", bbox_inches="tight", dpi=150)
    plt.close()


def bad_financial_context():
    """Single '$1.1B Net Income' shown in isolation — no comparison."""
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.axis("off")
    fig.patch.set_facecolor("white")
    rect = FancyBboxPatch(
        (0.15, 0.25),
        0.70,
        0.50,
        boxstyle="round,pad=0.02",
        facecolor="#f0f0f0",
        edgecolor="#bbb",
        linewidth=2,
        transform=fig.transFigure,
        clip_on=False,
    )
    fig.add_artist(rect)
    fig.text(
        0.5,
        0.65,
        "Q3 Net Income",
        ha="center",
        va="center",
        fontsize=14,
        color="#555",
        transform=fig.transFigure,
    )
    fig.text(
        0.5,
        0.50,
        "$3.7B",
        ha="center",
        va="center",
        fontsize=36,
        fontweight="bold",
        color="#222",
        transform=fig.transFigure,
    )
    fig.text(
        0.5,
        0.35,
        "(Tesla Q4 2022)",
        ha="center",
        va="center",
        fontsize=11,
        color="#777",
        transform=fig.transFigure,
    )
    fig.text(
        0.5,
        0.12,
        "← Is this a record? A miss? Up or down? No context = uninterpretable",
        ha="center",
        fontsize=9,
        color=R,
        style="italic",
    )
    plt.savefig("bad_financial_context.png", bbox_inches="tight", dpi=150)
    plt.close()


def good_financial():
    """3 KPI cards + 8-quarter trend line (current highlighted) + annotation."""
    fig = plt.figure(figsize=(14, 8), facecolor="white")
    fig.text(
        0.5,
        0.97,
        "Tesla Q4 2022 — Record automotive deliveries drove Q3 outperformance",
        ha="center",
        va="top",
        fontsize=13,
        fontweight="bold",
        color=TESLA,
    )

    sparks = [
        [18.8, 16.9, 21.5, 24.3, 23.3, 19.9, 21.4, 24.3],
        [32.9, 27.9, 25.1, 23.8, 25.6, 26.1, 26.8, 27.3],
        [2.2, 1.4, 3.3, 1.4, 0.5, 2.0, 3.3, 1.9],
    ]
    kpis = [
        ("Revenue", "$24.3B", "+36% YoY", True),
        ("Gross Margin", "23.8%", "-9.1pp YoY", False),
        ("Free Cash Flow", "$1.4B", "-57% YoY", False),
    ]
    cw, gap, sx, cy, ch = 0.22, 0.04, 0.04, 0.71, 0.20
    for i, ((lbl, val, dlt, pos), sp) in enumerate(zip(kpis, sparks)):
        kpi_card(
            fig,
            sx + i * (cw + gap),
            cy,
            cw,
            ch,
            lbl,
            val,
            dlt,
            pos,
            sp,
            color=TESLA,
            bg="#fff0ee",
        )

    # 8-quarter revenue trend
    ax1 = fig.add_axes([0.04, 0.27, 0.62, 0.38])
    qs = ["Q1'21", "Q2'21", "Q3'21", "Q4'21", "Q1'22", "Q2'22", "Q3'22", "Q4'22"]
    rev = [10.4, 11.9, 13.8, 17.7, 18.8, 16.9, 21.5, 24.3]
    ax1.plot(qs, rev, color=TESLA, marker="o", linewidth=2.5, zorder=4)
    ax1.fill_between(range(len(qs)), rev, alpha=0.15, color=TESLA)
    # Highlight current quarter
    ax1.scatter([7], [24.3], s=150, color=TESLA, zorder=6)
    ax1.annotate(
        "Q4'22\n$24.3B\n(Record)",
        xy=(7, 24.3),
        xytext=(5.8, 22.5),
        fontsize=9,
        color=TESLA,
        fontweight="bold",
        arrowprops=dict(arrowstyle="->", color=TESLA, lw=1.5),
    )
    # Forecast
    ax1.plot(
        [7, 8, 9],
        [24.3, 25.8, 27.2],
        color=TESLA,
        linewidth=1.5,
        linestyle=":",
        alpha=0.6,
        marker="s",
        markersize=5,
    )
    ax1.text(8.5, 26.0, "Forecast", fontsize=8, color=TESLA, alpha=0.7, style="italic")
    ax1.set_title(
        "8-Quarter Revenue Trend ($B)", fontsize=10, fontweight="bold", color=TESLA
    )
    ax1.set_ylabel("Revenue ($B)", fontsize=9)
    ax1.set_xticks(range(len(qs)))
    ax1.set_xticklabels(qs, fontsize=8)
    ax1.grid(axis="y", alpha=0.3)
    ax1.spines["top"].set_visible(False)
    ax1.spines["right"].set_visible(False)

    # Grouped bar: Q3 comparison 3 years
    ax2 = fig.add_axes([0.70, 0.27, 0.27, 0.38])
    years = ["2020", "2021", "2022"]
    q3_rev = [8.8, 13.8, 21.5]
    ax2.bar(years, q3_rev, color=[TESLA] * 3, alpha=0.8, width=0.5)
    for i, v in enumerate(q3_rev):
        ax2.text(i, v + 0.2, f"${v}B", ha="center", fontsize=10, fontweight="bold")
    ax2.set_title("Q3 Revenue YoY", fontsize=10, fontweight="bold", color=TESLA)
    ax2.set_ylabel("Revenue ($B)", fontsize=9)
    ax2.grid(axis="y", alpha=0.3)
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_visible(False)

    plt.savefig("good_financial.png", bbox_inches="tight", dpi=150)
    plt.close()


def good_financial_metrics():
    """Three large KPI cards: Revenue, Gross Margin, FCF with YoY delta and sparkline."""
    fig = plt.figure(figsize=(13, 5.5), facecolor="white")
    fig.text(
        0.5,
        0.97,
        "Q4 2022 — Key Financial KPIs",
        ha="center",
        va="top",
        fontsize=13,
        fontweight="bold",
        color=TESLA,
    )
    sparks = [[18.8, 16.9, 21.5, 24.3], [32.9, 27.9, 25.1, 23.8], [2.2, 1.4, 3.3, 1.4]]
    kpis = [
        ("Revenue", "$24.3B", "+36% YoY", True),
        ("Gross Margin", "23.8%", "-9.1pp YoY", False),
        ("Free Cash Flow", "$1.4B", "-57% YoY", False),
    ]
    for i, ((lbl, val, dlt, pos), sp) in enumerate(zip(kpis, sparks)):
        kpi_card(
            fig,
            0.04 + i * 0.33,
            0.10,
            0.28,
            0.76,
            lbl,
            val,
            dlt,
            pos,
            sp,
            color=TESLA,
            bg="#fff0ee",
        )
    plt.savefig("good_financial_metrics.png", bbox_inches="tight", dpi=150)
    plt.close()


def good_financial_trends():
    """8-quarter line chart, current quarter highlighted with callout, dotted forecast line."""
    fig, ax = plt.subplots(figsize=(11, 6))
    qs = ["Q1'21", "Q2'21", "Q3'21", "Q4'21", "Q1'22", "Q2'22", "Q3'22", "Q4'22"]
    rev = [10.4, 11.9, 13.8, 17.7, 18.8, 16.9, 21.5, 24.3]
    ax.plot(range(len(qs)), rev, color=TESLA, marker="o", linewidth=2.5, zorder=4)
    ax.fill_between(range(len(qs)), rev, alpha=0.12, color=TESLA)
    ax.scatter([7], [24.3], s=180, color=TESLA, zorder=6)
    ax.annotate(
        "Q4 '22: $24.3B\n▲ +13% vs Q3",
        xy=(7, 24.3),
        xytext=(5.5, 22.5),
        fontsize=10,
        color=TESLA,
        fontweight="bold",
        arrowprops=dict(arrowstyle="->", color=TESLA, lw=1.5),
        bbox=dict(boxstyle="round,pad=0.3", facecolor="#fff0ee", edgecolor=TESLA),
    )
    # Forecast
    ax.plot(
        [7, 8, 9],
        [24.3, 25.8, 27.2],
        color=TESLA,
        linewidth=1.8,
        linestyle=":",
        marker="s",
        markersize=6,
        alpha=0.65,
    )
    ax.text(
        8.05,
        25.3,
        "2-quarter forecast",
        fontsize=8.5,
        color=TESLA,
        alpha=0.75,
        style="italic",
    )
    ax.set_title(
        "Tesla Revenue — 8-Quarter Trend with Forecast ($B)",
        fontsize=12,
        fontweight="bold",
        color=TESLA,
    )
    ax.set_xticks(range(10))
    ax.set_xticklabels(list(qs) + ["Q1'23", "Q2'23"], fontsize=9)
    ax.set_ylabel("Revenue ($B)", fontsize=10)
    ax.grid(axis="y", alpha=0.3)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.tight_layout()
    plt.savefig("good_financial_trends.png", bbox_inches="tight", dpi=150)
    plt.close()


def good_financial_comparison():
    """Grouped bar chart comparing Q3 across 2020, 2021, 2022."""
    fig, ax = plt.subplots(figsize=(10, 6))
    years = ["2020", "2021", "2022"]
    q3_rev = [8.8, 13.8, 21.5]
    q3_margin = [27.7, 26.6, 25.1]
    x = np.arange(len(years))
    w = 0.35
    b1 = ax.bar(x - w / 2, q3_rev, w, label="Revenue ($B)", color=TESLA, alpha=0.85)
    b2 = ax.bar(
        x + w / 2, q3_margin, w, label="Gross Margin (%)", color="#c0392b", alpha=0.65
    )
    for bar in b1:
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.3,
            f"${bar.get_height()}B",
            ha="center",
            fontsize=10,
            fontweight="bold",
        )
    for bar in b2:
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.3,
            f"{bar.get_height():.1f}%",
            ha="center",
            fontsize=9,
            color="#c0392b",
        )
    ax.set_xticks(x)
    ax.set_xticklabels([f"Q3 {y}" for y in years], fontsize=11)
    ax.set_title(
        "Q3 Performance — Revenue & Gross Margin YoY (2020–2022)",
        fontsize=12,
        fontweight="bold",
        color=TESLA,
    )
    ax.legend(fontsize=10)
    ax.grid(axis="y", alpha=0.3)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.tight_layout()
    plt.savefig("good_financial_comparison.png", bbox_inches="tight", dpi=150)
    plt.close()


# ── USAGE ─────────────────────────────────────────────────────────────────────


def bad_usage():
    """Raw table with 15 columns — feature codes, no aggregation, no charts."""
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.axis("off")
    ax.set_title("Netflix Usage Events Export — Session-Level Data", fontsize=11, pad=8)
    np.random.seed(3)
    feature_ids = [
        "HM001",
        "SR002",
        "RC003",
        "ML004",
        "CW005",
        "NR006",
        "TR007",
        "DL008",
    ]
    cols = [
        "feature_id",
        "session_count",
        "avg_duration_sec",
        "p50_eng",
        "p95_eng",
        "total_plays",
        "unique_users",
        "ctr%",
        "skip_rate%",
        "completion%",
        "thumbs_up",
        "thumbs_down",
        "added_to_list",
        "shared",
        "downloaded",
    ]
    rows = [
        [fid] + [str(int(np.random.uniform(100, 50000))) for _ in range(len(cols) - 1)]
        for fid in feature_ids * 3
    ]
    tbl = ax.table(cellText=rows[:15], colLabels=cols, loc="center", cellLoc="center")
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(7)
    tbl.scale(1, 1.15)
    for (r, c), cell in tbl.get_celld().items():
        if r == 0:
            cell.set_facecolor("#ccc")
            cell.set_text_props(fontweight="bold", fontsize=6.5)
    plt.savefig("bad_usage.png", bbox_inches="tight", dpi=150)
    plt.close()


def bad_usage_data():
    """200 rows × 12 columns spreadsheet grid — no aggregation."""
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.axis("off")
    ax.set_title("usage_events.csv — Raw Export (200 rows shown)", fontsize=11, pad=8)
    np.random.seed(6)
    cols = [
        "user_id",
        "session_id",
        "feature_code",
        "timestamp",
        "duration_sec",
        "device_type",
        "country",
        "os",
        "app_version",
        "action_count",
        "plays",
        "errors",
    ]
    sample_rows = [
        [
            f"u{int(np.random.uniform(1e6,9e6))}",
            f"s{int(np.random.uniform(1e8,9e8))}",
            np.random.choice(["HM", "SR", "RC", "ML", "CW"]),
            f"2024-{np.random.randint(1,12):02d}-{np.random.randint(1,28):02d}",
            str(int(np.random.uniform(30, 3600))),
            np.random.choice(["mobile", "tv", "web"]),
            np.random.choice(["US", "UK", "DE", "AU"]),
            np.random.choice(["iOS", "Android", "Web"]),
            f"5.{np.random.randint(0,9)}.{np.random.randint(0,20)}",
            str(int(np.random.uniform(1, 50))),
            str(int(np.random.uniform(0, 10))),
            str(int(np.random.uniform(0, 3))),
        ]
        for _ in range(12)
    ]
    tbl = ax.table(cellText=sample_rows, colLabels=cols, loc="center", cellLoc="center")
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(7)
    tbl.scale(1, 1.4)
    for (r, c), cell in tbl.get_celld().items():
        if r == 0:
            cell.set_facecolor("#ddd")
            cell.set_text_props(fontweight="bold", fontsize=6.5)
    fig.text(
        0.5,
        0.02,
        "200 rows × 12 columns — viewer must write additional queries to extract any insight",
        ha="center",
        fontsize=9,
        color="#999",
        style="italic",
    )
    plt.savefig("bad_usage_data.png", bbox_inches="tight", dpi=150)
    plt.close()


def bad_usage_visuals():
    """Feature names and session counts as a numbered list — no bar chart."""
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.axis("off")
    fig.patch.set_facecolor("white")
    ax.set_title("Top Features by Usage — Weekly Report", fontsize=13, pad=12)
    items = [
        "1.  Homepage            — 95,000 weekly active users",
        "2.  Continue Watching  — 85,000 weekly active users",
        "3.  Recommendations    — 75,000 weekly active users",
        "4.  My List             — 60,000 weekly active users",
        "5.  Search              — 45,000 weekly active users",
        "6.  New Releases        — 40,000 weekly active users",
        "7.  Trending Now        — 32,000 weekly active users",
        "8.  Categories          — 28,000 weekly active users",
        "9.  Downloads           — 12,000 weekly active users",
        "10. Settings            —  8,000 weekly active users",
    ]
    for i, item in enumerate(items):
        ax.text(
            0.06,
            0.87 - i * 0.085,
            item,
            va="top",
            ha="left",
            fontsize=11.5,
            transform=ax.transAxes,
            color="#222",
            family="monospace",
        )
    fig.text(
        0.5,
        0.03,
        "← A 10x usage gap looks identical in a list — bar chart would show it instantly",
        ha="center",
        fontsize=9,
        color="#999",
        style="italic",
    )
    plt.savefig("bad_usage_visuals.png", bbox_inches="tight", dpi=150)
    plt.close()


def bad_usage_patterns():
    """Daily active users line chart — weekend dips present but unlabelled."""
    fig, ax = plt.subplots(figsize=(12, 5))
    np.random.seed(14)
    days = np.arange(28)
    base = 2400 + np.cumsum(np.random.normal(5, 30, 28))
    # Add weekend dips (days 5,6,12,13,19,20,26,27)
    weekends = [5, 6, 12, 13, 19, 20, 26, 27]
    for w in weekends:
        base[w] -= np.random.uniform(200, 400)
    ax.plot(days, base, color=NETFLIX, linewidth=2, marker="o", markersize=4)
    ax.fill_between(days, base, alpha=0.12, color=NETFLIX)
    ax.set_title("Daily Active Users — Last 28 Days", fontsize=12)
    ax.set_xlabel("Day")
    ax.set_ylabel("Daily Active Users")
    ax.set_xticks(days[::2])
    ax.set_xticklabels(range(1, 29, 2), fontsize=8)
    ax.grid(alpha=0.3)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    fig.text(
        0.5,
        0.01,
        "← Weekend dips visible but unexplained — viewers may interpret as bugs or data errors",
        ha="center",
        fontsize=9,
        color="#999",
        style="italic",
    )
    plt.tight_layout()
    plt.savefig("bad_usage_patterns.png", bbox_inches="tight", dpi=150)
    plt.close()


def good_usage():
    """Dashboard: sorted feature bar + Sankey-style flow + hours×days heatmap."""
    fig = plt.figure(figsize=(15, 9), facecolor="white")
    fig.text(
        0.5,
        0.97,
        "Netflix User Engagement Analytics",
        ha="center",
        va="top",
        fontsize=14,
        fontweight="bold",
        color=NETFLIX,
    )

    # ── Panel 1: Sorted feature bar with teal/gray semantic color ──
    ax1 = fig.add_axes([0.04, 0.55, 0.28, 0.36])
    features = [
        "Homepage",
        "Cont. Watch.",
        "Recommend.",
        "My List",
        "Search",
        "New Releases",
        "Downloads",
    ]
    wau = [95, 85, 75, 60, 45, 40, 12]
    idx = np.argsort(wau)
    f_s, w_s = [features[i] for i in idx], [wau[i] for i in idx]
    bar_c = [ATEAL if w >= 45 else GR for w in w_s]
    bars = ax1.barh(f_s, w_s, color=bar_c, height=0.6, alpha=0.88)
    for i, w in enumerate(w_s):
        ax1.text(w + 0.8, i, f"{w}K", va="center", fontsize=8, color=bar_c[i])
    ax1.set_title("Feature WAU (sorted)", fontsize=10, fontweight="bold", color=NETFLIX)
    ax1.set_xlabel("Weekly Active Users (K)", fontsize=8)
    ax1.spines["top"].set_visible(False)
    ax1.spines["right"].set_visible(False)
    ax1.grid(axis="x", alpha=0.3)
    handles = [
        mpatches.Patch(color=ATEAL, label="Invest"),
        mpatches.Patch(color=GR, label="Review"),
    ]
    ax1.legend(handles=handles, fontsize=8, loc="lower right")

    # ── Panel 2: Sankey-style navigation flow ──
    ax2 = fig.add_axes([0.36, 0.55, 0.30, 0.36])
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 5)
    ax2.axis("off")
    ax2.set_title(
        "Navigation Flow (path width ∝ users)",
        fontsize=10,
        fontweight="bold",
        color=NETFLIX,
    )
    nodes = [
        ("Home", 1, 2.5),
        ("Browse", 4, 4.0),
        ("Search", 4, 2.5),
        ("Recommend", 4, 1.0),
        ("Play", 7, 3.0),
        ("Exit", 7, 1.5),
    ]
    for name, x, y in nodes:
        rect = FancyBboxPatch(
            (x - 0.5, y - 0.35),
            1.5,
            0.7,
            boxstyle="round,pad=0.05",
            facecolor=NETFLIX,
            edgecolor="white",
            linewidth=1.5,
            alpha=0.85,
        )
        ax2.add_patch(rect)
        ax2.text(
            x + 0.25,
            y,
            name,
            ha="center",
            va="center",
            fontsize=8.5,
            color="white",
            fontweight="bold",
        )
    flows = [
        ("Home", "Browse", 40),
        ("Home", "Search", 25),
        ("Home", "Recommend", 20),
        ("Browse", "Play", 35),
        ("Search", "Play", 20),
        ("Recommend", "Play", 30),
        ("Browse", "Exit", 5),
        ("Search", "Exit", 5),
        ("Recommend", "Exit", 10),
    ]
    node_pos = {name: (x, y) for name, x, y in nodes}
    for src, dst, vol in flows:
        sx, sy = node_pos[src]
        dx, dy = node_pos[dst]
        lw = vol / 8
        ax2.annotate(
            "",
            xy=(dx - 0.5, dy),
            xytext=(sx + 1.0, sy),
            arrowprops=dict(arrowstyle="->", color="#888", lw=lw, alpha=0.7),
        )
        mx, my = (sx + dx) / 2, (sy + dy) / 2
        ax2.text(mx + 0.5, my, f"{vol}K", fontsize=7, color="#555", ha="center")

    # ── Panel 3: Heatmap hours×days ──
    ax3 = fig.add_axes([0.69, 0.55, 0.28, 0.36])
    np.random.seed(7)
    days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    hours = [f"{h}:00" for h in [8, 10, 12, 14, 16, 18, 20, 22]]
    data = np.random.uniform(20, 80, (len(hours), len(days_of_week)))
    data[5:7, 4:6] *= 1.8  # Fri/Sat evening peak
    data[5:7, 4:6] = np.clip(data[5:7, 4:6], 0, 100)
    data[0:2, :] *= 0.5  # morning low
    im = ax3.imshow(data, aspect="auto", cmap="Reds", vmin=0, vmax=100)
    ax3.set_xticks(range(len(days_of_week)))
    ax3.set_xticklabels(days_of_week, fontsize=8)
    ax3.set_yticks(range(len(hours)))
    ax3.set_yticklabels(hours, fontsize=8)
    ax3.set_title(
        "Sessions by Hour × Day\n(dark = peak)",
        fontsize=10,
        fontweight="bold",
        color=NETFLIX,
    )
    plt.colorbar(im, ax=ax3, label="Relative Volume", shrink=0.8)

    # ── Bottom summary row ──
    ax4 = fig.add_axes([0.04, 0.08, 0.93, 0.40])
    ax4.axis("off")
    insights = [
        (
            "Top Insight",
            "• Homepage → Play is the dominant path (40K users direct)\n• Continue Watching drives highest engagement time\n• Downloads: 12K WAU — lowest by far",
        ),
        (
            "Recommendations",
            "• Invest in Recommendations & Continue Watching\n• Redesign discovery for Downloads (12K WAU → target 40K)\n• Schedule push notifications before Fri/Sat 8 PM peak",
        ),
        (
            "Peak Engagement",
            "• Fri/Sat 8–10 PM: highest volume window\n• Monday mornings: lowest engagement\n• Promotions should launch Wed to peak on weekend",
        ),
    ]
    for i, (title, body) in enumerate(insights):
        x = 0.01 + i * 0.34
        rect = FancyBboxPatch(
            (x, 0.05),
            0.30,
            0.90,
            boxstyle="round,pad=0.01",
            facecolor="#fff5f5",
            edgecolor=NETFLIX,
            linewidth=1.5,
            transform=ax4.transAxes,
            clip_on=False,
        )
        ax4.add_patch(rect)
        ax4.text(
            x + 0.15,
            0.88,
            title,
            ha="center",
            va="center",
            fontsize=9,
            fontweight="bold",
            color=NETFLIX,
            transform=ax4.transAxes,
        )
        ax4.text(
            x + 0.15,
            0.50,
            body,
            ha="center",
            va="center",
            fontsize=8.5,
            color="#333",
            transform=ax4.transAxes,
            multialignment="left",
            linespacing=1.6,
        )
    plt.savefig("good_usage.png", bbox_inches="tight", dpi=150)
    plt.close()


def good_usage_flow():
    """Sankey-style diagram: Home/Search/Browse/Recommend → Play/Exit."""
    fig, ax = plt.subplots(figsize=(13, 7))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 7)
    ax.axis("off")
    ax.set_title(
        "Netflix Navigation Flow — Path Width ∝ Users",
        fontsize=12,
        fontweight="bold",
        color=NETFLIX,
    )
    fig.patch.set_facecolor("white")

    nodes = [
        ("Home", 0.5, 3.5),
        ("Browse", 4.0, 5.0),
        ("Search", 4.0, 3.5),
        ("Recommend", 4.0, 2.0),
        ("Play", 8.5, 3.5),
        ("Exit", 8.5, 1.5),
    ]
    for name, x, y in nodes:
        rect = FancyBboxPatch(
            (x, y - 0.4),
            2.0,
            0.8,
            boxstyle="round,pad=0.08",
            facecolor=NETFLIX,
            edgecolor="white",
            linewidth=2,
            alpha=0.9,
        )
        ax.add_patch(rect)
        ax.text(
            x + 1.0,
            y,
            name,
            ha="center",
            va="center",
            fontsize=11,
            color="white",
            fontweight="bold",
        )

    # Flow arrows with proportional linewidths
    flows = [
        ("Home", "Browse", 40, "#555"),
        ("Home", "Search", 25, "#666"),
        ("Home", "Recommend", 20, "#777"),
        ("Browse", "Play", 35, NETFLIX),
        ("Search", "Play", 20, NETFLIX),
        ("Recommend", "Play", 30, NETFLIX),
        ("Browse", "Exit", 5, "#aaa"),
        ("Search", "Exit", 5, "#aaa"),
        ("Recommend", "Exit", 10, "#aaa"),
    ]
    npos = {n: (x + 2.0, y) for n, x, y in nodes}
    npos_l = {n: (x, y) for n, x, y in nodes}

    for src, dst, vol, col in flows:
        sx, sy = npos[src]
        dx, dy = npos_l[dst]
        lw = max(1, vol / 6)
        ax.annotate(
            "",
            xy=(dx, dy),
            xytext=(sx, sy),
            arrowprops=dict(
                arrowstyle="->",
                color=col,
                lw=lw,
                alpha=0.75,
                connectionstyle="arc3,rad=0.05",
            ),
        )
        mx, my = (sx + dx) / 2, (sy + dy) / 2 + 0.15
        ax.text(
            mx,
            my,
            f"{vol}K",
            fontsize=9,
            color=col,
            ha="center",
            bbox=dict(
                boxstyle="round,pad=0.2", facecolor="white", edgecolor=col, alpha=0.8
            ),
        )

    ax.text(
        1.5,
        0.3,
        "← Widest arrow: Home → Browse (40K) shows dominant path",
        fontsize=9.5,
        color="#555",
        style="italic",
    )
    plt.tight_layout()
    plt.savefig("good_usage_flow.png", bbox_inches="tight", dpi=150)
    plt.close()


def good_usage_features():
    """Horizontal bar chart sorted descending, top 3 teal, bottom 2 gray."""
    fig, ax = plt.subplots(figsize=(10, 6))
    features = [
        "Homepage",
        "Cont. Watching",
        "Recommend.",
        "My List",
        "Search",
        "New Releases",
        "Downloads",
    ]
    wau = [95, 85, 75, 60, 45, 40, 12]
    idx = np.argsort(wau)[::-1]
    f_s, w_s = [features[i] for i in idx], [wau[i] for i in idx]
    bar_c = [ATEAL] * 3 + ["#95a5a6"] * 2 + [GR] * 2
    bars = ax.barh(f_s[::-1], w_s[::-1], color=bar_c[::-1], height=0.55, alpha=0.88)
    for i, w in enumerate(w_s[::-1]):
        c = ATEAL if w >= 45 else GR
        ax.text(
            w + 0.8,
            len(w_s) - 1 - i,
            f"{w}K WAU",
            va="center",
            fontsize=9.5,
            color=c,
            fontweight="bold",
        )
    ax.set_title(
        "Netflix Features — Weekly Active Users (sorted)",
        fontsize=12,
        fontweight="bold",
        color=NETFLIX,
    )
    ax.set_xlabel("Weekly Active Users (thousands)", fontsize=10)
    ax.set_xlim(0, 115)
    handles = [
        mpatches.Patch(color=ATEAL, label="Invest (top 3 by WAU)"),
        mpatches.Patch(color=GR, label="Deprioritize (bottom)"),
    ]
    ax.legend(handles=handles, fontsize=10, loc="lower right")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis="x", alpha=0.3)
    plt.tight_layout()
    plt.savefig("good_usage_features.png", bbox_inches="tight", dpi=150)
    plt.close()


def good_usage_patterns():
    """Heatmap: sessions by hour of day (y) × day of week (x). Fri/Sat evenings darkest."""
    fig, ax = plt.subplots(figsize=(11, 7))
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    hours = [f"{h}:00" for h in [6, 8, 10, 12, 14, 16, 18, 20, 22]]
    np.random.seed(20)
    data = np.random.uniform(15, 60, (len(hours), len(days)))
    # Fri/Sat evenings (idx 4,5) at hours 18-22 (idx 6,7,8) are peak
    data[6:9, 4:6] = np.random.uniform(75, 100, (3, 2))
    # Mon mornings low
    data[0:3, 0] = np.random.uniform(5, 20, 3)
    im = ax.imshow(data, aspect="auto", cmap="Reds", vmin=0, vmax=100)
    ax.set_xticks(range(len(days)))
    ax.set_xticklabels(days, fontsize=11)
    ax.set_yticks(range(len(hours)))
    ax.set_yticklabels(hours, fontsize=11)
    ax.set_title(
        "Netflix Streaming Sessions — Hour of Day × Day of Week",
        fontsize=12,
        fontweight="bold",
        color=NETFLIX,
    )
    ax.set_xlabel("Day of Week", fontsize=10)
    ax.set_ylabel("Hour of Day", fontsize=10)
    cb = plt.colorbar(im, ax=ax, label="Relative Session Volume")
    # Annotate peaks
    ax.annotate(
        "Peak\n8–10 PM\nFri/Sat",
        xy=(4.5, 7.5),
        xytext=(1.5, 5.5),
        fontsize=9.5,
        color=NETFLIX,
        fontweight="bold",
        arrowprops=dict(arrowstyle="->", color=NETFLIX, lw=1.5),
        bbox=dict(boxstyle="round,pad=0.3", facecolor="#fff0ee", edgecolor=NETFLIX),
    )
    ax.annotate(
        "Low Mon\nmornings",
        xy=(0, 0.5),
        xytext=(2.0, 1.0),
        fontsize=8.5,
        color="#555",
        arrowprops=dict(arrowstyle="->", color="#999", lw=1.2),
    )
    plt.tight_layout()
    plt.savefig("good_usage_patterns.png", bbox_inches="tight", dpi=150)
    plt.close()


# ── BEFORE/AFTER SUMMARY ──────────────────────────────────────────────────────


def before_after_example():
    """Side-by-side summary of before/after across all 5 case studies."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 7))
    for ax in axes:
        ax.axis("off")
    fig.patch.set_facecolor("white")
    fig.suptitle(
        "The Before/After Pattern — Consistent Across All 5 Case Studies",
        fontsize=13,
        fontweight="bold",
        y=0.97,
    )

    before = [
        "✗  50+ KPIs, random colors, no hierarchy",
        "✗  Text-heavy, no visual flow or funnel",
        "✗  Raw 20-row table, no story, no benchmark",
        "✗  80 financial cells, trends buried in prose",
        "✗  200-row CSV, numbered list, no annotations",
    ]
    after = [
        "✓  5 KPI cards + sparklines + semantic color",
        "✓  Visual funnel, color-coded, drop-off callout",
        "✓  Horizontal ROAS bar, narrative headline, rec.",
        "✓  3 KPI cards, 8-quarter trend, YoY grouped bar",
        "✓  Sorted bar (teal/gray), Sankey, hours heatmap",
    ]

    ax_l, ax_r = axes
    # Left: before
    ax_l.set_title(
        "BEFORE — Common Problems", fontsize=12, color=R, fontweight="bold", pad=10
    )
    rect_l = FancyBboxPatch(
        (0.04, 0.05),
        0.92,
        0.88,
        boxstyle="round,pad=0.01",
        facecolor="#fff5f5",
        edgecolor=R,
        linewidth=2,
        transform=ax_l.transAxes,
        clip_on=False,
    )
    ax_l.add_patch(rect_l)
    for i, line in enumerate(before):
        ax_l.text(
            0.07,
            0.82 - i * 0.16,
            line,
            va="top",
            ha="left",
            fontsize=11,
            transform=ax_l.transAxes,
            color="#333",
        )
    topics = ["Dashboard", "Journey", "Campaign", "Financial", "Usage"]
    for i, t in enumerate(topics):
        ax_l.text(
            0.07,
            0.86 - i * 0.16,
            f"Case {i+1}: {t}",
            va="top",
            ha="left",
            fontsize=9,
            color=R,
            style="italic",
            transform=ax_l.transAxes,
        )

    # Right: after
    ax_r.set_title(
        "AFTER — Three Consistent Fixes",
        fontsize=12,
        color=G,
        fontweight="bold",
        pad=10,
    )
    rect_r = FancyBboxPatch(
        (0.04, 0.05),
        0.92,
        0.88,
        boxstyle="round,pad=0.01",
        facecolor="#f0fff4",
        edgecolor=G,
        linewidth=2,
        transform=ax_r.transAxes,
        clip_on=False,
    )
    ax_r.add_patch(rect_r)
    for i, line in enumerate(after):
        ax_r.text(
            0.07,
            0.82 - i * 0.16,
            line,
            va="top",
            ha="left",
            fontsize=11,
            transform=ax_r.transAxes,
            color="#333",
        )
        ax_r.text(
            0.07,
            0.86 - i * 0.16,
            f"Case {i+1}: {topics[i]}",
            va="top",
            ha="left",
            fontsize=9,
            color=G,
            style="italic",
            transform=ax_r.transAxes,
        )

    # Three principles at bottom
    fig.text(
        0.5,
        0.04,
        "FOCUS (show less, show what matters)   ·   CONTEXT (add comparisons & benchmarks)   ·   ACTION (end with a recommendation)",
        ha="center",
        fontsize=10,
        color="#444",
        fontweight="bold",
    )

    plt.savefig("before_after_example.png", bbox_inches="tight", dpi=150)
    plt.close()


if __name__ == "__main__":
    import os

    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print("Generating dashboard images...")
    bad_dashboard()
    good_dashboard()
    bad_dashboard_metrics()
    good_dashboard_metrics()
    bad_dashboard_colors()
    good_dashboard_colors()
    bad_dashboard_hierarchy()
    good_dashboard_hierarchy()

    print("Generating journey images...")
    bad_journey()
    good_journey()
    bad_journey_text()
    good_journey_flow()
    bad_journey_metrics()
    good_journey_metrics()
    bad_journey_flow()
    good_journey_insights()

    print("Generating campaign images...")
    bad_campaign()
    good_campaign()
    bad_campaign_data()
    good_campaign_narrative()
    bad_campaign_story()
    good_campaign_comparisons()
    bad_campaign_context()
    good_campaign_roi()

    print("Generating financial images...")
    bad_financial()
    good_financial()
    bad_financial_numbers()
    good_financial_metrics()
    bad_financial_visuals()
    good_financial_trends()
    bad_financial_context()
    good_financial_comparison()

    print("Generating usage images...")
    bad_usage()
    good_usage()
    bad_usage_data()
    good_usage_flow()
    bad_usage_visuals()
    good_usage_features()
    bad_usage_patterns()
    good_usage_patterns()

    print("Generating before/after...")
    before_after_example()

    print("Done.")
