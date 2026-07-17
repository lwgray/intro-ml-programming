# Appendix C: Cross-Validation Implementation Guide

**Complete standalone reference for cross-validation in machine learning**

---

## Table of Contents

1. [What is Cross-Validation?](#what-is-cross-validation)
2. [Why Use Cross-Validation?](#why-use-cross-validation)
3. [Types of Cross-Validation](#types-of-cross-validation)
4. [Implementation with sklearn](#implementation-with-sklearn)
5. [Choosing K (Number of Folds)](#choosing-k-number-of-folds)
6. [Interpreting Results](#interpreting-results)
7. [Common Mistakes](#common-mistakes)
8. [Advanced Techniques](#advanced-techniques)
9. [When NOT to Use Cross-Validation](#when-not-to-use-cross-validation)
10. [Complete Code Examples](#complete-code-examples)

---

## What is Cross-Validation?

Cross-validation is a model evaluation technique that assesses how well a machine learning model generalizes to unseen data by:

1. **Splitting the dataset into multiple subsets** (called "folds")
2. **Training and testing multiple times**, each time using a different fold as the test set
3. **Averaging the results** to get a more reliable performance estimate

**Key Principle:** Instead of relying on a single train/test split, cross-validation uses multiple splits to reduce variance in performance estimates.

---

## Why Use Cross-Validation?

### Problem with Single Train/Test Split

```python
from sklearn.model_selection import train_test_split

# Single split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model.fit(X_train, y_train)
score = model.score(X_test, y_test)  # One number: e.g., 0.85
```

**Limitations:**
- **Variance**: Score depends heavily on which 20% ended up in test set
- **Luck factor**: Might get "easy" or "hard" test set by chance
- **No confidence interval**: Is 0.85 good? Could it be 0.75 or 0.95?
- **Wastes data**: Only trains on 80% of data

### Solution: Cross-Validation

```python
from sklearn.model_selection import cross_val_score

# Multiple splits
scores = cross_val_score(model, X, y, cv=5)  # Five different train/test splits
print(f"Scores: {scores}")  # e.g., [0.83, 0.87, 0.81, 0.85, 0.84]
print(f"Mean: {scores.mean():.3f} ± {scores.std():.3f}")  # 0.84 ± 0.021
```

**Advantages:**
- **Reduced variance**: Average of 5 scores is more stable
- **Confidence interval**: Standard deviation shows reliability
- **Better data usage**: Each sample is used for training and testing
- **Robustness check**: Large std indicates model is unstable

---

## Types of Cross-Validation

### 1. K-Fold Cross-Validation

**Most common type.** Splits data into K equal-sized folds.

```
Dataset: [1 2 3 4 5 6 7 8 9 10]  (10 samples, K=5)

Fold 1: Test [1 2]      Train [3 4 5 6 7 8 9 10]  → Score 1
Fold 2: Test [3 4]      Train [1 2 5 6 7 8 9 10]  → Score 2
Fold 3: Test [5 6]      Train [1 2 3 4 7 8 9 10]  → Score 3
Fold 4: Test [7 8]      Train [1 2 3 4 5 6 9 10]  → Score 4
Fold 5: Test [9 10]     Train [1 2 3 4 5 6 7 8]  → Score 5

Final score: Average(Score 1, Score 2, ..., Score 5)
```

**Implementation:**

```python
from sklearn.model_selection import KFold, cross_val_score
from sklearn.linear_model import LogisticRegression

# Create K-Fold splitter
kfold = KFold(n_splits=5, shuffle=True, random_state=42)

# Evaluate model
model = LogisticRegression()
scores = cross_val_score(model, X, y, cv=kfold, scoring='accuracy')

print(f"Scores: {scores}")
print(f"Mean accuracy: {scores.mean():.3f} ± {scores.std():.3f}")
```

**Parameters:**
- `n_splits`: Number of folds (K). Default: 5
- `shuffle`: Whether to shuffle data before splitting. Default: False
- `random_state`: Seed for reproducibility when shuffle=True

**When to use:**
- Default choice for most problems
- Balanced datasets
- When you want good bias-variance tradeoff

---

### 2. Stratified K-Fold Cross-Validation

**For imbalanced classification.** Ensures each fold has the same class distribution as the complete dataset.

**Example Problem:**

```
Dataset: 90 samples class 0, 10 samples class 1

Regular K-Fold (K=5):
Fold 1: 20 samples → might get 19 class 0, 1 class 1  (imbalanced!)
Fold 2: 20 samples → might get 17 class 0, 3 class 1
Fold 3: 20 samples → might get 20 class 0, 0 class 1  (no class 1!)
...

Stratified K-Fold (K=5):
Fold 1: 20 samples → guaranteed 18 class 0, 2 class 1  (balanced!)
Fold 2: 20 samples → guaranteed 18 class 0, 2 class 1
Fold 3: 20 samples → guaranteed 18 class 0, 2 class 1
...
Each fold represents the 90/10 distribution!
```

**Implementation:**

```python
from sklearn.model_selection import StratifiedKFold, cross_val_score

# Create Stratified K-Fold splitter
skfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# Evaluate model
scores = cross_val_score(model, X, y, cv=skfold, scoring='accuracy')

print(f"Mean accuracy: {scores.mean():.3f} ± {scores.std():.3f}")
```

**When to use:**
- **Classification problems** with imbalanced classes
- When some classes have very few samples
- Default for classification in sklearn (cross_val_score uses StratifiedKFold automatically for classifiers)

**Not applicable to:**
- Regression problems (no classes to stratify)

---

### 3. Leave-One-Out Cross-Validation (LOOCV)

**Extreme case: K = N** (number of samples). Each sample is a test set once.

```
Dataset: [1 2 3 4 5]  (5 samples)

Fold 1: Test [1]      Train [2 3 4 5]  → Score 1
Fold 2: Test [2]      Train [1 3 4 5]  → Score 2
Fold 3: Test [3]      Train [1 2 4 5]  → Score 3
Fold 4: Test [4]      Train [1 2 3 5]  → Score 4
Fold 5: Test [5]      Train [1 2 3 4]  → Score 5

Final score: Average(all 5 scores)
```

**Implementation:**

```python
from sklearn.model_selection import LeaveOneOut, cross_val_score

# Create LOOCV splitter
loo = LeaveOneOut()

# Evaluate model
scores = cross_val_score(model, X, y, cv=loo, scoring='accuracy')

print(f"Number of folds: {len(scores)}")  # Same as number of samples!
print(f"Mean accuracy: {scores.mean():.3f} ± {scores.std():.3f}")
```

**Advantages:**
- **Maximum data usage**: Train on N-1 samples each time
- **Deterministic**: No randomness in splitting
- **Low bias**: Nearly all data used for training

**Disadvantages:**
- **Very slow**: N model trainings for N samples
- **High variance**: Each test set has only 1 sample
- **Not recommended for large datasets** (computationally expensive)

**When to use:**
- **Small datasets only** (N < 100)
- When you can't afford to "waste" data in a test set
- When computational time is not a concern

---

### 4. Time Series Cross-Validation

**For temporal data.** Respects time order - never trains on future data to predict past.

**Standard K-Fold is WRONG for time series:**

```
Time series: [Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec]

Regular K-Fold might do:
Fold 1: Test [Mar Apr]      Train [Jan Feb May Jun Jul Aug Sep Oct Nov Dec]
        ⚠️ Training on future data (May-Dec) to predict past (Mar-Apr)!
```

**Time Series Split is CORRECT:**

```
Time series: [Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec]

Fold 1: Test [May]          Train [Jan Feb Mar Apr]
Fold 2: Test [Jun]          Train [Jan Feb Mar Apr May]
Fold 3: Test [Jul]          Train [Jan Feb Mar Apr May Jun]
Fold 4: Test [Aug]          Train [Jan Feb Mar Apr May Jun Jul]
Fold 5: Test [Sep]          Train [Jan Feb Mar Apr May Jun Jul Aug]
...

Always: Train on PAST → Predict FUTURE
```

**Implementation:**

```python
from sklearn.model_selection import TimeSeriesSplit, cross_val_score

# Create Time Series splitter
tscv = TimeSeriesSplit(n_splits=5)

# Evaluate model
scores = cross_val_score(model, X, y, cv=tscv, scoring='r2')

print(f"Mean R²: {scores.mean():.3f} ± {scores.std():.3f}")
```

**Visualization of splits:**

```python
import numpy as np

# Show how TimeSeriesSplit creates folds
X = np.arange(100)  # 100 time steps
tscv = TimeSeriesSplit(n_splits=5)

for i, (train_idx, test_idx) in enumerate(tscv.split(X)):
    print(f"Fold {i+1}:")
    print(f"  Train: {train_idx[0]} to {train_idx[-1]} ({len(train_idx)} samples)")
    print(f"  Test:  {test_idx[0]} to {test_idx[-1]} ({len(test_idx)} samples)")
```

**When to use:**
- Stock prices, sales forecasting, weather prediction
- Any data with temporal dependencies
- When order matters!

**When NOT to use:**
- Non-temporal data (use regular K-Fold instead)

---

### 5. Group K-Fold Cross-Validation

**For grouped data.** Ensures samples from the same group don't appear in both train and test.

**Example Problem:**

```
Medical data: Multiple measurements per patient

Patient A: [measurement1, measurement2, measurement3]
Patient B: [measurement1, measurement2]
Patient C: [measurement1, measurement2, measurement3, measurement4]

WRONG (regular K-Fold):
Train: [Patient A measurement1, Patient B measurement1, Patient C measurement1]
Test:  [Patient A measurement2, Patient B measurement2, Patient C measurement2]
⚠️ Patient A data in both train AND test → Leakage!

CORRECT (Group K-Fold):
Train: [All measurements from Patient A, Patient B]
Test:  [All measurements from Patient C]
✓ No patient appears in both train and test
```

**Implementation:**

```python
from sklearn.model_selection import GroupKFold, cross_val_score

# Define groups (e.g., patient IDs)
groups = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4]  # Patient IDs for 11 measurements

# Create Group K-Fold splitter
gkfold = GroupKFold(n_splits=3)

# Evaluate model
scores = cross_val_score(model, X, y, cv=gkfold, groups=groups, scoring='accuracy')

print(f"Mean accuracy: {scores.mean():.3f} ± {scores.std():.3f}")
```

**When to use:**
- Medical data (multiple measurements per patient)
- Customer data (multiple transactions per customer)
- Sensor data (multiple readings per device)
- When samples are not independent

---

## Implementation with sklearn

### Method 1: `cross_val_score()` (Simple)

**Best for:** Quick evaluation with a single metric

```python
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=100, random_state=42)
scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')

print(f"Accuracy: {scores.mean():.3f} ± {scores.std():.3f}")
```

**Parameters:**
- `estimator`: Model to evaluate
- `X`: Features
- `y`: Target
- `cv`: Number of folds or CV splitter object
- `scoring`: Metric to compute (see Scoring Metrics below)
- `n_jobs`: Number of CPU cores to use (-1 = all cores)

**Returns:**
- Array of scores, one per fold

---

### Method 2: `cross_validate()` (Advanced)

**Best for:** Multiple metrics, access to train scores, fit times

```python
from sklearn.model_selection import cross_validate

results = cross_validate(
    model, X, y, cv=5,
    scoring=['accuracy', 'precision', 'recall'],
    return_train_score=True,
    return_estimator=True
)

print("Test accuracy:", results['test_accuracy'].mean())
print("Test precision:", results['test_precision'].mean())
print("Test recall:", results['test_recall'].mean())
print("Fit times:", results['fit_time'])
print("Score times:", results['score_time'])
```

**Returns:** Dictionary with:
- `test_<metric>`: Test scores for each metric
- `train_<metric>`: Train scores (if return_train_score=True)
- `fit_time`: Time to fit each fold
- `score_time`: Time to score each fold
- `estimator`: Trained models (if return_estimator=True)

---

### Method 3: Manual Loop (Full Control)

**Best for:** Custom logic, saving predictions, debugging

```python
from sklearn.model_selection import KFold
import numpy as np

kfold = KFold(n_splits=5, shuffle=True, random_state=42)
scores = []

for fold, (train_idx, test_idx) in enumerate(kfold.split(X)):
    # Split data
    X_train, X_test = X[train_idx], X[test_idx]
    y_train, y_test = y[train_idx], y[test_idx]

    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate
    score = model.score(X_test, y_test)
    scores.append(score)

    print(f"Fold {fold+1}: {score:.3f}")

print(f"\nMean: {np.mean(scores):.3f} ± {np.std(scores):.3f}")
```

**When to use:**
- Need predictions for each fold
- Custom evaluation logic
- Debugging cross-validation issues

---

## Scoring Metrics

### Classification Metrics

```python
# Accuracy (default for classifiers)
scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')

# Precision, Recall, F1
scores = cross_val_score(model, X, y, cv=5, scoring='precision')  # Binary only
scores = cross_val_score(model, X, y, cv=5, scoring='precision_weighted')  # Multiclass

# ROC AUC
scores = cross_val_score(model, X, y, cv=5, scoring='roc_auc')  # Binary only
scores = cross_val_score(model, X, y, cv=5, scoring='roc_auc_ovr')  # Multiclass

# Log Loss
scores = cross_val_score(model, X, y, cv=5, scoring='neg_log_loss')
```

### Regression Metrics

```python
# R² (default for regressors)
scores = cross_val_score(model, X, y, cv=5, scoring='r2')

# Mean Squared Error (note: negative!)
scores = cross_val_score(model, X, y, cv=5, scoring='neg_mean_squared_error')
rmse = np.sqrt(-scores)  # Convert to RMSE

# Mean Absolute Error (note: negative!)
scores = cross_val_score(model, X, y, cv=5, scoring='neg_mean_absolute_error')
mae = -scores
```

**Note:** sklearn returns negative error scores (to maintain "higher is better" convention)

### Custom Scoring

```python
from sklearn.metrics import make_scorer, f1_score

# Define custom scorer
def custom_metric(y_true, y_pred):
    # Your custom logic
    return f1_score(y_true, y_pred, average='weighted') * 2

scorer = make_scorer(custom_metric)
scores = cross_val_score(model, X, y, cv=5, scoring=scorer)
```

---

## Choosing K (Number of Folds)

### Common Values

| K | Train% | Test% | Use Case |
|---|--------|-------|----------|
| 3 | 67% | 33% | Quick experiments, very small datasets |
| 5 | 80% | 20% | **Default choice** - good balance |
| 10 | 90% | 10% | More thorough, larger datasets |
| N (LOOCV) | ~100% | ~0% | Very small datasets only |

### Guidelines

**Use K=3:**
- Very small datasets (N < 100)
- Expensive models (deep learning)
- Quick prototyping

**Use K=5 (Most Common):**
- Medium datasets (100 < N < 10,000)
- Default choice
- Good bias-variance tradeoff

**Use K=10:**
- Large datasets (N > 10,000)
- When computational cost is not an issue
- When you want more thorough evaluation

**Use LOOCV (K=N):**
- Very small datasets (N < 50)
- When data is precious
- Academic/research settings

### Bias-Variance Tradeoff

```
K=2 (50% train)
↓
More bias (less training data)
Less variance (more unique test sets)
Faster

K=5 (80% train)
↓
Balanced

K=10 (90% train)
↓
Less bias (more training data)
More variance (similar test sets)
Slower

K=N (LOOCV)
↓
Very low bias
Very high variance
Very slow
```

**Empirical finding:** K=5 or K=10 typically gives best bias-variance tradeoff.

---

## Interpreting Results

### Understanding Mean and Standard Deviation

```python
scores = cross_val_score(model, X, y, cv=5)
# Output: [0.82, 0.85, 0.81, 0.87, 0.84]

mean = scores.mean()  # 0.838
std = scores.std()    # 0.023

print(f"{mean:.3f} ± {std:.3f}")
# Output: 0.838 ± 0.023
```

**Interpretation:**

**Mean (0.838):**
- Expected performance on unseen data
- More reliable than single train/test split

**Standard Deviation (0.023):**
- **Low std (< 0.05)**: Model is **stable** - performs consistently
- **High std (> 0.10)**: Model is **unstable** - sensitive to training data

**Example comparisons:**

```python
Model A: 0.85 ± 0.02  (stable, reliable)
Model B: 0.87 ± 0.15  (higher mean but unstable!)

Choose Model A! Consistency matters.
```

### Statistical Significance

**Question:** Is Model A (0.85 ± 0.02) really better than Model B (0.83 ± 0.03)?

**Basic rule of thumb:**
- If confidence intervals overlap → difference might not be significant
- If intervals don't overlap → difference likely significant

```python
# Confidence interval (approximate): mean ± 2*std
Model A: [0.81, 0.89]  # 0.85 ± 2*0.02
Model B: [0.77, 0.89]  # 0.83 ± 2*0.03
# Overlap → difference might not be significant
```

**Formal test (paired t-test):**

```python
from scipy import stats

scores_A = cross_val_score(model_A, X, y, cv=5)
scores_B = cross_val_score(model_B, X, y, cv=5)

t_stat, p_value = stats.ttest_rel(scores_A, scores_B)

if p_value < 0.05:
    print("Statistically significant difference")
else:
    print("No significant difference")
```

---

## Common Mistakes

### Mistake 1: Data Leakage - Preprocessing Before Cross-Validation

**WRONG:**

```python
# ❌ Fit scaler on ALL data before CV
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)  # ← Leakage! Test folds influence scaler

scores = cross_val_score(model, X_scaled, y, cv=5)  # Inflated scores!
```

**Problem:** Scaler learned statistics from ALL data, including test folds. Test data "leaked" into training.

**CORRECT:**

```python
# ✓ Use Pipeline - preprocessing happens inside CV
from sklearn.pipeline import Pipeline

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression())
])

scores = cross_val_score(pipeline, X, y, cv=5)  # No leakage!
```

**Why Pipeline works:**
- For each fold, scaler fits on training data only
- Scaler transforms test data using training statistics
- No leakage!

---

### Mistake 2: Not Shuffling Data

**Problem:** If data has order (e.g., sorted by class), folds might be imbalanced

```python
# Data sorted: [0,0,0,0,0,1,1,1,1,1]

# Without shuffle - BAD
kfold = KFold(n_splits=5, shuffle=False)
# Fold 1: Test [0,0]  Train [0,0,0,1,1,1,1,1]  ← Imbalanced!
# Fold 2: Test [0,0]  Train [0,0,1,1,1,1,1,1]
# Fold 3: Test [0,1]  Train [0,0,0,0,1,1,1,1]
# Fold 4: Test [1,1]  Train [0,0,0,0,0,1,1,1]
# Fold 5: Test [1,1]  Train [0,0,0,0,0,0,1,1]

# With shuffle - GOOD
kfold = KFold(n_splits=5, shuffle=True, random_state=42)
# Folds are now mixed!
```

**Solution:** Always use `shuffle=True` (unless data is temporal)

---

### Mistake 3: Using Cross-Validation for Hyperparameter Tuning Incorrectly

**WRONG:**

```python
# ❌ Tune hyperparameters using CV, then report CV score
best_score = 0
for max_depth in [3, 5, 10]:
    model = DecisionTreeClassifier(max_depth=max_depth)
    scores = cross_val_score(model, X, y, cv=5)
    if scores.mean() > best_score:
        best_score = scores.mean()
        best_depth = max_depth

print(f"Best score: {best_score}")  # ← Optimistically biased!
```

**Problem:** You tuned on the CV data, so the CV score is biased (optimistic).

**CORRECT:**

```python
# ✓ Use nested cross-validation or separate validation set
from sklearn.model_selection import GridSearchCV

# Method 1: Use GridSearchCV with separate test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

param_grid = {'max_depth': [3, 5, 10]}
grid = GridSearchCV(DecisionTreeClassifier(), param_grid, cv=5)
grid.fit(X_train, y_train)

print(f"Best params: {grid.best_params_}")
print(f"CV score: {grid.best_score_}")  # Tuned on train CV
print(f"Test score: {grid.score(X_test, y_test)}")  # Unbiased estimate

# Method 2: Nested cross-validation (advanced)
from sklearn.model_selection import cross_val_score

scores = cross_val_score(grid, X, y, cv=5)  # Outer CV
print(f"Nested CV score: {scores.mean():.3f}")  # Unbiased!
```

---

### Mistake 4: Using Wrong CV for Time Series

**WRONG:**

```python
# ❌ Regular K-Fold on time series
scores = cross_val_score(model, X_timeseries, y_timeseries, cv=5)
# Trains on future to predict past!
```

**CORRECT:**

```python
# ✓ TimeSeriesSplit
from sklearn.model_selection import TimeSeriesSplit

tscv = TimeSeriesSplit(n_splits=5)
scores = cross_val_score(model, X_timeseries, y_timeseries, cv=tscv)
```

---

### Mistake 5: Ignoring Standard Deviation

**WRONG:**

```python
Model A: mean = 0.87
Model B: mean = 0.85

# "Model A is better!" ← Not necessarily!
```

**CORRECT:**

```python
Model A: 0.87 ± 0.12  (unstable!)
Model B: 0.85 ± 0.02  (stable)

# Model B might be better - more consistent performance
```

---

## Advanced Techniques

### Nested Cross-Validation

**Purpose:** Get unbiased performance estimate when tuning hyperparameters

**Structure:**
- **Outer loop:** Estimates model performance (5-fold CV)
- **Inner loop:** Tunes hyperparameters (5-fold CV)
- Total: 5 × 5 = 25 model trainings

```python
from sklearn.model_selection import GridSearchCV, cross_val_score

# Define model with hyperparameter search
param_grid = {'max_depth': [3, 5, 10], 'n_estimators': [50, 100]}
inner_cv = GridSearchCV(RandomForestClassifier(), param_grid, cv=5)

# Outer CV for unbiased performance estimate
outer_scores = cross_val_score(inner_cv, X, y, cv=5)

print(f"Nested CV score: {outer_scores.mean():.3f} ± {outer_scores.std():.3f}")
# This is an unbiased estimate of true performance!
```

**When to use:**
- When reporting model performance AND tuning hyperparameters
- Academic papers, research
- When you need rigorous evaluation

**Computational cost:** High (outer_cv × inner_cv model trainings)

---

### Stratified Group K-Fold

**Combines stratification AND grouping**

```python
from sklearn.model_selection import StratifiedGroupKFold

# For classification with groups and class imbalance
sgkf = StratifiedGroupKFold(n_splits=5)

scores = cross_val_score(model, X, y, cv=sgkf, groups=groups)
```

**When to use:**
- Classification + grouped data + imbalanced classes
- Example: Medical diagnosis with multiple measurements per patient and rare disease

---

### Cross-Validation with Pipelines and GridSearchCV

**Complete workflow:**

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

# Build pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', RandomForestClassifier())
])

# Define parameter grid (note: use 'step__param' syntax)
param_grid = {
    'classifier__max_depth': [10, 20, 30],
    'classifier__n_estimators': [100, 200],
    'classifier__min_samples_split': [2, 5]
}

# GridSearch with CV
grid = GridSearchCV(pipeline, param_grid, cv=5, n_jobs=-1, verbose=1)
grid.fit(X_train, y_train)

print(f"Best params: {grid.best_params_}")
print(f"Best CV score: {grid.best_score_:.3f}")
print(f"Test score: {grid.score(X_test, y_test):.3f}")
```

**This is the gold standard for production ML!**

---

## When NOT to Use Cross-Validation

### 1. Very Large Datasets

If N > 100,000, single train/test split might be sufficient (variance is low)

```python
# For large datasets, simple split is often enough
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model.fit(X_train, y_train)
test_score = model.score(X_test, y_test)
```

**Reason:** With 80,000 training samples, variance in performance estimate is already very low

---

### 2. Extremely Expensive Models

Deep learning, very large ensemble models → training once is already slow

**Alternative:** Use validation set instead of CV

```python
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5)

# Train: 70%, Validation: 15%, Test: 15%
```

---

### 3. When You Have Explicit Time Series Validation Needs

For deployment prediction, use walk-forward validation instead

```python
# Walk-forward validation (closer to production)
train_end = 0.8 * len(X)
X_train, y_train = X[:train_end], y[:train_end]
X_test, y_test = X[train_end:], y[train_end:]
```

---

### 4. Data Leakage Concerns

If preprocessing is complex and you're not confident about Pipeline, single split might be safer (for learning)

---

## Complete Code Examples

### Example 1: Basic Classification

```python
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, StratifiedKFold

# Load data
X, y = load_breast_cancer(return_X_y=True)

# Define model
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Cross-validate with stratification
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=cv, scoring='accuracy')

print(f"Accuracy: {scores.mean():.3f} ± {scores.std():.3f}")
print(f"Individual fold scores: {scores}")
```

---

### Example 2: Regression with Multiple Metrics

```python
from sklearn.datasets import load_diabetes
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import cross_validate
import numpy as np

# Load data
X, y = load_diabetes(return_X_y=True)

# Define model
model = GradientBoostingRegressor(n_estimators=100, random_state=42)

# Cross-validate with multiple metrics
results = cross_validate(
    model, X, y, cv=5,
    scoring=['r2', 'neg_mean_squared_error', 'neg_mean_absolute_error'],
    return_train_score=True
)

print(f"R²: {results['test_r2'].mean():.3f} ± {results['test_r2'].std():.3f}")

rmse = np.sqrt(-results['test_neg_mean_squared_error'])
print(f"RMSE: {rmse.mean():.3f} ± {rmse.std():.3f}")

mae = -results['test_neg_mean_absolute_error']
print(f"MAE: {mae.mean():.3f} ± {mae.std():.3f}")
```

---

### Example 3: Complete Pipeline with GridSearchCV

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline

# Load data
X, y = load_iris(return_X_y=True)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Build pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('svm', SVC())
])

# Define parameter grid
param_grid = {
    'svm__C': [0.1, 1, 10],
    'svm__kernel': ['linear', 'rbf'],
    'svm__gamma': ['scale', 'auto']
}

# GridSearch with CV
grid = GridSearchCV(
    pipeline, param_grid, cv=5, scoring='accuracy', n_jobs=-1, verbose=1
)

# Fit
grid.fit(X_train, y_train)

# Results
print(f"Best parameters: {grid.best_params_}")
print(f"Best CV accuracy: {grid.best_score_:.3f}")
print(f"Test accuracy: {grid.score(X_test, y_test):.3f}")

# Detailed results
import pandas as pd
results_df = pd.DataFrame(grid.cv_results_)
print(results_df[['params', 'mean_test_score', 'std_test_score']].head(10))
```

---

### Example 4: Time Series Cross-Validation

```python
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.model_selection import TimeSeriesSplit, cross_val_score

# Generate time series data
n_samples = 1000
X = np.arange(n_samples).reshape(-1, 1)
y = np.sin(X.ravel() / 50) + np.random.randn(n_samples) * 0.1

# Time series CV
tscv = TimeSeriesSplit(n_splits=5)

# Visualize splits
for i, (train_idx, test_idx) in enumerate(tscv.split(X)):
    print(f"Fold {i+1}:")
    print(f"  Train: {train_idx[0]} to {train_idx[-1]} ({len(train_idx)} samples)")
    print(f"  Test:  {test_idx[0]} to {test_idx[-1]} ({len(test_idx)} samples)")

# Evaluate
model = Ridge()
scores = cross_val_score(model, X, y, cv=tscv, scoring='r2')
print(f"\nR²: {scores.mean():.3f} ± {scores.std():.3f}")
```

---

### Example 5: Nested Cross-Validation

```python
from sklearn.datasets import load_digits
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, cross_val_score

# Load data
X, y = load_digits(return_X_y=True)

# Inner CV: hyperparameter tuning
param_grid = {
    'max_depth': [10, 20, 30],
    'n_estimators': [50, 100, 200]
}

inner_cv = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    cv=3,  # 3-fold for inner (faster)
    scoring='accuracy'
)

# Outer CV: performance estimation
outer_scores = cross_val_score(inner_cv, X, y, cv=5, scoring='accuracy')

print(f"Nested CV accuracy: {outer_scores.mean():.3f} ± {outer_scores.std():.3f}")
print(f"Individual outer fold scores: {outer_scores}")
```

**Interpretation:** This 0.XXX ± 0.XXX is an unbiased estimate of how the model + hyperparameter tuning procedure will perform on unseen data.

---

## Quick Reference Table

| CV Type | Use Case | Parameters | Code |
|---------|----------|------------|------|
| **K-Fold** | General purpose | `n_splits=5` | `KFold(n_splits=5, shuffle=True)` |
| **Stratified K-Fold** | Imbalanced classification | `n_splits=5` | `StratifiedKFold(n_splits=5, shuffle=True)` |
| **LOOCV** | Very small datasets | None (K=N) | `LeaveOneOut()` |
| **Time Series** | Temporal data | `n_splits=5` | `TimeSeriesSplit(n_splits=5)` |
| **Group K-Fold** | Grouped data | `n_splits=5` | `GroupKFold(n_splits=5)` |
| **Stratified Group** | Groups + imbalance | `n_splits=5` | `StratifiedGroupKFold(n_splits=5)` |

---

## Summary

**Cross-validation is the industry-standard approach for:**
1. Evaluating model performance reliably
2. Detecting overfitting
3. Comparing models
4. Tuning hyperparameters

**Key principles:**
- Use **K=5** as default
- Use **StratifiedKFold** for classification
- Use **TimeSeriesSplit** for time series
- Always use **Pipeline** to prevent data leakage
- Report both **mean and std** of scores
- For hyperparameter tuning, use **GridSearchCV** or **nested CV**

**Remember:** Cross-validation gives you confidence in your model's generalization ability! 📊
