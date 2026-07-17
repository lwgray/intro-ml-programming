# Week 7 Pre-Class Practice Notebook - Redesign Specification

**Date:** March 9, 2026
**Author:** Claude (AI Assistant)
**Purpose:** Redesign Week 7 pre-class practice to avoid duplication with live session

---

## Problem Statement

### Current Issue
The current Week 7 pre-class practice notebook uses **Fashion-MNIST**, which is the **exact same dataset** used in the live session. This creates duplication similar to the Week 5 issue we just fixed.

**Evidence:**
- Pre-class practice: Fashion-MNIST review
- Live session Segment 2: Introduce Fashion-MNIST
- Live session Segment 4: Intentionally overfit Fashion-MNIST
- Live session Segment 6: Build complete Fashion-MNIST classifier with regularization
- Live session Segment 7: Pair programming - fix overfitting on Fashion-MNIST

**Result:** Students practice the exact same thing twice, reducing the value of both activities.

---

## Solution Approach

### Design Philosophy (Mirroring Week 5 Fix)

**Week 5 Solution Applied:**
- Pre-class: Synthetic blob data (visual, exploratory)
- Live session: Real Mall Customers data (business application)
- **Result:** Different datasets, complementary learning

**Week 7 Solution:**
- Pre-class: Simple 2D moons dataset (visual curve-reading practice)
- Live session: Real Fashion-MNIST (production regularization techniques)
- **Result:** Build intuition first, apply to real data in class

---

## Detailed Changes

### 1. Dataset Change

#### OLD (Current):
```python
from keras.datasets import fashion_mnist
(X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()
```
- Fashion-MNIST (28×28 images, 10 classes)
- Same as live session
- Complex for learning curve interpretation

#### NEW (Proposed):
```python
from sklearn.datasets import make_moons
X, y = make_moons(n_samples=1000, noise=0.2, random_state=42)
```
- Two interleaving half-moons (2D, binary classification)
- **Different from live session**
- Simple visualization makes overfitting patterns obvious

**WHY:**
- 2D scatter plots are easier to understand than 28×28 images
- Overfitting is visually obvious in simple data
- Saves Fashion-MNIST for live session impact
- Focuses student attention on CURVE READING, not data complexity

---

### 2. Learning Objective Change

#### OLD (Current):
**Objective:** Review Week 6 neural network basics
- Load and visualize Fashion-MNIST
- Build basic neural network
- Train and plot curves
- **Problem:** This is just Week 6 review, not Week 7 prep

#### NEW (Proposed):
**Objective:** Learn to DIAGNOSE overfitting from curves
- See three models with different behaviors
- Practice identifying overfitting visually
- Understand good fit vs. overfit vs. underfit
- **Benefit:** Direct preparation for Week 7's main topic

**WHY:**
- Week 7 is about PRODUCTION PRACTICES, not building networks
- Students need to recognize problems BEFORE learning solutions
- Detective approach (diagnosis) before treatment (regularization)

---

### 3. Structure Change

#### OLD (Current):
6 parts:
1. Load Fashion-MNIST
2. Normalize/flatten
3. Build network
4. Train model
5. Plot curves
6. Review questions

**Problem:** Linear, procedural, no exploration

#### NEW (Proposed):
6 parts:
1. Setup
2. Simple dataset introduction
3. **Three models comparison** (overfit, underfit, good fit)
4. **Side-by-side visual comparison**
5. Preview of fixes (Dropout, EarlyStopping)
6. Test your understanding

**WHY:**
- Comparative approach: see patterns across multiple examples
- Visual focus: curves tell the story
- Detective work: students actively diagnose, not just follow steps
- Preview: connects to live session without duplicating it

---

### 4. Specific Content Changes

#### Change 4A: Add Three Model Comparison

**NEW CONTENT:**

