# Week 4 sklearn Cheat Sheet

**Quick reference for Pipeline, ColumnTransformer, Cross-Validation, and GridSearchCV**

---

## 1. Cross-Validation

### Basic Cross-Validation
```python
from sklearn.model_selection import cross_val_score

# Simple k-fold CV
scores = cross_val_score(model, X, y, cv=5)
print(f"CV Score: {scores.mean():.3f} ± {scores.std():.3f}")
```

### Stratified Cross-Validation (for classification)
```python
from sklearn.model_selection import StratifiedKFold, cross_val_score

# For imbalanced classes
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=cv)
print(f"Stratified CV: {scores.mean():.3f} ± {scores.std():.3f}")
```

### Multiple Metrics
```python
from sklearn.model_selection import cross_validate

# Get multiple scores at once
scoring = ['accuracy', 'precision', 'recall', 'f1']
results = cross_validate(model, X, y, cv=5, scoring=scoring)

print(f"Accuracy: {results['test_accuracy'].mean():.3f}")
print(f"Precision: {results['test_precision'].mean():.3f}")
print(f"Recall: {results['test_recall'].mean():.3f}")
print(f"F1: {results['test_f1'].mean():.3f}")
```

---

## 2. GridSearchCV

### Basic GridSearchCV Template
```python
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

# Define parameter grid
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [5, 10, 20, None],
    'min_samples_split': [2, 5, 10]
}

# Create GridSearchCV
grid = GridSearchCV(
    estimator=RandomForestClassifier(random_state=42),
    param_grid=param_grid,
    cv=5,                    # 5-fold cross-validation
    scoring='accuracy',       # Can be 'f1', 'roc_auc', etc.
    n_jobs=-1,               # Use all CPU cores
    verbose=1                # Show progress
)

# Fit (tries all combinations)
grid.fit(X_train, y_train)

# Get results
print(f"Best parameters: {grid.best_params_}")
print(f"Best CV score: {grid.best_score_:.3f}")
print(f"Test score: {grid.score(X_test, y_test):.3f}")

# Use best model
best_model = grid.best_estimator_
predictions = best_model.predict(X_test)
```

### GridSearchCV with Multiple Models
```python
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

# Compare different algorithms
models = {
    'Logistic Regression': LogisticRegression(max_iter=1000),
    'Decision Tree': DecisionTreeClassifier(random_state=42),
    'Random Forest': RandomForestClassifier(random_state=42)
}

param_grids = {
    'Logistic Regression': {'C': [0.01, 0.1, 1, 10]},
    'Decision Tree': {'max_depth': [5, 10, 20]},
    'Random Forest': {'n_estimators': [50, 100], 'max_depth': [10, 20]}
}

results = {}
for name, model in models.items():
    grid = GridSearchCV(model, param_grids[name], cv=5, n_jobs=-1)
    grid.fit(X_train, y_train)
    results[name] = {
        'best_params': grid.best_params_,
        'cv_score': grid.best_score_,
        'test_score': grid.score(X_test, y_test)
    }

# Print comparison
for name, res in results.items():
    print(f"{name}:")
    print(f"  Best params: {res['best_params']}")
    print(f"  CV score: {res['cv_score']:.3f}")
    print(f"  Test score: {res['test_score']:.3f}\n")
```

### RandomizedSearchCV (for large parameter spaces)
```python
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint, uniform

# Define distributions instead of lists
param_dist = {
    'n_estimators': randint(50, 500),
    'max_depth': randint(5, 50),
    'min_samples_split': randint(2, 20),
    'max_features': uniform(0.1, 0.9)
}

# Random search
random_search = RandomizedSearchCV(
    RandomForestClassifier(random_state=42),
    param_distributions=param_dist,
    n_iter=50,           # Try 50 random combinations
    cv=5,
    n_jobs=-1,
    random_state=42
)

random_search.fit(X_train, y_train)
```

---

## 3. Regularization

### Ridge (L2)
```python
from sklearn.linear_model import Ridge, RidgeClassifier

# For regression
ridge_reg = Ridge(alpha=1.0)
ridge_reg.fit(X_train, y_train)

# For classification
ridge_clf = RidgeClassifier(alpha=1.0)
ridge_clf.fit(X_train, y_train)

# Tune alpha with GridSearchCV
param_grid = {'alpha': [0.001, 0.01, 0.1, 1, 10, 100]}
grid = GridSearchCV(Ridge(), param_grid, cv=5)
grid.fit(X_train, y_train)
print(f"Best alpha: {grid.best_params_['alpha']}")
```

### Lasso (L1)
```python
from sklearn.linear_model import Lasso

# For regression
lasso = Lasso(alpha=1.0)
lasso.fit(X_train, y_train)

# See feature selection
print(f"Non-zero coefficients: {np.sum(lasso.coef_ != 0)}")
print(f"Sparsity: {np.sum(lasso.coef_ == 0) / len(lasso.coef_) * 100:.1f}%")
```

