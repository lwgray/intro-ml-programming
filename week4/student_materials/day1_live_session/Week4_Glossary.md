# Week 4 Glossary: Model Selection & Avoiding Pitfalls

**Complete reference for Week 4 terminology and concepts**

---

## Cross-Validation Terms

### Cross-Validation
The process of evaluating a model's performance by training and testing on multiple different splits of the data, then averaging the results to get a more reliable performance estimate.

**Why it matters:** Single train/test splits can be misleading due to random chance. CV gives you confidence in your performance estimate.

**Example:** 5-fold CV trains 5 different models on 5 different 80/20 splits, then averages their test scores.

---

### k-Fold Cross-Validation
A specific CV strategy that divides data into k equal-sized parts (folds), then trains k models where each fold serves as the test set once.

**Common k values:** 3, 5, or 10 folds

**Tradeoff:** Higher k = more reliable estimate but slower computation

**Example:** 5-fold CV creates 5 folds, trains 5 models, produces 5 scores → report mean ± std

---

### Stratified Cross-Validation
A variant of k-fold CV that ensures each fold has the same class distribution as the overall dataset.

**When to use:** Classification problems with imbalanced classes

**Why it matters:** Prevents accidentally creating folds with very different class ratios

**sklearn function:** `StratifiedKFold(n_splits=5)`

---

### Fold
One of the k equal-sized subsets of data in k-fold cross-validation. Each fold takes a turn being the test set.

**Visual:**
```
Fold 1: [Test][Train][Train][Train][Train]
Fold 2: [Train][Test][Train][Train][Train]
Fold 3: [Train][Train][Test][Train][Train]
...
```

---

## Hyperparameter Tuning Terms

### Parameter
A value **learned** from data during training (not set beforehand).

**Examples:**
- Linear regression coefficients
- Neural network weights
- Decision tree split thresholds

**Key:** You DON'T choose these - the training algorithm does.

---

### Hyperparameter
A value **set before training** that controls the learning process or model structure.

**Examples:**
- `max_depth` in Decision Trees
- `n_estimators` in Random Forests
- `alpha` in regularized models
- `C` in Logistic Regression

**Key:** YOU choose these (or use GridSearchCV to systematically search for best values).

---

### Grid Search
An exhaustive search over a predefined set of hyperparameter values, trying every combination and selecting the one with best CV performance.

**Example:** If you have 3 values for `max_depth` and 4 values for `n_estimators`, grid search tries all 3×4=12 combinations.

**Tradeoff:** Thorough but can be slow for large grids

---

### GridSearchCV
sklearn's implementation of grid search with built-in cross-validation.

**What it does:**
1. Takes a parameter grid (all combinations to try)
2. For each combination, performs k-fold CV
3. Selects combination with highest mean CV score
4. Refits final model on all training data with best parameters

**Key attributes:**
- `best_params_`: The winning hyperparameter combination
- `best_score_`: The CV score of the best combination
- `best_estimator_`: The refitted model using best parameters

---

### Random Search
Like grid search, but randomly samples hyperparameter combinations instead of trying all of them.

**When to use:** When param_grid is too large (100+ combinations)

**Tradeoff:** Faster but less thorough than grid search

**sklearn function:** `RandomizedSearchCV(n_iter=20)`

---

### param_grid
A dictionary defining which hyperparameters to tune and what values to try for each.

**Syntax:**
```python
param_grid = {
    'max_depth': [5, 10, 20],
    'min_samples_split': [2, 5, 10]
}
# Grid search tries 3×3=9 combinations
```

---

## Regularization Terms

### Regularization
The practice of adding a penalty term to the loss function to constrain model complexity and prevent overfitting.

**Analogy:** Like a speed limit for models - prevents them from being too complex and "memorizing" training data.

**Effect:** Reduces training accuracy but improves test accuracy (generalization)

---

### L1 Regularization (Lasso)
Adds a penalty proportional to the **absolute value** of coefficients.

**Effect:** Sets many coefficients to **exactly zero** (performs automatic feature selection)

**When to use:** When you have many features and want to select the most important ones

**sklearn classes:** `Lasso`, `LogisticRegression(penalty='l1')`

**Math:** Loss = Prediction Error + α × Σ|coefficients|

---

### L2 Regularization (Ridge)
Adds a penalty proportional to the **square** of coefficients.

**Effect:** Shrinks all coefficients toward zero but rarely sets them to exactly zero

**When to use:** Default choice - when you think most features are relevant

**sklearn classes:** `Ridge`, `LogisticRegression(penalty='l2')`

**Math:** Loss = Prediction Error + α × Σ(coefficients²)

---

### Lasso
Linear regression or classification with L1 regularization.

**Key feature:** Automatic feature selection through sparsity

**sklearn:** `Lasso(alpha=1.0)` for regression

---

### Ridge
Linear regression or classification with L2 regularization.

**Key feature:** Handles multicollinearity well by shrinking correlated features together

**sklearn:** `Ridge(alpha=1.0)` for regression

---

### Elastic Net
Combines L1 and L2 regularization, offering a balance between feature selection and coefficient shrinkage.

