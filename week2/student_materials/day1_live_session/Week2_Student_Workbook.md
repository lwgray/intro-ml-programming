# Week 2: Classification - Student Workbook

**Date:** ________________
**Name:** ________________

**Purpose:** Note-taking template for today's live session
**How to use:** Fill in the blanks as the instructor explains each concept

---

## 📋 Session Overview

**Today's Topic:** Binary Classification with Logistic Regression
**Time:** 3 hours (0:00 - 3:00)
**Goal:** Master confusion matrices and classification metrics!

---

## 🎯 Learning Objectives (Check off as you learn!)

By the end of today, I will be able to:

- [ ] Build a complete classification pipeline using logistic regression
- [ ] Draw and label a confusion matrix from memory
- [ ] Calculate precision, recall, and F1-score by hand
- [ ] Explain when accuracy is misleading
- [ ] Use `predict_proba()` to get probability predictions
- [ ] Interpret ROC curves and AUC scores
- [ ] Choose metrics based on business costs

---

## Part 1: Week 1 Recap & Week 2 Preview (0:00 - 0:15)

### Quick Wins from Week 1

What was the most important lesson from Week 1?

____________________________________________________________________

____________________________________________________________________

### The sklearn Pattern (Universal!)

```
1. Create model: model = _____________()
2. Train model:  model._____(X_train, y_train)
3. Predict:      y_pred = model._____(X_test)
```

**This pattern works for BOTH regression and classification!** ✓

### Week 2 Focus: Classification

**Classification vs Regression:**

| Aspect | Regression | Classification |
|--------|-----------|----------------|
| **Predicts** | _______________ values | _______________ labels |
| **Example** | House price ($250,000) | _______________ |
| **Algorithms** | Linear Regression | _______________ |
| **Metrics** | MSE, RMSE, R² | _______________ |

---

## Part 2: Quick Classification Demo (0:15 - 0:45)

### Dataset: Breast Cancer Wisconsin

- **Features:** ______ measurements from cell images
- **Target classes:**
  - `0` = _______________
  - `1` = _______________
- **Samples:** ______ patients

### Key Observations from Demo

**Accuracy:** ______ %

**But is that the whole story?** (Answer after next section!)

____________________________________________________________________

____________________________________________________________________

---

## Part 3: Classification Concepts (0:45 - 1:15)

### What is Binary Classification?

**Definition:** Predicting one of ______ possible classes (0 or 1)

**Real-world examples:**
- Email: ______________________ or ______________________
- Medical: ____________________ or ______________________
- Finance: ____________________ or ______________________

### Logistic Regression: The Basics

**Key differences from linear regression:**

1. **Output transformation:** Linear regression outputs continuous values.
   Logistic regression outputs through a _____________ function.

2. **Output range:** Linear regression: -∞ to +∞.
   Logistic regression: ______ to ______ (probabilities!)

3. **Decision boundary:** Uses a _____________ (default: 0.5) to convert
   probabilities to class predictions.

### The Sigmoid Function

**Draw the S-curve:** (Sketch as instructor explains)

```
   1.0 ┤         ╭─────────
       │       ╭─
       │     ╭─
   0.5 ┤   ╭─
       │ ╭─
       │─
   0.0 ┤
       └─────────────────────
```

**What does it do?**

____________________________________________________________________

____________________________________________________________________

### From Probabilities to Predictions

**Example:** Model outputs probability = 0.73 for class 1

- If threshold = 0.5 → Predict class ______
- If threshold = 0.8 → Predict class ______

**Why might we adjust the threshold?**

____________________________________________________________________

____________________________________________________________________

---

## Part 4: The Confusion Matrix ⭐ **CRITICAL**

### Draw the Confusion Matrix (Practice!)

```
                Predicted
                 NEG    POS
              ┌──────┬──────┐
Actual    NEG │      │      │
              ├──────┼──────┤
          POS │      │      │
              └──────┴──────┘
```

**Label each quadrant with:** TN, TP, FP, FN

### Medical Test Analogy

**Fill in the interpretation for each quadrant:**

**TN (True Negative):**
- Test says: _______________
- Reality: _______________
- Outcome: ✓ CORRECT!

**TP (True Positive):**
- Test says: _______________
- Reality: _______________
- Outcome: ✓ CORRECT!

**FP (False Positive):**
- Test says: _______________
- Reality: _______________
- Outcome: ✗ WRONG! (Also called: _______________)

