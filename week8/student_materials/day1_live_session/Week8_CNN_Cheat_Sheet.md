# Week 8 CNN Cheat Sheet

Quick reference. Print or keep on a second screen during the post-class exercise.

---

## Setup boilerplate

```python
import os
os.environ['KERAS_BACKEND'] = 'torch'

import keras
from keras import layers
import numpy as np
import matplotlib.pyplot as plt

keras.utils.set_random_seed(42)
```

---

## Loading datasets

```python
# Fashion-MNIST: grayscale, 28×28, 10 classes
(X_train, y_train), (X_test, y_test) = keras.datasets.fashion_mnist.load_data()

# CIFAR-10: RGB, 32×32, 10 classes (note: needs flatten on labels)
(X_train, y_train), (X_test, y_test) = keras.datasets.cifar10.load_data()
y_train = y_train.flatten(); y_test = y_test.flatten()

# MNIST: grayscale, 28×28, 10 classes (handwritten digits)
(X_train, y_train), (X_test, y_test) = keras.datasets.mnist.load_data()
```

---

## Preprocessing

```python
# Normalize pixel values to [0, 1]
X_train = X_train.astype('float32') / 255.0
X_test = X_test.astype('float32') / 255.0

# Add channel dimension (only needed for grayscale; RGB already has it)
X_train = np.expand_dims(X_train, axis=-1)  # (N, H, W) -> (N, H, W, 1)
X_test = np.expand_dims(X_test, axis=-1)
```

---

## Common CNN architecture patterns

### Small CNN (Fashion-MNIST style, ~111K params)
```python
model = keras.Sequential([
    layers.Input(shape=(28, 28, 1)),
    layers.Conv2D(32, 3, activation='relu', padding='same'),
    layers.MaxPooling2D(2),
    layers.Conv2D(32, 3, activation='relu', padding='same'),
    layers.MaxPooling2D(2),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(10, activation='softmax')
])
```

### Medium CNN (CIFAR-10 style, VGG-inspired)
```python
model = keras.Sequential([
    layers.Input(shape=(32, 32, 3)),
    layers.Conv2D(32, 3, activation='relu', padding='same'),
    layers.Conv2D(32, 3, activation='relu', padding='same'),
    layers.MaxPooling2D(2),
    layers.Conv2D(64, 3, activation='relu', padding='same'),
    layers.Conv2D(64, 3, activation='relu', padding='same'),
    layers.MaxPooling2D(2),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(10, activation='softmax')
])
```

### Modern CNN with GAP (no big Dense)
```python
model = keras.Sequential([
    layers.Input(shape=(32, 32, 3)),
    layers.Conv2D(32, 3, activation='relu', padding='same'),
    layers.MaxPooling2D(2),
    layers.Conv2D(64, 3, activation='relu', padding='same'),
    layers.MaxPooling2D(2),
    layers.Conv2D(128, 3, activation='relu', padding='same'),
    layers.GlobalAveragePooling2D(),  # No flatten + dense
    layers.Dense(10, activation='softmax')
])
```

---

## Compile + train (same pattern as Week 7)

```python
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

callbacks = [
    keras.callbacks.EarlyStopping(
        monitor='val_loss', patience=4, restore_best_weights=True
    )
]

history = model.fit(
    X_train, y_train,
    epochs=20,
    batch_size=128,
    validation_split=0.1,
    callbacks=callbacks,
    verbose=2
)

test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
print(f'Test accuracy: {test_acc:.4f}')
```

---

## Save + load (same as Week 7)

```python
model.save('my_cnn.keras')
loaded = keras.models.load_model('my_cnn.keras')
```

---

## Visualization recipes

### Plot first-layer filters
```python
filters, biases = model.layers[0].get_weights()
filters = (filters - filters.min()) / (filters.max() - filters.min())

n_filters = filters.shape[-1]
fig, axes = plt.subplots(4, 8, figsize=(12, 6))
for i, ax in enumerate(axes.flat):
    if i < n_filters:
        ax.imshow(filters[:, :, 0, i], cmap='gray')
    ax.axis('off')
plt.show()
```

