# Appendix B: Classification Metrics Guide

**Purpose:** A complete reference for calculating and interpreting classification metrics from a confusion matrix

**When to use:** Reference this guide whenever you need to calculate metrics by hand, understand what metrics mean, or select the right metric for your problem

---

## 📊 The Confusion Matrix Foundation

Every classification metric starts with the confusion matrix:

```
                   Predicted
                Negative    Positive
             ┌──────────┬──────────┐
  Actual  N  │    TN    │    FP    │
             ├──────────┼──────────┤
          P  │    FN    │    TP    │
             └──────────┴──────────┘
```

**The Four Values:**
- **TP (True Positive):** Correctly predicted positive
- **TN (True Negative):** Correctly predicted negative
- **FP (False Positive):** Incorrectly predicted positive (Type I error)
- **FN (False Negative):** Incorrectly predicted negative (Type II error)

**Memory Aid:**
- First word = Is the prediction correct? (True/False)
- Second word = What did we predict? (Positive/Negative)

---

## 🧮 All Metrics: Formulas and Meanings

### 1. Accuracy

**Formula:**
```
Accuracy = (TP + TN) / (TP + TN + FP + FN)
```

**Meaning:** What percentage of all predictions were correct?

**When to use:**
- Balanced datasets only
- When false positives and false negatives have equal cost

**When NOT to use:**
- Imbalanced datasets (can be misleading)
- When one type of error is more costly than the other

**Range:** 0.0 to 1.0 (0% to 100%)

**Example:**
```
TP=85, TN=900, FP=10, FN=5

Accuracy = (85 + 900) / (85 + 900 + 10 + 5)
        = 985 / 1000
        = 0.985 or 98.5%
```

---

### 2. Precision (Positive Predictive Value)

**Formula:**
```
Precision = TP / (TP + FP)
```

**Meaning:** Of all the positive predictions we made, what percentage were actually correct?

**Alternative phrasing:** "When I predict positive, how often am I right?"

