# Week 2 Glossary - Classification

**Purpose:** Key terms and concepts from Week 2 defined clearly
**Format:** Alphabetically organized with examples and cross-references

---

## How to Use This Glossary

- **Bold terms** are defined in this glossary
- *Italicized terms* are related concepts
- 📌 indicates especially important terms to memorize
- → indicates "see also" cross-references
- 🔥 indicates terms commonly confused by students

---

## A

### Accuracy
The proportion of correct predictions out of all predictions made.

**Formula:**
```
Accuracy = (TP + TN) / (TP + TN + FP + FN)
```

**Example:** If a model makes 95 correct predictions out of 100, accuracy = 95%.

**⚠️ Warning:** Can be misleading with imbalanced classes!

**When to trust:** Balanced datasets with equal error costs.

**Python:**
```python
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, y_pred)
```

→ See also: *Confusion Matrix*, *Class Imbalance*, *Precision*, *Recall*

---

### AUC (Area Under Curve) 📌
The area under the ROC curve, providing a single number to summarize classifier performance. Ranges from 0.5 (random guessing) to 1.0 (perfect classifier).

**Interpretation guide:**
- 0.9-1.0: Excellent
- 0.8-0.9: Good
- 0.7-0.8: Fair
- 0.6-0.7: Poor
- 0.5: Random guessing (worthless)
- <0.5: Worse than random (model is backwards)

**Advantage:** Threshold-independent metric.

**Python:**
```python
from sklearn.metrics import roc_auc_score
auc = roc_auc_score(y_test, y_pred_proba[:, 1])
```

→ See also: *ROC Curve*, *TPR*, *FPR*

---

## B

### Baseline Model
A simple, naive model used as a benchmark to evaluate if a more complex model is worthwhile.

**Examples:**
- Always predict majority class
- Random guessing
- Predict based on single most important feature

**Use case:** If your logistic regression only beats baseline by 2%, it's not very useful!

→ See also: *Accuracy*, *Class Imbalance*

---

### Binary Classification 📌
A classification task with exactly two possible classes (0 and 1).

**Examples:**
- Email: spam or not spam
- Medical: disease present or absent
- Finance: fraud or legitimate transaction
- Customer: will churn or stay

**Contrast with:** *Multi-class classification* (3+ classes, covered in Week 3)

→ See also: *Class Label*, *Positive Class*, *Negative Class*

---

## C

### Class
One of the categories in a classification problem.

**In binary classification:**
- Class 0: Often called the "negative class"
- Class 1: Often called the "positive class"

**Example:** In spam detection:
- Class 0 = not spam (negative)
- Class 1 = spam (positive)

→ See also: *Binary Classification*, *Class Label*, *Target Variable*

---

### Class Imbalance 🔥
When one class has significantly more samples than another.

**Example:** Fraud detection where 99% of transactions are legitimate (class 0) and only 1% are fraudulent (class 1).

**Why it matters:** A model that always predicts the majority class will have high accuracy but be completely useless!

**Solutions:**
- Use precision, recall, F1 instead of accuracy
- Resampling techniques (Week 7)
- Adjust class weights
- Use appropriate metrics

**Rule of thumb:** If one class is >70% of data, consider it imbalanced.

→ See also: *Accuracy*, *Precision*, *Recall*, *Baseline Model*

---

### Class Label
The category assigned to each sample. In binary classification: 0 or 1.

**Synonyms:** Target, output, dependent variable, y

→ See also: *Binary Classification*, *Target Variable*

---

### Classification
A supervised learning task where the goal is to predict categorical labels (classes).

**Types:**
- **Binary:** 2 classes (Week 2)
- **Multi-class:** 3+ classes (Week 3)
- **Multi-label:** Multiple labels per sample (advanced)

**Contrast with:** *Regression* (predicting continuous values)

→ See also: *Binary Classification*, *Supervised Learning*

---

### Classification Report
A comprehensive summary of classification metrics for each class.

**Includes:** Precision, recall, F1-score, and support for each class.

**Python:**
```python
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))
```

→ See also: *Precision*, *Recall*, *F1-Score*

---

### Confusion Matrix 📌 🔥
A 2x2 table showing the counts of True Positives, True Negatives, False Positives, and False Negatives.

