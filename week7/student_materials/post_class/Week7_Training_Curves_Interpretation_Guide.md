# Week 7: Training Curves Interpretation Guide

**Visual guide to diagnosing model training from curves**

---

## Overview

Training curves are your diagnostic tool. Learn to read them like a doctor reads medical charts!

**What we plot:**
- Loss (left plot): Lower is better
- Accuracy (right plot): Higher is better
- Training line: Performance on training data
- Validation line: Performance on validation data

**Key insight:** The relationship between training and validation curves tells you what's happening.

---

## The Four Classic Patterns

### Pattern 1: Healthy Learning ✅

**Visual Description:**
```
Loss                           Accuracy
↑                              ↑
│                              │ train ----
│ train ----                   │        ----
│      ----   val ----         │            ----
│          ----    ----        │ val ----       ----
│              ----            │      ----           ----
└─────────────────→ Epochs     └─────────────────→ Epochs
```

**Characteristics:**
- Both training and validation loss decreasing
- Both accuracies increasing
- Lines stay close together (small gap)
- Validation line slightly below training (normal)

**Diagnosis:** Model is learning well! No action needed.

**Typical metrics:**
- Training accuracy: 88%
- Validation accuracy: 87%
- Gap: < 2%

**What this means:**
- Model generalizes well
- Not overfitting
- Good balance of capacity and regularization

**Example code that produces this:**
```python
model = keras.Sequential([
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.3),  # Good regularization
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(10, activation='softmax')
])

early_stop = EarlyStopping(
    monitor='val_loss',
    patience=5,
    restore_best_weights=True
)
```

---

### Pattern 2: Beginning to Overfit ⚠️

**Visual Description:**
```
Loss                           Accuracy
↑                              ↑
│                              │
│ train ----                   │ train ----
│      ----                    │        --------
│          ----                │               ----
│ val ----    ----             │
│      ----       ↗            │ val ----
│          ----                │      ----
│              ----            │          ----
└─────────────────→ Epochs     └─────────────────→ Epochs
   gap opening                    gap opening
```

**Characteristics:**
- Training loss still decreasing
- Validation loss flattening or slightly increasing
- Training accuracy climbing
- Validation accuracy plateauing
- Gap starting to widen (3-5%)

**Diagnosis:** Early overfitting. EarlyStopping should trigger soon.

**Typical metrics:**
- Training accuracy: 92%
- Validation accuracy: 87%
- Gap: 5%

**What to do:**
- Wait for EarlyStopping to trigger
- If no EarlyStopping, stop training manually
- Consider adding more Dropout
- Acceptable if gap < 5%

**Why this happens:**
- Model has sufficient capacity
- Starting to memorize training specifics
- Needs to stop soon

---

### Pattern 3: Severe Overfitting ❌

**Visual Description:**
```
Loss                           Accuracy
↑                              ↑
│                              │
│                              │ train ----
│ train ----                   │        --------
│      ----                    │               --------
│          ----                │                      ----
│              ----            │
│ val ----                     │
│      ----  ↗↗↗               │ val ----
│          ↗↗                  │      ----
│        ↗↗                    │          ----
└─────────────────→ Epochs     └─────────────────→ Epochs
   LARGE GAP                      LARGE GAP
```

**Characteristics:**
- Training loss very low and still decreasing
- Validation loss INCREASING (diverging)
- Training accuracy very high (95%+)
- Validation accuracy stagnant or dropping
- Large gap (> 10%)

**Diagnosis:** Model is memorizing training data! Overfitting badly.

**Typical metrics:**
- Training accuracy: 98%
- Validation accuracy: 82%
- Gap: 16%

**What went wrong:**
- No Dropout or insufficient dropout rate
- No EarlyStopping or patience too high
- Model too complex for dataset
- Training too long

**How to fix:**
```python
# Add Dropout
layers.Dropout(0.4)  # Increase rate

# Add EarlyStopping with lower patience
early_stop = EarlyStopping(
    monitor='val_loss',
    patience=3,  # Stop sooner
    restore_best_weights=True
)

# Or: Use simpler architecture
# Fewer layers or neurons per layer
```

**Real example that causes this:**
```python
# BAD: No regularization!
model = keras.Sequential([
    layers.Dense(512, activation='relu'),
    layers.Dense(256, activation='relu'),
    layers.Dense(128, activation='relu'),
    # NO Dropout!
    layers.Dense(10, activation='softmax')
])

# Training for 50 epochs without EarlyStopping
history = model.fit(X_train, y_train, epochs=50)  # No validation_data!
```

---

### Pattern 4: Underfitting 📉

**Visual Description:**
```
Loss                           Accuracy
↑                              ↑
│                              │
│ train ────────────           │ train ────────────
│                              │
│                              │
│ val ──────────────           │ val ──────────────
│                              │
│                              │
│                              │
└─────────────────→ Epochs     └─────────────────→ Epochs
   Both high                      Both low
```

**Characteristics:**
- Both training and validation loss HIGH
- Both accuracies LOW (< 80%)
- Lines close together but flat
- No improvement over epochs

**Diagnosis:** Model too simple! Can't learn patterns.

**Typical metrics:**
- Training accuracy: 75%
- Validation accuracy: 74%
- Gap: 1% (good!) but both too low

**What went wrong:**
- Model architecture too simple
- Too much regularization (dropout rate too high)
- Learning rate too low
- Not enough training epochs

**How to fix:**
```python
# Increase model capacity
model = keras.Sequential([
    layers.Dense(256, activation='relu'),  # More neurons
    layers.Dropout(0.2),  # Lower dropout rate
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(10, activation='softmax')
])

# Train longer
history = model.fit(X_train, y_train, epochs=30)  # More epochs

# Or: Remove some Dropout
# Or: Use larger learning rate
```

