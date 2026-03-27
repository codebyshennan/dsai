# Advanced Topics in Naive Bayes

**After this lesson:** you can explain the core ideas in “Advanced Topics in Naive Bayes” and reproduce the examples here in your own notebook or environment.

## Helpful video

Crash Course AI: supervised learning for classical algorithms.

<iframe width="560" height="315" src="https://www.youtube.com/embed/4qVRBYAdLAo" title="Supervised Learning: Crash Course AI" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Welcome to Advanced Naive Bayes

Now that you've mastered the basics, let's explore some advanced techniques that will make your Naive Bayes models even better. Think of this as adding special tools to your machine learning toolbox!

## 1. Feature Engineering: Making Your Data Work Better

### What is Feature Engineering?

Feature engineering is like being a chef who transforms basic ingredients into a delicious meal. You take your raw data and transform it into features that help your model make better predictions.

### Text Feature Engineering

Let's say you're building a spam detector. Instead of just using raw words, you can create smarter features:

#### TF-IDF pipeline with custom preprocessing

**Purpose:** Show a `Pipeline` of `TfidfVectorizer` (with a callable `preprocessor` for cleaning) plus `MultinomialNB`, without extra NLP dependencies.

**Walkthrough:**
- `normalize_text` lowercases and strips non-letters (keeping `!?.`).
- `TfidfVectorizer(preprocessor=..., ngram_range=(1, 3), max_features=1000)` feeds `MultinomialNB`.

```python
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline


def normalize_text(text):
    """Lightweight cleaning before tokenization."""
    text = text.lower()
    return re.sub(r"[^a-zA-Z\s!?.]", "", text)


pipeline = Pipeline(
    [
        (
            "vectorizer",
            TfidfVectorizer(
                preprocessor=normalize_text,
                ngram_range=(1, 3),
                max_features=1000,
            ),
        ),
        ("classifier", MultinomialNB()),
    ]
)
```

### Numerical Feature Engineering

When working with numbers (like age or income), you can transform them to better fit the Gaussian distribution:

#### Power transform + Gaussian NB

**Purpose:** Pipeline `PowerTransformer` (Yeo–Johnson) before `GaussianNB` when features are skewed.

**Walkthrough:**
- `PowerTransformer(method='yeo-johnson')` learns a per-feature transform; `GaussianNB` then fits on the transformed space.

```python
from sklearn.preprocessing import PowerTransformer
from sklearn.naive_bayes import GaussianNB
from sklearn.pipeline import Pipeline

def transform_numerical_features():
    """Create better numerical features"""
    return Pipeline([
        ('transformer', PowerTransformer(
            method='yeo-johnson'  # Handles positive and negative numbers
        )),
        ('classifier', GaussianNB())
    ])
```

## 2. Handling Missing Data: Don't Let Gaps Stop You

### Why Missing Data Matters

Imagine you're a doctor with incomplete patient records. You can't just ignore missing information - you need to handle it smartly!

### Smart Ways to Handle Missing Data

#### KNN imputer + scaler + Gaussian NB (sketch)

**Purpose:** Illustrate plugging `KNNImputer` (or `IterativeImputer`) ahead of scaling and `GaussianNB` in a `Pipeline`.

**Walkthrough:**
- `KNNImputer(n_neighbors=5)` fills missing numeric cells; `StandardScaler` then `GaussianNB` for the final classifier.

```python
from sklearn.experimental import enable_iterative_imputer  # noqa: F401
from sklearn.impute import KNNImputer, IterativeImputer
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.pipeline import Pipeline

class SmartDataImputer:
    def __init__(self, strategy='knn'):
        self.strategy = strategy
        
    def impute(self, data):
        """Fill in missing values intelligently"""
        if self.strategy == 'knn':
            # Use similar patients to fill in missing values
            imputer = KNNImputer(n_neighbors=5)
        else:
            # Use iterative approach (enable experimental import in sklearn if required)
            imputer = IterativeImputer(max_iter=10)
            
        return imputer.fit_transform(data)

# Prefer sklearn imputers directly inside Pipeline (SmartDataImputer is illustrative)
pipeline = Pipeline([
    ('imputer', KNNImputer(n_neighbors=5)),
    ('scaler', StandardScaler()),
    ('classifier', GaussianNB())
])
```

