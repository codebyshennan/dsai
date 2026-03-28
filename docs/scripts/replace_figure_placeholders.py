"""
Replace > **Figure (add screenshot or diagram):** placeholders in Module 3.

Rules:
- If the referenced assets/ file exists relative to the lesson file → replace with ![alt](assets/file.png)
- If it's a BI tool screenshot (tableau, powerbi, looker) → replace with > **Screenshot pending:** description
- If the file doesn't exist in assets/ → leave as-is but upgrade wording
"""
import re
from pathlib import Path

DOCS = Path(__file__).parent.parent
VIZ_DIR = DOCS / "3-data-visualization"

# Map from placeholder caption text to (assets_subdir, filename, alt_text)
# None for assets_subdir means look in the lesson's own assets/
CAPTION_MAP = {
    # 3.1 README
    "Chart Selection Guide": ("3.1-intro-data-viz/assets", "chart_selection_guide.png",
                               "Chart selection guide: which chart type fits which question"),
    "Visual Hierarchy Example": ("3.1-intro-data-viz/assets", "visual_hierarchy.png",
                                  "Visual hierarchy in chart design"),
    "Color Schemes": ("3.1-intro-data-viz/assets", "color_schemes.png",
                       "Color scheme examples for data visualization"),
    "Before and After Example": ("3.1-intro-data-viz/assets", "before_after.png",
                                  "Before and after: cluttered vs. clean chart"),

    # 3.4 narrative-techniques
    "Story Structure": ("3.4-data-storytelling/assets", "story_structure.png",
                         "Narrative story structure for data presentations"),
    "Visual Hierarchy": ("3.4-data-storytelling/assets", "visual_hierarchy.png",
                          "Visual hierarchy principles in data storytelling"),
    "Visualization Decision Tree": ("3.4-data-storytelling/assets", "visualization_decision_tree.png",
                                     "Decision tree for choosing the right visualization"),
    "Color Palette Guide": ("3.4-data-storytelling/assets", "color_palette_guide.png",
                             "Color palette guide for data storytelling"),
    "Story Creation Process": ("3.4-data-storytelling/assets", "story_creation_process.png",
                                "Step-by-step story creation process"),
    "Quality Checklist": ("3.4-data-storytelling/assets", "quality_checklist.png",
                           "Quality checklist for data stories"),

    # 3.4 visual-storytelling (also references chart_selection_guide but in 3.4 assets)
    "Narrative Arc": ("3.4-data-storytelling/assets", "narrative_arc.png",
                       "Narrative arc: setup, conflict, resolution in data stories"),
    "Story Arc": ("3.4-data-storytelling/assets", "story_arc.png",
                   "Story arc template for data presentations"),
    "Layout Examples": ("3.4-data-storytelling/assets", "layout_examples.png",
                         "Dashboard layout examples"),

    # 3.4 case-studies
    "Before and After Transformation": ("3.4-data-storytelling/assets", "before_after_example.png",
                                         "Before and after: chart improvement example"),

    # common-mistakes.md - these reference the 3.4 before_after asset
    "Before and After Transformation": ("3.4-data-storytelling/assets", "before_after_example.png",
                                         "Before vs after: fixing a cluttered chart"),
}

# BI tool pages - replace with screenshot pending note
BI_PAGES = {
    "powerbi-case-study.md",
    "tableau-basics.md",
    "tableau-case-study.md",
    "looker-studio-case-study.md",
}

PLACEHOLDER_PATTERN = re.compile(
    r'> \*\*Figure \(add screenshot or diagram\):\*\* (.+?)$',
    re.MULTILINE
)


def process_file(filepath: Path):
    text = filepath.read_text()
    original = text

    def replace_match(m):
        caption = m.group(1).strip()
        filename = filepath.name

        # BI tool pages: upgrade to screenshot pending
        if filename in BI_PAGES:
            return f'> **Screenshot pending:** {caption}'

        # Look up in caption map
        if caption in CAPTION_MAP:
            subdir, asset_file, alt = CAPTION_MAP[caption]
            asset_path = DOCS / "3-data-visualization" / subdir / asset_file
            if asset_path.exists():
                # Make path relative to lesson file directory
                rel_base = filepath.parent
                rel_to_viz = Path("3-data-visualization") / subdir / asset_file
                # Compute relative path from lesson to asset
                try:
                    rel = asset_path.relative_to(rel_base)
                    return f'![{alt}]({rel})'
                except ValueError:
                    # Different subdir: use relative path
                    dots = "../" * len(rel_base.relative_to(DOCS).parts)
                    return f'![{alt}]({dots}3-data-visualization/{subdir}/{asset_file})'

        # No match found — leave as upgraded note
        return f'> **Screenshot pending:** {caption}'

    new_text = PLACEHOLDER_PATTERN.sub(replace_match, text)

    if new_text != original:
        filepath.write_text(new_text)
        changed = new_text.count("Screenshot pending") - original.count("Screenshot pending")
        replaced = original.count("> **Figure") - new_text.count("> **Figure")
        print(f"  {filepath.relative_to(DOCS)}: {replaced} replaced as image, "
              f"{original.count('> **Figure') - replaced} → screenshot pending")
    else:
        print(f"  {filepath.relative_to(DOCS)}: no changes")


print("Processing Module 3 figure placeholders...\n")
md_files = list(VIZ_DIR.rglob("*.md"))
md_files = [f for f in md_files if "_site" not in str(f) and ".venv" not in str(f)]

for f in sorted(md_files):
    if PLACEHOLDER_PATTERN.search(f.read_text()):
        process_file(f)

print("\nDone.")
