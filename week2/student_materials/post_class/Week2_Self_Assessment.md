# Week 2: Classification - Self-Assessment

**Purpose:** Evaluate your understanding of Week 2 concepts
**Time:** 20-30 minutes
**Instructions:** Answer honestly - this is for YOUR learning, not grading!

---

## How to Use This Assessment

1. **Complete AFTER** finishing the post-class exercise
2. **Answer without looking at notes** first
3. **Then check your answers** against the glossary and materials
4. **Identify gaps** in your understanding
5. **Review weak areas** before Week 3

---

## Part 1: Concept Mastery (Rate Your Confidence)

For each concept, rate your confidence level:
- **5 - Expert:** Could teach this to someone else
- **4 - Proficient:** Comfortable using in practice
- **3 - Adequate:** Understand with occasional reference
- **2 - Developing:** Need review and practice
- **1 - Novice:** Didn't understand yet

### Core Concepts

| Concept | Confidence (1-5) | Notes |
|---------|------------------|-------|
| **Binary classification** | ___ | |
| **Logistic regression** | ___ | |
| **Sigmoid function** | ___ | |
| **Probability threshold** | ___ | |
| **Confusion matrix structure** | ___ | |
| **True Positive (TP)** | ___ | |
| **True Negative (TN)** | ___ | |
| **False Positive (FP)** | ___ | |
| **False Negative (FN)** | ___ | |
| **Accuracy metric** | ___ | |
| **When accuracy is misleading** | ___ | |
| **Precision metric** | ___ | |
| **Recall metric** | ___ | |
| **F1-score** | ___ | |
| **Precision-recall tradeoff** | ___ | |
| **ROC curve** | ___ | |
| **AUC score** | ___ | |
| **Class imbalance** | ___ | |
| **predict() vs predict_proba()** | ___ | |
| **Feature scaling for classification** | ___ | |

**Total confidence points:** _____ / 100

**Interpretation:**
- 80-100: Excellent! You've mastered Week 2
- 60-79: Good understanding, review concepts rated < 4
- 40-59: Adequate grasp, significant review needed
- < 40: Need to revisit core concepts before Week 3

---

## Part 2: Knowledge Check Questions

### Section A: Confusion Matrix (THE FOUNDATION!)

**Question 1:** Draw a confusion matrix from memory and label all four quadrants.

```
Draw here:








```

**Self-check:** Compare with Week2_Glossary.md. Did you get it right?
☐ Yes, perfectly
☐ Close, minor errors
☐ Significant errors
☐ Couldn't remember

---

**Question 2:** Given this confusion matrix, calculate the metrics:

```
                Predicted
                 0      1
              ┌──────┬──────┐
Actual     0  │  85  │  15  │
              ├──────┼──────┤
           1  │  10  │  90  │
              └──────┴──────┘
```

Calculate WITHOUT a calculator (approximate is fine):

a) **Accuracy** = _____ / _____ = _____ (≈____%)

b) **Precision** = _____ / _____ = _____ (≈____%)

c) **Recall** = _____ / _____ = _____ (≈____%)

d) **F1-Score** = 2 × (_____ × _____) / (_____ + _____) = _____ (≈____%)

**Self-check:**
- Accuracy: (85+90)/200 = 0.875 (87.5%)
- Precision: 90/(90+15) = 0.857 (85.7%)
- Recall: 90/(90+10) = 0.900 (90%)
- F1: 2×(0.857×0.900)/(0.857+0.900) = 0.878 (87.8%)

**How did you do?**
☐ All correct
☐ 3/4 correct
☐ 2/4 correct
☐ 0-1/4 correct

---

### Section B: Precision vs Recall

**Question 3:** In your own words, explain:

a) **What is precision?**

___________________________________________________________________

___________________________________________________________________

___________________________________________________________________

b) **What is recall?**

___________________________________________________________________

___________________________________________________________________

___________________________________________________________________

c) **Why can't you maximize both simultaneously?**

___________________________________________________________________

___________________________________________________________________

___________________________________________________________________

**Self-check:** Compare your answers to Week2_Glossary.md entries for precision and recall.

---

**Question 4:** For each scenario, which metric should you optimize?

| Scenario | Optimize | Why? |
|----------|----------|------|
| **Spam email filter** | ☐ Precision<br>☐ Recall<br>☐ F1 | _________________ |
| **Cancer screening** | ☐ Precision<br>☐ Recall<br>☐ F1 | _________________ |
| **Fraud detection** | ☐ Precision<br>☐ Recall<br>☐ F1 | _________________ |
| **Loan approval** | ☐ Precision<br>☐ Recall<br>☐ F1 | _________________ |