### Elastic Net
```python
from sklearn.linear_model import ElasticNet

# Combines L1 + L2
elastic = ElasticNet(alpha=1.0, l1_ratio=0.5)  # 50% L1, 50% L2
elastic.fit(X_train, y_train)

# Tune both parameters
param_grid = {
    'alpha': [0.01, 0.1, 1, 10],
    'l1_ratio': [0.1, 0.5, 0.9]
}
grid = GridSearchCV(ElasticNet(), param_grid, cv=5)
grid.fit(X_train, y_train)
```

### Logistic Regression with Regularization
```python
from sklearn.linear_model import LogisticRegression

# L2 (default)
lr_l2 = LogisticRegression(penalty='l2', C=1.0, max_iter=1000)

# L1 (requires saga solver)
lr_l1 = LogisticRegression(penalty='l1', C=1.0, solver='saga', max_iter=1000)

# Elastic Net
lr_elastic = LogisticRegression(
    penalty='elasticnet',
    C=1.0,
    l1_ratio=0.5,
    solver='saga',
    max_iter=1000
)

# Tune regularization
param_grid = {
    'penalty': ['l1', 'l2'],
    'C': [0.001, 0.01, 0.1, 1, 10, 100],
    'solver': ['saga']
}
grid = GridSearchCV(LogisticRegression(max_iter=1000), param_grid, cv=5)
grid.fit(X_train, y_train)
```

**Note:** In `LogisticRegression`, `C` is the **inverse** of regularization strength.
- High C = Less regularization
- Low C = More regularization

---

## 4. Basic Pipeline

### Simple Pipeline (Scaling + Model)
```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# Create Pipeline
pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', LogisticRegression())
])

# Use like a normal model
pipe.fit(X_train, y_train)
predictions = pipe.predict(X_test)
score = pipe.score(X_test, y_test)
```

### Pipeline with Multiple Preprocessing Steps
```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression

pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('pca', PCA(n_components=10)),
    ('classifier', LogisticRegression())
])

pipe.fit(X_train, y_train)
```

### Pipeline + GridSearchCV
```python
# Create Pipeline
pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', LogisticRegression())
])

# Define parameter grid (use double underscore for pipeline steps)
param_grid = {
    'classifier__C': [0.1, 1, 10],
    'classifier__penalty': ['l1', 'l2'],
    'classifier__solver': ['saga']
}

# GridSearchCV on Pipeline
grid = GridSearchCV(pipe, param_grid, cv=5, n_jobs=-1)
grid.fit(X_train, y_train)

print(f"Best params: {grid.best_params_}")
print(f"Test score: {grid.score(X_test, y_test):.3f}")
```

**Pipeline naming:** Use `step_name__parameter_name` in param_grid

---

## 5. ColumnTransformer (Mixed Data Types)

### Basic ColumnTransformer
```python
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# Identify column types
numeric_features = ['age', 'hours_per_week', 'capital_gain']
categorical_features = ['workclass', 'education', 'marital_status']

# Create transformers
numeric_transformer = StandardScaler()
categorical_transformer = OneHotEncoder(handle_unknown='ignore')

# Combine transformers
preprocessor = ColumnTransformer([
    ('num', numeric_transformer, numeric_features),
    ('cat', categorical_transformer, categorical_features)
])

# Use in Pipeline
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier

pipe = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier())
])

pipe.fit(X_train, y_train)
```

### ColumnTransformer with Imputation + Scaling
```python
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# Define numeric preprocessing pipeline
numeric_transformer = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

# Define categorical preprocessing pipeline
categorical_transformer = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# Combine
preprocessor = ColumnTransformer([
    ('num', numeric_transformer, numeric_features),
    ('cat', categorical_transformer, categorical_features)
])

# Full pipeline
full_pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression())
])

full_pipeline.fit(X_train, y_train)
```

### Complete Production Pipeline Template
```python
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

# 1. Identify feature types
numeric_features = ['age', 'hours_per_week']
categorical_features = ['workclass', 'education']

# 2. Define transformers
numeric_transformer = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# 3. Combine with ColumnTransformer
preprocessor = ColumnTransformer([
    ('num', numeric_transformer, numeric_features),
    ('cat', categorical_transformer, categorical_features)
])

# 4. Full pipeline
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(random_state=42))
])

# 5. Hyperparameter tuning
param_grid = {
    'preprocessor__num__imputer__strategy': ['mean', 'median'],
    'classifier__n_estimators': [50, 100, 200],
    'classifier__max_depth': [10, 20, None]
}

grid_search = GridSearchCV(
    pipeline,
    param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1,
    verbose=1
)

# 6. Fit
grid_search.fit(X_train, y_train)

# 7. Evaluate
print(f"Best params: {grid_search.best_params_}")
print(f"Best CV score: {grid_search.best_score_:.3f}")
print(f"Test score: {grid_search.score(X_test, y_test):.3f}")

# 8. Save
import joblib
joblib.dump(grid_search.best_estimator_, 'production_model.pkl')
```

---

## 6. Accessing Pipeline Components

### Get pipeline step
```python
# Access a specific step
scaler = pipe.named_steps['scaler']
classifier = pipe.named_steps['classifier']

# Alternative syntax
scaler = pipe['scaler']
classifier = pipe['classifier']
```

