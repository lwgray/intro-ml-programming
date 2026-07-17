# Week 2: Classification Fundamentals - Pre-Class Study Guide

**Time Required:** 30 minutes
**Purpose:** Prime your understanding of classification concepts before the live session

---

## Welcome to Week 2!

Last week you mastered **regression** - predicting continuous values like house prices. This week we're tackling **classification** - predicting categories like "yes/no", "positive/negative", or "benign/malignant".

**The good news:** The sklearn API pattern you learned (fit/predict) stays exactly the same!

**The new skills:** Understanding different evaluation metrics and learning when accuracy can lie to you.

---

## Pre-Class Activities (Complete Before Live Session)

### Part 1: Watch These Videos (25 minutes total)

Watch in this order:

1. **StatQuest - Logistic Regression** (15 min)

   [Watch: StatQuest - Logistic Regression](https://www.youtube.com/watch?v=yIYKR4sgzI8)

   **What to focus on:**

   - How logistic regression creates an S-shaped curve
   - Why it's called "regression" even though it does classification
   - What probability outputs mean

2. **StatQuest - Confusion Matrix** (8 min)

   [Watch: StatQuest - Confusion Matrix](https://www.youtube.com/watch?v=Kdsp6soqA7o)

   **What to focus on:**

   - The 2x2 grid structure (you'll draw this many times today!)
   - True Positives, True Negatives, False Positives, False Negatives
   - Why this matters for understanding model performance

3. **Optional: Google ML Crash Course - Classification** (Read sections 1-3 only)

   [Click here for Google ML Crash Course - Classification](https://developers.google.com/machine-learning/crash-course/classification)

   **What to focus on:**

   - Decision boundaries
   - Why classification is different from regression

---

## Part 2: Key Concepts to Understand

By the end of the videos, you should have a basic understanding of:

### Classification vs Regression

| Regression | Classification |
|------------|----------------|
| Predicts **numbers** | Predicts **categories** |
| Example: House price ($250,000) | Example: Spam or not spam |
| Outputs: Continuous values | Outputs: Class labels (0 or 1) |
| Week 1 focus | Week 2 focus |

### Binary Classification

**Binary** means two classes:
- Yes / No
- Positive / Negative
- Malignant / Benign (cancer vs not cancer)
- Fraud / Legitimate

**This week's dataset:** Breast Cancer Wisconsin
- **Class 0 (malignant):** Cancer is present
- **Class 1 (benign):** No cancer

### The Confusion Matrix (Preview)

You'll become very familiar with this 2x2 grid:

```
                Predicted
                 Neg    Pos
              ┌──────┬──────┐
Actual    Neg │  TN  │  FP  │
              ├──────┼──────┤
          Pos │  FN  │  TP  │
              └──────┴──────┘
```

**Don't worry if this looks confusing!** We'll spend significant time on this during the live session. For now, just notice the structure.

### Logistic Regression Basics

**Key points from the video:**

- Takes continuous inputs (like linear regression)
- Squashes output through an S-shaped curve (sigmoid function)
- Outputs probabilities between 0 and 1
- Converts probabilities to class predictions using a threshold (default: 0.5)

**Analogy:** Think of it like a dimmer switch:
- Linear regression: outputs any brightness (0 to infinity watts)
- Logistic regression: outputs brightness percentage (0% to 100%)

---

## Part 3: Vocabulary Pre-Reading

These terms will appear frequently in Week 2. You don't need to memorize them now - just get familiar:

| Term | Quick Definition |
|------|------------------|
| **Binary Classification** | Predicting one of two classes (0 or 1) |
| **Sigmoid Function** | S-shaped curve that converts any number to 0-1 range |
| **Probability Threshold** | Cutoff point (default 0.5) for converting probability to class |
| **Confusion Matrix** | 2x2 table showing correct and incorrect predictions |
| **True Positive (TP)** | Correctly predicted positive class |
| **True Negative (TN)** | Correctly predicted negative class |
| **False Positive (FP)** | Incorrectly predicted positive (false alarm) |
| **False Negative (FN)** | Incorrectly predicted negative (missed case) |
| **Precision** | Of all positive predictions, how many were correct? |
| **Recall** | Of all actual positives, how many did we catch? |
| **Accuracy** | Percentage of all predictions that were correct |

**Medical test analogy:** Think of a COVID test:
- **TP:** Test says positive, you have COVID ✓
- **TN:** Test says negative, you don't have COVID ✓
- **FP:** Test says positive, but you're healthy ✗ (false alarm)
- **FN:** Test says negative, but you have COVID ✗ (missed diagnosis!)

---

## Part 4: Connection to Week 1

**What stays the same:**

- Load data with sklearn
- Split into training and test sets (BEFORE preprocessing!)
- Use `model.fit(X_train, y_train)` to train
- Use `model.predict(X_test)` to make predictions
- Evaluate performance with metrics

**What's new:**

- Using `LogisticRegression` instead of `LinearRegression`
- New method: `predict_proba()` for probability outputs
- Different metrics: confusion matrix, precision, recall instead of MSE/RMSE
- Binary target variable (0 or 1) instead of continuous

**The pattern is the same. The tools are the same. Only the problem type changed!**

---

## Part 5: Questions to Think About

Come to the live session with thoughts on these questions:

1. If a cancer screening test is 99% accurate, does that mean it's a great test? (Hint: Think about what happens if only 1% of people have cancer...)

2. In spam filtering, which is worse:
   - Letting spam through to your inbox? (False Negative)
   - Blocking an important email? (False Positive)

3. For cancer diagnosis, which is worse:
   - Telling a healthy person they have cancer? (False Positive)
   - Missing a cancer diagnosis? (False Negative)

**These questions have no universal "right" answer - it depends on context!** That's why we need multiple metrics, not just accuracy.

---

## Part 6: Pre-Class Practice (Optional but Recommended)

If you have an extra 10-15 minutes, try this quick exercise:

**Draw a confusion matrix from memory:**
1. Get a piece of paper
2. Draw a 2x2 grid
3. Label it with: Actual (rows), Predicted (columns), TP, TN, FP, FN
4. Check your drawing against the visual in Part 2

**Try a simple calculation:**

Imagine a cancer test with these results on 100 patients:
- 90 healthy patients, 10 with cancer
- Test correctly identifies 8 cancer cases (TP = 8)
- Test misses 2 cancer cases (FN = 2)
- Test correctly identifies 85 healthy (TN = 85)
- Test gives 5 false alarms (FP = 5)

Calculate:
- Accuracy = (TP + TN) / Total = ?
- What percentage of cancer cases did we catch? (This is called "recall")

**Answers:**
- Accuracy = (8 + 85) / 100 = 93%
- Recall = 8 / 10 = 80% (we caught 80% of cancer cases)

---

## What to Expect in Week 2

**Week 2 has TWO sessions:**

### Day 1: Classification Fundamentals (3 hours)

**Schedule:**
- 0:00-0:15: Week 1 recap & Week 2 overview
- 0:15-0:40: Classification concepts (confusion matrix on whiteboard)
- 0:40-1:00: Logistic regression theory
- 1:00-1:15: Advanced classification concepts
- 1:15-1:30: **BREAK**
- 1:30-2:25: Live coding - complete classification pipeline (Breast Cancer dataset)
- 2:25-2:35: Threshold tuning interpretation
- 2:35-2:45: Business cost analysis
- 2:45-3:15: Pair programming - Titanic survival prediction
- 3:15-3:20: Wrap-up & preview Day 2

**What to bring:**
- Questions from the videos
- Notebook for taking notes during whiteboard session
- Curiosity about metrics!

### Day 2: Deep Dive & Guided Practice (1 hour)

**Schedule:**
- 0:00-0:05: Recap
- 0:05-0:25: Deep dive on class imbalance and metric selection
- 0:25-0:45: Guided practice on new dataset (Heart Disease) with instructor support
- 0:45-0:55: Quiz (8 questions, 60% to pass)
- 0:55-1:00: Week 3 preview

**Purpose:** Day 2 gives you deeper understanding and more practice with instructor support before tackling homework solo.

---

## Success Checklist

Before the live session, you should:

- [ ] Watched StatQuest - Logistic Regression video
- [ ] Watched StatQuest - Confusion Matrix video
- [ ] Reviewed vocabulary list
- [ ] Thought about the discussion questions
- [ ] (Optional) Practiced drawing confusion matrix
- [ ] Ready to learn about classification!

---

## If You're Feeling Overwhelmed

**Don't worry!** These concepts are new and can feel abstract. The live session is designed to make everything concrete through:

- Visual demonstrations
- Live coding examples
- Real dataset (cancer screening)
- Pair programming practice
- Lots of repetition

**Remember:** You don't need to master these concepts before class. The pre-work is meant to prime your brain, not teach you everything. The real learning happens during the live session!

---

## Questions Before Class?

If anything is unclear, don't stress! The live session will bring it all together.

**Common questions we'll answer:**

- "Why is it called logistic REGRESSION if it does classification?"
- "How do I choose between precision and recall?"
- "When is accuracy misleading?"
- "What's the difference between predict() and predict_proba()?"

---

**See you in the live session!**

---

*Week 2 Pre-Class Study Guide v1.0 | December 2025*
