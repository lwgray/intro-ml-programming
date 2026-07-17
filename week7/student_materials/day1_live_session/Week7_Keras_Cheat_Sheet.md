# Week 7 Keras Cheat Sheet

**Quick Reference for Deep Learning Best Practices**

---

## Building Models with Regularization

### Basic Sequential Model
```python
import keras
from keras import layers

model = keras.Sequential([
    layers.Input(shape=(784,)),  # Flattened Fashion-MNIST
    layers.Dense(128, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])
```

### Model with Dropout
```python
model = keras.Sequential([
    layers.Input(shape=(784,)),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.3),  # Drop 30% of neurons
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(10, activation='softmax')
])
```

**Dropout Guidelines:**
- Typical rates: 0.2 - 0.5
- Place after Dense layers
- Higher rates = more regularization
- Don't use on output layer

---

## Compiling Models

```python
model.compile(
    optimizer='adam',  # Good default choice
    loss='sparse_categorical_crossentropy',  # For integer labels
    metrics=['accuracy']
)
```

**Loss Function Guide:**
- `sparse_categorical_crossentropy`: Labels are integers (0-9)
- `categorical_crossentropy`: Labels are one-hot encoded
- `binary_crossentropy`: Binary classification (2 classes)

---

## Training with Validation

### Basic Training
```python
history = model.fit(
    X_train, y_train,
    epochs=20,
    batch_size=32,
    validation_split=0.2  # Use 20% of training data for validation
)
```

### Training with Separate Validation Set
```python
history = model.fit(
    X_train, y_train,
    epochs=20,
    batch_size=32,
    validation_data=(X_val, y_val)  # Use specific validation set
)
```

---

## Callbacks

### EarlyStopping
```python
from keras.callbacks import EarlyStopping

early_stop = EarlyStopping(
    monitor='val_loss',           # Watch validation loss
    patience=3,                   # Wait 3 epochs before stopping
    restore_best_weights=True,    # Go back to best epoch
    verbose=1                     # Print when stopping
)

history = model.fit(
    X_train, y_train,
    epochs=50,
    validation_data=(X_val, y_val),
    callbacks=[early_stop]
)
```

**EarlyStopping Parameters:**
- `monitor`: Metric to watch ('val_loss', 'val_accuracy')
- `patience`: Epochs to wait without improvement
- `restore_best_weights`: True = use best, False = use last
- `min_delta`: Minimum change to count as improvement (default: 0)
- `mode`: 'min' (loss) or 'max' (accuracy), 'auto' detects

### ModelCheckpoint
```python
from keras.callbacks import ModelCheckpoint

checkpoint = ModelCheckpoint(
    filepath='best_model.keras',
    monitor='val_accuracy',
    save_best_only=True,
    mode='max',
    verbose=1
)

history = model.fit(
    X_train, y_train,
    epochs=50,
    validation_data=(X_val, y_val),
    callbacks=[checkpoint]
)
```

### Using Multiple Callbacks
```python
callbacks_list = [early_stop, checkpoint]

history = model.fit(
    X_train, y_train,
    epochs=50,
    validation_data=(X_val, y_val),
    callbacks=callbacks_list
)
```

---

## Model Saving and Loading

### Save Complete Model
```python
# Saves architecture + weights + optimizer state
model.save('my_model.keras')
```

### Load Complete Model
```python
from keras.models import load_model

loaded_model = load_model('my_model.keras')

# Ready to use immediately
predictions = loaded_model.predict(X_test)
```

### Save Only Weights
```python
# Saves just the weights, not architecture
model.save_weights('weights.h5')

# To load: need to build model first, then load weights
model.load_weights('weights.h5')
```

**Recommendation:** Use `model.save()` for complete persistence.

---

## Plotting Training History

### Basic Loss Plot
```python
import matplotlib.pyplot as plt

plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.title('Training History')
plt.show()
```

### Loss and Accuracy Subplots
```python
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 4))

# Loss subplot
plt.subplot(1, 2, 1)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.title('Loss Over Time')

# Accuracy subplot
plt.subplot(1, 2, 2)
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.title('Accuracy Over Time')

plt.tight_layout()
plt.show()
```

---

## Evaluation and Prediction

### Evaluate on Test Set
```python
test_loss, test_accuracy = model.evaluate(X_test, y_test)
print(f"Test accuracy: {test_accuracy:.4f}")
```

### Make Predictions
```python
predictions = model.predict(X_test)
# Returns probabilities for each class

# Get predicted class
predicted_classes = predictions.argmax(axis=1)
```

### Single Prediction
```python
import numpy as np

# Add batch dimension
single_image = np.expand_dims(X_test[0], axis=0)
prediction = model.predict(single_image)
predicted_class = prediction.argmax()
```

---

## Data Preprocessing

### Fashion-MNIST Loading
```python
from keras.datasets import fashion_mnist

(X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()
```

