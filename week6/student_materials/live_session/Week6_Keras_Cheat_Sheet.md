# Week 6: Keras Quick Reference Cheat Sheet

**Keep this open while coding!**

---

## ⚡ The Essential Workflow

```python
# STEP 1: Setup (ALWAYS set backend FIRST!)
import os
os.environ['KERAS_BACKEND'] = 'torch'
import keras
from keras import layers

# STEP 2: Build model
model = keras.Sequential([
    layers.Dense(units, activation='relu'),
    layers.Dense(units, activation='softmax')
])

# STEP 3: Compile
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# STEP 4: Train
history = model.fit(X_train, y_train, epochs=10, validation_split=0.2)

# STEP 5: Evaluate
test_loss, test_acc = model.evaluate(X_test, y_test)

# STEP 6: Predict
predictions = model.predict(X_new)
```

---

## 🔧 Building Models

### Sequential API

```python
model = keras.Sequential([
    layers.Layer1(...),
    layers.Layer2(...),
    layers.Layer3(...)
])
```

### Common Layers

```python
# Flatten: 2D/3D → 1D
layers.Flatten(input_shape=(28, 28))

# Dense (fully connected)
layers.Dense(units=128, activation='relu')

# Dropout (Week 7)
layers.Dropout(rate=0.2)
```

### First Layer Only
```python
layers.Dense(128, activation='relu', input_shape=(num_features,))
# OR for images:
layers.Flatten(input_shape=(height, width))
```

---

## 🎯 Activation Functions

| Task | Hidden Layers | Output Layer |
|------|---------------|--------------|
| **Binary classification** | `'relu'` | `'sigmoid'` (1 neuron) |
| **Multi-class classification** | `'relu'` | `'softmax'` (N neurons) |
| **Regression** | `'relu'` | None or `'linear'` (1 neuron) |

**Code:**
```python
# Hidden layer
layers.Dense(64, activation='relu')

# Binary output
layers.Dense(1, activation='sigmoid')

# Multi-class output (10 classes)
layers.Dense(10, activation='softmax')
```

---

## 📉 Loss Functions

### Decision Tree

```
What's your task?
│
├─ Binary classification (0 or 1)
│  └─ loss='binary_crossentropy'
│
├─ Multi-class classification
│  ├─ Integer labels (0, 1, 2, ...)?
│  │  └─ loss='sparse_categorical_crossentropy' ⭐
│  └─ One-hot labels ([1,0,0], [0,1,0], ...)?
│     └─ loss='categorical_crossentropy'
│
└─ Regression (continuous values)
   └─ loss='mse' or loss='mae'
```

**Most common for Week 6:** `'sparse_categorical_crossentropy'` (MNIST uses integer labels)

---

## ⚙️ Optimizers

**Just use Adam:**
```python
optimizer='adam'
```

**Other options (rare for beginners):**
```python
optimizer='sgd'      # Simpler, requires tuning
optimizer='rmsprop'  # Good for RNNs
```

---

## 📊 Metrics

```python
metrics=['accuracy']  # Most common

# Multi-metric:
metrics=['accuracy', 'precision', 'recall']
```

**Note:** Metrics are for monitoring only (NOT used in optimization).

---

## 🏋️ Training Configuration

```python
history = model.fit(
    X_train, y_train,
    epochs=10,              # How many complete passes through data
    batch_size=32,          # Samples per batch (32, 64, or 128)
    validation_split=0.2,   # Use 20% for validation
    verbose=1               # 1=progress bar, 0=silent
)
```

### Common Patterns

**Quick training (development):**
```python
epochs=5, batch_size=128, validation_split=0.2
```

**Standard training:**
```python
epochs=10, batch_size=32, validation_split=0.2
```

**Longer training (better accuracy):**
```python
epochs=20, batch_size=32, validation_split=0.2
```

---

## 🔍 Model Inspection

```python
# Architecture summary
model.summary()

# Get configuration
model.get_config()

# Count parameters
model.count_params()
```

---

## 📈 Accessing Training History

```python
history = model.fit(...)

# Training metrics
history.history['loss']         # Training loss per epoch
history.history['accuracy']     # Training accuracy per epoch

# Validation metrics
history.history['val_loss']      # Validation loss per epoch
history.history['val_accuracy']  # Validation accuracy per epoch
```

### Plot Training Curves

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 4))

# Plot accuracy
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Train')
plt.plot(history.history['val_accuracy'], label='Val')
plt.title('Accuracy')
plt.legend()

# Plot loss
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Train')
plt.plot(history.history['val_loss'], label='Val')
plt.title('Loss')
plt.legend()

plt.show()
```

---

## 🎲 Making Predictions

```python
# Get predictions (probabilities)
predictions = model.predict(X_test)

# Binary classification
predicted_classes = (predictions > 0.5).astype(int)

