# Week 3 sklearn Cheat Sheet - Trees & Ensembles

**Quick reference for Decision Trees, Random Forests, and XGBoost**

---

## Decision Tree Classifier

### Basic Usage

```python
from sklearn.tree import DecisionTreeClassifier

# Create model
dt = DecisionTreeClassifier(
    max_depth=5,              # Limit depth to prevent overfitting
    min_samples_split=20,     # Minimum samples to split a node
    min_samples_leaf=10,      # Minimum samples in leaf node
    random_state=42           # Reproducibility
)

# Train
dt.fit(X_train, y_train)

# Predict
y_pred = dt.predict(X_test)
y_pred_proba = dt.predict_proba(X_test)  # Probability scores

# Evaluate
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, y_pred)
```

---

### Key Hyperparameters

| Parameter | Default | Typical Values | Purpose |
|-----------|---------|----------------|---------|
| `max_depth` | None | 3-10 | Limit tree depth (prevent overfitting) |
| `min_samples_split` | 2 | 10-100 | Min samples to split internal node |
| `min_samples_leaf` | 1 | 5-50 | Min samples in leaf node |
| `criterion` | 'gini' | 'gini', 'entropy' | Impurity measure |
| `random_state` | None | 42 | Reproducibility |

**Common patterns:**
- **Prevent overfitting:** `max_depth=5, min_samples_split=20`
- **Quick baseline:** `DecisionTreeClassifier()` (defaults)
- **Interpretable:** `max_depth=3` (very shallow, easy to visualize)

---

### Feature Importance

```python
# Get feature importance
importance = dt.feature_importances_  # Array of values (sum to 1.0)

# Visualize
import pandas as pd
import matplotlib.pyplot as plt

feature_importance_df = pd.DataFrame({
    'Feature': feature_names,
    'Importance': importance
}).sort_values('Importance', ascending=False)

plt.barh(feature_importance_df['Feature'], feature_importance_df['Importance'])
plt.xlabel('Importance')
plt.title('Feature Importance')
plt.show()
```

---

### Tree Visualization

```python
from sklearn import tree

# Method 1: Plot tree (requires graphviz)
plt.figure(figsize=(20, 10))
tree.plot_tree(dt,
               feature_names=feature_names,
               class_names=['Class 0', 'Class 1'],
               filled=True,
               fontsize=10)
plt.show()

# Method 2: Text representation (no graphviz needed)
text_representation = tree.export_text(dt, feature_names=feature_names)
print(text_representation)
```

---

## Random Forest Classifier

### Basic Usage

```python
from sklearn.ensemble import RandomForestClassifier

# Create model
rf = RandomForestClassifier(
    n_estimators=100,         # Number of trees
    max_depth=5,              # Depth of each tree
    min_samples_split=20,     # Min samples to split
    max_features='sqrt',      # Features to consider per split
    oob_score=True,           # Out-of-bag validation
    random_state=42,
    n_jobs=-1                 # Use all CPU cores
)

# Train
rf.fit(X_train, y_train)

# Predict
y_pred = rf.predict(X_test)
y_pred_proba = rf.predict_proba(X_test)

# Evaluate
accuracy = accuracy_score(y_test, y_pred)
oob_accuracy = rf.oob_score_  # Out-of-bag validation score
```

---

### Key Hyperparameters

| Parameter | Default | Typical Values | Purpose |
|-----------|---------|----------------|---------|
| `n_estimators` | 100 | 100-500 | Number of trees in forest |
| `max_depth` | None | 5-20 | Depth of each tree |
| `max_features` | 'sqrt' | 'sqrt', 'log2', None | Features per split |
| `min_samples_split` | 2 | 10-100 | Min samples to split |
| `oob_score` | False | True/False | Use out-of-bag validation |
| `n_jobs` | 1 | -1 | Parallel processing (−1 = all cores) |
| `random_state` | None | 42 | Reproducibility |

**Common patterns:**
- **Good default:** `RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)`
- **Prevent overfitting:** `max_depth=10, min_samples_split=50`
- **Fast training:** `n_estimators=50, n_jobs=-1`
- **Maximum performance:** `n_estimators=500, max_depth=20`

---

### Feature Importance

```python
# Same as Decision Tree
importance = rf.feature_importances_

# Often more stable than single tree importance
# (averaged across 100+ trees)
```

---

### Out-of-Bag (OOB) Validation

```python
# Enable OOB scoring
rf = RandomForestClassifier(n_estimators=100, oob_score=True, random_state=42)
rf.fit(X_train, y_train)

# Get OOB score (no need for separate validation set!)
print(f"OOB Score: {rf.oob_score_:.3f}")

# Compare to test score
test_accuracy = accuracy_score(y_test, rf.predict(X_test))
print(f"Test Accuracy: {test_accuracy:.3f}")
```

