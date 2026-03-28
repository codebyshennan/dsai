---
published: false
---
# Code block annotations (Module 5 — ML fundamentals)

Use this template for Markdown lessons, notebooks, and slide-adjacent docs so every substantive code fence has a clear teaching role. **Do not change program behavior** in snippets unless the curriculum explicitly requires it.

## Block ID scheme (reproducibility)

Use stable IDs when referencing blocks in issues, scripts, or reviews:

`5-<submodule>-<file-stem>-<ordinal>`

Examples: `5-5.5-sklearn-pipelines-01`, `5-1.1-ml-workflow-04`.

Ordinals count fenced blocks in file order (all languages), or only `python` blocks if you standardize that convention in a given PR.

## Structure

For each important fence:

1. **Title** — Short heading (`####`), bold line, or slide bullet: what this block shows.
2. **Purpose:** — What the learner should understand or be able to do after reading/running it; tie to the narrative or learning objective.
3. **Walkthrough:** — (Optional) Pointers to lines, APIs, or steps that matter—not line-by-line narration.

```markdown
#### Title in plain language

**Purpose:** One or two sentences.

**Walkthrough:** Optional. Key APIs, steps, or line ranges worth noticing.

\`\`\`python
# code
\`\`\`
```

## Injected stdout / plots

When the repo uses `pnpm run inject-python-outputs`, a bare \`\`\` output fence may follow a Python fence. Separate that from the next code block with a caption so fences are not “orphan pairs”:

```markdown
**Captured stdout** (from running the snippet above; may be auto-injected on build):

\`\`\`
Pipeline score: 0.990
\`\`\`
```

If a figure follows instead of text, use:

**Figure** (generated when the site build runs the snippet): `assets/<lesson>_fig_*.png`

## Exercises and stubs

For `pass`, `# your code here`, or TODO stubs:

**Exercise:** `<id>` — Brief pointer to the task defined in the section heading or assignment doc.

## Orphan fences

Avoid two runnable/illustrative fences back-to-back with no prose, caption, or callout between them. If the medium requires it (e.g. code + stdout), tie the second fence to the first with a **Captured stdout** / **Expected output** line.

## Checklist before merge

- [ ] Each substantive `python` (and other teaching) fence has **Purpose:** (and title).
- [ ] Walkthroughs match the actual code (no generic filler).
- [ ] No unexplained consecutive code fences without a caption.
- [ ] Exercise stubs reference an exercise ID or stated task.

## Automation

From `docs/`:

```bash
pnpm run audit-ml-code-blocks
# or:
uv run python scripts/audit_ml_fundamentals_code_blocks.py
```

Reports consecutive bare fences and files that may need annotation passes (heuristic).

## Coverage status (manual passes)

Incremental PRs should run the audit and chip away at remaining ` ```python ` fences.

- **Done (annotated):** `5.1-intro-to-ml/` (`what-is-ml.md`, `ml-workflow.md`, `feature-engineering.md`, `feature-engineering-new.md`, `bias-variance.md`); `5.5-model-eval/sklearn-pipelines.md`, `accuracy.md`, `cross-validation.md`.
- **Done (annotated):** `5.2-supervised-learning-1/` — module `README.md`; **decision-trees** (`1-introduction` through `5-applications`); **kNN** (`1-introduction` through `5-applications`); **naive-bayes** (`2-math-foundation` through `5-advanced-topics`; intro is prose-only); **svm** (`2-math-kernels` through `5-applications`; `1-introduction` and root `svm.md` are navigation-only). Stdout fences use **Captured stdout** where applicable; some Naive Bayes / kNN snippets were minimally repaired for imports or runnable pipelines (see git history for that pass).
- **Remaining:** `5.3-supervised-learning-2/`, `5.4-unsupervised-learning/`, and the rest of `5.5-model-eval/`—follow the same title → **Purpose** → optional **Walkthrough** pattern; label injected stdout blocks as **Captured stdout**.