# Multi-class classification
predicted_classes = np.argmax(predictions, axis=1)
```

---

## 📁 Saving and Loading

```python
# Save complete model
model.save('my_model.keras')

# Load model
loaded_model = keras.models.load_model('my_model.keras')
```

---

## 🧹 Data Preprocessing

### Normalization (CRITICAL!)

```python
# For images (0-255 → 0-1)
X_train = X_train / 255.0
X_test = X_test / 255.0

# Alternative (mean=0, std=1)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
```

### Train/Test Split

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

---

## 🏗️ Common Architectures

### MNIST Classifier
```python
model = keras.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(128, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])
```

### Binary Classifier
```python
model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(num_features,)),
    layers.Dense(32, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])
```

### Regression
```python
model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(num_features,)),
    layers.Dense(32, activation='relu'),
    layers.Dense(1)  # No activation for regression
])
```

---

## 🐛 Troubleshooting

### Issue: Low accuracy (~10% for MNIST)

**Likely cause:** Forgot to normalize!
```python
# FIX:
X_train = X_train / 255.0
X_test = X_test / 255.0
```

---

### Issue: "ValueError: No gradients provided"

**Likely cause:** Wrong loss function for label format

**FIX:**
```python
# Integer labels (0, 1, 2, ...)
model.compile(loss='sparse_categorical_crossentropy', ...)

# One-hot labels ([1,0,0], [0,1,0], ...)
model.compile(loss='categorical_crossentropy', ...)
```

---

### Issue: Training loss is NaN

**Likely causes:**
1. Didn't normalize inputs
2. Learning rate too high

**FIX:**
```python
# Normalize inputs
X = X / 255.0

# Use Adam (handles learning rate automatically)
model.compile(optimizer='adam', ...)
```

---

### Issue: Model overfitting (high train acc, low val acc)

**Solutions (Week 7):**
```python
# Add Dropout
layers.Dropout(0.2)

# Use early stopping (callback)
keras.callbacks.EarlyStopping(monitor='val_loss', patience=3)

# Reduce model complexity
# (fewer layers or neurons)
```

---

## ✅ Pre-Training Checklist

Before calling `model.fit()`, verify:

- [ ] Backend is set (`os.environ['KERAS_BACKEND'] = 'torch'`)
- [ ] Data is normalized (0-1 range for images)
- [ ] Model is built (`model = keras.Sequential([...])`)
- [ ] `model.summary()` looks correct
- [ ] Model is compiled
- [ ] Loss function matches label format
- [ ] Activation functions are correct (ReLU hidden, Softmax/Sigmoid output)

---

## 🎯 Decision Trees

### Choose Activation for Output Layer

```
What's your task?
│
├─ Binary classification (yes/no, 0/1)
│  └─ activation='sigmoid', units=1
│
├─ Multi-class classification (3+ classes)
│  └─ activation='softmax', units=num_classes
│
└─ Regression (predict number)
   └─ activation=None or 'linear', units=1
```

---

### Choose Loss Function

```
What kind of labels do you have?
│
├─ Binary (0 or 1)
│  └─ loss='binary_crossentropy'
│
├─ Multi-class
│  ├─ Integers? (0, 1, 2, 3, ...)
│  │  └─ loss='sparse_categorical_crossentropy'
│  │
│  └─ One-hot? ([1,0,0], [0,1,0], [0,0,1], ...)
│     └─ loss='categorical_crossentropy'
│
└─ Continuous? (1.5, 2.7, 100.3, ...)
   └─ loss='mse' or 'mae'
```

---

## 💡 Quick Tips

**When building models:**
- Start simple (1-2 hidden layers, ~64-128 neurons)
- Always use `model.summary()` to verify
- ReLU for hidden layers (default choice)
- Adam for optimizer (default choice)

**When training:**
- Start with 10 epochs, increase if needed
- Use validation_split=0.2 to monitor overfitting
- Plot training curves after training

**When stuck:**
1. Did you normalize? (X / 255.0)
2. Did you set backend before importing keras?
3. Does loss match label format?
4. Did you call model.compile()?

---

## 📚 Most Common Patterns

### Complete MNIST Pipeline

```python
import os
os.environ['KERAS_BACKEND'] = 'torch'
import keras
from keras import layers

# Load data
(X_train, y_train), (X_test, y_test) = keras.datasets.mnist.load_data()

# Normalize
X_train = X_train / 255.0
X_test = X_test / 255.0

# Build
model = keras.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(128, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# Compile
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Train
history = model.fit(
    X_train, y_train,
    epochs=10,
    validation_split=0.2,
    verbose=1
)

# Evaluate
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f"Test accuracy: {test_acc:.4f}")
```

---

## 🚀 Next Steps (Week 7)

**You'll learn:**
- Dropout (regularization)
- Early stopping (callbacks)
- Model saving/loading
- Data augmentation
- Fashion-MNIST dataset

---

*Print this and keep it handy while coding!*

*Last Updated: 2026-02-02*