## 3. Ensemble Methods: Teamwork Makes the Dream Work

### What are Ensembles?

An ensemble is like a team of experts working together. Instead of relying on one model, we combine multiple models to get better predictions.

### Voting Classifier

#### VotingClassifier with multiple NB variants (illustrative)

**Purpose:** Show how `VotingClassifier` combines estimators; in practice each base learner must see compatible features (often separate pipelines per modality).

**Walkthrough:**
- List named steps (`multinomial`, `gaussian`, `bernoulli`); `voting='soft'` averages predicted probabilities.

```python
from sklearn.ensemble import VotingClassifier
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB

def create_naive_bayes_team():
    """Create a team of Naive Bayes models"""
    models = [
        ('multinomial', MultinomialNB()),  # For text
        ('gaussian', GaussianNB()),        # For numbers
        ('bernoulli', BernoulliNB())       # For yes/no features
    ]
    
    return VotingClassifier(
        estimators=models,
        voting='soft'  # Use probability estimates
    )
```

### Stacking Classifier

#### StackingClassifier with logistic meta-learner

**Purpose:** Stack several Naive Bayes variants with `LogisticRegression` as the final estimator (conceptual; feature alignment across bases is required in real use).

**Walkthrough:**
- `StackingClassifier(estimators=..., final_estimator=LogisticRegression(), cv=5)`.

```python
from sklearn.ensemble import StackingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB

def create_stacked_model():
    """Create a stacked model with Naive Bayes"""
    base_models = [
        ('mnb', MultinomialNB()),
        ('gnb', GaussianNB()),
        ('bnb', BernoulliNB())
    ]
    
    return StackingClassifier(
        estimators=base_models,
        final_estimator=LogisticRegression(),
        cv=5  # Use 5-fold cross-validation
    )
```

## 4. Model Deployment: Taking Your Model to the Real World

### Saving Your Model

#### Persist estimator with joblib and sidecar JSON

**Purpose:** Save a fitted model to disk with `joblib` and optional metadata for deployment.

**Walkthrough:**
- `joblib.dump` the estimator; write `model_info.json`; `load` reverses the steps.

```python
import json

import joblib

class ModelSaver:
    def __init__(self, model, info=None):
        self.model = model
        self.info = info or {}
        
    def save(self, folder):
        """Save model and its information"""
        # Save the model
        joblib.dump(self.model, f"{folder}/model.joblib")
        
        # Save additional information
        with open(f"{folder}/model_info.json", 'w') as f:
            json.dump(self.info, f)
            
    @classmethod
    def load(cls, folder):
        """Load a saved model"""
        model = joblib.load(f"{folder}/model.joblib")
        with open(f"{folder}/model_info.json", 'r') as f:
            info = json.load(f)
        return cls(model, info)
```

### Monitoring Your Model

#### Track predictions for simple drift-style checks

**Purpose:** Keep a lightweight log of predictions (and optional labels) to compute rolling accuracy offline.

**Walkthrough:**
- Append dicts with `features`, `prediction`, optional `actual`, and `datetime.now()`.

```python
from datetime import datetime

class ModelMonitor:
    def __init__(self):
        self.predictions = []
        self.timestamps = []
        
    def track_prediction(self, features, prediction, actual=None):
        """Keep track of model predictions"""
        self.predictions.append({
            'features': features,
            'prediction': prediction,
            'actual': actual,
            'time': datetime.now()
        })
        
    def check_performance(self, window=100):
        """Check recent model performance"""
        if len(self.predictions) < window:
            return "Not enough data"
            
        recent = self.predictions[-window:]
        accuracy = sum(1 for p in recent if p['prediction'] == p['actual']) / window
        return f"Recent accuracy: {accuracy:.2%}"
```

## 5. Hyperparameter Tuning: Finding the Best Settings

### What are Hyperparameters?

Hyperparameters are like the settings on your camera. You need to adjust them to get the best results for each situation.

