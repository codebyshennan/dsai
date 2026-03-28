"""Generate educational diagrams for the SQL module."""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path

OUT = Path(__file__).parent

plt.rcParams.update({
    "font.family": "monospace",
    "figure.dpi": 120,
})

# ── helpers ───────────────────────────────────────────────────────────────────
def table_box(ax, x, y, title, cols, width=2.8, row_h=0.38, header_color="#2171b5"):
    """Draw a simple table diagram at (x, y)."""
    n = len(cols)
    total_h = row_h * (n + 1)
    # Header
    hdr = FancyBboxPatch((x, y - row_h), width, row_h,
                          boxstyle="square,pad=0", fc=header_color, ec="#555", lw=1.2)
    ax.add_patch(hdr)
    ax.text(x + width / 2, y - row_h / 2, title,
            ha="center", va="center", fontsize=9, fontweight="bold", color="white")
    # Rows
    for i, (col, is_pk, is_fk) in enumerate(cols):
        bg = "#eaf3fb" if i % 2 == 0 else "#f7f7f7"
        row = FancyBboxPatch((x, y - row_h * (i + 2)), width, row_h,
                              boxstyle="square,pad=0", fc=bg, ec="#ccc", lw=0.8)
        ax.add_patch(row)
        icon = "PK " if is_pk else ("FK " if is_fk else "   ")
        label = f"{icon}{col}"
        ax.text(x + 0.12, y - row_h * (i + 2) + row_h / 2, label,
                ha="left", va="center", fontsize=8,
                color="#c94040" if is_pk else ("#2171b5" if is_fk else "#333"))
    return total_h


# ── 1. relational_model.png ───────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(9, 5))
ax.set_xlim(0, 9)
ax.set_ylim(0, 5)
ax.axis("off")
ax.set_title("Relational Model: Tables and Keys", fontsize=12, fontweight="bold",
             fontfamily="sans-serif", pad=10)

# customers table
table_box(ax, 0.4, 4.5, "customers",
          [("customer_id (PK)", True, False),
           ("name", False, False),
           ("email", False, False),
           ("created_at", False, False)],
          header_color="#2171b5")

# orders table
table_box(ax, 5.8, 4.5, "orders",
          [("order_id (PK)", True, False),
           ("customer_id (FK)", False, True),
           ("amount", False, False),
           ("order_date", False, False)],
          header_color="#2ca25f")

# Arrow FK → PK
ax.annotate("", xy=(5.8, 3.74), xytext=(3.2, 3.74),
            arrowprops=dict(arrowstyle="-|>", color="#888", lw=1.8,
                            connectionstyle="arc3,rad=0."))
ax.text(4.5, 3.95, "FK → PK\n1 customer : many orders",
        ha="center", va="center", fontsize=8, color="#555",
        fontfamily="sans-serif")

# Legend
legend_items = [
    mpatches.Patch(color="#2171b5", label="Primary Key (PK) — unique row identifier"),
    mpatches.Patch(color="#2ca25f", label="Foreign Key (FK) — links to another table"),
]
ax.legend(handles=legend_items, loc="lower center", fontsize=8,
          frameon=True, ncol=2, bbox_to_anchor=(0.5, 0.0))

plt.tight_layout()
plt.savefig(OUT / "relational_model.png", bbox_inches="tight")
plt.close()
print("Saved relational_model.png")


# ── 2. join_types.png ─────────────────────────────────────────────────────────
fig, axes = plt.subplots(2, 2, figsize=(10, 7))
fig.suptitle("SQL Join Types", fontsize=13, fontweight="bold",
             fontfamily="sans-serif", y=0.98)

join_configs = [
    ("INNER JOIN", "#2171b5", "#2ca25f", "Only matching rows\nin both tables",
     [True, True, True, False, False, False]),
    ("LEFT JOIN", "#2171b5", "#2ca25f", "All rows from LEFT table;\nNULL where no match on right",
     [True, True, True, True, True, True]),
    ("RIGHT JOIN", "#2171b5", "#2ca25f", "All rows from RIGHT table;\nNULL where no match on left",
     [True, True, True, False, False, False]),
    ("FULL OUTER JOIN", "#2171b5", "#2ca25f", "All rows from both tables;\nNULL where no match",
     [True, True, True, True, True, True]),
]

sample_left = ["L1", "L2", "L3", "L4"]
sample_right = ["R2", "R3", "R5", "R6"]  # L2/L3 match, L1/L4 don't

for ax, (title, lc, rc, desc, _) in zip(axes.flat, join_configs):
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 5)
    ax.axis("off")
    ax.set_title(title, fontsize=10, fontweight="bold", fontfamily="sans-serif")

    # Left circle
    circ_l = plt.Circle((2.0, 2.6), 1.3, fc=lc, ec="white", alpha=0.4, lw=1.5)
    ax.add_patch(circ_l)
    # Right circle
    circ_r = plt.Circle((4.0, 2.6), 1.3, fc=rc, ec="white", alpha=0.4, lw=1.5)
    ax.add_patch(circ_r)

    # Highlight logic
    is_inner = "INNER" in title
    is_left = "LEFT" in title and "FULL" not in title
    is_right = "RIGHT" in title and "FULL" not in title
    is_full = "FULL" in title

    if is_inner or is_left or is_right or is_full:
        # Always highlight intersection
        inter = plt.Circle((3.0, 2.6), 0.65, fc="#f7c948", ec="none", alpha=0.75)
        ax.add_patch(inter)
    if is_left or is_full:
        left_only = plt.Circle((1.8, 2.6), 0.85, fc=lc, ec="none", alpha=0.75)
        ax.add_patch(left_only)
    if is_right or is_full:
        right_only = plt.Circle((4.2, 2.6), 0.85, fc=rc, ec="none", alpha=0.75)
        ax.add_patch(right_only)

    ax.text(1.4, 2.6, "Left\ntable", ha="center", va="center",
            fontsize=7.5, fontfamily="sans-serif", color="white", fontweight="bold")
    ax.text(4.6, 2.6, "Right\ntable", ha="center", va="center",
            fontsize=7.5, fontfamily="sans-serif", color="white", fontweight="bold")
    ax.text(3.0, 0.5, desc, ha="center", va="center", fontsize=8,
            fontfamily="sans-serif", color="#333")

