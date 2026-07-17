# Week 4 Student Materials Guide

**Welcome to Week 4: Production ML Methodology!**

This guide explains how to navigate Week 4 materials and understand the learning progression.

---

## Overview: What Makes Week 4 Different

**Week 1-3:** You learned ML algorithms (Linear Regression, Logistic Regression, Decision Trees, Random Forests, XGBoost)

**Week 4:** You learn HOW to use those algorithms professionally in production systems

**The Four Pillars:**
1. **Cross-Validation** - Get reliable performance estimates
2. **GridSearchCV** - Tune hyperparameters systematically
3. **Regularization** - Prevent overfitting
4. **Pipeline** - Prevent data leakage

---

## Materials Organization

### Pre-Class Materials (Complete BEFORE live session)

📂 **Location:** `pre_class/`

**1. Week4_Pre_Class_Study_Guide.pdf**
- Read: 10-15 minutes
- Topics: CV theory, regularization concepts, pipeline architecture
- **Purpose:** Conceptual foundation

**2. week4_preclass_practice.ipynb**
- Code: 30-45 minutes
- Dataset: Breast Cancer (simple, clean)
- Scaffolding: 70% (fill-in-the-blank style)
- **Purpose:** Hands-on familiarity with CV

**⚠️ IMPORTANT:** Pre-class practice is NOT optional. Live session builds on this foundation.

---

### Day 1 Live Session Materials

📂 **Location:** `day1_live_session/`

**During class, you'll use:**

**1. week4_cv_demo.ipynb**
- **When:** Segment 2 (0:30-0:40)
- **Format:** Instructor demonstrates while you observe
- **Dataset:** Breast Cancer (same as pre-class)
- **Purpose:** See CV concepts with instructor narration

**Why use this if I already did pre-class practice?**
- **Pre-class:** You practiced alone (hands-on discovery)
- **Live demo:** Instructor demonstrates (instructional clarity)
- **NOT redundant** - Different learning functions

**2. week4_live_session.ipynb**
- **When:** Segment 7 (1:35-2:00)
- **Format:** Collaborative coding (you direct, instructor types)
- **Dataset:** Adult Income (complex, realistic)
- **Purpose:** Build production pipeline together

**3. Supporting Materials:**
- `Week4_Student_Workbook.md` - Notes template for concepts
- `Week4_Glossary.md` - Key terms (CV, GridSearchCV, Pipeline, etc.)
- `Week4_sklearn_cheat_sheet.md` - Quick sklearn syntax reference

---

### Day 1 Pair Programming

📂 **Location:** `day1_pair_programming/`

**1. week4_pair_programming.ipynb**
- **When:** Segment 8 (2:00-2:30)
- **Format:** Pairs in breakout rooms
- **Task:** Find and fix 3 data leakage bugs
- **Purpose:** Active debugging practice

**Leakage bugs to find:**
1. Scaling before train/test split
2. Using test set for hyperparameter selection
3. Target variable leaking into features

---

### Post-Class Materials (Complete AFTER live session)

📂 **Location:** `day2_post_class/`

**1. week4_postclass_practice.ipynb** (Coming: will be provided after live session)
- **Time:** 45-60 minutes solo work
- **Dataset:** NEW dataset (not Breast Cancer or Adult Income)
- **Scaffolding:** 30% (minimal hints - you build most of it)
- **Purpose:** Independent mastery check

**What you'll build:**
- Complete end-to-end production pipeline
- ColumnTransformer for mixed data types
- Pipeline + GridSearchCV integration
- Cross-validation for evaluation
- Save final model with joblib

**2. Week4_Self_Assessment.md**
- Reflection questions
- Concept checks
- "Can you explain to a friend?" tests

---

## Learning Progression: Why You See Things Multiple Times

**You'll encounter Cross-Validation THREE times in Week 4. Here's why:**

### Encounter 1: Pre-Class Practice (Hands-On Discovery)
- **You code CV yourself** on Breast Cancer dataset
- **70% scaffolding** - fill in TODOs
- **Purpose:** Familiarity through practice
- **Time:** ~30 min alone

### Encounter 2: Live Demo (Instructional Clarity)
- **Instructor demonstrates** `week4_cv_demo.ipynb`
- **Same dataset** (Breast Cancer) - intentional for consistency
- **Purpose:** See it WITH theory context and instructor narration
- **Time:** 10 min observation

### Encounter 3: Production Pipeline (Collaborative Mastery)
- **Build together** in Segment 7 collaborative coding
- **Different dataset** (Adult Income) - more complex
- **Purpose:** Integrate CV into complete production workflow
- **Time:** 25 min collaborative

**Is this redundant?** NO! Each serves a different learning function:
- Practice alone → Watch instructor explain → Build together in production context
- Progressive scaffolding: 70% → Demonstration → 50% collaboration

This is **intentional pedagogical design**, not redundancy.

---

## Common Questions

### Q: "Why do we use Breast Cancer dataset multiple times?"

**A:** Consistent dataset lets you focus on METHODOLOGY, not data quirks.
- Pre-class: You practice CV on Breast Cancer
- Live demo: Instructor demonstrates CV on same data (shows consistency)
- Live coding: Different dataset (Adult Income) for production context

Same dataset in pre-class + demo = intentional. Shows the methodology works consistently.

---

### Q: "Is the live demo the same as pre-class practice?"

**A:** Same notebook, different PURPOSE:
- **Pre-class:** You figure it out (scaffolded practice)
- **Live demo:** Instructor explains WHY (instructional demonstration)

