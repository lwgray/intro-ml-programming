# Week 2 Pair Programming Exercise - Changes Summary

## What Was Fixed

The original notebook had several critical issues that would have confused students and taught incorrect concepts. Here's what was changed:

---

## 🔴 Problems in Original Version

### Problem 1: Narrative Mismatch
- **Issue**: Notebook said "95% accuracy" but actual accuracy was 81.6%
- **Impact**: Students would immediately notice the discrepancy and question the exercise

### Problem 2: Wrong Fix Approach
- **Issue**: Notebook tried to "fix" the problem by using `threshold = 0.95` (HIGHER than default 0.5)
- **Impact**:
  - This is backwards! To catch MORE malignant cases, you need a LOWER threshold
  - The "fix" made accuracy crash from 81.6% → 25.4%
  - Recall for benign dropped to 0%
  - Students would learn the WRONG approach

### Problem 3: Misleading Text
- **Issue**: Text said accuracy "decreased slightly" when it actually dropped 56 percentage points
- **Impact**: Students would lose trust in the material

### Problem 4: Wrong Pedagogical Approach
- **Issue**: Trying to "fix" a badly-trained model with threshold adjustment doesn't work well
- **Impact**: Students learn to patch symptoms instead of fixing root causes

---

## ✅ Solutions Implemented

### Fix 1: Corrected Narrative
- Changed scenario text from "95% accuracy" to "82% accuracy"
- Now aligns with actual model performance (81.6%)
- Students won't be confused by discrepancies

### Fix 2: Proper Solution Approach
- **Removed**: Broken threshold adjustment section
- **Added**: Proper fix by retraining with `class_weight='balanced'`
- **Result**:
  - Accuracy improves from 81.6% → 98.2% ✅
  - Recall for malignant improves from 51.2% → 97.7% ✅ (+47 percentage points!)
  - Recall for benign stays high at 98.6% ✅
  - A win-win solution with no negative tradeoffs

### Fix 3: Teaches Correct Lesson
Students now learn:
- ✅ Fix the ROOT CAUSE (bad class weights) by retraining properly
- ✅ Use `class_weight='balanced'` for imbalanced datasets
- ✅ Don't try to patch a badly-trained model - retrain it correctly
- ✅ Confusion matrices help diagnose the problem
- ✅ Recall per class reveals hidden issues

### Fix 4: Student-Friendly Scaffolding
- **Student version**: Has blanks (`____`) for students to fill in
- **Solution version**: Complete with all answers and detailed explanations
- Both versions are pedagogically sound and teach the right lessons

---

## 📊 Performance Comparison

| Metric | Buggy Model | Fixed Model | Improvement |
|--------|-------------|-------------|-------------|
| Overall Accuracy | 81.6% | 98.2% | +16.7pp |
| Recall (Malignant) | 51.2% | 97.7% | **+46.5pp** ⬆️ |
| Recall (Benign) | 100.0% | 98.6% | -1.4pp |

**Key Insight**: The fix dramatically improves malignant recall (catching cancer cases) while maintaining excellent overall performance!

---

## 🎯 Learning Objectives Achieved

Students will now:
1. ✅ Use confusion matrices to diagnose classifier problems
2. ✅ Identify when accuracy is misleading
3. ✅ Calculate and interpret precision and recall
4. ✅ Understand class imbalance issues
5. ✅ **FIX problems by retraining with proper class weights** (NEW!)

---

## 📁 Files Created

1. **`week2_pair_programming_STUDENT.ipynb`** - For students, with blanks to fill in
2. **`week2_pair_programming_SOLUTION.ipynb`** - Complete solution with explanations
3. **`verify_solution.py`** - Verification script to ensure correctness

---

## ⚠️ Note About RuntimeWarnings

When running the buggy model, you may see sklearn warnings like:
```
RuntimeWarning: divide by zero encountered in matmul
RuntimeWarning: overflow encountered in matmul
```

**This is expected!** The extreme class weights `{0: 0.01, 1: 20}` cause numerical instability. This actually reinforces the lesson that badly configured models have problems.

The warnings disappear when using the properly balanced model.

---

## 🚀 Recommendation

**Use the new versions (`_STUDENT` and `_SOLUTION`) going forward.**

The original version (`week2_pair_programming copy.ipynb`) should be deprecated or deleted to avoid confusion.

---

## Questions?

If you have questions about these changes or want to discuss the pedagogical approach, feel free to reach out!

---

*Updated: February 2026*
