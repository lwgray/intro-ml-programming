# Week 4 Self-Assessment

**Check your understanding of Model Selection & Avoiding Pitfalls**

---

## How to Use This Self-Assessment

1. **Answer each question** honestly without looking at notes first
2. **Check your answers** against the answer key at the bottom
3. **Revisit materials** for any topics you struggled with
4. **Target:** 80%+ correct on each section before moving to Week 5

---

## Section 1: Cross-Validation (8 questions)

### Question 1.1
**Why is a single train/test split unreliable?**

A) It wastes too much data
B) Performance can vary significantly based on random split
C) It takes too long to compute
D) sklearn doesn't support it

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 1.2
**In 5-fold cross-validation, how many models are trained?**

A) 1 model
B) 5 models
C) 10 models
D) It depends on the dataset size

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 1.3
**What does `cross_val_score(model, X, y, cv=5)` return?**

A) A single accuracy score
B) An array of 5 scores (one per fold)
C) The best model
D) A confusion matrix

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 1.4
**When should you use StratifiedKFold instead of regular KFold?**

A) When you have regression problems
B) When you have imbalanced classification
C) When your dataset is very large
D) Never - regular KFold is always better

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 1.5
**What does it mean if CV scores are: [0.82, 0.84, 0.81, 0.83, 0.85]?**

A) The model is overfitting
B) The model performance is stable across folds
C) There's data leakage
D) The model is underfitting

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 1.6
**Complete this code to perform stratified 5-fold CV:**
```python
from sklearn.model_selection import ______, cross_val_score

cv = ______(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=______)
```

<details>
<summary>Your Answer:</summary>
</details>

---

### Question 1.7
**True or False: You should use cross-validation on your final test set to get a better performance estimate.**

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 1.8
**How do you report CV results professionally?**

A) "My model got 85% accuracy"
B) "My model got 0.850 ± 0.012 across 5 folds"
C) "My model scored well"
D) "Accuracy: 85.0%"

<details>
<summary>Your Answer: _____</summary>
</details>

---

## Section 2: Hyperparameter Tuning (7 questions)

### Question 2.1
**What's the difference between a parameter and a hyperparameter?**

A) Parameters are tuned, hyperparameters are learned
B) Parameters are learned, hyperparameters are set before training
C) They're the same thing
D) Parameters are for regression, hyperparameters for classification

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 2.2
**What does GridSearchCV do?**

A) Searches for the best dataset
B) Tries all combinations of hyperparameters and selects the best via CV
C) Tunes parameters during training
D) Visualizes model performance

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 2.3
**If param_grid has 3 values for `max_depth` and 4 values for `n_estimators`, how many total combinations will GridSearchCV try?**

A) 3
B) 4
C) 7 (3+4)
D) 12 (3×4)

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 2.4
**After running GridSearchCV, how do you access the best hyperparameters?**

A) `grid.best_model`
B) `grid.best_params_`
C) `grid.parameters`
D) `grid.get_best()`

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 2.5
**When should you use RandomizedSearchCV instead of GridSearchCV?**

A) When you have a small param_grid
B) When you have a very large param_grid (100+ combinations)
C) Never - GridSearchCV is always better
D) Only for deep learning

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 2.6
**Complete this GridSearchCV code:**
```python
from sklearn.model_selection import GridSearchCV

param_grid = {'max_depth': [5, 10, 20]}
grid = GridSearchCV(______, ______, cv=5)
grid.______(X_train, y_train)
print(f"Best params: {______}")
```

<details>
<summary>Your Answer:</summary>
</details>

---

### Question 2.7
**True or False: GridSearchCV automatically refits the best model on all training data after finding optimal hyperparameters.**

<details>
<summary>Your Answer: _____</summary>
</details>

---

## Section 3: Regularization (8 questions)

### Question 3.1
**What is the purpose of regularization?**

A) To increase model complexity
B) To prevent overfitting by constraining model complexity
C) To speed up training
D) To improve data quality

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 3.2
**What's the main difference between L1 (Lasso) and L2 (Ridge) regularization?**

A) L1 sets many coefficients to zero; L2 shrinks all coefficients
B) L2 sets coefficients to zero; L1 shrinks them
C) They're the same
D) L1 is for regression, L2 for classification

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 3.3
**When should you use L1 (Lasso) regularization?**

