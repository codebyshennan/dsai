# Mastering Basic SQL Operations: Your Data Query Journey

**After this lesson:** You can **CREATE** tables, **INSERT** rows, **SELECT** and filter data with **WHERE**, **UPDATE** and **DELETE** safely, and read simple query plans.

## Helpful video

High-level introduction to SQL and relational databases.

<iframe width="560" height="315" src="https://www.youtube.com/embed/27axs9dO7AE" title="What is SQL?" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Overview

**Prerequisites:** [Introduction to Databases](intro-databases.md) (tables, keys, types). Have a SQL client and a practice database as described in the [module README](README.md).

> **Time needed:** About 60–90 minutes with hands-on practice.

## Introduction to SQL Basics

SQL (Structured Query Language) is the standard language for managing and manipulating relational databases. Understanding basic SQL operations is crucial for:

- Data retrieval and analysis
- Database management
- Data integrity maintenance
- Application development

## CRUD Operations

### 1. CREATE: Adding Data

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
-- Create a new table
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert single row
INSERT INTO customers (first_name, last_name, email)
VALUES ('John', 'Doe', 'john.doe@email.com');

-- Insert multiple rows
INSERT INTO customers (first_name, last_name, email)
VALUES 
    ('Jane', 'Smith', 'jane.smith@email.com'),
    ('Bob', 'Johnson', 'bob.johnson@email.com');
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-9" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Create a new table</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–9: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="10-18" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Insert single row</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 10–18: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

### 2. READ: Querying Data

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
-- Select all columns
SELECT * FROM customers;

-- Select specific columns
SELECT first_name, last_name, email 
FROM customers;

-- Basic filtering
SELECT * FROM customers
WHERE last_name = 'Smith';

-- Pattern matching
SELECT * FROM customers
WHERE email LIKE '%@email.com';
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-14" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Select all columns</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–14: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

### 3. UPDATE: Modifying Data

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
-- Update single record
UPDATE customers
SET email = 'new.email@email.com'
WHERE customer_id = 1;

-- Update multiple records
UPDATE customers
SET created_at = CURRENT_TIMESTAMP
WHERE created_at IS NULL;

-- Update with conditions
UPDATE customers
SET 
    first_name = INITCAP(first_name),
    last_name = INITCAP(last_name)
WHERE 
    first_name != INITCAP(first_name) OR
    last_name != INITCAP(last_name);
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-9" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Update single record</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–9: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="10-18" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Update with conditions</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 10–18: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

### 4. DELETE: Removing Data

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
-- Delete specific records
DELETE FROM customers
WHERE customer_id = 1;

-- Delete with conditions
DELETE FROM customers
WHERE created_at < CURRENT_DATE - INTERVAL '1 year';

-- Delete all records
TRUNCATE TABLE customers;
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-10" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Delete specific records</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–10: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

## Basic Query Structure

### 1. SELECT Statement Anatomy

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
SELECT 
    column1,
    column2,
    column3 AS alias,
    CONCAT(column4, ' ', column5) as derived_column
FROM table_name
WHERE condition
GROUP BY column1
HAVING group_condition
ORDER BY column3 DESC
LIMIT 10;
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-11" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">SELECT</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–11: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

### 2. Filtering and Sorting

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
-- Basic WHERE clauses
SELECT * FROM products
WHERE 
    category = 'Electronics' AND
    price >= 100 AND
    stock_quantity > 0;

-- Multiple conditions
SELECT * FROM orders
WHERE 
    status IN ('pending', 'processing') AND
    order_date BETWEEN 
        CURRENT_DATE - INTERVAL '30 days' 
        AND CURRENT_DATE;

-- Pattern matching
SELECT * FROM customers
WHERE 
    email LIKE '%.com' AND
    first_name ILIKE 'j%';  -- Case-insensitive

-- Sorting results
SELECT 
    product_name,
    price,
    stock_quantity
FROM products
ORDER BY 
    price DESC,
    product_name ASC;
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-15" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Basic WHERE clauses</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–15: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="16-30" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Pattern matching</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 16–30: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

## Data Types and Constraints

