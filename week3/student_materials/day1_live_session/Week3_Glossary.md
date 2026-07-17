# Week 3 Glossary - Decision Trees & Ensembles

**Purpose:** Key terms and concepts from Week 3 defined clearly
**Format:** Alphabetically organized with examples and cross-references

---

## How to Use This Glossary

- **Bold terms** are defined in this glossary
- *Italicized terms* are related concepts
- 📌 indicates especially important terms to memorize
- → indicates "see also" cross-references

---

## B

### Bagging 📌
Bootstrap Aggregating - an ensemble method where multiple models are trained on different random samples (with replacement) of the training data, then predictions are averaged/voted.

**How it works:**
1. Create bootstrap samples (random samples with replacement)
2. Train one model on each sample
3. Aggregate predictions (vote for classification, average for regression)

**Example:** Random Forest uses bagging with decision trees.

**Python:**
```python
from sklearn.ensemble import RandomForestClassifier
# This uses bagging automatically
rf = RandomForestClassifier(n_estimators=100)
```

→ See also: *Random Forest*, *Ensemble*, *Bootstrap Sample*

---

### Boosting 📌
An ensemble method where models are trained sequentially, with each new model focusing on correcting mistakes made by previous models.

**Key difference from bagging:** Sequential (not parallel) - each tree learns from previous trees' errors.

**Analogy:** Like a study group where each person teaches what the previous person struggled with.

**Example:** XGBoost, AdaBoost, Gradient Boosting

**Why it works:** Later trees focus on hard-to-classify examples that early trees got wrong.

→ See also: *XGBoost*, *Gradient Boosting*, *learning_rate*

---

### Bootstrap Sample
A random sample drawn WITH REPLACEMENT from the original dataset, same size as original.

**With replacement** means the same data point can appear multiple times in a bootstrap sample.

**Example:**
- Original: [1, 2, 3, 4, 5]
- Bootstrap sample 1: [1, 1, 3, 5, 5]
- Bootstrap sample 2: [2, 2, 3, 4, 4]

**Used in:** Random Forests (each tree sees a different bootstrap sample)

→ See also: *Bagging*, *Random Forest*

---

## D

### Decision Boundary
The line/surface that separates different classes in feature space.

**For decision trees:** Axis-aligned rectangles (splits only on one feature at a time).

**Example:** If tree splits on "age > 30" then "income > 50K", the boundary is a rectangle, not a diagonal line.

**Contrast with:** Logistic regression creates smooth diagonal boundaries.

→ See also: *Decision Tree*, *Split*

---

### Decision Tree 📌
A supervised learning algorithm that makes predictions by asking a series of yes/no questions (binary splits) on features.

**Structure:**
- **Root node:** Top of tree (all training data)
- **Internal nodes:** Decision points (ask questions)
- **Leaf nodes:** Final predictions

**Analogy:** Playing "20 Questions" - each question splits possibilities into groups.

**sklearn:**
```python
from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier(max_depth=5, random_state=42)
dt.fit(X_train, y_train)
```

**Strengths:**
- Interpretable (can explain exact prediction path)
- Handles mixed feature types naturally
- No feature scaling needed

**Weaknesses:**
- Prone to overfitting without depth limits
- Unstable (small data changes → different tree)

→ See also: *Information Gain*, *Gini Impurity*, *max_depth*, *Overfitting*

---

## E

### Early Stopping
A technique to prevent overfitting in boosting algorithms by stopping training when validation performance stops improving.

**How it works:** Monitor validation error during training; stop if it doesn't improve for N rounds.

**XGBoost example:**
```python
xgb_model.fit(X_train, y_train,
              early_stopping_rounds=10,
              eval_set=[(X_val, y_val)])
```

**Benefit:** Faster training + prevents overfitting

→ See also: *XGBoost*, *Overfitting*, *Boosting*

---

### Ensemble 📌
A machine learning technique that combines multiple models to produce better predictions than any single model.

**Core idea:** "Wisdom of crowds" - averaging many imperfect models often beats one perfect model.

**Types:**
- **Bagging:** Parallel models (Random Forest)
- **Boosting:** Sequential models (XGBoost)
- **Stacking:** Layered models (Week 7)

**Analogy:** Committee decision vs individual expert.

→ See also: *Bagging*, *Boosting*, *Random Forest*, *XGBoost*

