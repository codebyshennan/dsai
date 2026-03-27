# 5.2 Supervised Learning Part 1

**After this submodule:** you can use the lessons linked below and complete the exercises that match **5.2 Supervised Learning Part 1** in your course schedule.

Welcome to the first part of supervised learning! Here we'll explore fundamental algorithms that form the backbone of machine learning. Think of these algorithms as different tools in your ML toolkit - each with its own strengths and ideal use cases.

## Helpful video

Crash Course AI: supervised learning for classical algorithms.

<iframe width="560" height="315" src="https://www.youtube.com/embed/4qVRBYAdLAo" title="Supervised Learning: Crash Course AI" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Learning Objectives

By the end of this section, you will be able to:

1. Understand and implement Naive Bayes classifiers for text classification
2. Master k-Nearest Neighbors (kNN) for both classification and regression tasks
3. Apply Support Vector Machines (SVM) for complex decision boundaries
4. Build and interpret Decision Trees for transparent decision-making
5. Choose the optimal algorithm for different problem types

## Algorithm Overview

### 1. [Naive Bayes](broken-reference)

Probabilistic classifier based on Bayes' Theorem:

$$P(y|X) = \frac{P(X|y)P(y)}{P(X)}$$

Perfect for:

* Text classification (spam detection, sentiment analysis)
* High-dimensional data
* Real-time prediction needs
* When independence assumption holds

### 2. [k-Nearest Neighbors](broken-reference)

Instance-based learning using distance metrics:

$$\text{distance}(p,q) = \sqrt{\sum_{i=1}^n (p_i - q_i)^2}$$

Ideal for:

* Recommendation systems
* Pattern recognition
* Anomaly detection
* When data is well-clustered

### 3. [Support Vector Machines](broken-reference)

Finds optimal hyperplane with maximum margin:

$$\min_{w,b} \frac{1}{2}||w||^2 \text{ subject to } y_i(w^Tx_i + b) \geq 1$$

Best for:

* Complex classification tasks
* Non-linear decision boundaries
* High-dimensional spaces
* When clear margin of separation exists

### 4. [Decision Trees](broken-reference)

Hierarchical decisions using information theory:

$$\text{Information Gain} = H(\text{parent}) - \sum_{j=1}^m \frac{N_j}{N} H(\text{child}_j)$$

Excellent for:

* Interpretable models
* Mixed data types
* Feature importance analysis
* When non-linear relationships exist

## Algorithm Selection Guide

### Classification Tasks

#### Heuristic mapping from data traits to a first algorithm

**Purpose:** Give learners a memorable decision stub—not a rule—linking text data, interpretability, dimensionality, and geometry to Naive Bayes, trees, SVM, or kNN.

**Walkthrough:** Replace `data_characteristics` with your real checks (imbalance, $n$, latency); always validate with CV and baselines.

```python
def select_classifier(data_characteristics):
    if data_characteristics.text_data:
        return "Naive Bayes"
    elif data_characteristics.need_interpretability:
        return "Decision Tree"
    elif data_characteristics.high_dimensional:
        return "SVM"
    elif data_characteristics.well_clustered:
        return "kNN"
    else:
        return "Try multiple and compare"
```

### Performance Comparison

| Algorithm      | Training Speed | Prediction Speed | Interpretability | Memory Usage |
| -------------- | -------------- | ---------------- | ---------------- | ------------ |
| Naive Bayes    |          |            |              |            |
| kNN            |          |                |            |        |
| SVM            |              |              |                |          |
| Decision Trees |            |            |            |            |

## Prerequisites

Before diving in, ensure you're comfortable with:

### 1. Mathematics

* Basic probability theory
* Linear algebra fundamentals
* Information theory concepts
* Distance metrics

### 2. Programming

#### Core imports for this module

**Purpose:** Align vocabulary with the rest of the course: NumPy/Pandas for data, scikit-learn for estimators, Matplotlib for plots.

```python
# Essential Python libraries
import numpy as np          # Numerical operations
import pandas as pd         # Data manipulation
import sklearn             # Machine learning tools
import matplotlib.pyplot as plt  # Visualization
```

### 3. Concepts

* Feature engineering
* Model evaluation metrics
* Cross-validation
* Bias-variance tradeoff

## Real-World Applications

### 1. Email Classification