**Self-check:**
- Spam: Precision (don't block real emails)
- Cancer: Recall (don't miss cancer cases)
- Fraud: Recall (catch all fraud)
- Loan: Depends on business (precision = don't reject good customers)

---

### Section C: When Accuracy Lies

**Question 5:** A disease affects 1% of the population. A "dumb" model always predicts "no disease."

a) What is the accuracy of this model? _____%

b) What is the recall for detecting the disease? _____%

c) Is this model useful? Why or why not?

___________________________________________________________________

___________________________________________________________________

___________________________________________________________________

**Self-check:**
- Accuracy: 99% (correct on 99% who don't have disease)
- Recall: 0% (catches zero disease cases)
- Useful: NO! Useless despite high accuracy - misses all actual cases

---

### Section D: Technical Implementation

**Question 6:** What's wrong with this code?

```python
# Load data
X, y = load_data()

# Preprocess
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2
)

# Train
model = LogisticRegression()
model.fit(X_train, y_train)
```

**What's the problem?**

___________________________________________________________________

___________________________________________________________________

**How would you fix it?**

___________________________________________________________________

___________________________________________________________________

**Self-check:** Data leakage! Split BEFORE preprocessing. The scaler saw test data statistics, which leaks information.

---

**Question 7:** Complete this code to get probability predictions:

```python
model = LogisticRegression()
model.fit(X_train, y_train)

# Get class predictions (0 or 1)
y_pred = model._________(X_test)

# Get probability predictions
y_pred_proba = model._________(X_test)

# Get probability of positive class only
prob_positive = y_pred_proba[:, ___]
```

**Self-check:**
```python
y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)
prob_positive = y_pred_proba[:, 1]
```

---

### Section E: ROC and AUC

**Question 8:** True or False?

| Statement | T/F | Explanation if False |
|-----------|-----|---------------------|
| An AUC of 0.5 means the model is perfect | ___ | ___________________ |
| An AUC of 0.9 is considered excellent | ___ | ___________________ |
| ROC curve plots precision vs recall | ___ | ___________________ |
| Higher AUC always means better for my problem | ___ | ___________________ |
| AUC is threshold-independent | ___ | ___________________ |

**Self-check:**
1. FALSE - 0.5 is random guessing, 1.0 is perfect
2. TRUE - 0.9-1.0 is excellent range
3. FALSE - ROC plots TPR (recall) vs FPR
4. FALSE - Need to consider business context and which errors matter more
5. TRUE - AUC summarizes performance across all thresholds

---

## Part 3: Practical Application

### Scenario: Medical Diagnosis

You built a heart disease classifier with these results:

```
Test set: 100 patients (40 with disease, 60 healthy)

Confusion Matrix (threshold=0.5):
              Predicted
               Healthy  Disease
            ┌─────────┬─────────┐
Actual  H   │   55    │    5    │
            ├─────────┼─────────┤
        D   │   8     │   32    │
            └─────────┴─────────┘
```

**Question 9:** Answer these questions:

a) Calculate accuracy: ________

b) Calculate recall for disease class: ________

c) How many disease cases did the model miss? ________

d) If you lower the threshold to 0.3, what will likely happen to:
   - Recall: ☐ Increase  ☐ Decrease  ☐ Stay same
   - Precision: ☐ Increase  ☐ Decrease  ☐ Stay same
   - False Negatives: ☐ Increase  ☐ Decrease  ☐ Stay same

e) Would you recommend using this model in production? Why or why not?

___________________________________________________________________

___________________________________________________________________

___________________________________________________________________

**Self-check:**
- a) Accuracy: (55+32)/100 = 87%
- b) Recall: 32/(32+8) = 80%
- c) Missed: 8 cases (false negatives)
- d) Lower threshold: Recall ↑, Precision ↓, FN ↓
- e) Depends! 80% recall means missing 20% of diseases - may need threshold tuning or better features

---

## Part 4: Reflection

### What I Learned

**Question 10:** What are the three most important things you learned in Week 2?

1. ___________________________________________________________________

   ___________________________________________________________________

2. ___________________________________________________________________

   ___________________________________________________________________

3. ___________________________________________________________________

   ___________________________________________________________________

---

### What I Still Need to Work On

**Question 11:** Which concepts do you need to review?

☐ Confusion matrix interpretation
☐ Calculating metrics by hand
☐ Choosing the right metric for business context
☐ Understanding precision-recall tradeoff
☐ ROC curves and AUC
☐ Feature scaling
☐ predict() vs predict_proba()
☐ Threshold tuning
☐ Class imbalance issues
☐ Other: ________________

---

### Comparison to Week 1

**Question 13:** How is classification (Week 2) different from regression (Week 1)?

**Differences:**

___________________________________________________________________

___________________________________________________________________

___________________________________________________________________

**Similarities:**