---

## F

### Feature Importance 📌
A score indicating how much each feature contributes to model predictions.

**For tree models:** Based on how much each feature reduces impurity when used for splits.

**Interpretation:**
- Higher value = more important
- Sum to 1.0 across all features
- Relative, not absolute (importance compared to other features)

**Python:**
```python
importance = rf_model.feature_importances_
# Array: [0.35, 0.22, 0.18, 0.15, 0.10, ...]
```

**CRITICAL WARNING:** Feature importance shows correlation, NOT causation! High importance doesn't mean a feature CAUSES the target.

**Different algorithms give different importance rankings!** Always check multiple models.

→ See also: *Decision Tree*, *Random Forest*, *XGBoost*

---

## G

### Gini Impurity 📌
A measure of how "mixed" a group of samples is. Used by decision trees to decide where to split.

**Formula:** Gini = 1 - Σ(p_i²) where p_i is proportion of class i

**Scale:**
- 0 = perfectly pure (all samples one class)
- 0.5 = maximally impure (equal mix of two classes)

**Example:**
- Group 1: [100 positive, 0 negative] → Gini = 0 (pure!)
- Group 2: [50 positive, 50 negative] → Gini = 0.5 (mixed)

**What decision trees want:** Low Gini (pure groups)

**Alternative:** Entropy (same intuition, different math)

→ See also: *Information Gain*, *Entropy*, *Decision Tree*

---

### Gradient Boosting
A boosting algorithm that builds trees sequentially, where each tree predicts the residual errors of previous trees.

**How it differs from Random Forest:** Sequential (not parallel), focuses on mistakes

**Variants:**
- GradientBoostingClassifier (sklearn)
- XGBoost (faster, more features)
- LightGBM, CatBoost (alternatives)

**Why "gradient":** Uses gradient descent to minimize loss function

→ See also: *Boosting*, *XGBoost*, *learning_rate*

---

## I

### Information Gain 📌
The reduction in impurity (Gini or entropy) achieved by splitting on a feature.

**Formula:** Information Gain = Impurity(parent) - Weighted Average Impurity(children)

**How decision trees use it:** Choose split with highest information gain.

**Analogy:** In "20 Questions", good questions eliminate many possibilities. High information gain = good question.

**Example:**
- Split on "age > 30": Information Gain = 0.15
- Split on "capital_gain > 5000": Information Gain = 0.28 ← Tree chooses this!

→ See also: *Gini Impurity*, *Entropy*, *Decision Tree*

---

### Interpretability
How easily a human can understand and explain a model's predictions.

**Most interpretable to least:**
1. Single Decision Tree (can trace exact path)
2. Random Forest (feature importance, but hard to trace)
3. XGBoost (feature importance, complex interactions)
4. Neural Networks (mostly black box)

**When it matters:**
- Regulated industries (banking, healthcare)
- Explaining to stakeholders
- Debugging model mistakes
- Building trust with users

**Trade-off:** Usually less interpretable = more accurate

→ See also: *Decision Tree*, *Feature Importance*, *Stakeholder Communication*

---

## L

### Leaf Node
A terminal node in a decision tree that contains the final prediction.

**Classification:** Leaf predicts the majority class of training samples that reach it.
**Regression:** Leaf predicts the mean of training samples that reach it.

**Example:**
```
If age > 30 AND education > 12:
    Leaf: Predict "High Income" (73% of samples at this leaf are high income)
```

**Purity:** Best leaves are pure (all samples same class).

→ See also: *Decision Tree*, *Node*, *Overfitting*

---

### learning_rate 📌
A hyperparameter in boosting algorithms that controls how much each tree contributes to the final prediction.

**Range:** Typically 0.01 to 0.3
- **Small (0.01):** Conservative, needs more trees, less overfitting
- **Large (0.3):** Aggressive, needs fewer trees, more overfitting risk

**Analogy:** Step size when walking downhill. Small steps = slow but safe. Large steps = fast but might overshoot.

**XGBoost default:** 0.3

**Best practice:** Start with 0.1, tune if needed.

**Python:**
```python
xgb_model = xgb.XGBClassifier(
    n_estimators=100,
    learning_rate=0.1,  # How much each tree contributes
    random_state=42
)
```

→ See also: *XGBoost*, *Boosting*, *n_estimators*