### Plot feature maps for an image
```python
feature_extractor = keras.Model(
    inputs=model.inputs,
    outputs=model.layers[N].output  # Pick layer index N
)
feature_maps = feature_extractor.predict(image[np.newaxis, ...])

fig, axes = plt.subplots(4, 8, figsize=(12, 6))
for i, ax in enumerate(axes.flat):
    if i < feature_maps.shape[-1]:
        ax.imshow(feature_maps[0, :, :, i], cmap='viridis')
    ax.axis('off')
plt.show()
```

### Plot training curves
```python
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].plot(history.history['accuracy'], label='train')
axes[0].plot(history.history['val_accuracy'], label='val')
axes[0].legend(); axes[0].set_title('Accuracy')
axes[1].plot(history.history['loss'], label='train')
axes[1].plot(history.history['val_loss'], label='val')
axes[1].legend(); axes[1].set_title('Loss')
plt.show()
```

### Inspect misclassifications
```python
predictions = model.predict(X_test, verbose=0)
predicted = np.argmax(predictions, axis=1)
wrong = np.where(predicted != y_test)[0]

fig, axes = plt.subplots(1, 8, figsize=(16, 2))
for i, ax in enumerate(axes):
    idx = wrong[i]
    ax.imshow(X_test[idx].squeeze(), cmap='gray' if X_test[idx].shape[-1]==1 else None)
    ax.set_title(f'P:{predicted[idx]} A:{y_test[idx]}', fontsize=8)
    ax.axis('off')
plt.show()
```

---

## Hyperparameter tuning quick reference

| Want to... | Change... | Effect |
|---|---|---|
| Increase capacity | Filter counts (32→64→128) | More patterns, more params |
| Go deeper | Add another Conv block | More abstract features |
| Reduce overfitting | Increase Dropout (0.3 → 0.5) | More regularization |
| Reduce overfitting | EarlyStopping patience smaller | Stop sooner |
| Speed training | Larger batch_size (128 → 256) | Faster epochs (if GPU memory allows) |
| Reduce learning rate | `Adam(learning_rate=1e-4)` | Slower but more stable |

---

## Common shape errors and fixes

| Error message includes | Likely cause | Fix |
|---|---|---|
| `expected min_ndim=4, found ndim=3` | Channel dim missing | `np.expand_dims(X, -1)` |
| `Shape mismatch in loss computation` | Sparse vs categorical | Use `sparse_categorical_crossentropy` with integer labels |
| `Negative dimension` | Too many `valid` pools | Use `padding='same'` |
| `Out of memory` | Batch too big | Reduce `batch_size` |

---

## Parameter count formulas

**Conv2D layer:**
```
params = (kernel_h × kernel_w × input_channels × num_filters) + num_filters
```
Example (our 2nd conv): Conv2D(32, 3) on 32-channel input = 3×3×32×32 + 32 = 9,248

**Dense layer:**
```
params = (input_size × output_size) + output_size
```
Example (our dense head): Dense(64) after Flatten on 7×7×32 = 1568×64 + 64 = 100,416

**MaxPooling2D / Flatten / Dropout / GlobalAveragePooling2D:**
Zero parameters (no learnable weights).

---

## What's next: Week 9

You'll learn to use a model someone else trained — `keras.applications.MobileNetV2` and friends — and adapt it to your data. The conv block pattern stays; you'll just be using SOMEONE ELSE's pretrained conv blocks as the foundation.

```python
# Sneak peek of Week 9
base_model = keras.applications.MobileNetV2(
    input_shape=(224, 224, 3),
    include_top=False,
    weights='imagenet'
)
base_model.trainable = False  # Freeze
# ... add custom head and train
```

---

**Version:** Week 8 Cheat Sheet v1.0 | April 2026
