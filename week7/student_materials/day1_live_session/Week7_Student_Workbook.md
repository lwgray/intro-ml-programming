# Week 7 Student Workbook

**Deep Learning Best Practices with Keras**
**Dataset:** Fashion-MNIST
**Duration:** 3 hours

---

## How to Use This Workbook

This workbook provides space for notes, diagrams, and reflections during Week 7's live session. Fill it out as you learn to reinforce concepts and create a personalized reference.

---

## Pre-Session Checklist

Before class starts:
- [ ] Completed pre-class videos (StatQuest Neural Networks Part 8, Keras Training Guide)
- [ ] Reviewed Week 6 materials (Keras basics, Sequential API, MNIST)
- [ ] Have week7_live_session.ipynb open and ready
- [ ] Keras environment verified and working

---

## Segment 1: Week 6 Recap (0:00-0:15)

### What I Remember from Week 6

**Keras Sequential API:**


**Dense Layers:**


**model.compile(), model.fit(), model.predict():**


### Week 7 Preview: What's New Today

Key concepts we'll learn:
1.
2.
3.
4.

**Connection:** "Week 6: Make it work. Week 7: _________________________________"

---

## Segment 2: Data Pipeline (0:15-0:45)

### Fashion-MNIST Dataset

**10 Classes (fill in as instructor shows):**
0. _____________ (T-shirt/top)
1. _____________ (Trouser)
2. _____________ (Pullover)
3. _____________ (Dress)
4. _____________ (Coat)
5. _____________ (Sandal)
6. _____________ (Shirt)
7. _____________ (Sneaker)
8. _____________ (Bag)
9. _____________ (Ankle boot)

**Why Fashion-MNIST instead of MNIST?**



### Three-Way Data Split

Draw the split diagram:

```
[Full Dataset: 70,000 images]
├── Training Set: _______ samples → Purpose: ___________________
├── Validation Set: _______ samples → Purpose: ___________________
└── Test Set: _______ samples → Purpose: ___________________
```

**Key Question:** Why do we need a validation set? (Not just train/test)



**Code Pattern:**
```python
# Split training data into train + validation
from sklearn.model_selection import train_test_split

X_train, X_val, y_train, y_val = train_test_split(
    X_train, y_train,
    test_size=_____,  # What percentage?
    random_state=42
)
```

---

## Segment 3: Overfitting Deep Dive (0:45-1:15)

### Teaching Metaphor: "Overfitting Detective"

**What is overfitting?**



**How do we detect it?** (Draw the curves)

Training Loss vs Validation Loss:


### Four Training Curve Patterns

Sketch each pattern:

**Pattern 1: Healthy Learning**
- Training curve:
- Validation curve:
- Diagnosis:
- Action:

**Pattern 2: Beginning to Overfit**
- Training curve:
- Validation curve:
- Diagnosis:
- Action:

**Pattern 3: Overfitting**
- Training curve:
- Validation curve:
- Diagnosis:
- Action:

**Pattern 4: Underfitting**
- Training curve:
- Validation curve:
- Diagnosis:
- Action:

**Detective Question:** Which pattern indicates our model is memorizing training data?



---

## Segment 4: Break (1:15-1:30)

Use this time to:
- [ ] Review your notes so far
- [ ] Ask questions about overfitting patterns
- [ ] Look at training curve examples

---

## Segment 5: Regularization Techniques (1:30-2:00)

### Solution 1: Dropout

**Teaching Metaphor: "Network on a Diet"**

**What is Dropout?**



**How it works:**
- During training:
- During inference (prediction):

**Code Pattern:**
```python
from keras import layers

model = keras.Sequential([
    layers.Dense(128, activation='relu'),
    layers.Dropout(_____),  # What rate? Hint: 0.2-0.5
    layers.Dense(64, activation='relu'),
    layers.Dropout(_____),
    layers.Dense(10, activation='softmax')
])
```

**Typical dropout rates:** ___________

**Where to place Dropout?** (Draw in architecture diagram)


### Solution 2: Early Stopping

**Teaching Metaphor: "Validation Alarm"**

**What is Early Stopping?**



**How it works:**



**Key Parameters:**

| Parameter | What It Does | Typical Value |
|-----------|--------------|---------------|
| monitor | | |
| patience | | |
| restore_best_weights | | |

**Code Pattern:**
```python
from keras.callbacks import EarlyStopping

early_stop = EarlyStopping(
    monitor=_______________,  # What metric to watch?
    patience=_______________,  # How many epochs to wait?
    restore_best_weights=_______________ # True or False?
)

history = model.fit(
    X_train, y_train,
    validation_data=_______________,  # Critical! What goes here?
    epochs=50,
    callbacks=[early_stop]
)
```

**Important:** What happens if you forget `validation_data`?



---

## Segment 6: Live Coding - Fashion-MNIST (2:00-2:35)

### Complete Pipeline Checklist

Follow along as instructor codes:

- [ ] Load Fashion-MNIST dataset
- [ ] Normalize data (pixel values 0-255 → 0-1)
- [ ] Three-way split (train/val/test)
- [ ] Build model with Dropout layers
- [ ] Configure EarlyStopping callback
- [ ] Compile model
- [ ] Train with validation monitoring
- [ ] Plot training curves
- [ ] Diagnose results
- [ ] Save model

### Architecture Notes

**Model architecture used:**
```python
# Fill in as instructor codes

model = keras.Sequential([
    layers.Input(shape=(_____,)),  # Fashion-MNIST flattened size
    layers.Dense(_____, activation='_____'),
    layers.Dropout(_____),
    layers.Dense(_____, activation='_____'),
    layers.Dropout(_____),
    layers.Dense(_____, activation='_____')
])
```

### Training Results

**Training accuracy:** _________
**Validation accuracy:** _________
**Test accuracy:** _________

**Diagnosis:** Is this overfitting, healthy, or underfitting?



### Plotting Training Curves

**Code pattern to remember:**
```python
import matplotlib.pyplot as plt

plt.plot(history.history['_____'], label='Training Loss')
plt.plot(history.history['_____'], label='Validation Loss')
plt.legend()
plt.show()
```

**What we're looking for:** ___________________________________________

### Model Saving

**How to save:**
```python
model.save('___________________.keras')  # Filename
```

**How to load:**
```python
from keras.models import load_model
loaded_model = load_model('___________________.keras')
```

**What gets saved?**
- [ ] Architecture
- [ ] Weights
- [ ] Optimizer state
- [ ] Training configuration

---

## Segment 7: Pair Programming - "Regularization Detective" (2:35-2:55)

### Exercise Overview

**Task:** Diagnose and fix an overfitting model

**With your partner:**
1. Run the provided overfitting model
2. Plot training curves
3. Diagnose the problem
4. Add Dropout layers
5. Add EarlyStopping callback
6. Re-train and compare
7. Save the improved model

### Your Results

**Before Regularization:**
- Training accuracy: _________
- Validation accuracy: _________
- Pattern observed: _________

**After Regularization:**
- Training accuracy: _________
- Validation accuracy: _________
- Pattern observed: _________

**What you added:**
1. Dropout rate: _________
2. EarlyStopping patience: _________
3. EarlyStopping monitor: _________

**Improvement:** Validation accuracy improved by _________ %

### Insights

**What did you learn from this exercise?**



**What would you try differently next time?**



---

## Segment 8: Wrap-Up (2:55-3:00)

### Key Takeaways

**Three ways to detect overfitting:**
1.
2.
3.

**Three ways to prevent overfitting:**
1.
2.
3.

**Three teaching metaphors:**
1. "_______________________" - Training curves reveal overfitting
2. "_______________________" - Dropout strengthens the model
3. "_______________________" - Early stopping watches for problems

### Week 7 Skills Checklist

By the end of today, I can:
- [ ] Split data into train/validation/test sets
- [ ] Plot training and validation curves
- [ ] Diagnose overfitting from curves
- [ ] Add Dropout layers to a neural network
- [ ] Configure EarlyStopping callback
- [ ] Train with validation monitoring
- [ ] Save and load Keras models
- [ ] Explain when to use regularization

### Questions to Ask

**Questions I still have:**
1.
2.
3.

---

## Post-Class Action Items

- [ ] Complete post-class exercise (week7_postclass_exercise.ipynb)
- [ ] Review training curve patterns
- [ ] Try bonus architecture experiments
- [ ] Complete self-assessment checklist
- [ ] Prepare questions for next week

---

## Personal Notes & Reflections

**What clicked for me today:**



**What I need to review:**



**Connections to my project:**



**Resources to explore:**



---

## Quick Reference Cards

### Callback Configuration Card

```python
from keras.callbacks import EarlyStopping, ModelCheckpoint

# Early Stopping
early_stop = EarlyStopping(
    monitor='val_loss',
    patience=3,
    restore_best_weights=True
)

# Model Checkpoint
checkpoint = ModelCheckpoint(
    filepath='best_model.keras',
    monitor='val_accuracy',
    save_best_only=True
)

# Use in training
history = model.fit(
    X_train, y_train,
    validation_data=(X_val, y_val),
    epochs=50,
    callbacks=[early_stop, checkpoint]
)
```

### Training Curve Diagnosis Card

| Training Loss | Validation Loss | Diagnosis | Action |
|---------------|-----------------|-----------|--------|
| ↓ Decreasing | ↓ Decreasing | Healthy | Continue |
| ↓ Decreasing | → Flat | Beginning overfit | Watch closely |
| ↓ Decreasing | ↑ Increasing | Overfitting | Add regularization |
| → Flat | → Flat | Underfitting | More capacity |

### Dropout Best Practices Card

- **Typical rates:** 0.2 - 0.5
- **Placement:** After Dense layers
- **Where:** Hidden layers, not output layer
- **At inference:** Automatically disabled by Keras
- **Effect:** Reduces overfitting, may slightly reduce training accuracy

---

**Week 7 Complete! Ready for Week 8: Algorithm Selection Framework**

---

*Version: Week 7 Student Workbook v1.0 | February 2026*
