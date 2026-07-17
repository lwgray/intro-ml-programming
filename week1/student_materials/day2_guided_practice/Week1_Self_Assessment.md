# Week 1: Self-Assessment Checklist

**Purpose:** Evaluate your understanding of Week 1 concepts
**When to use:** After completing all Week 1 activities (live session, pair programming, homework)
**Time:** 15-20 minutes

---

## 📋 How to Use This Checklist

**Be honest with yourself!** This is for YOUR benefit, not graded.

**For each item:**
- ✅ Check if you can do it confidently
- ⚠️ Mark if you need review
- ❌ Mark if you're still confused

**After completing:**
- Review materials for items marked ⚠️ or ❌
- Ask questions in discussion forum or office hours
- Revisit this checklist before Week 2

---

## Part 1: Conceptual Understanding

### Machine Learning Pipeline

- [ ] I can explain what machine learning is in simple terms
- [ ] I can list the 5 steps of an ML pipeline (Load, Split, Train, Predict, Evaluate)
- [ ] I understand why we split data into training and test sets
- [ ] I can explain what happens if we skip the train-test split
- [ ] I understand why we must split BEFORE preprocessing (data leakage prevention)

**If you checked all boxes:** ✅ Great! You understand the ML pipeline.

**If you missed any:** Review [Teaching Guide Section 5 (Segment 2)], [Pre-Class Study Guide]

---

### Linear Regression Fundamentals

- [ ] I can explain what linear regression is in one sentence
- [ ] I understand that linear regression predicts continuous values (not categories)
- [ ] I can write the linear regression equation: y = β₀ + β₁X₁ + β₂X₂ + ...
- [ ] I understand what the intercept (β₀) represents
- [ ] I understand what coefficients (β₁, β₂, ...) represent
- [ ] I can explain what "holding other features constant" means
- [ ] I know the goal is to minimize squared errors

**If you checked all boxes:** ✅ Excellent! You grasp linear regression basics.

**If you missed any:** Review [Glossary: Linear Regression], [StatQuest video]

---

### When to Use Linear Regression

- [ ] I can identify when linear regression is appropriate (continuous target, linear relationship)
- [ ] I can explain when NOT to use linear regression (categorical target, nonlinear relationship)
- [ ] I understand that residual plots help validate whether LR is appropriate
- [ ] I know that LR is one of many algorithms (more coming in Weeks 2-6!)

**If you checked all boxes:** ✅ You understand LR's place in the ML toolkit.

**If you missed any:** Review [Teaching Guide Section 7: Common Questions]

---

## Part 2: Technical Skills (sklearn)

### Data Loading and Exploration

- [ ] I can load a built-in dataset using sklearn (e.g., `fetch_california_housing()`)
- [ ] I can extract features (X) and target (y) from a dataset
- [ ] I can check the shape of X and y using `.shape`
- [ ] I can list feature names using `data.feature_names`

**Test yourself:**
```python
from sklearn.datasets import load_diabetes
data = load_diabetes()
X = data.data
y = data.target

# Can you answer these without running code?
# 1. What is X.shape?  Answer: ___________
# 2. What is y.shape?  Answer: ___________
# 3. How many features? Answer: ___________
```

**Answers:** (442, 10), (442,), 10 features

**If you got it right:** ✅ You can load and explore data.

**If you missed any:** Review [Live Session Notebook: Step 2], [Cheat Sheet: Loading Data]

---

### Train-Test Split

- [ ] I can split data using `train_test_split()`
- [ ] I understand the `test_size` parameter (e.g., 0.2 = 20% for testing)
- [ ] I understand the `random_state` parameter (ensures reproducibility)
- [ ] I can verify the split worked by checking shapes

**Test yourself:**
```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# If X has 442 samples, after 80/20 split:
# X_train has _____ samples
# X_test has _____ samples
```

**Answers:** 353 (train), 89 (test) - approximately 80/20

**If you got it right:** ✅ You can split data properly.

**If you missed any:** Review [Cheat Sheet: Splitting Data], [Live Session Notebook: Step 3]

---

### Training a Model

- [ ] I can import LinearRegression from sklearn
- [ ] I can create a LinearRegression model instance
- [ ] I can train a model using `.fit(X_train, y_train)`
- [ ] I understand that `.fit()` learns the coefficients
- [ ] I can access coefficients using `model.coef_`
- [ ] I can access the intercept using `model.intercept_`

**Test yourself:**
```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)

# What do these return?
# model.intercept_ → Answer: ___________
# model.coef_ → Answer: ___________
```