**Parameters:**
- `alpha`: Overall regularization strength
- `l1_ratio`: Balance between L1 and L2 (0=pure L2, 1=pure L1, 0.5=equal mix)

**When to use:** When features are correlated and you want some feature selection

**sklearn:** `ElasticNet(alpha=1.0, l1_ratio=0.5)`

---

### Alpha (α)
The regularization strength parameter in Ridge, Lasso, and Elastic Net.

**Higher alpha** = Stronger penalty = Simpler model = More regularization
**Lower alpha** = Weaker penalty = More complex model = Less regularization

**Range:** Typically between 0.001 and 100

**Tuning:** Use GridSearchCV to find optimal value

**Warning:** In `LogisticRegression`, sklearn uses `C` (inverse of alpha) instead!

---

### C Parameter
The **inverse** of regularization strength in `LogisticRegression` and `SVC`.

**Higher C** = LESS regularization = More complex model
**Lower C** = MORE regularization = Simpler model

**Confusing!** C is the opposite of alpha. Always check documentation!

---

## Data Leakage Terms

### Data Leakage
Using information during training that will **not be available** at prediction time in production, resulting in falsely inflated performance estimates.

**Analogy:** Like studying with tomorrow's exam answers - you'll ace the practice test but fail the real exam.

**Common causes:**
- Fitting preprocessing on entire dataset before splitting
- Including target-derived features
- Using future information to predict the past

**Detection:** Test accuracy >> expected, or model fails in production despite good CV scores

---

### Target Leakage
A specific type of data leakage where features are derived from (or directly include) the target variable.

**Example:** Predicting loan default but including "late_payment_flag" as a feature (late payments only occur AFTER default)

**How to avoid:** Carefully audit features - ask "Will this be known at prediction time?"

---

### Temporal Leakage
Using information from the future to predict the past in time-series data.

**Example:** Training on 2024 data to predict 2023 outcomes

**How to avoid:** Use `TimeSeriesSplit` instead of random splitting

---

### Train/Test Contamination
When test set information influences training, most commonly through preprocessing.

**Example:**
```python
# BAD - test data contamination
scaler.fit(X_all)  # Uses test set!
X_train, X_test = train_test_split(X_all)
```

**Solution:** Always split BEFORE fitting any preprocessing

---

## Pipeline Terms

### Pipeline
An sklearn object that chains together multiple preprocessing steps and a final estimator, ensuring correct fit/transform order and preventing data leakage.

**Structure:** List of (name, transformer/estimator) tuples

**Syntax:**
```python
Pipeline([
    ('step1_name', Transformer1()),
    ('step2_name', Transformer2()),
    ('estimator_name', Estimator())
])
```

**Key benefit:** Impossible to accidentally leak information from test set

---

### ColumnTransformer
An sklearn object that applies different transformations to different columns (features).

**Use case:** When you have mixed data types (numeric + categorical) requiring different preprocessing

**Syntax:**
```python
ColumnTransformer([
    ('numeric', numeric_transformer, numeric_columns),
    ('categorical', categorical_transformer, categorical_columns)
])
```

---

### Transformer
Any sklearn object that has `fit()` and `transform()` methods.

**Examples:**
- `StandardScaler`
- `OneHotEncoder`
- `SimpleImputer`
- `PCA`

**Usage in Pipeline:**
- During training: `fit_transform()` called on training data
- During prediction: `transform()` called on new data (using parameters learned from training)

---

### Estimator
An sklearn object that has `fit()` and `predict()` methods (the final model in a pipeline).

**Examples:**
- `LogisticRegression`
- `RandomForestClassifier`
- `Ridge`
- `SVC`

**Position in Pipeline:** Always the last step

---

### fit_transform()
Method that **learns** parameters from data (fit) AND applies the transformation (transform) in one step.

**When to use:** ONLY on training data in manual preprocessing

**In Pipeline:** Automatically called on training data for all transformer steps

---

### transform()
Method that applies a transformation using **already-learned** parameters.

**When to use:** On test data or new data after fitting on training data

**Key:** Does NOT relearn parameters - uses statistics from original fit

**In Pipeline:** Automatically called on test/new data

---

### make_pipeline()
A convenience function that creates a Pipeline without requiring you to name each step.

**Comparison:**
```python
# Explicit names
Pipeline([('scaler', StandardScaler()), ('lr', LogisticRegression())])

# Auto-generated names
make_pipeline(StandardScaler(), LogisticRegression())
```

**When to use:** Quick prototyping (but explicit names better for GridSearchCV)

---

## Advanced CV Terms

### Nested Cross-Validation
A two-layer CV strategy: outer loop estimates model performance, inner loop selects hyperparameters.

**Purpose:** Prevents overfitting to the validation set during hyperparameter tuning

**When to use:** When you want an unbiased estimate of how well GridSearchCV generalizes

**Structure:**
- Outer loop: 5-fold CV for performance estimation
- Inner loop: GridSearchCV for hyperparameter selection (on each outer fold)

---

