# Implementing KNN: A Step-by-Step Guide

**After this lesson:** you can explain the core ideas in “Implementing KNN: A Step-by-Step Guide” and reproduce the examples here in your own notebook or environment.

Welcome to the practical side of KNN! In this section, we'll learn how to implement KNN both from scratch (to understand how it works) and using scikit-learn (for real-world applications).

![Effect of Different k Values](assets/knn_different_k.png)
*Figure: How different values of k affect the decision boundary in KNN*

## Helpful video

Crash Course AI: supervised learning for classical algorithms.

<iframe width="560" height="315" src="https://www.youtube.com/embed/4qVRBYAdLAo" title="Supervised Learning: Crash Course AI" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Understanding k in KNN

The parameter k in KNN (k-Nearest Neighbors) is a crucial hyperparameter that determines how many neighboring data points to consider when making a prediction. Here's what you need to know about k:

- **What is k?**: k is the number of nearest neighbors that the algorithm considers when making a prediction
- **How it works**:
  - For a new data point, KNN finds the k closest points in the training data
  - The algorithm then takes a "majority vote" among these k neighbors
  - The most common class among these k neighbors becomes the prediction
- **Impact of k**:
  - Small k (e.g., k=1): More sensitive to noise, captures local patterns
  - Large k: More stable but might include irrelevant points
  - Rule of thumb: Start with k = √n (where n is number of training samples)

Think of k like asking for advice:

- k=1 is like asking only your closest friend
- k=5 is like asking your 5 closest friends
- k=20 is like asking a larger group of friends

## Why Implementation Matters

Understanding how to implement KNN is crucial because:

- It helps you understand how the algorithm works under the hood
- You can customize it for your specific needs
- You'll be better at debugging when things go wrong
- You can optimize it for your particular use case

## Implementation from Scratch

Let's build a simple KNN classifier step by step. Think of it like building a recommendation system that asks your closest friends for advice.

### Step 1: Create the Basic Structure

#### SimpleKNN class skeleton

**Purpose:** Defines a minimal `SimpleKNN` that stores `k` and memorizes training examples in `fit`—the lazy-learning pattern (no iterative training).

**Walkthrough:**
- `__init__` keeps `k`; `fit` only assigns `X_train` and `y_train`.

```python
import numpy as np
from collections import Counter

class SimpleKNN:
    def __init__(self, k=3):
        """Initialize with k neighbors (default: 3)"""
        self.k = k
        
    def fit(self, X, y):
        """Store the training data - KNN doesn't actually train!"""
        self.X_train = X
        self.y_train = y
```

**What's happening here:**