**Answers:** A single number (intercept), An array of numbers (coefficients)

**If you got it right:** ✅ You can train models.

**If you missed any:** Review [Cheat Sheet: Training Linear Regression], [Live Session Notebook: Step 4]

---

### Making Predictions

- [ ] I can make predictions using `model.predict(X_test)`
- [ ] I understand that `y_pred` has the same shape as `y_test`
- [ ] I can compare predictions to actual values
- [ ] I know NOT to use training data for evaluation (use test data!)

**Test yourself:**
```python
y_pred = model.predict(X_test)

# If y_test.shape is (89,), what is y_pred.shape?
# Answer: ___________
```

**Answer:** (89,) - same shape

**If you got it right:** ✅ You can make predictions.

**If you missed any:** Review [Cheat Sheet: Making Predictions], [Live Session Notebook: Step 5]

---

### Evaluating Models

- [ ] I can calculate R² using `r2_score(y_test, y_pred)`
- [ ] I can calculate MSE using `mean_squared_error(y_test, y_pred)`
- [ ] I can calculate RMSE using `np.sqrt(mean_squared_error(...))`
- [ ] I can interpret R²: 0 = terrible, 1 = perfect
- [ ] I can interpret RMSE: average error in original units
- [ ] I understand that lower MSE/RMSE is better, higher R² is better

**Test yourself:**
```python
# If R² = 0.52, the model explains _____ % of variance.
# If RMSE = 55.3 and target is disease progression score,
# the average error is _____ points.
```

**Answers:** 52%, 55.3 points

**If you got it right:** ✅ You can evaluate models.

**If you missed any:** Review [Cheat Sheet: Evaluating Models], [Live Session Notebook: Step 6], [Glossary: R², MSE, RMSE]

---

### Creating Visualizations

- [ ] I can create a residual plot using matplotlib
- [ ] I can calculate residuals: `y_test - y_pred`
- [ ] I can add a reference line at y=0 using `plt.axhline(y=0)`
- [ ] I can add labels, title, and grid to plots

**Test yourself:**
```python
# Fill in the blanks
residuals = _______ - _______  # Calculate residuals

plt.scatter(y_pred, residuals)
plt.axhline(y=___, color='red', linestyle='--')  # Reference line
plt.xlabel('________')  # What goes on x-axis?
plt.ylabel('________')  # What goes on y-axis?
plt.show()
```

**Answers:** `y_test - y_pred`, `y=0`, `'Predicted Values'`, `'Residuals'`

**If you got it right:** ✅ You can create diagnostic plots.

**If you missed any:** Review [Cheat Sheet: Visualizations], [Live Session Notebook: Step 7]

---

## Part 3: Interpretation & Analysis

### Residual Plot Interpretation

- [ ] I can identify random scatter in a residual plot (GOOD - LR is appropriate)
- [ ] I can identify a curved pattern (BAD - nonlinear relationship, try polynomial features)
- [ ] I can identify a funnel shape (BAD - heteroscedasticity, try transformation)
- [ ] I can identify clusters (BAD - missing categorical features)
- [ ] I understand that residual plots validate model assumptions
- [ ] I can explain what to do when I see each bad pattern (curve → polynomial features; funnel → transform target)

**Test yourself:**

Which residual plot pattern indicates a good model fit?
- (a) Curved pattern
- (b) Funnel shape getting wider
- (c) Random scatter around zero ✅
- (d) Two distinct clusters

**Answer:** (c)

**If you got it right:** ✅ You can interpret residual plots.

**If you missed any:** Review [Deep Dive: Residual Analysis], [Glossary: Residual Plot]

---

### Coefficient Interpretation

- [ ] I can explain what a coefficient means using "holding all else constant" language
- [ ] I can interpret both the sign (direction) and magnitude (strength) of coefficients
- [ ] I can rank features by importance using absolute coefficient values
- [ ] I can communicate coefficient meanings to non-technical stakeholders
- [ ] I understand the difference between correlation and causation when interpreting coefficients

**Test yourself:**

Given this equation:
```
Price = 50,000 + 150×(SqFt) + 20,000×(Bedrooms) - 5,000×(Age)
```

What happens to price if:
1. Square feet increases by 10 (holding bedrooms and age constant)?
   Answer: Price increases by ___________

2. Age increases by 5 years (holding sqft and bedrooms constant)?
   Answer: Price __________ by ___________

