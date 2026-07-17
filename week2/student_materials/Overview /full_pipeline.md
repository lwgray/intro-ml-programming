# Understanding ROC Curves: The Complete Pipeline

---

## Step 1: The Raw Data

Imagine we work at a hospital and we want to **predict who is sick** based on two measurements: body temperature and white blood cell count (WBC). We collected data from 10 patients where we already know whether they were sick or healthy.

| Person | Temperature (°F) | WBC Count (×1000) | Actually |
|--------|-----------------|-------------------|----------|
| A | 102.5 | 14.2 | Sick |
| B | 101.8 | 13.1 | Sick |
| C | 101.0 | 11.5 | Sick |
| D | 100.5 | 10.8 | Sick |
| E | 99.8 | 9.5 | Sick |
| F | 98.6 | 7.0 | Healthy |
| G | 98.2 | 6.5 | Healthy |
| H | 98.8 | 7.8 | Healthy |
| I | 97.9 | 6.0 | Healthy |
| J | 98.0 | 5.5 | Healthy |

---

## Step 2: Training a Logistic Regression Model

We feed this data into a logistic regression model. The model needs to learn the right coefficients (weights) for each feature. It does this through **gradient descent** — an iterative optimization process where:

1. The model starts with random coefficients
2. It makes predictions with those coefficients
3. It measures how wrong those predictions are using a loss function (log loss)
4. It adjusts the coefficients slightly in the direction that reduces the error
5. It repeats steps 2–4 thousands of times until the coefficients converge

After gradient descent finishes, the model has learned coefficients like:

**P(sick) = sigmoid(−50 + 0.3 × Temperature + 0.2 × WBC)**

The sigmoid function squishes the output into a probability between 0 and 1. The coefficients (0.3 for temperature, 0.2 for WBC) were found by gradient descent — they weren't set by hand. The model learned that higher temperature and higher WBC both increase the probability of being sick.

---

## Step 3: Three Different Models

Now let's see what happens when we train logistic regression on different quality features. The quality of the features determines how well the model can separate sick from healthy, which directly affects the ROC curve.

---

### Scenario 1: Excellent Model (AUC ≈ 1.00)

Trained on temperature and WBC — features that are strongly related to being sick. Gradient descent found coefficients that cleanly separate the two groups.

| Person | Temperature | WBC | Model Score | Actually |
|--------|------------|-----|-------------|----------|
| A | 102.5 | 14.2 | 0.97 | Sick |
| B | 101.8 | 13.1 | 0.92 | Sick |
| C | 101.0 | 11.5 | 0.85 | Sick |
| D | 100.5 | 10.8 | 0.78 | Sick |
| E | 99.8 | 9.5 | 0.62 | Sick |
| F | 98.8 | 7.8 | 0.18 | Healthy |
| G | 98.6 | 7.0 | 0.13 | Healthy |
| H | 98.2 | 6.5 | 0.09 | Healthy |
| I | 97.9 | 6.0 | 0.05 | Healthy |
| J | 98.0 | 5.5 | 0.03 | Healthy |

Notice the clear gap — the lowest sick score (0.62) is far above the highest healthy score (0.18).

**Threshold = 0.90:**
- TPR = 2/5 = 0.4 | FPR = 0/5 = 0.0 | Point: (0.0, 0.4)

| | Predicted Sick | Predicted Healthy |
|--|---------------|-------------------|
| **Actually Sick** | 2 (TP) | 3 (FN) |
| **Actually Healthy** | 0 (FP) | 5 (TN) |

**Threshold = 0.50:**
- TPR = 5/5 = 1.0 | FPR = 0/5 = 0.0 | Point: (0.0, 1.0)

| | Predicted Sick | Predicted Healthy |
|--|---------------|-------------------|
| **Actually Sick** | 5 (TP) | 0 (FN) |
| **Actually Healthy** | 0 (FP) | 5 (TN) |

Perfect confusion matrix. Because the scores are so well separated, there's a threshold that catches every sick person without flagging any healthy person.

**Threshold = 0.01:**
- TPR = 5/5 = 1.0 | FPR = 5/5 = 1.0 | Point: (1.0, 1.0)

| | Predicted Sick | Predicted Healthy |
|--|---------------|-------------------|
| **Actually Sick** | 5 (TP) | 0 (FN) |
| **Actually Healthy** | 5 (FP) | 0 (TN) |

**The curve shoots up along the y-axis and across the top, hugging the top-left corner.**