---

## XGBoost Classifier

### Installation

```bash
# Install XGBoost (not included in sklearn)
pip install xgboost

# Or with conda
conda install -c conda-forge xgboost
```

---

### Basic Usage

```python
import xgboost as xgb

# Create model
xgb_model = xgb.XGBClassifier(
    n_estimators=100,         # Number of boosting rounds
    max_depth=3,              # Shallower than Random Forest!
    learning_rate=0.1,        # Step size (eta)
    subsample=0.8,            # Fraction of samples per tree
    colsample_bytree=0.8,     # Fraction of features per tree
    random_state=42,
    n_jobs=-1                 # Use all CPU cores
)

# Train
xgb_model.fit(X_train, y_train)

# Predict
y_pred = xgb_model.predict(X_test)
y_pred_proba = xgb_model.predict_proba(X_test)

# Evaluate
accuracy = accuracy_score(y_test, y_pred)
```

---

### Key Hyperparameters

| Parameter | Default | Typical Values | Purpose |
|-----------|---------|----------------|---------|
| `n_estimators` | 100 | 100-1000 | Number of boosting rounds |
| `max_depth` | 6 | 3-10 | Max tree depth (use shallower than RF!) |
| `learning_rate` (eta) | 0.3 | 0.01-0.3 | Step size for boosting |
| `subsample` | 1.0 | 0.6-1.0 | Fraction of samples per tree |
| `colsample_bytree` | 1.0 | 0.6-1.0 | Fraction of features per tree |
| `gamma` | 0 | 0-5 | Min loss reduction for split |
| `reg_alpha` | 0 | 0-1 | L1 regularization |
| `reg_lambda` | 1 | 0-10 | L2 regularization |
| `random_state` | 0 | 42 | Reproducibility |

**Common patterns:**
- **Good default:** `XGBClassifier(n_estimators=100, max_depth=3, learning_rate=0.1, random_state=42)`
- **Prevent overfitting:** `max_depth=3, learning_rate=0.05, subsample=0.8, colsample_bytree=0.8`
- **Maximum performance:** `n_estimators=500, max_depth=6, learning_rate=0.1, early stopping`
- **Fast training:** `n_estimators=50, max_depth=3, learning_rate=0.2`

---

### Early Stopping

```python
# Split training data for early stopping
X_train_split, X_val, y_train_split, y_val = train_test_split(
    X_train, y_train, test_size=0.2, random_state=42
)

# Train with early stopping
xgb_model = xgb.XGBClassifier(
    n_estimators=1000,  # Set high, early stopping will stop sooner
    max_depth=3,
    learning_rate=0.1,
    random_state=42
)

xgb_model.fit(
    X_train_split, y_train_split,
    early_stopping_rounds=10,  # Stop if no improvement for 10 rounds
    eval_set=[(X_val, y_val)],  # Validation set
    verbose=False  # Suppress output
)

# Get best iteration
print(f"Best iteration: {xgb_model.best_iteration}")
print(f"Best score: {xgb_model.best_score}")
```

---

### Feature Importance (XGBoost-specific)

```python
# Method 1: Weight-based (default)
importance = xgb_model.feature_importances_

# Method 2: Gain-based (recommended)
importance_gain = xgb_model.get_booster().get_score(importance_type='gain')

# Method 3: Built-in plot
xgb.plot_importance(xgb_model, max_num_features=10)
plt.show()
```

---

## Systematic Algorithm Comparison Workflow

### Step 1: Train All Models on Same Data

```python
from sklearn.model_selection import train_test_split

# Single train/test split for fair comparison
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Decision Tree
dt = DecisionTreeClassifier(max_depth=5, random_state=42)
dt.fit(X_train, y_train)

# Train Random Forest
rf = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
rf.fit(X_train, y_train)

# Train XGBoost
xgb_model = xgb.XGBClassifier(n_estimators=100, max_depth=3, learning_rate=0.1, random_state=42)
xgb_model.fit(X_train, y_train)
```

---

### Step 2: Calculate Metrics for Each

```python
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Decision Tree metrics
y_pred_dt = dt.predict(X_test)
dt_accuracy = accuracy_score(y_test, y_pred_dt)
dt_precision = precision_score(y_test, y_pred_dt)
dt_recall = recall_score(y_test, y_pred_dt)
dt_f1 = f1_score(y_test, y_pred_dt)

# Random Forest metrics
y_pred_rf = rf.predict(X_test)
rf_accuracy = accuracy_score(y_test, y_pred_rf)
rf_precision = precision_score(y_test, y_pred_rf)
rf_recall = recall_score(y_test, y_pred_rf)
rf_f1 = f1_score(y_test, y_pred_rf)

# XGBoost metrics
y_pred_xgb = xgb_model.predict(X_test)
xgb_accuracy = accuracy_score(y_test, y_pred_xgb)
xgb_precision = precision_score(y_test, y_pred_xgb)
xgb_recall = recall_score(y_test, y_pred_xgb)
xgb_f1 = f1_score(y_test, y_pred_xgb)
```