**Model A: "The Eager Student"** (Overfitting)
- Architecture: 3 layers, 128 neurons each
- Training: 200 epochs
- Result: Training acc ~100%, Validation acc ~85% (BIG GAP)
- **Learning:** This is overfitting - memorizing training data

**Model B: "The Lazy Student"** (Underfitting)
- Architecture: 2 layers, 4 neurons each
- Training: 50 epochs
- Result: Training acc ~75%, Validation acc ~73% (small gap, both LOW)
- **Learning:** This is underfitting - too simple to learn patterns

**Model C: "The Goldilocks"** (Good Fit)
- Architecture: 2 layers, 16 neurons each
- Training: 100 epochs
- Result: Training acc ~90%, Validation acc ~88% (small gap, both HIGH)
- **Learning:** This is good fit - generalizes well

**WHY:**
- Students see all three scenarios in one session
- Pattern recognition: visual comparison makes differences obvious
- Practical: "Which would you deploy?" question builds judgment

---

#### Change 4B: Add Detective Questions

**NEW INTERACTIVE ELEMENTS:**

After each model, students answer:
1. **Is this model overfitting?** (Yes/No)
2. **What clues tell you this?** (Gap size, curve divergence)
3. **Would you deploy this to production?** (Judgment call)

**WHY:**
- Active learning vs. passive reading
- Forces students to articulate what they see
- Builds confidence in diagnosis
- Prepares for live session discussions

---

#### Change 4C: Add Side-by-Side Comparison

**NEW VISUALIZATION:**

```python
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
# Plot all three models' curves side-by-side
# Color code: Blue = training, Orange = validation
```

Shows all three models' accuracy curves in one plot with labels:
- Model A: "The Eager Student" (overfitting)
- Model B: "The Lazy Student" (underfitting)
- Model C: "The Goldilocks" (good fit)

**WHY:**
- Visual comparison is more powerful than sequential
- Students can directly compare gap sizes
- Pattern recognition: spot overfitting at a glance
- Memorable: "Goldilocks" metaphor sticks

---

#### Change 4D: Add Solutions Preview (Not Implementation)

**NEW SECTION: "How Do We Fix Overfitting?"**

Show CODE SNIPPETS (not full implementation):

```python
# 1. Dropout
layers.Dropout(0.3)  # Turn off 30% randomly

# 2. EarlyStopping
keras.callbacks.EarlyStopping(patience=10)

# 3. Smaller network
# Instead of 128 neurons, use 16-32
```

**WHY:**
- Preview of live session topics
- Builds anticipation without duplication
- Students arrive with questions ("How does Dropout work?")
- Connects pre-class to live session

---

### 5. Time Optimization

#### OLD: 15-20 minutes
- 5 min: Load/visualize Fashion-MNIST
- 5 min: Build/train network
- 5 min: Plot curves
- 5 min: Answer questions

#### NEW: 10-15 minutes
- 2 min: Setup and simple dataset
- 3 min: Model A (overfit) - train and analyze
- 3 min: Model B (underfit) - train and analyze
- 3 min: Model C (good fit) - train and analyze
- 2 min: Side-by-side comparison
- 2 min: Solutions preview

**WHY:**
- Shorter is better for pre-class (students busy)
- Simple data trains FAST (2D moons vs 28×28 images)
- Focuses on ONE skill: reading curves
- More engaging: variety (3 models) vs. repetition (1 model)

---

### 6. Pedagogical Improvements

#### Change 6A: Metaphors

**NEW METAPHORS:**
- **"The Eager Student"** (overfits): Studies too hard, memorizes answers
- **"The Lazy Student"** (underfits): Doesn't study enough, guesses
- **"The Goldilocks"** (good fit): Studies just right, understands concepts

**WHY:**
- Relatable: students understand school metaphors
- Memorable: easier to recall "Eager Student = overfitting"
- Fun: makes technical concepts approachable

---

#### Change 6B: Progressive Disclosure

**OLD:** All concepts at once (normalization, flattening, architecture, training, curves)

