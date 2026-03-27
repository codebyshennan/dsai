# Scikit-learn Pipelines

**After this lesson:** you can explain the core ideas in “Scikit-learn Pipelines” and reproduce the examples here in your own notebook or environment.

Imagine building a car assembly line - each step needs to happen in the right order, and you want to be able to replicate the process exactly. That's what scikit-learn pipelines do for machine learning workflows! Let's learn how to build efficient and reproducible pipelines.

## Helpful video

StatQuest: why cross-validation matters for model evaluation.

<iframe width="560" height="315" src="https://www.youtube.com/embed/fSytzGwwBVw" title="Machine Learning Fundamentals: Cross Validation" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Understanding Pipelines

Pipelines help us:

1. Ensure preprocessing steps are consistent
2. Prevent data leakage
3. Simplify model deployment
4. Make code more maintainable

#### Minimal `Pipeline`: scale then classify

**Purpose:** Show the canonical pattern: preprocessing steps run inside `fit`/`predict`, so the same transformations apply on train and test without leakage.

**Walkthrough:** Steps are named tuples; `StandardScaler` learns on `X_train` only inside `pipeline.fit`; `score` evaluates held-out accuracy.

```python
import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Create sample dataset
np.random.seed(42)
n_samples = 1000

# Generate features
age = np.random.normal(35, 10, n_samples)
income = np.random.exponential(50000, n_samples)
credit_score = np.random.normal(700, 100, n_samples)

X = np.column_stack([age, income, credit_score])
y = (credit_score + income/1000 + age > 800).astype(int)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create simple pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', LogisticRegression())
])

# Fit and evaluate
pipeline.fit(X_train, y_train)
print(f"Pipeline score: {pipeline.score(X_test, y_test):.3f}")
```

**Captured stdout** (from running the snippet above; may be auto-injected on build):

```
Pipeline score: 0.990
```

## Building Complex Pipelines

### Feature Unions

Combine multiple feature processing steps:

#### Parallel feature branches with `FeatureUnion`

**Purpose:** Concatenate outputs from PCA and univariate selection so the classifier sees a wider engineered view of `X` in one `Pipeline`.

**Walkthrough:** `FeatureUnion` runs `pca` and `select_best` on the same input and stacks columns; the final `LogisticRegression` consumes the combined matrix.

```python
from sklearn.pipeline import FeatureUnion
from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectKBest

def create_feature_union_pipeline():
    # Create feature processors
    feature_processing = FeatureUnion([
        ('pca', PCA(n_components=2)),
        ('select_best', SelectKBest(k=2))
    ])
    
    # Create full pipeline
    pipeline = Pipeline([
        ('features', feature_processing),
        ('classifier', LogisticRegression())
    ])
    
    return pipeline

# Create and use pipeline
union_pipeline = create_feature_union_pipeline()
union_pipeline.fit(X_train, y_train)
print(f"Feature union score: {union_pipeline.score(X_test, y_test):.3f}")
```

**Captured stdout** (from running the snippet above; may be auto-injected on build):

```
Feature union score: 0.980
```

### Custom Transformers

Create your own preprocessing steps:

#### Custom `TransformerMixin` for outlier clipping

**Purpose:** Extend sklearn with domain-specific steps while staying compatible with `Pipeline` (implement `fit` / `transform`).

**Walkthrough:** `fit` stores column means/stds; `transform` caps extreme z-scores by replacing masked cells—pair with `StandardScaler` + classifier as usual.

```python
from sklearn.base import BaseEstimator, TransformerMixin

class OutlierHandler(BaseEstimator, TransformerMixin):
    def __init__(self, threshold=3):
        self.threshold = threshold
    
    def fit(self, X, y=None):
        # Calculate z-scores for each feature
        self.mean_ = np.mean(X, axis=0)
        self.std_ = np.std(X, axis=0)
        return self
    
    def transform(self, X):
        # Replace outliers with mean values
        z_scores = np.abs((X - self.mean_) / self.std_)
        mask = z_scores > self.threshold
        X_copy = X.copy()
        X_copy[mask] = np.take(self.mean_, range(X.shape[1]))
        return X_copy

# Use custom transformer in pipeline
pipeline_with_custom = Pipeline([
    ('outlier_handler', OutlierHandler(threshold=3)),
    ('scaler', StandardScaler()),
    ('classifier', LogisticRegression())
])

pipeline_with_custom.fit(X_train, y_train)
print(f"Custom pipeline score: {pipeline_with_custom.score(X_test, y_test):.3f}")
```

## Real-World Example: Text Classification

#### Text preprocessing + TF–IDF + logistic regression in one `Pipeline`

**Purpose:** Chain token cleanup, sparse vectorization, and a linear model so raw strings never bypass the same path used at training time.

**Walkthrough:** `FunctionTransformer` wraps list-wise `preprocess_text`; `TfidfVectorizer` builds sparse features; `train_test_split` on lists works like tabular splits.

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import FunctionTransformer
import re

# Sample text data
texts = [
    "Machine learning is fascinating",
    "Deep neural networks are powerful",
    "Data science is growing rapidly",
    "AI transforms industries"
]
labels = [1, 1, 1, 1]  # Positive class for all

def preprocess_text(text):
    """Basic text preprocessing"""
    # Convert to lowercase
    text = text.lower()
    # Remove special characters
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text

# Create text processing pipeline
text_pipeline = Pipeline([
    ('preprocessor', FunctionTransformer(lambda x: [preprocess_text(text) for text in x])),
    ('vectorizer', TfidfVectorizer(max_features=1000)),
    ('classifier', LogisticRegression())
])

