# Week 1 - Day 1: Live Session Materials

**Duration:** 2 hours
**Format:** Instructor-led with hands-on practice

---

## 📁 Contents

### Main Notebooks

1. **`week1_live_session.ipynb`** - California Housing Demo
   - Instructor live codes, students follow along
   - Complete ML pipeline walkthrough
   - 8 features, 20,640 houses
   - Demonstrates: Split, Train, Evaluate, Residual Plots

2. **`week1_pair_programming.ipynb`** - Diabetes Dataset
   - Students work in pairs
   - Fill-in-blanks format with guidance
   - Different dataset, same pipeline
   - Practice without instructor scaffolding

### Support Materials

3. **`Week1_Student_Workbook.md`** - Note-taking guide
4. **`Week1_Glossary.md`** - Key terms and definitions
5. **`Week1_sklearn_cheat_sheet.md`** - Quick reference for sklearn commands
6. **`images/`** - Visual aids and diagrams
7. **`mse_linear_regression_demo.html`** - Interactive visualization (optional)

---

## 🎯 Learning Objectives (Day 1)

By the end of Day 1, students will:
- Execute the complete 6-step ML pipeline
- Understand data leakage and prevention ("locked vault")
- Know how Linear Regression works (best line, MSE, Normal Equation)
- Identify 5 residual patterns visually
- Interpret coefficients ("holding all else constant")
- Use sklearn pattern: Create → Fit → Predict

---

## ⏱️ Day 1 Timeline

```
0:00-0:15  Welcome & Course Overview
0:15-0:40  ML Pipeline Concepts (whiteboard)
0:40-1:00  Linear Regression Theory (whiteboard)
1:00-1:15  Residual Plots Preview (whiteboard)
1:15-1:30  BREAK
1:30-2:25  Live Coding: California Housing (55 min)
2:25-2:55  Pair Programming: Diabetes (30 min)
2:55-3:00  Wrap-up & Preview
```

---

## 📊 Key Concepts Covered

### ML Pipeline (6 Steps)
1. Load Data
2. **Split Data** (BEFORE preprocessing!)
3. Preprocess
4. Train Model
5. Evaluate
6. Interpret

### Linear Regression Basics
- Finds the "best line" through data
- Minimizes Mean Squared Error (MSE)
- sklearn uses Normal Equation (closed-form, NOT gradient descent)
- Coefficients show feature effects

### 5 Residual Patterns (Visual Recognition)
1. ✅ Random scatter (good!)
2. ❌ Curve (nonlinear)
3. ❌ Funnel (heteroscedasticity)
4. ❌ Clusters (missing features)
5. ⚠️ Outliers (investigate)

---

## 🚀 After Day 1

**What's Next:**
- Day 2: Deep Dive into WHY patterns matter (statistical foundations)
- Guided practice with Boston Housing dataset
- Assessment quiz
- Week 2: Classification with Logistic Regression

**No homework assigned after Day 1** - Day 2 continues the next session.

---

## 💡 Tips for Success

1. **Follow along during live coding** - type the code yourself
2. **Ask questions** - if you're confused, others probably are too
3. **Focus on the workflow** - the pattern repeats for every ML project
4. **Take notes** - especially on data leakage prevention
5. **Practice the sklearn pattern** - Create, Fit, Predict

---

## 🔗 Related Materials

- **Teaching Guide:** `teaching_guide/WEEK1_STREAMLINED_TEACHING_PLAN.md`
- **Instructor Segments:** `teaching_guide/live_session_segments/`
- **Day 2 Materials:** `day2_guided_practice/`
- **Deep Dives (Instructor):** `instructor_materials/deep_dives/`

---

*If you're returning after a break: This folder contains all Day 1 (first 2 hours) materials.*
