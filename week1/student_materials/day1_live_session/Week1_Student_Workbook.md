# Week 1: Linear Regression - Student Workbook

**Date:** ________________
**Name:** ________________

**Purpose:** Note-taking template for today's live session
**How to use:** Fill in the blanks as the instructor explains each concept

---

## 📋 Session Overview

**Today's Topic:** Linear Regression
**Time:** 3 hours (0:00 - 3:00)
**Goal:** Build your first complete machine learning pipeline!

---

## 🎯 Learning Objectives (Check off as you learn!)

By the end of today, I will be able to:

- [ ] Execute a complete ML pipeline from data loading to evaluation
- [ ] Implement linear regression using sklearn
- [ ] Interpret R², MSE, and RMSE metrics
- [ ] Create and interpret residual plots
- [ ] Recognize when to split data (and why!)

---

## Part 1: Welcome & Course Roadmap (0:00 - 0:20)

### The 8-Week Journey

Fill in the algorithm for each week:

| Week | Algorithm | Type |
|------|-----------|------|
| 1 | _________________________ | Regression |
| 2 | _________________________ | Classification |
| 3 | _________________________ | Both |
| 4 | _________________________ | Regression |
| 5 | _________________________ | Clustering |
| 6 | _________________________ | Deep Learning |
| 7 | _________________________ | Advanced |
| 8 | _________________________ | Capstone |

### Key Principle

> Every week follows the same _____________ : Load → Split → Train → Evaluate

---

## Part 2: The ML Pipeline (0:20 - 0:50)

### The 5 Essential Steps

Fill in the missing steps:

```
1. Load _______________
2. Split data into ____________ and ____________ sets
3. Train the _______________
4. Make _______________
5. _______________ performance
```

### Critical Rule: Split BEFORE Preprocessing

**Why is this so important?**

____________________________________________________________________

____________________________________________________________________

____________________________________________________________________

**What happens if you split AFTER preprocessing?**

____________________________________________________________________

____________________________________________________________________

**Analogy:** (Fill in as instructor explains)

____________________________________________________________________

____________________________________________________________________

---

## Part 3: Linear Regression Deep Dive (0:50 - 1:20)

### What is Linear Regression?

**Definition:** _________________________________________________________

_______________________________________________________________________

### The Linear Equation

Fill in the equation:

```
y = _____ + _____X₁ + _____X₂ + ... + _____Xₚ

Where:
  y  = ___________________ (what we're predicting)
  X  = ___________________ (input variables)
  β₀ = ___________________ (y-value when all X = 0)
  β₁, β₂, ... = ___________________ (slopes for each feature)
```

### Real-World Example: House Prices

```
Price = 50,000 + 150×(SqFt) + 20,000×(Bedrooms) - 5,000×(Age)
```

**Interpretation:**

- The **intercept** (50,000) means: ________________________________________

- The **SqFt coefficient** (150) means: ___________________________________

  ______________________________________________________________________

- The **Bedrooms coefficient** (20,000) means: ____________________________

  ______________________________________________________________________

- The **Age coefficient** (-5,000) means: _________________________________

  ______________________________________________________________________

### The Goal of Linear Regression

Linear regression finds the coefficients (β) that __________________________

_______________________________________________________________________

---

### How Does It Find the Best Line?

**Method 1: Normal Equation**
- ___________________________________________________________________

**Method 2: Gradient Descent**
- ___________________________________________________________________

**Visual:** (Sketch as instructor draws)

```
    y │
      │
      │
      │
      │
      └────────── X
```

---

### The sklearn Pattern (MEMORIZE THIS!)

Fill in the three steps:

```
1. _______________ the model
2. _______________ the model on training data
3. _______________ on test data
```

**Python code template:**

```python
from sklearn.linear_model import LinearRegression

# Step 1:
model = ___________________________

# Step 2:
model._________(X_train, y_train)

# Step 3:
y_pred = model._________(X_test)
```

---

## Part 4: BREAK (1:20 - 1:35)

Take a break! When you return, we'll do live coding.

---

## Part 5: Live Coding Demo (1:35 - 2:15)

**Dataset:** California Housing (20,640 samples, 8 features)
**Goal:** Predict median house value