**Structure:**
```
                Predicted
                 NEG    POS
              ┌──────┬──────┐
Actual    NEG │  TN  │  FP  │
              ├──────┼──────┤
          POS │  FN  │  TP  │
              └──────┴──────┘
```

**Read as:**
- **Diagonal (TN, TP):** Correct predictions ✅
- **Off-diagonal (FP, FN):** Errors ❌

**Why it's critical:** Foundation for all classification metrics (precision, recall, F1, etc.)

**Python:**
```python
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
```

→ See also: *True Positive*, *True Negative*, *False Positive*, *False Negative*

---

## D

### Decision Boundary
The threshold that separates one class from another. In logistic regression with default settings, this is when predicted probability = 0.5.

**Adjusting the boundary:** Change the probability threshold to optimize for specific business goals.

→ See also: *Threshold*, *Logistic Regression*, *Sigmoid Function*

---

### Decision Threshold
See *Threshold*

---

## F

### F1-Score 📌
The harmonic mean of precision and recall, providing a single balanced metric.

**Formula:**
```
F1 = 2 × (Precision × Recall) / (Precision + Recall)
```

**Range:** 0 (worst) to 1 (perfect)

**When to use:**
- When you care equally about false positives and false negatives
- When you need a single metric for model comparison
- With imbalanced datasets

**Why harmonic mean?** Penalizes extreme values more than arithmetic mean. If either precision or recall is low, F1 will be low.

**Python:**
```python
from sklearn.metrics import f1_score
f1 = f1_score(y_test, y_pred)
```

→ See also: *Precision*, *Recall*, *Precision-Recall Tradeoff*

---

### False Alarm
Informal term for *False Positive*

→ See also: *False Positive*, *Type I Error*

---

### False Negative (FN) 📌 🔥
When the model predicts the negative class (0) but the actual class is positive (1).

**Medical example:** Test says "no cancer" but patient has cancer (missed diagnosis)

**Spam example:** Spam email reaches inbox (missed spam)

**Location in confusion matrix:** Bottom-left

**Also called:** Type II Error, missed detection

**Python access:**
```python
cm = confusion_matrix(y_test, y_pred)
fn = cm[1, 0]  # Row 1, Column 0
```

→ See also: *Confusion Matrix*, *Recall*, *Type II Error*

---

### False Negative Rate (FNR)
The proportion of actual positives that were incorrectly classified as negative.

**Formula:**
```
FNR = FN / (FN + TP) = 1 - Recall
```

→ See also: *False Negative*, *Recall*

---

### False Positive (FP) 📌 🔥
When the model predicts the positive class (1) but the actual class is negative (0).

**Medical example:** Test says "cancer" but patient is healthy (false alarm)

**Spam example:** Legitimate email goes to spam folder (blocked real email)

**Location in confusion matrix:** Top-right

**Also called:** Type I Error, false alarm

**Python access:**
```python
cm = confusion_matrix(y_test, y_pred)
fp = cm[0, 1]  # Row 0, Column 1
```

→ See also: *Confusion Matrix*, *Precision*, *Type I Error*

---

### False Positive Rate (FPR)
The proportion of actual negatives that were incorrectly classified as positive.

**Formula:**
```
FPR = FP / (FP + TN)
```

**Used in:** ROC curves (x-axis)

**Ideal value:** 0 (no false positives)

→ See also: *False Positive*, *ROC Curve*, *Specificity*

---

### Feature Scaling
The process of standardizing features to similar ranges. Important for logistic regression!

**Why it matters:** Logistic regression converges faster and performs better with scaled features.

**Common method:** StandardScaler (mean=0, std=1)