---

### Step 3: Create Comparison Table

```python
import pandas as pd

comparison_df = pd.DataFrame({
    'Algorithm': ['Decision Tree', 'Random Forest', 'XGBoost'],
    'Accuracy': [dt_accuracy, rf_accuracy, xgb_accuracy],
    'Precision': [dt_precision, rf_precision, xgb_precision],
    'Recall': [dt_recall, rf_recall, xgb_recall],
    'F1-Score': [dt_f1, rf_f1, xgb_f1]
})

print(comparison_df.to_string(index=False))
```

---

### Step 4: Compare Feature Importance

```python
# Extract importance from all three
dt_importance = dt.feature_importances_
rf_importance = rf.feature_importances_
xgb_importance = xgb_model.feature_importances_

# Create comparison DataFrame
importance_df = pd.DataFrame({
    'Feature': feature_names,
    'Decision Tree': dt_importance,
    'Random Forest': rf_importance,
    'XGBoost': xgb_importance
})

# Sort and display top 10
importance_df = importance_df.sort_values('Random Forest', ascending=False)
print(importance_df.head(10))

# Visualize
fig, ax = plt.subplots(figsize=(10, 6))
x = range(len(importance_df.head(10)))
width = 0.25

ax.bar([i - width for i in x], importance_df.head(10)['Decision Tree'],
       width, label='Decision Tree', alpha=0.8)
ax.bar(x, importance_df.head(10)['Random Forest'],
       width, label='Random Forest', alpha=0.8)
ax.bar([i + width for i in x], importance_df.head(10)['XGBoost'],
       width, label='XGBoost', alpha=0.8)

ax.set_xticks(x)
ax.set_xticklabels(importance_df.head(10)['Feature'], rotation=45, ha='right')
ax.set_ylabel('Importance')
ax.set_title('Top 10 Features: Importance Comparison')
ax.legend()
plt.tight_layout()
plt.show()
```

---

## Common Issues & Solutions

### XGBoost Installation Fails

**Problem:** `pip install xgboost` fails with compiler errors

**Solutions:**
1. Try conda: `conda install -c conda-forge xgboost`
2. Use sklearn's GradientBoostingClassifier instead (slower but similar)
3. On Windows: Install Visual C++ Build Tools

---

### Tree Visualization Doesn't Work

**Problem:** `plot_tree()` produces blank plot or error

**Solutions:**
1. Install graphviz: `pip install graphviz` or `conda install graphviz`
2. Use text representation: `tree.export_text(dt)`
3. Reduce `max_depth` (deep trees are unreadable anyway)

---

### Models Take Too Long to Train

**Problem:** Training is very slow

**Solutions:**
1. Use `n_jobs=-1` (Random Forest, XGBoost)
2. Reduce `n_estimators` (100 is usually enough)
3. Reduce `max_depth`
4. Subsample data for initial experiments

---

### Different Results Each Time

**Problem:** Results vary between runs

**Solutions:**
1. Always set `random_state=42` in ALL models
2. Set `random_state` in `train_test_split()`
3. For XGBoost, also set `random_state` parameter

---

## Algorithm Selection Guide

### Decision Tree
**Use when:** Interpretability critical, need to visualize model
**Don't use when:** Need maximum accuracy

### Random Forest
**Use when:** Want robust baseline, good all-around performance
**Don't use when:** Memory/speed critical (uses 100x memory of single tree)

### XGBoost
**Use when:** Need maximum accuracy, have time to tune
**Don't use when:** Need interpretability, or XGBoost won't install

---

## Quick Reference Table

| Task | Decision Tree | Random Forest | XGBoost |
|------|--------------|---------------|---------|
| **Training Speed** | Fast | Medium | Slow |
| **Prediction Speed** | Fast | Medium | Fast |
| **Accuracy** | Medium | High | Very High |
| **Interpretability** | High | Medium | Low |
| **Overfitting Risk** | High | Low | Medium |
| **Memory Usage** | Low | High | Medium |
| **Hyperparameter Tuning** | Easy | Easy | Complex |

---

**Pro tip:** Start with Random Forest as your default. It works well out-of-the-box with minimal tuning. Switch to XGBoost if you need 1-2% better accuracy and have time to tune hyperparameters.

---

*Last Updated: 2026-01-24*
