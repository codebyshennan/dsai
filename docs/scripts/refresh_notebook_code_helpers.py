#!/usr/bin/env python3
"""Tutorial notebook helpers: execution-focused explanations.

**What to write:** Use **`What this code does:`** (or **`What you should write:`** for exercises)
with bullets that walk through the actual steps, variables, and outputs—**not** generic
**Purpose:** paragraphs that restate learning objectives without tying to the snippet.

**Linear algebra:** A clean notebook (no helpers) gets markdown inserted automatically
(`bootstrap_linalg_helpers`). Re-running updates text from the `LINALG` dict by heading.

**Pandas:** Exercise 2/3 helpers are matched by heading (`**Exercise 2**`, …) so cell indices
cannot drift.

Run from docs/:  uv run python scripts/refresh_notebook_code_helpers.py
"""

from __future__ import annotations

import json
from pathlib import Path


def lines_to_source(lines: list[str]) -> list[str]:
    return [f"{line}\n" for line in lines]


def replace_markdown_by_index(nb: dict, updates: dict[int, list[str]]) -> None:
    for idx, lines in updates.items():
        cell = nb["cells"][idx]
        if cell.get("cell_type") != "markdown":
            raise ValueError(
                f"Expected markdown at index {idx}, got {cell.get('cell_type')}"
            )
        cell["source"] = lines_to_source(lines)


def replace_markdown_by_heading(nb: dict, heading_first_line: str, lines: list[str]) -> None:
    """Replace the first markdown cell whose first line matches `heading_first_line`."""
    for cell in nb["cells"]:
        if cell.get("cell_type") != "markdown":
            continue
        src = cell.get("source", [])
        if not src:
            continue
        first = src[0].strip() if isinstance(src[0], str) else ""
        if first == heading_first_line.strip():
            cell["source"] = lines_to_source(lines)
            return
    raise KeyError(f"No markdown cell with heading {heading_first_line!r}")


def insert_cell(nb: dict, index: int, lines: list[str]) -> None:
    nb["cells"].insert(
        index, {"cell_type": "markdown", "metadata": {}, "source": lines_to_source(lines)}
    )