**NEW:** One concept at a time
1. First, see what overfitting LOOKS like (Model A curves)
2. Then, see what underfitting LOOKS like (Model B curves)
3. Then, see what good fit LOOKS like (Model C curves)
4. Finally, compare all three side-by-side

**WHY:**
- Cognitive load management: one pattern at a time
- Pattern recognition: repeated exposure to same task (reading curves)
- Scaffolding: simple → complex

---

#### Change 6C: Active Learning

**OLD:** Read → Fill blanks → Run code → Done

**NEW:** Observe → Diagnose → Reflect → Compare
- **Observe:** Look at curves (what do you see?)
- **Diagnose:** Is it overfitting? (Yes/No + Why)
- **Reflect:** Would you deploy this? (Judgment)
- **Compare:** Which model is best? (Synthesis)

**WHY:**
- Bloom's Taxonomy: moves beyond "remember" to "analyze" and "evaluate"
- Engagement: students think, not just execute
- Preparation: live session will ask same questions about Fashion-MNIST

---

### 7. Connection to Live Session

#### How Pre-Class Prepares for Live Session

**Pre-class builds:** Curve-reading intuition with simple data

**Live session applies:** Same intuition to real Fashion-MNIST

**Specific connections:**

| Pre-Class | Live Session | Connection |
|-----------|--------------|------------|
| See overfitting in moons | Intentionally overfit Fashion-MNIST | "Remember the Eager Student? This is the same pattern!" |
| Learn gap = overfitting | Monitor Fashion-MNIST val curves | "You already know to watch for the gap!" |
| Preview Dropout code | Implement Dropout | "You saw this snippet - now let's use it!" |
| Compare 3 models visually | Try different architectures | "Same comparison, real data!" |

**WHY:**
- Scaffolding: simple practice → complex application
- Confidence: students recognize patterns in new context
- Efficiency: live session can skip basics, dive into techniques

---

## Implementation Notes

### Code Structure

**Notebook organization:**
```
Part 1: Setup (imports, simple dataset)
Part 2: Model A - The Eager Student
  - Build (128 neurons, 3 layers)
  - Train (200 epochs)
  - Plot curves
  - Detective questions
Part 3: Model B - The Lazy Student
  - Build (4 neurons, 2 layers)
  - Train (50 epochs)
  - Plot curves
  - Detective questions
Part 4: Model C - The Goldilocks
  - Build (16 neurons, 2 layers)
  - Train (100 epochs)
  - Plot curves
  - Detective questions
Part 5: Side-by-Side Comparison
  - All three models in one plot
  - Key patterns summary
Part 6: Solutions Preview
  - Dropout snippet
  - EarlyStopping snippet
  - Preview of live session
Part 7: Test Understanding
  - 3 multiple choice questions
  - Answers at bottom
```

---

### Visual Design

**Consistent color scheme:**
- Training curves: **Blue**
- Validation curves: **Orange**
- Good fits: Green highlight
- Bad fits: Red highlight

**Plot sizes:**
- Individual model plots: 14×5 inches (2 subplots)
- Comparison plot: 18×5 inches (3 subplots)
- Consistent font sizes (12-14pt)

---

### Student Experience

**What students will experience:**

1. **Minute 0-2:** "Oh, this is a simple 2D dataset - I can see the two moons!"
2. **Minute 2-5:** "Model A looks perfect on training... but wait, validation is bad. That's the gap they mentioned!"
3. **Minute 5-8:** "Model B has no gap, but both are terrible. I guess that's underfitting?"
4. **Minute 8-11:** "Model C looks balanced - this is the 'good' one!"
5. **Minute 11-13:** "Looking at all three side-by-side, I can now spot overfitting instantly!"
6. **Minute 13-15:** "Oh, Dropout and EarlyStopping are how we fix it. Can't wait for class!"

