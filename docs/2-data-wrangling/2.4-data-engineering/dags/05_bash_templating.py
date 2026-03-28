"""BashOperator + Jinja — full teaching notes live in DAG_DOC below."""

from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

DAG_DOC = """
## Lesson 5 — BashOperator and Jinja templates

### What this teaches
- **BashOperator** runs a shell command on a worker (good for scripts, CLIs,
  small utilities).
- **`{{ ... }}`** is **Jinja** templating: Airflow replaces **macros** before
  the shell runs the command.

### Important distinction
- **`{{ ds }}`** — logical **date** for the data interval (often `YYYY-MM-DD`),
  filled in by Airflow.
- **`$VAR`** — shell variable, only known if **you** export/set it in the same
  command or environment.

Students often confuse the two; call it out in the room.

### Common macros (see Airflow docs for the full list)
- **`{{ ds }}`** — date string
- **`{{ ds_nodash }}`** — same date, no hyphens
- **`{{ ts }}`** — timestamp
- **`{{ dag.dag_id }}`** — this DAG’s id

### Try in the UI
Trigger a run and read **task logs** for **`print_execution_date`**: the echoed
line should show the **logical date** for that run.

### Safety
Do not paste untrusted input into `bash_command` in production; treat it like
any shell injection surface.
"""

DAG_DOC = DAG_DOC.strip()

with DAG(
    dag_id="05_bash_templating",
    doc_md=DAG_DOC,
    tags=["tutorial", "05-bash-jinja"],
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    default_args={"owner": "tutorial", "retries": 0},
) as dag:
    print_date = BashOperator(
        task_id="print_execution_date",
        doc_md="""
**Jinja macro `{{ ds }}`** is expanded **before** the process runs.

The shell sees a normal string like `Running for date: 2026-03-26`, not the
literal braces.
        """.strip(),
        bash_command="echo 'Running for date: {{ ds }}'",
    )

    greet = BashOperator(
        task_id="greet",
        doc_md="""
Static command — no templates. Runs **after** **`print_execution_date`**
because of **>>** below.
        """.strip(),
        bash_command="echo 'Hello from Bash!'",
    )

    print_date >> greet
