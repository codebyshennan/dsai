# Data Engineering Assignment

**After this lesson:** You design or prototype an **ETL**-style pipeline (code or diagram plus narrative) with extract, transform, and load steps, basic quality checks, and a plausible failure-handling story.

## Helpful video

DAGs, tasks, and scheduling—conceptual background for ETL-style pipelines.

<iframe width="560" height="315" src="https://www.youtube.com/embed/eeSLDdz-aLg" title="Apache Airflow Tutorial for Beginners" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Overview

**Prerequisites:** [ETL fundamentals](etl-fundamentals.md), [data storage](data-storage.md), and [data integration](data-integration.md). Comfortable Python; optional [Airflow](../../0-prep/airflow.md) if you orchestrate with it.

> **Time needed:** Often 8–15 hours for a solid submission.

In this comprehensive assignment, you'll build a production-ready data engineering pipeline that demonstrates your ability to handle real-world data processing challenges. You'll apply advanced ETL concepts, implement robust error handling, and ensure scalable performance.

### Learning Objectives

- Master ETL pipeline development
- Implement data quality controls
- Handle complex transformations
- Ensure system reliability
- Optimize performance
- Monitor pipeline health

## Project Description

You'll be building an enterprise-grade data pipeline for an e-commerce company that processes millions of transactions daily. The system needs to:

### Data Collection

- **Sales Data**:
  - API integration with order system
  - Database connection to inventory
  - File imports from legacy systems
  - Real-time transaction streams

### Data Processing

- **Transformation**:
  - Clean and standardize data
  - Apply business rules
  - Calculate derived metrics
  - Validate data quality

### Data Storage

- **Warehouse Design**:
  - Dimensional modeling
  - Fact table design
  - Incremental loading
  - Performance optimization

### Reporting

- **Analytics Support**:
  - Sales analytics
  - Inventory metrics
  - Customer insights
  - Performance KPIs

## Setup

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight python %}
# Required libraries
import pandas as pd
import numpy as np
import sqlalchemy
import requests
import logging
from datetime import datetime
from typing import Dict, List, Any

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-7" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Required libraries</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–7: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="8-15" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">From typing import Dict, List, Any</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 8–15: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

## Tasks

### 1. Data Source Integration (25 points)

a) API Integration (10 points)

- Implement API client for sales data
- Handle authentication
- Implement error handling and retries
- Add rate limiting

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight python %}
class SalesAPIClient:
    """
    Implement API client for sales data
    """
    def __init__(self, base_url: str, api_key: str):
        # Your code here
        pass
    
    def fetch_sales(self, start_date: str, end_date: str) -> pd.DataFrame:
        """Fetch sales data for date range"""
        # Your code here
        pass
    
    def handle_rate_limit(self):
        """Implement rate limiting"""
        # Your code here
        pass
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-8" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Class SalesAPIClient:</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–8: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="9-17" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Def fetch_sales(self, start_date: str, end_da…</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 9–17: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

b) Database Integration (10 points)

- Connect to source database
- Implement efficient query patterns
- Handle large data volumes
- Implement connection pooling

c) File Integration (5 points)

- Handle different file formats
- Implement file validation
- Process files in batches
- Track processed files

### 2. Data Transformation (25 points)