Analogy: Pre-class = you try recipe alone. Live demo = chef shows you technique.

---

### Q: "Do I need to complete pre-class practice?"

**A:** YES! Live session assumes you've:
- Practiced `cross_val_score()` syntax
- Seen single split variance vs CV stability
- Understood basic k-fold mechanics

Without pre-class, live session will feel too fast.

---

### Q: "What if I get stuck on pre-class practice?"

**A:** Pre-class is SCAFFOLDED (70% code provided). If stuck:
1. Review Week4_Pre_Class_Study_Guide.pdf first
2. Check Week4_Glossary.md for term definitions
3. Look at Week4_sklearn_cheat_sheet.md for syntax
4. Bring questions to live session!

It's OKAY to not finish perfectly - bring questions.

---

### Q: "Can I skip pair programming and just watch?"

**A:** Pair programming is where you APPLY learning. Debugging leakage bugs cements understanding. Passive watching doesn't build skills.

If shy about pairs, you can work alone, but actively CODE the fixes.

---

### Q: "What's the difference between live_session and postclass notebooks?"

**A:**

**live_session (Segment 7):**
- Collaborative (instructor + students together)
- Adult Income dataset
- 50% scaffolding
- PURPOSE: Build production pipeline WITH support

**postclass (solo homework):**
- Independent (you alone)
- NEW dataset
- 30% scaffolding
- PURPOSE: Prove mastery without safety net

Post-class is your "production ML certification" - can you do it solo?

---

## Success Checklist

**By end of Week 4, you should be able to:**

### Cross-Validation
- [ ] Explain why single splits are unreliable (using dating analogy)
- [ ] Use `cross_val_score()` with appropriate cv parameter
- [ ] Interpret results: "84.2% ± 0.9% across 5 folds"
- [ ] Choose StratifiedKFold for classification, KFold for regression
- [ ] Explain when to use k=3 vs k=5 vs k=10

### GridSearchCV
- [ ] Define param_grid for common algorithms
- [ ] Use `GridSearchCV(model, param_grid, cv=5)`
- [ ] Extract `best_params_` and `best_score_`
- [ ] Understand why GridSearchCV uses CV internally

### Regularization
- [ ] Explain L1 (Lasso) vs L2 (Ridge) tradeoffs
- [ ] Choose regularization based on feature count
- [ ] Tune regularization strength (C or alpha parameter)

### Pipeline
- [ ] Build ColumnTransformer for mixed data types
- [ ] Wrap in Pipeline with model
- [ ] Explain how Pipeline prevents data leakage
- [ ] Use Pipeline with GridSearchCV
- [ ] Save Pipeline with joblib for deployment

### Integration
- [ ] Build end-to-end production pipeline independently
- [ ] Explain why each component matters
- [ ] Debug common leakage mistakes
- [ ] Report results professionally (mean ± std)

---

## File Organization Summary

```
week4/student_materials/
│
├── pre_class/                      ← Do BEFORE live session
│   ├── week4_preclass_practice.ipynb
│   └── Week4_Pre_Class_Study_Guide.pdf
│
├── day1_live_session/             ← Use DURING live session
│   ├── week4_cv_demo.ipynb       (Segment 2: 0:30-0:40)
│   ├── week4_live_session.ipynb  (Segment 7: 1:35-2:00)
│   ├── Week4_Student_Workbook.md
│   ├── Week4_Glossary.md
│   └── Week4_sklearn_cheat_sheet.md
│
├── day1_pair_programming/         ← Use DURING pair work
│   └── week4_pair_programming.ipynb (Segment 8: 2:00-2:30)
│
└── day2_post_class/               ← Do AFTER live session
    ├── week4_postclass_practice.ipynb
    └── Week4_Self_Assessment.md
```

---

## Tips for Success

**Before Live Session:**
1. ✅ Complete pre-class practice (even if not perfect)
2. ✅ Read study guide PDF
3. ✅ Bring questions about pre-class struggles
4. ✅ Review Week 3 (algorithms you'll use with Week 4 methods)

**During Live Session:**
1. ✅ Take notes in Week4_Student_Workbook.md
2. ✅ Ask questions during whiteboard segments
3. ✅ Observe demo closely (connects pre-class practice to theory)
4. ✅ Actively code during Segment 7 (don't just watch)
5. ✅ Debug aggressively during pair programming

**After Live Session:**
1. ✅ Complete post-class practice notebook independently
2. ✅ Don't look at solutions until you've attempted fully
3. ✅ Fill out Week4_Self_Assessment.md honestly
4. ✅ Review any concepts where self-assessment shows gaps

---

## Getting Help

**If stuck on pre-class:** Bring questions to live session

**If stuck during live session:** Raise hand or use chat - instructor is there to help!

**If stuck on post-class:** Office hours, peer study groups, re-watch segments

**Red flags (seek help immediately):**
- Can't run `cross_val_score()` successfully
- Don't understand what mean ± std means
- Think CV is redundant with single split (it's not!)
- Can't build Pipeline independently

---

## Week 4 Mindset

**Week 1-3:** "I can code ML algorithms"
**Week 4:** "I can deploy ML professionally"

**Skills gained this week:**
- Reliable performance reporting (not lucky guesses)
- Systematic tuning (not random hyperparameter tries)
- Production-ready code (no data leakage)
- Professional communication ("84% ± 1.5%" not "about 84%")

**By Friday, you're ready for real-world ML deployment!**

---

*Week 4 Student Materials Guide v1.0 | 2026-03-02*
