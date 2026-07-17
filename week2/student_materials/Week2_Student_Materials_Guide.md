# Week 2 Student Materials Guide

**Binary Classification & Logistic Regression**

Welcome to Week 2! This guide helps you navigate all the materials and understand when to use each notebook.

---

## 📚 Complete Materials Overview

### Before Class (Pre-Class)
1. **Week2_Pre_Class_Study_Guide.md** - READ FIRST (30 min)
2. **week2_preclass_practice.ipynb** - PRACTICE (20 min)

### Day 1: Live Session (3 hours)
3. **week2_live_session.ipynb** - FOLLOW ALONG (instructor-led)
4. **Week2_Student_Workbook.md** - TAKE NOTES (write key concepts)
5. **Week2_Glossary.md** - REFERENCE (look up terms)
6. **Week2_sklearn_cheat_sheet.md** - QUICK REFERENCE

### Day 1: Pair Programming
7. **week2_pair_programming.ipynb** - WORK WITH PARTNER (30 min)

### Day 2: Guided Practice (1 hour)
8. **week2_heart_disease_guided.ipynb** - FOLLOW ALONG (new dataset)

### After Class (Post-Class)
9. **week2_postclass_exercise.ipynb** - HOMEWORK (solo practice)
10. **week2_bonus_threshold_tuning.ipynb** - OPTIONAL (advanced)
11. **Week2_Self_Assessment.md** - REFLECT (check understanding)

---

## 🎯 When to Use Each Material

### **Pre-Class Materials** (Do BEFORE Day 1)

**📖 Week2_Pre_Class_Study_Guide.md**
- **When:** Before Day 1 live session
- **Time:** 30 minutes
- **Purpose:** Get familiar with classification concepts
- **What you'll learn:**
  - Difference between regression and classification
  - What confusion matrix means
  - Basic logistic regression idea
- **Scaffolding:** 100% reading (no coding yet)
- **Success criteria:** Can explain TP, TN, FP, FN in your own words

**💻 week2_preclass_practice.ipynb**
- **When:** After reading study guide
- **Time:** 20 minutes
- **Purpose:** Try basic sklearn classification
- **What you'll do:**
  - Load Iris dataset
  - Train simple classifier
  - See predict() output
- **Scaffolding:** 90% (fill in 2-3 lines)
- **Success criteria:** Notebook runs without errors

---

### **Day 1 Materials** (3-Hour Live Session)

**📓 week2_live_session.ipynb** ⭐ PRIMARY NOTEBOOK
- **When:** During Day 1 live session
- **Time:** 55 minutes (Segment 6: Live Coding)
- **Purpose:** Learn complete classification pipeline
- **What's included:**
  - Load Breast Cancer dataset
  - Split data (prevent data leakage!)
  - Scale features
  - Train logistic regression
  - Evaluate with confusion matrix
  - Calculate precision, recall, F1
  - Tune decision threshold
  - Business cost analysis
- **Scaffolding:** 100% (code provided - you run cells and follow along)
- **Instructor demonstrates:** Yes - follow their screen
- **Your role:** Run cells, ask questions, understand each step
- **Success criteria:** Understand why we split before scaling, can interpret confusion matrix

**📝 Week2_Student_Workbook.md**
- **When:** Throughout Day 1 (keep open while coding)
- **Purpose:** Take notes, track key concepts
- **What to write:**
  - Confusion matrix diagram
  - Precision vs recall formulas
  - When to optimize each metric
  - Threshold tuning insights
- **Use this:** Reference during pair programming and homework!

**📚 Week2_Glossary.md**
- **When:** Anytime you hear an unfamiliar term
- **Purpose:** Quick definitions
- **Contains:**
  - Confusion Matrix
  - TP, TN, FP, FN
  - Precision, Recall, F1
  - ROC, AUC
  - Class imbalance
  - Threshold
- **Tip:** Keep this open in a browser tab during class!

**🔧 Week2_sklearn_cheat_sheet.md**
- **When:** During coding (quick syntax reference)
- **Purpose:** Copy-paste sklearn code patterns
- **Contains:**
  - `LogisticRegression()` syntax
  - `confusion_matrix()` usage
  - `classification_report()` example
  - `predict()` vs `predict_proba()`
- **Use this when:** You forget exact syntax during practice

---

### **Day 1 Pair Programming** (30 Minutes)

**👥 week2_pair_programming.ipynb**
- **When:** End of Day 1 (Segment 7)
- **Time:** 30 minutes
- **Purpose:** Apply what you learned with a partner
- **Dataset:** Titanic survival (different from live session!)
- **What you'll do:**
  - Load and explore Titanic data
  - Split, scale, train classifier
  - **YOUR TASK:** Interpret confusion matrix (fill in TP, TN, FP, FN)
  - **YOUR TASK:** Calculate metrics manually
  - **YOUR TASK:** Analyze threshold choices
