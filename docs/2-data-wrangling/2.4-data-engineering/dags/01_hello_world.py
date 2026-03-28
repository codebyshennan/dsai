"""Minimal single-task DAG — full teaching notes live in DAG_DOC below."""

from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

# Rendered in the Airflow UI under DAG details (Markdown).
DAG_DOC = """
## Lesson 1 — Hello, Airflow

### What this teaches
- The smallest useful DAG: **one DAG**, **one task**, **one operator type**
- How **schedule** and **catchup** affect whether past dates run automatically

### Vocabulary (use the same words with students)
| Term | Meaning |
|------|---------|
| **DAG** | The workflow definition (this file). |
| **Task** | One step in the graph. |
| **DAG run** | A single execution of the DAG for a logical date interval. |
| **Task instance** | One execution of a task inside a specific DAG run. |

### Parameters worth naming aloud
- **`schedule="@daily"`** — Airflow schedules a run per day (timezone: see
  config / UTC by default in many setups).
- **`catchup=False`** — Do **not** backfill every day from `start_date` to
  today; only schedule from roughly when the DAG is active onward.
- **`start_date`** — Anchor for scheduling math; with `catchup=False` it does
  not mean “run all history.”

### Try in the UI
1. Turn the DAG **on**, trigger a run, open **Graph** or **Grid**.
2. Click the **`say_hello`** task → **Logs** — you should see the print output.

### If something fails
- Check **task logs** first; import errors appear on the DAG or in processor
  logs.
"""

DAG_DOC = DAG_DOC.strip()


def say_hello():
    """Runs inside the worker; open task logs in the UI to see output."""
    print("Hello, Airflow!")


with DAG(
    dag_id="01_hello_world",
    doc_md=DAG_DOC,
    tags=["tutorial", "01-basics"],
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    default_args={
        "owner": "tutorial",
        "retries": 0,
    },
) as dag:
    hello_task = PythonOperator(
        task_id="say_hello",
        doc_md="""
### PythonOperator — `say_hello`

Runs the Python callable **`say_hello`** on a worker.

**Tip:** Anything you `print()` here shows up in the **task log** for this run,
not in the scheduler log.
        """.strip(),
        python_callable=say_hello,
    )
