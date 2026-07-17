# Week 3: Decision Trees & Ensembles - Student Workbook

**Date:** ________________
**Name:** ________________

**Purpose:** Note-taking template for today's live session
**How to use:** Fill in the blanks as the instructor explains each concept

---

## 📋 Session Overview

**Today's Topic:** Decision Trees, Random Forests, and XGBoost
**Time:** 3 hours (0:00 - 3:00)
**Goal:** Learn to compare multiple algorithms systematically!

---

## 🎯 Learning Objectives (Check off as you learn!)

By the end of today, I will be able to:

- [ ] Implement Decision Trees, Random Forests, and XGBoost using sklearn
- [ ] Explain how decision trees split data using information gain
- [ ] Extract and interpret feature importance from tree models
- [ ] Compare three algorithms systematically on the same dataset
- [ ] Choose the best algorithm based on business constraints

---

## Part 1: Week 2 Recap & Week 3 Preview (0:00 - 0:15)

### Week 2 Key Concepts Review

**Classification metrics we learned:**

1. _________________ - Percentage of correct predictions
2. _________________ - Of positive predictions, how many were correct?
3. _________________ - Of actual positives, how many did we catch?
4. _________________ - Harmonic mean of precision and recall

**Question from instructor:** When is accuracy misleading?

_______________________________________________________________________

_______________________________________________________________________

### Week 3 Overview

**The three algorithms we'll compare today:**

1. _________________ (single tree - most interpretable)
2. _________________ (ensemble of trees via bagging)
3. _________________ (ensemble of trees via boosting)

**Why compare multiple algorithms?**

_______________________________________________________________________

_______________________________________________________________________

---

## Part 2: Decision Trees (0:15 - 0:45)

### The "20 Questions Game" Analogy

**How decision trees work:**

_______________________________________________________________________

_______________________________________________________________________

_______________________________________________________________________

**Draw the tree structure as instructor explains:**

```
                  Root Node
               [All Training Data]
                      |
          Question: _________________?
             /              \
          Yes               No
          /                  \
    [_____ people]       [_____ people]
         |                    |
    Next question...      Next question...
```

---

### How Trees Decide Which Question to Ask

**The tree wants to maximize:** _________________

**Definition of Information Gain:**

_______________________________________________________________________

_______________________________________________________________________

**Example - Which split is better?**

Split A: Creates groups with 90% purity
Split B: Creates groups with 60% purity

**Better split:** _____ because _________________________________________

---

### Gini Impurity

**What it measures:** _____________________________________________________

**Scale:**
- ______ = perfectly pure (all samples one class)
- ______ = maximally mixed (equal mix of classes)

