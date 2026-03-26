# Understanding Pandas Series

## Overview

**Primary outcome:** You can create a **Series**, interpret its index and **dtype**, and perform basic math and summary stats—thinking of it as one labeled column.

**Prerequisites:** [Introduction to Python](../1.2-intro-python/README.md) and [Introduction to NumPy](../1.4-data-foundation-linear-algebra/intro-numpy.md) (arrays) at a basic level.

## What is a Series?

A Pandas Series is like a column in a spreadsheet or a single list of data with labels. Think of it as a smart, one-dimensional array that knows the name of each item! It's perfect for:

- Time series data (stock prices over time)
- Storing categorical data (product categories)
- Tracking measurements (temperatures, distances)
- Working with labeled data (student grades)

Real-world applications:

- Financial data analysis
- Daily temperature readings
- Survey responses
- Sales performance tracking

---

### Creating Your First Series

Let's explore different ways to create a Series:

```python
import pandas as pd
import numpy as np

# From a list
numbers = pd.Series([5, 6, -3, 2])
print("Simple Series:")
print(numbers)
print("\nType:", numbers.dtype)
print("Size:", numbers.size)
print("Shape:", numbers.shape)

# From a NumPy array
array_data = np.array([1.1, 2.2, 3.3, 4.4])
float_series = pd.Series(array_data)
print("\nFrom NumPy array:")
print(float_series)

# From a scalar value
constant = pd.Series(5, index=['a', 'b', 'c'])
print("\nConstant value Series:")
print(constant)

# Real-world example - Daily temperatures
temperatures = pd.Series([20.5, 22.1, 23.4, 21.8, 20.9],
                        index=['Mon', 'Tue', 'Wed', 'Thu', 'Fri'])
print("\nWeekly Temperatures:")
print(temperatures)
print("\nAverage temperature:", temperatures.mean())
print("Highest temperature:", temperatures.max())
```

Notice how Pandas automatically creates numbered labels (0, 1, 2, 3) for each value!

---

### Custom Labels

You can create your own labels (called an index) for each value:

```python
# Create a Series with custom labels
grades = pd.Series([90, 85, 95, 78], 
                  index=['Alice', 'Bob', 'Charlie', 'David'])
print(grades)
```

Output:

```
Alice      90
Bob        85
Charlie    95
David      78
dtype: int64
```

Now you can access values using these friendly names!

---

### Working with Series

Here are some common ways to work with your Series:

```python
# Access a single value using its label
print(f"Charlie's grade: {grades['Charlie']}")  # Output: 95

# Get multiple values
print(grades[['Alice', 'Bob']])

# Filter values
passing_grades = grades[grades >= 90]
print("\nStudents with A grades:")
print(passing_grades)
```

## Series from Dictionary

---

### Creating from Dictionary

A Series can be created from a dictionary, where:

- Dictionary keys become the index (labels)
- Dictionary values become the Series values

```python
# Create a Series from a dictionary
population = pd.Series({
    'New York': 8.4,
    'London': 9.0,
    'Tokyo': 37.4,
    'Paris': 2.2
})
print(population)
```

Output:

```
New York     8.4
London       9.0
Tokyo       37.4
Paris        2.2
dtype: float64
```

---

### Converting Back to Dictionary

You can convert your Series back to a dictionary:

```python
# Convert Series to dictionary
pop_dict = population.to_dict()
print(pop_dict)
```

Output:

```python
{'New York': 8.4, 'London': 9.0, 'Tokyo': 37.4, 'Paris': 2.2}
```

## Working with Missing Data

---

### Understanding Missing Data

In the real world, data is often incomplete. Pandas uses `NaN` (Not a Number) to represent missing values:

```python
# Series with missing data
scores = pd.Series({'Math': 90, 'English': 85, 'Science': None, 'History': 88})
print(scores)
```

Output:

```
Math       90.0
English    85.0
Science     NaN
History    88.0
dtype: float64
```

---

### Handling Missing Data

Pandas provides tools to work with missing data:

```python
# Check for missing values
print("Missing values?")
print(scores.isna())

# Drop missing values
print("\nScores without missing values:")
print(scores.dropna())

# Fill missing values
print("\nScores with filled values (0):")
print(scores.fillna(0))
```

## Series Operations

---

### Basic Math Operations

Series support mathematical operations, just like regular numbers:

```python
# Original grades
grades = pd.Series({
    'Alice': 85,
    'Bob': 90,
    'Charlie': 78
})

# Add 5 points to everyone's grade
curved_grades = grades + 5
print("Grades after curve:")
print(curved_grades)
```

---

### Statistical Operations

Pandas provides many built-in statistical methods:

```python
print(f"Average grade: {grades.mean()}")
print(f"Highest grade: {grades.max()}")
print(f"Lowest grade: {grades.min()}")
print(f"Grade summary:\n{grades.describe()}")
```

## Best Practices and Tips

1. **Always Label Your Data**: Using meaningful index labels makes your data more readable and easier to work with.
2. **Check Data Types**: Use `dtype` to confirm your Series has the right data type.
3. **Handle Missing Values**: Always check for and handle missing values appropriately.
4. **Use Method Chaining**: You can combine operations like `grades.dropna().mean()`.

Remember: A Series is just the beginning. Once you're comfortable with Series, you'll be ready to tackle DataFrames, which are like multiple Series working together.

## Common pitfalls

- Forgetting that **Series** alignment is by **index** — operations pair labels, not just positions.
- Mixing up **loc** (label-based) and **iloc** (position-based) when you slice (covered in more detail in later lessons).
- Ignoring **NaN** values before calling **.mean()** or similar — check **.isna()** first when data is messy.

## Next steps

Continue to [Understanding DataFrames](./dataframe.md) to combine multiple columns and work with full tables.
