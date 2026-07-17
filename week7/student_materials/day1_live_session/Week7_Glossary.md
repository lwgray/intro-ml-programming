# Week 7 Glossary - Deep Learning Best Practices

**Quick reference for key terms in Week 7**

---

## Core Concepts

### Overfitting
**Definition:** When a model memorizes the training data instead of learning general patterns, resulting in poor performance on new data.

**Symptoms:**
- Training accuracy high (95%+)
- Validation accuracy much lower (85%)
- Large gap between training and validation performance

**Example:** Student who memorizes exact practice problems but can't solve variations.

**Code indicator:**
```python
# Training curves show:
# - Training loss: ↓ decreasing
# - Validation loss: ↑ increasing
```

---

### Underfitting
**Definition:** When a model is too simple to capture patterns in the data, resulting in poor performance on both training and validation sets.

**Symptoms:**
- Training accuracy low
- Validation accuracy also low
- Both metrics plateau early

**Solution:** Increase model capacity (more layers/neurons) or train longer.

---

### Generalization
**Definition:** A model's ability to perform well on data it hasn't seen during training.

**Good generalization:** Small gap between training and validation accuracy
**Poor generalization:** Large gap (overfitting)

---

## Data Splitting

### Training Set
**Definition:** Data used to update model weights during training.

**Size:** Typically 60-80% of total data
**Week 7:** 48,000 samples (60% of 60,000 after test set removed)

**Used in:**
```python
model.fit(X_train, y_train, ...)  # First two arguments
```

---

### Validation Set
**Definition:** Data used to monitor model performance during training WITHOUT updating weights.

**Purpose:** Detect overfitting while training is happening
**Size:** Typically 10-20% of total data
**Week 7:** 12,000 samples (20% of 60,000)

**Used in:**
```python
model.fit(X_train, y_train,
          validation_data=(X_val, y_val),  # Monitor here
          ...)
```

**Analogy:** Practice test you take while studying to check progress

---

### Test Set
**Definition:** Data held out until final evaluation, used only once.

**Purpose:** Unbiased estimate of model performance
**Size:** Typically 10-20% of total data
**Week 7:** 10,000 samples (provided by Fashion-MNIST)

**Used in:**
```python
model.evaluate(X_test, y_test)  # Only after all training complete!
```

**Analogy:** Final exam - you only take it once

---

### Three-Way Split
**Definition:** Splitting data into train, validation, and test sets.

**Code:**
```python
from sklearn.model_selection import train_test_split

# Split train into train + validation
X_train, X_val, y_train, y_val = train_test_split(
    X_train_full, y_train_full, test_size=0.2, random_state=42
)
```

**Remember:** Train = update weights, Validation = monitor, Test = final eval

---

## Regularization Techniques

### Regularization
**Definition:** Techniques to prevent overfitting by constraining model complexity.

**Common methods:**
- Dropout
- Early Stopping
- L2 regularization (weight decay)
- Data augmentation

---

### Dropout
**Definition:** Regularization technique that randomly sets a fraction of neurons to zero during each training step.

**How it works:** If dropout rate = 0.3, randomly drop 30% of neurons each batch

**Why it helps:** Prevents network from relying on specific neurons, forces learning of robust features

**Placement:**
```python
Dense(256, activation='relu')
Dropout(0.3)  # After Dense, before next layer
Dense(128, activation='relu')
Dropout(0.3)
Dense(10, activation='softmax')  # NO Dropout after output!
```

**Typical rates:**
- 0.2 = light regularization
- 0.3 = good default
- 0.5 = heavy regularization

**Auto-disabled:** Dropout is automatically turned off during prediction (model.predict())

**Metaphor:** "Network on a Diet" - training with random neurons missing each practice

---

### Dropout Rate
**Definition:** Fraction of neurons to randomly drop during training.

**Example:** dropout_rate=0.3 means drop 30% of neurons

**Code:**
```python
layers.Dropout(0.3)  # 30% dropout rate
```

---

## Callbacks

### Callback
**Definition:** Object that performs actions at specific points during training.

**Common callbacks:**
- EarlyStopping: Stop training when metric stops improving
- ModelCheckpoint: Save model at intervals
- ReduceLROnPlateau: Reduce learning rate when metric plateaus

**Usage:**
```python
history = model.fit(
    X_train, y_train,
    callbacks=[early_stop, checkpoint]  # Pass as list
)
```

---

### EarlyStopping
**Definition:** Callback that stops training when monitored metric stops improving.

**Purpose:** Prevent overfitting by not training too long

**Key parameters:**
- `monitor`: What metric to watch ('val_loss', 'val_accuracy')
- `patience`: How many epochs to wait before stopping
- `restore_best_weights`: Whether to revert to best epoch

**Code:**
```python
from keras.callbacks import EarlyStopping

early_stop = EarlyStopping(
    monitor='val_loss',
    patience=3,
    restore_best_weights=True
)
```

**Metaphor:** "Validation Alarm" - smoke detector for overfitting

---

### Patience
**Definition:** Number of epochs to wait before stopping if no improvement.

**Example:** patience=3 means wait 3 epochs of no improvement before stopping

**How it works:**
- Epoch 10: val_loss=0.50 (best)
- Epoch 11: val_loss=0.52 (worse, patience counter=1)
- Epoch 12: val_loss=0.51 (worse, patience counter=2)
- Epoch 13: val_loss=0.53 (worse, patience counter=3 → STOP!)

**Typical values:** 3-5 (start with 3)

---

### restore_best_weights
**Definition:** EarlyStopping parameter that reverts model weights to the best epoch when stopping.

**Why critical:** Without this, you keep weights from the last epoch (possibly overfitted), not the best epoch

