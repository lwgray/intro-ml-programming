# Week 4 Student Workbook: Model Selection & Avoiding Pitfalls

**Date:** ____________
**Name:** ____________

---

## Session Overview

**Four Pillars of Production ML:**
1. Cross-Validation
2. GridSearchCV (Hyperparameter Tuning)
3. Regularization
4. Pipeline (Data Leakage Prevention)

---

## Segment 1: Week 3 Recap (0:00-0:15)

### Quick Recall

**Q: What three algorithms did we learn in Week 3?**

1. _______________________
2. _______________________
3. _______________________

**Q: What's the difference between bagging and boosting?**

_________________________________________________________________

_________________________________________________________________

### Today's Big Shift

**Week 3:** _How do algorithms work?_ (Understanding mechanisms)

**Week 4:** _How do I build TRUSTWORTHY models?_ (Methodology)

---

## Segment 2: Cross-Validation (0:15-0:45)

### The Dating Analogy

"Would you marry someone after one date?"

**Why not?**

_________________________________________________________________

_________________________________________________________________

**Connection to ML:**

_________________________________________________________________

_________________________________________________________________

### Single Split Problem

**Demo observation:** Same model, same data, 10 different random splits gave:
- Lowest accuracy: ___________
- Highest accuracy: ___________
- Range: ___________ (this is the problem!)

### k-Fold Cross-Validation

**How it works:**

1. _________________________________________________________________

2. _________________________________________________________________

3. _________________________________________________________________

4. _________________________________________________________________

5. _________________________________________________________________

**Key code:**
```python
from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, X, y, cv=______)
print(f"CV: {scores.mean():.3f} ± {scores.std():.3f}")
```

### Stratified CV

**When to use:** _________________________________________________________________

**Key code:**
```python
from sklearn.model_selection import StratifiedKFold

stratified_cv = StratifiedKFold(n_splits=______, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=stratified_cv)
```

---

## Segment 3: Hyperparameter Tuning (0:45-1:15)

### Parameters vs Hyperparameters

**Parameters:** _________________________________________________________________
- Examples: _________________________________________________________________

**Hyperparameters:** _________________________________________________________________
- Examples: _________________________________________________________________

### Manual Tuning Problem

**Why manual tuning is tedious:**

1. _________________________________________________________________

2. _________________________________________________________________

3. _________________________________________________________________

### GridSearchCV Solution

**What it does:**

_________________________________________________________________

_________________________________________________________________

**Key code:**
```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    'max_depth': [______, ______, ______],
    'min_samples_split': [______, ______, ______]
}

grid_search = GridSearchCV(
    estimator=______,
    param_grid=______,
    cv=______,
    scoring=______,
    n_jobs=-1
)

grid_search.fit(X_train, y_train)

print(f"Best params: {grid_search.best_params_}")
print(f"Best CV score: {grid_search.best_score_:.3f}")
```

**Results from demo:**
- Best max_depth: ______
- Best min_samples_split: ______
- Best CV score: ______

---

## Segment 4: BREAK (1:15-1:30)

*Stretch, hydrate, prepare for second half!*

---

## Segment 5: Regularization (1:30-1:55)

### Purpose of Regularization

**Problem:** _________________________________________________________________

**Solution:** _________________________________________________________________

### Three Types

**1. L1 (Lasso):**
- Penalty type: _________________________________________________________________
- Effect: _________________________________________________________________
- Use when: _________________________________________________________________

**2. L2 (Ridge):**
- Penalty type: _________________________________________________________________
- Effect: _________________________________________________________________
- Use when: _________________________________________________________________

**3. Elastic Net:**
- Combination: _________________________________________________________________
- Use when: _________________________________________________________________

### Alpha Parameter

**What it controls:** _________________________________________________________________

**Effect of values:**
- alpha = 0: _________________________________________________________________
- alpha = small (0.01-0.1): _________________________________________________________________
- alpha = large (10-100): _________________________________________________________________

