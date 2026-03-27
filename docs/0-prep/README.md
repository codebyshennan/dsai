# Getting started: setup guides

**After this folder (essential path):** you meet every bullet under **You are ready when** below—a working env, imports, Jupyter, and ideally VS Code tied to the same interpreter.

Welcome to the Data Science and AI bootcamp. The pages in this folder get your **Python environment**, **libraries**, **editor**, and **notebooks** working so lesson time can focus on ideas instead of install errors.

**Start here:** if you have done nothing yet, do only this sequence today: (1) install [Anaconda](./anaconda.md) or [uv](./anaconda.md), (2) install the [Python data science stack](./python-ds-stack.md), (3) open [Jupyter](./jupyter-notebook.md) and run a one-cell “hello” notebook. Add [VS Code](./vscode.md) when you want a full editor for `.py` files. Everything else on this page is optional until a module tells you to install it.

## Helpful video

Short overview of **what data science is** and how teams use data (about 8 minutes)—context before setup, not a substitute for the lessons.

<iframe width="560" height="315" src="https://www.youtube.com/embed/RBSUwFGa6Fk" title="What is Data Science?" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## You are ready when

You can check all of the following:

- You have a **conda env** or **uv `.venv`** you know how to activate, and you use it every time you open a terminal.
- `python -c "import pandas, numpy, matplotlib"` runs with **no** `ModuleNotFoundError`.
- You can **start Jupyter** (from Anaconda Navigator or the command line) and run a cell that prints something.
- Optional but recommended: VS Code opens a `.py` file and uses the **same** interpreter as your course environment (status bar shows the env).

If any box fails, stay on that step until it passes—adding more tools rarely fixes a broken base install.

## Quick start (order matters)

1. **Python environment** (pick one):
   - [Anaconda](./anaconda.md) if you are new to Python or want a GUI.
   - **uv** only if you are already comfortable in the terminal—follow the same guide.
2. **Libraries** — [Python data science stack](./python-ds-stack.md)
3. **Editor** — [VS Code](./vscode.md) (recommended for scripts)
4. **Notebooks** — [Jupyter](./jupyter-notebook.md)

> **Note:** GitHub-style `- [ ]` task lists do not render as checkboxes on the course site, so use your own checklist or notes to track progress.

## Essential tools

### Must have

1. **[Anaconda or uv](./anaconda.md)** — isolates project packages  
   - **Time:** about 15–20 minutes  
   - Prefer Anaconda if you are new to programming.

2. **[Python data science libraries](./python-ds-stack.md)** — NumPy, pandas, plotting, sklearn, etc.  
   - **Time:** about 10–15 minutes after the env exists  

3. **[Jupyter Notebook](./jupyter-notebook.md)** — where most early exercises run  
   - **Time:** usually zero extra install if you use Anaconda with Jupyter included  

### Recommended

4. **[VS Code](./vscode.md)** — editing and debugging `.py` files  
5. **[DBeaver](./dbeaver.md)** — connect to databases for SQL lessons (any SQL client you prefer is fine)

### Optional (install when a module needs them)

| Guide | Use case |
|-------|----------|
| [Google Colab](./google-colab.md) | Browser notebooks, no local install |
| [Tableau Public](./tableau.md) | BI / visualization modules |
| [Snowflake](./snowflake.md) | Cloud warehouse and advanced SQL |
| [Databricks](./databricks.md) | Spark / big data lessons |
| [Airflow](./airflow.md) | Workflow and scheduling labs |

## Suggested timeline

**Week 1 — core setup:** conda or uv, libraries, confirm Jupyter, then VS Code.

**Later — as assigned:** DBeaver when SQL starts; Tableau, Snowflake, Databricks, or Airflow when the module syllabus says so.

## Getting help

1. Troubleshooting sections in each guide  
2. [How this course works](./pedagogy.md) — what to bring to office hours  
3. Your instructor’s syllabus and announced channels  

### Common first-time issues

- **“Command not found”** — the tool is not on your `PATH`; restart the terminal after install, or use the “Anaconda Prompt” / full path your guide mentions.
- **Installs take a long time** — normal for large scientific stacks; use a stable connection.
- **Permission errors** — on macOS/Linux avoid `sudo` for Python envs; fix ownership or use a user-level install instead.
- **Wrong Python** — multiple Pythons are normal; always **activate** the course env before `pip`/`conda`/`uv`.

## How teaching works here

We use a **flipped** model: you study materials before live sessions and use class time to practice. Read [How this course works](./pedagogy.md) for a concrete week-by-week pattern and how to use office hours well.

## Tips

1. Finish core setup before racing ahead—broken envs waste more time than slow installs.  
2. After each install, run the **verification** step in that guide.  
3. Keep a short log of errors and fixes; it speeds up help.  
4. Use one folder or repo for course work so paths stay predictable.

## Need more help?

- Each guide links to official documentation for the tool.  
- Contributors: [Documentation guidelines](https://github.com/codebyshennan/tamkeen-data/blob/main/docs/meta/DOCUMENTATION_GUIDELINES.md) (the `docs/meta` folder is not published on the site).  
- Grading and policies: your instructor and syllabus.

---

**Next step:** [Anaconda or uv](./anaconda.md), or [How this course works](./pedagogy.md) if your environment is already working.