### Leave-One-Out Cross-Validation (LOOCV)
Extreme case of k-fold CV where k = number of samples (each fold has 1 test sample).

**Pros:** Maximum use of training data
**Cons:** Extremely slow, high variance

**When to use:** Very small datasets (<100 samples) where you can't afford to hold out data

**Recommendation:** Usually better to use k=5 or k=10

---

### TimeSeriesSplit
A CV strategy for time-series data that respects temporal order.

**How it works:** Each fold trains on past data and tests on future data (no shuffling)

**Example:**
```
Fold 1: [Train: 2020] [Test: 2021]
Fold 2: [Train: 2020-2021] [Test: 2022]
Fold 3: [Train: 2020-2022] [Test: 2023]
```

**When to use:** Any time-ordered data (stock prices, weather, user behavior over time)

---

## Workflow Terms

### Production Pipeline
A complete ML workflow that is ready for deployment in a real-world system.

**Must include:**
1. Data validation
2. Preprocessing (in Pipeline)
3. Model training
4. Performance monitoring
5. Leakage prevention
6. Version control

**Week 4 focus:** Items 2, 3, 5

---

### Model Persistence
Saving a trained model to disk so it can be loaded and used later without retraining.

**sklearn tool:** `joblib`

**Syntax:**
```python
import joblib
joblib.dump(model, 'model.pkl')  # Save
loaded_model = joblib.load('model.pkl')  # Load
```

**Best practice:** Save the entire Pipeline, not just the final estimator

---

### Production-Ready
A model that has been rigorously validated and is suitable for deployment in a real-world system.

**Checklist:**
- ✅ Cross-validation performed
- ✅ Hyperparameters tuned with GridSearchCV
- ✅ Regularization applied if needed
- ✅ Pipeline prevents data leakage
- ✅ Performance tested on held-out test set
- ✅ Model saved with joblib
- ✅ Edge cases handled

---

## Comparison: Key Distinctions

### Parameter vs Hyperparameter
| Parameter | Hyperparameter |
|-----------|----------------|
| Learned during training | Set before training |
| E.g., coefficients | E.g., max_depth |
| Optimized by algorithm | Optimized by you (or GridSearchCV) |

---

### L1 vs L2 Regularization
| L1 (Lasso) | L2 (Ridge) |
|------------|------------|
| Absolute value penalty | Squared penalty |
| Sets coefficients to zero | Shrinks coefficients |
| Feature selection | Keeps all features |
| Sparse models | Dense models |
| Use when: many irrelevant features | Use when: most features useful |

---

### fit_transform() vs transform()
| fit_transform() | transform() |
|-----------------|-------------|
| Learn + apply | Just apply |
| Use on training data | Use on test/new data |
| Calculates statistics | Uses stored statistics |
| Example: learn mean/std + scale | Example: scale using learned mean/std |

---

### GridSearchCV vs RandomizedSearchCV
| GridSearchCV | RandomizedSearchCV |
|--------------|-------------------|
| Tries ALL combinations | Tries RANDOM sample |
| Exhaustive | Probabilistic |
| Slower | Faster |
| Use when: small param_grid | Use when: large param_grid |

---

### Cross-Validation vs Test Set
| Cross-Validation | Test Set |
|------------------|----------|
| Multiple train/test splits | Single train/test split |
| For model selection/tuning | For final evaluation |
| Used during development | Used once at the end |
| Touches all data (in rotation) | Never seen during training |

---

## Common Acronyms

- **CV:** Cross-Validation
- **LOOCV:** Leave-One-Out Cross-Validation
- **L1:** Lasso regularization (absolute penalty)
- **L2:** Ridge regularization (squared penalty)
- **MSE:** Mean Squared Error
- **MAE:** Mean Absolute Error
- **RMSE:** Root Mean Squared Error
- **R²:** R-squared (coefficient of determination)

---

## Quick Reference: When to Use What

**Imbalanced classification?** → Use `StratifiedKFold`

**Many features, want feature selection?** → Use L1 (Lasso)

**Default regularization?** → Use L2 (Ridge)

**Correlated features?** → Use Elastic Net

**Large param_grid (100+ combos)?** → Use `RandomizedSearchCV`

**Time-series data?** → Use `TimeSeriesSplit`

**Mixed numeric/categorical data?** → Use `ColumnTransformer`

**Prevent data leakage?** → ALWAYS use `Pipeline`

---

## Resources for Deeper Learning

**StatQuest Videos:**
- Cross-Validation Explained
- Regularization (Ridge, Lasso, Elastic Net)
- Bias-Variance Tradeoff

**sklearn Documentation:**
- [Pipeline User Guide](https://scikit-learn.org/stable/modules/compose.html)
- [Cross-validation Guide](https://scikit-learn.org/stable/modules/cross_validation.html)
- [GridSearchCV API](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html)

**Books:**
- *Hands-On Machine Learning* (Aurélien Géron) - Chapter 2
- *Introduction to Statistical Learning* (James et al.) - Chapter 5

---

*This glossary covers all Week 4 terminology. Bookmark for quick reference during exercises!*