A) Always
B) When you want automatic feature selection
C) When you have few features
D) Never

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 3.4
**In Ridge/Lasso, what does the alpha parameter control?**

A) Learning rate
B) Regularization strength (higher = more penalty)
C) Number of features
D) Training speed

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 3.5
**In LogisticRegression, what does the C parameter represent?**

A) Regularization strength (higher = more penalty)
B) Inverse of regularization (higher = LESS penalty)
C) Number of classes
D) Convergence threshold

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 3.6
**What is Elastic Net?**

A) A neural network architecture
B) A combination of L1 and L2 regularization
C) A type of cross-validation
D) A data preprocessing technique

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 3.7
**True or False: Regularization typically decreases training accuracy but improves test accuracy.**

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 3.8
**Which sklearn class implements L2 regularization for regression?**

A) `Lasso`
B) `Ridge`
C) `ElasticNet`
D) `LinearRegression`

<details>
<summary>Your Answer: _____</summary>
</details>

---

## Section 4: Data Leakage (10 questions)

### Question 4.1
**What is data leakage?**

A) When your model leaks memory
B) Using information during training that won't be available at prediction time
C) When data is corrupted
D) When the test set is too small

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 4.2
**Which code has data leakage?**

A)
```python
X_train, X_test = train_test_split(X)
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

B)
```python
scaler.fit(X)
X_scaled = scaler.transform(X)
X_train, X_test = train_test_split(X_scaled)
```

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 4.3
**What's the difference between `fit_transform()` and `transform()`?**

A) They're the same
B) `fit_transform()` learns parameters AND transforms; `transform()` just transforms
C) `transform()` is faster
D) `fit_transform()` is for training, `transform()` for testing

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 4.4
**When should you use `fit_transform()`?**

A) On both training and test data
B) Only on training data
C) Only on test data
D) Never

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 4.5
**How does sklearn Pipeline prevent data leakage?**

A) It splits the data automatically
B) It enforces correct fit/transform order, making leakage impossible
C) It uses encryption
D) It doesn't - you still need to be careful

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 4.6
**True or False: You should always split your data BEFORE any preprocessing.**

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 4.7
**What's a red flag that indicates possible data leakage?**

A) Training accuracy is 70%
B) Test accuracy significantly exceeds training accuracy
C) Model trains quickly
D) Cross-validation shows high variance

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 4.8
**Which of these causes leakage?**

A) Using `transform()` on test data
B) Using `fit_transform()` on all data before splitting
C) Splitting data before preprocessing
D) Using cross-validation

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 4.9
**In a Pipeline, what happens when you call `pipe.fit(X_train, y_train)`?**

A) All steps use `transform()` on training data
B) All steps use `fit_transform()` on training data, then final estimator uses `fit()`
C) Only the final estimator is fitted
D) Nothing - you need to fit each step manually

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 4.10
**Complete this leakage-free preprocessing:**
```python
# Split first
X_train, X_test, y_train, y_test = train_test_split(X, y)

# Fit scaler
scaler = StandardScaler()
X_train_scaled = scaler.______(X_train)  # fit_transform or transform?
X_test_scaled = scaler.______(X_test)     # fit_transform or transform?
```

<details>
<summary>Your Answer:</summary>
</details>

---

## Section 5: Pipeline (10 questions)

### Question 5.1
**What is a sklearn Pipeline?**

A) A way to parallelize training
B) A container that chains preprocessing steps + final estimator
C) A data visualization tool
D) A hyperparameter tuning method

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 5.2
**What's the correct Pipeline syntax?**

A) `Pipeline({'scaler': StandardScaler(), 'model': LogisticRegression()})`
B) `Pipeline([StandardScaler(), LogisticRegression()])`
C) `Pipeline([('scaler', StandardScaler()), ('model', LogisticRegression())])`
D) `Pipeline(StandardScaler() + LogisticRegression())`

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 5.3
**What must be the last step in a Pipeline?**

A) A scaler
B) An imputer
C) An estimator (model)
D) It doesn't matter

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 5.4
**What does ColumnTransformer do?**

A) Renames columns
B) Applies different transformations to different columns
C) Selects the best columns
D) Converts column types

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 5.5
**How do you access a specific step in a Pipeline?**

A) `pipe.steps[0]`
B) `pipe['step_name']` or `pipe.named_steps['step_name']`
C) `pipe.get_step('step_name')`
D) `pipe.step_name`

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 5.6
**How do you specify Pipeline hyperparameters in GridSearchCV?**

A) `{'max_depth': [5, 10]}`
B) `{'classifier__max_depth': [5, 10]}`
C) `{'step1.max_depth': [5, 10]}`
D) `{'params': {'max_depth': [5, 10]}}`

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 5.7
**Complete this Pipeline:**
```python
from sklearn.pipeline import Pipeline