# Split text data
X_train, X_test, y_train, y_test = train_test_split(
    texts, labels, test_size=0.2, random_state=42
)

# Fit pipeline
text_pipeline.fit(X_train, y_train)

# Make predictions
predictions = text_pipeline.predict(X_test)
```

## Pipeline Persistence

Save and load pipelines:

#### Serialize a fitted pipeline with `joblib`

**Purpose:** Deploy or resume training by dumping the entire estimator graph—including any fitted preprocessing—to disk.

**Walkthrough:** `joblib.dump` / `load` preserves Python objects; use the same sklearn version when unpickling in production.

```python
import joblib

def save_pipeline(pipeline, filename):
    """Save pipeline to file"""
    joblib.dump(pipeline, filename)

def load_pipeline(filename):
    """Load pipeline from file"""
    return joblib.load(filename)

# Example usage
save_pipeline(pipeline, 'model_pipeline.joblib')
loaded_pipeline = load_pipeline('model_pipeline.joblib')
```

## Advanced Techniques

### 1. Memory Caching

#### Cache intermediate pipeline outputs on disk

**Purpose:** Speed up repeated fits during tuning by memoizing transformers when inputs are unchanged (large grids or CV).

**Walkthrough:** Prefer `from joblib import Memory` on current sklearn; `memory=` attaches to the `Pipeline` so steps reuse cached transforms when possible.

```python
from sklearn.pipeline import Pipeline
from sklearn.externals import Memory

# Set up caching
memory = Memory(location='./cachedir', verbose=0)

# Create pipeline with caching
cached_pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('pca', PCA(n_components=2)),
    ('classifier', LogisticRegression())
], memory=memory)
```

### 2. Parameter Grid Search

#### Tune nested steps with `__` hyperparameter names

**Purpose:** Search preprocessing and model settings jointly while respecting pipeline ordering—no manual refits between steps.

**Walkthrough:** Keys like `pca__n_components` target step attributes; `GridSearchCV` runs inner CV on the full `pipeline` object.

```python
from sklearn.model_selection import GridSearchCV

# Define parameters for multiple steps
param_grid = {
    'scaler__with_mean': [True, False],
    'pca__n_components': [2, 3, 4],
    'classifier__C': [0.1, 1.0, 10.0]
}

# Perform grid search
grid_search = GridSearchCV(pipeline, param_grid, cv=5)
grid_search.fit(X_train, y_train)
```

### 3. Column Transformer

#### Different transformers per column group

**Purpose:** Apply numeric scaling and one-hot encoding in parallel, then feed the concatenated matrix to a single estimator—essential for mixed-type tables.

**Walkthrough:** Indices `[0,1]` / `[2]` are placeholders; replace with column names + `ColumnTransformer(..., remainder='drop')` in real projects.

```python
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

# Create column transformer
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), [0, 1]),  # Numerical columns
        ('cat', OneHotEncoder(), [2])       # Categorical columns
    ])

# Create pipeline with column transformer
column_pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression())
])
```

## Best Practices

### 1. Naming Conventions

#### Readable step names for grids and debugging

**Purpose:** Names appear in `get_params()`, error traces, and `GridSearchCV` keys—clear labels save time when pipelines grow.

**Walkthrough:** Order matches execution left-to-right; each name must be unique in the `Pipeline` list.

```python
# Use descriptive names for steps
pipeline = Pipeline([
    ('missing_handler', SimpleImputer()),
    ('feature_scaler', StandardScaler()),
    ('dim_reducer', PCA()),
    ('classifier', LogisticRegression())
])
```

### 2. Error Handling

#### Illustrative try/except inside `transform`

**Purpose:** Show a pattern for failing soft on bad batches; production code should log and validate inputs explicitly.

**Walkthrough:** `transformed_X` is not defined in the stub—replace with real logic; fallback returns `X` unchanged.

```python
class RobustTransformer(BaseEstimator, TransformerMixin):
    def transform(self, X):
        try:
            # Transformation logic
            return transformed_X
        except Exception as e:
            print(f"Error in transformation: {e}")
            # Return safe fallback
            return X
```

### 3. Validation

#### CV helper for any pipeline object

**Purpose:** Score the full pipeline out-of-fold so preprocessing is refit each fold—mirrors honest generalization.

**Walkthrough:** `cross_val_score` clones `pipeline` per fold; function prints fold scores plus mean $\pm$2 std.

```python
from sklearn.model_selection import cross_val_score

def validate_pipeline(pipeline, X, y, cv=5):
    # Perform cross-validation
    scores = cross_val_score(pipeline, X, y, cv=cv)
    
    # Print results
    print(f"Cross-validation scores: {scores}")
    print(f"Mean CV score: {scores.mean():.3f} (+/- {scores.std() * 2:.3f})")
```

## Common Pitfalls and Solutions

1. **Data Leakage**
   - Keep all preprocessing in pipeline
   - Use ColumnTransformer for mixed data
   - Validate transformation order

2. **Memory Issues**
   - Use memory caching
   - Implement batch processing
   - Monitor memory usage

3. **Performance**
   - Profile pipeline steps
   - Optimize transformers
   - Use parallel processing

## Additional Resources

- [Scikit-learn Pipeline Documentation](https://scikit-learn.org/stable/modules/pipeline.html)
- [Pipeline Best Practices](https://scikit-learn.org/stable/modules/compose.html)
- [Custom Transformers Guide](https://scikit-learn.org/stable/modules/generated/sklearn.base.TransformerMixin.html)

Remember: Pipelines are your best friend for reproducible machine learning workflows!