**Example that causes this:**
```python
# BAD: Too simple!
model = keras.Sequential([
    layers.Dense(32, activation='relu'),  # Only 32 neurons
    layers.Dropout(0.7),  # Way too much dropout!
    layers.Dense(10, activation='softmax')
])
```

---

## Quick Diagnostic Flowchart

```
Start: Look at your training curves
│
├─ Training and validation close together?
│  ├─ YES, both improving → ✅ Healthy Learning
│  └─ YES, both flat/high → 📉 Underfitting
│
└─ Training and validation diverging?
   ├─ Small gap (3-5%) → ⚠️ Beginning to Overfit (OK if EarlyStopping soon)
   └─ Large gap (> 10%) → ❌ Severe Overfitting
```

---

## Pattern Recognition Practice

### Example 1
- Training accuracy: 89%
- Validation accuracy: 88%
- Curves: Both decreasing smoothly

**Answer:** Healthy Learning ✅

---

### Example 2
- Training accuracy: 96%
- Validation accuracy: 80%
- Curves: Train improving, validation flat

**Answer:** Severe Overfitting ❌

---

### Example 3
- Training accuracy: 72%
- Validation accuracy: 71%
- Curves: Both flat, not improving

**Answer:** Underfitting 📉

---

### Example 4
- Training accuracy: 91%
- Validation accuracy: 87%
- Curves: Small gap opening

**Answer:** Beginning to Overfit ⚠️

---

## Common Questions

**Q: Is ANY gap between train/val bad?**
A: No! Small gap (1-3%) is normal. Training set is easier because model sees it repeatedly. Only large gaps (> 5%) indicate problems.

**Q: My validation loss is higher from epoch 1. Is that overfitting?**
A: No. Validation loss is often slightly higher initially (especially with Dropout). Look for divergence over time, not absolute values.

**Q: Can I have high accuracy but still be overfitting?**
A: Yes! If training accuracy is 98% and validation is 85%, you're overfitting even though 85% seems good. The gap matters.

**Q: What if train/val curves are noisy/jumpy?**
A: Common causes:
- Batch size too small (try 128 instead of 32)
- Learning rate too high (rare with Adam)
- Dataset has high variance
Normal for some data. Look at trend, not individual points.

**Q: Should I always use EarlyStopping?**
A: Yes for production! It's free insurance against overfitting. Only skip for quick experiments.

---

## How to Use This Guide During Training

**Step 1: Train model**
```python
history = model.fit(...)
```

**Step 2: Plot curves**
```python
plt.plot(history.history['loss'], label='Training')
plt.plot(history.history['val_loss'], label='Validation')
plt.legend()
plt.show()
```

**Step 3: Identify pattern**
- Compare to the 4 patterns above
- Check gap size
- Look at curve shapes

**Step 4: Take action**
- Healthy Learning → Deploy!
- Beginning to Overfit → Wait for EarlyStopping
- Severe Overfitting → Add regularization
- Underfitting → Increase capacity

---

## Real Week 7 Examples

### From Live Session (Segment 3)
**Before regularization:**
```
Pattern: Severe Overfitting ❌
Train accuracy: 99%
Val accuracy: 85%
Gap: 14%
Action: Add Dropout + EarlyStopping
```

### From Live Session (Segment 6)
**After regularization:**
```
Pattern: Healthy Learning ✅
Train accuracy: 89%
Val accuracy: 87%
Gap: 2%
Result: Production-ready!
```

### From Pair Programming
**Overfitting model provided:**
```
Pattern: Severe Overfitting ❌
Students fix with Dropout
Result: Healthy Learning ✅
```

---

## Advanced: Epoch-by-Epoch Analysis

Sometimes you need to analyze specific epochs:

**Epoch 5:**
- Train loss: 0.45, Val loss: 0.48 → Healthy

**Epoch 10:**
- Train loss: 0.32, Val loss: 0.40 → Healthy

**Epoch 15:**
- Train loss: 0.22, Val loss: 0.41 → Beginning to overfit

**Epoch 20:**
- Train loss: 0.15, Val loss: 0.45 → Overfitting worsening

**Epoch 23:**
- EarlyStopping triggers! Restores weights from epoch 10

**This is why we set patience=5:** Give model 5 epochs to improve before stopping.

---

## Summary Table

| Pattern | Train Acc | Val Acc | Gap | Action |
|---------|-----------|---------|-----|--------|
| Healthy Learning | 88% | 87% | 1-3% | Deploy! |
| Beginning Overfit | 92% | 87% | 5% | Wait for EarlyStopping |
| Severe Overfit | 98% | 82% | 16% | Add Dropout, reduce capacity |
| Underfitting | 75% | 74% | 1% | Increase capacity, lower dropout |

---

## Checklist: Can You Diagnose Curves?

After studying this guide, can you:
- [ ] Recognize Healthy Learning pattern
- [ ] Identify overfitting from diverging curves
- [ ] Distinguish beginning vs severe overfitting
- [ ] Recognize underfitting (both curves flat/high)
- [ ] Calculate gap between train/val accuracy
- [ ] Suggest fixes for each pattern
- [ ] Explain why gap matters more than absolute accuracy

---

## Practice Exercise

**Go to your Week 7 post-class notebook and:**
1. Plot your training curves
2. Identify which pattern you see
3. Calculate the gap
4. Determine if your model is production-ready

**Share your curves in #week7-discussion and practice diagnosing classmates' curves!**

---

*Week 7 Training Curves Guide | Version 1.0 | February 2026*