### Finding the Best Settings

#### RandomizedSearchCV over vectorizer + MultinomialNB

**Purpose:** Search `max_features`, `ngram_range`, and `alpha` on a text pipeline with cross-validation.

**Walkthrough:**
- `param_options` uses `randint` / `uniform` distributions; `RandomizedSearchCV(..., n_iter=20, cv=3)`; return `best_params_`.

```python
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import uniform, randint
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

def find_best_settings(X, y):
    """Find the best hyperparameters"""
    # Define what settings to try
    param_options = {
        'vectorizer__max_features': randint(100, 10000),
        'vectorizer__ngram_range': [(1, 1), (1, 2), (1, 3)],
        'classifier__alpha': uniform(0.1, 2.0)
    }
    
    # Create the model
    model = Pipeline([
        ('vectorizer', TfidfVectorizer()),
        ('classifier', MultinomialNB())
    ])
    
    # Search for best settings
    search = RandomizedSearchCV(
        model, param_options,
        n_iter=20,  # Try 20 different combinations
        cv=3,       # Use 3-fold CV (needs enough samples vs n_splits)
        scoring='accuracy'
    )
    
    # Find the best settings
    search.fit(X, y)
    return search.best_params_


# Example: small text corpus (enough rows for cv=3)
X_text = [
    "sports team wins game",
    "stock market news today",
    "team scores in final quarter",
    "finance report earnings beat",
    "championship final overtime",
    "investors buy tech shares",
    "roster injury update",
    "quarterly revenue growth",
    "playoff bracket announced",
    "dividend yield increases",
]
y_text = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
best = find_best_settings(X_text, y_text)
```

## Common Advanced Challenges and Solutions

### 1. Dealing with Class Imbalance

When one class is much more common than others:

#### Normalize balanced weights to `class_prior`

**Purpose:** Turn `compute_class_weight` outputs into a proper prior vector summing to 1 for `MultinomialNB`.

```python
import numpy as np
from sklearn.utils.class_weight import compute_class_weight
from sklearn.naive_bayes import MultinomialNB

y = np.array([0] * 90 + [1] * 10)
class_weights = compute_class_weight("balanced", classes=np.unique(y), y=y)
priors = class_weights / class_weights.sum()
model = MultinomialNB(class_prior=priors)
```

### 2. Handling High-Dimensional Data

When you have too many features:

#### Chi-squared feature selection before NB

**Purpose:** Reduce dimensionality with `SelectKBest` and `chi2` (non-negative counts required).

**Walkthrough:**
- `SelectKBest(chi2, k=1000).fit_transform(X, y)` returns a reduced sparse or dense matrix.

```python
import numpy as np
from sklearn.feature_selection import SelectKBest, chi2
from scipy.sparse import csr_matrix

rng = np.random.default_rng(0)
X = csr_matrix(rng.integers(1, 10, size=(50, 200)))
y = rng.integers(0, 2, size=50)

selector = SelectKBest(chi2, k=100)  # keep top features for this toy size
X_new = selector.fit_transform(X, y)
```

### 3. Improving Numeric Stability

When dealing with very small probabilities:

#### Argmax on `predict_log_proba`

**Purpose:** Use log-probabilities for numerical stability when comparing classes (equivalent argmax to `predict` for many models).

**Walkthrough:**
- Fit `BernoulliNB` on a tiny binary matrix; `predict_log_proba` then `np.argmax` along classes.

```python
import numpy as np
from sklearn.naive_bayes import BernoulliNB

X = np.array([[1, 0, 1], [0, 1, 0], [1, 1, 0]])
y = np.array([0, 1, 0])
model = BernoulliNB().fit(X, y)

log_probs = model.predict_log_proba(X)
predictions = np.argmax(log_probs, axis=1)
```

## Next Steps

Ready to become a Naive Bayes expert? Try these challenges:

1. Implement feature engineering in your own project
2. Experiment with different ensemble methods
3. Deploy a model and monitor its performance
4. Try hyperparameter tuning on a real dataset

Remember: The best way to learn is by doing! Start with small experiments and gradually tackle more complex problems.