**Python:**
```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

**⚠️ Critical:** Fit on training data only!

→ See also: *StandardScaler*, *Preprocessing*, *Data Leakage*

---

## H

### Harmonic Mean
A type of average that penalizes extreme values more than arithmetic mean. Used in F1-score calculation.

**Why use it?** If either precision or recall is very low, the F1-score will be low (can't game the metric by optimizing just one).

→ See also: *F1-Score*

---

## L

### Logistic Regression 📌
A classification algorithm that models the probability of the positive class using a sigmoid function.

**Despite the name:** It's used for classification, not regression!

**Key components:**
1. Linear combination of features (like linear regression)
2. Sigmoid function to convert to probabilities (0 to 1)
3. Threshold to convert probabilities to class predictions

**Formula:**
```
P(y=1|X) = 1 / (1 + e^(-z))
where z = β₀ + β₁X₁ + β₂X₂ + ...
```

**Python:**
```python
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)
```

→ See also: *Sigmoid Function*, *Binary Classification*, *Threshold*

---

### Log Loss
(Preview for Week 3) A loss function for classification that penalizes confident wrong predictions more heavily.

→ See also: *Logistic Regression*

---

## M

### Majority Class
The class with the most samples in a dataset.

**Example:** In a dataset with 90 benign tumors and 10 malignant tumors, benign is the majority class.

**Relevance:** A "dumb" baseline model that always predicts the majority class will have 90% accuracy in this example!

→ See also: *Minority Class*, *Class Imbalance*, *Baseline Model*

---

### Minority Class
The class with fewer samples in a dataset.

**Often:** The more important class to detect (e.g., disease, fraud)

→ See also: *Majority Class*, *Class Imbalance*

---

### Misclassification
Any prediction error. Includes both false positives and false negatives.

→ See also: *False Positive*, *False Negative*, *Confusion Matrix*

---

## N

### Negative Class
In binary classification, typically labeled as class 0.

**Naming is arbitrary!** Don't assume "negative" means "bad" - it's just a label.

**Examples:**
- Medical: healthy (absence of disease)
- Spam: legitimate email
- Fraud: legitimate transaction

→ See also: *Positive Class*, *Binary Classification*

---

## O

### Odds
The ratio of the probability of an event occurring to the probability of it not occurring.

**Formula:**
```
Odds = P(event) / (1 - P(event))
```

**Example:** If P(cancer) = 0.75, then Odds = 0.75 / 0.25 = 3
(3:1 odds in favor of cancer)

**Relevance:** Logistic regression models log-odds (logit).

→ See also: *Logistic Regression*, *Probability*

---

## P

### Positive Class 📌
In binary classification, typically labeled as class 1. Usually the class of primary interest.

**Examples:**
- Medical: disease present
- Spam: spam email
- Fraud: fraudulent transaction
- Churn: customer will leave

**Why it matters:** Precision and recall are calculated with respect to the positive class!

→ See also: *Negative Class*, *Binary Classification*, *Precision*, *Recall*

---

### Precision 📌 🔥
Of all samples predicted as positive, what proportion were actually positive?

**Formula:**
```
Precision = TP / (TP + FP)
```

**Question answered:** "When I predict POSITIVE, how often am I right?"

**Mnemonic:** **P**recision = When I **P**redict **P**ositive

**Example:** Medical test with 100 positive predictions:
- 90 actually have disease (TP = 90)
- 10 are healthy (FP = 10)
- Precision = 90/100 = 90%

**When to optimize:** When false positives are costly
- Spam filter (don't block real emails!)
- Loan approval (don't reject good customers)

**Python:**
```python
from sklearn.metrics import precision_score
precision = precision_score(y_test, y_pred)
```

→ See also: *Recall*, *F1-Score*, *Precision-Recall Tradeoff*, *False Positive*

---

### Precision-Recall Tradeoff 🔥
The inverse relationship between precision and recall - improving one typically worsens the other.

**Why it happens:**
- To increase recall (catch more positives), you lower the threshold → more predictions → more false positives → lower precision
- To increase precision (be more confident), you raise the threshold → fewer predictions → miss some positives → lower recall

**Business decision:** Which metric to prioritize depends on the cost of each type of error!

**Visualization:** Precision-recall curve shows this tradeoff at different thresholds.

→ See also: *Precision*, *Recall*, *Threshold*, *F1-Score*

---

### predict() vs predict_proba() 🔥
Two different prediction methods in sklearn classifiers:

**predict():**
- Returns class labels (0 or 1)
- Uses default threshold (usually 0.5)
- Returns: `array([0, 1, 1, 0, ...])`

**predict_proba():**
- Returns probability estimates for each class
- Returns: `array([[0.7, 0.3], [0.2, 0.8], ...])`
- Each row sums to 1.0
- Column 0 = P(class 0), Column 1 = P(class 1)

**Python:**
```python
y_pred = model.predict(X_test)           # Hard predictions
y_pred_proba = model.predict_proba(X_test)  # Probabilities
```

**When to use probabilities:**
- Custom threshold adjustment
- ROC curve calculation
- Understanding model confidence
- Ranking predictions by certainty

→ See also: *Threshold*, *Logistic Regression*, *Probability*

---

### Preprocessing
Transforming raw data before training a model. For classification, often includes feature scaling.

**Common steps:**
1. Handle missing values
2. Encode categorical variables
3. Scale features (StandardScaler)
4. Feature engineering

**⚠️ Golden rule:** Fit on training data only!

→ See also: *Feature Scaling*, *StandardScaler*, *Data Leakage*

---

### Probability Threshold
See *Threshold*

---

## R

### Recall 📌 🔥
Of all actual positive samples, what proportion did the model correctly identify?

**Formula:**
```
Recall = TP / (TP + FN)
```

**Question answered:** "Of all actual POSITIVES, how many did I catch?"

**Mnemonic:** **R**ecall = Catch all **R**eal positives

**Also called:** Sensitivity, True Positive Rate (TPR)

**Example:** 100 patients with cancer:
- Test catches 85 (TP = 85)
- Test misses 15 (FN = 15)
- Recall = 85/100 = 85%

**When to optimize:** When false negatives are costly
- Cancer screening (don't miss cancer!)
- Fraud detection (catch all fraud)
- Safety systems (detect all failures)

**Python:**
```python
from sklearn.metrics import recall_score
recall = recall_score(y_test, y_pred)
```

→ See also: *Precision*, *F1-Score*, *Precision-Recall Tradeoff*, *False Negative*

---

### ROC Curve (Receiver Operating Characteristic) 📌
A plot showing the tradeoff between True Positive Rate (recall) and False Positive Rate at various threshold settings.

**Axes:**
- X-axis: False Positive Rate (FPR)
- Y-axis: True Positive Rate (TPR = Recall)

**Interpretation:**
- Diagonal line: Random guessing (AUC = 0.5)
- Curve above diagonal: Better than random
- Curve hugging top-left: Excellent model (high TPR, low FPR)

**Use case:** Comparing models (higher curve = better)

**Python:**
```python
from sklearn.metrics import roc_curve
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba[:, 1])
```

→ See also: *AUC*, *TPR*, *FPR*, *Threshold*

---

## S

### Sensitivity
Another name for *Recall* or *True Positive Rate*.

→ See also: *Recall*, *TPR*

---

### Sigmoid Function 📌
An S-shaped function that maps any real number to a value between 0 and 1. Core of logistic regression.

**Formula:**
```
σ(z) = 1 / (1 + e^(-z))
```

**Properties:**
- Input: Any real number (-∞ to +∞)
- Output: Value between 0 and 1
- At z=0: σ(0) = 0.5
- As z→∞: σ(z)→1
- As z→-∞: σ(z)→0

**Why it's useful:** Converts linear model output to probabilities!

**Visualization:**
```
1.0 ┤         ╭─────
    │       ╭─
    │     ╭─