**Formula** (don't need to memorize, just understand):

Gini = _______________

**Alternative to Gini:** _________________ (same intuition, different math)

---

### Overfitting in Decision Trees

**What happens if we let trees grow without limits?**

_______________________________________________________________________

_______________________________________________________________________

**Training accuracy:** _______  Test accuracy: _______  (Example numbers)

**This is called:** _________________

**How to prevent it:**

Use the _________________ hyperparameter to limit tree depth.

**Recommended max_depth values:** _____ to _____

---

### Decision Tree in sklearn

**Fill in the code pattern:**

```python
from sklearn.tree import _________________

# Create model
dt_model = DecisionTreeClassifier(
    max_depth=_____,      # Prevent overfitting
    random_state=_____    # Reproducibility
)

# Train model
dt_model._____(X_train, y_train)

# Make predictions
y_pred = dt_model._____(X_test)
```

---

### When to Use Decision Trees

**Strengths:**

1. _____________________________________________________________________
2. _____________________________________________________________________
3. _____________________________________________________________________

**Weaknesses:**

1. _____________________________________________________________________
2. _____________________________________________________________________
3. _____________________________________________________________________

---

## Part 3: Random Forests (0:45 - 1:10)

### Ensemble Methods Intuition

**What is an ensemble?**

_______________________________________________________________________

_______________________________________________________________________

**Analogy:** "Wisdom of crowds"

_______________________________________________________________________

---

### Bagging (Bootstrap Aggregating)

**What is a bootstrap sample?**

_______________________________________________________________________

_______________________________________________________________________

**Example:**
- Original data: [1, 2, 3, 4, 5]
- Bootstrap sample 1: _____________________________
- Bootstrap sample 2: _____________________________

**How Random Forest uses bagging:**

Step 1: _________________________________________________________________

Step 2: _________________________________________________________________

Step 3: _________________________________________________________________

Step 4: _________________________________________________________________

---

### Random Forest Hyperparameters

**Fill in the key parameters:**

```python
from sklearn.ensemble import RandomForestClassifier

rf_model = RandomForestClassifier(
    n_estimators=_____,   # Number of trees in forest
    max_depth=_____,      # Depth of each tree
    random_state=_____    # Reproducibility
)
```

**n_estimators:**
- Typical value: _____
- Too few: _________________
- Too many: _________________

**max_depth for Random Forest:**
- Can be deeper than single tree because: _________________________________

---

### Feature Importance

**What is feature importance?**

_______________________________________________________________________

_______________________________________________________________________

**How to extract it:**

```python
importance = rf_model._________________
```

**How to interpret it:**

- Values range from _____ to _____
- Higher values mean: __________________________________________________
- Values sum to: _____

**CRITICAL WARNING:**

Feature importance shows _________________, NOT _________________!

---

### When to Use Random Forests

**Use Random Forest when:**

✅ _____________________________________________________________________

✅ _____________________________________________________________________

✅ _____________________________________________________________________

**Instructor's recommendation:** Start with Random Forest as your ___________

---

## Part 4: BREAK (1:10 - 1:25)

Take a break! When you return, we'll learn XGBoost.

---

## Part 5: XGBoost (1:25 - 1:55)

### Boosting vs Bagging

**Fill in the comparison:**

| Aspect | Bagging (Random Forest) | Boosting (XGBoost) |
|--------|------------------------|-------------------|
| Training | _________________ | _________________ |
| Tree relationship | _________________ | _________________ |
| Focus | _________________ | _________________ |

**Boosting intuition:**

_______________________________________________________________________

_______________________________________________________________________

**Analogy:** Study group where each person focuses on what previous person struggled with

---

### Gradient Boosting

**What it means:**

_______________________________________________________________________

_______________________________________________________________________

**How XGBoost differs from sklearn's GradientBoostingClassifier:**

1. _____________________________________________________________________
2. _____________________________________________________________________
3. _____________________________________________________________________

---

### XGBoost Hyperparameters

**Fill in the code:**

```python
import xgboost as xgb

xgb_model = xgb.XGBClassifier(
    n_estimators=_____,     # Number of boosting rounds
    max_depth=_____,        # Shallower than Random Forest!
    learning_rate=_____,    # NEW! Step size for boosting
    random_state=_____
)
```

**learning_rate:**
- Range: _____ to _____
- Small values (0.01): __________________________________________________
- Large values (0.3): __________________________________________________
- Recommended starting point: _____

**Why shallower trees for XGBoost (max_depth=3) vs Random Forest (max_depth=5)?**

_______________________________________________________________________

_______________________________________________________________________

---

### When to Use XGBoost

**Use XGBoost when:**

✅ _____________________________________________________________________

✅ _____________________________________________________________________

**Don't use XGBoost when:**

❌ _____________________________________________________________________

❌ _____________________________________________________________________

---

### XGBoost Installation Notes

**How to install:**

```bash
pip install xgboost
```

**Common issues noted in class:**

_______________________________________________________________________

_______________________________________________________________________

---

## Part 6: Live Coding - Systematic Algorithm Comparison (1:55 - 2:30)

**Dataset:** Adult Income (Census data)
**Goal:** Predict if income > $50K
**Task:** Compare all three algorithms

### Data Overview

**Number of samples:** _________________
**Number of features:** _________________
**Class distribution:** ______% low income, ______% high income

**Important features noted:**

1. _____________________________________________________________________
2. _____________________________________________________________________
3. _____________________________________________________________________

---

### Results: Decision Tree

**Hyperparameters used:**
- max_depth: _____
- random_state: _____

**Metrics:**
- Accuracy: _______
- Precision: _______
- Recall: _______
- F1-Score: _______

**Observations:**

_______________________________________________________________________

---

### Results: Random Forest

**Hyperparameters used:**
- n_estimators: _____
- max_depth: _____
- random_state: _____

**Metrics:**
- Accuracy: _______
- Precision: _______
- Recall: _______
- F1-Score: _______

**Improvement over Decision Tree:** +______ percentage points

**Observations:**

_______________________________________________________________________

---

### Results: XGBoost

**Hyperparameters used:**
- n_estimators: _____
- max_depth: _____
- learning_rate: _____
- random_state: _____

**Metrics:**
- Accuracy: _______
- Precision: _______
- Recall: _______
- F1-Score: _______

**Improvement over Random Forest:** +______ percentage points

**Observations:**

_______________________________________________________________________

---

### Feature Importance Comparison

**Top 3 most important features (according to XGBoost):**

1. _________________ (importance: _____)
2. _________________ (importance: _____)
3. _________________ (importance: _____)

**Did all three models agree on top features?**

_______________________________________________________________________

**Which features showed the biggest disagreement across models?**

_______________________________________________________________________

**Why might different algorithms rank features differently?**

_______________________________________________________________________

_______________________________________________________________________

---

### Final Comparison Table

| Algorithm | Accuracy | Precision | Recall | F1-Score | Interpretability | Training Time |
|-----------|----------|-----------|--------|----------|------------------|---------------|
| Decision Tree | _______ | _______ | _______ | _______ | _______ | _______ |
| Random Forest | _______ | _______ | _______ | _______ | _______ | _______ |
| XGBoost | _______ | _______ | _______ | _______ | _______ | _______ |

---

### Algorithm Selection Discussion

**Scenario 1: Bank needs interpretable model for loan approval**

**Recommended algorithm:** _________________

**Why:** _______________________________________________________________

_______________________________________________________________________

---

**Scenario 2: E-commerce company wants maximum click prediction accuracy**

**Recommended algorithm:** _________________

**Why:** _______________________________________________________________

_______________________________________________________________________

---

**Scenario 3: Startup needs quick baseline model**

**Recommended algorithm:** _________________

**Why:** _______________________________________________________________

_______________________________________________________________________

---

### Key Takeaway from This Segment

**The most important lesson:**

_______________________________________________________________________

_______________________________________________________________________

_______________________________________________________________________

---

## Part 7: Pair Programming - Algorithm Showdown (2:30 - 2:50)

**My partner:** ___________________________

**Role:** Navigator ___  or  Driver ___ (check one)

### Task 1: Explain Decision Tree Prediction Path

**Sample being explained:**
- Age: _____
- Education: _____
- Hours-per-week: _____
- Prediction: _________________

**Prediction path through tree:**

Root → _________________________________________ →

_______________________________________________________ →

_______________________________________________________ →

Leaf: Predict _________________

**Why did tree predict this?**

_______________________________________________________________________

---

### Task 2: Feature Importance Comparison

**Features all models agree are important:**

1. _____________________________________________________________________
2. _____________________________________________________________________

**Features where models disagree:**

_______________________________________________________________________

**My explanation for disagreement:**

_______________________________________________________________________

_______________________________________________________________________

---

### Task 3: Business Scenarios

**Our recommendation for medical diagnosis scenario:**

**Algorithm:** _________________

**Reasoning:** _____________________________________________________________

_______________________________________________________________________

_______________________________________________________________________

---

### Pair Programming Reflection

**What I learned from my partner:**

_______________________________________________________________________

**What was challenging:**

_______________________________________________________________________

**Key insight from this exercise:**

_______________________________________________________________________

---

## Part 8: Wrap-Up & Next Steps (2:50 - 3:00)

### Today's Key Concepts Review

**Fill in the systematic comparison workflow:**

1. _____________________________________________________________________
2. _____________________________________________________________________
3. _____________________________________________________________________
4. _____________________________________________________________________
5. _____________________________________________________________________

**The algorithm selection principle:**

Choose based on _________________, not just _________________

---

### Post-Class Homework

**Due:** _________________ (date/time)

**Tasks:**

- [ ] Complete `week3_postclass_exercise.ipynb` (Titanic dataset)
- [ ] Implement all three algorithms
- [ ] Create feature importance visualization
- [ ] Write 2-paragraph algorithm recommendation
- [ ] (Optional) Bonus: Advanced feature engineering

**What to submit:**

_______________________________________________________________________

---

### Preview: Week 4

**Next week's topic:** _____________________

**Key concepts:**
- _____________________________________________________________________
- _____________________________________________________________________
- _____________________________________________________________________

**Why it matters:**

_______________________________________________________________________

_______________________________________________________________________

---

## 📝 My Notes & Observations

**Use this space for any additional notes during the session:**

_______________________________________________________________________

_______________________________________________________________________

_______________________________________________________________________

_______________________________________________________________________

_______________________________________________________________________

_______________________________________________________________________

_______________________________________________________________________

_______________________________________________________________________

---

## 🎯 Self-Assessment

**Rate your understanding (1 = confused, 5 = confident):**

| Concept | Rating (1-5) | Notes |
|---------|--------------|-------|
| Decision Trees | _____ | ________________________________ |
| Random Forests | _____ | ________________________________ |
| XGBoost | _____ | ________________________________ |
| Bagging vs Boosting | _____ | ________________________________ |
| Feature Importance | _____ | ________________________________ |
| Algorithm Comparison | _____ | ________________________________ |
| Algorithm Selection | _____ | ________________________________ |

**Overall confidence:** _____ / 5

**Concepts I want to review:**

1. _____________________________________________________________________
2. _____________________________________________________________________
3. _____________________________________________________________________

---

## ❓ Questions for Instructor

**Write down any questions to ask during Q&A or office hours:**

1. _____________________________________________________________________

2. _____________________________________________________________________

3. _____________________________________________________________________

4. _____________________________________________________________________

---

## 🔗 Resources to Review

**Check off as you review these resources:**

- [ ] Week 3 glossary (key terms)
- [ ] Week 3 sklearn cheat sheet (quick reference)
- [ ] StatQuest Decision Trees (18 min - review if needed)
- [ ] StatQuest Random Forests (10 min - review if needed)
- [ ] XGBoost documentation (for hyperparameter details)
- [ ] sklearn Decision Tree visualization tutorial

---

## 🎉 Congratulations!

You've completed Week 3 of Introduction to Machine Learning Programming!

**You can now:**
- ✅ Implement three powerful tree-based algorithms
- ✅ Compare algorithms systematically
- ✅ Extract and interpret feature importance
- ✅ Choose algorithms based on business constraints
- ✅ Explain tree predictions to stakeholders

**Next step:** Complete the post-class homework to solidify these skills on a different dataset (Titanic)!

---

**Remember:** The workflow you learned today (systematic algorithm comparison) is what data scientists use in practice. Master this workflow and you can apply it to any classification problem!

---

*Questions? Reach out to the instructor or post in the discussion forum.*

**Instructor:** ____________________
**Email:** ____________________
**Office hours:** ____________________