**Always set to True:**
```python
early_stop = EarlyStopping(
    monitor='val_loss',
    patience=3,
    restore_best_weights=True  # ALWAYS True!
)
```

---

### ModelCheckpoint
**Definition:** Callback that saves model to disk during training.

**Purpose:** Save best model automatically, survive crashes

**Key parameters:**
- `filepath`: Where to save model
- `monitor`: What metric to watch
- `save_best_only`: Only save when metric improves
- `mode`: 'min' (minimize metric) or 'max' (maximize)

**Code:**
```python
from keras.callbacks import ModelCheckpoint

checkpoint = ModelCheckpoint(
    filepath='best_model.keras',
    monitor='val_accuracy',
    save_best_only=True,
    mode='max',  # Maximize accuracy
    verbose=1
)
```

---

## Model Persistence

### Model Persistence
**Definition:** Saving trained model to disk for later use.

**Why important:** Deploy model, share with others, resume training

---

### model.save()
**Definition:** Method to save complete model (architecture + weights + optimizer) to disk.

**File format:** .keras (Keras 3.x native format)

**Code:**
```python
model.save('my_model.keras')  # Saves everything
```

**What's saved:**
- Model architecture (layers, connections)
- Trained weights
- Optimizer state
- Compilation configuration

---

### load_model()
**Definition:** Function to load a saved model from disk.

**Code:**
```python
from keras.models import load_model

loaded_model = load_model('my_model.keras')

# Ready to use immediately!
predictions = loaded_model.predict(X_test)
```

**No recompilation needed** - model is ready to use

---

### model.save_weights()
**Definition:** Save only the weights (not architecture).

**When to use:** When you want to save just trained parameters, not full model

**Limitation:** Must rebuild architecture before loading weights

**Code:**
```python
# Save weights only
model.save_weights('weights.h5')

# Load (must rebuild architecture first!)
model = build_model()  # Rebuild same architecture
model.load_weights('weights.h5')
```

**Recommendation:** Use `model.save()` instead (saves everything)

---

## Training Concepts

### Training Curves
**Definition:** Plots showing how loss and accuracy change over epochs.

**What to plot:**
- Training loss vs epochs
- Validation loss vs epochs
- Training accuracy vs epochs
- Validation accuracy vs epochs

**Code:**
```python
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
```

**Used for:** Diagnosing overfitting, underfitting, or healthy training

**Metaphor:** "Overfitting Detective" - curves are clues

---

### Training Curve Patterns

**Pattern 1: Healthy**
- Train loss: ↓ decreasing
- Val loss: ↓ decreasing
- Action: Continue training

**Pattern 2: Beginning Overfit**
- Train loss: ↓ decreasing
- Val loss: → flat
- Action: Consider stopping soon

**Pattern 3: Overfitting**
- Train loss: ↓ decreasing
- Val loss: ↑ increasing
- Action: Stop; add regularization

**Pattern 4: Underfitting**
- Train loss: → flat
- Val loss: → flat
- Action: More capacity or more epochs

---

### Epoch
**Definition:** One complete pass through the entire training dataset.

**Example:** If you have 48,000 training samples and batch_size=128:
- 48,000 / 128 = 375 batches per epoch
- Training for 10 epochs = 3,750 total batches

---

### Batch Size
**Definition:** Number of samples processed before updating model weights.

**Common values:** 32, 64, 128, 256

**Trade-offs:**
- Smaller (32): More frequent updates, slower but potentially better
- Larger (256): Fewer updates, faster but potentially less stable

**Week 7 default:** 128

---

## Dataset

### Fashion-MNIST
**Definition:** Dataset of 70,000 grayscale images of clothing items.

**Structure:**
- Training: 60,000 images
- Test: 10,000 images
- Image size: 28×28 pixels
- Classes: 10

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

**Why use it:** Slightly harder than MNIST → overfitting more likely → better for teaching regularization

**Loading:**
```python
from keras.datasets import fashion_mnist
(X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()
```

---

## Quick Reference Table

| Term | One-Line Definition |
|------|-------------------|
| **Overfitting** | Model memorizes training data, fails on new data |
| **Validation set** | Data to monitor overfitting during training |
| **Test set** | Data for final evaluation only |
| **Dropout** | Randomly drop neurons during training |
| **Dropout rate** | Fraction of neurons to drop (e.g., 0.3 = 30%) |
| **Callback** | Function that runs at specific training points |
| **EarlyStopping** | Stop training when val metric stops improving |
| **Patience** | Epochs to wait before EarlyStopping triggers |
| **restore_best_weights** | Revert to best epoch when stopping |
| **ModelCheckpoint** | Save model to disk during training |
| **model.save()** | Save complete model to file |
| **load_model()** | Load saved model from file |
| **Training curves** | Plots of loss/accuracy over epochs |
| **Fashion-MNIST** | 70k clothing images dataset |

---

## Common Confusions - Clarified

**"Do I turn off Dropout during prediction?"**
→ No! Keras does this automatically.

**"Why is validation loss higher from epoch 1?"**
→ Normal with Dropout. During training, neurons are dropped (artificial handicap). During validation, all neurons active.

**"What if training stops at epoch 10 when I set epochs=50?"**
→ That's EarlyStopping working! It stopped early because validation stopped improving.

**"Do I use training, validation, or test set for model.evaluate()?"**
→ Test set, and only once at the very end. Validation set is used during training via `validation_data`.

**"Where does Dropout go?"**
→ After Dense layers, before the next layer. NEVER after the output layer.

**"What's restore_best_weights?"**
→ Parameter that reverts weights to the best epoch (not last epoch) when EarlyStopping triggers. Always set to True!

---

**Version:** Week 7 Glossary v1.0 | February 2026