**FN (False Negative):**
- Test says: _______________
- Reality: _______________
- Outcome: ✗ WRONG! (Also called: _______________)

### Practice Example

**Given:** 100 patients tested

```
                Predicted
                HEALTHY  CANCER
              ┌────────┬────────┐
Actual HEALTHY│   70   │   10   │
              ├────────┼────────┤
      CANCER  │   5    │   15   │
              └────────┴────────┘
```

**Identify:**
- TN = ______  (Correctly identified healthy)
- TP = ______  (Correctly identified cancer)
- FP = ______  (False alarms)
- FN = ______  (Missed diagnoses) ← DANGEROUS!

**Which error is WORSE in cancer screening?** ______

**Why?**

____________________________________________________________________

____________________________________________________________________

---

## Part 5: Metrics Deep Dive (1:45 - 2:00)

### Accuracy

**Formula:**

```
Accuracy = (_____ + _____) / Total
```

**From our example:**

```
Accuracy = (70 + 15) / 100 = _____ = _____%
```

**Interpretation:** ____% of all predictions were correct

### When Accuracy LIES ⚠️

**The "99% Accurate But Useless" Example:**

**Scenario:** Rare disease (1% of population has it)
- 990 healthy, 10 sick
- "Lazy model" always predicts HEALTHY

```
                Predicted
                HEALTHY  SICK
              ┌────────┬──────┐
Actual HEALTHY│  990   │  0   │
              ├────────┼──────┤
      SICK    │  10    │  0   │
              └────────┴──────┘
```

**Accuracy = ____________ = ______%** (Sounds great!)

**But:**
- Recall = ____/10 = ______% (Catches ZERO sick patients!) ← USELESS!

**The lesson:**

____________________________________________________________________

____________________________________________________________________

____________________________________________________________________

### Precision

**Formula:**

```
Precision = TP / (TP + FP) = ______ / ______
```

**Question answered:** "When I predict POSITIVE, how often am I right?"

**From our cancer example:**

```
Precision = 15 / (15 + 10) = 15 / 25 = _____ = _____%
```

**Interpretation:**

____________________________________________________________________

____________________________________________________________________

**Mnemonic:** **P**recision = When I **P**redict **P**ositive

### Recall

**Formula:**

```
Recall = TP / (TP + FN) = ______ / ______
```

**Question answered:** "Of all actual POSITIVES, how many did I catch?"

**From our cancer example:**

```
Recall = 15 / (15 + 5) = 15 / 20 = _____ = _____%
```

**Interpretation:**

____________________________________________________________________

____________________________________________________________________

**Mnemonic:** **R**ecall = Catch all **R**eal positives

### The Precision-Recall Tradeoff

**Key insight:** You can't maximize both simultaneously!

```
↑ Higher Recall (catch more) → More FP → ↓ Lower Precision
↑ Higher Precision (fewer false alarms) → More FN → ↓ Lower Recall
```

**Business decision:** Which to optimize depends on context!

**Examples:**

| Use Case | Optimize | Reason |
|----------|----------|--------|
| Cancer screening | _____________ | _________________________________ |
| Spam filtering | _____________ | _________________________________ |
| Fraud detection | _____________ | _________________________________ |
| Loan approval | _____________ | _________________________________ |

### F1-Score

**Formula:**

```
F1 = 2 × (Precision × Recall) / (Precision + Recall)
```

**What is it?** Harmonic mean of precision and recall

**When to use:** When you care _____________ about FP and FN

**From our example:**

```
F1 = 2 × (0.60 × 0.75) / (0.60 + 0.75) = _______
```

### Practice Calculation

**Given this confusion matrix:**

```
               Predicted
                 0     1
              ┌─────┬─────┐
Actual     0  │ 40  │  5  │
              ├─────┼─────┤
           1  │ 10  │ 45  │
              └─────┴─────┘
```

**Calculate:**

- **Accuracy** = (_____ + _____) / _____ = _______

- **Precision** = _____ / (_____ + _____) = _______

- **Recall** = _____ / (_____ + _____) = _______

- **F1** = 2 × (_____ × _____) / (_____ + _____) = _______

---

## Part 6: ROC Curves and AUC (Brief)

### What is ROC?

**ROC = Receiver Operating Characteristic**

**It plots:**
- **X-axis:** _______________________ Rate (FPR)
- **Y-axis:** _______________________ Rate (TPR = Recall)

**Each point on the curve:** Different probability _____________