**When to use:**
- When false positives are costly
- Email spam detection (don't want to flag real emails as spam)
- Medical screening where false alarms are expensive
- Fraud detection with limited investigation resources

**Range:** 0.0 to 1.0 (0% to 100%)

**Example:**
```
TP=85, FP=10

Precision = 85 / (85 + 10)
         = 85 / 95
         = 0.8947 or 89.47%
```

**Interpretation:** Of the 95 positive predictions, 85 were actually correct.

---

### 3. Recall (Sensitivity, True Positive Rate)

**Formula:**
```
Recall = TP / (TP + FN)
```

**Meaning:** Of all the actual positives, what percentage did we correctly identify?

**Alternative phrasing:** "Of all the real positives, how many did I catch?"

**When to use:**
- When false negatives are costly
- Cancer detection (can't afford to miss cancer)
- Fraud detection (can't afford to miss fraud)
- Quality control for safety-critical defects

**Range:** 0.0 to 1.0 (0% to 100%)

**Example:**
```
TP=85, FN=5

Recall = 85 / (85 + 5)
      = 85 / 90
      = 0.9444 or 94.44%
```

**Interpretation:** Of the 90 actual positive cases, we correctly identified 85.

---

### 4. F1 Score

**Formula:**
```
F1 = 2 × (Precision × Recall) / (Precision + Recall)
```

**Alternative formula (from confusion matrix):**
```
F1 = 2 × TP / (2 × TP + FP + FN)
```

**Meaning:** Harmonic mean of precision and recall (balanced metric)

**When to use:**
- When you need a single metric that balances precision and recall
- When you have imbalanced data
- When false positives and false negatives are both important

**Range:** 0.0 to 1.0 (0% to 100%)

**Example:**
```
Precision = 0.8947
Recall = 0.9444

F1 = 2 × (0.8947 × 0.9444) / (0.8947 + 0.9444)
   = 2 × 0.8449 / 1.8391
   = 1.6898 / 1.8391
   = 0.9188 or 91.88%
```

**Why harmonic mean?** It penalizes extreme values. If either precision or recall is very low, F1 will be low.

---

### 5. Specificity (True Negative Rate)

**Formula:**
```
Specificity = TN / (TN + FP)
```

**Meaning:** Of all the actual negatives, what percentage did we correctly identify?

**When to use:**
- When correctly identifying negatives is important
- Medical screening (confirming healthy patients are healthy)
- Binary classification where both classes matter equally

**Range:** 0.0 to 1.0 (0% to 100%)

**Example:**
```
TN=900, FP=10

Specificity = 900 / (900 + 10)
           = 900 / 910
           = 0.9890 or 98.90%
```

---

### 6. False Positive Rate (Fall-out)

**Formula:**
```
FPR = FP / (FP + TN) = 1 - Specificity
```

**Meaning:** Of all the actual negatives, what percentage did we incorrectly classify as positive?

**When to use:**
- ROC curve (x-axis)
- Understanding the cost of false alarms

**Range:** 0.0 to 1.0 (0% to 100%)

**Example:**
```
FP=10, TN=900

FPR = 10 / (10 + 900)
    = 10 / 910
    = 0.0110 or 1.10%
```

---

## 📐 Complete Worked Example

**Scenario:** Cancer screening test on 1,000 patients

**Confusion Matrix:**
```
                   Predicted
                Healthy    Cancer
             ┌──────────┬──────────┐
  Actual  H  │   900    │    10    │
             ├──────────┼──────────┤
          C  │    5     │    85    │
             └──────────┴──────────┘
```

**Values:**
- TP = 85 (correctly identified cancer)
- TN = 900 (correctly identified healthy)
- FP = 10 (false alarm - said cancer but healthy)
- FN = 5 (missed cancer - said healthy but cancer)

**Step-by-Step Calculations:**

**1. Accuracy**
```
Accuracy = (TP + TN) / Total
        = (85 + 900) / 1000
        = 985 / 1000
        = 0.985 or 98.5%
```
Interpretation: 98.5% of all predictions were correct.

**2. Precision**
```
Precision = TP / (TP + FP)
         = 85 / (85 + 10)
         = 85 / 95
         = 0.8947 or 89.47%
```
Interpretation: When we predict cancer, we're correct 89.47% of the time.

**3. Recall**
```
Recall = TP / (TP + FN)
      = 85 / (85 + 5)
      = 85 / 90
      = 0.9444 or 94.44%
```
Interpretation: We catch 94.44% of all cancer cases.

**4. F1 Score**
```
F1 = 2 × (Precision × Recall) / (Precision + Recall)
   = 2 × (0.8947 × 0.9444) / (0.8947 + 0.9444)
   = 2 × 0.8449 / 1.8391
   = 0.9188 or 91.88%
```
Interpretation: Balanced metric shows good overall performance.

**5. Specificity**
```
Specificity = TN / (TN + FP)
           = 900 / (900 + 10)
           = 900 / 910
           = 0.9890 or 98.90%
```
Interpretation: We correctly identify 98.90% of healthy patients.

**6. False Positive Rate**
```
FPR = FP / (FP + TN)
    = 10 / (10 + 900)
    = 10 / 910
    = 0.0110 or 1.10%
```
Interpretation: Only 1.10% of healthy patients get false alarms.

---

## 🎯 The Precision-Recall Tradeoff

**Key insight:** You can't maximize both precision and recall simultaneously.

**Increasing the threshold:**
- ↑ Precision (fewer false positives)
- ↓ Recall (more false negatives)
- More conservative predictions

**Decreasing the threshold:**
- ↓ Precision (more false positives)
- ↑ Recall (fewer false negatives)
- More aggressive predictions

**Visual representation:**
```
Low Threshold              Default              High Threshold
(predict more positive)    (0.5)               (predict more negative)
        ↓                    ↓                        ↓
   High Recall           Balanced              High Precision
   Low Precision                               Low Recall
```

---

## 🧭 Decision Guide: Which Metric to Use?

Use this flowchart to select the right metric:

```
START: What are you optimizing for?
│
├─ Both errors equally bad + balanced data
│  → Use ACCURACY
│
├─ False positives are costly
│  (false alarms are expensive)
│  → Use PRECISION
│  Examples: spam detection, medical procedures
│
├─ False negatives are costly
│  (missing positives is dangerous)
│  → Use RECALL
│  Examples: cancer detection, fraud detection
│
├─ Both errors matter + need single metric
│  → Use F1 SCORE
│  Examples: imbalanced data, general classification
│
└─ Need to tune threshold + see tradeoffs
   → Use ROC CURVE and PR CURVE
   Examples: when threshold matters, comparing models
```

---

## 📋 Quick Reference Table

| Metric | Formula | Answers | Best When |
|--------|---------|---------|-----------|
| **Accuracy** | (TP+TN)/Total | % correct overall | Balanced data, equal costs |
| **Precision** | TP/(TP+FP) | When I say yes, how often am I right? | False positives costly |
| **Recall** | TP/(TP+FN) | Of all real yes, how many did I catch? | False negatives costly |
| **F1** | 2PR/(P+R) | Balanced single score | Imbalanced data |
| **Specificity** | TN/(TN+FP) | Of all real no, how many did I catch? | Need to confirm negatives |
| **FPR** | FP/(FP+TN) | % false alarms | Understanding mistakes |

---

## 🚨 Common Mistakes to Avoid

### Mistake 1: Using accuracy on imbalanced data

**Wrong:**
```python
# Dataset: 990 healthy, 10 cancer patients
# Accuracy: 99%
# But model predicts EVERYONE as healthy!
```

**Why wrong:** A dumb model that always predicts "healthy" gets 99% accuracy but catches 0% of cancer.

**Fix:** Use precision, recall, or F1 for imbalanced data.

---

### Mistake 2: Confusing precision and recall

**Memory tricks:**
- **Precision:** "When I **P**redict **P**ositive, am I right?"
- **Recall:** "Did I **R**ecall (catch) all the **R**eal positives?"

---

### Mistake 3: Forgetting the denominator

**Precision denominator:** TP + FP (all predicted positives)
**Recall denominator:** TP + FN (all actual positives)

**Tip:** Draw the confusion matrix and circle which cells you're using!

---

### Mistake 4: Not considering the business context

**Medical example:**
- Cancer screening: Optimize for **recall** (can't miss cancer)
- Follow-up biopsy: Optimize for **precision** (biopsies are expensive)

**Business example:**
- Fraud detection: Optimize for **recall** (catch all fraud)
- Fraud investigation: Optimize for **precision** (limited investigators)

---

## 🔧 Sklearn Implementation

**Calculate all metrics from confusion matrix:**

```python
from sklearn.metrics import confusion_matrix, classification_report

# Get predictions
y_pred = model.predict(X_test)

# Get confusion matrix
cm = confusion_matrix(y_test, y_pred)

# Extract values
TN = cm[0, 0]
FP = cm[0, 1]
FN = cm[1, 0]
TP = cm[1, 1]

# Calculate metrics manually
accuracy = (TP + TN) / (TP + TN + FP + FN)
precision = TP / (TP + FP)
recall = TP / (TP + FN)
f1 = 2 * (precision * recall) / (precision + recall)
specificity = TN / (TN + FP)
fpr = FP / (FP + TN)

print(f"Accuracy:    {accuracy:.4f}")
print(f"Precision:   {precision:.4f}")
print(f"Recall:      {recall:.4f}")
print(f"F1:          {f1:.4f}")
print(f"Specificity: {specificity:.4f}")
print(f"FPR:         {fpr:.4f}")

# Or use sklearn functions
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

# Or get comprehensive report
print(classification_report(y_test, y_pred))
```

---

## 📚 Practice Problems

### Problem 1: Basic Calculation

Given this confusion matrix:
```
               Predicted
            No      Yes
Actual  No  450     50
        Yes  25    475
```

Calculate: accuracy, precision, recall, F1

<details>
<summary>Click for answer</summary>

**Values:** TP=475, TN=450, FP=50, FN=25

**Accuracy:** (475+450)/1000 = 0.925 or 92.5%

**Precision:** 475/(475+50) = 0.905 or 90.5%

**Recall:** 475/(475+25) = 0.95 or 95%

**F1:** 2×(0.905×0.95)/(0.905+0.95) = 0.927 or 92.7%
</details>

---

### Problem 2: Metric Selection

**Scenario:** Building a spam filter for email.

**Question:** Should you optimize for precision or recall? Why?

<details>
<summary>Click for answer</summary>

**Answer:** Optimize for **PRECISION**

**Why:** False positives (marking real email as spam) are very costly - users might miss important messages. False negatives (letting spam through) are annoying but less costly - users can just delete spam.

**Result:** High precision means when you flag email as spam, you're very confident it's actually spam.
</details>

---

### Problem 3: The 99% Accurate But Useless Model

**Scenario:** Disease detection with 1% prevalence (10 sick out of 1,000 people).

Model predicts EVERYONE as healthy.

**Question:** Calculate accuracy, precision, recall. Why is this model useless?

<details>
<summary>Click for answer</summary>

**Confusion Matrix:**
```
               Predicted
            Healthy  Sick
Actual  H    990      0
        S     10      0
```

**Accuracy:** 990/1000 = 99% ← Looks great!

**Precision:** 0/0 = undefined (never predicts sick)

**Recall:** 0/10 = 0% ← Catches NO sick patients!

**Why useless:** Despite 99% accuracy, it has 0% recall - it never identifies any sick patients! This is why accuracy is misleading for imbalanced data.
</details>

---

## 🎓 Key Takeaways

1. **All metrics start from the confusion matrix** - master this 2×2 table first
2. **Accuracy is NOT always the right metric** - especially for imbalanced data
3. **Precision vs Recall is a tradeoff** - you can't maximize both
4. **Choose metrics based on business cost** - which error is more expensive?
5. **F1 balances precision and recall** - good default for imbalanced data
6. **Always calculate metrics on TEST set** - never on training set

---

## 📖 Additional Resources

- **sklearn metrics documentation:** https://scikit-learn.org/stable/modules/model_evaluation.html
- **Confusion matrix visualization:** Use `sns.heatmap(cm, annot=True, fmt='d')`
- **ROC curves:** Will cover in Week 2 Demo
- **Cross-validation:** Will cover in Week 4

---

**Bookmark this page - you'll reference it constantly throughout the course and in real-world projects!**
