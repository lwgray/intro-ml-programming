# Week 7 Pre-Class Study Guide

**Topic:** Deep Learning Best Practices
**Estimated Time:** 25 minutes
**Due:** Before Week 7 live session

---

## Overview

This week you'll learn production-ready deep learning practices: diagnosing overfitting, applying regularization, and saving models. Week 7 builds directly on Week 6's neural network foundations.

---

## Learning Objectives

By the end of Week 7, you will:

1. Diagnose overfitting by plotting training/validation curves
2. Implement three-way data split (train/validation/test)
3. Apply Dropout regularization to prevent overfitting
4. Use EarlyStopping callback to stop training automatically
5. Save and load complete Keras models

---

## Review: Week 6 Concepts

Before Week 7, make sure you understand these Week 6 concepts:

### Keras Sequential API
```python
from keras import models, layers

model = models.Sequential([
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')
])
```

### Compile, Fit, Predict Pattern
```python
# Compile
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Fit (train)
history = model.fit(X_train, y_train, epochs=10)

# Predict
predictions = model.predict(X_test)
```

### Training History
```python
# Plot training curves
import matplotlib.pyplot as plt
plt.plot(history.history['loss'])
plt.plot(history.history['accuracy'])
```

**Self-Check:** Can you build and train a simple neural network on MNIST from memory?

---

## New Concepts for Week 7

### 1. Overfitting (The Problem We're Solving)

**Definition:** Model memorizes training data instead of learning general patterns.

**Symptoms:**

- Training accuracy: 95%
- Validation accuracy: 85%
- Large gap between train and validation performance

**Analogy:** Student who memorizes exact practice problems but can't solve new problems.

---

### 2. Three-Way Data Split (Our Diagnostic Tool)

**Week 6:** Train/Test split (2 sets)
**Week 7:** Train/Validation/Test split (3 sets)

| Set | Purpose | When Used |
|-----|---------|-----------|
| Training | Update model weights | During model.fit() |
| Validation | Monitor overfitting | During model.fit() (via `validation_data`) |
| Test | Final evaluation | After training complete (via model.evaluate()) |

**Analogy:**

- Training set = Textbook (you learn from it)
- Validation set = Practice test (check progress while studying)
- Test set = Final exam (evaluate once at end)

**Code:**
```python
from sklearn.model_selection import train_test_split

X_train, X_val, y_train, y_val = train_test_split(
    X_train_full, y_train_full, test_size=0.2, random_state=42
)
```

---

### 3. Training Curves (Diagnosing Overfitting)

**Healthy Training:**

- Training loss: ↓ decreasing
- Validation loss: ↓ decreasing

**Overfitting:**

- Training loss: ↓ decreasing
- Validation loss: ↑ increasing

**Key Insight:** If training and validation curves diverge, you're overfitting!

---

### 4. Dropout (Our First Fix)

**What it does:** Randomly drops 30% of neurons during training

**Why it helps:** Forces network to learn robust features, not rely on specific neurons

**Where to place:** After Dense layers (not after output layer)

**Code:**
```python
from keras import layers

model = models.Sequential([
    layers.Dense(256, activation='relu'),
    layers.Dropout(0.3),  # Drop 30% of neurons
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(10, activation='softmax')  # NO Dropout here!
])
```

**Common dropout rates:** 0.2 (light), 0.3 (default), 0.5 (heavy)

---

### 5. EarlyStopping (Our Second Fix)

**What it does:** Automatically stops training when validation loss stops improving

**Why it helps:** Prevents overfitting by not training too long

**Code:**
```python
from keras.callbacks import EarlyStopping

early_stop = EarlyStopping(
    monitor='val_loss',           # Watch validation loss
    patience=3,                   # Wait 3 epochs before stopping
    restore_best_weights=True,    # Revert to best epoch
    verbose=1
)

history = model.fit(
    X_train, y_train,
    validation_data=(X_val, y_val),  # Required!
    epochs=50,
    callbacks=[early_stop]
)
```

**Key parameter:** `patience=3` means "if validation loss doesn't improve for 3 consecutive epochs, stop"

---

### 6. Model Saving & Loading

**Save complete model:**
```python
model.save('my_model.keras')
```

**Load model:**
```python
from keras.models import load_model
loaded_model = load_model('my_model.keras')
```

**What's saved:** Architecture + weights + optimizer state (everything!)

---

## Required Pre-Class Viewing

### Video 1: StatQuest - Bias and Variance (6 min)
**URL:** https://www.youtube.com/watch?v=EuBBz3bI-aA

**What you'll learn:**