a) Data Cleaning (10 points)

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight python %}
class DataCleaner:
    """
    Implement data cleaning operations
    """
    def clean_sales_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Clean sales data
        - Handle missing values
        - Remove duplicates
        - Fix data types
        - Validate data
        """
        # Your code here
        pass
    
    def validate_data(self, df: pd.DataFrame) -> bool:
        """
        Implement data validation rules
        """
        # Your code here
        pass
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-10" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Class DataCleaner:</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–10: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="11-21" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">- Validate data</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 11–21: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

b) Data Enrichment (10 points)

- Add derived columns
- Calculate aggregations
- Join with reference data
- Apply business rules

c) Data Quality (5 points)

- Implement data quality checks
- Generate quality metrics
- Handle validation failures
- Log quality issues

### 3. Data Storage (25 points)

a) Schema Design (10 points)

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight python %}
class WarehouseSchema:
    """
    Define data warehouse schema
    """
    def create_tables(self, engine):
        """Create warehouse tables"""
        # Define fact table
        fact_sales = """
        CREATE TABLE IF NOT EXISTS fact_sales (
            sale_id INTEGER PRIMARY KEY,
            date_id INTEGER,
            product_id INTEGER,
            customer_id INTEGER,
            quantity INTEGER,
            amount DECIMAL(10,2),
            FOREIGN KEY (date_id) REFERENCES dim_date(date_id),
            FOREIGN KEY (product_id) REFERENCES dim_product(product_id),
            FOREIGN KEY (customer_id) REFERENCES dim_customer(customer_id)
        )
        """
        
        # Define dimension tables
        dim_date = """
        CREATE TABLE IF NOT EXISTS dim_date (
            date_id INTEGER PRIMARY KEY,
            date DATE,
            year INTEGER,
            month INTEGER,
            day INTEGER,
            quarter INTEGER,
            is_weekend BOOLEAN
        )
        """
        
        # Execute schema creation
        with engine.connect() as conn:
            conn.execute(dim_date)
            conn.execute(fact_sales)
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-12" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Class WarehouseSchema:</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–12: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="13-25" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Customer_id INTEGER,</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 13–25: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="26-38" data-tint="3">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Date DATE,</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 26–38: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

b) Data Loading (10 points)

- Implement efficient load patterns
- Handle incremental loads
- Manage transactions
- Implement error recovery

c) Performance Optimization (5 points)

- Implement indexing strategy
- Optimize query performance
- Manage data partitioning
- Monitor performance

### 4. Pipeline Orchestration (15 points)

a) Pipeline Implementation (10 points)

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight python %}
class DataPipeline:
    """
    Implement data pipeline
    """
    def __init__(self):
        self.api_client = SalesAPIClient(base_url, api_key)
        self.cleaner = DataCleaner()
        self.warehouse = WarehouseSchema()
    
    def run_pipeline(self, start_date: str, end_date: str):
        """
        Run complete pipeline
        - Extract data
        - Transform data
        - Load data
        - Handle errors
        - Log progress
        """
        try:
            # Extract
            raw_data = self.api_client.fetch_sales(start_date, end_date)
            
            # Transform
            clean_data = self.cleaner.clean_sales_data(raw_data)
            
            # Load
            self.load_to_warehouse(clean_data)
            
        except Exception as e:
            logger.error(f"Pipeline failed: {str(e)}")
            raise
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-10" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Class DataPipeline:</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–10: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="11-20" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">&quot;&quot;&quot;</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 11–20: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="21-31" data-tint="3">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Raw_data = self.api_client.fetch_sales(start_…</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 21–31: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

b) Monitoring and Logging (5 points)

- Implement logging
- Track metrics
- Monitor performance
- Generate alerts

### 5. Documentation and Testing (10 points)

a) Documentation

- Code documentation
- Architecture diagram
- Setup instructions
- Maintenance guide

b) Testing

- Unit tests
- Integration tests
- Performance tests
- Error handling tests

## Deliverables

1. Python Package containing:
   - All implementation code
   - Tests
   - Documentation
   - Requirements file

2. Technical Documentation:
   - Architecture overview
   - Setup instructions
   - API documentation
   - Maintenance guide

3. Test Results:
   - Unit test results
   - Integration test results
   - Performance metrics
   - Code coverage report

## Evaluation Criteria

- Code quality and organization (20%)
- Implementation completeness (30%)
- Error handling and resilience (20%)
- Documentation quality (15%)
- Test coverage (15%)

## Solution Template

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight python %}
# Configuration
config = {
    'api': {
        'base_url': 'https://api.example.com',
        'api_key': 'your_api_key'
    },
    'database': {
        'warehouse': 'postgresql://localhost/warehouse',
        'source': 'postgresql://localhost/source'
    },
    'files': {
        'input_path': 'data/input',
        'processed_path': 'data/processed',
        'failed_path': 'data/failed'
    }
}

# Pipeline implementation
class SalesDataPipeline:
    """
    Main pipeline implementation
    """
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.setup_components()
    
    def setup_components(self):
        """Initialize pipeline components"""
        # Setup API client
        self.api_client = SalesAPIClient(
            self.config['api']['base_url'],
            self.config['api']['api_key']
        )
        
        # Setup database connections
        self.warehouse = sqlalchemy.create_engine(
            self.config['database']['warehouse']
        )
        
        # Setup data cleaner
        self.cleaner = DataCleaner()
    
    def run_daily_load(self):
        """Run daily data load"""
        try:
            # Extract data
            sales_data = self.extract_daily_data()
            
            # Clean and transform
            clean_data = self.cleaner.clean_sales_data(sales_data)
            
            # Load to warehouse
            self.load_to_warehouse(clean_data)
            
            logger.info("Daily load completed successfully")
            
        except Exception as e:
            logger.error(f"Daily load failed: {str(e)}")
            raise
    
    def extract_daily_data(self) -> pd.DataFrame:
        """Extract daily data from all sources"""
        # Your code here
        pass
    
    def load_to_warehouse(self, df: pd.DataFrame):
        """Load data to warehouse"""
        # Your code here
        pass

# Example usage
if __name__ == "__main__":
    # Initialize pipeline
    pipeline = SalesDataPipeline(config)
    
    try:
        # Run daily load
        pipeline.run_daily_load()
        
    except Exception as e:
        logger.error(f"Pipeline failed: {str(e)}")
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-13" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Configuration</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–13: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="14-27" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">&#x27;failed_path&#x27;: &#x27;data/failed&#x27;</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 14–27: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="28-40" data-tint="3">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">&quot;&quot;&quot;Initialize pipeline components&quot;&quot;&quot;</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 28–40: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="41-54" data-tint="4">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Self.cleaner = DataCleaner()</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 41–54: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="55-67" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Logger.info(&quot;Daily load completed successfully&quot;)</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 55–67: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="68-81" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Your code here</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 68–81: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

## Bonus Challenges

1. **Real-time Processing**
   - Implement streaming data processing
   - Handle real-time updates
   - Implement real-time monitoring
   - Add alerting system

2. **Advanced Features**
   - Add data versioning
   - Implement data lineage
   - Add data quality scoring
   - Implement automated testing

3. **Performance Optimization**
   - Implement parallel processing
   - Optimize memory usage
   - Add caching layer
   - Implement query optimization

Good luck! Remember to focus on building a robust and maintainable solution!