- **Scaffolding:** 60% (you fill in diagnostic analysis)
- **Partner roles:**
  - **Navigator:** Describes what to code
  - **Driver:** Types the code
  - **Switch every 10 minutes!**
- **Solutions:** Posted after class (compare your approach)
- **Success criteria:** Correctly interpret confusion matrix, explain threshold choice

---

### **Day 2 Materials** (1-Hour Session)

**🩺 week2_heart_disease_guided.ipynb**
- **When:** Day 2 live session
- **Time:** 20 minutes (Segment 4)
- **Purpose:** Practice pipeline on new dataset WITH instructor support
- **Dataset:** Heart Disease UCI (different from Day 1!)
- **What you'll do:**
  - Follow same 6-step pipeline
  - **YOUR TASK:** Fill in confusion matrix values
  - **YOUR TASK:** Calculate accuracy, precision, recall manually
  - Compare three thresholds (0.3, 0.5, 0.7)
  - Apply business cost framework
- **Scaffolding:** 70% (code provided, you fill in analysis)
- **Instructor support:** YES - they circulate and help
- **Solutions:** Posted immediately after Day 2
- **Success criteria:** Independently calculate metrics from confusion matrix

---

### **Post-Class Materials** (After Day 2)

**📊 week2_postclass_exercise.ipynb** (HOMEWORK)
- **When:** After completing Day 1 and Day 2
- **Time:** 60-90 minutes
- **Purpose:** Solo practice to solidify understanding
- **Dataset:** NEW dataset (Diabetes or Bank Marketing)
- **What you'll do:**
  - Complete FULL pipeline yourself
  - Load data ✅
  - Split data (you write the code!)
  - Scale features (you write the code!)
  - Train model (you write the code!)
  - Evaluate and interpret
  - Tune threshold based on business scenario
- **Scaffolding:** 50% (you write more code than Day 1/Day 2)
- **Hints provided:** Yes (in markdown cells)
- **Solutions:** Posted 24 hours after assignment
- **Due:** Before Week 3 Day 1
- **Success criteria:** Pipeline runs successfully, you can justify threshold choice

**🚀 week2_bonus_threshold_tuning.ipynb** (OPTIONAL)
- **When:** If you finish homework and want more practice
- **Time:** 30-45 minutes
- **Purpose:** Deep dive into advanced threshold tuning
- **What you'll explore:**
  - Precision-recall curves
  - ROC curves
  - Finding optimal threshold with constraints
  - Cost-sensitive learning
- **Scaffolding:** 30% (less guidance - you explore!)
- **Solutions:** Provided (multiple valid approaches)
- **Not required for:** Week 3 preparation
- **Do this if:** You want to go beyond the basics!

**🤔 Week2_Self_Assessment.md**
- **When:** After completing all practice materials
- **Time:** 10 minutes
- **Purpose:** Check your understanding before Week 3
- **What's included:**
  - Reflection questions
  - Concept checklist (can you explain these?)
  - Common misconceptions to avoid
  - Week 3 readiness check
- **Success criteria:** Can answer all questions without looking at notes

---

## 📊 Scaffolding Levels Explained

**What is scaffolding?**
Scaffolding = how much code is provided vs how much you write

| Level | Code Provided | You Write | Purpose |
|-------|---------------|-----------|---------|
| 90% | Almost all | Fill in 1-2 lines | Learn by observing |
| 70% | Most | Fill in analysis/interpretation | Apply concepts |
| 60% | More than half | Fill in key steps | Active practice |
| 50% | Half | Write significant portions | Independent application |
| 30% | Hints only | Most of the code | Mastery/exploration |

**Progression:**
```
Pre-class (90%) → Day 1 Live (100% demo) → Pair Programming (60%)
→ Day 2 Guided (70%) → Homework (50%) → Bonus (30%)
```

This gradual release ensures you build confidence before tackling harder challenges!

---

## 🎓 Learning Path

**Recommended order:**

```
1. Pre-Class Study Guide ────→ 2. Pre-Class Practice
                                        ↓
                                  ──────────────
                                        ↓
3. Day 1 Live Session ───────→ 4. Day 1 Pair Programming
   (week2_live_session.ipynb)      (week2_pair_programming.ipynb)
   Take notes in Workbook!
                                        ↓
5. Day 2 Deep Dive ───────────→ 6. Day 2 Guided Practice
   (Class imbalance concepts)      (week2_heart_disease_guided.ipynb)
                                        ↓
7. Post-Class Exercise ───────→ 8. Self-Assessment
   (week2_postclass_exercise)       (Check understanding)
                                        ↓
9. (Optional) Bonus Material
   (week2_bonus_threshold_tuning)
```

---

## ✅ Weekly Checklist