**Key code:**
```python
from sklearn.linear_model import Ridge, Lasso, ElasticNet

ridge = Ridge(alpha=______)
lasso = Lasso(alpha=______)
elastic = ElasticNet(alpha=______, l1_ratio=______)
```

---

## Segment 6: Data Leakage (1:55-2:20)

### What is Data Leakage?

**Definition:** _________________________________________________________________

_________________________________________________________________

### Common Leakage Scenarios

**1. Scaling before splitting:**
```python
# WRONG - causes leakage!
X_scaled = scaler.fit_transform(X)  # Scaler sees ALL data
X_train, X_test = train_test_split(X_scaled, y)

# RIGHT - no leakage
X_train, X_test, y_train, y_test = train_test_split(X, y)
scaler.fit(X_train)  # Scaler only sees training data
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

**2. Other leakage sources:**

- _________________________________________________________________

- _________________________________________________________________

- _________________________________________________________________

### Pipeline Solution

**What Pipeline does:** _________________________________________________________________

_________________________________________________________________

**Key benefit:** _________________________________________________________________

**Basic Pipeline structure:**
```python
from sklearn.pipeline import Pipeline

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression())
])

pipeline.fit(X_train, y_train)  # Fits scaler + model on train only
pipeline.predict(X_test)  # Transforms test using train stats, then predicts
```

---

## Segment 7: Live Coding - Complete Pipeline (2:20-2:40)

### ColumnTransformer (for mixed data types)

**Purpose:** _________________________________________________________________

**Structure:**
```python
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

numeric_features = [______, ______, ______]
categorical_features = [______, ______, ______]

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(drop='first', handle_unknown='ignore'), categorical_features)
    ]
)
```

### Complete Production Pipeline

**Full structure:**
```python
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression())
])
```

### GridSearchCV on Pipeline

**Hyperparameter naming:** `stepname__parametername`

**Example:**
```python
param_grid = {
    'classifier__C': [______, ______, ______],
    'classifier__penalty': [______, ______]
}

grid_search = GridSearchCV(pipeline, param_grid, cv=5)
grid_search.fit(X_train, y_train)
```

**Results from demo:**
- Best C: ______
- Best penalty: ______
- Best CV score: ______
- Test score: ______

### Saving/Loading Pipeline

**Save:**
```python
import joblib

joblib.dump(grid_search.best_estimator_, 'model_pipeline.pkl')
```

**Load:**
```python
loaded_pipeline = joblib.load('model_pipeline.pkl')
predictions = loaded_pipeline.predict(new_data)
```

---

## Segment 8: Pair Programming (2:40-2:55)

### "Data Leakage Detective" Exercise

**Partner name:** ____________

**Leakage bugs found:**

1. _________________________________________________________________

2. _________________________________________________________________

3. _________________________________________________________________

4. _________________________________________________________________

5. _________________________________________________________________

**Fix applied:** _________________________________________________________________

---

## Segment 9: Wrap-up (2:55-3:00)

### Production ML Checklist

- [ ] Use cross-validation (NOT single split)
- [ ] Tune hyperparameters with GridSearchCV
- [ ] Apply regularization to prevent overfitting
- [ ] Use Pipeline to prevent data leakage
- [ ] Save trained pipeline with joblib

### Key Takeaways

**Most important lesson from today:**

_________________________________________________________________

_________________________________________________________________

### Questions for Office Hours

_________________________________________________________________

_________________________________________________________________

---

## Post-Class Action Items

- [ ] Complete post-class exercise (build complete pipeline from scratch)
- [ ] Review Pipeline syntax (it's the new standard!)
- [ ] Try bonus exercise (nested CV for advanced students)
- [ ] Complete self-assessment
- [ ] Post questions in course forum

---

*Remember: Production ML is 20% algorithm choice, 80% methodology!*