0.5 ┤   ╭─
    │ ╭─
    ├─
0.0 ┤
    └───────────────
```

→ See also: *Logistic Regression*, *Probability*

---

### Specificity
The proportion of actual negatives correctly identified.

**Formula:**
```
Specificity = TN / (TN + FP) = 1 - FPR
```

**Interpretation:** "Of all actual negatives, how many did we correctly identify?"

**Contrast with:** *Recall* (which focuses on positives)

→ See also: *True Negative*, *False Positive Rate*, *ROC Curve*

---

### StandardScaler
A sklearn preprocessing tool that standardizes features to have mean=0 and standard deviation=1.

**Formula for each feature:**
```
X_scaled = (X - mean) / std
```

**Why use it:** Logistic regression performs better with scaled features.

**Python:**
```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  # Fit and transform
X_test_scaled = scaler.transform(X_test)        # Transform only
```

**⚠️ Critical:** Fit on training data, transform both sets!

→ See also: *Feature Scaling*, *Preprocessing*, *Data Leakage*

---

### Supervised Learning
Machine learning where the training data includes both features (X) and labels (y).

**Types:**
- **Classification:** Predict categories (Week 2)
- **Regression:** Predict continuous values (Week 1)

**Contrast with:** *Unsupervised Learning* (no labels, Week 5)

→ See also: *Classification*, *Regression*

---

## T

### Target Variable
The variable you're trying to predict (y). In classification, this is the class label.

**Also called:** Label, output, dependent variable, response variable

→ See also: *Class Label*, *Feature*

---

### Threshold 📌
The probability cutoff for converting predicted probabilities to class predictions.

**Default:** 0.5
- If P(class 1) ≥ 0.5 → Predict class 1
- If P(class 1) < 0.5 → Predict class 0

**Adjusting the threshold:**
- **Lower threshold (e.g., 0.3):** More predictions of class 1 → Higher recall, lower precision
- **Higher threshold (e.g., 0.7):** Fewer predictions of class 1 → Lower recall, higher precision

**Business example:** In cancer screening, use threshold=0.3 to catch more cases (optimize recall), accepting more false alarms.

**Python:**
```python
# Custom threshold
threshold = 0.3
y_pred_custom = (y_pred_proba[:, 1] >= threshold).astype(int)
```

→ See also: *Precision-Recall Tradeoff*, *predict_proba()*, *ROC Curve*

---

### TPR (True Positive Rate)
Another name for *Recall*.

**Formula:**
```
TPR = TP / (TP + FN) = Recall
```

**Used in:** ROC curves (y-axis)

→ See also: *Recall*, *ROC Curve*, *Sensitivity*

---

### True Negative (TN) 📌
When the model correctly predicts the negative class.

**Medical example:** Test says "no cancer" and patient is healthy ✅

**Spam example:** Legitimate email goes to inbox ✅

**Location in confusion matrix:** Top-left

**Python access:**
```python
cm = confusion_matrix(y_test, y_pred)
tn = cm[0, 0]  # Row 0, Column 0
```

→ See also: *Confusion Matrix*, *Specificity*

---

### True Positive (TP) 📌
When the model correctly predicts the positive class.

**Medical example:** Test says "cancer" and patient has cancer ✅

**Spam example:** Spam email goes to spam folder ✅

**Location in confusion matrix:** Bottom-right

**Python access:**
```python
cm = confusion_matrix(y_test, y_pred)
tp = cm[1, 1]  # Row 1, Column 1
```

→ See also: *Confusion Matrix*, *Precision*, *Recall*

---

### Type I Error
Statistical term for *False Positive* - rejecting a true null hypothesis.

→ See also: *False Positive*

---

### Type II Error
Statistical term for *False Negative* - failing to reject a false null hypothesis.

→ See also: *False Negative*

---

## Quick Reference Tables

### Confusion Matrix Positions
```
                Predicted
                 0      1
              ┌──────┬──────┐
Actual     0  │  TN  │  FP  │
              ├──────┼──────┤
           1  │  FN  │  TP  │
              └──────┴──────┘
```

### Metric Formulas
| Metric | Formula | Focus |
|--------|---------|-------|
| Accuracy | (TP + TN) / Total | Overall correctness |
| Precision | TP / (TP + FP) | Positive predictions |
| Recall | TP / (TP + FN) | Actual positives |
| F1-Score | 2×(P×R)/(P+R) | Balance both |
| Specificity | TN / (TN + FP) | Negative identification |

### When to Use Which Metric
| Scenario | Optimize | Why |
|----------|----------|-----|
| Cancer screening | Recall | Don't miss cancer (FN deadly) |
| Spam filter | Precision | Don't block real emails (FP costly) |
| Fraud detection | Recall | Catch all fraud (FN costly) |
| Loan approval | Precision | Don't reject good customers (FP costly) |
| Balanced data | F1 or Accuracy | Both errors equally costly |

---

**Master these terms and you'll excel at classification!** 🎓

---

*Week 2 Glossary v1.0 | December 2025*