- We create a class called <code>SimpleKNN</code>
- The <code>__init__</code> method sets up how many neighbors (k) we want to consider
- The <code>fit</code> method just stores our training data (unlike other algorithms, KNN doesn't need training!)

### Step 2: Add Prediction Logic

#### Predict with Euclidean distance and majority vote

**Purpose:** For each query row, computes distances to all training points, selects the `k` smallest, and returns the most common class label among those neighbors.

**Walkthrough:**
- Euclidean distance via `np.sqrt(np.sum((x - x_train)**2))`; `np.argsort` + slice for top-`k`; `Counter` for the mode.

```python
    def predict(self, X):
        """Make predictions for new data points"""
        return np.array([self._predict_single(x) for x in X])
    
    def _predict_single(self, x):
        """Predict class for a single point"""
        # Calculate distances to all training points
        distances = [np.sqrt(np.sum((x - x_train)**2)) 
                    for x_train in self.X_train]
        
        # Get k nearest neighbors
        k_indices = np.argsort(distances)[:self.k]
        k_nearest_labels = [self.y_train[i] for i in k_indices]
        
        # Return most common class
        most_common = Counter(k_nearest_labels).most_common(1)
        return most_common[0][0]
```

**Breaking it down:**

1. <code>predict</code> handles multiple points at once
2. <code>_predict_single</code> works on one point at a time:
   - Calculates distances to all training points
   - Finds the k closest points
   - Returns the most common class among them

### Step 3: Try it Out

#### Demo: synthetic movie genres with `SimpleKNN(k=3)`

**Purpose:** Builds toy training data with action vs romance feature scores, fits the scratch classifier, and predicts a label for a new mixed-genre point.

**Walkthrough:**
- `np.array` for `X_train` / `y_train`; `fit` then `predict([new_movie])`; `print` shows the predicted genre.

```python
# Example: Movie Genre Classification
# Features: [Action Score, Romance Score]
X_train = np.array([
    [8, 2],  # Action movie
    [7, 3],  # Action movie
    [2, 8],  # Romance movie
    [3, 7],  # Romance movie
    [1, 9],  # Romance movie
    [9, 1]   # Action movie
])
y_train = np.array(['Action', 'Action', 'Romance', 'Romance', 'Romance', 'Action'])

# Create and train model
knn = SimpleKNN(k=3)
knn.fit(X_train, y_train)

# Predict a new movie
new_movie = np.array([4, 6])  # Mix of action and romance
prediction = knn.predict([new_movie])
print(f"Predicted genre: {prediction[0]}")
```

## Using Scikit-learn

While implementing from scratch is educational, scikit-learn provides a robust, optimized version of KNN. Let's see how to use it for a real-world problem.

### Example: Iris Flower Classification

#### Iris pipeline: split, scale, `KNeighborsClassifier`, metrics

**Purpose:** Loads the Iris dataset, holds out a test set, applies `StandardScaler` so all features contribute equally to distances, fits a 5-neighbor KNN, and prints accuracy plus a classification report.

**Walkthrough:**
- `load_iris`, `train_test_split`, `StandardScaler.fit_transform` / `transform`, `KNeighborsClassifier` with `metric='euclidean'`, `accuracy_score`, `classification_report` with `target_names`.

```python
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.datasets import load_iris

def classify_iris_flowers():
    """Complete example of classifying iris flowers"""
    # Load the famous Iris dataset
    iris = load_iris()
    X, y = iris.data, iris.target
    
    # Split into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Scale the features (important for KNN!)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Create and train the model
    knn = KNeighborsClassifier(
        n_neighbors=5,          # Number of neighbors to consider
        weights='uniform',      # All neighbors have equal weight
        metric='euclidean'      # Distance metric to use
    )
    knn.fit(X_train_scaled, y_train)
    
    # Make predictions
    y_pred = knn.predict(X_test_scaled)
    
    # Evaluate the model
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("\nDetailed Report:")
    print(classification_report(y_test, y_pred,
                              target_names=iris.target_names))
    
    return knn, scaler

# Run the example
model, scaler = classify_iris_flowers()
```

**Captured stdout** (from running the snippet above; may be auto-injected on build):

```
Accuracy: 1.0

Detailed Report:
              precision    recall  f1-score   support

      setosa       1.00      1.00      1.00        10
  versicolor       1.00      1.00      1.00         9
   virginica       1.00      1.00      1.00        11

    accuracy                           1.00        30
   macro avg       1.00      1.00      1.00        30
weighted avg       1.00      1.00      1.00        30
```

## Common Mistakes to Avoid

1. **Forgetting to Scale Features**

   #### Wrong vs right: scale features before `KNeighborsClassifier`

   **Purpose:** Contrasts fitting KNN on raw `X_train` (distances dominated by large-scale columns) with fitting after `StandardScaler` so every feature is comparable.

   **Walkthrough:**
   - `StandardScaler().fit_transform(X_train)` then `knn.fit` on the scaled matrix.

   ```python
   #  Wrong way
   knn = KNeighborsClassifier()
   knn.fit(X_train, y_train)  # Features not scaled
   
   #  Right way
   scaler = StandardScaler()
   X_train_scaled = scaler.fit_transform(X_train)
   knn.fit(X_train_scaled, y_train)
   ```

**Captured stdout** (from running the snippet above; may be auto-injected on build):

```
KNeighborsClassifier()
```

2. **Choosing the Wrong k Value**

   #### Grid search `n_neighbors` instead of fixing `k=1`

   **Purpose:** Replaces a noise-sensitive `k=1` model with a `GridSearchCV` sweep over several odd `k` values using 5-fold CV on the training data.

   **Walkthrough:**
   - `param_grid = {'n_neighbors': [...]}`; `GridSearchCV(knn, param_grid, cv=5)` and `fit`.

   ```python
   #  Using k=1 (too sensitive to noise)
   knn = KNeighborsClassifier(n_neighbors=1)
   
   #  Try different values and use cross-validation
   from sklearn.model_selection import GridSearchCV
   param_grid = {'n_neighbors': [3, 5, 7, 9, 11]}
   grid_search = GridSearchCV(knn, param_grid, cv=5)
   grid_search.fit(X_train_scaled, y_train)
   ```

3. **Not Handling Categorical Features**

   #### Encode categories before distance-based fitting

   **Purpose:** Shows that string or categorical columns cannot be subtracted in distance formulas—`OneHotEncoder` (or similar) turns them into numeric columns KNN can use.

   **Walkthrough:**
   - `OneHotEncoder().fit_transform(X_with_categories)` then `knn.fit` on `X_encoded`.

   ```python
   #  Using categorical features directly
   knn.fit(X_with_categories, y)
   
   #  Encode categorical features first
   from sklearn.preprocessing import OneHotEncoder
   encoder = OneHotEncoder()
   X_encoded = encoder.fit_transform(X_with_categories)
   knn.fit(X_encoded, y)
   ```

## Best Practices

1. **Always Scale Your Features**

   #### Apply `StandardScaler` to the full feature matrix

   **Purpose:** Fits the scaler on `X` and returns `X_scaled` with zero mean and unit variance per feature—a default preprocessing step for KNN.

   **Walkthrough:**
   - `StandardScaler().fit_transform(X)`.

   ```python
   from sklearn.preprocessing import StandardScaler
   scaler = StandardScaler()
   X_scaled = scaler.fit_transform(X)
   ```

2. **Use Cross-Validation**

   #### Mean CV accuracy with `cross_val_score`

   **Purpose:** Estimates how well the current KNN configuration generalizes by averaging accuracy across five folds on `X_scaled` and `y`.

   **Walkthrough:**
   - `cross_val_score(knn, X_scaled, y, cv=5)` and `scores.mean()`.

   ```python
   from sklearn.model_selection import cross_val_score
   scores = cross_val_score(knn, X_scaled, y, cv=5)
   print(f"Average accuracy: {scores.mean():.3f}")
   ```

3. **Optimize Hyperparameters**

   #### Joint grid over `n_neighbors`, `weights`, and `metric`

   **Purpose:** Uses `GridSearchCV` to pick the combination of neighbor count, neighbor weighting, and distance metric that maximizes CV accuracy on the scaled data.

   **Walkthrough:**
   - `param_grid` with three keys; `grid_search.fit(X_scaled, y)`; `best_params_`.

   ```python
   from sklearn.model_selection import GridSearchCV
   
   param_grid = {
       'n_neighbors': [3, 5, 7, 9, 11],
       'weights': ['uniform', 'distance'],
       'metric': ['euclidean', 'manhattan']
   }
   
   grid_search = GridSearchCV(knn, param_grid, cv=5)
   grid_search.fit(X_scaled, y)
   print(f"Best parameters: {grid_search.best_params_}")
   ```

## Detailed Implementation Guide

### Understanding Common Mistakes in Depth

1. **Feature Scaling: Why It's Critical**
   - **The Problem**: KNN is distance-based, making it sensitive to feature scales
   - **Real-world Impact**:
     - Features with larger scales (e.g., income: 0-1000000) dominate distance calculations
     - Features with smaller scales (e.g., age: 0-100) become less influential
   - **Solution Details**:

     #### Fit scaler on train only; transform test with the same stats

     **Purpose:** Prevents information leakage by learning mean and scale from `X_train`, then applying that same transformation to `X_test`.

     **Walkthrough:**
     - `fit_transform(X_train)` vs `transform(X_test)`.

     ```python
     # 1. Create the scaler
     scaler = StandardScaler()
     
     # 2. Fit and transform training data
     X_train_scaled = scaler.fit_transform(X_train)
     
     # 3. Transform test data (using same scaling as training)
     X_test_scaled = scaler.transform(X_test)
     ```

   - **Why StandardScaler Works**:
     - Transforms features to have mean = 0 and standard deviation = 1
     - Ensures all features contribute equally to distance calculations
     - Makes the model more robust and interpretable

2. **K Value Selection: Finding the Sweet Spot**
   - **Impact of Different k Values**:
     - Too small (k=1):
       - Pros: Captures local patterns well
       - Cons: Highly sensitive to noise, prone to overfitting
     - Too large:
       - Pros: More stable predictions
       - Cons: May include irrelevant points from other classes
   - **Optimal Selection Strategy**:
     - Start with k = √n (where n is number of training samples)
     - Use cross-validation to evaluate different k values
     - Consider the balance between bias and variance
   - **Implementation with GridSearchCV**:

     #### `GridSearchCV` setup for KNN (parallel, accuracy scoring)

     **Purpose:** Declares a search space over `k`, weighting, and distance metric with 5-fold CV and all CPU cores—call `fit` on training data to get `best_params_`.

     **Walkthrough:**
     - `KNeighborsClassifier()` as estimator; `param_grid`; `cv=5`, `scoring='accuracy'`, `n_jobs=-1`.

     ```python
     from sklearn.model_selection import GridSearchCV
     
     # Define parameter grid
     param_grid = {
         'n_neighbors': [3, 5, 7, 9, 11],
         'weights': ['uniform', 'distance'],
         'metric': ['euclidean', 'manhattan']
     }
     
     # Create and run grid search
     grid_search = GridSearchCV(
         KNeighborsClassifier(),
         param_grid,
         cv=5,  # 5-fold cross-validation
         scoring='accuracy',
         n_jobs=-1  # Use all available CPU cores
     )
     ```

3. **Categorical Feature Handling: Beyond One-Hot Encoding**
   - **Why It Matters**:
     - KNN requires numerical features for distance calculations
     - Categorical variables need proper encoding to preserve their meaning
   - **Encoding Strategies**:
       - **One-Hot Encoding**: For nominal categories (no inherent order)

       #### One-hot encode nominal columns (`sparse=False`)

       **Purpose:** Expands each category into binary columns so distances treat distinct categories as separate directions, not ordered numbers.

       **Walkthrough:**
       - `OneHotEncoder(sparse=False)`; `fit_transform(X_categorical)`.

       ```python
       from sklearn.preprocessing import OneHotEncoder
       encoder = OneHotEncoder(sparse=False)
       X_encoded = encoder.fit_transform(X_categorical)
       ```

     - **Label Encoding**: For ordinal categories (has inherent order)

       #### Integer encode ordered categories

       **Purpose:** Maps ordered categories to consecutive integers when a single numeric feature is appropriate (unlike one-hot for nominal data).

       **Walkthrough:**
       - `LabelEncoder().fit_transform(X_ordinal)`.

       ```python
       from sklearn.preprocessing import LabelEncoder
       encoder = LabelEncoder()
       X_encoded = encoder.fit_transform(X_ordinal)
       ```

   - **Best Practices**:
     - Always use One-Hot Encoding for nominal categories
     - Consider feature interactions after encoding
     - Handle missing values before encoding

### Advanced Best Practices

1. **Cross-Validation: Beyond Basic Implementation**
   - **Purpose and Benefits**:
     - More reliable performance estimation
     - Better use of limited data
     - Early detection of overfitting
   - **Implementation with Detailed Metrics**:

     #### Multi-metric `cross_validate` with train scores

     **Purpose:** Runs 5-fold CV with both accuracy and weighted F1, optionally exposing train-fold scores to spot overfitting.

     **Walkthrough:**
     - `cross_validate` with `scoring` dict and `return_train_score=True`; prints mean train vs test accuracy.

     ```python
     from sklearn.model_selection import cross_validate
     
     # Define multiple scoring metrics
     scoring = {
         'accuracy': 'accuracy',
         'f1': 'f1_weighted'
     }
     
     # Perform cross-validation with multiple metrics
     scores = cross_validate(
         knn, 
         X_scaled, 
         y,
         cv=5,
         scoring=scoring,
         return_train_score=True
     )
     
     # Print detailed results
     print(f"Training Accuracy: {scores['train_accuracy'].mean():.3f} (+/- {scores['train_accuracy'].std() * 2:.3f})")
     print(f"Validation Accuracy: {scores['test_accuracy'].mean():.3f} (+/- {scores['test_accuracy'].std() * 2:.3f})")
     ```

2. **Hyperparameter Optimization: A Systematic Approach**
   - **Key Parameters to Tune**:
     - <code>n_neighbors</code>: Number of neighbors (k)
     - <code>weights</code>: How to weight the neighbors
       - 'uniform': All neighbors have equal weight
       - 'distance': Weight by inverse of distance
     - <code>metric</code>: Distance metric to use
       - 'euclidean': Standard straight-line distance
       - 'manhattan': City-block distance
       - 'minkowski': Generalization of both
   - **Comprehensive Grid Search**:

     #### Wide grid: `n_neighbors`, weights, Minkowski `metric` and `p`

     **Purpose:** Searches a larger hyperparameter space including Minkowski order `p`, uses parallel workers and verbosity, then reads `best_params_` and `best_score_`.

     **Walkthrough:**
     - `param_grid` includes `'p'` for `metric='minkowski'`; `GridSearchCV(..., n_jobs=-1, verbose=1)`; `fit` on `X_scaled`, `y`.

     ```python
     from sklearn.model_selection import GridSearchCV
     
     # Define extensive parameter grid
     param_grid = {
         'n_neighbors': [3, 5, 7, 9, 11, 13, 15],
         'weights': ['uniform', 'distance'],
         'metric': ['euclidean', 'manhattan', 'minkowski'],
         'p': [1, 2, 3]  # For Minkowski distance
     }
     
     # Create and run grid search with parallel processing
     grid_search = GridSearchCV(
         KNeighborsClassifier(),
         param_grid,
         cv=5,
         scoring='accuracy',
         n_jobs=-1,
         verbose=1
     )
     
     # Fit and get best parameters
     grid_search.fit(X_scaled, y)
     print(f"Best parameters: {grid_search.best_params_}")
     print(f"Best cross-validation score: {grid_search.best_score_:.3f}")
     ```

3. **Model Evaluation and Monitoring**
   - **Performance Metrics**:
     - Accuracy: Overall correctness
     - Precision: Accuracy of positive predictions
     - Recall: Ability to find all positive cases
     - F1-score: Harmonic mean of precision and recall
   - **Implementation**:

     #### Classification report and confusion matrix on held-out data

     **Purpose:** Summarizes per-class precision/recall/F1 and shows the confusion matrix for the KNN’s test predictions.

     **Walkthrough:**
     - `knn.predict(X_test_scaled)`; `classification_report`; `confusion_matrix`.

     ```python
     from sklearn.metrics import classification_report, confusion_matrix
     
     # Get predictions
     y_pred = knn.predict(X_test_scaled)
     
     # Print detailed classification report
     print(classification_report(y_test, y_pred))
     
     # Create confusion matrix
     cm = confusion_matrix(y_test, y_pred)
     print("Confusion Matrix:")
     print(cm)
     ```

Remember: Successful KNN implementation requires careful consideration of:

- Data preprocessing and scaling
- Appropriate k value selection
- Proper handling of categorical variables
- Systematic hyperparameter optimization
- Comprehensive model evaluation

## Additional Resources

For more learning:

- [Scikit-learn KNN Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html)
- [KNN Visualization Tool](https://www.cs.waikato.ac.nz/ml/weka/)
- [Interactive KNN Demo](https://www.cs.cornell.edu/courses/cs4780/2018fa/lectures/lecturenote16.html)

Remember: The key to successful KNN implementation is understanding your data and choosing the right parameters. Don't be afraid to experiment and try different approaches!
