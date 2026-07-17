# Appendix C: Complete Tree & Ensemble Methods Guide

**Purpose:** Comprehensive reference for decision trees, Random Forests, and XGBoost

**When to use:** Reference this guide when working with tree-based algorithms in projects or homework

---

## Table of Contents

1. [Decision Trees](#decision-trees)
2. [Random Forests](#random-forests)
3. [XGBoost (Gradient Boosting)](#xgboost-gradient-boosting)
4. [Algorithm Selection Guide](#algorithm-selection-guide)
5. [Feature Importance](#feature-importance)
6. [Common Pitfalls & Best Practices](#common-pitfalls--best-practices)
7. [Hyperparameter Tuning Reference](#hyperparameter-tuning-reference)
8. [Quick Code Templates](#quick-code-templates)

---

## Decision Trees

### What Are Decision Trees?

Decision trees are supervised learning algorithms that make predictions by asking a series of binary (yes/no) questions about features. Think of them like playing "20 Questions" - each question splits the data into two groups until you reach a final prediction.

### How They Work

**The Tree Structure:**
```
                   Root Node
               [All Training Data]
                      |
          Question: Feature A > threshold?
             /                    \
           Yes                    No
          /                        \
     Left Subtree              Right Subtree
    [Subset of data]          [Subset of data]
          |                        |
    Next question...          Next question...
          |                        |
          ▼                        ▼
    Leaf (Prediction)        Leaf (Prediction)
```

**Training Process:**

1. **Start at root:** All training data is at the top
2. **Choose best split:** Find the feature and threshold that best separates classes
   - For each feature, try all possible thresholds
   - Calculate information gain (or Gini impurity reduction)
   - Choose split with highest information gain
3. **Create branches:** Divide data into left (yes) and right (no) groups
4. **Repeat recursively:** For each group, find the next best split
5. **Stop when:** Groups are pure (all same class) OR max_depth reached OR min_samples met
6. **Create leaves:** Final nodes contain predictions (majority class for classification, mean for regression)

**Prediction Process:**

1. Start at root with new example
2. Answer the question (feature > threshold?)
3. Go left or right based on answer
4. Continue until reaching a leaf
5. Return the leaf's prediction

### Pros and Cons

**Advantages:**
- ✅ **Highly interpretable** - Can visualize and explain exact decision path
- ✅ **No feature scaling needed** - Works with raw data
- ✅ **Handles mixed data types** - Numeric and categorical features
- ✅ **Non-linear relationships** - Can capture complex patterns
- ✅ **Fast training and prediction**
- ✅ **Feature importance built-in**

**Disadvantages:**
- ❌ **Prone to overfitting** - Especially with deep trees
- ❌ **High variance** - Small data changes → very different trees
- ❌ **Lower accuracy** - Compared to ensemble methods
- ❌ **Biased to dominant classes** - In imbalanced datasets
- ❌ **Axis-aligned splits** - Can't capture diagonal boundaries well

### Key Hyperparameters

| Parameter | Description | Default | Typical Range | Effect |
|-----------|-------------|---------|---------------|--------|
| **max_depth** | Maximum tree depth | None (unlimited) | 3-10 | Higher = more complex, more overfitting |
| **min_samples_split** | Min samples to split a node | 2 | 2-20 | Higher = simpler tree, less overfitting |
| **min_samples_leaf** | Min samples in leaf node | 1 | 1-10 | Higher = smoother predictions |
| **criterion** | Split quality measure | 'gini' | 'gini', 'entropy' | Usually doesn't matter much |
| **max_features** | Features to consider per split | All | 'sqrt', 'log2', int | Lower = more diverse trees |

**Most Important:** `max_depth` - Controls overfitting more than anything else

### When to Use Decision Trees

**Use Decision Trees when:**
- ✅ You need to **explain predictions** to non-technical stakeholders
- ✅ You need a **quick baseline** (fast to train)
- ✅ **Interpretability is critical** (e.g., medical diagnosis, loan approval)
- ✅ You have **small datasets** where ensemble methods might overfit

**Don't use Decision Trees when:**
- ❌ You need **maximum predictive performance** (use ensembles instead)
- ❌ You have **very high-dimensional data** (use neural networks)
- ❌ You need **smooth probability estimates** (use logistic regression)

### Code Example: Classification

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Load and split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train model
tree = DecisionTreeClassifier(
    max_depth=5,           # Prevent overfitting
    min_samples_split=10,  # Require at least 10 samples to split
    criterion='gini',      # Default split criterion
    random_state=42
)

tree.fit(X_train, y_train)

# Make predictions
y_pred = tree.predict(X_test)

# Evaluate
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.3f}")
print(classification_report(y_test, y_pred))

# Visualize tree (optional)
from sklearn import tree
import matplotlib.pyplot as plt

plt.figure(figsize=(20, 10))
tree.plot_tree(tree, filled=True, feature_names=feature_names, class_names=class_names)
plt.show()
```

### Code Example: Regression

```python
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Create and train model
tree_reg = DecisionTreeRegressor(
    max_depth=5,
    min_samples_leaf=5,
    random_state=42
)

tree_reg.fit(X_train, y_train)

# Predict
y_pred = tree_reg.predict(X_test)

# Evaluate
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f"RMSE: {rmse:.3f}")
print(f"R²: {r2:.3f}")
```

---

## Random Forests

### What Are Random Forests?

Random Forests are **ensemble methods** that combine multiple decision trees to make better predictions. Instead of asking one expert (one tree), you ask 100 experts (100 trees) and take a vote.

### How They Work

**The "Committee Decision" Approach:**

1. **Bootstrap sampling:** Create N random samples of training data (with replacement)
   - Each sample is ~63% of original data
   - Some examples appear multiple times, some don't appear at all
2. **Train N trees:** Each tree trained on its own bootstrap sample
   - Trees trained independently in parallel
   - Each tree also uses random subset of features at each split
3. **Aggregate predictions:**
   - **Classification:** Majority vote (most popular class wins)
   - **Regression:** Average all predictions

**Why This Works (Variance Reduction):**

- Individual trees are high variance (small data changes → different trees)
- Different trees make different mistakes (because they saw different data)
- When averaging, errors cancel out
- Result: More stable and accurate than single tree

**Example:**
```
Tree 1 sees sample [1, 1, 3, 5, 5] → predicts Class A
Tree 2 sees sample [2, 2, 3, 4, 4] → predicts Class A
Tree 3 sees sample [1, 2, 2, 3, 5] → predicts Class B
Tree 4 sees sample [1, 3, 4, 5, 5] → predicts Class A
... 96 more trees ...

Final vote: 73 trees say Class A, 27 say Class B
Prediction: Class A (majority wins)
```

### Pros and Cons

**Advantages:**
- ✅ **Higher accuracy** than single trees
- ✅ **Reduced overfitting** (averaging smooths out errors)
- ✅ **Robust to outliers** (averaged across many trees)
- ✅ **Works well out-of-the-box** (default parameters often good)
- ✅ **Handles missing values** (can use surrogate splits)
- ✅ **Parallel training** (fast on multi-core machines)
- ✅ **Feature importance** still available

**Disadvantages:**
- ❌ **Less interpretable** than single tree (can't visualize 100 trees)
- ❌ **Slower prediction** (must run through all trees)
- ❌ **Larger model size** (storing 100 trees vs 1)
- ❌ **Slightly slower than XGBoost** in some cases

### Key Hyperparameters

| Parameter | Description | Default | Typical Range | Effect |
|-----------|-------------|---------|---------------|--------|
| **n_estimators** | Number of trees | 100 | 100-500 | More = better, but diminishing returns |
| **max_depth** | Depth of each tree | None | 5-15 | Higher = more complex trees |
| **min_samples_split** | Min samples to split | 2 | 2-20 | Higher = simpler trees |
| **max_features** | Features per split | 'sqrt' | 'sqrt', 'log2' | Lower = more diversity |
| **bootstrap** | Use bootstrap samples? | True | True | Should stay True |
| **oob_score** | Use out-of-bag score? | False | True/False | True = free validation score |

**Most Important:** `n_estimators` (more trees = better, usually), `max_depth` (controls tree complexity)

### When to Use Random Forests

**Use Random Forests when:**
- ✅ You want a **robust default** algorithm (works well on most problems)
- ✅ You need **good performance without much tuning**
- ✅ You have **tabular/structured data** (rows and columns)
- ✅ You want **some interpretability** (via feature importance)
- ✅ You need **fast training** (parallel trees)

**Don't use Random Forests when:**
- ❌ You need **perfect interpretability** (use single decision tree)
- ❌ You need **absolute maximum accuracy** (try XGBoost)
- ❌ You have **very large datasets** (XGBoost might be faster)
- ❌ You have **high-dimensional sparse data** (neural networks better)

### Code Example: Classification

```python
from sklearn.ensemble import RandomForestClassifier

# Create model
rf = RandomForestClassifier(
    n_estimators=100,      # 100 trees in the forest
    max_depth=10,          # Each tree max depth 10
    min_samples_split=5,   # Need 5 samples to split
    max_features='sqrt',   # Use sqrt(n_features) per split
    bootstrap=True,        # Use bootstrap sampling
    oob_score=True,        # Calculate out-of-bag score
    n_jobs=-1,             # Use all CPU cores
    random_state=42
)

# Train
rf.fit(X_train, y_train)

# Predict
y_pred = rf.predict(X_test)
y_prob = rf.predict_proba(X_test)  # Get probabilities

# Evaluate
from sklearn.metrics import accuracy_score, classification_report
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.3f}")
print(f"OOB Score: {rf.oob_score_:.3f}")  # Free validation score!
print(classification_report(y_test, y_pred))

# Feature importance
importances = rf.feature_importances_
for feature, importance in zip(feature_names, importances):
    print(f"{feature}: {importance:.3f}")
```

### Code Example: Regression

```python
from sklearn.ensemble import RandomForestRegressor

# Create model
rf_reg = RandomForestRegressor(
    n_estimators=200,
    max_depth=15,
    min_samples_leaf=3,
    n_jobs=-1,
    random_state=42
)

# Train
rf_reg.fit(X_train, y_train)

# Predict
y_pred = rf_reg.predict(X_test)

# Evaluate
from sklearn.metrics import mean_squared_error, r2_score
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"RMSE: {np.sqrt(mse):.3f}")
print(f"R²: {r2:.3f}")
```

---

## XGBoost (Gradient Boosting)

### What Is XGBoost?

XGBoost (Extreme Gradient Boosting) is an advanced ensemble method that trains trees **sequentially**, where each new tree focuses on fixing the mistakes of previous trees. Think of it as "learning from mistakes" - Tree 1 tries, Tree 2 fixes Tree 1's errors, Tree 3 fixes Tree 2's errors, and so on.

### How It Works

**The "Learning from Mistakes" Approach:**

1. **Train Tree 1:**
   - Make predictions on all training data
   - Calculate errors (residuals = actual - predicted)
   - Some examples predicted correctly, some not

2. **Train Tree 2:**
   - Focus on examples Tree 1 got wrong
   - Train new tree to predict the **residuals** (errors)
   - Add Tree 2's predictions to Tree 1 (weighted by learning_rate)

3. **Train Tree 3:**
   - Calculate new errors (after Tree 1 + Tree 2)
   - Train Tree 3 to fix these new errors
   - Add Tree 3 to the ensemble

4. **Repeat for N trees:**
   - Each tree corrects previous ensemble's mistakes
   - Final prediction = sum of all trees (weighted)

**Example:**
```
Data point actual value: 10

Tree 1 predicts: 6 (error = +4, too low)
Tree 2 learns to predict: +3 (fixes most of error)
Ensemble after Tree 2: 6 + (0.1 × 3) = 6.3

Tree 3 learns to predict: +2 (fixes remaining error)
Ensemble after Tree 3: 6.3 + (0.1 × 2) = 6.5

... 100 trees later ...
Final prediction: 9.8 (very close to actual 10!)
```

### Gradient Boosting Explained (Simplified)

**What are "gradients"?**

Gradients (from calculus) tell you the direction and amount to change predictions to reduce error. Think of them as "smart error signals" that guide each new tree.

- Traditional boosting: `residual = actual - predicted` (simple subtraction)
- Gradient boosting: Uses calculus to compute optimal direction to improve

**You don't need to know the math** - just understand that gradients make the error correction more efficient.

### Pros and Cons

**Advantages:**
- ✅ **Highest accuracy** (often wins Kaggle competitions)
- ✅ **Handles missing values** automatically
- ✅ **Built-in regularization** (prevents overfitting)
- ✅ **Feature importance** available
- ✅ **Flexible** (many loss functions supported)
- ✅ **Efficient** (optimized C++ implementation)

**Disadvantages:**
- ❌ **Slower training** (sequential trees, can't parallelize fully)
- ❌ **More hyperparameters** to tune
- ❌ **Can overfit** if not careful (need to tune learning_rate, n_estimators)
- ❌ **Less interpretable** than single tree or Random Forest
- ❌ **Requires more expertise** to use well

### Key Hyperparameters

| Parameter | Description | Default | Typical Range | Effect |
|-----------|-------------|---------|---------------|--------|
| **n_estimators** | Number of boosting rounds | 100 | 100-1000 | More = better, but can overfit |
| **learning_rate** | Step size (eta) | 0.3 | 0.01-0.3 | Lower = slower learning, more trees needed |
| **max_depth** | Max tree depth | 6 | 3-10 | Lower than Random Forest (3-5 typical) |
| **min_child_weight** | Min sum of weights in child | 1 | 1-10 | Higher = more conservative |
| **subsample** | Fraction of samples per tree | 1 | 0.5-1.0 | Lower = more regularization |
| **colsample_bytree** | Fraction of features per tree | 1 | 0.5-1.0 | Lower = more diversity |
| **gamma** | Min loss reduction to split | 0 | 0-5 | Higher = more conservative |
| **reg_alpha** | L1 regularization | 0 | 0-1 | Higher = sparser models |
| **reg_lambda** | L2 regularization | 1 | 0-10 | Higher = smoother models |

**Most Important:** `learning_rate` and `n_estimators` (inversely related), `max_depth`

**Typical Combinations:**
- **Fast training:** `learning_rate=0.3, n_estimators=100, max_depth=6`
- **Balanced:** `learning_rate=0.1, n_estimators=200, max_depth=5`
- **Best accuracy:** `learning_rate=0.01, n_estimators=1000, max_depth=3`

### When to Use XGBoost

**Use XGBoost when:**
- ✅ You need **maximum predictive accuracy**
- ✅ You have **tabular/structured data**
- ✅ You have **time to tune hyperparameters**
- ✅ You're in a **Kaggle competition** or production system
- ✅ You don't need to explain individual predictions

**Don't use XGBoost when:**
- ❌ You need **perfect interpretability** (use decision tree)
- ❌ You want **fast experimentation** with minimal tuning (use Random Forest)
- ❌ You have **very small datasets** (<1000 examples)
- ❌ You have **images, text, or audio** (use neural networks)

### Code Example: Classification

```python
import xgboost as xgb
from sklearn.metrics import accuracy_score, classification_report

# Create model
xgb_clf = xgb.XGBClassifier(
    n_estimators=100,        # Number of boosting rounds
    max_depth=5,             # Shallower than Random Forest
    learning_rate=0.1,       # Step size (eta)
    subsample=0.8,           # Use 80% of data per tree
    colsample_bytree=0.8,    # Use 80% of features per tree
    gamma=0,                 # Min loss reduction
    reg_alpha=0,             # L1 regularization
    reg_lambda=1,            # L2 regularization
    random_state=42,
    n_jobs=-1                # Use all CPU cores
)

# Train with early stopping (optional but recommended)
xgb_clf.fit(
    X_train, y_train,
    eval_set=[(X_val, y_val)],           # Validation set
    early_stopping_rounds=10,            # Stop if no improvement for 10 rounds
    verbose=False                        # Don't print each iteration
)

# Predict
y_pred = xgb_clf.predict(X_test)
y_prob = xgb_clf.predict_proba(X_test)

# Evaluate
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.3f}")
print(f"Best iteration: {xgb_clf.best_iteration}")
print(classification_report(y_test, y_pred))

# Feature importance
importances = xgb_clf.feature_importances_
for feature, importance in zip(feature_names, importances):
    print(f"{feature}: {importance:.3f}")
```

### Code Example: Regression

```python
import xgboost as xgb
from sklearn.metrics import mean_squared_error, r2_score

# Create model
xgb_reg = xgb.XGBRegressor(
    n_estimators=500,
    max_depth=3,
    learning_rate=0.01,    # Low learning rate, more trees
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42,
    n_jobs=-1
)

# Train
xgb_reg.fit(
    X_train, y_train,
    eval_set=[(X_val, y_val)],
    early_stopping_rounds=20,
    verbose=False
)

# Predict
y_pred = xgb_reg.predict(X_test)

# Evaluate
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)
print(f"RMSE: {rmse:.3f}")
print(f"R²: {r2:.3f}")
```

---

## Algorithm Selection Guide

### Decision Flowchart

```
START: Need to solve a tabular ML problem

├─ Do you need to explain predictions to stakeholders?
│  │
│  ├─ YES → Use DECISION TREE
│  │         (Visualize tree, explain decision path)
│  │
│  └─ NO → Continue...
│
├─ Do you need maximum accuracy? Can you spend time tuning?
│  │
│  ├─ YES → Use XGBOOST
│  │         (Best accuracy, requires tuning)
│  │
│  └─ NO → Continue...
│
├─ Do you want a robust default with good performance?
│  │
│  ├─ YES → Use RANDOM FOREST
│  │         (Good out-of-the-box, minimal tuning)
│  │
│  └─ NO → You probably want Random Forest anyway!
│
END
```

### Comparison Table

| Criterion | Decision Tree | Random Forest | XGBoost |
|-----------|--------------|---------------|---------|
| **Accuracy** | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Training Speed** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Prediction Speed** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| **Interpretability** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| **Ease of Use** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Overfitting Risk** | ⭐⭐ (high) | ⭐⭐⭐⭐ (low) | ⭐⭐⭐ (medium) |
| **Hyperparameter Tuning** | ⭐⭐⭐⭐⭐ (easy) | ⭐⭐⭐⭐ (easy) | ⭐⭐ (hard) |

### Real-World Use Cases

**Decision Trees:**
- Medical diagnosis (need to explain to doctors)
- Loan approval (regulators require explainability)
- Initial exploration (quick baseline)

**Random Forests:**
- Fraud detection (balance accuracy and speed)
- Customer churn prediction (good default)
- Feature selection (identify important features)
- Most production systems (reliable and robust)

**XGBoost:**
- Kaggle competitions (maximize accuracy)
- Ad click prediction (slight improvements = big revenue)
- Risk modeling (when accuracy is critical)
- Recommendation systems (need best performance)

### Practical Workflow

**Step 1: Start with Random Forest**
- Train with default parameters
- Get baseline accuracy
- Extract feature importance

**Step 2: If accuracy not sufficient, try XGBoost**
- Use same train/test split
- Start with conservative parameters
- Tune learning_rate and n_estimators
- Compare to Random Forest

**Step 3: If interpretability needed, use Decision Tree**
- Set max_depth=5-7 to prevent overfitting
- Visualize tree structure
- Explain to stakeholders

**Step 4: Compare all three**
- Use same metrics (accuracy, precision, recall, F1)
- Consider business constraints (speed, interpretability, accuracy)
- Choose based on tradeoffs

---

## Feature Importance

### What Is Feature Importance?

Feature importance measures how much each feature contributes to the model's predictions. It answers: "Which features matter most for making predictions?"

### How It's Calculated (Tree Models)

**For Decision Trees and Random Forests:**
1. When a feature is used to split, calculate how much it improved purity (information gain)
2. Sum the improvements across all splits using that feature
3. Normalize so all importances sum to 1.0

**For XGBoost:**
- Similar to above, but weighted by gradient information
- Can use multiple importance types: 'weight', 'gain', 'cover'

### How to Extract and Use

```python
# After training any tree model
importances = model.feature_importances_

# Create DataFrame for easy viewing
import pandas as pd
importance_df = pd.DataFrame({
    'feature': feature_names,
    'importance': importances
}).sort_values('importance', ascending=False)

print(importance_df.head(10))  # Top 10 features

# Visualize
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
plt.barh(importance_df['feature'][:10], importance_df['importance'][:10])
plt.xlabel('Importance')
plt.title('Top 10 Most Important Features')
plt.gca().invert_yaxis()
plt.show()
```

### Interpretation Guide

**What high importance means:**
- ✅ Feature is frequently used for splits
- ✅ Feature improves model predictions
- ✅ Feature helps separate classes/predict target

**What high importance does NOT mean:**
- ❌ Feature CAUSES the outcome (correlation ≠ causation)
- ❌ Changing this feature will change prediction (may have confounders)
- ❌ This feature is the "most important" in real world

### Critical Warnings

**1. Correlation, not Causation**
- High importance shows the model USES this feature
- Does NOT prove changing feature will change outcome
- Example: "Hours worked" might be important for income prediction, but increasing hours might not increase income if you're salaried

**2. Correlated Features**
- If two features are correlated, importance splits between them
- Removing one might increase the other's importance
- Don't conclude one is "unimportant" if its twin is important

**3. Algorithm Differences**
- Different algorithms rank features differently
- Decision Tree: Few features get all importance (sparse)
- Random Forest: More distributed importance
- XGBoost: Different still (based on gradients)
- Solution: Check importance across multiple models

**4. Model-Specific**
- Importance shows what THIS model uses
- Different model architecture → different importances
- Importance is NOT a universal property of features

### Using Feature Importance for Feature Selection

```python
# Train model
model.fit(X_train, y_train)

# Get importances
importances = model.feature_importances_

# Select features with importance > threshold
threshold = 0.01  # Features must contribute at least 1%
important_features = [feature for feature, imp in zip(feature_names, importances) if imp > threshold]

print(f"Keeping {len(important_features)} out of {len(feature_names)} features")

# Retrain with selected features
X_train_selected = X_train[important_features]
X_test_selected = X_test[important_features]

model.fit(X_train_selected, y_train)
```

**Caution:** Don't do this on test set! Use cross-validation or separate validation set.

---

## Common Pitfalls & Best Practices

### Pitfall 1: Not Preventing Overfitting in Trees

**Problem:**
```python
# BAD: Unlimited depth tree
tree = DecisionTreeClassifier()  # max_depth=None (default)
tree.fit(X_train, y_train)
# Result: 100% train accuracy, 60% test accuracy (overfitting!)
```

**Solution:**
```python
# GOOD: Limit tree depth
tree = DecisionTreeClassifier(max_depth=5, min_samples_split=10)
tree.fit(X_train, y_train)
# Result: 85% train accuracy, 82% test accuracy (good generalization)
```

**Best Practice:** Always set max_depth for single trees (5-10 typical)

---

### Pitfall 2: Using Too Few Trees in Random Forest

**Problem:**
```python
# BAD: Only 10 trees
rf = RandomForestClassifier(n_estimators=10)
# Result: High variance, unstable predictions
```

**Solution:**
```python
# GOOD: Use at least 100 trees
rf = RandomForestClassifier(n_estimators=100)
# Better: Use 200-500 for important projects
rf = RandomForestClassifier(n_estimators=200)
```

**Best Practice:** Start with 100 trees, increase if performance improves

---

### Pitfall 3: Wrong learning_rate in XGBoost

**Problem:**
```python
# BAD: High learning rate with many trees
xgb_clf = xgb.XGBClassifier(learning_rate=0.3, n_estimators=1000)
# Result: Overfitting
```

**Solution:**
```python
# GOOD: Match learning_rate to n_estimators
# High learning_rate → fewer trees
xgb_clf = xgb.XGBClassifier(learning_rate=0.3, n_estimators=100)

# OR low learning_rate → more trees
xgb_clf = xgb.XGBClassifier(learning_rate=0.01, n_estimators=1000)
```

**Best Practice:** Inverse relationship - lower learning_rate needs more trees

---

### Pitfall 4: Not Using Cross-Validation

**Problem:**
```python
# BAD: Single train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y)
model.fit(X_train, y_train)
score = model.score(X_test, y_test)
# Result: Might get lucky/unlucky with split
```

**Solution:**
```python
# GOOD: Use cross-validation
from sklearn.model_selection import cross_val_score
scores = cross_val_score(model, X, y, cv=5)
print(f"Mean: {scores.mean():.3f} (+/- {scores.std():.3f})")
# Result: More reliable estimate
```

**Best Practice:** Use cross-validation for model evaluation (Week 4 topic)

---

### Pitfall 5: Feature Leakage in Trees

**Problem:**
```python
# BAD: Including target-derived features
df['income_category'] = df['income'].apply(lambda x: 'high' if x > 50000 else 'low')
X = df.drop('income', axis=1)  # But includes 'income_category'!
y = df['income']
# Result: Perfect predictions (but useless in production)
```

**Solution:**
```python
# GOOD: Only use features available at prediction time
X = df[['age', 'education', 'hours_worked']]  # No target-derived features
y = df['income']
```

**Best Practice:** Ask "Will I have this feature when making real predictions?"

---

### Pitfall 6: Comparing Algorithms Unfairly

**Problem:**
```python
# BAD: Different preprocessing for each algorithm
rf.fit(X_train, y_train)  # No scaling
xgb_clf.fit(X_train_scaled, y_train)  # Scaled
# Result: Can't fairly compare
```

**Solution:**
```python
# GOOD: Same data for all algorithms
# Trees don't need scaling, but use same data anyway
for model in [decision_tree, random_forest, xgboost]:
    model.fit(X_train, y_train)
    scores.append(model.score(X_test, y_test))
```

**Best Practice:** Use identical train/test split and preprocessing for all comparisons

---

### Pitfall 7: Ignoring Class Imbalance

**Problem:**
```python
# Dataset: 95% class 0, 5% class 1
tree = DecisionTreeClassifier()
tree.fit(X_train, y_train)
accuracy = tree.score(X_test, y_test)  # 95% accuracy!
# But model just predicts class 0 every time (useless)
```

**Solution:**
```python
# GOOD: Use class_weight='balanced' or stratified splitting
tree = DecisionTreeClassifier(class_weight='balanced')
tree.fit(X_train, y_train)
# AND use appropriate metrics (precision, recall, F1)
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))
```

**Best Practice:** Always check class distribution and use balanced metrics

---

### Best Practices Summary

**Data Preparation:**
- ✅ Check for missing values before training
- ✅ Split data BEFORE any preprocessing
- ✅ Use stratification for classification (preserves class distribution)
- ✅ Set random_state for reproducibility

**Model Training:**
- ✅ Always limit max_depth for single trees (5-10)
- ✅ Use at least 100 trees for Random Forest
- ✅ Set learning_rate and n_estimators together for XGBoost
- ✅ Use cross-validation for reliable evaluation

**Model Evaluation:**
- ✅ Evaluate on BOTH train and test (detect overfitting)
- ✅ Use multiple metrics (accuracy, precision, recall, F1)
- ✅ Check confusion matrix for classification
- ✅ Plot residuals for regression

**Interpretation:**
- ✅ Extract feature importance
- ✅ Compare across multiple models
- ✅ Remember: correlation ≠ causation
- ✅ Visualize decision trees when interpretability matters

---

## Hyperparameter Tuning Reference

### Decision Tree Tuning

**Start with these defaults:**
```python
DecisionTreeClassifier(
    max_depth=5,
    min_samples_split=10,
    min_samples_leaf=5,
    criterion='gini'
)
```

**Tuning strategy:**
1. Vary max_depth: [3, 5, 7, 10, 15]
2. If overfitting, increase min_samples_split
3. If underfitting, increase max_depth

---

### Random Forest Tuning

**Start with these defaults:**
```python
RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    min_samples_split=5,
    max_features='sqrt',
    bootstrap=True
)
```

**Tuning strategy:**
1. Increase n_estimators until performance plateaus (100 → 200 → 500)
2. Vary max_depth: [5, 10, 15, 20, None]
3. Adjust min_samples_split if overfitting: [2, 5, 10]
4. Usually don't need to change max_features

---

### XGBoost Tuning

**Start with these defaults:**
```python
xgb.XGBClassifier(
    n_estimators=100,
    max_depth=5,
    learning_rate=0.1,
    subsample=0.8,
    colsample_bytree=0.8
)
```

**Tuning strategy (in order):**

1. **Fix learning_rate=0.1, tune max_depth and n_estimators**
   - max_depth: [3, 5, 7, 9]
   - n_estimators: [50, 100, 200, 500]

2. **Tune subsample and colsample_bytree (regularization)**
   - subsample: [0.6, 0.7, 0.8, 0.9, 1.0]
   - colsample_bytree: [0.6, 0.7, 0.8, 0.9, 1.0]

3. **Tune regularization parameters**
   - reg_alpha: [0, 0.1, 0.5, 1]
   - reg_lambda: [0, 0.1, 0.5, 1, 2]

4. **Lower learning_rate and increase n_estimators for final model**
   - learning_rate: 0.01
   - n_estimators: 1000+ (with early stopping)

---

### Grid Search Example

```python
from sklearn.model_selection import GridSearchCV