# --- Pandas: key = cell index of markdown cell to replace ---
PANDAS: dict[int, list[str]] = {
    6: [
        "**Custom index, selection, and boolean masks**",
        "",
        "**What this code does:**",
        "- Builds `grades_labeled` from the same four scores as before, but passes `index=['Alice', 'Bob', 'Charlie', 'David']` so the row labels are names instead of 0..3.",
        "- Prints the whole Series, then selects one value with `grades_labeled['Charlie']` (label-based lookup, not position).",
        "- Computes `grades_labeled >= 90`, which returns a boolean Series aligned to the index, and passes it into `[ ]` to keep only rows where the value is True—so you see Alice and Charlie.",
    ],
    8: [
        "**Series from a dictionary**",
        "",
        "**What this code does:**",
        "- Calls `pd.Series({...})` with student names as keys and grades as values; pandas turns keys into the index and values into the Series values.",
        "- Prints the result—same labels as the previous cell, but the data came from a mapping instead of a list + index.",
    ],
    10: [
        "**Dictionary data with an explicit index order**",
        "",
        "**What this code does:**",
        "- Builds a population Series from a dict of city → millions, then passes `index=['New York', 'Tokyo', 'London', 'Paris']` to force row order and membership (same four cities, but ordered as listed).",
        "- Prints the Series, then prints `population.mean()`—the arithmetic mean of the four displayed values.",
    ],
    14: [
        "**Build a DataFrame from column-wise lists**",
        "",
        "**What this code does:**",
        "- Builds `data` as a dict: each key becomes a column name, each value is a list of cell values; row `i` is built from the `i`-th entry of every list.",
        "- Calls `pd.DataFrame(data)` and prints `\"DataFrame:\"`; the last expression `df` makes Jupyter render the HTML table.",
    ],
    16: [
        "**Select columns by dtype**",
        "",
        "**What this code does:**",
        "- Runs `df.select_dtypes(exclude=['number'])` on the current `df`, which returns only columns whose dtype is not numeric (e.g. `Name`, `City` if they are object strings).",
    ],
    18: [
        "**Shape, column names, and dtypes**",
        "",
        "**What this code does:**",
        "- Prints `df.shape` (rows, columns), `list(df.columns)`, and `df.dtypes` so you see dimensions, column names, and storage type per column.",
    ],
    20: [
        "**`info()` and `describe()`**",
        "",
        "**What this code does:**",
        "- Calls `df.info()` to print row counts, column names, dtypes, and non-null counts.",
        "- Calls `df.describe()` to summarize numeric columns (count, mean, std, min, quartiles, max) and returns it so Jupyter displays the summary table.",
    ],
    22: [
        "**Column order and subset of columns**",
        "",
        "**What this code does:**",
        "- Rebuilds a DataFrame from the same `data` dict but passes `columns=[\"Name\", \"Salary\", \"Age\", \"City\"]` to pick columns and set their left-to-right order (here `Salary` comes before `Age`).",
        "- Displays `df2` as the last value in the cell.",
    ],
    24: [
        "**The `Index` object**",
        "",
        "**What this code does:**",
        "- Creates `obj` as a short Series with labels `a`, `b`, `c`, then assigns `index = obj.index` and evaluates `index` so Jupyter shows the Index object’s contents.",
    ],
    26: [
        "**Slicing an Index**",
        "",
        "**What this code does:**",
        "- Takes the Index from the previous cell and applies `index[1:]`, which returns a new Index containing the labels from position 1 onward (`b`, `c` for string labels).",
    ],
    28: [
        "**Constructing a `pd.Index`**",
        "",
        "**What this code does:**",
        "- Builds `labels = pd.Index(np.arange(1, 4))`, so the index holds integer labels `1`, `2`, `3`, and displays that `Index` object.",
    ],
    30: [
        "**Align a Series to a prepared Index**",
        "",
        "**What this code does:**",
        "- Creates `obj2` with values `[1.5, -2.5, 0]` and uses the `labels` Index from the previous cell as its index—so the first value is paired with `1`, the second with `2`, etc.",
        "- Displays `obj2`.",
    ],
    34: [
        "**Row `reindex` introduces missing rows**",
        "",
        "**What this code does:**",
        "- Starts from `frame` (3×3 with rows `a`, `c`, `d`).",
        "- Calls `frame.reindex(['a', 'b', 'c', 'd'])` to force row order `a`–`d`; row `b` did not exist, so that row is filled with NaN.",
        "- Prints `frame2.dtypes` to show dtypes after reindexing.",
    ],
    36: [
        "**Original `frame` reference**",
        "",
        "**What this code does:**",
        "- Evaluates `frame` again so you can compare the original 3×3 matrix to the reindexed variants in surrounding cells.",
    ],
    38: [
        "**Column `reindex`**",
        "",
        "**What this code does:**",
        "- Defines `states = [\"Texas\", \"Utah\", \"California\"]` and calls `frame.reindex(columns=states)` so columns are exactly those three names in that order; any column not present in `frame` (e.g. `Utah`) becomes all NaN.",
        "- Displays `frame3`.",
    ],
    40: [
        "**`reindex` with `axis=`**",
        "",
        "**What this code does:**",
        "- Calls `frame.reindex([\"a\",\"b\",\"c\",\"d\"], axis=\"index\")` to reindex rows explicitly (same idea as `frame.reindex([...])` but axis is spelled out).",
        "- Displays `frame4`.",
    ],
    42: [
        "**Mixed dtypes and memory**",
        "",
        "**What this code does:**",
        "- Builds `df_types` with int, string, float, and `pd.Categorical` columns.",
        "- Prints `df_types.dtypes`, then `df_types.memory_usage(deep=True)` so you see bytes per column (with `deep=True` for object/category columns).",
    ],
    44: [
        "**Set and reset the index**",
        "",
        "**What this code does:**",
        "- Builds `sales_idx` with a month index and prints one element by label (`sales_idx['Feb']`).",
        "- Builds `df_city`, then `set_index('City')` moves `City` into the row index; prints `reset_index()` to move it back to a column.",
    ],
    48: [
        "**Drop columns and rows**",
        "",
        "**What this code does:**",
        "- Builds a small `df_drop` with columns `name`, `grade`, `extra`.",
        "- Prints `df_drop.drop('extra', axis=1)` (drop column) and `df_drop.drop(0)` (drop row label `0`).",
    ],
    50: [
        "**Series before `drop`**",
        "",
        "**What this code does:**",
        "- Creates `obj` = `0.`..`4.` with index labels `a`–`e` and displays it—this object is the starting point for the next `drop` calls.",
    ],
    52: [
        "**Drop one row label**",
        "",
        "**What this code does:**",
        "- Calls `obj.drop(\"c\")`, which returns a new Series without label `c` (values `0`–`4` remain for the other labels).",
        "- Displays `new_obj`.",
    ],
    54: [
        "**Drop multiple labels**",
        "",
        "**What this code does:**",
        "- Calls `obj.drop([\"d\", \"c\"])` to remove two index labels in one call; returns a Series with only `a`, `b`, `e`.",
        "- Displays `new_obj2`.",
    ],
    56: [
        "**4x4 DataFrame for `drop`**",
        "",
        "**What this code does:**",
        "- Builds `data` as a 4×4 integer grid with column names `one`…`four` and displays it.",
    ],
    58: [
        "**Drop rows by index values**",
        "",
        "**What this code does:**",
        "- Calls `data.drop(index=np.arange(1,4))` to drop rows whose index labels are `1`, `2`, and `3`, leaving only row `0` (and the four columns).",
        "- Displays `data1`.",
    ],
    62: [
        "**`fill_value` and `combine_first`**",
        "",
        "**What this code does:**",
        "- Builds two overlapping DataFrames `df1` and `df2` on different index sets.",
        "- Prints `df1.add(df2, fill_value=0)` so missing pairs in the aligned add are treated as 0 before addition.",
        "- Builds `primary` and `secondary` with NaNs in `primary`, then prints `primary.combine_first(secondary)` to fill NaNs from `secondary` where `primary` is missing.",
    ],
    66: [
        "**`map` on a Series**",
        "",
        "**What this code does:**",
        "- Creates `codes` with product codes and a `names` dict mapping each code to a product name.",
        "- Prints `codes.map(names).tolist()`—each element is replaced by the dict value, producing `['Laptop', 'Mouse', 'Keyboard']`.",
    ],
    70: [
        "**Sort by one or more columns**",
        "",
        "**What this code does:**",
        "- Prints the top 5 rows by `Sales` descending via `sort_values('Sales', ascending=False).head()`.",
        "- Prints a multi-key sort: `sort_values(['Region', 'Sales'], ascending=[True, False])` so regions are alphabetical and within each region sales are highest-first.",
    ],
    72: [
        "**Ranking and `nlargest`**",
        "",
        "**What this code does:**",
        "- On `scores`, prints `rank()` and `rank(method='min')` so you see how tie-breaking changes the rank numbers.",
        "- Prints `sales.nlargest(3, 'Sales')`—the three rows with the largest `Sales` without sorting the full table.",
    ],
}

