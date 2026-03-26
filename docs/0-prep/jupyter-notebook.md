# Introduction to Jupyter Notebook

## What is Jupyter Notebook?

Jupyter Notebook is a **free** web-based tool that lets you create documents that combine code, text, images, and charts all in one place. It's the most popular tool for data science work!

**In simple terms:** Think of Jupyter Notebook as a digital lab notebook. Instead of writing code in separate files and results in different places, everything lives together - your code, explanations, results, and visualizations are all in one document.

**Why use Jupyter Notebook?**
- ✅ **Interactive** - Run code and see results immediately
- ✅ **Visual** - Create charts and graphs right in your notebook
- ✅ **Documentation** - Write explanations alongside your code
- ✅ **Shareable** - Easy to share with others
- ✅ **Industry standard** - Used by data scientists worldwide

> **Figure (add screenshot or diagram):** Jupyter notebook with a code cell, output, and markdown.

> **Note:** This guide assumes you have Anaconda or **uv** installed. If not, start with the [Anaconda guide](./anaconda.md) or your course’s Python setup materials.

## Understanding Notebooks

### What is a Cell?

A notebook is made up of **cells** - think of them as building blocks. Each cell can contain either code or text.

### Cell Types

**1. Code Cells** (for writing Python code):
- Type your Python code here
- Press **Shift + Enter** to run the code
- Results appear directly below the cell
- You can run cells in any order (but usually top to bottom)

**2. Markdown Cells** (for writing explanations):
- Write text, explanations, and notes
- Supports formatting (bold, italics, headers, lists)
- Can include images, links, and even math equations
- Great for documenting what your code does

> **Figure (add screenshot or diagram):** Side-by-side or stacked view of a code cell vs a markdown cell.

> **Tip:** You can mix code and markdown cells to create a story with your data analysis!

## Running Your Code

**How to execute (run) a cell:**

1. **Click the "Run" button** in the toolbar, OR
2. **Press Shift + Enter** (runs the cell and moves to the next one)
3. **Press Ctrl + Enter** (runs the cell but stays on the same cell)
4. **Press Alt + Enter** (runs the cell and creates a new cell below)

> **Tip:** The most common way is **Shift + Enter** — it runs your code and automatically moves to the next cell!

> **Figure (add screenshot or diagram):** Toolbar with the Run control highlighted.

## Keyboard Shortcuts (Hotkeys)

Jupyter has two modes, and different shortcuts work in each:

### Command Mode (Blue Border)
Press **Esc** to enter command mode. The cell border turns blue.

**Most Useful Shortcuts:**
- **a** — Insert a new cell **above** the current one
- **b** — Insert a new cell **below** the current one
- **d** twice — **Delete** the current cell (press **d** two times)
- **z** — **Undo** cell deletion
- **m** — Change cell to **Markdown** (for text/explanations)
- **y** — Change cell to **Code** (for Python code)

### Edit Mode (Green Border)
Press **Enter** to enter edit mode. The cell border turns green.

**Most Useful Shortcuts:**
- **Shift + Enter** — Run cell and move to next
- **Ctrl + Enter** — Run cell (stay on same cell)
- **Alt + Enter** — Run cell and create new cell below

> **Tip:** Don't try to memorize all shortcuts at once! Start with **Shift + Enter** to run cells, and **a** / **b** to add cells. You'll learn the rest as you go.

> **Figure (add screenshot or diagram):** Same cell in command mode (blue border) vs edit mode (green border).

## Installation

### If You're Using Anaconda

Jupyter Notebook comes pre-installed with Anaconda. Either:

1. Open Anaconda Navigator and click **Launch** under **Jupyter Notebook**, or

2. Use the terminal:

```bash
# Make sure your environment is activated
conda activate dsai

# Classic Notebook interface
jupyter notebook
```

**JupyterLab** (a newer interface for the same `.ipynb` format) is also common:

```bash
jupyter lab
```

### If You're Using uv

```bash
# Step 1: Activate your virtual environment
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows

# Step 2: Install Jupyter (Notebook and/or Lab)
uv pip install jupyter notebook jupyterlab

# Step 3: Launch
jupyter notebook
# or: jupyter lab
```

**What happens next:**
- Your web browser will open automatically
- You'll see the Jupyter file browser
- Navigate to your project folder
- Click "New" → "Python 3" to create a new notebook

> **Figure (add screenshot or diagram):** Jupyter file browser / home page listing folders and **New** menu.

## Useful Resources

- [Official Jupyter Documentation](https://jupyter.org/)
- [Jupyter Notebook Tutorial](https://www.dataquest.io/blog/jupyter-notebook-tutorial/)
- [Markdown Guide](https://www.markdownguide.org/)
- [Jupyter Notebook Shortcuts (Towards Data Science)](https://towardsdatascience.com/jupyter-notebook-shortcuts-bf0101a98330)