- Bias = underfitting (model too simple)
- Variance = overfitting (model too complex)
- Visual intuition for overfitting

**Key Takeaway:** Overfitting happens when model is too complex for the data.

---

### Reading: Keras Training Guide - Callbacks Section (15 min)
**URL:** https://keras.io/guides/training_with_built_in_methods/

**What to focus on:**

- How to use `validation_data` in model.fit()
- EarlyStopping callback examples
- ModelCheckpoint callback basics

**Don't worry about:** Custom callbacks, advanced training loops

---

## Fashion-MNIST Dataset Preview

Week 7 uses **Fashion-MNIST** instead of MNIST:

**Similarities to MNIST:**

- 28×28 grayscale images
- 60,000 training, 10,000 test
- 10 classes
- Same loading API

**Differences:**

- Clothing items (not digits)
- Slightly harder to classify
- More realistic challenge

**Classes:**

0. T-shirt/top
1. Trouser
2. Pullover
3. Dress
4. Coat
5. Sandal
6. Shirt
7. Sneaker
8. Bag
9. Ankle boot

**Why Fashion-MNIST?** Harder than MNIST → overfitting more likely → better for learning regularization!

---

## Pre-Class Practice (Optional)

**Notebook:** `week7_preclass_practice.ipynb` (in this folder)

**What it covers:**
- Load MNIST (refresher from Week 6)
- Build simple neural network
- Plot training history
- Practice train/test split

**Estimated time:** 15-20 minutes

**Scaffolding:** 70% provided (focus on reviewing concepts)

---

## Self-Check Questions

Before Week 7, can you answer these?

1. **What's the difference between training and validation sets?**

   <details>
   <summary>Answer</summary>
   Training set: used to update weights. Validation set: used to monitor overfitting (not used for weight updates).
   </details>

2. **How do you recognize overfitting from training curves?**

   <details>
   <summary>Answer</summary>
   Training loss decreasing, but validation loss increasing (or flat). Large gap between training and validation accuracy.
   </details>

3. **Where should you place Dropout layers?**

   <details>
   <summary>Answer</summary>
   After Dense layers, before the next layer. NOT after the output layer.
   </details>

4. **What does patience=5 mean in EarlyStopping?**

   <details>
   <summary>Answer</summary>
   If validation loss doesn't improve for 5 consecutive epochs, stop training.
   </details>

5. **What file extension should you use to save Keras 3.x models?**

   <details>
   <summary>Answer</summary>
   .keras (not .h5, which is legacy format)
   </details>

---

## Common Confusions (Preview)

**"Do I turn off Dropout during prediction?"**

→ No! Keras does this automatically.

**"Why is my validation loss higher from epoch 1?"**

→ This is normal with Dropout. Look for divergence over epochs.

**"What if my training stops at epoch 10 when I set epochs=50?"**

→ That's EarlyStopping working! It stopped early because validation loss stopped improving.

---

## What to Bring to Live Session

1. **Completed pre-class viewing** (videos + reading)
2. **Questions** about overfitting, Dropout, or callbacks
3. **Laptop** with Jupyter and Keras 3.x installed
4. **Refreshed memory** of Week 6 Keras basics

---

## Week 7 Roadmap

**Live Session (3 hours):**

1. Week 6 recap (15 min)
2. Three-way data split (30 min)
3. Overfitting deep dive (30 min)
4. Break (15 min)
5. Regularization techniques (30 min)
6. Live coding: Fashion-MNIST complete pipeline (35 min)
7. Pair programming: "Regularization Detective" (20 min)
8. Wrap-up (5 min)

**Post-Class:**

- Build Fashion-MNIST classifier from scratch
- Experiment with dropout rates
- Practice using callbacks

---

## Key Vocabulary

| Term | Simple Definition |
|------|-------------------|
| **Overfitting** | Model memorizes training data, performs poorly on new data |
| **Validation set** | Data used to monitor overfitting during training |
| **Dropout** | Randomly deactivate neurons during training |
| **Callback** | Function that runs at specific points during training |
| **Patience** | How many epochs to wait before EarlyStopping triggers |
| **restore_best_weights** | Revert to best epoch when stopping |

---

## Next Steps

1. ✅ Watch StatQuest video (6 min)
2. ✅ Read Keras training guide - callbacks section (15 min)
3. ✅ Review this study guide (you're doing it now!)
4. ⬜ (Optional) Complete pre-class practice notebook
5. ⬜ (Optional) Download Fashion-MNIST dataset

## Questions Before Class?

If anything is unclear, don't stress! The live session will bring it all together.

---

**See you in Week 7!**

---

**Version:** Week 7 Study Guide v1.0 | February 2026