PANDAS_EXERCISES: dict[str, list[str]] = {
    "**Exercise 2**": [
        "**Exercise 2**",
        "",
        "**What you should write:**",
        "- Add a new column (e.g. `sales['Rank']`) equal to `sales['Sales'].rank(ascending=False)` so the largest sale gets rank 1 (adjust `ascending` if your prompt asks otherwise).",
    ],
    "**Exercise 3**": [
        "**Exercise 3**",
        "",
        "**What you should write:**",
        "- Build a `Series` with a gap in the index (e.g. only `Jan` and `Mar`), then `reindex` to include `Feb` and use `.ffill()` so the missing month fills from the previous value.",
    ],
}

PANDAS_INSERT_EX1: list[str] = [
    "**Exercise 1**",
    "",
    "**What you should write:**",
    "- Call `sales.sort_values(['Region', 'Sales'], ascending=[True, False])` so rows are sorted first by `Region` ascending, then by `Sales` descending within each region (matches the printed exercise title above).",
    "- Display or assign the result to confirm row order.",
]


def refresh_pandas(path: Path) -> None:
    nb = json.loads(path.read_text(encoding="utf-8"))
    # Insert Exercise 1 helper before body replacements so cell indices ≤72 stay stable
    has_ex1 = any(
        c.get("cell_type") == "markdown"
        and "**Exercise 1**" in "".join(c.get("source", []))
        and "What you should write" in "".join(c.get("source", []))
        for c in nb["cells"]
    )
    if not has_ex1:
        insert_idx = next(
            (
                i
                for i, c in enumerate(nb["cells"])
                if c.get("cell_type") == "markdown"
                and "## 8. Practice" in "".join(c.get("source", []))
            ),
            None,
        )
        if insert_idx is not None:
            insert_cell(nb, insert_idx + 1, PANDAS_INSERT_EX1)
    replace_markdown_by_index(nb, PANDAS)
    for heading, lines in PANDAS_EXERCISES.items():
        replace_markdown_by_heading(nb, heading, lines)
    path.write_text(json.dumps(nb, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")


LINALG: dict[int, list[str]] = {
    2: [
        "**Imports and environment check**",
        "",
        "**What this code does:**",
        "- Imports `numpy`, `matplotlib.pyplot`, and `time`, then prints `np.__version__` so you confirm the kernel sees the expected NumPy.",
    ],
    8: [
        "**Why NumPy is fast (concept + tiny demo)**",
        "",
        "**What this code does:**",
        "- Prints short bullet points, then builds `arr = np.array([1,2,3,4,5])` and prints `arr * 2` and `arr ** 2` to show elementwise arithmetic on the whole vector in one expression.",
    ],
    12: [
        "**Create arrays from lists; reshape dtypes**",
        "",
        "**What this code does:**",
        "- Builds `arr1d` from a mixed list (promotes to float) and `arr2d` from nested lists (strings).",
        "- Converts with `arr1d.astype(\"i1\")` to 1-byte integers and prints the array and `dtype`.",
    ],
    14: [
        "**Factory helpers: zeros, ones, identity, ranges**",
        "",
        "**What this code does:**",
        "- Prints `np.zeros((3,4))`, `np.ones((2,3))`, `np.eye(3)`, `np.arange(0,10,2)`, and `np.linspace(0,1,5)`—each call allocates a new array with a known pattern.",
    ],
    16: [
        "**Random arrays**",
        "",
        "**What this code does:**",
        "- Sets `np.random.seed(42)` for reproducibility, then prints `rand` (uniform [0,1)), `randn` (standard normal), and `randint(1,11, size=(2,3))` (integer samples).",
    ],
    18: [
        "**`dtype` and `astype`**",
        "",
        "**What this code does:**",
        "- Prints int and float arrays and their `dtype`s, converts integers to float with `astype`, then truncates floats to int32 with `astype(np.int32)` and prints before/after.",
    ],
    22: [
        "**Broadcasting**",
        "",
        "**What this code does:**",
        "- Adds `10` to a 1D array (scalar broadcasts across the vector), then multiplies by `2`.",
        "- Adds a 1D vector to a 2D matrix so the vector broadcasts across rows (see printed shapes in output).",
    ],
    24: [
        "**Elementwise comparisons**",
        "",
        "**What this code does:**",
        "- Compares two same-shape 2D arrays with `>`, `==`, and chained comparisons, producing boolean arrays of the same shape.",
    ],
    26: [
        "**1D indexing and slices**",
        "",
        "**What this code does:**",
        "- Uses integer indices, slices (`2:7`), negative indices, and two-element slices (`1:8:2`) on `np.arange(10)`.",
    ],
    28: [
        "**2D indexing and slices**",
        "",
        "**What this code does:**",
        "- On a 3×4 matrix, selects rows, columns, single elements, row slices, column slices, and sub-blocks (`[0:2, 1:3]`).",
    ],
    32: [
        "**Combine boolean conditions**",
        "",
        "**What this code does:**",
        "- Builds masks with `>`, combines with `&` and `|` (with parentheses), and negates with `~`—each step prints a boolean array.",
    ],
    34: [
        "**Masking with real labels**",
        "",
        "**What this code does:**",
        "- Uses parallel arrays `names` and `scores`, filters scores with `scores >= 5`, then uses that mask to subset `names` to students who passed.",
    ],
    36: [
        "**Assign through a mask**",
        "",
        "**What this code does:**",
        "- Copies `arr`, then assigns `5` everywhere `arr > 2` is True, and prints before/after.",
    ],
    40: [
        "**Stack arrays**",
        "",
        "**What this code does:**",
        "- Vertically and horizontally stacks 1D arrays `a` and `b` with `vstack` and `hstack`.",
    ],
    42: [
        "**Universal functions and a quick plot**",
        "",
        "**What this code does:**",
        "- Creates `x = np.linspace(0, 2π, 100)` and plots `sin(x)` and `cos(x)` in two subplots with matplotlib.",
    ],
    44: [
        "**`np.where` conditional selection**",
        "",
        "**What this code does:**",
        "- Calls `np.where(arr > 5, arr, 0)` so elements ≤5 become 0 and elements >5 stay unchanged; prints the result.",
    ],
    46: [
        "**Aggregate over the whole array**",
        "",
        "**What this code does:**",
        "- On a `np.random.randint` matrix, prints `sum`, `mean`, `std`, `min`, `max` across all elements (global reductions).",
    ],
    48: [
        "**Aggregate along an axis**",
        "",
        "**What this code does:**",
        "- Prints `np.sum(data, axis=1)` (row sums) and `np.sum(data, axis=0)` (column sums) so you see how `axis` picks which dimension collapses.",
    ],
    50: [
        "**`any` and `all` on booleans**",
        "",
        "**What this code does:**",
        "- Evaluates `np.any` / `np.all` on a boolean vector and on a boolean matrix with `axis=0` and `axis=1`.",
    ],
    52: [
        "**Sort and argsort**",
        "",
        "**What this code does:**",
        "- Prints `np.sort(arr)` (sorted copy) and `np.argsort(arr)` (indices that would sort the array).",
    ],
    56: [
        "**Matrix multiplication vs elementwise product**",
        "",
        "**What this code does:**",
        "- Prints `A` and `B`, then `A @ B` (matrix multiply) and `A * B` (same-shape elementwise product)—same symbols as in math vs NumPy’s `*` rule.",
    ],
    58: [
        "**Determinant and inverse**",
        "",
        "**What this code does:**",
        "- Prints `det(A)`, `inv(A)`, and `A @ inv(A)` rounded to verify the identity matrix.",
    ],
    60: [
        "**Solve \\(Ax = b\\)**",
        "",
        "**What this code does:**",
        "- Defines `A` and `b` for a 2×2 system, calls `np.linalg.solve(A, b)` to get `x`, then plugs `x` back into the two equations to print verification lines.",
    ],
    62: [
        "**Rank, trace, eigenvalues**",
        "",
        "**What this code does:**",
        "- Prints `matrix_rank`, `trace`, then `eig` which returns eigenvalues and eigenvector columns for `A`.",
    ],
}

LINALG_ARITHMETIC: list[str] = [
    "**Elementwise arithmetic on a 2D array**",
    "",
    "**What this code does:**",
    "- Creates `arr` as a 2×3 float matrix and prints it.",
    "- Prints `arr + 10` and `arr * 2` (scalar broadcasts to every entry).",
    "- Prints `arr ** 2` elementwise, then `np.sqrt(arr)` (ufunc applied to each element).",
]


def _linalg_has_behavior_helpers(nb: dict) -> bool:
    return any(
        c.get("cell_type") == "markdown"
        and "**What this code does:**" in "".join(c.get("source", []))
        for c in nb["cells"]
    )


def bootstrap_linalg_helpers(nb: dict) -> None:
    """Insert markdown before each code-after-code pair (e.g. clean notebook from git)."""
    ordered = [LINALG[k] for k in sorted(LINALG)]
    new_cells: list[dict] = []
    oi = 0
    for i, cell in enumerate(nb["cells"]):
        if (
            i > 0
            and cell["cell_type"] == "code"
            and nb["cells"][i - 1]["cell_type"] == "code"
        ):
            new_cells.append(
                {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": lines_to_source(ordered[oi]),
                }
            )
            oi += 1
        new_cells.append(cell)
    if oi != len(ordered):
        raise RuntimeError(
            f"bootstrap_linalg_helpers: expected {len(ordered)} inserts, got {oi}"
        )
    nb["cells"] = new_cells
    for i, c in enumerate(nb["cells"]):
        if c.get("cell_type") != "code":
            continue
        if "# Arithmetic operations (vectorized)" in "".join(c.get("source", [])):
            insert_cell(nb, i, LINALG_ARITHMETIC)
            return
    raise RuntimeError("bootstrap_linalg_helpers: arithmetic code cell not found")


def refresh_linalg(path: Path) -> None:
    nb = json.loads(path.read_text(encoding="utf-8"))
    if not _linalg_has_behavior_helpers(nb):
        bootstrap_linalg_helpers(nb)
    else:
        for k in sorted(LINALG):
            replace_markdown_by_heading(nb, LINALG[k][0], LINALG[k])
        replace_markdown_by_heading(nb, LINALG_ARITHMETIC[0], LINALG_ARITHMETIC)
    path.write_text(json.dumps(nb, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    refresh_pandas(root / "1-data-fundamentals/1.5-data-analysis-pandas/tutorial.ipynb")
    refresh_linalg(root / "1-data-fundamentals/1.4-data-foundation-linear-algebra/tutorial.ipynb")
    print("Refreshed pandas and linear-algebra tutorial helpers.")


if __name__ == "__main__":
    main()
