# Mastering SQL Joins: Connecting Your Data Universe

**After this lesson:** You can choose the right join type (**INNER**, **LEFT**, **RIGHT**, **FULL**) for a question, write multi-table queries with clear aliases, and avoid accidental Cartesian products.

## Helpful video

Quick tour of join types in SQL (inner, left, right, full).

<iframe width="560" height="315" src="https://www.youtube.com/embed/9yeOJ0ZMUYw" title="SQL Joins Explained" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Overview

**Prerequisites:** [Basic SQL Operations](basic-operations.md) and [Aggregations](aggregations.md). You should recognize foreign keys from [Introduction to Databases](intro-databases.md).

> **Time needed:** About 60–90 minutes with practice queries.

## Introduction to SQL Joins

SQL joins combine rows from two or more tables based on related columns. They are essential for:

- Retrieving related data across tables
- Building comprehensive reports
- Analyzing relationships in data
- Creating meaningful insights

## Types of SQL Joins

### 1. INNER JOIN

Returns only matching rows from both tables.

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
-- Basic INNER JOIN
SELECT 
    o.order_id,
    c.customer_name,
    o.order_date,
    o.total_amount
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id;

-- Multiple conditions
SELECT 
    o.order_id,
    c.customer_name
FROM orders o
INNER JOIN customers c 
    ON o.customer_id = c.customer_id
    AND o.store_id = c.preferred_store_id;
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-8" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Basic INNER JOIN</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–8: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="9-17" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Multiple conditions</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 9–17: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

### 2. LEFT JOIN (LEFT OUTER JOIN)

Returns all rows from the left table and matching rows from the right table.

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
-- Basic LEFT JOIN
SELECT 
    c.customer_name,
    COUNT(o.order_id) as order_count,
    COALESCE(SUM(o.total_amount), 0) as total_spent
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_name;

-- Finding missing relationships
SELECT 
    c.customer_name,
    'No orders' as status
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-8" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Basic LEFT JOIN</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–8: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="9-16" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Finding missing relationships</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 9–16: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

### 3. RIGHT JOIN (RIGHT OUTER JOIN)

Returns all rows from the right table and matching rows from the left table.

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
-- Basic RIGHT JOIN
SELECT 
    p.product_name,
    COALESCE(SUM(oi.quantity), 0) as total_ordered
FROM order_items oi
RIGHT JOIN products p ON oi.product_id = p.product_id
GROUP BY p.product_name;

-- Finding unused products
SELECT 
    p.product_name,
    'Never ordered' as status
FROM order_items oi
RIGHT JOIN products p ON oi.product_id = p.product_id
WHERE oi.order_id IS NULL;
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-7" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Basic RIGHT JOIN</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–7: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="8-15" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Finding unused products</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 8–15: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

### 4. FULL JOIN (FULL OUTER JOIN)

Returns all rows when there's a match in either left or right table.

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
-- Basic FULL JOIN
SELECT 
    c.customer_name,
    p.product_name,
    COUNT(o.order_id) as times_ordered
FROM customers c
FULL JOIN orders o ON c.customer_id = o.customer_id
FULL JOIN order_items oi ON o.order_id = oi.order_id
FULL JOIN products p ON oi.product_id = p.product_id
GROUP BY c.customer_name, p.product_name;

-- Finding all missing relationships
SELECT 
    COALESCE(c.customer_name, 'No Customer') as customer,
    COALESCE(p.product_name, 'No Product') as product,
    'Missing Relationship' as status
FROM customers c
FULL JOIN orders o ON c.customer_id = o.customer_id
FULL JOIN order_items oi ON o.order_id = oi.order_id
FULL JOIN products p ON oi.product_id = p.product_id
WHERE o.order_id IS NULL;
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-10" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Basic FULL JOIN</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–10: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="11-21" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Finding all missing relationships</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 11–21: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

### 5. CROSS JOIN

Returns Cartesian product of both tables.

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
-- Basic CROSS JOIN
SELECT 
    p.product_name,
    c.category_name
FROM products p
CROSS JOIN categories c;

-- Generate date-product combinations
SELECT 
    d.date,
    p.product_name
FROM generate_series(
    CURRENT_DATE,
    CURRENT_DATE + INTERVAL '7 days',
    INTERVAL '1 day'
) as d(date)
CROSS JOIN products p;
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-8" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Basic CROSS JOIN</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–8: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="9-17" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">SELECT</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 9–17: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

## Common Join Patterns