___________________________________________________________________

___________________________________________________________________

___________________________________________________________________

---

## Part 4.5: Day 2 Deep Dive Reflection

*Complete this section after Day 2 class imbalance and guided practice session*

### The Accuracy Trap

**Question 12a:** In your own words, explain why 99% accuracy can be useless.

___________________________________________________________________

___________________________________________________________________

___________________________________________________________________

**Give a real-world example from Day 2:**

___________________________________________________________________

___________________________________________________________________

**Self-check:** Did you mention class imbalance and the baseline model problem? (E.g., fraud detection with 99% legitimate transactions - a "dumb" model predicting "no fraud" gets 99% accuracy but catches zero fraud)

---

### Metric Selection Framework

**Question 12b:** For each scenario, which error is MORE COSTLY and which metric should you optimize?

| Scenario | FN More Costly or FP? | Why? | Optimize Which Metric? |
|----------|----------------------|------|------------------------|
| **Heart disease screening** | ☐ FN  ☐ FP | _____________ | ☐ Precision  ☐ Recall |
| **Credit card fraud** | ☐ FN  ☐ FP | _____________ | ☐ Precision  ☐ Recall |
| **Marketing email** | ☐ FN  ☐ FP | _____________ | ☐ Precision  ☐ Recall |
| **Airport security** | ☐ FN  ☐ FP | _____________ | ☐ Precision  ☐ Recall |

**Self-check:**
- Heart disease: FN more costly (miss disease = fatal) → Optimize **Recall**
- Fraud: FN more costly (miss fraud = losses) → Optimize **Recall**
- Marketing: FP more costly (annoy customer) → Optimize **Precision**
- Airport security: FN more costly (miss threat = catastrophic) → Optimize **Recall**

**Pattern:** When negative outcome is dangerous → Optimize Recall (minimize FN)

---

### Class Imbalance Strategies

**Question 12c:** You have a dataset with 95% class 0 and 5% class 1. What should you do?

Check all that apply:
- ☐ Use accuracy as your primary metric
- ☐ Use precision, recall, and F1 instead of accuracy
- ☐ Apply `class_weight='balanced'` in sklearn
- ☐ Ignore the imbalance - it doesn't matter
- ☐ Use stratified splitting
- ☐ Consider resampling techniques (SMOTE)

**Self-check:**
Correct answers: 2, 3, 5, 6 (NOT 1 or 4!)
- Never rely on accuracy with >10:1 imbalance
- Always use class weights or resampling
- Stratified split maintains class balance in train/test
- SMOTE (Week 5 topic) can help with extreme imbalance

---

### Threshold Tuning

**Question 12d:** Complete this statement:

"Lowering the decision threshold from 0.5 to 0.3 will:
- **Increase** _________________ (which metric?)
- **Decrease** _________________ (which metric?)
- **Reduce** _________________ (which type of error?)
- **Increase** _________________ (which type of error?)"

**Self-check:**
- Increase: **Recall** (catch more positives)
- Decrease: **Precision** (more false alarms)
- Reduce: **False Negatives** (FN)
- Increase: **False Positives** (FP)

---

**Question 12e:** Given costs: FN = $100,000, FP = $2,000

Would you recommend:
- ☐ Higher threshold (0.7) - fewer predictions of positive class
- ☐ Lower threshold (0.3) - more predictions of positive class
- ☐ Keep default (0.5)

**Why?**

___________________________________________________________________

___________________________________________________________________

**Self-check:** Lower threshold (0.3) because FN is 50x more expensive. Better to accept more $2K false alarms than risk $100K missed cases.

---

### ROC and AUC Deep Understanding

**Question 12f:** Match the AUC score to its meaning:

| AUC Score | Meaning |
|-----------|---------|
| 0.5 | ___ a) Excellent discrimination |
| 0.7 | ___ b) Random guessing |
| 0.85 | ___ c) Good discrimination |
| 0.95 | ___ d) Fair discrimination |

**Self-check:** 0.5→b, 0.7→d, 0.85→c, 0.95→a

---

**Question 12g:** True or False?

| Statement | T/F |
|-----------|-----|
| You can use AUC to choose the best threshold for your specific business problem | ___ |
| AUC tells you overall model discrimination ability | ___ |
| A model with AUC=0.9 is always better than AUC=0.8 for production use | ___ |
| ROC curve is useful when you have balanced classes | ___ |
| Precision-Recall curve is better than ROC for highly imbalanced data | ___ |

**Self-check:**
1. FALSE - AUC is threshold-independent; use precision-recall curve or cost analysis for threshold choice
2. TRUE - That's exactly what AUC measures
3. FALSE - Must consider business context, costs, and which errors matter more
4. TRUE - But also useful for imbalanced classes
5. TRUE - PR curve focuses on positive class performance, better for imbalanced scenarios

