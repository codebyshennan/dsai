# Advanced SQL Concepts: Beyond the Basics

**After this lesson:** You can use **CTEs** (Common Table Expressions) to structure complex queries, apply **window functions** for rankings and running metrics, and read **EXPLAIN** output to spot expensive scans.

## Helpful video

High-level introduction to SQL and relational databases.

<iframe width="560" height="315" src="https://www.youtube.com/embed/27axs9dO7AE" title="What is SQL?" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Overview

**Prerequisites:** Solid comfort with [Joins](joins.md) and [Aggregations](aggregations.md). This lesson goes deeper than day-one analyst SQL—take breaks and run examples in your own database.

> **Time needed:** 90+ minutes; split across sessions if needed.

> **Warning:** Dialects differ (PostgreSQL vs SQL Server vs BigQuery). Treat advanced snippets as patterns and check your engine’s docs for exact syntax.

## Why this matters

Readable SQL survives code review and production debugging. **CTEs** break big questions into named steps; **window functions** answer “rank within group” without self-joins; **EXPLAIN** shows whether the database is scanning whole tables or using indexes. Together, these are the bridge from “it runs” to “it runs efficiently.”

## Introduction to Advanced SQL

SQL mastery goes beyond basic CRUD operations. Advanced SQL concepts enable you to:

- Write complex, performant queries
- Handle large-scale data processing
- Implement sophisticated business logic
- Optimize database operations

## Advanced SQL Functions

### 1. JSON Operations

Applications often store nested payloads (orders with line items, flexible attributes) as **JSON** next to relational columns. Database engines expose functions to build, query, and unnest JSON so you can stay in SQL for many reporting tasks instead of exporting everything to Python first.

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
-- JSON creation and manipulation
SELECT 
    order_id,
    jsonb_build_object(
        'customer', customer_name,
        'items', (
            SELECT jsonb_agg(
                jsonb_build_object(
                    'product', product_name,
                    'quantity', quantity,
                    'price', price
                )
            )
            FROM order_items oi
            JOIN products p ON oi.product_id = p.product_id
            WHERE oi.order_id = o.order_id
        )
    ) as order_details
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id;

-- JSON querying
SELECT 
    order_id,
    order_details -> 'customer' as customer,
    jsonb_array_length(order_details -> 'items') as item_count,
    jsonb_path_query_array(
        order_details,
        '$.items[*].price'
    ) as prices
FROM order_details_json;
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-10" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">JSON creation and manipulation</span>
    </div>
    <div class="code-callout__body">
      <p><strong>JSON creation and manipulation</strong> — lines 1-10 in the highlighted code. Identify what this band does: DDL (table/column definitions), row changes (<code>INSERT</code>/<code>UPDATE</code>/<code>DELETE</code>), or a <code>SELECT</code> pipeline—then read joins and predicates in snippet order.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="11-20" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">&#x27;price&#x27;, price</span>
    </div>
    <div class="code-callout__body">
      <p><strong>&#x27;price&#x27;, price</strong> — lines 11-20 in the highlighted code. Identify what this band does: DDL (table/column definitions), row changes (<code>INSERT</code>/<code>UPDATE</code>/<code>DELETE</code>), or a <code>SELECT</code> pipeline—then read joins and predicates in snippet order.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="21-31" data-tint="3">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">JSON querying</span>
    </div>
    <div class="code-callout__body">
      <p><strong>JSON querying</strong> — lines 21-31 in the highlighted code. Identify what this band does: DDL (table/column definitions), row changes (<code>INSERT</code>/<code>UPDATE</code>/<code>DELETE</code>), or a <code>SELECT</code> pipeline—then read joins and predicates in snippet order.</p>
    </div>
  </div>
</aside>
</div>

### 2. Full-Text Search

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
-- Create search vectors
CREATE INDEX idx_products_search ON products USING gin(
    to_tsvector('english', 
        coalesce(name,'') || ' ' || 
        coalesce(description,'') || ' ' || 
        coalesce(category,'')
    )
);

-- Perform search with ranking
SELECT 
    name,
    description,
    ts_rank(
        to_tsvector('english', 
            coalesce(name,'') || ' ' || 
            coalesce(description,'') || ' ' || 
            coalesce(category,'')
        ),
        plainto_tsquery('english', 'search term')
    ) as relevance