![ROC Curve — Excellent Model](roc_excellent.png)

---

### Scenario 2: OK Model (AUC ≈ 0.76)

Trained on temperature only — a decent but imperfect feature. Some healthy people have slightly elevated temperatures and some sick people have mild temperatures, so gradient descent found coefficients that partially separate the groups but with overlap.

| Person | Temperature | Model Score | Actually |
|--------|------------|-------------|----------|
| A | 102.5 | 0.90 | Sick |
| B | 101.8 | 0.75 | Sick |
| C | 101.0 | 0.55 | Sick |
| D | 100.5 | 0.40 | Sick |
| E | 99.8 | 0.25 | Sick |
| F | 98.8 | 0.70 | Healthy |
| G | 98.6 | 0.45 | Healthy |
| H | 98.2 | 0.35 | Healthy |
| I | 97.9 | 0.15 | Healthy |
| J | 98.0 | 0.10 | Healthy |

Notice the overlap — Healthy Person F (0.70) scores higher than Sick Person D (0.40) and Sick Person E (0.25).

**Threshold = 0.80:**
- TPR = 1/5 = 0.2 | FPR = 0/5 = 0.0 | Point: (0.0, 0.2)

| | Predicted Sick | Predicted Healthy |
|--|---------------|-------------------|
| **Actually Sick** | 1 (TP) | 4 (FN) |
| **Actually Healthy** | 0 (FP) | 5 (TN) |

Very conservative — only catches the most obvious case.

**Threshold = 0.60:**
- Classified as sick: A (0.90), B (0.75), F (0.70) — but F is healthy.
- TPR = 2/5 = 0.4 | FPR = 1/5 = 0.2 | Point: (0.2, 0.4)

| | Predicted Sick | Predicted Healthy |
|--|---------------|-------------------|
| **Actually Sick** | 2 (TP) | 3 (FN) |
| **Actually Healthy** | 1 (FP) | 4 (TN) |

Trying to catch more sick people has started pulling in healthy people too.

**Threshold = 0.30:**
- TPR = 4/5 = 0.8 | FPR = 2/5 = 0.4 | Point: (0.4, 0.8)

| | Predicted Sick | Predicted Healthy |
|--|---------------|-------------------|
| **Actually Sick** | 4 (TP) | 1 (FN) |
| **Actually Healthy** | 2 (FP) | 3 (TN) |

We're catching most sick people, but the cost is growing — 2 healthy people are now being told they're sick.

**Threshold = 0.01:**
- TPR = 1.0 | FPR = 1.0 | Point: (1.0, 1.0)

| | Predicted Sick | Predicted Healthy |
|--|---------------|-------------------|
| **Actually Sick** | 5 (TP) | 0 (FN) |
| **Actually Healthy** | 5 (FP) | 0 (TN) |

**The curve bows moderately above the diagonal.**

![ROC Curve — OK Model](roc_ok.png)

---

### Scenario 3: Bad Model (AUC ≈ 0.40)

Trained on shoe size and hair length — features that have absolutely nothing to do with being sick. Gradient descent tried its best but couldn't find any meaningful relationship, so the coefficients it found are essentially noise. The resulting scores are randomly scattered with no pattern.

| Person | Shoe Size | Hair Length | Model Score | Actually |
|--------|----------|-------------|-------------|----------|
| A | 10 | 6 in | 0.85 | Sick |
| B | 8 | 12 in | 0.50 | Sick |
| C | 9 | 18 in | 0.30 | Sick |
| D | 7 | 4 in | 0.20 | Sick |
| E | 11 | 22 in | 0.10 | Sick |
| F | 6 | 8 in | 0.80 | Healthy |
| G | 12 | 3 in | 0.60 | Healthy |
| H | 9 | 14 in | 0.45 | Healthy |
| I | 8 | 10 in | 0.35 | Healthy |
| J | 10 | 20 in | 0.15 | Healthy |

The scores are completely mixed. Sick and healthy people have scores scattered all over the place.

**Threshold = 0.70:**
- Classified as sick: A (0.85), F (0.80) — 1 sick and 1 healthy.
- TPR = 1/5 = 0.2 | FPR = 1/5 = 0.2 | Point: (0.2, 0.2)

| | Predicted Sick | Predicted Healthy |
|--|---------------|-------------------|
| **Actually Sick** | 1 (TP) | 4 (FN) |
| **Actually Healthy** | 1 (FP) | 4 (TN) |

