# Week 3 Self-Assessment - Decision Trees & Ensembles

**Purpose:** Evaluate your understanding of Week 3 concepts
**Time:** 15-20 minutes
**Format:** Answer questions honestly, then check answers

---

## Instructions

1. Answer all questions WITHOUT looking at notes or solutions
2. Check your answers using the answer key at the bottom
3. For questions you miss, review the corresponding glossary entry
4. Rate your confidence for each concept
5. Identify areas to review before Week 4

**This is for YOUR learning - be honest with yourself!**

---

## Part 1: Conceptual Understanding (30 points)

### Question 1 (5 points)
**Explain how a decision tree makes a prediction for a new data point.**

Your answer:

_______________________________________________________________________

_______________________________________________________________________

_______________________________________________________________________

**Confidence (1-5):** _____

---

### Question 2 (5 points)
**What is the difference between bagging and boosting?**

Your answer:

_______________________________________________________________________

_______________________________________________________________________

_______________________________________________________________________

**Confidence (1-5):** _____

---

### Question 3 (5 points)
**Why do Random Forests use bootstrap samples instead of training all trees on the full dataset?**

Your answer:

_______________________________________________________________________

_______________________________________________________________________

_______________________________________________________________________

**Confidence (1-5):** _____

---

### Question 4 (5 points)
**Explain what feature importance tells you and what it does NOT tell you.**

Your answer:

_______________________________________________________________________

_______________________________________________________________________

_______________________________________________________________________

**Confidence (1-5):** _____

---

### Question 5 (5 points)
**Why does XGBoost typically use shallower trees (max_depth=3) compared to Random Forest (max_depth=5-10)?**

Your answer:

_______________________________________________________________________

_______________________________________________________________________

_______________________________________________________________________

**Confidence (1-5):** _____

---

### Question 6 (5 points)
**What is the purpose of the `learning_rate` parameter in XGBoost, and what happens if it's too high or too low?**

Your answer:

_______________________________________________________________________

_______________________________________________________________________

_______________________________________________________________________

**Confidence (1-5):** _____

---

## Part 2: Code Understanding (25 points)

### Question 7 (5 points)
**What is wrong with this code?**

```python
from sklearn.tree import DecisionTreeClassifier

dt = DecisionTreeClassifier()
dt.fit(X_train, y_train)
y_pred = dt.predict(X_test)
```

Your answer:

_______________________________________________________________________

_______________________________________________________________________

**Confidence (1-5):** _____

---

### Question 8 (5 points)
**Fill in the blanks to create a Random Forest with 200 trees, depth 10, using all CPU cores:**

```python
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(
    n_estimators=_____,
    max_depth=_____,
    n_jobs=_____,
    random_state=42
)
```

Your answer: n_estimators=_____, max_depth=_____, n_jobs=_____

**Confidence (1-5):** _____

---

### Question 9 (5 points)
**What does this code extract from a trained Random Forest?**

```python
importance = rf_model.feature_importances_
```

Your answer:

_______________________________________________________________________

_______________________________________________________________________

**Confidence (1-5):** _____

---

### Question 10 (5 points)
**Identify the error in this XGBoost code:**

```python
import xgboost as xgb

xgb_model = xgb.XGBClassifier(
    n_estimators=100,
    max_depth=15,  # Deep tree for maximum accuracy!
    learning_rate=0.5,  # Large step for faster training!
    random_state=42
)
```

Your answer:

_______________________________________________________________________

_______________________________________________________________________

**Confidence (1-5):** _____

---