pipe = Pipeline([
    ('scaler', ______),
    ('classifier', ______)
])
```

<details>
<summary>Your Answer:</summary>
</details>

---

### Question 5.8
**Complete this ColumnTransformer:**
```python
from sklearn.compose import ColumnTransformer

preprocessor = ColumnTransformer([
    ('num', numeric_transformer, ______),
    ('cat', categorical_transformer, ______)
])
```

<details>
<summary>Your Answer:</summary>
</details>

---

### Question 5.9
**True or False: You can use GridSearchCV on a Pipeline to tune preprocessing AND model hyperparameters simultaneously.**

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 5.10
**How do you save a trained Pipeline?**

A) `pipeline.save('model.pkl')`
B) `joblib.dump(pipeline, 'model.pkl')`
C) `pickle.save(pipeline)`
D) Pipelines can't be saved

<details>
<summary>Your Answer: _____</summary>
</details>

---

## Section 6: Practical Application (5 questions)

### Question 6.1
**You have a dataset with 5000 samples. What's a reasonable k value for cross-validation?**

A) k=2
B) k=5 or k=10
C) k=100
D) k=5000 (LOOCV)

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 6.2
**Your model has training accuracy 95% and test accuracy 98%. What's likely happening?**

A) Perfect model
B) Overfitting
C) Data leakage
D) Underfitting

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 6.3
**You have 200 features. Which regularization should you try first?**

A) No regularization
B) L1 (Lasso) for automatic feature selection
C) L2 (Ridge)
D) Elastic Net

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 6.4
**Your GridSearchCV has been running for 3 hours on a small dataset. What's likely wrong?**

A) Your computer is slow
B) Your param_grid is too large
C) You didn't set n_jobs=-1
D) Both B and C

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 6.5
**What's the correct workflow for production ML?**

A) Train → Test → Deploy
B) Split → Preprocess → Train → Test → Deploy
C) Split → Build Pipeline → GridSearchCV → Evaluate on Test → Save → Deploy
D) Preprocess → Split → Train → Deploy

<details>
<summary>Your Answer: _____</summary>
</details>

---

## Section 7: Code Debugging (3 questions)

### Question 7.1
**What's wrong with this code?**
```python
from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, X_test, y_test, cv=5)
```

<details>
<summary>Your Answer:</summary>
</details>

---

### Question 7.2
**What's wrong with this code?**
```python
pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('pca', PCA()),
    ('selector', SelectKBest()),
    ('lr', LogisticRegression())
])
```

<details>
<summary>Your Answer:</summary>
</details>

---

### Question 7.3
**What's wrong with this code?**
```python
scaler = StandardScaler()
X_train_scaled = scaler.transform(X_train)  # Before fit!
X_test_scaled = scaler.transform(X_test)
```

<details>
<summary>Your Answer:</summary>
</details>

---

## Scoring Guide

**Section 1 (CV):** _____ / 8
**Section 2 (Tuning):** _____ / 7
**Section 3 (Regularization):** _____ / 8
**Section 4 (Leakage):** _____ / 10
**Section 5 (Pipeline):** _____ / 10
**Section 6 (Practical):** _____ / 5
**Section 7 (Debugging):** _____ / 3

**Total:** _____ / 51

**Percentage:** _____ %

---

## Interpretation

- **90-100%:** Excellent! You're ready for Week 5
- **80-89%:** Good! Review topics you missed
- **70-79%:** Decent foundation, but review weak areas before Week 5
- **Below 70%:** Revisit Week 4 materials and exercises before continuing

---

# Answer Key

<details>
<summary>Click to reveal answers (only after attempting all questions!)</summary>

## Section 1: Cross-Validation

1.1: **B** - Performance varies based on random split
1.2: **B** - 5 models (one per fold)
1.3: **B** - Array of 5 scores
1.4: **B** - Imbalanced classification
1.5: **B** - Stable performance
1.6: `StratifiedKFold`, `StratifiedKFold`, `cv`
1.7: **False** - Never CV on test set
1.8: **B** - Report mean ± std

## Section 2: Hyperparameter Tuning

2.1: **B** - Parameters learned, hyperparameters set
2.2: **B** - Tries all combinations via CV
2.3: **D** - 12 combinations (3×4)
2.4: **B** - `grid.best_params_`
2.5: **B** - Large param_grid
2.6: `model`, `param_grid`, `fit`, `grid.best_params_`
2.7: **True** - GridSearchCV refits automatically

## Section 3: Regularization

3.1: **B** - Prevent overfitting
3.2: **A** - L1 sets to zero, L2 shrinks
3.3: **B** - Feature selection
3.4: **B** - Regularization strength
3.5: **B** - Inverse (higher C = less penalty)
3.6: **B** - L1 + L2 combination
3.7: **True** - Trades training for test accuracy
3.8: **B** - `Ridge`

## Section 4: Data Leakage

4.1: **B** - Using unavailable information
4.2: **B** - Fitting on all data before split
4.3: **B** - fit_transform learns, transform just applies
4.4: **B** - Only on training data
4.5: **B** - Enforces correct order
4.6: **True** - Always split first
4.7: **B** - Test >> train accuracy
4.8: **B** - fit_transform before split
4.9: **B** - All steps fit_transform, final step fit
4.10: `fit_transform`, `transform`

## Section 5: Pipeline

5.1: **B** - Chains preprocessing + estimator
5.2: **C** - List of (name, object) tuples
5.3: **C** - Estimator (model)
5.4: **B** - Different transforms per column
5.5: **B** - `pipe['step_name']`
5.6: **B** - `'step__param'` notation
5.7: `StandardScaler()`, `LogisticRegression()`
5.8: `numeric_features`, `categorical_features`
5.9: **True** - GridSearchCV works with Pipeline
5.10: **B** - `joblib.dump()`

## Section 6: Practical Application

6.1: **B** - k=5 or k=10
6.2: **C** - Data leakage
6.3: **B** - L1 (Lasso) for feature selection
6.4: **D** - Both B and C
6.5: **C** - Complete workflow with Pipeline

## Section 7: Code Debugging

7.1: Using CV on test set (should use X_train, y_train)
7.2: Nothing wrong! (This is valid - just checking attention)
7.3: Must call `fit()` or `fit_transform()` before `transform()`

</details>

---

## Next Steps

Based on your score:

**If you scored 80%+:**
- ✅ Move to Week 5 materials
- ✅ Consider the bonus nested CV exercise
- ✅ Help peers who struggled

**If you scored 70-79%:**
- 📚 Review sections where you scored <70%
- 📚 Redo post-class exercises
- 📚 Watch StatQuest videos on weak topics

**If you scored <70%:**
- 📚 Rewatch live session recording
- 📚 Redo all Week 4 exercises
- 📚 Schedule office hours with instructor
- 📚 Don't move to Week 5 until you hit 80%+

---

## Additional Resources

**StatQuest Videos:**
- Cross-Validation: https://youtu.be/fSytzGwwBVw
- Regularization: https://youtu.be/Q81RR3yKn30
- Ridge Regression: https://youtu.be/Q81RR3yKn30

**sklearn Documentation:**
- Cross-validation: https://scikit-learn.org/stable/modules/cross_validation.html
- Pipeline: https://scikit-learn.org/stable/modules/compose.html
- GridSearchCV: https://scikit-learn.org/stable/modules/grid_search.html

**Practice:**
- Week 4 post-class exercise
- Week 4 bonus nested CV notebook
- Kaggle competitions (use Pipeline!)

---

*This self-assessment covers all Week 4 learning objectives. Use it to identify gaps before Week 5!*