### Normalization
```python
# Normalize pixel values (0-255 → 0-1)
X_train = X_train / 255.0
X_test = X_test / 255.0
```

### Flattening for Dense Networks
```python
# Fashion-MNIST: 28×28 images
X_train = X_train.reshape(-1, 784)  # 28*28 = 784
X_test = X_test.reshape(-1, 784)
```

### Three-Way Split
```python
from sklearn.model_selection import train_test_split

# Split training data into train + validation
X_train, X_val, y_train, y_val = train_test_split(
    X_train, y_train,
    test_size=0.2,  # 20% for validation
    random_state=42
)

# Result:
# X_train, y_train: 48,000 samples (training)
# X_val, y_val: 12,000 samples (validation monitoring)
# X_test, y_test: 10,000 samples (final evaluation)
```

---

## Common Patterns

### Complete Fashion-MNIST Pipeline
```python
from keras.datasets import fashion_mnist
from keras import layers, models
from keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Load and preprocess
(X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()
X_train = X_train / 255.0
X_test = X_test / 255.0
X_train = X_train.reshape(-1, 784)
X_test = X_test.reshape(-1, 784)

# Three-way split
X_train, X_val, y_train, y_val = train_test_split(
    X_train, y_train, test_size=0.2, random_state=42
)

# Build model
model = keras.Sequential([
    layers.Input(shape=(784,)),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(10, activation='softmax')
])

# Compile
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Configure callback
early_stop = EarlyStopping(
    monitor='val_loss',
    patience=3,
    restore_best_weights=True
)

# Train
history = model.fit(
    X_train, y_train,
    epochs=50,
    batch_size=32,
    validation_data=(X_val, y_val),
    callbacks=[early_stop],
    verbose=1
)

# Plot results
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(history.history['loss'], label='Training')
plt.plot(history.history['val_loss'], label='Validation')
plt.legend()
plt.title('Loss')

plt.subplot(1, 2, 2)
plt.plot(history.history['accuracy'], label='Training')
plt.plot(history.history['val_accuracy'], label='Validation')
plt.legend()
plt.title('Accuracy')
plt.show()

# Evaluate
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f"Test accuracy: {test_acc:.4f}")

# Save
model.save('fashion_mnist_model.keras')
```

---

## Troubleshooting

### Problem: Model not improving
**Solutions:**
- Check learning rate (try 'adam' optimizer with default lr)
- Verify data is normalized (0-1 range)
- Ensure correct loss function
- Check if model has enough capacity

### Problem: Overfitting (validation worse than training)
**Solutions:**
- Add Dropout layers
- Use EarlyStopping callback
- Reduce model size
- Get more training data

### Problem: Underfitting (both train and val low)
**Solutions:**
- Increase model capacity (more neurons/layers)
- Train for more epochs
- Reduce regularization (lower dropout rate)
- Check data quality

### Problem: EarlyStopping doesn't work
**Solutions:**
- Did you provide `validation_data` argument?
- Check `monitor` parameter (should be 'val_loss' or 'val_accuracy')
- Increase `patience` if stopping too early
- Set `restore_best_weights=True`

### Problem: Model saved but won't load
**Solutions:**
- Use `.keras` extension (not `.h5`)
- Import: `from keras.models import load_model`
- Check file path is correct
- Ensure same Keras version

---

## Quick Checklist for Week 7

**Before Training:**
- [ ] Data normalized (0-1 range)
- [ ] Data split into train/val/test
- [ ] Model architecture includes Dropout
- [ ] EarlyStopping callback configured
- [ ] `validation_data` provided to model.fit()

**During Training:**
- [ ] Monitor both training and validation metrics
- [ ] Watch for overfitting patterns in curves
- [ ] Note when EarlyStopping triggers

**After Training:**
- [ ] Plot training history
- [ ] Evaluate on test set (once only!)
- [ ] Save model if performance is good
- [ ] Document parameters used

---

## Keras Version Note

**Week 7 uses Keras 3.x**

Check your version:
```python
import keras
print(keras.__version__)  # Should be 3.x
```

**Backend:**
```python
print(keras.backend.backend())  # Should show 'tensorflow' or 'torch'
```

**Installation:**
```bash
pip install keras>=3.0
pip install tensorflow>=2.15  # Provides backend
```

---

## Fashion-MNIST Class Names

**Remember the 10 classes:**
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

---

## Additional Resources

**Keras Documentation:**
- Callbacks: https://keras.io/api/callbacks/
- Sequential API: https://keras.io/guides/sequential_model/
- Training & Evaluation: https://keras.io/guides/training_with_built_in_methods/

**Week 7 Course Materials:**
- Week7_Glossary.md (terminology)
- Week7_Student_Workbook.md (note-taking)
- Week7_Training_Curves_Interpretation_Guide.md (visual diagnosis)

---

*Version: Week 7 Keras Cheat Sheet v1.0 | February 2026*
