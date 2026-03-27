# Code block pattern (Module 1)

Use this template when adding or revising **substantive** fenced code in Module 1 lessons (Markdown, notebooks, or slides). It keeps **title → purpose → optional walkthrough** consistent and avoids **orphan** code (two runnable blocks back-to-back with no prose).

## Template (Markdown)

Place **immediately before** the opening Python (or other) fenced block:

1. A **short title** (bold line or `####` heading).
2. A bullet **Purpose:** one or two sentences.
3. Optionally **Walkthrough:** key lines/APIs—skip redundant line-by-line narration.

Then the fenced code block (unchanged unless the task explicitly asks for behavior changes).

If the next fence is **injected stdout** (from `pnpm run inject-python-outputs`), add a one-line label before it when the medium allows, for example: Sample output (may vary slightly with versions):

## Exercises and stubs

For `# Your code here` or comment-only exercise blocks, add:

- **Purpose:** Stub for **Exercise N** in this section—complete the bullets in the exercise heading above.

## Checklist (repeatable)

1. Scan for consecutive Python fences with only blank lines between—insert prose, a Purpose line, or a caption between them.
2. For each important block, add **Purpose**; add **Walkthrough** when the snippet is long or API-heavy.
3. Re-read **Purpose** against the code—no generic filler.
4. If you bulk-edit, key by **section heading + block index** so parallel copies do not drift.

## Related site docs

- Interactive lessons with **line callouts** may use the `code-explainer` pattern; see `docs/CLAUDE.md`.
- Course-wide authoring notes: `docs/meta/DOCUMENTATION_GUIDELINES.md`.