---

## M

### max_depth 📌
A hyperparameter that limits how many sequential questions (splits) a decision tree can ask.

**Purpose:** Prevent overfitting by stopping trees from growing too deep.

**Typical values:** 3-10
- **Shallow (3-5):** Less overfitting, less expressive
- **Deep (10+):** More expressive, more overfitting risk

**Example:**
- max_depth=3: Tree asks at most 3 questions before predicting
- max_depth=None: Tree grows until all leaves are pure (DANGER: overfitting!)

**For boosting (XGBoost):** Use shallower trees (3-6) because they're combined sequentially.

**For Random Forest:** Can use deeper trees (5-10) because averaging reduces overfitting.

**Python:**
```python
dt_model = DecisionTreeClassifier(max_depth=5)
```

→ See also: *Decision Tree*, *Overfitting*, *Hyperparameter*

---

## N

### n_estimators 📌
The number of trees in an ensemble (Random Forest or XGBoost).

**Typical values:** 100-500
- **Small (10-50):** Fast training, may underfit
- **Medium (100-200):** Good balance (recommended starting point)
- **Large (500+):** Better performance, slow training, diminishing returns

**Rule of thumb:** More trees = better performance, up to a point (then plateaus).

**Random Forest:** Can't overfit by adding more trees (just slows down training).
**XGBoost:** Can overfit with too many trees (use early stopping).

**Python:**
```python
rf_model = RandomForestClassifier(n_estimators=100)
xgb_model = xgb.XGBClassifier(n_estimators=100)
```

→ See also: *Random Forest*, *XGBoost*, *Ensemble*

---

### Node
A point in a decision tree where a binary decision is made.

**Types:**
- **Root node:** Top of tree (all training data)
- **Internal node:** Asks a question, has children
- **Leaf node:** Terminal node, makes prediction

**Each internal node contains:**
- Feature to split on (e.g., "age")
- Threshold value (e.g., "> 30")
- Number of samples reaching this node
- Impurity score (Gini)

→ See also: *Decision Tree*, *Split*, *Leaf Node*

---

## O

### Out-of-Bag (OOB) Score
A validation method unique to Random Forests that uses samples NOT included in a tree's bootstrap sample.

**How it works:**
- Each tree trained on ~63% of data (bootstrap sample)
- Remaining ~37% used for validation
- Average validation accuracy across all trees

**Advantage:** No need for separate validation set!

**Python:**
```python
rf_model = RandomForestClassifier(n_estimators=100, oob_score=True)
rf_model.fit(X_train, y_train)
print(f"OOB Score: {rf_model.oob_score_}")
```

→ See also: *Random Forest*, *Bootstrap Sample*, *Cross-Validation*

---

### Overfitting
When a model performs very well on training data but poorly on new data because it memorized noise instead of learning patterns.

**For decision trees:** Deep trees without max_depth create very specific rules that don't generalize.

**Signs of overfitting:**
- Train accuracy: 98%
- Test accuracy: 75%
- Tree has hundreds of leaves

**Prevention:**
- Set max_depth
- Use min_samples_split, min_samples_leaf
- Use ensemble methods (Random Forest, XGBoost)
- Prune trees

→ See also: *max_depth*, *Generalization*, *Ensemble*

---

## P

### Pruning
Removing branches from a decision tree to prevent overfitting.

**Two types:**
- **Pre-pruning:** Stop growing tree early (max_depth, min_samples_split)
- **Post-pruning:** Grow full tree, then remove branches (cost-complexity pruning)

**sklearn uses pre-pruning** (hyperparameters like max_depth).

**Analogy:** Trimming a bush to keep it healthy and manageable.

→ See also: *Overfitting*, *max_depth*, *Decision Tree*

---

## R

### Random Forest 📌
An ensemble learning algorithm that combines many decision trees trained on different bootstrap samples and random feature subsets.

**How it works:**
1. Create N bootstrap samples
2. Train one decision tree on each
3. For each split, consider only a random subset of features
4. Final prediction = majority vote (classification) or average (regression)

**Why "random":**
- Random bootstrap samples
- Random feature subsets at each split

**Strengths:**
- Robust to overfitting
- High accuracy on many problems
- Minimal hyperparameter tuning
- Works well "out of the box"

**Weaknesses:**
- Less interpretable than single tree
- Slower than single tree
- Requires more memory