### 1. Common Data Types

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
CREATE TABLE products (
    -- Numeric types
    product_id SERIAL PRIMARY KEY,
    price DECIMAL(10,2),
    weight INTEGER,
    
    -- String types
    name VARCHAR(100),
    description TEXT,
    
    -- Date/Time types
    created_at TIMESTAMP,
    sale_date DATE,
    
    -- Boolean type
    is_active BOOLEAN,
    
    -- Enumerated type
    status product_status
);
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-10" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">CREATE TABLE products (</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–10: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="11-20" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Date/Time types</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 11–20: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

### 2. Constraints

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
CREATE TABLE orders (
    -- Primary Key
    order_id SERIAL PRIMARY KEY,
    
    -- Foreign Key
    customer_id INTEGER REFERENCES customers(customer_id),
    
    -- Not Null
    order_date TIMESTAMP NOT NULL,
    
    -- Unique
    tracking_number VARCHAR(50) UNIQUE,
    
    -- Check constraint
    total_amount DECIMAL(10,2) CHECK (total_amount >= 0),
    
    -- Default value
    status VARCHAR(20) DEFAULT 'pending'
);
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-9" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">CREATE TABLE orders (</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–9: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="10-19" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Unique</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 10–19: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

## Table Relationships

### 1. One-to-Many Relationship

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
CREATE TABLE categories (
    category_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    category_id INTEGER REFERENCES categories(category_id),
    name VARCHAR(100) NOT NULL
);
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-10" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">CREATE TABLE categories (</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–10: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

### 2. Many-to-Many Relationship

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    order_date TIMESTAMP NOT NULL
);

CREATE TABLE order_items (
    order_id INTEGER REFERENCES orders(order_id),
    product_id INTEGER REFERENCES products(product_id),
    quantity INTEGER NOT NULL,
    price_at_time DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (order_id, product_id)
);
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-8" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">CREATE TABLE products (</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–8: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="9-17" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">);</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 9–17: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

## Basic Joins

### 1. INNER JOIN

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
-- Get all orders with customer information
SELECT 
    o.order_id,
    o.order_date,
    c.first_name,
    c.last_name,
    o.total_amount
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id;
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-9" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Get all orders with customer information</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–9: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

### 2. LEFT JOIN

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
-- Get all customers and their orders (if any)
SELECT 
    c.customer_id,
    c.first_name,
    c.last_name,
    COUNT(o.order_id) as order_count,
    COALESCE(SUM(o.total_amount), 0) as total_spent
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name;
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-10" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Get all customers and their orders (if any)</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–10: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

### 3. Multiple Joins

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
-- Get order details with product and customer information
SELECT 
    o.order_id,
    c.first_name || ' ' || c.last_name as customer_name,
    p.name as product_name,
    oi.quantity,
    oi.price_at_time,
    oi.quantity * oi.price_at_time as line_total
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
ORDER BY o.order_id, p.name;
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-13" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Get order details with product and customer i…</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–13: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

## Additional Real-World Business Scenarios

### 1. E-commerce Order Analytics

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
-- Comprehensive order analysis with multiple metrics
WITH order_metrics AS (
    SELECT 
        DATE_TRUNC('day', order_date) as order_day,
        COUNT(*) as total_orders,
        COUNT(DISTINCT customer_id) as unique_customers,
        SUM(total_amount) as revenue,
        AVG(total_amount) as avg_order_value,
        COUNT(DISTINCT CASE 
            WHEN customer_id NOT IN (
                SELECT customer_id 
                FROM orders o2 
                WHERE o2.order_date < o.order_date
            ) THEN customer_id 
        END) as new_customers
    FROM orders o
    WHERE order_date >= CURRENT_DATE - INTERVAL '30 days'
    GROUP BY DATE_TRUNC('day', order_date)
)
SELECT 
    order_day,
    total_orders,
    unique_customers,
    ROUND(revenue::numeric, 2) as revenue,
    ROUND(avg_order_value::numeric, 2) as aov,
    new_customers,
    ROUND(
        (new_customers::float / NULLIF(unique_customers, 0) * 100)::numeric,
        2
    ) as new_customer_percentage,
    ROUND(
        (revenue::float / NULLIF(unique_customers, 0))::numeric,
        2
    ) as revenue_per_customer
FROM order_metrics
ORDER BY order_day DESC;
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-12" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Comprehensive order analysis with multiple me…</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–12: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="13-24" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">WHERE o2.order_date &lt; o.order_date</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 13–24: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="25-36" data-tint="3">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">ROUND(avg_order_value::numeric, 2) as aov,</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 25–36: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

### 2. Customer Segmentation

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
WITH customer_metrics AS (
    SELECT 
        c.customer_id,
        c.email,
        COUNT(o.order_id) as order_count,
        SUM(o.total_amount) as total_spent,
        MAX(o.order_date) as last_order_date,
        MIN(o.order_date) as first_order_date,
        COUNT(DISTINCT DATE_TRUNC('month', o.order_date)) as active_months,
        AVG(o.total_amount) as avg_order_value
    FROM customers c
    LEFT JOIN orders o ON c.customer_id = o.customer_id
    GROUP BY c.customer_id, c.email
)
SELECT 
    email,
    order_count,
    ROUND(total_spent::numeric, 2) as total_spent,
    last_order_date,
    first_order_date,
    active_months,
    ROUND(avg_order_value::numeric, 2) as avg_order_value,
    CASE 
        WHEN order_count = 0 THEN 'Never Ordered'
        WHEN last_order_date >= CURRENT_DATE - INTERVAL '30 days' THEN 'Active'
        WHEN last_order_date >= CURRENT_DATE - INTERVAL '90 days' THEN 'At Risk'
        ELSE 'Churned'
    END as customer_status,
    CASE 
        WHEN total_spent >= 1000 AND order_count >= 10 THEN 'VIP'
        WHEN total_spent >= 500 OR order_count >= 5 THEN 'Regular'
        WHEN order_count > 0 THEN 'New'
        ELSE 'Inactive'
    END as customer_segment
FROM customer_metrics
ORDER BY total_spent DESC NULLS LAST;
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-12" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">WITH customer_metrics AS (</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–12: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="13-24" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">GROUP BY c.customer_id, c.email</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 13–24: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="25-36" data-tint="3">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">WHEN last_order_date &gt;= CURRENT_DATE - INTERV…</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 25–36: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

### 3. Product Performance

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
WITH product_metrics AS (
    SELECT 
        p.product_id,
        p.name,
        p.category,
        p.price,
        COUNT(DISTINCT o.order_id) as order_count,
        SUM(oi.quantity) as units_sold,
        SUM(oi.quantity * oi.price_at_time) as revenue,
        COUNT(DISTINCT o.customer_id) as customer_count,
        AVG(r.rating) as avg_rating,
        COUNT(r.review_id) as review_count
    FROM products p
    LEFT JOIN order_items oi ON p.product_id = oi.product_id
    LEFT JOIN orders o ON oi.order_id = o.order_id
    LEFT JOIN reviews r ON p.product_id = r.product_id
    GROUP BY p.product_id, p.name, p.category, p.price
)
SELECT 
    name,
    category,
    price,
    order_count,
    units_sold,
    ROUND(revenue::numeric, 2) as revenue,
    customer_count,
    ROUND(avg_rating::numeric, 2) as avg_rating,
    review_count,
    ROUND(
        (revenue / NULLIF(units_sold, 0))::numeric,
        2
    ) as avg_selling_price,
    ROUND(
        (units_sold::float / NULLIF(customer_count, 0))::numeric,
        2
    ) as units_per_customer
FROM product_metrics
ORDER BY revenue DESC NULLS LAST;
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-12" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">WITH product_metrics AS (</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–12: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="13-25" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">FROM products p</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 13–25: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="26-38" data-tint="3">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Customer_count,</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 26–38: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

## Performance Optimization Examples

### 1. Index Usage

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
-- Create strategic indexes
CREATE INDEX idx_orders_customer_date 
ON orders(customer_id, order_date DESC);

CREATE INDEX idx_products_category_price 
ON products(category_id, price)
INCLUDE (name, stock_quantity);

-- Use indexes effectively
EXPLAIN ANALYZE
SELECT 
    c.name,
    COUNT(*) as order_count,
    SUM(o.total_amount) as total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE 
    o.order_date >= CURRENT_DATE - INTERVAL '30 days'
    AND o.total_amount > 100
GROUP BY c.customer_id, c.name;
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-10" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Create strategic indexes</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–10: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="11-20" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">SELECT</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 11–20: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

### 2. Query Optimization

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
-- Bad: Inefficient subquery
SELECT *
FROM orders
WHERE customer_id IN (
    SELECT customer_id
    FROM customers
    WHERE status = 'active'
);

-- Good: Use JOIN
SELECT o.*
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE c.status = 'active';

-- Better: Use EXISTS
SELECT o.*
FROM orders o
WHERE EXISTS (
    SELECT 1
    FROM customers c
    WHERE c.customer_id = o.customer_id
    AND c.status = 'active'
);
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-12" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Bad: Inefficient subquery</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–12: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="13-24" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">JOIN customers c ON o.customer_id = c.custome…</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 13–24: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

### 3. Batch Processing

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
-- Process large datasets in batches
DO $$
DECLARE
    batch_size INT := 1000;
    total_processed INT := 0;
    batch_count INT := 0;
BEGIN
    LOOP
        WITH batch AS (
            SELECT order_id
            FROM orders
            WHERE processed = false
            ORDER BY order_date
            LIMIT batch_size
            FOR UPDATE SKIP LOCKED
        )
        UPDATE orders o
        SET processed = true
        FROM batch b
        WHERE o.order_id = b.order_id;
        
        GET DIAGNOSTICS batch_count = ROW_COUNT;
        
        EXIT WHEN batch_count = 0;
        
        total_processed := total_processed + batch_count;
        RAISE NOTICE 'Processed % orders', total_processed;
        
        COMMIT;
    END LOOP;
END $$;
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-10" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Process large datasets in batches</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–10: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="11-20" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">FROM orders</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 11–20: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="21-31" data-tint="3">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">GET DIAGNOSTICS batch_count = ROW_COUNT;</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 21–31: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

## Common Pitfalls and Solutions

### 1. N+1 Query Problem

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
-- Bad: Separate query for each order
SELECT o.order_id, 
       (SELECT c.name FROM customers c WHERE c.id = o.customer_id) as customer_name
FROM orders o;

-- Good: Single JOIN query
SELECT o.order_id, c.name as customer_name
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id;
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-9" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Bad: Separate query for each order</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–9: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

### 2. Cartesian Products

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
-- Bad: Implicit cross join
SELECT * FROM orders, customers 
WHERE orders.customer_id = customers.customer_id;

-- Good: Explicit JOIN syntax
SELECT * FROM orders o
JOIN customers c ON o.customer_id = c.customer_id;
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-7" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Bad: Implicit cross join</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–7: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

### 3. NULL Handling

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
-- Bad: NULL comparison
SELECT * FROM products WHERE price = NULL;

-- Good: IS NULL operator
SELECT * FROM products WHERE price IS NULL;

-- Better: COALESCE for default values
SELECT 
    product_id,
    name,
    COALESCE(price, 0) as price,
    COALESCE(description, 'No description available') as description
FROM products;
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-13" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Bad: NULL comparison</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–13: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

## Best Practices Checklist

1. **Query Structure**
   - Use meaningful table aliases
   - Format queries for readability
   - Comment complex logic
   - Use CTEs for better organization

2. **Performance**
   - Create appropriate indexes
   - Filter early in the query
   - Avoid SELECT *
   - Use EXPLAIN ANALYZE

3. **Data Quality**
   - Handle NULL values appropriately
   - Validate input data
   - Use constraints
   - Implement error handling

4. **Maintenance**
   - Document queries
   - Use version control
   - Monitor performance
   - Regular optimization

Remember: "Clean, efficient queries lead to better performance and maintainability!"

## Next steps

- [Aggregations](aggregations.md) — **GROUP BY**, aggregate functions, **HAVING**
- [Joins](joins.md) — combine rows from multiple tables
- [Advanced SQL Concepts](advanced-concepts.md) — window functions, CTEs, and optimization