TP and FP are equal. For every sick person we catch, we're incorrectly flagging a healthy person too.

**Threshold = 0.40:**
- Classified as sick: A, F, G, B, H — 2 sick and 3 healthy.
- TPR = 2/5 = 0.4 | FPR = 3/5 = 0.6 | Point: (0.6, 0.4)

| | Predicted Sick | Predicted Healthy |
|--|---------------|-------------------|
| **Actually Sick** | 2 (TP) | 3 (FN) |
| **Actually Healthy** | 3 (FP) | 2 (TN) |

Worse than random — we're flagging more healthy people (3) than we're catching sick people (2).

**Threshold = 0.01:**
- TPR = 1.0 | FPR = 1.0 | Point: (1.0, 1.0)

| | Predicted Sick | Predicted Healthy |
|--|---------------|-------------------|
| **Actually Sick** | 5 (TP) | 0 (FN) |
| **Actually Healthy** | 5 (FP) | 0 (TN) |

**The curve sits right along the diagonal.**

![ROC Curve — Bad Model](roc_bad.png)

---

## Step 4: Comparing All Three Models

![ROC Curve Comparison — All Three Models](roc_comparison.png)

The confusion matrices across the three models reveal what the ROC curve is showing:

- **Excellent model (temperature + WBC):** TP increases quickly while FP stays at 0 for a long time. Gradient descent found strong coefficients because the features genuinely relate to sickness. The curve hugs the top-left. AUC near 1.0.

- **OK model (temperature only):** TP increases but FP creeps up alongside it. Gradient descent found a partial relationship, but one feature alone isn't enough for clean separation. The curve bows above the diagonal. AUC around 0.76.

- **Bad model (shoe size + hair length):** TP and FP increase at the same rate. Gradient descent couldn't find any meaningful relationship because there isn't one. The curve follows the diagonal. AUC near 0.50.

---

## Step 5: What Is a Good AUC?

![AUC Interpretation Guide](auc_guide.png)

| AUC Range | Interpretation | What It Means |
|-----------|---------------|---------------|
| 1.0 | Perfect | Complete separation between classes |
| 0.9 – 1.0 | Excellent | Model almost always ranks a positive higher than a negative |
| 0.8 – 0.9 | Good | Model has strong discriminative ability |
| 0.7 – 0.8 | Fair | Model is useful but makes notable mistakes |
| 0.6 – 0.7 | Poor | Model has weak discriminative ability |
| 0.5 | Random | No discrimination — equivalent to flipping a coin |
| Below 0.5 | Worse than random | Model is systematically wrong (may have labels flipped) |

What counts as "good enough" depends on your use case. In cancer screening, you might need an AUC of 0.95+ because missing a sick patient is very costly. In spam filtering, an AUC of 0.80 might be perfectly acceptable.

There's also a helpful intuitive interpretation of AUC: **it's the probability that if you randomly pick one positive example and one negative example, the model gives the positive example a higher score.** So an AUC of 0.90 means if you randomly grab a sick person and a healthy person, there's a 90% chance the model assigned a higher probability to the sick person.

---

## The Complete Pipeline Summary

1. **Collect raw data** — features like temperature and WBC, plus the true label of sick or healthy
2. **Train a logistic regression model** — gradient descent iteratively adjusts the coefficients to minimize prediction error, finding the best weights for each feature
3. **The model outputs probability scores** for each person based on the learned coefficients
4. **Choose a threshold** to convert probabilities into yes/no predictions
5. **The ROC curve** shows the TPR vs FPR tradeoff at every possible threshold, telling you how well the model separates sick from healthy
6. **The confusion matrix** at any given threshold shows the exact counts of TP, FP, TN, and FN
7. **The AUC** summarizes the model's separation ability in a single number — closer to 1.0 means the model truly learned to distinguish sick from healthy, closer to 0.5 means it's guessing

---

## Key Definitions Quick Reference

| Term | Formula | Meaning |
|------|---------|---------|
| **Precision** | TP / (TP + FP) | Of those predicted positive, how many are correct? |
| **Recall (TPR)** | TP / (TP + FN) | Of all actual positives, how many did we catch? |
| **False Positive Rate** | FP / (FP + TN) | Of all actual negatives, how many did we incorrectly flag? |
| **Specificity** | TN / (TN + FP) | Of all actual negatives, how many did we correctly identify? (1 − FPR) |
| **AUC** | Area under the ROC curve | Overall measure of how well the model separates the two classes |