### AUC (Area Under Curve)

**Range:** ______ (worst) to ______ (best)

**Interpretation guide:**

| AUC Score | Interpretation |
|-----------|----------------|
| 1.0 | _________________ |
| 0.9 - 1.0 | _________________ |
| 0.8 - 0.9 | _________________ |
| 0.7 - 0.8 | _________________ |
| 0.5 | Random guessing (WORTHLESS!) |
| < 0.5 | _________________ |

**Our model AUC:** ______

**Meaning:** _____________________________________________________

---

## Part 7: Live Coding (2:00 - 2:30)

### Code Pattern (Fill in as we code!)

```python
# Step 1: Load data
data = load_breast_cancer()
X, y = _____________, _____________

# Step 2: Split
X_train, X_test, y_train, y_test = _____________

# Step 3: Preprocess
scaler = StandardScaler()
X_train_scaled = scaler._____________(_____________)
X_test_scaled = scaler._____________(_____________)

# Step 4: Train
model = _____________()
model._____________(_____________, _____________)

# Step 5: Predict
y_pred = model._____________(_____________)
y_pred_proba = model._____________(_____________)  # NEW!

# Step 6: Evaluate
accuracy = _____________
cm = _____________
precision = _____________
recall = _____________
f1 = _____________
```

### Key Observations from Live Coding

**Most important takeaway:**

____________________________________________________________________

____________________________________________________________________

**Most surprising result:**

____________________________________________________________________

____________________________________________________________________

---

## Part 8: Pair Programming (2:30 - 2:50)

### Exercise: DIAGNOSTIC Challenge

**Task:** A classifier is broken. Use confusion matrix to diagnose the problem!

**Problems to look for:**
- [ ] Always predicting one class
- [ ] Threshold issues
- [ ] Data leakage
- [ ] Wrong metric optimization

**My findings:**

____________________________________________________________________

____________________________________________________________________

____________________________________________________________________

**Fix applied:**

____________________________________________________________________

____________________________________________________________________

---

## Part 9: Wrap-Up (2:50 - 3:00)

### Three Most Important Things I Learned Today

1. ____________________________________________________________________

   ____________________________________________________________________

2. ____________________________________________________________________

   ____________________________________________________________________

3. ____________________________________________________________________

   ____________________________________________________________________

### Questions I Still Have

1. ____________________________________________________________________

2. ____________________________________________________________________

3. ____________________________________________________________________

### Homework Preview

**Post-class exercise:** Build classifier on _____________ Disease dataset

**Key differences from live session:**
- ______% scaffolding (you write more code!)
- Different dataset
- Additional challenge questions

**Bonus exercise:** _______________________ tuning

---

## Quick Reference Card (Keep This Handy!)

### Confusion Matrix Quick Draw

```
                Predicted
                 NEG    POS
              ┌──────┬──────┐
Actual    NEG │  TN  │  FP  │
              ├──────┼──────┤
          POS │  FN  │  TP  │
              └──────┴──────┘
```

### Metric Formulas

```
Accuracy  = (TP + TN) / Total
Precision = TP / (TP + FP)  [When I predict POS]
Recall    = TP / (TP + FN)  [Of all actual POS]
F1        = 2 × (P × R) / (P + R)
```

### When to Use Which Metric

| Metric | Use When |
|--------|----------|
| **Accuracy** | Balanced classes, equal error costs |
| **Precision** | FP is costly (spam filter, loan approval) |
| **Recall** | FN is costly (cancer, fraud detection) |
| **F1** | Balance both, or when class imbalance |
| **AUC** | Comparing models overall |

### sklearn Methods

```python
model.fit(X_train, y_train)           # Train
model.predict(X_test)                 # Class predictions
model.predict_proba(X_test)           # Probabilities
```

---

## Post-Session Action Items

**Before next week:**
- [ ] Complete post-class exercise (Heart Disease dataset)
- [ ] Review confusion matrix until you can draw it from memory
- [ ] Try the bonus threshold tuning exercise
- [ ] Fill out self-assessment
- [ ] Review Week 2 glossary

**For deeper learning:**
- [ ] Re-watch StatQuest videos on confusion matrix and logistic regression
- [ ] Practice calculating metrics by hand with new examples
- [ ] Read sklearn documentation on classification metrics

---

**Great work today! You've mastered the foundation of classification!** 🎓

---

*Week 2 Student Workbook v1.0 | December 2025*