**Before Day 1:**
- [ ] Read Pre-Class Study Guide
- [ ] Complete Pre-Class Practice notebook
- [ ] Review Week 1 confusion concepts (data leakage!)

**Day 1:**
- [ ] Attend live session (3 hours)
- [ ] Run all cells in week2_live_session.ipynb
- [ ] Take notes in Student Workbook
- [ ] Complete pair programming exercise
- [ ] Ask questions in chat or forum!

**Day 2:**
- [ ] Attend deep dive session (1 hour)
- [ ] Complete Heart Disease guided practice
- [ ] Pass quiz (5+/8 questions)
- [ ] Review concepts you struggled with

**After Day 2:**
- [ ] Complete post-class exercise (solo)
- [ ] Compare your solution to posted answers
- [ ] Complete self-assessment
- [ ] (Optional) Bonus threshold tuning
- [ ] Post your R² score in forum (optional community engagement)

**Before Week 3:**
- [ ] Review confusion matrix one more time
- [ ] Can explain precision vs recall without notes
- [ ] Understand when to use each metric
- [ ] Ready for Decision Trees!

---

## 💡 Tips for Success

### During Live Sessions
✅ **Do:**
- Run every cell as instructor demonstrates
- Ask questions immediately when confused
- Take notes in Student Workbook
- Reference Glossary for unfamiliar terms

❌ **Don't:**
- Try to code ahead (follow instructor pace)
- Skip cells (every step builds on previous)
- Wait until homework to ask questions

### During Pair Programming
✅ **Do:**
- Switch roles every 10 minutes (set a timer!)
- Navigator: Explain your reasoning out loud
- Driver: Ask questions if unclear
- Collaborate - discuss different approaches

❌ **Don't:**
- Let one person do all the work
- Rush to finish (understanding > speed)
- Look at solutions before attempting

### During Homework
✅ **Do:**
- Read all markdown cells (they have hints!)
- Reference Day 1/Day 2 notebooks
- Try before looking at solutions
- Post specific questions in forum

❌ **Don't:**
- Copy-paste code without understanding
- Skip the interpretation questions
- Give up after first error (debugging is learning!)

---

## 🆘 When You're Stuck

### Error Messages
1. **Read the error carefully** (last line tells you what went wrong)
2. **Check common issues:**
   - Did you split before scaling?
   - Are feature and target shapes compatible?
   - Did you import all libraries?
3. **Reference:** Week2_sklearn_cheat_sheet.md
4. **Ask:** Post in forum with error message

### Concept Confusion
1. **Reference:** Week2_Glossary.md
2. **Review:** Student Workbook notes
3. **Watch:** Recorded lecture (if available)
4. **Ask:** Office hours or forum

### "I don't know where to start"
1. **Look at:** Previous notebook (Day 1 live session)
2. **Find:** Similar cell structure
3. **Adapt:** Change dataset/variable names
4. **Ask:** "How do I approach this?" in forum

---

## 📞 Getting Help

**During Class:**
- Raise hand (in-person)
- Use chat/reactions (virtual)
- Ask partner first (pair programming)

**Outside Class:**
- Forum (post questions - TAs and peers respond)
- Office hours (schedule on course site)
- Study groups (form with classmates)

**Response Time Expectations:**
- Forum: Within 24 hours
- Office hours: Immediate (during scheduled time)
- Email instructor: Within 48 hours

---

## 🎯 Learning Objectives Tracker

By the end of Week 2, you should be able to:

**Conceptual:**
- [ ] Explain difference between classification and regression
- [ ] Draw and label confusion matrix (TP, TN, FP, FN)
- [ ] Define precision, recall, F1, accuracy
- [ ] Explain why accuracy fails with class imbalance
- [ ] Choose appropriate metric based on business cost

**Technical:**
- [ ] Load dataset and check class distribution
- [ ] Split data (preventing data leakage)
- [ ] Scale features using StandardScaler
- [ ] Train LogisticRegression classifier
- [ ] Generate confusion matrix
- [ ] Calculate metrics manually and with sklearn
- [ ] Tune decision threshold (0.3, 0.5, 0.7)
- [ ] Perform business cost analysis

**Application:**
- [ ] Identify when FN vs FP is more costly
- [ ] Justify threshold choice to stakeholders
- [ ] Interpret model performance in business terms
- [ ] Apply pipeline to new dataset independently

---

## 🚀 Preparing for Week 3

**What's coming:**
- Decision Trees & Random Forests
- Same confusion matrix! (you're already an expert)
- Same metrics! (precision, recall, F1)
- NEW: Non-linear decision boundaries
- NEW: Feature importance interpretation

**To prepare:**
- Review confusion matrix (you'll use it every week!)
- Ensure you understand train/test split
- Rest up - Week 3 builds on this foundation!

---

**Questions about materials? Ask in forum or office hours. You've got this! 🎓**
