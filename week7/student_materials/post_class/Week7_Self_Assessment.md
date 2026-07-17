# Week 7 Self-Assessment Checklist

**Purpose:** Verify your understanding of Week 7 concepts before Week 8

**Instructions:** Complete this honestly to identify areas for review

---

## How to Use This Checklist

For each skill:
- ✅ **Confident:** Can do independently without references
- ⚠️ **Needs Practice:** Understand concept but need to review
- ❌ **Need Help:** Don't understand or can't do yet

**Be honest!** This helps you focus your study time.

---

## Part 1: Conceptual Understanding

### Overfitting Diagnosis

| Skill | Status | Notes |
|-------|--------|-------|
| I can explain what overfitting is in my own words | ☐ | |
| I can recognize overfitting from training curves | ☐ | |
| I understand why overfitting is a problem | ☐ | |
| I can explain the difference between bias and variance | ☐ | |

**Self-Check Question:** *If training accuracy is 95% and validation accuracy is 75%, what's the problem?*
<details>
<summary>Answer</summary>
Overfitting - the model memorized training data but doesn't generalize to new data.
</details>

---

### Data Splitting Strategy

| Skill | Status | Notes |
|-------|--------|-------|
| I understand the purpose of training set | ☐ | |
| I understand the purpose of validation set | ☐ | |
| I understand the purpose of test set | ☐ | |
| I know when to use each set | ☐ | |
| I can explain why we DON'T use test set during training | ☐ | |

**Self-Check Question:** *Why do we need both validation and test sets? Why not just train/test?*
<details>
<summary>Answer</summary>
Validation set monitors overfitting during training. Test set provides final, unbiased evaluation after all training decisions are made. Using only train/test risks overfitting to the test set through hyperparameter tuning.
</details>

---

### Dropout Regularization

| Skill | Status | Notes |
|-------|--------|-------|
| I can explain how Dropout prevents overfitting | ☐ | |
| I know where to place Dropout layers | ☐ | |
| I know where NOT to place Dropout (output layer) | ☐ | |
| I understand what dropout rate means | ☐ | |
| I know typical dropout rates (0.2-0.5) | ☐ | |

**Self-Check Question:** *Why do we NOT add Dropout after the output layer?*
<details>
<summary>Answer</summary>
Output layer needs all neurons active for predictions. Dropout is only for training regularization, and randomly dropping output neurons would corrupt predictions.
</details>

---

### EarlyStopping Callback

| Skill | Status | Notes |
|-------|--------|-------|
| I can explain what EarlyStopping does | ☐ | |
| I understand what 'patience' parameter means | ☐ | |
| I know why we monitor 'val_loss' not 'loss' | ☐ | |
| I understand 'restore_best_weights' purpose | ☐ | |
| I know EarlyStopping requires validation_data | ☐ | |

**Self-Check Question:** *What does patience=5 mean?*
<details>
<summary>Answer</summary>
If validation loss doesn't improve for 5 consecutive epochs, stop training. This gives the model time to improve before stopping.
</details>

---

## Part 2: Practical Skills

### Data Preparation

| Skill | Status | Notes |
|-------|--------|-------|
| I can load Fashion-MNIST dataset | ☐ | |
| I can normalize pixel values (/ 255.0) | ☐ | |
| I can perform three-way split using train_test_split | ☐ | |
| I can flatten images for Dense layers | ☐ | |
| I can verify data shapes after preprocessing | ☐ | |

**Hands-On Test:** Can you write code from memory to load, normalize, split, and flatten Fashion-MNIST?

---

### Model Architecture

| Skill | Status | Notes |
|-------|--------|-------|
| I can build Sequential model with Dropout layers | ☐ | |
| I can add Dropout after Dense layers correctly | ☐ | |
| I can choose appropriate dropout rates | ☐ | |
| I can use model.summary() to check architecture | ☐ | |
| I can count trainable parameters | ☐ | |

**Hands-On Test:** Build model: 784 → Dense(128, relu) → Dropout(0.3) → Dense(64, relu) → Dropout(0.3) → Dense(10, softmax)

---

### Training Configuration

| Skill | Status | Notes |
|-------|--------|-------|
| I can compile model with correct optimizer, loss, metrics | ☐ | |
| I can create EarlyStopping callback | ☐ | |
| I can train model with validation_data | ☐ | |
| I can pass callbacks to model.fit() | ☐ | |
| I can set appropriate epochs and batch_size | ☐ | |

**Hands-On Test:** Configure EarlyStopping monitoring val_loss, patience=5, restore_best_weights=True

---

### Training Curves Analysis

| Skill | Status | Notes |
|-------|--------|-------|
| I can plot training and validation curves | ☐ | |
| I can identify healthy learning pattern | ☐ | |
| I can identify overfitting pattern | ☐ | |
| I can identify underfitting pattern | ☐ | |
| I can calculate gap between train/val accuracy | ☐ | |

**Hands-On Test:** Plot loss and accuracy curves side-by-side with proper labels and legends

---

### Model Evaluation & Persistence