**Emotional journey:**
- Confusion → Recognition → Confidence → Anticipation

---

## Success Metrics

### How to measure if redesign worked:

**Immediate (Pre-class):**
- [ ] Students complete notebook in 10-15 minutes
- [ ] Students correctly identify overfitting in test questions
- [ ] Students express curiosity about solutions in pre-session questions

**Live Session:**
- [ ] Students recognize overfitting in Fashion-MNIST without prompting
- [ ] Students reference "Eager Student" metaphor when discussing overfitting
- [ ] Instructor can skip curve-reading basics, dive into regularization
- [ ] Students successfully diagnose pair programming model issues

**Post-Class:**
- [ ] Homework submissions show correct overfitting diagnosis
- [ ] Student evaluations mention "pre-class prepared me well"
- [ ] Fewer basic questions about "what is overfitting?"

---

## Comparison Summary

### Side-by-Side: Old vs New

| Aspect | OLD (Current) | NEW (Proposed) |
|--------|---------------|----------------|
| **Dataset** | Fashion-MNIST | 2D Moons |
| **Same as live?** | ❌ YES (duplicates) | ✅ NO (different) |
| **Objective** | Review Week 6 | Learn to spot overfitting |
| **Approach** | Procedural steps | Detective exploration |
| **Models** | 1 model | 3 models (compare) |
| **Time** | 15-20 min | 10-15 min |
| **Focus** | Building networks | Reading curves |
| **Complexity** | High (28×28 images) | Low (2D scatter) |
| **Engagement** | Passive (fill blanks) | Active (diagnose) |
| **Connection** | Weak (review) | Strong (prepares) |
| **Memorability** | Low | High (metaphors) |

---

## Risk Mitigation

### Potential Issues and Solutions

**Issue 1:** "Students might find moons dataset too simple/boring"
- **Mitigation:** Frame as "detective training" - simple data lets you see patterns clearly
- **Mitigation:** Emphasize "you'll apply this to Fashion-MNIST in class!"

**Issue 2:** "Three models might take too long to train"
- **Mitigation:** Moons dataset trains in seconds (vs. minutes for Fashion-MNIST)
- **Mitigation:** Use `verbose=0` to suppress training output

**Issue 3:** "Students might want to practice Fashion-MNIST before class"
- **Mitigation:** Pre-class guide says "Fashion-MNIST in live session - focus on curves now"
- **Mitigation:** Make moons practice SO engaging they don't miss Fashion-MNIST

**Issue 4:** "Instructor might not know about the redesign"
- **Mitigation:** Add note at top of notebook explaining the change
- **Mitigation:** Update teaching guide to reference pre-class detective work

---

## Next Steps

1. **Get approval** for redesign approach
2. **Write new notebook** with three-model comparison
3. **Test notebook** (run all cells, verify plots)
4. **Update teaching guide** to reference pre-class learning
5. **Add connection points** in live session ("Remember the Eager Student?")
6. **Update pre-class study guide** to mention detective approach

---

## Conclusion

**The Problem:**
Week 7 pre-class practice duplicates the live session by using Fashion-MNIST.

**The Solution:**
Redesign pre-class practice to use simple 2D moons dataset with three-model comparison (overfit, underfit, good fit), teaching curve-reading as a detective skill.

**The Benefit:**
- Students learn ONE focused skill: spotting overfitting from curves
- Live session can build on this foundation with real Fashion-MNIST + regularization
- No duplication - complementary learning like Week 5's redesign
- More engaging - detective metaphors, visual comparison, active diagnosis
- Better preparation - students arrive knowing what overfitting LOOKS like

**The Why:**
Just like Mall Customers is more impactful when students have blob-clustering intuition first, Fashion-MNIST regularization is more impactful when students can already read curves and spot overfitting.

---

**Ready to implement:** This specification provides complete details for creating the new notebook. All content, code, structure, and pedagogical decisions are documented.

---

*End of Specification Document*