**Answers:**
1. Price increases by $1,500 (10 × $150)
2. Price decreases by $25,000 (5 × -$5,000)

**If you got it right:** ✅ You can interpret coefficients.

**If you missed any:** Review [Glossary: Coefficient, Partial Effect], [Live Session Notebook: Step 4]

---

### Model Performance Assessment

- [ ] I can determine if a model is overfitting (high train R², low test R²)
- [ ] I can determine if a model is underfitting (low train R², low test R²)
- [ ] I can explain my model's performance to a non-technical person
- [ ] I can identify when my model is "good enough" vs needs improvement

**Test yourself:**

Scenario: Train R² = 0.95, Test R² = 0.40

What's happening?
- (a) Good model, ready for production
- (b) Overfitting - model memorized training data ✅
- (c) Underfitting - model too simple
- (d) Data leakage issue

**Answer:** (b) Overfitting

**If you got it right:** ✅ You can assess model quality.

**If you missed any:** Review [Glossary: Overfitting, Generalization]

---

## Part 4: Workflow & Best Practices

### Complete Pipeline

- [ ] I can execute a complete ML pipeline from start to finish without help
- [ ] I can adapt the pipeline to a new dataset
- [ ] I remember to set `random_state` for reproducibility
- [ ] I follow the pattern: Load → Split → Train → Predict → Evaluate

**Test yourself:**

Put these steps in the correct order:
- (a) model.fit(X_train, y_train)
- (b) X_train, X_test, y_train, y_test = train_test_split(X, y)
- (c) r2 = r2_score(y_test, y_pred)
- (d) X = data.data; y = data.target
- (e) y_pred = model.predict(X_test)

**Correct order:** _______, _______, _______, _______, _______

**Answer:** d, b, a, e, c (Load, Split, Train, Predict, Evaluate)

**If you got it right:** ✅ You understand the workflow.

**If you missed any:** Review [Cheat Sheet: Complete Pipeline Template]

---

### Troubleshooting

- [ ] I can read and understand sklearn error messages
- [ ] I know how to check data shapes when I get errors
- [ ] I can fix the "Expected 2D array, got 1D array" error
- [ ] I can fix the "X has Y features but model expects Z" error

**Common errors I've encountered and know how to fix:**

List any errors you've seen:
1. _______________________________________________________________
2. _______________________________________________________________
3. _______________________________________________________________

**If you've seen errors and fixed them:** ✅ Great learning experience!

**If you haven't encountered errors yet:** You will! Refer to [Cheat Sheet: Common Errors & Fixes] when they happen.

---

## Part 5: Applied Knowledge

### Homework Completion

- [ ] I completed the post-class exercise independently
- [ ] My code runs without errors
- [ ] My residual plot looks reasonable (random scatter)
- [ ] I can explain my R² score
- [ ] I answered all reflection questions thoughtfully

**My homework R² score:** ___________

**Is this good or bad for the Diabetes dataset?** ___________

**Typical R² for Diabetes dataset:** 0.40 - 0.55 (domain-dependent!)

---

### Real-World Application

- [ ] I can think of a problem in my field where linear regression would be useful
- [ ] I can identify the features and target for that problem
- [ ] I know what data I would need to collect
- [ ] I can anticipate potential issues (data leakage, outliers, etc.)

**My real-world application idea:**

Problem: _____________________________________________________________

Target variable: ______________________________________________________

Features (list 3-5): __________________________________________________

____________________________________________________________________

Potential challenges: _________________________________________________

____________________________________________________________________

---

## 📊 Overall Self-Assessment Score

**Count your checkmarks:**

- **Conceptual Understanding (Part 1):** _____ / 18
- **Technical Skills (Part 2):** _____ / 33
- **Interpretation & Analysis (Part 3):** _____ / 15
- **Workflow & Best Practices (Part 4):** _____ / 9
- **Applied Knowledge (Part 5):** _____ / 9

**Total:** _____ / 84

---

## Scoring Guide

### 75-84 (90%+): Excellent! ✅

**You're ready for Week 2!**

Next steps:
- (Optional) Complete bonus challenge (polynomial features)
- Help classmates in discussion forum
- Preview Week 2 pre-class materials
- Celebrate your success!

---

### 60-74 (71-89%): Good! ✓

**You understand most concepts but have some gaps.**

Next steps:
- Review sections where you missed items
- Re-watch StatQuest videos
- Redo homework with fresh eyes
- Attend office hours with specific questions
- Review before Week 2

---

### 45-59 (54-70%): Needs Review ⚠️