| Skill | Status | Notes |
|-------|--------|-------|
| I can evaluate model on test set | ☐ | |
| I can compare test vs validation accuracy | ☐ | |
| I can save model with .keras extension | ☐ | |
| I can load saved model | ☐ | |
| I can use loaded model for predictions | ☐ | |

**Hands-On Test:** Save model to 'my_model.keras', load it back, and make predictions

---

## Part 3: Debugging Skills

### Common Errors I Can Fix

| Error | Can Fix? | Notes |
|-------|----------|-------|
| "EarlyStopping not working" (forgot validation_data) | ☐ | |
| Dropout after output layer reducing accuracy | ☐ | |
| Not normalizing data (values 0-255 instead of 0-1) | ☐ | |
| Wrong history keys ('val_loss' vs 'validation_loss') | ☐ | |
| Touching test set during training | ☐ | |
| Model not improving (learning rate too high/low) | ☐ | |

---

## Part 4: Week 7 Workflow Mastery

**The Complete Production Workflow:**

Can you perform these steps in order?

| Step | Can Do? | Notes |
|------|---------|-------|
| 1. Load and normalize data | ☐ | |
| 2. Perform three-way split (train/val/test) | ☐ | |
| 3. Flatten data for Dense layers | ☐ | |
| 4. Build model with Dropout layers | ☐ | |
| 5. Compile model | ☐ | |
| 6. Configure EarlyStopping callback | ☐ | |
| 7. Train with validation_data and callbacks | ☐ | |
| 8. Plot training curves | ☐ | |
| 9. Diagnose overfitting/underfitting | ☐ | |
| 10. Evaluate on test set (ONCE) | ☐ | |
| 11. Save model for deployment | ☐ | |

**Challenge:** Can you complete all 11 steps from memory in under 30 minutes?

---

## Part 5: Advanced Concepts (Bonus)

### Beyond Week 7 Basics

| Concept | Familiar? | Notes |
|---------|-----------|-------|
| L2 regularization (kernel_regularizer) | ☐ | |
| Batch normalization (layers.BatchNormalization) | ☐ | |
| Learning rate scheduling | ☐ | |
| Different optimizers (SGD, RMSprop) | ☐ | |
| ModelCheckpoint callback | ☐ | |

---

## Scoring Guide

Count your ✅ marks in Parts 1-4:

- **40-45 ✅:** Excellent! You've mastered Week 7
- **30-39 ✅:** Good! Review areas marked ⚠️ or ❌
- **20-29 ✅:** Needs work. Focus on weak areas before Week 8
- **< 20 ✅:** Significant gaps. Review Week 7 materials thoroughly

---

## Action Plan Based on Results

### If Score < 30: Priority Review Areas

1. **Re-watch:** StatQuest Bias-Variance video
2. **Re-read:** Week 7 Pre-Class Study Guide
3. **Re-do:** Week 7 live session notebook
4. **Practice:** Post-class exercise again
5. **Ask:** Post questions in #week7-questions

### If Score 30-39: Targeted Practice

1. Focus on ⚠️ and ❌ areas
2. Complete bonus architecture experiments
3. Pair programming exercise review
4. Practice debugging common errors

### If Score 40+: Extend Your Knowledge

1. Complete bonus architecture experiments
2. Explore L2 regularization
3. Try batch normalization
4. Help classmates in discussion forum
5. Read advanced Keras documentation

---

## Common Weak Areas & How to Improve

### "I understand concepts but struggle with code"

**Fix:** Practice typing code from memory
- Don't copy-paste
- Type each line, explain it out loud
- Do 3-4 complete pipelines from scratch

### "I can code but don't understand why"

**Fix:** Focus on conceptual understanding
- Draw training curves patterns
- Explain each technique to someone else
- Use analogies (Network on a Diet, Validation Alarm)

### "EarlyStopping confuses me"

**Fix:** Study the parameters
- Experiment with different patience values
- Watch training with and without EarlyStopping
- Plot curves to see when it stops

### "Dropout placement is unclear"

**Fix:** Remember the rules
- After Dense layers (not output)
- Before next layer
- Typical rates: 0.2-0.5
- Higher rate = stronger regularization

---

## Ready for Week 8?

**You're ready if you can:**
- ✅ Build Fashion-MNIST classifier with regularization from scratch
- ✅ Diagnose overfitting from training curves
- ✅ Apply Dropout and EarlyStopping correctly
- ✅ Achieve 85%+ test accuracy
- ✅ Save and load models

**Week 8 Preview:** Convolutional Neural Networks (CNNs) for image data

---

## Questions to Ask Before Week 8

If any of these are unclear, ask NOW:

1. Why do we need three data splits instead of two?
2. How does Dropout help during training but not during prediction?
3. Why monitor validation loss for EarlyStopping, not training loss?
4. What's the difference between early stopping and just training for fewer epochs?
5. When should I use Dropout vs L2 regularization?

---

## Self-Assessment Date: ______________

**Reassess after review:** ______________

**Notes for improvement:**
_________________________________________________________________________
_________________________________________________________________________
_________________________________________________________________________

---

*Week 7 Self-Assessment | Version 1.0 | February 2026*