**sklearn:**
```python
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(
    n_estimators=100,  # Number of trees
    max_depth=5,       # Depth of each tree
    random_state=42
)
rf.fit(X_train, y_train)
```

→ See also: *Bagging*, *Ensemble*, *Decision Tree*, *Bootstrap Sample*

---

## S

### Split 📌
A decision point in a tree where data is divided into two groups based on a feature threshold.

**Binary split:** "Is feature X > threshold?" → Yes (left) or No (right)

**Example:**
- Split: "age > 30"
- Left child: All samples with age > 30
- Right child: All samples with age ≤ 30

**Best split:** Maximizes information gain (creates purest children).

→ See also: *Decision Tree*, *Information Gain*, *Node*

---

### Systematic Algorithm Comparison
The methodology for comparing multiple ML algorithms on the same problem fairly.

**Week 3 workflow:**
1. Use SAME train/test split for all algorithms
2. Calculate SAME metrics for each (accuracy, precision, recall, F1)
3. Extract feature importance from each
4. Create comparison table
5. Choose algorithm based on business constraints (not just accuracy)

**Critical:** Compare on same data with same evaluation methods!

→ See also: *Feature Importance*, *Algorithm Selection*

---

## X

### XGBoost 📌
eXtreme Gradient Boosting - a highly optimized implementation of gradient boosting that often wins machine learning competitions.

**Why it's popular:**
- Often highest accuracy on tabular data
- Fast training (parallelized)
- Handles missing values
- Built-in regularization
- Early stopping support

**Key hyperparameters:**
- `n_estimators`: Number of trees
- `max_depth`: Tree depth (use shallower than Random Forest)
- `learning_rate`: Contribution of each tree
- `subsample`: Fraction of data to use per tree

**Installation:**
```bash
pip install xgboost
```

**Python:**
```python
import xgboost as xgb

xgb_model = xgb.XGBClassifier(
    n_estimators=100,
    max_depth=3,
    learning_rate=0.1,
    random_state=42
)
xgb_model.fit(X_train, y_train)
```

**When to use:**
- Need maximum accuracy
- Have time to tune hyperparameters
- Interpretability not critical

→ See also: *Boosting*, *Gradient Boosting*, *learning_rate*

---

## Quick Reference: Week 3 Key Terms

### Must Memorize

1. **Decision Tree** - Algorithm that makes predictions via yes/no questions
2. **Random Forest** - Ensemble of many trees via bagging
3. **XGBoost** - Gradient boosting algorithm (sequential trees)
4. **Bagging** - Parallel ensemble (bootstrap + aggregate)
5. **Boosting** - Sequential ensemble (learn from mistakes)
6. **max_depth** - Limit tree depth to prevent overfitting
7. **n_estimators** - Number of trees in ensemble
8. **learning_rate** - Step size in boosting (XGBoost)
9. **Feature Importance** - Which features contribute most to predictions
10. **Gini Impurity** - How "mixed" a group is (low = pure)

### Algorithm Selection Guide

**Use Decision Tree when:**
- Need to explain predictions to stakeholders
- Want to visualize model
- Baseline/quick prototype

**Use Random Forest when:**
- Want robust "Swiss Army knife" algorithm
- Don't need deep interpretability
- Good default starting point

**Use XGBoost when:**
- Need maximum accuracy
- Have time to tune hyperparameters
- Competition or production deployment

---

## Additional Resources

### sklearn Documentation:
- Decision Trees: https://scikit-learn.org/stable/modules/tree.html
- Random Forests: https://scikit-learn.org/stable/modules/ensemble.html#forests-of-randomized-trees
- Gradient Boosting: https://scikit-learn.org/stable/modules/ensemble.html#gradient-boosting

### XGBoost Documentation:
- Official Docs: https://xgboost.readthedocs.io/
- Python API: https://xgboost.readthedocs.io/en/latest/python/python_api.html

### Visual Resources:
- R2D3 Visual Intro: http://www.r2d3.us/visual-intro-to-machine-learning-part-1/
- Decision Tree Visualization: https://explained.ai/decision-tree-viz/

---

**Study tip:** Focus on understanding WHEN to use each algorithm (based on interpretability vs accuracy tradeoffs), not memorizing every hyperparameter!

---

*Last Updated: 2026-01-24*
