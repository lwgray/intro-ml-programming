# Appendix F: Keras Sequential API Complete Reference Guide

**A standalone guide to building neural networks with Keras**

---

## Table of Contents

1. [Introduction to Keras](#introduction-to-keras)
2. [The Sequential API Workflow](#the-sequential-api-workflow)
3. [Building Models Step-by-Step](#building-models-step-by-step)
4. [Layer Types](#layer-types)
5. [Activation Functions](#activation-functions)
6. [Loss Functions](#loss-functions)
7. [Optimizers](#optimizers)
8. [Compiling Models](#compiling-models)
9. [Training Models (model.fit)](#training-models-modelfit)
10. [Evaluating Models](#evaluating-models)
11. [Making Predictions](#making-predictions)
12. [Model Summary](#model-summary)
13. [Saving and Loading Models](#saving-and-loading-models)
14. [Troubleshooting Common Errors](#troubleshooting-common-errors)
15. [Complete Example](#complete-example)

---

## Introduction to Keras

### What is Keras?

**Keras** is a high-level neural network API that makes building, training, and deploying deep learning models simple and intuitive.

**Key features:**
- **User-friendly:** Designed for humans, not machines
- **Modular:** Build models like LEGO blocks
- **Flexible:** Works with TensorFlow, PyTorch backends
- **Production-ready:** Deploy models easily

**Keras 3.0** (current version) supports multiple backends:
- TensorFlow (default)
- PyTorch
- JAX

### Why Sequential API?

The **Sequential API** is the simplest way to build neural networks in Keras.

**Use Sequential when:**
- Layers stack in a linear sequence (input → hidden → output)
- Each layer has one input tensor and one output tensor
- No branching or complex connections needed

**Examples of Sequential-appropriate problems:**
- MNIST digit classification
- Fashion-MNIST clothing classification
- Binary classification (spam detection)
- Regression (house price prediction)

**Don't use Sequential when:**
- You need multiple inputs or outputs
- You need skip connections (like ResNet)
- You need shared layers
→ Use **Functional API** instead

---

## The Sequential API Workflow

**Standard workflow for every neural network project:**

```
1. LOAD DATA
   ↓
2. PREPROCESS
   - Normalize/standardize
   - Train/validation/test split
   ↓
3. BUILD MODEL
   - Create Sequential()
   - Add layers with activations
   ↓
4. COMPILE
   - Choose optimizer
   - Choose loss function
   - Choose metrics
   ↓
5. TRAIN (FIT)
   - model.fit() with training data
   - Monitor validation performance
   ↓
6. EVALUATE
   - model.evaluate() on test set
   - Final performance metrics
   ↓
7. PREDICT
   - model.predict() on new data
   - Inference/deployment
```

**Key rule: Build → Compile → Fit (in that order!)**

---

## Building Models Step-by-Step

### Method 1: Sequential with List

**Most common approach: Pass list of layers to Sequential()**

```python
import keras
from keras import layers

model = keras.Sequential([
    layers.Flatten(input_shape=(28, 28)),      # Input layer
    layers.Dense(128, activation='relu'),      # Hidden layer 1
    layers.Dense(64, activation='relu'),       # Hidden layer 2
    layers.Dense(10, activation='softmax')     # Output layer
])
```

**Advantages:**
- Concise and readable
- All layers defined in one place
- Easy to see architecture at a glance

---

### Method 2: Sequential with .add()

**Alternative: Create empty Sequential, then add layers**

```python
model = keras.Sequential()
model.add(layers.Flatten(input_shape=(28, 28)))
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))
```

**Advantages:**
- Flexible (can add layers conditionally)
- Clear separation of each layer

**Use when:**
- Building models programmatically
- Adding layers based on hyperparameters

---

### Method 3: Named Layers

**Optional: Name layers for easier debugging**

```python
model = keras.Sequential([
    layers.Flatten(input_shape=(28, 28), name='flatten_input'),
    layers.Dense(128, activation='relu', name='hidden_1'),
    layers.Dense(64, activation='relu', name='hidden_2'),
    layers.Dense(10, activation='softmax', name='output')
], name='mnist_classifier')
```

**Advantages:**
- Easier to debug (error messages reference layer names)
- Clearer model.summary() output
- Helps when visualizing model

---

## Layer Types

### Dense Layer (Fully Connected)

**Most common layer type: every neuron connects to all neurons in previous layer**

```python
layers.Dense(units, activation=None, use_bias=True, name=None)
```

**Parameters:**
- `units` (int): Number of neurons in this layer
- `activation` (str or function): Activation function ('relu', 'sigmoid', 'softmax', etc.)
- `use_bias` (bool): Whether to include bias term (default: True)
- `name` (str): Layer name (optional)

**Example:**
```python
layers.Dense(128, activation='relu')
```
- Creates 128 neurons
- Each neuron connected to all inputs from previous layer
- ReLU activation applied to each neuron's output

**Parameter count:**
```
parameters = (inputs × units) + units
           = weights      + biases

Example: 784 inputs → 128 Dense
parameters = (784 × 128) + 128 = 100,480
```

---

### Flatten Layer

**Converts multi-dimensional input to 1D vector**

```python
layers.Flatten(input_shape=None)
```

**Use case: Convert 2D images to 1D for Dense layers**

```python
layers.Flatten(input_shape=(28, 28))
# Converts 28×28 = 784 values
```

**Why needed:**
- Dense layers expect 1D input
- Images are 2D (height × width) or 3D (height × width × channels)
- Flatten reshapes without changing values

**Example:**
```
Input:  [[1, 2, 3],
         [4, 5, 6]]     Shape: (2, 3)

After Flatten: [1, 2, 3, 4, 5, 6]     Shape: (6,)
```

---

### Dropout Layer (Regularization)

**Randomly sets fraction of inputs to 0 during training to prevent overfitting**

```python
layers.Dropout(rate)
```

**Parameters:**
- `rate` (float): Fraction of inputs to drop (0.0 to 1.0)

**Example:**
```python
model = keras.Sequential([
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.5),              # Drop 50% of neurons randomly
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.3),              # Drop 30% of neurons
    layers.Dense(10, activation='softmax')
])
```

**How it works:**
- During training: Randomly sets 50% of neuron outputs to 0
- During inference: All neurons active (dropout disabled)
- Forces network to learn redundant representations

**When to use:**
- Model is overfitting (training accuracy >> validation accuracy)
- Typical rates: 0.2 to 0.5

---

### Input Layer (Explicit)

**Optional: Explicitly define input shape**

```python
layers.Input(shape)
```

**Usually not needed for Sequential** (first layer's `input_shape` suffices)

**Example:**
```python
# These are equivalent:

# Method 1 (common)
model = keras.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    ...
])

# Method 2 (explicit)
model = keras.Sequential([
    layers.Input(shape=(28, 28)),
    layers.Flatten(),
    ...
])
```

---

## Activation Functions

### Overview

**Activation functions introduce non-linearity, allowing networks to learn complex patterns**

**Without activations:**
```
f(g(h(x))) where f, g, h are linear → still linear!
Deep network = useless (equivalent to single layer)
```

**With activations:**
```
f(g(h(x))) where f, g, h are non-linear → complex function!
Deep network can approximate any function
```

---

### ReLU (Rectified Linear Unit)

**Formula:** `f(x) = max(0, x)`

**Behavior:**
- x < 0 → output = 0
- x ≥ 0 → output = x

**Use:** Hidden layers (default choice)

**Advantages:**
- Simple and fast
- No vanishing gradient problem
- Works well in practice

**Code:**
```python
layers.Dense(128, activation='relu')
```

**Example:**
```
Input:  [-2, -1, 0, 1, 2]
Output: [ 0,  0, 0, 1, 2]
```

---

### Sigmoid

**Formula:** `f(x) = 1 / (1 + e^(-x))`

**Behavior:**
- Squashes any input to (0, 1) range
- S-shaped curve

**Use:** Binary classification output layer

**Advantages:**
- Outputs interpretable as probabilities
- Smooth gradient

**Disadvantages:**
- Vanishing gradient in deep networks
- Not zero-centered

**Code:**
```python
layers.Dense(1, activation='sigmoid')  # Binary classification
```

**Example:**
```
Input:  [-5, -1, 0, 1, 5]
Output: [0.007, 0.27, 0.5, 0.73, 0.993]
```

---

### Softmax

**Formula:** `softmax(x_i) = e^(x_i) / Σ e^(x_j)`

**Behavior:**
- Converts raw scores (logits) to probabilities
- All outputs sum to 1.0

**Use:** Multi-class classification output layer

**Advantages:**
- Outputs valid probability distribution
- Differentiable (can backpropagate)

**Code:**
```python
layers.Dense(10, activation='softmax')  # 10-class classification
```

**Example:**
```
Input (logits):  [2.0, 1.0, 0.1]
Output (probs):  [0.66, 0.24, 0.10]  # Sum = 1.0
                  ↑ Highest → predicted class
```

---

### Tanh (Hyperbolic Tangent)

**Formula:** `f(x) = (e^x - e^(-x)) / (e^x + e^(-x))`

**Behavior:**
- Squashes input to (-1, 1) range
- S-shaped curve (like sigmoid, but zero-centered)

**Use:** Hidden layers (less common than ReLU)

**Code:**
```python
layers.Dense(64, activation='tanh')
```

**When to use:**
- ReLU isn't working well
- Need zero-centered activations

---

### Linear (No Activation)

**Formula:** `f(x) = x`

**Behavior:** Pass-through (no transformation)

**Use:** Regression output layer

**Code:**
```python
layers.Dense(1)  # No activation specified = linear
# or explicitly:
layers.Dense(1, activation='linear')
```

**Example:**
```python
# Predicting house prices (continuous output)
model = keras.Sequential([
    layers.Dense(64, activation='relu'),
    layers.Dense(32, activation='relu'),
    layers.Dense(1)  # Linear output for regression
])
```

---

### Activation Function Selection Guide

| Problem Type | Output Layer Activation | Loss Function |
|--------------|------------------------|---------------|
| **Binary classification** | sigmoid | binary_crossentropy |
| **Multi-class (one label)** | softmax | sparse_categorical_crossentropy |
| **Multi-label** | sigmoid | binary_crossentropy |
| **Regression** | linear (none) | mse or mae |

**Hidden layers:** Almost always use ReLU (default choice)

---

## Loss Functions

### What is a Loss Function?

**Loss** measures how wrong the model's predictions are.

**Training goal:** Minimize loss by adjusting weights

**Key distinction:**
- **Loss:** What the model optimizes (continuous, differentiable)
- **Metrics (accuracy):** What humans interpret (discrete, intuitive)

---

### Sparse Categorical Crossentropy

**Use for:** Multi-class classification with integer labels

**Formula:** `-log(p_true_class)`

**Example:**
```
True label: 3
Predictions: [0.01, 0.02, 0.05, 0.89, 0.03]
                                    ↑ p(class 3)
Loss = -log(0.89) = 0.12  (low loss = good!)

True label: 3
Predictions: [0.15, 0.20, 0.18, 0.10, 0.12]
                                    ↑ p(class 3)
Loss = -log(0.10) = 2.30  (high loss = bad!)
```

**Code:**
```python
model.compile(
    loss='sparse_categorical_crossentropy',  # Integer labels (0, 1, 2, ...)
    ...
)
```

**When to use:**
- Labels are integers (e.g., MNIST: 0-9)
- One correct class per example
- Predictions are probabilities (Softmax output)

---

### Categorical Crossentropy

**Use for:** Multi-class classification with one-hot encoded labels

**Difference from sparse:**
- **Sparse:** Labels are integers [0, 1, 2, 3, ...]
- **Categorical:** Labels are one-hot vectors [[1,0,0], [0,1,0], [0,0,1], ...]

**Code:**
```python
model.compile(
    loss='categorical_crossentropy',  # One-hot labels
    ...
)
```

**Example:**
```python
# If labels are one-hot encoded:
y_train = [[1, 0, 0],    # Class 0
           [0, 1, 0],    # Class 1
           [0, 0, 1]]    # Class 2

# Use categorical_crossentropy
```

**Recommendation:** Use `sparse_categorical_crossentropy` unless you specifically one-hot encode labels.

---

### Binary Crossentropy

**Use for:** Binary classification (two classes)

**Code:**
```python
model.compile(
    loss='binary_crossentropy',
    ...
)
```

**Example:**
```python
# Spam detection (spam=1, not spam=0)
model = keras.Sequential([
    layers.Dense(64, activation='relu'),
    layers.Dense(32, activation='relu'),
    layers.Dense(1, activation='sigmoid')  # Output: probability of spam
])

model.compile(
    loss='binary_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)
```

---

### Mean Squared Error (MSE)

**Use for:** Regression (predicting continuous values)

**Formula:** `MSE = (1/n) Σ (y_true - y_pred)^2`

**Code:**
```python
model.compile(
    loss='mse',  # or 'mean_squared_error'
    ...
)
```

**Example:**
```python
# House price prediction
model = keras.Sequential([
    layers.Dense(64, activation='relu'),
    layers.Dense(32, activation='relu'),
    layers.Dense(1)  # Linear output for regression
])

model.compile(
    loss='mse',
    optimizer='adam',
    metrics=['mae']  # Mean Absolute Error for interpretation
)
```

---

### Mean Absolute Error (MAE)

**Use for:** Regression (less sensitive to outliers than MSE)

**Formula:** `MAE = (1/n) Σ |y_true - y_pred|`

**Code:**
```python
model.compile(
    loss='mae',  # or 'mean_absolute_error'
    ...
)
```

**MSE vs MAE:**
- **MSE:** Penalizes large errors more (squared)
- **MAE:** Treats all errors equally (absolute value)
- **Use MSE:** When outliers should be heavily penalized
- **Use MAE:** When outliers are noise (ignore them)

---

## Optimizers

### What is an Optimizer?

**Optimizer** determines HOW weights are updated to minimize loss.

**Basic idea:**
1. Calculate gradient (how much to change each weight)
2. Update weights in direction that reduces loss

**All optimizers implement gradient descent, but differ in:**
- Learning rate (step size)
- Momentum (acceleration)
- Adaptive learning rates (per-parameter)

---

### Adam (Recommended Default)

**Adaptive Moment Estimation - best all-around optimizer**

**Advantages:**
- Adaptive learning rates (adjusts per parameter)
- Combines momentum + RMSprop
- Works well out-of-the-box
- Converges fast

**Code:**
```python
model.compile(
    optimizer='adam',  # Default learning rate = 0.001
    ...
)

# Or with custom learning rate:
model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=0.0001),
    ...
)
```

**When to use:** Almost always (default choice)

---

### SGD (Stochastic Gradient Descent)

**Classic optimizer - simpler but requires tuning**

**Code:**
```python
model.compile(
    optimizer='sgd',  # Default learning rate = 0.01
    ...
)

# With momentum:
model.compile(
    optimizer=keras.optimizers.SGD(learning_rate=0.01, momentum=0.9),
    ...
)
```

**Advantages:**
- Simple and interpretable
- With momentum, can escape local minima

**Disadvantages:**
- Requires careful learning rate tuning
- Same learning rate for all parameters

**When to use:**
- When Adam isn't working
- Research/experimentation

---

### RMSprop

**Root Mean Square Propagation - adaptive learning rates**

**Code:**
```python
model.compile(
    optimizer='rmsprop',
    ...
)
```

**When to use:**
- Recurrent neural networks (RNNs)
- When Adam isn't working well

---

### Optimizer Comparison

| Optimizer | Learning Rate | Adaptive? | Momentum? | Use Case |
|-----------|---------------|-----------|-----------|----------|
| **Adam** | 0.001 | Yes | Yes | Default choice (almost always) |
| **SGD** | 0.01 | No | Optional | Research, experimentation |
| **RMSprop** | 0.001 | Yes | No | RNNs, when Adam fails |

**Recommendation:** Start with Adam. Only switch if you have a specific reason.

---

## Compiling Models

### model.compile() Overview

**Compiling configures the model for training**

```python
model.compile(
    optimizer='adam',                          # How to update weights
    loss='sparse_categorical_crossentropy',    # What to minimize
    metrics=['accuracy']                       # What to report
)
```

**You MUST compile before fit()!**

---

### Complete compile() Examples

**Multi-class classification (MNIST):**
```python
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
```

**Binary classification (spam detection):**
```python
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)
```

**Regression (house prices):**
```python
model.compile(
    optimizer='adam',
    loss='mse',
    metrics=['mae']  # Mean Absolute Error for interpretation
)
```

**Custom learning rate:**
```python
model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=0.0001),  # Lower LR
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
```

---

## Training Models (model.fit)

### model.fit() Overview

**fit() trains the model on data**

```python
history = model.fit(
    X_train, y_train,       # Training data
    epochs=10,              # Number of complete passes through data
    batch_size=32,          # Examples per gradient update
    validation_split=0.2,   # Use 20% of training for validation
    verbose=1               # Show progress bar
)
```

**Returns:** History object containing training metrics

---

### Key Parameters

**epochs (int):**
- One epoch = one complete pass through training data
- More epochs = more training (but risk overfitting)
- Typical: 10-50 epochs for small datasets, 100+ for large

**batch_size (int):**
- Number of examples processed before updating weights
- Smaller batches: Noisier gradients, slower but more updates
- Larger batches: Smoother gradients, faster but fewer updates
- Typical: 32, 64, 128, 256
- Default: 32

**validation_split (float):**
- Fraction of training data to use for validation
- Validation data NOT used for training (monitoring only)
- Helps detect overfitting
- Typical: 0.1 to 0.2

**validation_data (tuple):**
- Alternative to validation_split
- Provide explicit validation set: `(X_val, y_val)`
- Use when you have separate validation data

**verbose (int):**
- 0: Silent
- 1: Progress bar (default)
- 2: One line per epoch

---

### Complete fit() Examples

**Basic training:**
```python
history = model.fit(
    X_train, y_train,
    epochs=10,
    batch_size=32,
    validation_split=0.2
)
```

**With explicit validation set:**
```python
history = model.fit(
    X_train, y_train,
    epochs=10,
    validation_data=(X_val, y_val)
)
```

**Silent training:**
```python
history = model.fit(
    X_train, y_train,
    epochs=10,
    verbose=0  # No output
)
```

---

### Understanding the History Object

**history.history is a dictionary containing:**
- `'loss'`: Training loss per epoch
- `'accuracy'`: Training accuracy per epoch (if accuracy in metrics)
- `'val_loss'`: Validation loss per epoch
- `'val_accuracy'`: Validation accuracy per epoch

**Plotting training curves:**
```python
import matplotlib.pyplot as plt

# Plot accuracy
plt.plot(history.history['accuracy'], label='Training')
plt.plot(history.history['val_accuracy'], label='Validation')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.title('Model Accuracy')
plt.show()

# Plot loss
plt.plot(history.history['loss'], label='Training')
plt.plot(history.history['val_loss'], label='Validation')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.title('Model Loss')
plt.show()
```

**Interpreting curves:**
- **Good:** Training & validation track closely, both improve
- **Overfitting:** Training keeps improving, validation plateaus/worsens
- **Underfitting:** Both plateau early at poor performance

---

## Evaluating Models

### model.evaluate()

**Evaluates model on test set (unseen data)**

```python
test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"Test accuracy: {test_accuracy:.4f}")
print(f"Test loss: {test_loss:.4f}")
```

**Returns:** List of metric values [loss, accuracy, ...]

**Why evaluate on test set?**
- Validation set used during training (can leak information)
- Test set completely unseen → true generalization performance

---

### Complete Evaluation Example

```python
# After training
history = model.fit(X_train, y_train, epochs=10, validation_split=0.2)

# Evaluate on test set
test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=1)

print(f"\nFinal Results:")
print(f"  Test Loss: {test_loss:.4f}")
print(f"  Test Accuracy: {test_accuracy:.4f}")

# Compare to training/validation
final_train_acc = history.history['accuracy'][-1]
final_val_acc = history.history['val_accuracy'][-1]

print(f"\nComparison:")
print(f"  Training Accuracy:   {final_train_acc:.4f}")
print(f"  Validation Accuracy: {final_val_acc:.4f}")
print(f"  Test Accuracy:       {test_accuracy:.4f}")
```

---

## Making Predictions

### model.predict()

**Makes predictions on new data**

```python
predictions = model.predict(X_new)
```

**Returns:** NumPy array of predictions

**Shape:**
- Binary classification: `(n_samples, 1)` - probabilities
- Multi-class: `(n_samples, n_classes)` - probabilities for each class
- Regression: `(n_samples, 1)` - continuous values

---

### Prediction Examples

**Multi-class classification:**
```python
# Predict on test set
predictions = model.predict(X_test)

# predictions shape: (10000, 10) for MNIST
# Each row: probabilities for 10 classes

# Get predicted class (highest probability)
predicted_classes = np.argmax(predictions, axis=1)

print(f"First prediction: {predictions[0]}")
# [0.01, 0.02, 0.05, 0.89, 0.01, 0.01, 0.00, 0.01, 0.00, 0.00]
#                      ↑ Highest → class 3

print(f"Predicted class: {predicted_classes[0]}")
# 3

print(f"True class: {y_test[0]}")
# 3 (correct!)
```

**Single prediction:**
```python
# Predict on one image
sample = X_test[0].reshape(1, 28, 28)  # Add batch dimension
prediction = model.predict(sample, verbose=0)

predicted_class = np.argmax(prediction[0])
confidence = np.max(prediction[0])

print(f"Predicted: {predicted_class} (confidence: {confidence:.2%})")
```

**Binary classification:**
```python
# Spam detection (sigmoid output)
predictions = model.predict(X_test)

# predictions shape: (n_samples, 1)
# Threshold at 0.5
predicted_classes = (predictions > 0.5).astype(int)
```

---

## Model Summary

### model.summary()

**Displays model architecture and parameter counts**

```python
model.summary()
```

**Example output:**
```
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #
=================================================================
flatten (Flatten)            (None, 784)               0
_________________________________________________________________
dense (Dense)                (None, 128)               100480
_________________________________________________________________
dense_1 (Dense)              (None, 64)                8256
_________________________________________________________________
dense_2 (Dense)              (None, 10)                650
=================================================================
Total params: 109,386
Trainable params: 109,386
Non-trainable params: 0
_________________________________________________________________
```

**Interpreting:**
- **Flatten layer:** 0 parameters (just reshapes)
- **First Dense:** (784 inputs × 128 neurons) + 128 biases = 100,480
- **Second Dense:** (128 × 64) + 64 = 8,256
- **Output Dense:** (64 × 10) + 10 = 650
- **Total:** 109,386 learnable weights

**Use summary() to:**
- Verify architecture is correct
- Check parameter counts
- Debug shape mismatches

---

## Saving and Loading Models

### Saving Complete Models

**Save entire model (architecture + weights + optimizer state):**

```python
# After training
model.save('my_model.keras')  # Recommended format (.keras)
```

**Loading:**
```python
loaded_model = keras.models.load_model('my_model.keras')

# Can now use for predictions
predictions = loaded_model.predict(X_new)
```

---

### Saving Weights Only

**Save only weights (not architecture):**

```python
model.save_weights('model_weights.weights.h5')
```

**Loading weights:**
```python
# Must rebuild architecture first
model = keras.Sequential([...])  # Same architecture
model.load_weights('model_weights.weights.h5')

# Compile before using
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
```

**When to use:**
- Saving checkpoints during training
- Experimenting with different architectures using same weights

---

### Best Practices

**For deployment:**
- Save complete model: `model.save('model.keras')`
- Easier to load and use

**For experiments:**
- Save weights only during training
- Smaller file size
- More flexible

---

## Troubleshooting Common Errors

### Error: "ValueError: Input shape mismatch"

**Cause:** First layer's input shape doesn't match data

**Solution:**
```python
# Check data shape
print(X_train.shape)  # e.g., (60000, 28, 28)

# Ensure Flatten matches
model = keras.Sequential([
    layers.Flatten(input_shape=(28, 28)),  # Must match (28, 28)
    ...
])
```

---

### Error: "You must compile your model before training"

**Cause:** Forgot to call model.compile()

**Solution:**
```python
model = keras.Sequential([...])

# MUST compile before fit
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

model.fit(X_train, y_train, epochs=10)  # Now works
```

---

### Error: "Loss is NaN" or "Loss explodes"

**Possible causes:**
1. Learning rate too high
2. Data not normalized
3. Wrong loss function

**Solutions:**
```python
# 1. Lower learning rate
model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=0.0001),  # Lower
    ...
)

# 2. Normalize data
X_train = X_train / 255.0  # Pixels to 0-1 range

# 3. Check loss function matches problem
# Multi-class: sparse_categorical_crossentropy
# Binary: binary_crossentropy
# Regression: mse or mae
```

---

### Error: "Negative dimension size"

**Cause:** Flatten layer receives wrong input shape

**Solution:**
```python
# For grayscale images (28×28)
layers.Flatten(input_shape=(28, 28))

# For RGB images (32×32×3)
layers.Flatten(input_shape=(32, 32, 3))
```

---

### Warning: "Output activation is linear but loss is crossentropy"

**Cause:** Forgot activation on output layer

**Solution:**
```python
# WRONG:
layers.Dense(10)  # No activation for classification!

# CORRECT:
layers.Dense(10, activation='softmax')  # Multi-class
layers.Dense(1, activation='sigmoid')   # Binary
```

---

### Low Accuracy (Model Not Learning)

**Possible causes:**
1. Data not normalized
2. Wrong loss function
3. Learning rate too low
4. Model too simple

**Debugging steps:**
```python
# 1. Check data normalization
print(X_train.min(), X_train.max())  # Should be 0-1 or normalized

# 2. Check loss function matches problem type
# Multi-class: sparse_categorical_crossentropy + softmax
# Binary: binary_crossentropy + sigmoid

# 3. Try default Adam (learning_rate=0.001)
model.compile(optimizer='adam', ...)

# 4. Add more layers or neurons
model = keras.Sequential([
    layers.Dense(256, activation='relu'),  # More neurons
    layers.Dense(128, activation='relu'),
    layers.Dense(64, activation='relu'),   # More layers
    layers.Dense(10, activation='softmax')
])
```

---

### Overfitting (Training >> Validation Accuracy)

**Symptoms:**
- Training accuracy: 99%
- Validation accuracy: 85%
- Gap indicates overfitting

**Solutions:**
```python
# 1. Add Dropout
model = keras.Sequential([
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.5),              # Drop 50% during training
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(10, activation='softmax')
])

# 2. Reduce model capacity
model = keras.Sequential([
    layers.Dense(64, activation='relu'),   # Fewer neurons
    layers.Dense(10, activation='softmax')
])

# 3. Get more training data

# 4. Use early stopping (Week 7)
```

---

## Complete Example

### Full MNIST Classification Pipeline

```python
import keras
from keras import layers
import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# STEP 1: LOAD DATA
# ============================================================
from keras.datasets import mnist
(X_train, y_train), (X_test, y_test) = mnist.load_data()

print(f"Training set: {X_train.shape}, {y_train.shape}")
print(f"Test set: {X_test.shape}, {y_test.shape}")

# ============================================================
# STEP 2: PREPROCESS
# ============================================================
# Normalize to 0-1 range
X_train = X_train / 255.0
X_test = X_test / 255.0

print(f"Data range: [{X_train.min()}, {X_train.max()}]")

# ============================================================
# STEP 3: BUILD MODEL
# ============================================================
model = keras.Sequential([
    layers.Flatten(input_shape=(28, 28)),      # 784 inputs
    layers.Dense(128, activation='relu'),      # Hidden layer 1
    layers.Dense(64, activation='relu'),       # Hidden layer 2
    layers.Dense(10, activation='softmax')     # Output layer
], name='mnist_classifier')

# View architecture
model.summary()

# ============================================================
# STEP 4: COMPILE
# ============================================================
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# ============================================================
# STEP 5: TRAIN (FIT)
# ============================================================
print("\nTraining...")
history = model.fit(
    X_train, y_train,
    epochs=10,
    batch_size=32,
    validation_split=0.2,
    verbose=1
)

# ============================================================
# STEP 6: EVALUATE
# ============================================================
test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"\nTest Accuracy: {test_accuracy:.4f}")

# ============================================================
# STEP 7: PREDICT
# ============================================================
# Predict on first 10 test images
sample_predictions = model.predict(X_test[:10], verbose=0)
predicted_classes = np.argmax(sample_predictions, axis=1)

print("\nSample Predictions:")
for i in range(10):
    print(f"True: {y_test[i]}, Predicted: {predicted_classes[i]}, "
          f"Confidence: {sample_predictions[i][predicted_classes[i]]:.2%}")

# ============================================================
# VISUALIZE TRAINING HISTORY
# ============================================================
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Accuracy
axes[0].plot(history.history['accuracy'], label='Training', marker='o')
axes[0].plot(history.history['val_accuracy'], label='Validation', marker='s')
axes[0].set_xlabel('Epoch')
axes[0].set_ylabel('Accuracy')
axes[0].set_title('Model Accuracy')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Loss
axes[1].plot(history.history['loss'], label='Training', marker='o')
axes[1].plot(history.history['val_loss'], label='Validation', marker='s')
axes[1].set_xlabel('Epoch')
axes[1].set_ylabel('Loss')
axes[1].set_title('Model Loss')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('training_history.png', dpi=150)
plt.show()

# ============================================================
# SAVE MODEL
# ============================================================
model.save('mnist_model.keras')
print("\nModel saved as 'mnist_model.keras'")

# Load and verify
loaded_model = keras.models.load_model('mnist_model.keras')
loaded_test_loss, loaded_test_acc = loaded_model.evaluate(X_test, y_test, verbose=0)
print(f"Loaded model test accuracy: {loaded_test_acc:.4f}")
```

---

## Summary

**Key takeaways from this guide:**

1. **Sequential API workflow:**
   - Load Data → Preprocess → Build → Compile → Fit → Evaluate → Predict

2. **Building models:**
   - Use `keras.Sequential([layers...])`
   - Stack Dense layers with activations
   - Flatten 2D inputs for Dense layers

3. **Activation functions:**
   - **Hidden layers:** ReLU (default)
   - **Binary output:** Sigmoid
   - **Multi-class output:** Softmax
   - **Regression output:** Linear (none)

4. **Loss functions:**
   - **Multi-class (int labels):** sparse_categorical_crossentropy
   - **Binary classification:** binary_crossentropy
   - **Regression:** mse or mae

5. **Optimizers:**
   - **Default choice:** Adam
   - Works well out-of-the-box

6. **Compiling:**
   - **Must** compile before fit
   - Specify: optimizer, loss, metrics

7. **Training:**
   - `model.fit()` trains the model
   - Use validation_split to monitor overfitting
   - epochs = number of passes through data

8. **Evaluation:**
   - `model.evaluate()` on test set for final performance
   - Plot training history to diagnose issues

9. **Predictions:**
   - `model.predict()` for new data
   - Use `np.argmax()` to get predicted class

10. **Saving:**
    - `model.save('model.keras')` for complete model
    - `keras.models.load_model()` to load

**This guide covers everything you need to build, train, and deploy neural networks with Keras Sequential API!**

---

## Additional Resources

**Official Keras Documentation:**
- https://keras.io/guides/

**Keras Examples:**
- https://keras.io/examples/

**TensorFlow Tutorials:**
- https://www.tensorflow.org/tutorials

**Books:**
- "Deep Learning with Python" by François Chollet (Keras creator)

---

**Version:** 1.0 | December 2025
**Course:** Introduction to Machine Learning Programming - Week 6