plt.tight_layout()
plt.savefig(OUT / "join_types.png", bbox_inches="tight")
plt.close()
print("Saved join_types.png")


# ── 3. query_execution_order.png ──────────────────────────────────────────────
steps = [
    ("1  FROM / JOIN", "#2171b5", "Identify source tables\nand join them"),
    ("2  WHERE", "#6baed6", "Filter individual rows"),
    ("3  GROUP BY", "#74c476", "Group rows for aggregation"),
    ("4  HAVING", "#31a354", "Filter groups"),
    ("5  SELECT", "#fd8d3c", "Choose columns,\napply expressions"),
    ("6  DISTINCT", "#e6550d", "Remove duplicate rows"),
    ("7  ORDER BY", "#9e9ac8", "Sort results"),
    ("8  LIMIT / OFFSET", "#756bb1", "Return N rows"),
]

fig, ax = plt.subplots(figsize=(5, 8))
ax.set_xlim(0, 5)
ax.set_ylim(0, len(steps) * 1.1 + 0.3)
ax.axis("off")
ax.set_title("SQL Query Execution Order", fontsize=12, fontweight="bold",
             fontfamily="sans-serif", pad=12)

for i, (label, color, note) in enumerate(reversed(steps)):
    y = i * 1.1 + 0.2
    box = FancyBboxPatch((0.3, y), 4.4, 0.85, boxstyle="round,pad=0.06",
                          fc=color, ec="white", lw=1.5, alpha=0.88)
    ax.add_patch(box)
    ax.text(2.5, y + 0.43, label, ha="center", va="center",
            fontsize=9, fontweight="bold", color="white", fontfamily="sans-serif")
    ax.text(2.5, y + 0.18, note, ha="center", va="center",
            fontsize=7, color="white", alpha=0.9, fontfamily="sans-serif")
    if i < len(steps) - 1:
        ax.annotate("", xy=(2.5, y + 0.85), xytext=(2.5, y + 1.1),
                    arrowprops=dict(arrowstyle="-|>", color="#888", lw=1.2))

plt.tight_layout()
plt.savefig(OUT / "query_execution_order.png", bbox_inches="tight")
plt.close()
print("Saved query_execution_order.png")


# ── 4. index_scan_vs_seq.png ──────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(10, 4.5))
fig.suptitle("Sequential Scan vs Index Scan", fontsize=12, fontweight="bold",
             fontfamily="sans-serif")

row_data = [10, 23, 7, 45, 31, 8, 51, 3, 99, 17]
target = 51
target_idx = row_data.index(target)

for ax, (title, highlight_all) in zip(axes, [("Sequential Scan\n(no index)", True),
                                               ("Index Scan\n(B-Tree index on id)", False)]):
    ax.set_xlim(0, 6)
    ax.set_ylim(0, len(row_data) * 0.55 + 0.3)
    ax.axis("off")
    ax.set_title(title, fontsize=10, fontweight="bold", fontfamily="sans-serif")

    for i, val in enumerate(row_data):
        y = (len(row_data) - i - 1) * 0.55 + 0.2
        if highlight_all:
            color = "#e8967a" if val == target else "#c6dbef"
            ec = "#c94040" if val == target else "#9ecae1"
        else:
            color = "#e8967a" if val == target else "#f7f7f7"
            ec = "#c94040" if val == target else "#ccc"
            if i != target_idx and not highlight_all:
                color = "#f7f7f7"
                ec = "#ddd"

        box = FancyBboxPatch((0.5, y), 2.2, 0.42, boxstyle="square,pad=0",
                              fc=color, ec=ec, lw=1)
        ax.add_patch(box)
        ax.text(1.6, y + 0.21, f"id = {val}", ha="center", va="center",
                fontsize=8, fontfamily="monospace",
                color="#333" if val != target else "#c94040",
                fontweight="bold" if val == target else "normal")

    if highlight_all:
        ax.text(3.5, len(row_data) * 0.55 / 2 + 0.3,
                "Reads EVERY\nrow: O(n)", ha="center", va="center",
                fontsize=9, color="#c94040", fontfamily="sans-serif")
    else:
        ax.text(3.5, len(row_data) * 0.55 / 2 + 0.3,
                "Jumps directly\nto id=51: O(log n)", ha="center", va="center",
                fontsize=9, color="#2ca25f", fontfamily="sans-serif")
        # Arrow pointing to target
        ty = (len(row_data) - target_idx - 1) * 0.55 + 0.2 + 0.21
        ax.annotate("", xy=(2.7, ty), xytext=(3.2, ty),
                    arrowprops=dict(arrowstyle="-|>", color="#2ca25f", lw=1.5))

plt.tight_layout()
plt.savefig(OUT / "index_scan_vs_seq.png", bbox_inches="tight")
plt.close()
print("Saved index_scan_vs_seq.png")

print("\nAll SQL assets generated.")