### Question 11 (5 points)
**What is the purpose of this parameter in the code below?**

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
#                         ^^^^^^^^
```

Your answer:

_______________________________________________________________________

_______________________________________________________________________

**Confidence (1-5):** _____

---

## Part 3: Algorithm Selection (20 points)

### Question 12 (10 points)
**You're building a credit risk model for a bank. Regulators require that you can explain why each loan was denied. The bank also wants reasonable accuracy. Which algorithm would you choose and why?**

Your algorithm choice: _________________

Your reasoning:

_______________________________________________________________________

_______________________________________________________________________

_______________________________________________________________________

**Confidence (1-5):** _____

---

### Question 13 (10 points)
**You're participating in a Kaggle competition where only accuracy matters (no interpretability requirement). You have time to tune hyperparameters. Which algorithm would you likely start with and why?**

Your algorithm choice: _________________

Your reasoning:

_______________________________________________________________________

_______________________________________________________________________

_______________________________________________________________________

**Confidence (1-5):** _____

---

## Part 4: Troubleshooting (15 points)

### Question 14 (5 points)
**A student's decision tree achieves 99% accuracy on training data but only 65% on test data. What's the problem and how would you fix it?**

Problem:

_______________________________________________________________________

Solution:

_______________________________________________________________________

_______________________________________________________________________

**Confidence (1-5):** _____

---

### Question 15 (5 points)
**When training XGBoost, a student gets this error:**
```
ModuleNotFoundError: No module named 'xgboost'
```

**What should they do?**

Your answer:

_______________________________________________________________________

_______________________________________________________________________

**Confidence (1-5):** _____

---

### Question 16 (5 points)
**A student trains three algorithms (Decision Tree, Random Forest, XGBoost) and gets these results:**

| Algorithm | Train Accuracy | Test Accuracy |
|-----------|---------------|---------------|
| Decision Tree | 85% | 82% |
| Random Forest | 92% | 89% |
| XGBoost | 97% | 88% |

**Which model would you recommend using in production and why?**

Your recommendation: _________________

Your reasoning:

_______________________________________________________________________

_______________________________________________________________________

**Confidence (1-5):** _____

---

## Part 5: Practical Application (10 points)

### Question 17 (10 points)
**You've trained a Random Forest on a medical diagnosis dataset. The top 3 features by importance are:**
1. blood_pressure (0.45)
2. age (0.28)
3. cholesterol (0.17)

**A colleague says: "Great! This proves that blood pressure CAUSES the disease, so we should focus treatment on lowering blood pressure."**

**Is your colleague's interpretation correct? Explain why or why not.**

Your answer:

_______________________________________________________________________

_______________________________________________________________________

_______________________________________________________________________

_______________________________________________________________________

**Confidence (1-5):** _____

---

## Scoring Guide

**Total Points Possible: 100**

**Grading Scale:**
- 90-100: Excellent understanding - ready for Week 4
- 75-89: Good understanding - review concepts you missed
- 60-74: Adequate understanding - spend extra time on glossary
- Below 60: Need significant review - attend office hours

**By Concept Area:**
- Part 1 (Conceptual): _____ / 30
- Part 2 (Code): _____ / 25
- Part 3 (Selection): _____ / 20
- Part 4 (Troubleshooting): _____ / 15
- Part 5 (Application): _____ / 10

**Total Score: _____ / 100**

---

## Reflection Questions

After completing the assessment:

### What concepts do I understand well?

1. _____________________________________________________________________
2. _____________________________________________________________________
3. _____________________________________________________________________

### What concepts need more review?

1. _____________________________________________________________________
2. _____________________________________________________________________
3. _____________________________________________________________________

### What will I do to improve my understanding?

_______________________________________________________________________

_______________________________________________________________________

_______________________________________________________________________

---

## Answer Key

<details>
<summary>Click to reveal answers (only after attempting all questions!)</summary>

### Part 1: Conceptual Understanding

**Question 1:** A decision tree makes predictions by starting at the root node and asking a series of yes/no questions about features. At each node, it follows the appropriate branch based on the answer. This continues until reaching a leaf node, which contains the final prediction (majority class for classification, mean value for regression).

**Question 2:**
- **Bagging:** Trains multiple models IN PARALLEL on different bootstrap samples, then averages/votes on predictions. Each model is independent. Example: Random Forest.
- **Boosting:** Trains models SEQUENTIALLY, where each new model focuses on correcting errors made by previous models. Example: XGBoost.

**Question 3:** Bootstrap samples create diversity among trees. Each tree sees a slightly different view of the data (some samples appear multiple times, others not at all). This diversity means trees make different mistakes, and averaging reduces overfitting. If all trees trained on same data, they'd all make the same mistakes.

**Question 4:**
- **What it tells you:** Which features the MODEL uses most for predictions. Relative importance compared to other features.
- **What it does NOT tell you:** Whether features CAUSE the target (correlation ≠ causation). Whether a feature is important for reasons we care about (could be proxy for confounding variable).

**Question 5:** In boosting, trees are combined SEQUENTIALLY - each tree learns from previous trees' mistakes. Shallow trees (3-6 levels) are sufficient because many sequential trees can represent complex patterns. Deep trees would overfit and not leave errors for subsequent trees to fix. In Random Forest, trees are PARALLEL, so each tree needs to be more expressive (deeper) since they don't learn from each other.

**Question 6:** `learning_rate` controls how much each tree contributes to the final prediction.
- **Too low (0.01):** Training is very slow (need many trees), but less overfitting risk.
- **Too high (0.5+):** Fast training but high overfitting risk, may overshoot optimal solution.
- **Just right (0.1):** Good balance - recommended starting point.

### Part 2: Code Understanding

**Question 7:** Not technically wrong, but BAD practice: no `max_depth` set! This tree will grow until all leaves are pure, causing severe overfitting (high train accuracy, low test accuracy). Should set `max_depth=5` or similar.

**Question 8:** n_estimators=200, max_depth=10, n_jobs=-1 (uses all available CPU cores)

**Question 9:** An array of feature importance values, one per feature, summing to 1.0. Higher values indicate features that contribute more to predictions. Based on how much each feature reduces impurity across all trees in the forest.

**Question 10:** TWO errors:
1. `max_depth=15` is TOO DEEP for XGBoost. Should be 3-6 (boosting works better with shallow trees).
2. `learning_rate=0.5` is TOO HIGH. Should be 0.1 or lower. High learning rate causes overfitting in boosting.

**Question 11:** `random_state=42` ensures reproducibility. The split will be identical every time you run the code (same samples in train/test). Without it, you'd get different splits each run, making results not comparable.

### Part 3: Algorithm Selection

**Question 12:** **Decision Tree** (or possibly Random Forest if some interpretability is acceptable).

**Reasoning:** Regulators require EXPLAINABILITY. Decision Trees are most interpretable - you can visualize the tree and explain exact path: "Loan denied because income < $40K AND debt-to-income > 0.5." Random Forest offers feature importance which helps explanation, but harder to trace exact decision path. XGBoost is too much of a black box for regulatory requirements.

**Question 13:** **XGBoost** (or possibly Random Forest to start, then XGBoost).

**Reasoning:** Kaggle competitions prioritize ACCURACY above all else. XGBoost typically achieves highest accuracy on tabular data. With time to tune hyperparameters, XGBoost almost always edges out Random Forest by 1-3%. No interpretability requirement, so XGBoost's black-box nature doesn't matter. Could start with Random Forest for quick baseline, then switch to XGBoost for final submission.

### Part 4: Troubleshooting

**Question 14:**
- **Problem:** Overfitting. Tree is too deep and memorized training data instead of learning generalizable patterns.
- **Solution:** Set `max_depth=5` (or 3-10). Could also increase `min_samples_split` or `min_samples_leaf`. Or use Random Forest/XGBoost instead of single tree.

**Question 15:** XGBoost is not installed. Run: `pip install xgboost` in terminal. If that fails, try `conda install -c conda-forge xgboost`. As last resort, can use sklearn's GradientBoostingClassifier instead (similar but slower).

**Question 16:** **Random Forest (89% test accuracy)**.

**Reasoning:** Although XGBoost has highest train accuracy (97%), its test accuracy (88%) is LOWER than Random Forest (89%), suggesting XGBoost is slightly overfitting. Random Forest shows good generalization (train 92%, test 89% - only 3-point gap). In production, test performance matters more than train performance. Random Forest is also simpler to maintain.

### Part 5: Practical Application

**Question 17:** NO, this interpretation is INCORRECT.

**Reasoning:** Feature importance shows CORRELATION, not CAUSATION. High blood_pressure importance means it's useful for PREDICTING disease, but we can't conclude it CAUSES disease. Possible alternatives:
- Blood pressure might be a SYMPTOM (not cause) of the disease
- Blood pressure might correlate with true cause (e.g., both caused by genetics)
- High blood pressure might be measured more accurately than other features (appears important due to data quality, not medical relevance)

**Correct interpretation:** "Blood pressure is the strongest PREDICTOR of disease in our model. To understand causation, we need controlled experiments or causal inference methods, not just feature importance."

</details>

---

## Next Steps Based on Your Score

### If you scored 90-100:
✅ Excellent! You're ready for Week 4.
- Skim the glossary for reinforcement
- Try the bonus exercise for challenge
- Help peers who are struggling

### If you scored 75-89:
✓ Good understanding, but some gaps.
- Review Week 3 glossary entries for missed questions
- Re-watch relevant segments of StatQuest videos
- Complete bonus exercise for extra practice
- Attend office hours if available

### If you scored 60-74:
⚠ Adequate but needs work.
- Carefully review Week 3 glossary
- Re-read teaching materials for weak areas
- Redo Week 3 notebooks with focus on understanding (not just running code)
- Attend office hours - ask specific questions
- Form study group with classmates

### If you scored below 60:
🚨 Significant gaps - action required!
- Schedule office hours with instructor
- Re-watch ALL pre-class videos with note-taking
- Complete Week 3 notebooks line-by-line, explaining each step to yourself
- Review Week 1-2 materials (foundation may be weak)
- Don't move to Week 4 until you can score 75+ on this assessment

---

## Concepts to Master Before Week 4

**You MUST understand these for Week 4 (Cross-Validation & Hyperparameter Tuning):**

- [ ] Decision trees make predictions via sequential yes/no questions
- [ ] Bagging = parallel ensemble, Boosting = sequential ensemble
- [ ] Feature importance shows correlation, NOT causation
- [ ] Random Forest is good robust default algorithm
- [ ] XGBoost offers highest accuracy but requires tuning
- [ ] Algorithm selection depends on business constraints (interpretability vs accuracy)
- [ ] Overfitting occurs when model memorizes training data
- [ ] max_depth controls tree depth and prevents overfitting

**If you can't check all these boxes confidently, REVIEW before Week 4!**

---

## Additional Practice

If you want more practice:

1. **Repeat Week 3 homework** on a different dataset (try Wine or Iris)
2. **Explain concepts to a friend** (teaching solidifies learning)
3. **Draw diagrams** of how bagging vs boosting works
4. **Write decision tree rules** for everyday decisions (e.g., "Should I bring an umbrella?")
5. **Read sklearn documentation** for DecisionTreeClassifier, RandomForestClassifier

---

**Remember:** Struggling is part of learning! If you scored low, that's INFORMATION about where to focus, not a judgment of your abilities. Review weak areas and you'll master this! 💪

---

*Questions? Confused by an answer? Post in the course forum or attend office hours.*

---

*Last Updated: 2026-01-24*
