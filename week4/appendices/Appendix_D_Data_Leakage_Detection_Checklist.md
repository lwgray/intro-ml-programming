# Appendix D: Data Leakage Detection & Prevention Checklist

**Complete standalone reference for detecting and preventing data leakage in machine learning**

---

## Table of Contents

1. [What is Data Leakage?](#what-is-data-leakage)
2. [Why Data Leakage Matters](#why-data-leakage-matters)
3. [Pre-Deployment Checklist](#pre-deployment-checklist)
4. [Common Sources Catalog](#common-sources-catalog)
5. [Detection Methods](#detection-methods)
6. [sklearn Pipeline Complete Guide](#sklearn-pipeline-complete-guide)
7. [Pipeline Template (Copy-Paste Ready)](#pipeline-template-copy-paste-ready)
8. [Case Studies](#case-studies)
9. [Advanced Leakage Scenarios](#advanced-leakage-scenarios)
10. [Quick Reference](#quick-reference)

---

## What is Data Leakage?

**Data leakage** occurs when information from outside the training dataset is used to create the model, leading to overly optimistic performance estimates that don't hold in production.

### The Core Problem

```
TRAINING (What you have)  →  DEPLOYMENT (What you'll get)
     Known data                  Unknown future data

❌ LEAKAGE: Future information flows backwards to influence training
✅ CORRECT: Only past/present information used for training
```

### Two Types of Leakage

**1. Train-Test Contamination**
- Information from test set leaks into training
- Example: Scaling data before splitting

**2. Target Leakage**
- Features include information about the target that wouldn't be available at prediction time
- Example: Using "purchased_amount" to predict "will_purchase"

---

## Why Data Leakage Matters

### Real-World Impact

| Phase | With Leakage | Without Leakage |
|-------|--------------|-----------------|
| **Development** | Accuracy: 95% 🎉 | Accuracy: 83% |
| **Stakeholder Demo** | "Amazing model!" | "Good model" |
| **Production** | Accuracy: 62% 💀 | Accuracy: 81% |
| **Outcome** | Project failure, loss of trust | Success, deployment |

### Consequences

1. **Technical:**
   - Model fails in production
   - Metrics drop dramatically
   - Predictions are unreliable

2. **Business:**
   - Wasted development time
   - Lost revenue/resources
   - Missed opportunities

3. **Career:**
   - Loss of credibility
   - Damage to reputation
   - Potential termination

**Prevention is 1000x easier than fixing after deployment!**

---

## Pre-Deployment Checklist

### ✓ Data Splitting Checklist

```
□ Did you split data BEFORE any preprocessing?
  ❌ scaler.fit(X); then train_test_split()
  ✓ train_test_split(); then scaler.fit(X_train)

□ Is your test set truly held out (untouched during development)?
  ❌ Checked test set distribution and adjusted features
  ✓ Locked test set away, only used for final evaluation

□ For time series: Are you predicting future from past only?
  ❌ Using regular K-Fold on time-ordered data
  ✓ Using TimeSeriesSplit or walk-forward validation

□ For grouped data: Are groups fully separated?
  ❌ Patient measurements split across train/test
  ✓ All measurements from same patient in same set
```

---

### ✓ Preprocessing Checklist

```
□ Are ALL transformations inside a Pipeline?
  ❌ Manual fit/transform outside Pipeline
  ✓ All preprocessing steps in Pipeline

□ Did you fit transformers on training data only?
  ❌ scaler.fit(X_all)
  ✓ scaler.fit(X_train) or use Pipeline

□ For imputation: Using training statistics only?
  ❌ df.fillna(df.mean()) before split
  ✓ imputer.fit(X_train) or SimpleImputer in Pipeline

□ For encoding: Did you fit encoder on training data?
  ❌ encoder.fit(X_all)
  ✓ encoder.fit(X_train) or in Pipeline

□ For feature scaling: Training statistics only?
  ❌ StandardScaler().fit(X_all)
  ✓ StandardScaler().fit(X_train) or in Pipeline
```

---

### ✓ Feature Engineering Checklist

```
□ Are features available at prediction time?
  ❌ Using future information (e.g., next_month_sales)
  ✓ Only past/current information

□ For aggregations: Using training data only?
  ❌ df.groupby('category')['price'].mean() on all data
  ✓ Calculate on training set, apply to test

□ For feature selection: Fit on training only?
  ❌ selector.fit(X_all, y_all)
  ✓ selector.fit(X_train, y_train) or in Pipeline

□ Did you avoid using the target variable in features?
  ❌ feature: avg_purchase_amount (when predicting purchase)
  ✓ No target-derived features
```

---

### ✓ Cross-Validation Checklist

```
□ Using Pipeline with cross-validation?
  ❌ cross_val_score(model, X_preprocessed, y)
  ✓ cross_val_score(pipeline, X, y)

□ Are transformations happening inside each fold?
  ❌ Fit preprocessor once, then cross-validate
  ✓ Pipeline refits preprocessor for each fold

□ For hyperparameter tuning: Using nested CV or holdout set?
  ❌ GridSearchCV, then report CV score
  ✓ GridSearchCV on train, evaluate on separate test set

□ Correct CV strategy for your data type?
  ❌ K-Fold on time series
  ✓ TimeSeriesSplit for temporal data
  ✓ StratifiedKFold for imbalanced classification
  ✓ GroupKFold for grouped data
```

---

### ✓ Validation Checklist

```
□ Are CV scores similar to test scores?
  ❌ CV: 0.95, Test: 0.75 → Suspect leakage!
  ✓ CV: 0.83, Test: 0.81 → Looks good

□ Does model performance make sense?
  ❌ 99% accuracy on a hard problem → Too good to be true
  ✓ 85% accuracy → Reasonable

□ Did you check feature importances for suspicious features?
  ❌ Top feature: "transaction_id" → Leakage!
  ✓ Top features: meaningful predictors

□ Have you tested on truly unseen data?
  ❌ Only evaluated on split from same dataset
  ✓ Tested on data collected at different time/place
```

---

## Common Sources Catalog

### 1. Scaling Before Splitting

**❌ WRONG:**

```python
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Fit scaler on ALL data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)  # ← LEAKAGE!

# Then split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y)

# Test statistics influenced the scaler!
```

**Why it's wrong:**
- Scaler calculated mean/std from ALL data (including test set)
- Test set information "leaked" into training preprocessing
- Model expects that specific distribution, fails in production

**✓ CORRECT:**

```python
# Method 1: Manual (error-prone)
X_train, X_test, y_train, y_test = train_test_split(X, y)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  # Fit on train only
X_test_scaled = scaler.transform(X_test)  # Apply to test

# Method 2: Pipeline (recommended)
from sklearn.pipeline import Pipeline

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression())
])

X_train, X_test, y_train, y_test = train_test_split(X, y)
pipeline.fit(X_train, y_train)  # Scaler fits on train only
```

**Impact:** Can inflate accuracy by 5-15 percentage points!

---

### 2. Imputation Using All Data

**❌ WRONG:**

```python
import pandas as pd

# Fill missing values using global mean
df['age'].fillna(df['age'].mean(), inplace=True)  # ← LEAKAGE!

# Then split
X_train, X_test, y_train, y_test = train_test_split(df, y)
```

**Why it's wrong:**
- Imputation used mean from ALL data (including test)
- If test set has different distribution, this won't work in production

**✓ CORRECT:**

```python
from sklearn.impute import SimpleImputer

# Split first
X_train, X_test, y_train, y_test = train_test_split(X, y)

# Impute using training mean only
imputer = SimpleImputer(strategy='mean')
X_train_imputed = imputer.fit_transform(X_train)  # Fit on train
X_test_imputed = imputer.transform(X_test)  # Apply to test

# Or use Pipeline (better)
pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    ('model', RandomForestClassifier())
])
```

---

### 3. Feature Selection on All Data

**❌ WRONG:**

```python
from sklearn.feature_selection import SelectKBest

# Select features using ALL data
selector = SelectKBest(k=10)
X_selected = selector.fit_transform(X, y)  # ← LEAKAGE!

# Then split
X_train, X_test, y_train, y_test = train_test_split(X_selected, y)
```

**Why it's wrong:**
- Feature selection saw test labels (y)
- Selected features that correlate well with test targets
- Overly optimistic performance

**✓ CORRECT:**

```python
# Split first
X_train, X_test, y_train, y_test = train_test_split(X, y)

# Select features on training data only
selector = SelectKBest(k=10)
X_train_selected = selector.fit_transform(X_train, y_train)
X_test_selected = selector.transform(X_test)

# Or use Pipeline
pipeline = Pipeline([
    ('selector', SelectKBest(k=10)),
    ('model', LogisticRegression())
])
```

---

### 4. Target Leakage (Features That Don't Exist at Prediction Time)

**❌ WRONG:**

```python
# Predicting: Will customer default on loan?
# Features include:
X = df[['income', 'credit_score', 'debt_after_default']]  # ← LEAKAGE!
#                                  ^
#                                  This only exists AFTER default!
```

**Why it's wrong:**
- `debt_after_default` is only known AFTER the event you're predicting
- In production, you won't have this feature
- Model relies on unavailable information

**✓ CORRECT:**

```python
# Only use features available BEFORE the prediction
X = df[['income', 'credit_score', 'current_debt', 'employment_length']]
# All of these exist at the time you need to make a prediction
```

**Examples of target leakage:**

| Prediction | Leaky Feature | Why |
|------------|---------------|-----|
| Will customer churn? | `last_login_date` | Only know after churn |
| Will patient recover? | `recovery_time` | Only know after recovery |
| Will transaction be fraud? | `chargeback_date` | Only know after fraud |
| Will student pass? | `final_exam_score` | The outcome itself! |

---

### 5. Using Future Information in Time Series

**❌ WRONG:**

```python
# Predicting stock price at time t
# Features include price at time t+1
df['target'] = df['price']
df['feature_next_day_price'] = df['price'].shift(-1)  # ← LEAKAGE!
```

**Why it's wrong:**
- You're using tomorrow's price to predict today's price
- Literal time travel!

**✓ CORRECT:**

```python
# Only use past information
df['target'] = df['price']
df['feature_yesterday_price'] = df['price'].shift(1)  # Past only
df['feature_7day_avg'] = df['price'].rolling(7).mean()  # Past only
```

---

### 6. Duplicates Across Train/Test Split

**❌ WRONG:**

```python
# Dataset has duplicate rows
X_train, X_test, y_train, y_test = train_test_split(X, y)
# Some duplicates in train, their copies in test → Model has seen them!
```

**Why it's wrong:**
- Model trained on exact copies of test samples
- Unrealistic perfect predictions on duplicates

**✓ CORRECT:**

```python
# Remove duplicates BEFORE splitting
df_unique = df.drop_duplicates()
X, y = df_unique.drop('target', axis=1), df_unique['target']
X_train, X_test, y_train, y_test = train_test_split(X, y)
```

---

### 7. Data Snooping (Looking at Test Set)

**❌ WRONG:**

```python
# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y)

# "Let me just check the test set distribution..."
print(X_test.describe())
# "Oh, test set has outliers. Let me remove outliers from training."
X_train = X_train[X_train['feature'] < 100]  # ← LEAKAGE!

# You made a training decision based on test set information!
```

**Why it's wrong:**
- Your knowledge of test set influenced training decisions
- Information leak through your brain!

**✓ CORRECT:**

```python
# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y)

# ONLY look at training data
print(X_train.describe())

# Make all decisions based on training data only
# Treat test set as if it doesn't exist until final evaluation
```

---

### 8. Using Test Set to Choose Model

**❌ WRONG:**

```python
X_train, X_test, y_train, y_test = train_test_split(X, y)

# Try different models
model_A = LogisticRegression().fit(X_train, y_train)
score_A = model_A.score(X_test, y_test)  # 0.85

model_B = RandomForest().fit(X_train, y_train)
score_B = model_B.score(X_test, y_test)  # 0.88

# "Model B is better, let's use it!"
final_model = model_B
final_score = score_B  # ← This score is biased!
```

**Why it's wrong:**
- You selected model_B BECAUSE it performed well on test set
- Test score is optimistically biased

**✓ CORRECT:**

```python
# Method 1: Use validation set
X_train_full, X_test, y_train_full, y_test = train_test_split(X, y, test_size=0.2)
X_train, X_val, y_train, y_val = train_test_split(X_train_full, y_train_full, test_size=0.2)

# Choose model using validation set
score_A = LogisticRegression().fit(X_train, y_train).score(X_val, y_val)
score_B = RandomForest().fit(X_train, y_train).score(X_val, y_val)

# Select best model
final_model = model_B  # Based on validation score

# Evaluate ONCE on test set
final_score = final_model.score(X_test, y_test)  # Unbiased!

# Method 2: Use cross-validation
scores_A = cross_val_score(LogisticRegression(), X_train_full, y_train_full, cv=5)
scores_B = cross_val_score(RandomForest(), X_train_full, y_train_full, cv=5)
# Choose based on CV scores, evaluate on test set once
```

---

## Detection Methods

### Method 1: Sanity Check - Too Good to Be True?

**Red flags:**

```python
# Accuracy on a difficult problem
Spam detection: 99.9% accuracy  # Suspicious! (Gmail is ~98%)
Cancer diagnosis: 99.5% accuracy  # Suspicious! (Humans are ~90%)
Stock prediction: 95% R²  # Definitely leakage!

# Perfect scores
Training: 1.00, Test: 1.00  # Almost certainly leakage
```

**What to do:**
- Research expected performance for your problem
- If your model is "too good," investigate for leakage

---

### Method 2: CV Score vs Test Score Gap

**Red flag: Large gap between CV and test scores**

```python
pipeline = Pipeline([...])

# CV on training set
cv_scores = cross_val_score(pipeline, X_train, y_train, cv=5)
print(f"CV: {cv_scores.mean():.3f}")  # 0.92

# Test set
test_score = pipeline.score(X_test, y_test)
print(f"Test: {test_score:.3f}")  # 0.73

# Gap: 0.92 - 0.73 = 0.19 (19 points!)
# ⚠️ Suspect leakage or overfitting
```

**Guidelines:**
- Gap < 0.05 (5 points): Normal
- Gap 0.05-0.10 (5-10 points): Check for overfitting
- Gap > 0.10 (>10 points): Likely leakage or severe overfitting

**What to do:**
1. Check for preprocessing before split
2. Ensure Pipeline used correctly
3. Check for target leakage
4. Review feature engineering

---

### Method 3: Feature Importance Analysis

**Red flag: Suspicious features have high importance**

```python
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()
model.fit(X_train, y_train)

# Get feature importances
importances = pd.DataFrame({
    'feature': X_train.columns,
    'importance': model.feature_importances_
}).sort_values('importance', ascending=False)

print(importances.head())
```

**Suspicious patterns:**

```
feature                  importance
transaction_id           0.45  ← Should be random! Leakage!
row_number               0.32  ← Should be meaningless! Leakage!
customer_lifetime_value  0.28  ← If predicting purchase, this is target leakage!
age                      0.15
income                   0.12
```

**What to do:**
- Remove ID features (they should not predict!)
- Investigate high-importance features: are they available at prediction time?
- Check for target-derived features

---

### Method 4: Temporal Validation (Time Series)

**Test:** Train on old data, test on future data

```python
# Sort by time
df = df.sort_values('date')

# Split: Train on 2020-2021, test on 2022
train = df[df['date'] < '2022-01-01']
test = df[df['date'] >= '2022-01-01']

X_train, y_train = train.drop('target', axis=1), train['target']
X_test, y_test = test.drop('target', axis=1), test['target']

# Evaluate
model.fit(X_train, y_train)
score = model.score(X_test, y_test)
```

**Red flag:**
- Performance drops dramatically on future data → Using future information

---

### Method 5: Leakage Audit - Manual Code Review

**Go through code line by line:**

```python
# For each preprocessing step, ask:
1. Does this use ALL data? → STOP! Leakage risk
2. Does this fit on training only? → Good
3. Is this inside Pipeline? → Good
4. Could this use test set information? → Investigate
```

**Create a preprocessing log:**

```
Step                    Fit on        Transform on    Leakage?
──────────────────────────────────────────────────────────────
StandardScaler          X_train       X_train, X_test    ✓ No
SimpleImputer           X_train       X_train, X_test    ✓ No
OneHotEncoder           X_train       X_train, X_test    ✓ No
Feature selection       X_train       X_train, X_test    ✓ No
```

If any step fits on `X_all` or `X` (before split) → **LEAKAGE!**

---

## sklearn Pipeline Complete Guide

### Why Pipeline?

**Pipeline automatically prevents leakage by:**
1. Fitting transformers on training data only
2. Applying transformers correctly to test data
3. Making it nearly impossible to accidentally leak

### Basic Pipeline Structure

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# Create pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),      # Step 1: Scale
    ('model', LogisticRegression())    # Step 2: Train model
])

# Each step is a tuple: ('name', transformer_or_estimator)
```

### How Pipeline Works

**When you call `pipeline.fit(X_train, y_train)`:**

```
1. scaler.fit(X_train)               ← Learns mean/std from TRAIN only
2. X_train_scaled = scaler.transform(X_train)
3. model.fit(X_train_scaled, y_train)
```

**When you call `pipeline.predict(X_test)`:**

```
1. X_test_scaled = scaler.transform(X_test)  ← Uses TRAIN mean/std!
2. predictions = model.predict(X_test_scaled)
```

**Key:** Scaler never sees test data during fit! No leakage!

---

### Pipeline with Multiple Preprocessing Steps

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.feature_selection import SelectKBest

pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),     # Step 1: Fill missing
    ('scaler', StandardScaler()),                    # Step 2: Scale
    ('selector', SelectKBest(k=10)),                 # Step 3: Select features
    ('model', RandomForestClassifier())              # Step 4: Train model
])

# All steps fit on training data only!
pipeline.fit(X_train, y_train)
```

**Execution order:**

```
Training:
X_train → Imputer.fit_transform → Scaler.fit_transform → Selector.fit_transform → Model.fit

Prediction:
X_test → Imputer.transform → Scaler.transform → Selector.transform → Model.predict
```

---

### Pipeline with ColumnTransformer (Different Preprocessing for Different Columns)

**Use case:** Numeric columns need scaling, categorical columns need encoding

```python
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

# Define which columns get which preprocessing
numeric_features = ['age', 'income', 'credit_score']
categorical_features = ['city', 'occupation', 'education']

# Create preprocessing pipelines for each column type
numeric_transformer = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline([
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('encoder', OneHotEncoder(handle_unknown='ignore'))
])

# Combine into ColumnTransformer
preprocessor = ColumnTransformer([
    ('num', numeric_transformer, numeric_features),
    ('cat', categorical_transformer, categorical_features)
])

# Final pipeline
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression())
])

# Use it
pipeline.fit(X_train, y_train)
pipeline.predict(X_test)
```

**Benefit:** Different columns get appropriate preprocessing, all leakage-free!

---

### Pipeline with GridSearchCV

**Tune hyperparameters while maintaining Pipeline benefits**

```python
from sklearn.model_selection import GridSearchCV

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', RandomForestClassifier())
])

# Parameter grid: use 'step_name__parameter_name' syntax
param_grid = {
    'model__max_depth': [10, 20, 30],
    'model__n_estimators': [100, 200, 300],
    'model__min_samples_split': [2, 5, 10]
}

# GridSearch with Pipeline
grid = GridSearchCV(pipeline, param_grid, cv=5, n_jobs=-1)
grid.fit(X_train, y_train)

print(f"Best params: {grid.best_params_}")
print(f"Best CV score: {grid.best_score_:.3f}")
print(f"Test score: {grid.score(X_test, y_test):.3f}")
```

**Magic:** For each CV fold, Pipeline refits the scaler! No leakage!

---

### Accessing Pipeline Steps

```python
# After fitting
pipeline.fit(X_train, y_train)

# Access fitted transformers
scaler = pipeline.named_steps['scaler']
print(scaler.mean_)  # Mean learned from training data

model = pipeline.named_steps['model']
print(model.feature_importances_)

# Or use indexing
scaler = pipeline[0]
model = pipeline[-1]  # Last step
```

---

### Custom Transformers in Pipeline

**Create your own preprocessing step:**

```python
from sklearn.base import BaseEstimator, TransformerMixin

class LogTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        # Nothing to learn
        return self

    def transform(self, X):
        # Apply log transformation
        return np.log1p(X)

# Use in Pipeline
pipeline = Pipeline([
    ('log', LogTransformer()),
    ('scaler', StandardScaler()),
    ('model', Ridge())
])
```

---

## Pipeline Template (Copy-Paste Ready)

### Template 1: Classification with Mixed Data Types

```python
"""
COPY-PASTE PIPELINE TEMPLATE FOR CLASSIFICATION
Handles numeric and categorical features separately
Prevents data leakage automatically
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# ============= LOAD YOUR DATA =============
# Replace with your data loading code
X, y = load_your_data()  # X: DataFrame, y: Series

# ============= DEFINE COLUMN TYPES =============
# List your numeric and categorical columns
numeric_features = ['age', 'income', 'hours_per_week']  # EDIT THIS
categorical_features = ['city', 'occupation', 'education']  # EDIT THIS

# ============= SPLIT DATA FIRST =============
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# ============= CREATE PREPROCESSING PIPELINES =============
# Numeric features: impute with median, then scale
numeric_transformer = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

# Categorical features: impute with constant, then one-hot encode
categorical_transformer = Pipeline([
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('encoder', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
])

# ============= COMBINE PREPROCESSING =============
preprocessor = ColumnTransformer([
    ('num', numeric_transformer, numeric_features),
    ('cat', categorical_transformer, categorical_features)
], remainder='drop')  # Drop columns not specified

# ============= CREATE FULL PIPELINE =============
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(random_state=42))
])

# ============= HYPERPARAMETER TUNING (OPTIONAL) =============
param_grid = {
    'classifier__max_depth': [10, 20, 30],
    'classifier__n_estimators': [100, 200],
    'classifier__min_samples_split': [2, 5]
}

grid_search = GridSearchCV(
    pipeline, param_grid, cv=5, scoring='accuracy', n_jobs=-1, verbose=1
)

# ============= TRAIN =============
grid_search.fit(X_train, y_train)

# ============= EVALUATE =============
print(f"Best parameters: {grid_search.best_params_}")
print(f"Best CV score: {grid_search.best_score_:.3f}")

# Test set evaluation
y_pred = grid_search.predict(X_test)
test_score = grid_search.score(X_test, y_test)
print(f"Test accuracy: {test_score:.3f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# ============= SAVE MODEL (OPTIONAL) =============
import joblib
joblib.dump(grid_search.best_estimator_, 'model_pipeline.pkl')

# ============= LOAD AND USE (OPTIONAL) =============
# loaded_pipeline = joblib.load('model_pipeline.pkl')
# predictions = loaded_pipeline.predict(X_new)
```

---

### Template 2: Regression with Numeric Data Only

```python
"""
COPY-PASTE PIPELINE TEMPLATE FOR REGRESSION
Numeric features only
Prevents data leakage automatically
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score

# ============= LOAD YOUR DATA =============
X, y = load_your_data()  # Replace with your data

# ============= SPLIT DATA FIRST =============
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ============= CREATE PIPELINE =============
pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler()),
    ('regressor', GradientBoostingRegressor(random_state=42))
])

# ============= TRAIN =============
pipeline.fit(X_train, y_train)

# ============= CROSS-VALIDATION =============
cv_scores = cross_val_score(
    pipeline, X_train, y_train, cv=5, scoring='r2'
)
print(f"CV R²: {cv_scores.mean():.3f} ± {cv_scores.std():.3f}")

# ============= EVALUATE =============
y_pred = pipeline.predict(X_test)
test_r2 = r2_score(y_test, y_pred)
test_rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"Test R²: {test_r2:.3f}")
print(f"Test RMSE: {test_rmse:.3f}")
```

---

### Template 3: Time Series with Pipeline

```python
"""
COPY-PASTE PIPELINE TEMPLATE FOR TIME SERIES
Uses TimeSeriesSplit to prevent future leakage
"""

import numpy as np
from sklearn.model_selection import TimeSeriesSplit, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge

# ============= LOAD YOUR TIME SERIES DATA =============
# Make sure data is sorted by time!
X, y = load_your_timeseries_data()

# ============= CREATE PIPELINE =============
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', Ridge())
])

# ============= TIME SERIES CROSS-VALIDATION =============
tscv = TimeSeriesSplit(n_splits=5)

# Cross-validate
cv_scores = cross_val_score(pipeline, X, y, cv=tscv, scoring='r2')
print(f"Time Series CV R²: {cv_scores.mean():.3f} ± {cv_scores.std():.3f}")

# ============= TRAIN ON ALL AVAILABLE DATA =============
# For time series, often train on all historical data
pipeline.fit(X, y)

# ============= PREDICT FUTURE =============
# X_future = ...  # Future time steps
# predictions = pipeline.predict(X_future)
```

---

## Case Studies

### Case Study 1: Kaggle Competition Leakage

**Scenario:** Predicting whether a passenger on the Titanic survived

**The Mistake:**

```python
# Load data
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

# Combine train and test to preprocess together
all_data = pd.concat([train, test])

# Fill missing ages with mean
all_data['Age'].fillna(all_data['Age'].mean(), inplace=True)  # ← LEAKAGE!

# One-hot encode
all_data = pd.get_dummies(all_data, columns=['Sex', 'Embarked'])  # ← LEAKAGE!

# Split back
train_processed = all_data[:len(train)]
test_processed = all_data[len(train):]
```

**Why it's wrong:**
- Test data influenced imputation (age mean)
- Test data influenced encoding (which categories exist)
- In real deployment, you won't have test data to combine!

**The Fix:**

```python
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer

# Load only training data
train = pd.read_csv('train.csv')
X_train = train.drop('Survived', axis=1)
y_train = train['Survived']

# Create pipeline
numeric_features = ['Age', 'Fare']
categorical_features = ['Sex', 'Embarked']

numeric_transformer = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline([
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('encoder', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer([
    ('num', numeric_transformer, numeric_features),
    ('cat', categorical_transformer, categorical_features)
])

pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier())
])

# Train (preprocessor learns from training data only)
pipeline.fit(X_train, y_train)

# When test data arrives, pipeline applies training transformations
test = pd.read_csv('test.csv')
predictions = pipeline.predict(test)  # Correct!
```

---

### Case Study 2: Medical Diagnosis Catastrophe

**Scenario:** Hospital builds model to predict patient mortality

**The Mistake:**

```python
# Load patient data
patients = pd.read_csv('patient_data.csv')

# Feature engineering
patients['avg_medication_cost'] = patients.groupby('hospital')['medication_cost'].transform('mean')  # ← LEAKAGE!

# This calculates average across ALL patients, including test set

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train
model.fit(X_train, y_train)
```

**Why it's wrong:**
- `avg_medication_cost` calculated from ALL patients (including test)
- Test patients influenced the feature
- In production, new patients arrive one at a time - you can't calculate "average across all future patients"

**Impact:**
- Development accuracy: 94%
- Production accuracy: 71%
- 23-point drop! Model deployed, made incorrect predictions, patients affected

**The Fix:**

```python
# Split FIRST
X_train, X_test, y_train, y_test = train_test_split(patients.drop('mortality', axis=1),
                                                      patients['mortality'],
                                                      test_size=0.2)

# Calculate averages from TRAINING data only
train_avg = X_train.groupby('hospital')['medication_cost'].mean()

# Create feature using training statistics
X_train['avg_medication_cost'] = X_train['hospital'].map(train_avg)
X_test['avg_medication_cost'] = X_test['hospital'].map(train_avg)  # Apply training stats to test

# Handle new hospitals in test set (not in training)
X_test['avg_medication_cost'].fillna(train_avg.mean(), inplace=True)

# Or better: Use a custom transformer in a Pipeline!
```

---

### Case Study 3: Credit Card Fraud - The ID Leak

**Scenario:** Detecting fraudulent credit card transactions

**The Mistake:**

```python
# Load data
df = pd.read_csv('transactions.csv')

# Features include transaction_id (unique identifier)
X = df[['transaction_id', 'amount', 'merchant', 'time']]  # ← LEAKAGE!
y = df['is_fraud']

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Accuracy: 99.9%! 🎉

# Check feature importance
print(model.feature_importances_)
# Output: transaction_id has 0.95 importance! ← Problem!
```

**Why it's wrong:**
- `transaction_id` is unique per transaction, should be random
- But if dataset has pattern (e.g., fraud transactions have IDs in a certain range), model learns that
- In production, IDs won't follow the same pattern → Model fails

**Impact:**
- Development: 99.9% accuracy
- Production: 48% recall (missed most fraud!)

**The Fix:**

```python
# Remove ID features before training
X = df[['amount', 'merchant', 'time', 'location']]  # No IDs!
y = df['is_fraud']

# Train
model.fit(X_train, y_train)

# Accuracy: 92% (realistic)
# Feature importances make sense now
```

**Lesson:** Always check feature importances! IDs should never be predictive.

---

## Advanced Leakage Scenarios

### Scenario 1: Leakage Through Data Collection Process

**Example:** Website A/B test

**The Problem:**

```python
# Data collected:
# Control group shown on Mondays
# Treatment group shown on Tuesdays

df['day_of_week'] = ...  # Feature includes this pattern

# Model learns: Monday → Control → Lower conversion
#              Tuesday → Treatment → Higher conversion

# But in production, both groups shown on all days → Model fails
```

**The Fix:**
- Be aware of data collection biases
- Features should not encode the randomization process
- Use stratified sampling to ensure balance

---

### Scenario 2: Leakage Through Label Encoding Order

**The Problem:**

```python
from sklearn.preprocessing import LabelEncoder

# Target: ['low', 'medium', 'high']
# LabelEncoder assigns: high=0, low=1, medium=2 (alphabetical)

# If you use these numbers as ordinal (0 < 1 < 2), that's wrong!
# 'high' (0) < 'low' (1) is backwards
```

**The Fix:**
- Use `OrdinalEncoder` with explicit ordering
- Or use `OneHotEncoder` for nominal categories

---

### Scenario 3: Leakage Through Feature Interactions

**The Problem:**

```python
# Predict: Will customer buy product?
# Feature 1: customer_lifetime_value (CLV)
# Feature 2: number_of_purchases

# But CLV is calculated FROM purchases!
# If someone bought (y=1), their CLV is high
# Feature 2 leaks into Feature 1
```

**The Fix:**
- Only use CLV calculated BEFORE the current purchase
- Or exclude target-derived features entirely

---

## Quick Reference

### Leakage Prevention Checklist (1-Page)

```
═══════════════════════════════════════════════════════════
DATA LEAKAGE PREVENTION CHECKLIST
═══════════════════════════════════════════════════════════

BEFORE TRAINING:
□ Split data FIRST, preprocess AFTER
□ Remove duplicate rows before split
□ Remove ID columns (transaction_id, row_number, etc.)
□ Check features: Are they available at prediction time?

DURING PREPROCESSING:
□ Use Pipeline for ALL transformations
□ Fit transformers on training data only
□ Never use df.fillna(df.mean()) before split
□ Never calculate statistics from entire dataset

DURING CROSS-VALIDATION:
□ Use cross_val_score(pipeline, X, y) - NOT cross_val_score(model, X_preprocessed, y)
□ Use TimeSeriesSplit for time series
□ Use StratifiedKFold for imbalanced classification
□ Use GroupKFold for grouped data

DURING HYPERPARAMETER TUNING:
□ Use GridSearchCV with separate test set
□ OR use nested cross-validation
□ Never report CV score from GridSearchCV as final score

VALIDATION:
□ Check: CV score ≈ Test score? (Gap < 0.05)
□ Check: Performance realistic for problem domain?
□ Check: Feature importances make sense?
□ Check: No suspicious features (IDs, future info)?

═══════════════════════════════════════════════════════════
```

---

### Pipeline Quick Reference

```python
# ============= BASIC PIPELINE =============
from sklearn.pipeline import Pipeline

pipeline = Pipeline([
    ('preprocessing_step_1', Transformer1()),
    ('preprocessing_step_2', Transformer2()),
    ('model', Estimator())
])

pipeline.fit(X_train, y_train)
pipeline.predict(X_test)

# ============= COLUMN TRANSFORMER =============
from sklearn.compose import ColumnTransformer

preprocessor = ColumnTransformer([
    ('numeric', numeric_pipeline, numeric_columns),
    ('categorical', categorical_pipeline, categorical_columns)
])

pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('model', model)
])

# ============= GRIDSEARCHCV =============
from sklearn.model_selection import GridSearchCV

param_grid = {
    'model__param1': [value1, value2],
    'model__param2': [value1, value2]
}

grid = GridSearchCV(pipeline, param_grid, cv=5)
grid.fit(X_train, y_train)

print(grid.best_params_)
print(grid.best_score_)
```

---

## Summary

**Data leakage is the #1 cause of production ML failures.**

**Prevention is simple:**
1. **Split first**, preprocess after
2. **Use Pipeline** for all transformations
3. **Check feature importances** for suspicious patterns
4. **Validate realistically**: CV score should match test score
5. **Think**: "Will this feature exist at prediction time?"

**Red flags:**
- ⚠️ Accuracy too good to be true
- ⚠️ Large gap between CV and test scores
- ⚠️ ID features have high importance
- ⚠️ Using future information
- ⚠️ Preprocessing before splitting

**Remember:** An honest 80% accuracy is infinitely better than a leaky 95% accuracy that fails in production! 🛡️