### Get parameters
```python
# See all tunable parameters
print(pipe.get_params())

# This shows you valid names for param_grid
```

### Get feature names after ColumnTransformer
```python
# After fitting ColumnTransformer
preprocessor.fit(X_train, y_train)

# Get feature names
feature_names = preprocessor.get_feature_names_out()
print(feature_names)
```

---

## 7. Saving & Loading Pipelines

### Save entire pipeline
```python
import joblib

# Save
joblib.dump(pipe, 'my_pipeline.pkl')

# Load
loaded_pipe = joblib.load('my_pipeline.pkl')

# Use immediately (no need to retrain)
predictions = loaded_pipe.predict(X_new)
```

### Save GridSearchCV results
```python
# Save best model from GridSearchCV
joblib.dump(grid_search.best_estimator_, 'best_model.pkl')

# Save entire grid (includes all tried combinations)
joblib.dump(grid_search, 'grid_search_results.pkl')

# Load and inspect
loaded_grid = joblib.load('grid_search_results.pkl')
print(loaded_grid.cv_results_)
```

---

## 8. Common Patterns

### Pattern: Train/Validate/Test Split with CV
```python
from sklearn.model_selection import train_test_split

# Split off test set first (never touch during development)
X_temp, X_test, y_temp, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Use CV on remaining data for model selection
grid_search.fit(X_temp, y_temp)

# Final evaluation on test set
final_score = grid_search.score(X_test, y_test)
print(f"Final test score: {final_score:.3f}")
```

### Pattern: Prevent Data Leakage Checklist
```python
# ✅ CORRECT: Split first, then fit Pipeline
X_train, X_test, y_train, y_test = train_test_split(X, y)
pipe.fit(X_train, y_train)  # Pipeline handles fit_transform internally

# ❌ WRONG: Fit before split (LEAKAGE!)
scaler.fit(X)  # Uses test data!
X_scaled = scaler.transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y)
```

### Pattern: Comparing Multiple Models
```python
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

models = {
    'Logistic Regression': LogisticRegression(max_iter=1000),
    'Decision Tree': DecisionTreeClassifier(random_state=42),
    'Random Forest': RandomForestClassifier(random_state=42)
}

# Evaluate each
for name, model in models.items():
    scores = cross_val_score(model, X_train, y_train, cv=5)
    print(f"{name}: {scores.mean():.3f} ± {scores.std():.3f}")
```

---

## 9. Quick Syntax Reference

### Pipeline Syntax
```python
Pipeline([
    ('step1_name', Transformer1()),
    ('step2_name', Transformer2()),
    ('final_step', Estimator())
])
```

### ColumnTransformer Syntax
```python
ColumnTransformer([
    ('transformer1_name', transformer1, columns1),
    ('transformer2_name', transformer2, columns2)
])
```

### GridSearchCV param_grid with Pipeline
```python
# For single-level Pipeline
{'step_name__param_name': [value1, value2]}

# For nested Pipeline (ColumnTransformer inside Pipeline)
{'preprocessor__num__scaler__param': [value1, value2]}
```

---

## 10. Troubleshooting

### Error: "Expected 2D array, got 1D array"
```python
# When predicting single sample
X_single = [[value1, value2, value3]]  # Note double brackets
prediction = pipe.predict(X_single)
```

### Error: "Found unknown categories"
```python
# Use handle_unknown='ignore' in OneHotEncoder
OneHotEncoder(handle_unknown='ignore')
```

### Error: "GridSearchCV taking too long"
```python
# Reduce param_grid size
# OR use RandomizedSearchCV instead
# OR use n_jobs=-1 to parallelize
# OR reduce cv folds (cv=3 instead of cv=5)
```

### Error: "Columns don't match"
```python
# Ensure X_train and X_test have same columns
assert list(X_train.columns) == list(X_test.columns)

# If using ColumnTransformer, ensure column names are exact
numeric_features = ['age', 'hours']  # Must match DataFrame column names exactly
```

---

## 11. Production Checklist

Before deploying your model, verify:

- [ ] Split data BEFORE any preprocessing
- [ ] All preprocessing in Pipeline (no manual fit/transform)
- [ ] Cross-validation used for model selection
- [ ] GridSearchCV used for hyperparameter tuning
- [ ] Regularization considered if overfitting observed
- [ ] Final test set evaluated ONCE at the end
- [ ] Entire pipeline saved with joblib
- [ ] Pipeline tested on sample new data
- [ ] Performance acceptable for production use

---

## 12. Resources

**sklearn Documentation:**
- [Pipeline User Guide](https://scikit-learn.org/stable/modules/compose.html)
- [GridSearchCV API](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html)
- [Cross-validation Guide](https://scikit-learn.org/stable/modules/cross_validation.html)

**Cheat Sheets:**
- [sklearn Official Cheat Sheet](https://scikit-learn.org/stable/tutorial/machine_learning_map/)

---

*Keep this cheat sheet handy during exercises - it covers 90% of Week 4 syntax needs!*
