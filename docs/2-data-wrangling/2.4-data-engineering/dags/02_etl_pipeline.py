"""Linear ETL-style chain — full teaching notes live in DAG_DOC below."""

from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

DAG_DOC = """
## Lesson 2 — Linear pipeline (ETL shape)

### What this teaches
- **Dependencies**: downstream tasks wait for upstream success.
- A common pattern: **extract → transform → load** (order matters).

### Reading the code
The line:

` t1 >> t2 >> t3 `

means **t2** runs after **t1**, and **t3** after **t2**. Same idea as
`set_downstream` / `set_upstream`, but `>>` is the usual style in tutorials.

### Try in the UI
1. Trigger a run and open **Graph**.
2. Watch run order: **extract** → **transform** → **load**.
3. Fail one task in a later exercise (not in this file) to show blocking.

### Design note
Here each step only **prints** — in production, callables would call databases,
APIs, or file systems. The *shape* of the DAG stays the same.
"""

DAG_DOC = DAG_DOC.strip()


def extract():
    print("Extracting data...")


def transform():
    print("Transforming data...")


def load():
    print("Loading data...")


with DAG(
    dag_id="02_etl_pipeline",
    doc_md=DAG_DOC,
    tags=["tutorial", "02-dependencies"],
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    default_args={"owner": "tutorial", "retries": 0},
) as dag:
    t1 = PythonOperator(
        task_id="extract",
        doc_md="""
**Extract** — first step of the pipeline.

In real jobs: read from DB, API, files, or streams. Here: a placeholder print.
        """.strip(),
        python_callable=extract,
    )
    t2 = PythonOperator(
        task_id="transform",
        doc_md="""
**Transform** — runs only after **extract** succeeds.

Typical work: clean, join, aggregate, type conversions.
        """.strip(),
        python_callable=transform,
    )
    t3 = PythonOperator(
        task_id="load",
        doc_md="""
**Load** — runs only after **transform** succeeds.

Typical work: write to warehouse, DB, or curated files.
        """.strip(),
        python_callable=load,
    )

    # Read left → right as execution order.
    t1 >> t2 >> t3