FROM products
WHERE to_tsvector('english', 
    coalesce(name,'') || ' ' || 
    coalesce(description,'') || ' ' || 
    coalesce(category,'')
) @@ plainto_tsquery('english', 'search term')
ORDER BY relevance DESC;
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-14" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Create search vectors</span>
    </div>
    <div class="code-callout__body">
      <p><strong>Create search vectors</strong> — lines 1-14 in the highlighted code. Identify what this band does: DDL (table/column definitions), row changes (<code>INSERT</code>/<code>UPDATE</code>/<code>DELETE</code>), or a <code>SELECT</code> pipeline—then read joins and predicates in snippet order.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="15-28" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">To_tsvector(&#x27;english&#x27;,</span>
    </div>
    <div class="code-callout__body">
      <p><strong>To_tsvector(&#x27;english&#x27;,</strong> — lines 15-28 in the highlighted code. Identify what this band does: DDL (table/column definitions), row changes (<code>INSERT</code>/<code>UPDATE</code>/<code>DELETE</code>), or a <code>SELECT</code> pipeline—then read joins and predicates in snippet order.</p>
    </div>
  </div>
</aside>
</div>

### 3. Recursive Queries

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
-- Employee hierarchy
WITH RECURSIVE employee_hierarchy AS (
    -- Base case: top-level employees
    SELECT 
        employee_id,
        name,
        manager_id,
        1 as level,
        ARRAY[name] as path
    FROM employees
    WHERE manager_id IS NULL
    
    UNION ALL
    
    -- Recursive case: employees with managers
    SELECT 
        e.employee_id,
        e.name,
        e.manager_id,
        eh.level + 1,
        eh.path || e.name
    FROM employees e
    JOIN employee_hierarchy eh ON e.manager_id = eh.employee_id
)
SELECT 
    level,
    lpad(' ', (level-1)*2) || name as employee,
    array_to_string(path, ' -> ') as hierarchy_path
FROM employee_hierarchy
ORDER BY path;
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-15" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Employee hierarchy</span>
    </div>
    <div class="code-callout__body">
      <p><strong>Employee hierarchy</strong> — lines 1-15 in the highlighted code. Identify what this band does: DDL (table/column definitions), row changes (<code>INSERT</code>/<code>UPDATE</code>/<code>DELETE</code>), or a <code>SELECT</code> pipeline—then read joins and predicates in snippet order.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="16-30" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">SELECT</span>
    </div>
    <div class="code-callout__body">
      <p><strong>SELECT</strong> — lines 16-30 in the highlighted code. Identify what this band does: DDL (table/column definitions), row changes (<code>INSERT</code>/<code>UPDATE</code>/<code>DELETE</code>), or a <code>SELECT</code> pipeline—then read joins and predicates in snippet order.</p>
    </div>
  </div>
</aside>
</div>

## Window Functions Deep Dive

### 1. Advanced Framing

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
SELECT 
    date,
    amount,
    -- Different frame specifications
    SUM(amount) OVER (
        ORDER BY date
        ROWS BETWEEN 
            UNBOUNDED PRECEDING 
            AND CURRENT ROW
    ) as cumulative_sum,
    
    AVG(amount) OVER (
        ORDER BY date
        ROWS BETWEEN 
            3 PRECEDING 
            AND 1 FOLLOWING
    ) as centered_average,
    
    SUM(amount) OVER (
        ORDER BY date
        RANGE BETWEEN 
            INTERVAL '1 month' PRECEDING 
            AND CURRENT ROW
    ) as rolling_monthly_sum
FROM transactions;
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-12" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">SELECT</span>
    </div>
    <div class="code-callout__body">
      <p><strong>SELECT</strong> — lines 1-12 in the highlighted code. Identify what this band does: DDL (table/column definitions), row changes (<code>INSERT</code>/<code>UPDATE</code>/<code>DELETE</code>), or a <code>SELECT</code> pipeline—then read joins and predicates in snippet order.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="13-25" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">ORDER BY date</span>
    </div>
    <div class="code-callout__body">
      <p><strong>ORDER BY date</strong> — lines 13-25 in the highlighted code. Identify what this band does: DDL (table/column definitions), row changes (<code>INSERT</code>/<code>UPDATE</code>/<code>DELETE</code>), or a <code>SELECT</code> pipeline—then read joins and predicates in snippet order.</p>
    </div>
  </div>
</aside>
</div>

### 2. Multiple Window Functions

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
SELECT 
    category,
    product_name,
    price,
    -- Rankings within category
    RANK() OVER w1 as price_rank,
    DENSE_RANK() OVER w1 as dense_rank,
    ROW_NUMBER() OVER w1 as row_num,
    
    -- Statistics within category
    AVG(price) OVER w2 as avg_price,
    price - AVG(price) OVER w2 as price_diff,
    
    -- Percentiles within category
    NTILE(4) OVER w1 as price_quartile,
    PERCENT_RANK() OVER w1 as price_percentile
FROM products
WINDOW 
    w1 as (PARTITION BY category ORDER BY price DESC),
    w2 as (PARTITION BY category);
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-10" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">SELECT</span>
    </div>
    <div class="code-callout__body">
      <p><strong>SELECT</strong> — lines 1-10 in the highlighted code. Identify what this band does: DDL (table/column definitions), row changes (<code>INSERT</code>/<code>UPDATE</code>/<code>DELETE</code>), or a <code>SELECT</code> pipeline—then read joins and predicates in snippet order.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="11-20" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">AVG(price) OVER w2 as avg_price,</span>
    </div>
    <div class="code-callout__body">
      <p><strong>AVG(price) OVER w2 as avg_price,</strong> — lines 11-20 in the highlighted code. Identify what this band does: DDL (table/column definitions), row changes (<code>INSERT</code>/<code>UPDATE</code>/<code>DELETE</code>), or a <code>SELECT</code> pipeline—then read joins and predicates in snippet order.</p>
    </div>
  </div>
</aside>
</div>

## Advanced Joins and Set Operations

### 1. Lateral Joins

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
SELECT 
    c.customer_name,
    recent_orders.order_id,
    recent_orders.order_date,
    recent_orders.amount
FROM customers c
CROSS JOIN LATERAL (
    SELECT 
        order_id,
        order_date,
        total_amount as amount
    FROM orders o
    WHERE o.customer_id = c.customer_id
    ORDER BY order_date DESC
    LIMIT 3
) recent_orders;
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-8" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">SELECT</span>
    </div>
    <div class="code-callout__body">
      <p><strong>SELECT</strong> — lines 1-8 in the highlighted code. Identify what this band does: DDL (table/column definitions), row changes (<code>INSERT</code>/<code>UPDATE</code>/<code>DELETE</code>), or a <code>SELECT</code> pipeline—then read joins and predicates in snippet order.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="9-16" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Order_id,</span>
    </div>
    <div class="code-callout__body">
      <p><strong>Order_id,</strong> — lines 9-16 in the highlighted code. Identify what this band does: DDL (table/column definitions), row changes (<code>INSERT</code>/<code>UPDATE</code>/<code>DELETE</code>), or a <code>SELECT</code> pipeline—then read joins and predicates in snippet order.</p>
    </div>
  </div>
</aside>
</div>

### 2. Set Operations with Ordering

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
-- Complex set operations
(
    SELECT 
        'Current' as period,
        category,
        SUM(amount) as total_sales
    FROM sales
    WHERE date >= CURRENT_DATE - INTERVAL '1 month'
    GROUP BY category
)
UNION ALL
(
    SELECT 
        'Previous' as period,
        category,
        SUM(amount) as total_sales
    FROM sales
    WHERE 
        date >= CURRENT_DATE - INTERVAL '2 months' AND
        date < CURRENT_DATE - INTERVAL '1 month'
    GROUP BY category
)
ORDER BY 
    category,
    period DESC;
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-12" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Complex set operations</span>
    </div>
    <div class="code-callout__body">
      <p><strong>Complex set operations</strong> — lines 1-12 in the highlighted code. Identify what this band does: DDL (table/column definitions), row changes (<code>INSERT</code>/<code>UPDATE</code>/<code>DELETE</code>), or a <code>SELECT</code> pipeline—then read joins and predicates in snippet order.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="13-25" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">SELECT</span>
    </div>
    <div class="code-callout__body">
      <p><strong>SELECT</strong> — lines 13-25 in the highlighted code. Identify what this band does: DDL (table/column definitions), row changes (<code>INSERT</code>/<code>UPDATE</code>/<code>DELETE</code>), or a <code>SELECT</code> pipeline—then read joins and predicates in snippet order.</p>
    </div>
  </div>
</aside>
</div>

## Error Handling and Transactions

### 1. Transaction Management

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
-- Complex transaction with savepoints
BEGIN;

SAVEPOINT order_start;

-- Create order
INSERT INTO orders (customer_id, order_date, status)
VALUES (123, CURRENT_TIMESTAMP, 'pending')
RETURNING order_id INTO v_order_id;

-- Check inventory and update stock
UPDATE products
SET stock_quantity = stock_quantity - order_quantity
WHERE product_id = v_product_id
AND stock_quantity >= order_quantity;

IF NOT FOUND THEN
    ROLLBACK TO order_start;
    RAISE EXCEPTION 'Insufficient stock for product %', v_product_id;
END IF;

-- Process payment
SAVEPOINT payment;

BEGIN
    -- Payment processing logic
    IF payment_failed THEN
        ROLLBACK TO payment;
        RAISE EXCEPTION 'Payment failed';
    END IF;
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK TO payment;
        RAISE;
END;

COMMIT;
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-12" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Complex transaction with savepoints</span>
    </div>
    <div class="code-callout__body">
      <p><strong>Complex transaction with savepoints</strong> — lines 1-12. The <code>WITH</code> clause names intermediate result sets; the outer query reads from them like views. Recursive CTEs union the base case with repeated expansion.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="13-24" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">SET stock_quantity = stock_quantity - order_q…</span>
    </div>
    <div class="code-callout__body">
      <p><strong>SET stock_quantity = stock_quantity - order_q…</strong> — lines 13-24 in the highlighted code. Identify what this band does: DDL (table/column definitions), row changes (<code>INSERT</code>/<code>UPDATE</code>/<code>DELETE</code>), or a <code>SELECT</code> pipeline—then read joins and predicates in snippet order.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="25-37" data-tint="3">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">BEGIN</span>
    </div>
    <div class="code-callout__body">
      <p><strong>BEGIN</strong> — lines 25-37 in the highlighted code. Identify what this band does: DDL (table/column definitions), row changes (<code>INSERT</code>/<code>UPDATE</code>/<code>DELETE</code>), or a <code>SELECT</code> pipeline—then read joins and predicates in snippet order.</p>
    </div>
  </div>
</aside>
</div>

### 2. Error Handling

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
CREATE OR REPLACE FUNCTION process_order(
    p_customer_id INT,
    p_items JSONB
) RETURNS INT AS $$
DECLARE
    v_order_id INT;
    v_item JSONB;
    v_total DECIMAL(10,2) := 0;
BEGIN
    -- Input validation
    IF p_items IS NULL OR jsonb_array_length(p_items) = 0 THEN
        RAISE EXCEPTION 'Order must contain at least one item';
    END IF;
    
    -- Start transaction
    BEGIN
        -- Create order
        INSERT INTO orders (customer_id, order_date, status)
        VALUES (p_customer_id, CURRENT_TIMESTAMP, 'pending')
        RETURNING order_id INTO v_order_id;
        
        -- Process items
        FOR v_item IN SELECT * FROM jsonb_array_elements(p_items)
        LOOP
            -- Add order item
            BEGIN
                INSERT INTO order_items (
                    order_id, 
                    product_id,
                    quantity,
                    price
                )
                VALUES (
                    v_order_id,
                    (v_item->>'product_id')::INT,
                    (v_item->>'quantity')::INT,
                    (v_item->>'price')::DECIMAL
                );
            EXCEPTION
                WHEN foreign_key_violation THEN
                    RAISE EXCEPTION 'Invalid product ID: %',
                        (v_item->>'product_id');
                WHEN numeric_value_out_of_range THEN
                    RAISE EXCEPTION 'Invalid quantity or price for product %',
                        (v_item->>'product_id');
            END;
            
            -- Update total
            v_total := v_total + 
                ((v_item->>'quantity')::INT * (v_item->>'price')::DECIMAL);
        END LOOP;
        
        -- Update order total
        UPDATE orders 
        SET total_amount = v_total,
            status = 'confirmed'
        WHERE order_id = v_order_id;
        
        RETURN v_order_id;
    EXCEPTION
        WHEN OTHERS THEN
            RAISE EXCEPTION 'Order processing failed: %', SQLERRM;
    END;
END;
$$ LANGUAGE plpgsql;
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-13" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">CREATE OR REPLACE FUNCTION process_order(</span>
    </div>
    <div class="code-callout__body">
      <p><strong>CREATE OR REPLACE FUNCTION process_order(</strong> — lines 1-13 in the highlighted code. Identify what this band does: DDL (table/column definitions), row changes (<code>INSERT</code>/<code>UPDATE</code>/<code>DELETE</code>), or a <code>SELECT</code> pipeline—then read joins and predicates in snippet order.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="14-26" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Start transaction</span>
    </div>
    <div class="code-callout__body">
      <p><strong>Start transaction</strong> — lines 14-26 in the highlighted code. Identify what this band does: DDL (table/column definitions), row changes (<code>INSERT</code>/<code>UPDATE</code>/<code>DELETE</code>), or a <code>SELECT</code> pipeline—then read joins and predicates in snippet order.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="27-39" data-tint="3">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">INSERT INTO order_items (</span>
    </div>
    <div class="code-callout__body">
      <p><strong>INSERT INTO order_items (</strong> — lines 27-39 in the highlighted code. Identify what this band does: DDL (table/column definitions), row changes (<code>INSERT</code>/<code>UPDATE</code>/<code>DELETE</code>), or a <code>SELECT</code> pipeline—then read joins and predicates in snippet order.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="40-52" data-tint="4">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">WHEN foreign_key_violation THEN</span>
    </div>
    <div class="code-callout__body">
      <p><strong>WHEN foreign_key_violation THEN</strong> — lines 40-52 in the highlighted code. Identify what this band does: DDL (table/column definitions), row changes (<code>INSERT</code>/<code>UPDATE</code>/<code>DELETE</code>), or a <code>SELECT</code> pipeline—then read joins and predicates in snippet order.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="53-65" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Update order total</span>
    </div>
    <div class="code-callout__body">
      <p><strong>Update order total</strong> — lines 53-65 in the highlighted code. Identify what this band does: DDL (table/column definitions), row changes (<code>INSERT</code>/<code>UPDATE</code>/<code>DELETE</code>), or a <code>SELECT</code> pipeline—then read joins and predicates in snippet order.</p>
    </div>
  </div>
</aside>
</div>

## Additional Real-World Scenarios

### 1. E-commerce Funnel Analysis

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
WITH user_journey AS (
    SELECT 
        u.user_id,
        u.email,
        COUNT(DISTINCT CASE WHEN e.event_type = 'view' THEN e.product_id END) as products_viewed,
        COUNT(DISTINCT CASE WHEN e.event_type = 'add_to_cart' THEN e.product_id END) as products_carted,
        COUNT(DISTINCT CASE WHEN e.event_type = 'purchase' THEN e.product_id END) as products_purchased,
        COUNT(DISTINCT CASE WHEN e.event_type = 'purchase' THEN e.session_id END) as purchase_sessions,
        COUNT(DISTINCT e.session_id) as total_sessions
    FROM users u
    LEFT JOIN events e ON u.user_id = e.user_id
    GROUP BY u.user_id, u.email
)
SELECT 
    ROUND(AVG(products_viewed)::numeric, 2) as avg_products_viewed,
    ROUND(AVG(products_carted)::numeric, 2) as avg_products_carted,
    ROUND(AVG(products_purchased)::numeric, 2) as avg_products_purchased,
    ROUND(
        100.0 * SUM(CASE WHEN products_carted > 0 THEN 1 END) / 
        NULLIF(SUM(CASE WHEN products_viewed > 0 THEN 1 END), 0),
        2
    ) as view_to_cart_rate,
    ROUND(
        100.0 * SUM(CASE WHEN products_purchased > 0 THEN 1 END) / 
        NULLIF(SUM(CASE WHEN products_carted > 0 THEN 1 END), 0),
        2
    ) as cart_to_purchase_rate
FROM user_journey;
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-14" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">WITH user_journey AS (</span>
    </div>
    <div class="code-callout__body">
      <p><strong>WITH user_journey AS (</strong> — lines 1-14. The <code>WITH</code> clause names intermediate result sets; the outer query reads from them like views. Recursive CTEs union the base case with repeated expansion.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="15-28" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">ROUND(AVG(products_viewed)::numeric, 2) as av…</span>
    </div>
    <div class="code-callout__body">
      <p><strong>ROUND(AVG(products_viewed)::numeric, 2) as av…</strong> — lines 15-28 in the highlighted code. Identify what this band does: DDL (table/column definitions), row changes (<code>INSERT</code>/<code>UPDATE</code>/<code>DELETE</code>), or a <code>SELECT</code> pipeline—then read joins and predicates in snippet order.</p>
    </div>
  </div>
</aside>
</div>

### 2. Fraud Detection System

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
WITH transaction_metrics AS (
    SELECT 
        t.transaction_id,
        t.user_id,
        t.amount,
        t.created_at,
        t.status,
        -- Time since last transaction
        EXTRACT(EPOCH FROM (
            t.created_at - LAG(t.created_at) OVER (
                PARTITION BY t.user_id 
                ORDER BY t.created_at
            )
        ))/60 as minutes_since_last_txn,
        -- Amount compared to user's average
        amount / NULLIF(AVG(amount) OVER (
            PARTITION BY t.user_id
        ), 0) as amount_vs_avg,
        -- Number of transactions in last hour
        COUNT(*) OVER (
            PARTITION BY t.user_id 
            ORDER BY t.created_at 
            RANGE BETWEEN INTERVAL '1 hour' PRECEDING 
            AND CURRENT ROW
        ) as txns_last_hour,
        -- Different locations in last 24 hours
        COUNT(DISTINCT location_id) OVER (
            PARTITION BY t.user_id 
            ORDER BY t.created_at 
            RANGE BETWEEN INTERVAL '24 hours' PRECEDING 
            AND CURRENT ROW
        ) as locations_24h
    FROM transactions t
)
SELECT 
    transaction_id,
    user_id,
    amount,
    created_at,
    CASE 
        WHEN minutes_since_last_txn < 1 
        AND amount_vs_avg > 3 THEN 'High Risk: Rapid Large Transaction'
        WHEN txns_last_hour > 10 THEN 'High Risk: High Frequency'
        WHEN locations_24h > 3 THEN 'High Risk: Multiple Locations'
        WHEN amount_vs_avg > 5 THEN 'Medium Risk: Unusual Amount'
        WHEN minutes_since_last_txn < 5 THEN 'Medium Risk: Rapid Transactions'
        ELSE 'Low Risk'
    END as risk_assessment
FROM transaction_metrics
WHERE 
    minutes_since_last_txn < 5 
    OR amount_vs_avg > 3 
    OR txns_last_hour > 10 
    OR locations_24h > 3;
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-13" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">WITH transaction_metrics AS (</span>
    </div>
    <div class="code-callout__body">
      <p><strong>WITH transaction_metrics AS (</strong> — lines 1-13. The <code>WITH</code> clause names intermediate result sets; the outer query reads from them like views. Recursive CTEs union the base case with repeated expansion.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="14-27" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">))/60 as minutes_since_last_txn,</span>
    </div>
    <div class="code-callout__body">
      <p><strong>))/60 as minutes_since_last_txn,</strong> — lines 14-27 in the highlighted code. Identify what this band does: DDL (table/column definitions), row changes (<code>INSERT</code>/<code>UPDATE</code>/<code>DELETE</code>), or a <code>SELECT</code> pipeline—then read joins and predicates in snippet order.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="28-40" data-tint="3">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">PARTITION BY t.user_id</span>
    </div>
    <div class="code-callout__body">
      <p><strong>PARTITION BY t.user_id</strong> — lines 28-40 in the highlighted code. Identify what this band does: DDL (table/column definitions), row changes (<code>INSERT</code>/<code>UPDATE</code>/<code>DELETE</code>), or a <code>SELECT</code> pipeline—then read joins and predicates in snippet order.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="41-54" data-tint="4">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">WHEN minutes_since_last_txn &lt; 1</span>
    </div>
    <div class="code-callout__body">
      <p><strong>WHEN minutes_since_last_txn &lt; 1</strong> — lines 41-54 in the highlighted code. Identify what this band does: DDL (table/column definitions), row changes (<code>INSERT</code>/<code>UPDATE</code>/<code>DELETE</code>), or a <code>SELECT</code> pipeline—then read joins and predicates in snippet order.</p>
    </div>
  </div>
</aside>
</div>

### 3. Inventory Optimization

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
WITH inventory_metrics AS (
    SELECT 
        p.product_id,
        p.name,
        p.category,
        p.stock_quantity,
        p.reorder_point,
        p.lead_time_days,
        -- Sales velocity
        SUM(oi.quantity) FILTER (
            WHERE o.order_date >= CURRENT_DATE - INTERVAL '30 days'
        ) as units_sold_30d,
        -- Stockout incidents
        COUNT(*) FILTER (
            WHERE p.stock_quantity = 0
        ) as stockout_count,
        -- Average daily sales
        COALESCE(
            SUM(oi.quantity) FILTER (
                WHERE o.order_date >= CURRENT_DATE - INTERVAL '90 days'
            )::float / 90,
            0
        ) as avg_daily_sales,
        -- Safety stock calculation
        SQRT(
            POWER(p.lead_time_days * STDDEV(oi.quantity), 2) +
            POWER(AVG(oi.quantity) * STDDEV(p.lead_time_days), 2)
        ) as safety_stock
    FROM products p
    LEFT JOIN order_items oi ON p.product_id = oi.product_id
    LEFT JOIN orders o ON oi.order_id = o.order_id
    GROUP BY 
        p.product_id, p.name, p.category, 
        p.stock_quantity, p.reorder_point, p.lead_time_days
)
SELECT 
    name,
    category,
    stock_quantity,
    units_sold_30d,
    ROUND(avg_daily_sales::numeric, 2) as avg_daily_sales,
    ROUND(safety_stock::numeric, 2) as recommended_safety_stock,
    CASE 
        WHEN stock_quantity = 0 THEN 'Out of Stock'
        WHEN stock_quantity < safety_stock THEN 'Below Safety Stock'
        WHEN stock_quantity < reorder_point THEN 'Reorder Needed'
        ELSE 'Adequate Stock'
    END as stock_status,
    CEIL(
        CASE 
            WHEN avg_daily_sales > 0 
            THEN stock_quantity / avg_daily_sales
            ELSE NULL
        END
    ) as days_of_inventory,
    ROUND(
        GREATEST(
            reorder_point - stock_quantity,
            (avg_daily_sales * lead_time_days) - stock_quantity,
            0
        )::numeric,
        0
    ) as suggested_order_quantity
FROM inventory_metrics
ORDER BY 
    CASE 
        WHEN stock_quantity = 0 THEN 1
        WHEN stock_quantity < safety_stock THEN 2
        WHEN stock_quantity < reorder_point THEN 3
        ELSE 4
    END,
    avg_daily_sales DESC;
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-14" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">WITH inventory_metrics AS (</span>
    </div>
    <div class="code-callout__body">
      <p><strong>WITH inventory_metrics AS (</strong> — lines 1-14. The <code>WITH</code> clause names intermediate result sets; the outer query reads from them like views. Recursive CTEs union the base case with repeated expansion.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="15-28" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">WHERE p.stock_quantity = 0</span>
    </div>
    <div class="code-callout__body">
      <p><strong>WHERE p.stock_quantity = 0</strong> — lines 15-28 in the highlighted code. Identify what this band does: DDL (table/column definitions), row changes (<code>INSERT</code>/<code>UPDATE</code>/<code>DELETE</code>), or a <code>SELECT</code> pipeline—then read joins and predicates in snippet order.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="29-43" data-tint="3">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">FROM products p</span>
    </div>
    <div class="code-callout__body">
      <p><strong>FROM products p</strong> — lines 29-43 in the highlighted code. Identify what this band does: DDL (table/column definitions), row changes (<code>INSERT</code>/<code>UPDATE</code>/<code>DELETE</code>), or a <code>SELECT</code> pipeline—then read joins and predicates in snippet order.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="44-57" data-tint="4">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">WHEN stock_quantity = 0 THEN &#x27;Out of Stock&#x27;</span>
    </div>
    <div class="code-callout__body">
      <p><strong>WHEN stock_quantity = 0 THEN &#x27;Out of Stock&#x27;</strong> — lines 44-57 in the highlighted code. Identify what this band does: DDL (table/column definitions), row changes (<code>INSERT</code>/<code>UPDATE</code>/<code>DELETE</code>), or a <code>SELECT</code> pipeline—then read joins and predicates in snippet order.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="58-72" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Reorder_point - stock_quantity,</span>
    </div>
    <div class="code-callout__body">
      <p><strong>Reorder_point - stock_quantity,</strong> — lines 58-72 in the highlighted code. Identify what this band does: DDL (table/column definitions), row changes (<code>INSERT</code>/<code>UPDATE</code>/<code>DELETE</code>), or a <code>SELECT</code> pipeline—then read joins and predicates in snippet order.</p>
    </div>
  </div>
</aside>
</div>

## Performance Optimization Tips

### 1. Query Plan Analysis

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
-- Analyze and explain complex queries
EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON)
SELECT 
    c.customer_name,
    COUNT(*) as order_count,
    SUM(o.total_amount) as total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE 
    o.order_date >= CURRENT_DATE - INTERVAL '1 year'
    AND o.total_amount > 100
GROUP BY c.customer_id, c.customer_name
HAVING COUNT(*) > 5
ORDER BY total_spent DESC;

-- Key metrics to monitor:
-- 1. Planning Time
-- 2. Execution Time
-- 3. Actual vs. Planned Rows
-- 4. Buffer Usage (shared_blks_hit vs. shared_blks_read)
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-10" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Analyze and explain complex queries</span>
    </div>
    <div class="code-callout__body">
      <p><strong>Analyze and explain complex queries</strong> — lines 1-10. <code>EXPLAIN</code> (or <code>EXPLAIN ANALYZE</code>) shows the plan: scan types, join order, and cost estimates.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="11-20" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">AND o.total_amount &gt; 100</span>
    </div>
    <div class="code-callout__body">
      <p><strong>AND o.total_amount &gt; 100</strong> — lines 11-20 in the highlighted code. Identify what this band does: DDL (table/column definitions), row changes (<code>INSERT</code>/<code>UPDATE</code>/<code>DELETE</code>), or a <code>SELECT</code> pipeline—then read joins and predicates in snippet order.</p>
    </div>
  </div>
</aside>
</div>

### 2. Index Design Patterns

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
-- Composite indexes for range + equality
CREATE INDEX idx_orders_customer_date 
ON orders(customer_id, order_date DESC);

-- Partial indexes for specific queries
CREATE INDEX idx_high_value_orders 
ON orders(order_date)
WHERE total_amount > 1000;

-- Expression indexes for function calls
CREATE INDEX idx_order_date_truncated 
ON orders(DATE_TRUNC('month', order_date));

-- Include columns to avoid table lookups
CREATE INDEX idx_orders_customer_details 
ON orders(customer_id)
INCLUDE (order_date, total_amount, status);
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-8" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Composite indexes for range + equality</span>
    </div>
    <div class="code-callout__body">
      <p><strong>Composite indexes for range + equality</strong> — lines 1-8 in the highlighted code. Identify what this band does: DDL (table/column definitions), row changes (<code>INSERT</code>/<code>UPDATE</code>/<code>DELETE</code>), or a <code>SELECT</code> pipeline—then read joins and predicates in snippet order.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="9-17" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Expression indexes for function calls</span>
    </div>
    <div class="code-callout__body">
      <p><strong>Expression indexes for function calls</strong> — lines 9-17 in the highlighted code. Identify what this band does: DDL (table/column definitions), row changes (<code>INSERT</code>/<code>UPDATE</code>/<code>DELETE</code>), or a <code>SELECT</code> pipeline—then read joins and predicates in snippet order.</p>
    </div>
  </div>
</aside>
</div>

### 3. Materialized Views with Refresh Strategies

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
-- Create materialized view
CREATE MATERIALIZED VIEW sales_summary AS
SELECT 
    DATE_TRUNC('day', order_date) as sale_date,
    category,
    SUM(total_amount) as revenue,
    COUNT(*) as order_count
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
GROUP BY 
    DATE_TRUNC('day', order_date),
    category;

-- Create indexes on materialized view
CREATE INDEX idx_sales_summary_date 
ON sales_summary(sale_date DESC);

CREATE INDEX idx_sales_summary_category 
ON sales_summary(category, sale_date DESC);

-- Refresh strategy
CREATE OR REPLACE FUNCTION refresh_sales_summary()
RETURNS trigger AS $$
BEGIN
    REFRESH MATERIALIZED VIEW CONCURRENTLY sales_summary;
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

-- Trigger for automatic refresh
CREATE TRIGGER refresh_sales_summary_trigger
AFTER INSERT OR UPDATE OR DELETE ON orders
FOR EACH STATEMENT
EXECUTE FUNCTION refresh_sales_summary();
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-11" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Create materialized view</span>
    </div>
    <div class="code-callout__body">
      <p><strong>Create materialized view</strong> — lines 1-11 in the highlighted code. Identify what this band does: DDL (table/column definitions), row changes (<code>INSERT</code>/<code>UPDATE</code>/<code>DELETE</code>), or a <code>SELECT</code> pipeline—then read joins and predicates in snippet order.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="12-23" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">DATE_TRUNC(&#x27;day&#x27;, order_date),</span>
    </div>
    <div class="code-callout__body">
      <p><strong>DATE_TRUNC(&#x27;day&#x27;, order_date),</strong> — lines 12-23 in the highlighted code. Identify what this band does: DDL (table/column definitions), row changes (<code>INSERT</code>/<code>UPDATE</code>/<code>DELETE</code>), or a <code>SELECT</code> pipeline—then read joins and predicates in snippet order.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="24-35" data-tint="3">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">RETURNS trigger AS $$</span>
    </div>
    <div class="code-callout__body">
      <p><strong>RETURNS trigger AS $$</strong> — lines 24-35 in the highlighted code. Identify what this band does: DDL (table/column definitions), row changes (<code>INSERT</code>/<code>UPDATE</code>/<code>DELETE</code>), or a <code>SELECT</code> pipeline—then read joins and predicates in snippet order.</p>
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
SELECT 
    o.order_id,
    (
        SELECT c.name 
        FROM customers c 
        WHERE c.id = o.customer_id
    ) as customer_name,
    (
        SELECT COUNT(*) 
        FROM order_items oi 
        WHERE oi.order_id = o.order_id
    ) as item_count
FROM orders o;

-- Good: Use JOINs and window functions
SELECT 
    o.order_id,
    c.name as customer_name,
    COUNT(*) OVER (PARTITION BY o.order_id) as item_count
FROM orders o
JOIN customers c ON o.customer_id = c.id
JOIN order_items oi ON o.order_id = oi.order_id;
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-11" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Bad: Separate query for each order</span>
    </div>
    <div class="code-callout__body">
      <p><strong>Bad: Separate query for each order</strong> — lines 1-11 in the snippet. Contrast this with the alternative below; the goal is to avoid accidental cartesian products, non-sargable predicates, or silent data loss.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="12-23" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">WHERE oi.order_id = o.order_id</span>
    </div>
    <div class="code-callout__body">
      <p><strong>WHERE oi.order_id = o.order_id</strong> — lines 12-23 in the highlighted code. Identify what this band does: DDL (table/column definitions), row changes (<code>INSERT</code>/<code>UPDATE</code>/<code>DELETE</code>), or a <code>SELECT</code> pipeline—then read joins and predicates in snippet order.</p>
    </div>
  </div>
</aside>
</div>

### 2. Inefficient Date Handling

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
-- Bad: Function on column prevents index use
SELECT * 
FROM orders 
WHERE EXTRACT(YEAR FROM order_date) = 2023;

-- Good: Range condition uses index
SELECT * 
FROM orders 
WHERE order_date >= '2023-01-01' 
AND order_date < '2024-01-01';
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-10" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Bad: Function on column prevents index use</span>
    </div>
    <div class="code-callout__body">
      <p><strong>Bad: Function on column prevents index use</strong> — lines 1-10 in the snippet. Contrast this with the alternative below; the goal is to avoid accidental cartesian products, non-sargable predicates, or silent data loss.</p>
    </div>
  </div>
</aside>
</div>

### 3. Subquery Performance

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
-- Bad: Correlated subquery runs for each row
SELECT 
    product_name,
    (
        SELECT AVG(quantity)
        FROM order_items oi
        WHERE oi.product_id = p.product_id
    ) as avg_quantity
FROM products p;

-- Good: Use window functions or JOIN
SELECT 
    p.product_name,
    AVG(oi.quantity) OVER (
        PARTITION BY p.product_id
    ) as avg_quantity
FROM products p
LEFT JOIN order_items oi ON p.product_id = oi.product_id;
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-9" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Bad: Correlated subquery runs for each row</span>
    </div>
    <div class="code-callout__body">
      <p><strong>Bad: Correlated subquery runs for each row</strong> — lines 1-9 in the snippet. Contrast this with the alternative below; the goal is to avoid accidental cartesian products, non-sargable predicates, or silent data loss.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="10-18" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Good: Use window functions or JOIN</span>
    </div>
    <div class="code-callout__body">
      <p><strong>Good: Use window functions or JOIN</strong> — lines 10-18. Trace the <code>ON</code> predicates and join type: they decide which rows survive and whether unmatched keys appear as <code>NULL</code> (outer joins).</p>
    </div>
  </div>
</aside>
</div>

Remember: "Performance optimization is an iterative process - measure, analyze, improve!"

## Best Practices and Guidelines

### 1. Query Writing

- Write self-documenting queries with clear aliases
- Use CTEs for better readability and maintenance
- Leverage appropriate indexes for performance
- Consider query plan and execution cost

### 2. Database Design

- Implement proper constraints and relationships
- Use appropriate data types
- Design with scalability in mind
- Regular maintenance and optimization

### 3. Development Process

- Version control your database changes
- Implement proper testing procedures
- Monitor query performance
- Regular code reviews and optimization

## Additional Resources

1. **Documentation**
   - [PostgreSQL Documentation](https://www.postgresql.org/docs/)
   - [SQL Performance Tuning](https://use-the-index-luke.com/)
   - [Modern SQL Guide](https://modern-sql.com/)

2. **Tools**
   - [pgAdmin](https://www.pgadmin.org/) for database management
   - [DBeaver](https://dbeaver.io/) for query development
   - [pg_stat_statements](https://www.postgresql.org/docs/current/pgstatstatements.html) for query analysis

Remember: "Complex queries should be like well-written essays - clear, structured, and purposeful!"

## Next steps

- [SQL project](project.md) — consolidate skills in one scenario
- [Exploratory Data Analysis (Module 2.3)](../2.3-eda/README.md) — after you extract data, explore it in Python
- [Module README](README.md) — resources and assignment