### 1. Multi-Table Joins

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
-- Order details with customer and product info
SELECT 
    o.order_id,
    c.customer_name,
    p.product_name,
    oi.quantity,
    oi.quantity * p.price as line_total
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id;
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-11" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Order details with customer and product info</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–11: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

### 2. Self Joins

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
-- Employee hierarchy
SELECT 
    e.employee_name as employee,
    m.employee_name as manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.employee_id;

-- Product recommendations
SELECT 
    p1.product_name,
    p2.product_name as recommended_product,
    COUNT(*) as times_bought_together
FROM order_items oi1
JOIN order_items oi2 
    ON oi1.order_id = oi2.order_id
    AND oi1.product_id < oi2.product_id
JOIN products p1 ON oi1.product_id = p1.product_id
JOIN products p2 ON oi2.product_id = p2.product_id
GROUP BY p1.product_name, p2.product_name
HAVING COUNT(*) > 5
ORDER BY times_bought_together DESC;
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-10" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Employee hierarchy</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–10: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="11-21" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">P2.product_name as recommended_product,</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 11–21: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

### 3. Conditional Joins

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
-- Join based on date ranges
SELECT 
    e.event_name,
    p.promotion_name
FROM events e
LEFT JOIN promotions p 
    ON e.event_date BETWEEN p.start_date AND p.end_date;

-- Join with multiple conditions
SELECT 
    o.order_id,
    d.driver_name
FROM orders o
LEFT JOIN drivers d 
    ON d.zone_id = o.delivery_zone_id
    AND d.is_active = true
    AND d.current_orders < d.max_orders;
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-8" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Join based on date ranges</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–8: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="9-17" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Join with multiple conditions</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 9–17: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

## Join Best Practices

### 1. Performance Optimization

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
-- Use proper indexes
CREATE INDEX idx_orders_customer 
ON orders(customer_id);

CREATE INDEX idx_order_items_composite 
ON order_items(order_id, product_id);

-- Join order matters
SELECT /*+ LEADING(small_table medium_table large_table) */
    *
FROM small_table
JOIN medium_table ON small_table.id = medium_table.id
JOIN large_table ON medium_table.id = large_table.id;
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-13" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Use proper indexes</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–13: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

### 2. Common Mistakes to Avoid

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
-- Avoid Cartesian products
-- Bad:
SELECT * FROM orders, customers;

-- Good:
SELECT * FROM orders
JOIN customers ON orders.customer_id = customers.customer_id;

-- Handle NULL values
SELECT 
    c.customer_name,
    COALESCE(SUM(o.total_amount), 0) as total_spent
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_name;
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-7" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Avoid Cartesian products</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–7: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="8-15" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Handle NULL values</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 8–15: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

### 3. Maintainability Tips

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
-- Use meaningful aliases
SELECT 
    cust.name,
    ord.order_date,
    prod.name as product_name
FROM customers cust
JOIN orders ord ON cust.customer_id = ord.customer_id
JOIN products prod ON ord.product_id = prod.product_id;

-- Break down complex joins
WITH customer_orders AS (
    SELECT 
        customer_id,
        COUNT(*) as order_count
    FROM orders
    GROUP BY customer_id
),
customer_spending AS (
    SELECT 
        customer_id,
        SUM(total_amount) as total_spent
    FROM orders
    GROUP BY customer_id
)
SELECT 
    c.customer_name,
    co.order_count,
    cs.total_spent