### Step 1: Imports

**Key libraries we're using:**

- `sklearn.datasets` → _______________________________________________
- `sklearn.model_selection` → ________________________________________
- `sklearn.linear_model` → ___________________________________________
- `sklearn.metrics` → ________________________________________________
- `matplotlib.pyplot` → ______________________________________________

---

### Step 2: Load Data

**Dataset shape:**

- Number of samples (houses): _________________
- Number of features per house: _________________

**Feature names:** (List as instructor shows them)

1. _____________________
2. _____________________
3. _____________________
4. _____________________
5. _____________________
6. _____________________
7. _____________________
8. _____________________

**Target variable:** _____________________

**Target units:** _____________________

---

### Step 3: Split Data

**Why split the data?**

_______________________________________________________________________

**Code:**

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size = _______,      # What percentage for testing?
    random_state = _______    # Why do we set this?
)
```

**What does `random_state=42` do?**

_______________________________________________________________________

**Our split ratio:**

- Training set: _______ samples (_____ %)
- Test set: _______ samples (_____ %)

---

### Step 4: Train Model

**Code:**

```python
model = LinearRegression()
model.________(X_train, y_train)
```

**What happens during `.fit()`?**

_______________________________________________________________________

_______________________________________________________________________

**Coefficients learned:**

| Feature | Coefficient | Interpretation |
|---------|-------------|----------------|
| MedInc | _________ | _________________________________ |
| HouseAge | _________ | _________________________________ |
| AveRooms | _________ | _________________________________ |
| AveBedrms | _________ | _________________________________ |
| Population | _________ | _________________________________ |
| AveOccup | _________ | _________________________________ |
| Latitude | _________ | _________________________________ |
| Longitude | _________ | _________________________________ |

**Intercept:** _________________

---

### Step 5: Make Predictions

**Code:**

```python
y_pred = model.__________(X_test)
```

**What is `y_pred`?**

_______________________________________________________________________

**Shape of predictions:** _________________

**First few predictions vs actuals:**

| Predicted | Actual | Difference |
|-----------|--------|------------|
| _________ | ______ | __________ |
| _________ | ______ | __________ |
| _________ | ______ | __________ |

---

### Step 6: Evaluate Model

**Three key metrics:**

#### Metric 1: R² (R-squared)

**Our R²:** _________________

**What does it mean?**

_______________________________________________________________________

_______________________________________________________________________

**Scale:** R² ranges from __________ (terrible) to __________ (perfect)

**Interpretation:** Our model explains _______ % of the variance in house prices.

---

#### Metric 2: MSE (Mean Squared Error)

**Our MSE:** _________________

**What does it mean?**

_______________________________________________________________________

_______________________________________________________________________

**Units:** _________________

**Problem with MSE:** ___________________________________________________

---

#### Metric 3: RMSE (Root Mean Squared Error)

**Our RMSE:** _________________

**What does it mean?**

_______________________________________________________________________

_______________________________________________________________________

**Why is RMSE better than MSE?**

_______________________________________________________________________

**In real dollars:** Our average error is $ ___________________

---

### Step 7: Residual Plot

**What is a residual?**

```
Residual = _____________ - _____________
```

**Why create a residual plot?**

_______________________________________________________________________

_______________________________________________________________________

**What we're looking for:**

✅ **GOOD pattern:** ____________________________________________________

❌ **BAD patterns:**

1. _____________________________________________________________________

2. _____________________________________________________________________

3. _____________________________________________________________________

**Our residual plot shows:** (Check one)

- [ ] ✅ Random scatter (good!)
- [ ] ❌ Curved pattern (nonlinear relationship)
- [ ] ❌ Funnel shape (heteroscedasticity)
- [ ] ❌ Clusters (missing categorical feature)

**Conclusion:** Is linear regression appropriate for this dataset?

_______________________________________________________________________

---

### Key Takeaways from Demo

**Most important things I learned:**

1. _____________________________________________________________________

2. _____________________________________________________________________

3. _____________________________________________________________________

**Questions I still have:**

1. _____________________________________________________________________

2. _____________________________________________________________________

3. _____________________________________________________________________

---

## Part 6: Pair Programming (2:15 - 2:45)

**Dataset:** Diabetes (442 samples, 10 features)
**Your role:** Navigator ___ or Driver ___ (fill in your role)

### My Pair Partner: ___________________________

### Role Responsibilities

**Navigator (my job if Navigator):**

- _____________________________________________________________________
- _____________________________________________________________________
- _____________________________________________________________________

**Driver (my job if Driver):**

- _____________________________________________________________________
- _____________________________________________________________________
- _____________________________________________________________________

**Role switch at:** _________ minutes

---

### Exercise Tasks (check off as you complete)

- [ ] Task 1: Load Diabetes dataset
- [ ] Task 2: Explore data shape and features
- [ ] Task 3: Split data (80/20)
- [ ] Task 4: Train LinearRegression model
- [ ] Task 5: Make predictions
- [ ] Task 6: Calculate R², MSE, RMSE
- [ ] Task 7: Create residual plot
- [ ] BONUS: Feature importance analysis

---

### Our Results

**R² score:** _________________

**RMSE:** _________________

**Best feature (highest coefficient):** _____________________

**Interpretation:** _____________________________________________________

_______________________________________________________________________

**Residual plot observation:** __________________________________________

_______________________________________________________________________

---

### Pair Programming Reflection

**What went well:**

_______________________________________________________________________

**What was challenging:**

_______________________________________________________________________

**What I learned from my partner:**

_______________________________________________________________________

---

## Part 7: Wrap-Up & Next Steps (2:45 - 3:00)

### Today's Key Concepts Review

Fill in the blanks:

1. Always split _____________ preprocessing to prevent _____________ leakage.

2. The sklearn pattern is: _____________ → _____________ → _____________

3. R² tells us the _____________ of variance explained by the model.

4. RMSE is better than MSE because it's in the same _____________ as the target.

5. Residual plots should show _____________ scatter if LR is appropriate.

---

### Post-Class Homework

**Due:** _________________ (date/time)

**Tasks:**

- [ ] Complete `week1_postclass_exercise.ipynb` (30 minutes)
- [ ] Post your R² score in the discussion forum
- [ ] Answer reflection questions
- [ ] (Optional) Bonus challenge: polynomial features

**What to submit:**

- _____________________________________________________________________
- _____________________________________________________________________

---

### Preview: Week 2

**Next week's topic:** ___________________________

**Type of problem:** ___________________________

**Key difference from Week 1:** _________________________________________

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
| ML Pipeline | _____ | ________________________________ |
| Data Splitting | _____ | ________________________________ |
| sklearn API | _____ | ________________________________ |
| Training Models | _____ | ________________________________ |
| R² Metric | _____ | ________________________________ |
| MSE/RMSE Metrics | _____ | ________________________________ |
| Residual Plots | _____ | ________________________________ |

**Overall confidence:** _____ / 5

---

## ❓ Questions for Instructor

**Write down any questions to ask during Q&A or office hours:**

1. _____________________________________________________________________

2. _____________________________________________________________________

3. _____________________________________________________________________

4. _____________________________________________________________________

5. _____________________________________________________________________

---

## 🔗 Resources to Review

**Check off as you review these resources:**

- [ ] Pre-class study guide (if you haven't already)
- [ ] StatQuest: Linear Regression (12 min video)
- [ ] StatQuest: Gradient Descent (10 min video)
- [ ] sklearn documentation: LinearRegression
- [ ] Week 1 glossary (key terms)
- [ ] Week 1 cheat sheet (quick reference)

---

## 🎉 Congratulations!

You've completed Week 1 of Introduction to Machine Learning Programming!

**You can now:**
- ✅ Build a complete ML pipeline
- ✅ Train and evaluate linear regression models
- ✅ Interpret model performance metrics
- ✅ Validate model assumptions with residual plots

**Next step:** Complete the post-class homework to reinforce these skills!

---

**Remember:** Practice is key. The more pipelines you build, the more natural it becomes!

---

*Questions? Reach out to the instructor or post in the discussion forum.*

**Instructor:** ____________________
**Email:** ____________________
**Office hours:** ____________________
