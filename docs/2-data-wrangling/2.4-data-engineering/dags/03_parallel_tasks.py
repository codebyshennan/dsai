"""Fan-out / fan-in DAG — full teaching notes live in DAG_DOC below."""

from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

DAG_DOC = """
## Lesson 3 — Parallel branches (then join)

### What this teaches
- **Fan-out**: one task connects to **many** downstream tasks.
- **Fan-in**: many tasks connect to **one** downstream task.
- **Parallelism** depends on the **executor** (and capacity), not on the graph
  alone.

### Reading the code
`start >> [a, b, c] >> finish`

- **a**, **b**, and **c** all depend on **start**.
- **finish** depends on **a**, **b**, and **c** (all three must succeed).

With **LocalExecutor** (or similar), **a**, **b**, **c** may run **concurrently**
up to the configured parallelism.

### Schedule
**`@once`** is useful for demos: it does not mean “cron every second”; it
schedules a **single** logical run pattern (good for teaching graphs without
noise from many scheduled runs).

### Try in the UI
Open **Graph** and trace arrows from **start** to the three branches, then to
**finish**. Compare **start** / **finish** timestamps in task logs if you want
to show overlap.
"""

DAG_DOC = DAG_DOC.strip()


def start_fn():
    print("Starting...")


def task_a():
    print("Running Task A")


def task_b():
    print("Running Task B")


def task_c():
    print("Running Task C")


def finish_fn():
    print("All done!")


with DAG(
    dag_id="03_parallel_tasks",
    doc_md=DAG_DOC,
    tags=["tutorial", "03-parallel"],
    start_date=datetime(2024, 1, 1),
    schedule="@once",
    catchup=False,
    default_args={"owner": "tutorial", "retries": 0},
) as dag:
    start = PythonOperator(
        task_id="start",
        doc_md="Runs first; **a**, **b**, **c** wait for this task.",
        python_callable=start_fn,
    )
    a = PythonOperator(
        task_id="task_a",
        doc_md="Branch **A**; may run in parallel with **task_b** / **task_c**.",
        python_callable=task_a,
    )
    b = PythonOperator(
        task_id="task_b",
        doc_md="Branch **B**; may run in parallel with **task_a** / **task_c**.",
        python_callable=task_b,
    )
    c = PythonOperator(
        task_id="task_c",
        doc_md="Branch **C**; may run in parallel with **task_a** / **task_b**.",
        python_callable=task_c,
    )
    finish = PythonOperator(
        task_id="finish",
        doc_md="Runs after **all** of **task_a**, **task_b**, **task_c** succeed.",
        python_callable=finish_fn,
    )

    # List after >> = multiple downstream tasks at the same dependency level.
    start >> [a, b, c] >> finish