FROM customers c
LEFT JOIN customer_orders co ON c.customer_id = co.customer_id
LEFT JOIN customer_spending cs ON c.customer_id = cs.customer_id;
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-10" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Use meaningful aliases</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–10: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="11-20" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">WITH customer_orders AS (</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 11–20: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="21-31" data-tint="3">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">SUM(total_amount) as total_spent</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 21–31: follow this band in the snippet.</p>
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
      <p>Lines 1–14: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="15-28" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">ROUND(AVG(products_viewed)::numeric, 2) as av…</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 15–28: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

### 2. Supply Chain Analysis

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
WITH supplier_performance AS (
    SELECT 
        s.supplier_id,
        s.supplier_name,
        COUNT(DISTINCT o.order_id) as orders_fulfilled,
        AVG(EXTRACT(EPOCH FROM (d.delivery_date - o.order_date))/86400) as avg_delivery_days,
        COUNT(DISTINCT CASE 
            WHEN d.delivery_date > o.expected_delivery 
            THEN o.order_id 
        END) as late_deliveries,
        SUM(o.total_amount) as total_purchase_value
    FROM suppliers s
    LEFT JOIN purchase_orders o ON s.supplier_id = o.supplier_id
    LEFT JOIN deliveries d ON o.order_id = d.order_id
    GROUP BY s.supplier_id, s.supplier_name
)
SELECT 
    supplier_name,
    orders_fulfilled,
    ROUND(avg_delivery_days::numeric, 1) as avg_delivery_days,
    ROUND(
        100.0 * late_deliveries / NULLIF(orders_fulfilled, 0),
        2
    ) as late_delivery_rate,
    ROUND(total_purchase_value::numeric, 2) as total_purchase_value,
    CASE 
        WHEN late_deliveries = 0 THEN 'Excellent'
        WHEN late_deliveries::float / orders_fulfilled <= 0.05 THEN 'Good'
        WHEN late_deliveries::float / orders_fulfilled <= 0.10 THEN 'Fair'
        ELSE 'Poor'
    END as performance_rating
FROM supplier_performance
ORDER BY orders_fulfilled DESC;
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-11" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">WITH supplier_performance AS (</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–11: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="12-22" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">FROM suppliers s</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 12–22: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="23-33" data-tint="3">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">2</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 23–33: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

### 3. Customer Service Integration

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
WITH ticket_metrics AS (
    SELECT 
        t.ticket_id,
        t.customer_id,
        t.created_at,
        t.resolved_at,
        t.status,
        t.priority,
        o.order_id,
        o.order_date,
        p.product_id,
        p.product_name,
        EXTRACT(EPOCH FROM (t.resolved_at - t.created_at))/3600 as resolution_time_hours
    FROM support_tickets t
    LEFT JOIN orders o ON t.order_id = o.order_id
    LEFT JOIN order_items oi ON o.order_id = oi.order_id
    LEFT JOIN products p ON oi.product_id = p.product_id
)
SELECT 
    priority,
    COUNT(*) as ticket_count,
    ROUND(AVG(resolution_time_hours)::numeric, 2) as avg_resolution_hours,
    ROUND(
        100.0 * COUNT(CASE WHEN status = 'resolved' THEN 1 END) / COUNT(*),
        2
    ) as resolution_rate,
    STRING_AGG(DISTINCT product_name, ', ' ORDER BY product_name) 
        FILTER (WHERE product_name IS NOT NULL) as affected_products
FROM ticket_metrics
GROUP BY priority
ORDER BY 
    CASE priority
        WHEN 'high' THEN 1
        WHEN 'medium' THEN 2
        WHEN 'low' THEN 3
    END;
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-12" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">WITH ticket_metrics AS (</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–12: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="13-24" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">EXTRACT(EPOCH FROM (t.resolved_at - t.created…</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 13–24: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="25-36" data-tint="3">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">2</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 25–36: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

## Performance Optimization Examples

### 1. Hash Join vs. Merge Join

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
-- Force hash join for large tables with no useful indexes
SELECT /*+ HASHJOIN(o c) */
    c.customer_name,
    COUNT(*) as order_count
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.customer_name;

-- Force merge join for indexed columns
SELECT /*+ MERGEJOIN(o c) */
    c.customer_name,
    COUNT(*) as order_count
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.customer_name;
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-7" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Force hash join for large tables with no usef…</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–7: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="8-15" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Force merge join for indexed columns</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 8–15: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

### 2. Partitioned Joins

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
-- Join with partitioned tables
CREATE TABLE orders (
    order_id INT,
    customer_id INT,
    order_date DATE,
    total_amount DECIMAL(10,2)
) PARTITION BY RANGE (order_date);

CREATE TABLE order_items (
    order_id INT,
    product_id INT,
    quantity INT,
    price DECIMAL(10,2)
) PARTITION BY RANGE (order_id);

-- Create corresponding partitions
CREATE TABLE orders_2023_q1 PARTITION OF orders
    FOR VALUES FROM ('2023-01-01') TO ('2023-04-01');
CREATE TABLE order_items_2023_q1 PARTITION OF order_items
    FOR VALUES FROM (1000) TO (2000);

-- Query specific partitions
SELECT 
    o.order_id,
    SUM(oi.quantity * oi.price) as total_value
FROM orders_2023_q1 o
JOIN order_items_2023_q1 oi ON o.order_id = oi.order_id
GROUP BY o.order_id;
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-14" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Join with partitioned tables</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–14: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="15-28" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Create corresponding partitions</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 15–28: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

### 3. Materialized Views for Complex Joins

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
-- Create materialized view for frequently joined data
CREATE MATERIALIZED VIEW order_summary AS
SELECT 
    o.order_id,
    c.customer_name,
    o.order_date,
    COUNT(oi.product_id) as total_items,
    SUM(oi.quantity * oi.price) as total_value,
    STRING_AGG(p.product_name, ', ') as products
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
GROUP BY o.order_id, c.customer_name, o.order_date;

-- Create indexes on materialized view
CREATE INDEX idx_order_summary_date ON order_summary(order_date);
CREATE INDEX idx_order_summary_customer ON order_summary(customer_name);

-- Refresh strategy
CREATE OR REPLACE FUNCTION refresh_order_summary()
RETURNS trigger AS $$
BEGIN
    REFRESH MATERIALIZED VIEW CONCURRENTLY order_summary;
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER refresh_order_summary_trigger
AFTER INSERT OR UPDATE OR DELETE ON orders
FOR EACH STATEMENT
EXECUTE FUNCTION refresh_order_summary();
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-10" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Create materialized view for frequently joine…</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–10: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="11-21" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">JOIN customers c ON o.customer_id = c.custome…</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 11–21: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="22-32" data-tint="3">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">RETURNS trigger AS $$</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 22–32: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

## Interactive Examples with Sample Data

### 1. Generate Sample Data

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
-- Create sample customers
INSERT INTO customers (customer_name, email, join_date)
SELECT 
    'Customer ' || i,
    'customer' || i || '@example.com',
    CURRENT_DATE - (random() * 365)::integer
FROM generate_series(1, 1000) i;

-- Create sample orders
INSERT INTO orders (customer_id, order_date, total_amount)
SELECT 
    (random() * 1000)::integer,
    CURRENT_DATE - (random() * 90)::integer,
    (random() * 1000)::numeric(10,2)
FROM generate_series(1, 5000);

-- Create sample products
INSERT INTO products (product_name, category_id, price)
SELECT 
    'Product ' || i,
    (random() * 10 + 1)::integer,
    (random() * 100 + 10)::numeric(10,2)
FROM generate_series(1, 100);
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-11" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Create sample customers</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–11: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="12-23" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">(random() * 1000)::integer,</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 12–23: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

### 2. Analysis Queries

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight sql %}
-- Customer purchase patterns
WITH customer_patterns AS (
    SELECT 
        c.customer_id,
        c.customer_name,
        COUNT(DISTINCT o.order_id) as order_count,
        COUNT(DISTINCT DATE_TRUNC('month', o.order_date)) as active_months,
        SUM(o.total_amount) as total_spent,
        AVG(o.total_amount) as avg_order_value
    FROM customers c
    LEFT JOIN orders o ON c.customer_id = o.customer_id
    GROUP BY c.customer_id, c.customer_name
)
SELECT 
    CASE 
        WHEN order_count = 0 THEN 'Never Ordered'
        WHEN order_count = 1 THEN 'One-Time'
        WHEN order_count > 1 AND active_months = 1 THEN 'Same Month Multiple'
        WHEN order_count > 1 THEN 'Returning'
    END as customer_type,
    COUNT(*) as customer_count,
    ROUND(AVG(order_count)::numeric, 2) as avg_orders,
    ROUND(AVG(total_spent)::numeric, 2) as avg_total_spent,
    ROUND(AVG(avg_order_value)::numeric, 2) as avg_order_value
FROM customer_patterns
GROUP BY 
    CASE 
        WHEN order_count = 0 THEN 'Never Ordered'
        WHEN order_count = 1 THEN 'One-Time'
        WHEN order_count > 1 AND active_months = 1 THEN 'Same Month Multiple'
        WHEN order_count > 1 THEN 'Returning'
    END
ORDER BY avg_total_spent DESC;
{% endhighlight %}
</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-11" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Customer purchase patterns</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 1–11: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="12-22" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">GROUP BY c.customer_id, c.customer_name</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 12–22: follow this band in the snippet.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="23-33" data-tint="3">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">ROUND(AVG(total_spent)::numeric, 2) as avg_to…</span>
    </div>
    <div class="code-callout__body">
      <p>Lines 23–33: follow this band in the snippet.</p>
    </div>
  </div>
</aside>
</div>

Remember: "Efficient joins are the key to unlocking insights from your data!"

## Next steps

- [Advanced SQL Concepts](advanced-concepts.md) — subqueries, CTEs, and window functions
- [SQL project](project.md) — apply joins in a structured brief
- [Data Wrangling (Module 2.2)](../2.2-data-wrangling/README.md) — cleaning and shaping data before or after SQL extracts