# Define parameter grid
param_grid = {
    'max_depth': [3, 5, 7],
    'n_estimators': [100, 200, 300],
    'learning_rate': [0.01, 0.1, 0.3]
}

# Create grid search
grid_search = GridSearchCV(
    xgb.XGBClassifier(),
    param_grid,
    cv=5,              # 5-fold cross-validation
    scoring='f1',      # Optimize for F1 score
    n_jobs=-1,         # Use all CPU cores
    verbose=1
)

# Run grid search
grid_search.fit(X_train, y_train)

# Best parameters
print(f"Best parameters: {grid_search.best_params_}")
print(f"Best F1 score: {grid_search.best_score_:.3f}")

# Use best model
best_model = grid_search.best_estimator_
```

**Caution:** Grid search can be slow! Start with small grid, expand if needed.

---

## Quick Code Templates

### Template 1: Train and Compare All Three Algorithms

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pandas as pd

# Train all three models
models = {
    'Decision Tree': DecisionTreeClassifier(max_depth=5, random_state=42),
    'Random Forest': RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42),
    'XGBoost': xgb.XGBClassifier(n_estimators=100, max_depth=5, learning_rate=0.1, random_state=42)
}

results = []

for name, model in models.items():
    # Train
    model.fit(X_train, y_train)

    # Predict
    y_pred = model.predict(X_test)

    # Calculate metrics
    results.append({
        'Algorithm': name,
        'Accuracy': accuracy_score(y_test, y_pred),
        'Precision': precision_score(y_test, y_pred, average='weighted'),
        'Recall': recall_score(y_test, y_pred, average='weighted'),
        'F1-Score': f1_score(y_test, y_pred, average='weighted')
    })

# Create comparison table
comparison_df = pd.DataFrame(results)
print(comparison_df.to_string(index=False))
```