#### Text pipeline sketch: TF–IDF + multinomial Naive Bayes

**Purpose:** Show the usual spam/sentiment stack—sparse word counts or TF–IDF feeding a fast generative classifier.

**Walkthrough:** `TfidfVectorizer` must `fit_transform` on training text only; `MultinomialNB` is a common default for word counts.

```python
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer

# Example: Spam Detection
vectorizer = TfidfVectorizer()
classifier = MultinomialNB()
```

### 2. Medical Diagnosis

#### Nonlinear SVM with RBF kernel (illustrative)

**Purpose:** Recall that margin-based classifiers with kernels handle nonlinear boundaries when features are mapped implicitly.

**Walkthrough:** `C` trades margin width vs violations; kernel choice and calibration matter—this is only a starting point.

```python
from sklearn.svm import SVC

# Example: Disease Classification
svm_classifier = SVC(kernel='rbf', C=1.0)
```

### 3. Credit Risk Assessment

#### Shallow tree for interpretable credit decisions

**Purpose:** Emphasize transparency and rule-like splits for regulated or explainable use cases.

**Walkthrough:** `max_depth` limits complexity; pair with cost-sensitive metrics if classes are imbalanced.

```python
from sklearn.tree import DecisionTreeClassifier

# Example: Loan Approval
dt_classifier = DecisionTreeClassifier(max_depth=5)
```

### 4. Recommendation Systems

#### kNN as a lazy learner for similarity-style classification

**Purpose:** Connect user–item or content similarity ideas to a distance-based vote among neighbors.

**Walkthrough:** Scale features first; `n_neighbors` and distance metric heavily affect results.

```python
from sklearn.neighbors import KNeighborsClassifier

# Example: Product Recommendations
knn_classifier = KNeighborsClassifier(n_neighbors=5)
```

## Learning Path

1. Start with [Naive Bayes](broken-reference)
   * Understand probability basics
   * Learn text classification
   * Master feature independence
2. Move to [k-Nearest Neighbors](broken-reference)
   * Grasp distance metrics
   * Understand k selection
   * Handle the curse of dimensionality
3. Progress to [Support Vector Machines](broken-reference)
   * Master linear classification
   * Explore kernel methods
   * Optimize hyperparameters
4. Conclude with [Decision Trees](broken-reference)
   * Learn tree construction
   * Understand splitting criteria
   * Practice pruning techniques

## Tools and Environment

### Required Libraries

#### Install scientific Python stack (example)

**Purpose:** One-line environment setup aligned with the lessons; use `uv`/`conda` in your own workflow if preferred.

```bash
# Install required packages
pip install numpy pandas scikit-learn matplotlib seaborn
```

### Recommended IDE Setup

#### Notebook starter imports and reproducibility

**Purpose:** Standardize evaluation imports and fixed randomness so notebooks reruns match teaching outputs.

**Walkthrough:** `train_test_split` + `accuracy_score` / `classification_report` cover common classification reporting; extend with your metric of record.

```python
# Standard imports for all notebooks
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# Set random seed for reproducibility
np.random.seed(42)
```

## Best Practices

1. Data Preparation
   * Handle missing values
   * Scale features appropriately
   * Split data properly
2. Model Selection
   * Consider problem characteristics
   * Start simple, increase complexity
   * Use cross-validation
3. Evaluation
   * Choose appropriate metrics
   * Test on holdout set
   * Consider computational costs

## Common Pitfalls

1. Naive Bayes
   * Zero frequency problem
   * Feature independence assumption
   * Numeric precision issues
2. kNN
   * Curse of dimensionality
   * Scale sensitivity
   * Memory requirements
3. SVM
   * Kernel selection
   * Parameter tuning
   * Scaling requirements
4. Decision Trees
   * Overfitting
   * Feature interaction handling
   * Categorical variable splits

## Assignment

Ready to apply your supervised learning knowledge? Head over to the [Supervised Learning Assignment](../_assignments/5.2-assignment.md) to test your understanding of these fundamental algorithms!

## Ready to Begin?

Start your journey with [Naive Bayes](broken-reference) to build a strong foundation in probabilistic classification. Each algorithm builds upon previous concepts, so following the suggested order will maximize your learning experience.

Remember: The best way to learn is by doing! Each section includes hands-on examples and exercises to reinforce your understanding. Let's dive in!
