"""XCom push/pull between tasks — full teaching notes live in DAG_DOC below."""

from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

DAG_DOC = """
## Lesson 4 — XComs (cross-task messages)

### What this teaches
- How tasks **pass small pieces of data** within a DAG run using **XComs**.
- Where the **TaskInstance** (`ti`) comes from: **`context["ti"]`** in a
  **PythonOperator** callable.

### Rules of thumb
- **Do** use XComs for: small IDs, counts, flags, short strings.
- **Do not** use XComs for: large blobs; use object storage + **paths** in XCom
  or plain task logic instead.

### Reading the code
1. **producer** calls `ti.xcom_push(key="my_number", value=42)`.
2. **consumer** calls `ti.xcom_pull(task_ids="producer", key="my_number")`.

The **`task_ids`** argument must match the **task_id** of the upstream task.

### Try in the UI
Trigger a run, then **check consumer logs** for the printed value. If your
Airflow version exposes **XCom** in the UI for a task, open it there too.

### Callable signature
We use **`**context`** so beginners see explicitly that Airflow passes a
**context** mapping; `ti` is the `TaskInstance` for the current task.
"""

DAG_DOC = DAG_DOC.strip()


def produce_value(**context):
    """Push a value into XCom storage for this DAG run."""
    ti = context["ti"]
    ti.xcom_push(key="my_number", value=42)


def consume_value(**context):
    """Pull the value from the upstream task that produced it."""
    ti = context["ti"]
    value = ti.xcom_pull(task_ids="producer", key="my_number")
    print(f"Received value: {value}")


with DAG(
    dag_id="04_xcom_example",
    doc_md=DAG_DOC,
    tags=["tutorial", "04-xcom"],
    start_date=datetime(2024, 1, 1),
    schedule="@once",
    catchup=False,
    default_args={"owner": "tutorial", "retries": 0},
) as dag:
    producer = PythonOperator(
        task_id="producer",
        doc_md="""
**Pushes** an XCom with key **`my_number`** and value **`42`**.

Downstream tasks in the **same DAG run** can read this with `xcom_pull`.
        """.strip(),
        python_callable=produce_value,
    )
    consumer = PythonOperator(
        task_id="consumer",
        doc_md="""
**Pulls** the XCom saved by **`producer`** using the same **key**.

If the key or `task_ids` is wrong, you get `None` or a clear error in logs.
        """.strip(),
        python_callable=consume_value,
    )

    producer >> consumer