**You have the foundation but need more practice.**

Next steps:
- **Schedule office hours** - bring this checklist!
- Re-do live session notebook from scratch
- Complete all pre-class materials if you skipped any
- Watch instructor demo video again
- Work through cheat sheet examples
- Practice with a study partner

---

### Below 45 (<54%): Remediation Needed ❌

**Don't panic! You need focused review before Week 2.**

Next steps:
- **Attend office hours ASAP** - this is critical
- Start over with pre-class study guide
- Watch all videos (StatQuest, live demo recording)
- Work through materials WITH a study partner
- Ask questions in discussion forum
- Consider re-doing Week 1 in parallel with Week 2

**Important:** Linear regression is foundational for the entire course. Investing time now will pay off later!

---

## 🎯 Action Plan

Based on my self-assessment, here's my action plan:

### Topics I Need to Review:

1. ___________________________________________________________________

2. ___________________________________________________________________

3. ___________________________________________________________________

### Specific Actions I Will Take:

- [ ] ___________________________________________________________________
- [ ] ___________________________________________________________________
- [ ] ___________________________________________________________________

### Questions to Ask in Office Hours / Forum:

1. ___________________________________________________________________

2. ___________________________________________________________________

3. ___________________________________________________________________

### By When:

I will complete this review by: ______________________ (date)

---

## 📚 Review Resources by Topic

### If you struggled with Conceptual Understanding:

**Review:**
- [Pre-Class Study Guide](../pre_class/Week1_Pre_Class_Study_Guide.md)
- [Glossary](../live_session/Week1_Glossary.md) - Key terms
- StatQuest: Linear Regression video (12 min)
- [Teaching Guide Section 5] - Conceptual explanations

---

### If you struggled with Technical Skills:

**Review:**
- [Cheat Sheet](../live_session/Week1_sklearn_cheat_sheet.md) - Copy-paste examples
- [Live Session Notebook](../live_session/week1_live_session.ipynb) - Re-run all cells
- sklearn documentation: LinearRegression
- Practice with different datasets (try Boston housing, load_diabetes)

---

### If you struggled with Interpretation:

**Review:**
- [Deep Dive: Residual Analysis](../../instructor_materials/deep_dives/Week1_DeepDive_Residual_Analysis.md)
- [Glossary: Coefficient, R², Residual](../live_session/Week1_Glossary.md)
- Re-read homework solutions with focus on interpretation questions

---

### If you struggled with Workflow:

**Review:**
- [Complete Pipeline Template](../live_session/Week1_sklearn_cheat_sheet.md#complete-pipeline-template)
- [Appendix A: ML Pipeline Template](../../appendices/Appendix_A_ML_Pipeline_Template.md)
- Practice running the pipeline 3 times on different datasets

---

## 🔄 Re-Assessment

After you've reviewed, come back and re-check items you missed.

**Re-assessment date:** ______________________

**New score:** _____ / 84

**Improvement:** _____ points

---

## 💬 Discussion Forum

**Share your progress!**

Post in the Week 1 forum:
- Your R² score from homework
- One thing you learned
- One thing you found challenging
- One question you still have

**Helping others reinforces your own learning!**

---

## 🚀 Looking Ahead: Week 2 Preview

**Next week's topic:** Logistic Regression (Classification)

**Key differences from Week 1:**
- Target is categorical (not continuous)
- Different metrics (accuracy, precision, recall - not R²)
- Different algorithm (logistic regression - not linear regression)

**Same pattern:**
- Load → Split → Train → Predict → Evaluate
- sklearn API: create → fit → predict
- Residual plots replaced with confusion matrices

**To prepare:**
- Ensure you're solid on Week 1 concepts (they build on each other!)
- Complete Week 2 pre-class materials
- Review classification vs regression in glossary

---

## ✅ Final Checklist

Before moving to Week 2:

- [ ] Completed this self-assessment honestly
- [ ] Identified areas needing review
- [ ] Created action plan for review
- [ ] Scheduled office hours if needed (score < 70%)
- [ ] Posted in discussion forum
- [ ] Feel confident (or have plan to get confident) before Week 2

---

**Remember:** Learning ML is a journey. Struggle is part of the process!

**The fact that you completed this self-assessment shows you're taking your learning seriously. That's the most important step!** 🎓

---

**Questions about this self-assessment?** Ask in the discussion forum or office hours.

**Instructor:** ____________________
**Office hours:** ____________________
**Forum link:** ____________________

---

*Last Updated: 2025-11-26*