---

### Template 2: Extract and Visualize Feature Importance

```python
import matplotlib.pyplot as plt
import pandas as pd

# After training model
importances = model.feature_importances_

# Create DataFrame
importance_df = pd.DataFrame({
    'feature': feature_names,
    'importance': importances
}).sort_values('importance', ascending=False)

# Print top 10
print("Top 10 Most Important Features:")
print(importance_df.head(10))

# Visualize
plt.figure(figsize=(10, 6))
top_10 = importance_df.head(10)
plt.barh(top_10['feature'], top_10['importance'])
plt.xlabel('Importance')
plt.ylabel('Feature')
plt.title('Top 10 Feature Importance')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()
```

---

### Template 3: XGBoost with Early Stopping

```python
import xgboost as xgb
from sklearn.model_selection import train_test_split

# Split into train and validation
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Create model
xgb_clf = xgb.XGBClassifier(
    n_estimators=1000,      # Many trees
    learning_rate=0.01,     # Low learning rate
    max_depth=5,
    random_state=42
)

# Train with early stopping
xgb_clf.fit(
    X_train, y_train,
    eval_set=[(X_val, y_val)],
    early_stopping_rounds=50,    # Stop if no improvement for 50 rounds
    verbose=10                   # Print every 10 rounds
)

print(f"Best iteration: {xgb_clf.best_iteration}")
print(f"Best score: {xgb_clf.best_score}")
```

---

## Additional Resources

**sklearn Documentation:**
- Decision Trees: https://scikit-learn.org/stable/modules/tree.html
- Random Forests: https://scikit-learn.org/stable/modules/ensemble.html#forest
- Feature Importance: https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_importances.html

**XGBoost Documentation:**
- Official Docs: https://xgboost.readthedocs.io/
- Parameters Guide: https://xgboost.readthedocs.io/en/stable/parameter.html
- Tutorials: https://xgboost.readthedocs.io/en/stable/tutorials/index.html

**Academic Papers:**
- Random Forests (Breiman, 2001): Original paper on Random Forests
- XGBoost (Chen & Guestrin, 2016): "XGBoost: A Scalable Tree Boosting System"

**Practical Guides:**
- Week 4 materials: Cross-validation and hyperparameter tuning
- Kaggle tutorials: Learn from competition winners who use these algorithms

---

## Version

Tree & Ensemble Methods Complete Guide v1.0 | Week 3 | January 24, 2026

**This appendix is a standalone reference. You can use it without taking the course.**

**Bookmark this page - you'll reference it in every tree-based ML project!**