---

### Guided Practice Reflection

**Question 12h:** During Day 2 Heart Disease guided practice, what was your biggest "aha!" moment?

___________________________________________________________________

___________________________________________________________________

___________________________________________________________________

**What concept from Day 2 are you still uncertain about?**

___________________________________________________________________

___________________________________________________________________

**Action:** ☐ I will review this concept before Week 3 by _________________

---

## Part 5: Action Plan

### Before Week 3

Based on your self-assessment, what will you do to prepare for Week 3?

**Concepts to review:**

1. ___________________________________________________________________

2. ___________________________________________________________________

3. ___________________________________________________________________

**Practice exercises:**

☐ Redraw confusion matrix until I can do it from memory
☐ Practice calculating precision/recall by hand
☐ Re-run post-class exercise with different dataset
☐ Complete bonus threshold tuning exercise
☐ Teach these concepts to someone else
☐ Review Week 2 glossary
☐ Re-watch StatQuest videos
☐ Other: ________________

---

## Part 6: Learning Effectiveness

### How confident do you feel about Week 2 material?

**Overall confidence (1-10):** _____

1-3: Need significant review
4-6: Adequate understanding, need practice
7-9: Strong understanding
10: Mastery - could teach others

### What helped you learn most effectively?

☐ Live session coding along
☐ Pair programming exercise
☐ Post-class homework
☐ Bonus threshold tuning exercise
☐ Reading glossary/documentation
☐ Practicing by hand (drawing, calculating)
☐ Discussion with classmates
☐ Re-watching video tutorials
☐ Trial and error with code

**Most effective learning activity for me:**

___________________________________________________________________

___________________________________________________________________

### What could improve your learning?

___________________________________________________________________

___________________________________________________________________

___________________________________________________________________

---

## Part 7: Growth Mindset Check

### Challenges This Week

**Question 14:** What was the most challenging concept this week?

___________________________________________________________________

___________________________________________________________________

**How did you overcome it (or how will you)?**

___________________________________________________________________

___________________________________________________________________

___________________________________________________________________

---

### Mistakes and Learning

**Question 15:** What mistake did you make this week that taught you something important?

___________________________________________________________________

___________________________________________________________________

**What did you learn from it?**

___________________________________________________________________

___________________________________________________________________

---

## Assessment Complete!

### Scoring Guide

**Count your totals:**

- **Part 1 (Confidence):** _____ / 100 points
- **Part 2 (Knowledge Check):** _____ / 8 questions fully correct
- **Part 3 (Practical Application):** Completed? ☐ Yes  ☐ No

### Interpretation

**If you scored:**

**90-100% on Part 1 + 7-8/8 on Part 2:**
- Excellent mastery! You're ready for Week 3.
- Consider the bonus exercise for deeper learning.
- Could you mentor a classmate?

**70-89% on Part 1 + 5-6/8 on Part 2:**
- Good understanding with some gaps.
- Review concepts rated < 4 in confidence.
- Practice calculating metrics by hand.
- Complete bonus exercise if time permits.

**50-69% on Part 1 + 3-4/8 on Part 2:**
- Adequate grasp but significant review needed.
- Focus on confusion matrix until it's automatic.
- Re-do post-class exercise slowly.
- Review glossary and cheat sheet.
- Attend office hours or ask questions in forum.

**< 50% on Part 1 + 0-2/8 on Part 2:**
- Need substantial review before Week 3.
- Schedule time to revisit core concepts.
- Re-watch live session recording.
- Work through solutions notebook step-by-step.
- Consider reaching out for 1-on-1 help.

---

## Next Steps

### Immediate Actions

Based on your assessment, what will you do RIGHT NOW?

1. ___________________________________________________________________

2. ___________________________________________________________________

3. ___________________________________________________________________

### Before Week 3 Live Session

**Goal:** Enter Week 3 with solid Week 2 foundation

☐ Review all concepts rated < 4 in Part 1
☐ Practice drawing confusion matrix from memory
☐ Review Week 2 glossary completely
☐ Re-attempt questions you got wrong
☐ Complete bonus exercise (if ready)
☐ Ask questions in forum about unclear concepts
☐ Review Week 2 cheat sheet

---

## Instructor Note

**This self-assessment is for YOUR benefit, not for grading.**

- Be honest about your understanding
- Identify gaps early while material is fresh
- Use this to guide your review
- Reach out if you need help!

**Remember:** Everyone learns at different paces. What matters is continuous improvement and asking for help when needed.

---

**Great work completing Week 2!** 🎓

**Ready for Week 3: Decision Trees and Random Forests!**

---

*Week 2 Self-Assessment v1.0 | December 2025*
