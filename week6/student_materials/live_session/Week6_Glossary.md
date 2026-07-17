# Week 6: Neural Networks & Keras - Glossary

**Purpose:** Quick reference for all key terms introduced in Week 6

**How to use:**
- Look up unfamiliar terms during study
- Review definitions before assessments
- Use as flashcards for memorization

---

## Neural Network Architecture Terms

### Neuron
**Definition:** The basic computational unit in a neural network.

**What it does:**
1. Receives inputs from previous layer (or raw data)
2. Computes weighted sum: Σ(input × weight) + bias
3. Applies activation function
4. Sends output to next layer

**Analogy:** Like a biological neuron that fires when stimulated above a threshold.

---

### Layer
**Definition:** A collection of neurons that operate in parallel at the same level of the network.

**Types:**
- **Input layer:** Receives raw data (often just conceptual, not an actual layer in code)
- **Hidden layer:** Intermediate layers that learn features
- **Output layer:** Produces final predictions

**Example:** In MNIST, we have Flatten → Dense(128) → Dense(64) → Dense(10)

---

### Weight
**Definition:** A parameter that scales the strength of a connection between neurons.

**Purpose:** Determines how much influence one neuron has on another.

**Learning:** Weights are adjusted during training (via backpropagation) to minimize loss.

**Notation:** Often denoted as W or w

**Example:** In a Dense layer with 784 inputs and 128 neurons, there are 784 × 128 = 100,352 weights.

---

### Bias
**Definition:** An additive parameter in each neuron that shifts the activation function.

**Purpose:** Allows the neuron to activate even when all inputs are zero.

**Learning:** Like weights, biases are learned during training.

**Notation:** Often denoted as b

**Example:** Each of the 128 neurons in a Dense(128) layer has its own bias, adding 128 bias parameters.

---

### Dense Layer (Fully Connected Layer)
**Definition:** A layer where every neuron connects to every neuron in the previous layer.

**Keras syntax:**
```python
layers.Dense(units, activation='relu')
```

**Parameters:**
- `units`: Number of neurons in this layer
- `activation`: Activation function to apply

**Why "Dense"?** Because connections are "dense" - every input connects to every output.

---

### Flatten Layer
**Definition:** A layer that reshapes multi-dimensional input into a 1D vector.

**Purpose:** Convert 2D images (or 3D data) into format suitable for Dense layers.

**Example:**
- Input: 28×28 image (2D)
- After Flatten: 784 values (1D)
- No parameters learned (just reshaping)

**Keras syntax:**
```python
layers.Flatten(input_shape=(28, 28))
```

---

## Activation Functions

### Activation Function
**Definition:** A non-linear function applied after the weighted sum in a neuron.

**Purpose:** Introduces non-linearity, allowing networks to learn complex patterns.

**Without activation:** Stacking layers is pointless (just creates a complicated linear function).

**Common ones:** ReLU, Sigmoid, Softmax, Tanh

---

### ReLU (Rectified Linear Unit)
**Definition:** Activation function that outputs max(0, x)

**Formula:**
- If input > 0: output = input
- If input ≤ 0: output = 0

**When to use:** Default choice for hidden layers

**Advantages:**
- Simple and fast
- Avoids vanishing gradient problem
- Works well in practice

**Graph:** A hockey stick shape (flat at 0, then linear slope)

---

### Sigmoid
**Definition:** Activation function that squashes input to range [0, 1]

**Formula:** σ(x) = 1 / (1 + e^(-x))

**When to use:** Binary classification output layer

**Purpose:** Converts any input to a probability (0 to 1)

**Example:** Predicting if an image contains a cat (yes/no)

**Note:** Avoid in hidden layers (causes vanishing gradients)

---

### Softmax
**Definition:** Activation function that converts outputs to probabilities that sum to 1

**Formula:** For each output: e^(x_i) / Σ(e^(x_j))

**When to use:** Multi-class classification output layer

**Purpose:** Gives probability distribution over classes

**Example MNIST:** 10 outputs (one per digit) that sum to 1.0
- [0.01, 0.02, 0.05, 0.85, 0.03, 0.01, 0.01, 0.01, 0.00, 0.01]
- Predicted class: 3 (highest probability)

---

### Tanh (Hyperbolic Tangent)
**Definition:** Activation function that squashes input to range [-1, 1]

**Formula:** tanh(x) = (e^x - e^(-x)) / (e^x + e^(-x))

**When to use:** Alternative to ReLU in hidden layers (less common)

**Advantage over Sigmoid:** Centered at 0 (mean of outputs is ~0)

**Note:** Can suffer from vanishing gradients (like Sigmoid)

---

## Training Concepts

### Forward Propagation
**Definition:** The process of passing input data through the network to produce a prediction.

**Steps:**
1. Input enters at first layer
2. Each layer applies: weighted sum → activation → pass to next layer
3. Final layer produces prediction

**Think of it as:** Data flowing forward through the network

---

### Backpropagation (Backprop)
**Definition:** The algorithm that calculates how to adjust weights to reduce error.

**Process:**
1. Calculate prediction error (how wrong was the output?)
2. Propagate error backward through layers
3. Compute gradient for each weight (how much did this weight contribute to error?)
4. Update weights in direction that reduces error

**Key insight:** You don't implement this! Keras does it automatically during `model.fit()`.

---

### Loss Function
**Definition:** A function that measures how wrong the model's predictions are.

**Purpose:** What the optimizer tries to minimize during training.

**Common ones:**
- **binary_crossentropy:** Binary classification
- **sparse_categorical_crossentropy:** Multi-class with integer labels
- **categorical_crossentropy:** Multi-class with one-hot labels
- **mse (mean squared error):** Regression

**Key:** Match loss to your problem type!

---

### Optimizer
**Definition:** The algorithm that adjusts weights to minimize loss.

**Common ones:**
- **Adam:** Adaptive learning rate, excellent default choice
- **SGD (Stochastic Gradient Descent):** Simpler, sometimes better with tuning
- **RMSprop:** Good for recurrent networks

**What it does:** Implements gradient descent (finding the "valley" in the loss landscape)

**Keras usage:**
```python
model.compile(optimizer='adam', ...)
```

---

### Epoch
**Definition:** One complete pass through the entire training dataset.

**Example:** If you have 60,000 training samples:
- 1 epoch = network sees all 60,000 samples once
- 10 epochs = network sees all 60,000 samples ten times

**Why multiple epochs?** Network needs multiple passes to learn patterns.

**Too few:** Underfitting (didn't learn enough)
**Too many:** Overfitting (memorized training data)

---

### Batch Size
**Definition:** Number of samples processed before updating weights.

**Example:** With 60,000 samples and batch_size=128:
- 60,000 ÷ 128 ≈ 469 batches per epoch
- Weights updated 469 times per epoch

**Trade-offs:**
- **Small batches (16-32):** More frequent updates, more noisy, can escape local minima
- **Large batches (128-256):** Fewer updates, more stable, faster per epoch

**Common choice:** 32 or 128

---

### Validation Split
**Definition:** Fraction of training data held out for validation during training.

**Purpose:** Monitor overfitting in real-time.

**Example:** `validation_split=0.2` means:
- 80% of training data used for training
- 20% used for validation (unseen during weight updates)

**Keras reports both:**
- Training metrics (on the 80%)
- Validation metrics (on the 20%)

**Key:** If validation performance drops while training improves → overfitting!

---

### Training History
**Definition:** Object returned by `model.fit()` containing metrics for each epoch.

**Contents:**
- `history.history['loss']`: Training loss per epoch
- `history.history['accuracy']`: Training accuracy per epoch
- `history.history['val_loss']`: Validation loss per epoch
- `history.history['val_accuracy']`: Validation accuracy per epoch

**Use:** Plot these to visualize learning and diagnose issues.

---

## Keras API Terms

### Sequential API
**Definition:** Keras API for building models as a linear stack of layers.

**When to use:** When layers connect sequentially (A → B → C)

**Syntax:**
```python
model = keras.Sequential([
    layer1,
    layer2,
    layer3
])
```

**Alternative:** Functional API (for complex architectures with branching - Week 7-8)

---

### model.compile()
**Definition:** Method that configures the model for training.

**Required arguments:**
- `optimizer`: How to update weights
- `loss`: What to minimize
- `metrics`: What to monitor (for reporting only)

**Example:**
```python
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
```

**When to call:** After building model, before training.

---

### model.fit()
**Definition:** Method that trains the model on data.

**Common arguments:**
- `X_train, y_train`: Training data and labels
- `epochs`: How many complete passes through data
- `batch_size`: Samples per batch
- `validation_split`: Fraction for validation
- `verbose`: Display mode (0=silent, 1=progress bar)

**Returns:** History object containing training metrics

**Example:**
```python
history = model.fit(X_train, y_train, epochs=10, validation_split=0.2)
```

---

### model.evaluate()
**Definition:** Method that evaluates model on test data.

**Returns:** Loss and all metrics specified in compile()

**Example:**
```python
test_loss, test_accuracy = model.evaluate(X_test, y_test)
```

**Purpose:** Assess final model performance on unseen data.

---

### model.predict()
**Definition:** Method that generates predictions for new data.

**Returns:** Raw output from model (probabilities for classification)

**Example:**
```python
predictions = model.predict(X_new)
```

**For classification:** Use `np.argmax(predictions, axis=1)` to get predicted classes.

---

### model.summary()
**Definition:** Method that displays model architecture.

**Shows:**
- Layer types and names
- Output shapes for each layer
- Number of parameters (weights + biases) per layer
- Total parameters

**Example output:**
```
Model: "sequential"
┏━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━┓
┃ Layer (type)      ┃ Output Shape  ┃  Param #  ┃
┣━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ dense (Dense)     ┃ (None, 128)   ┃   100,480 ┃
┃ dense_1 (Dense)   ┃ (None, 10)    ┃     1,290 ┃
┗━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━┻━━━━━━━━━━━┛
Total params: 101,770
```

**When to use:** After building model to verify architecture.

---

## Data Preprocessing Terms

### Normalization
**Definition:** Scaling input data to a standard range (typically 0-1 or -1 to 1)

**Why it's critical for neural networks:**
1. Training stability (large values cause unstable gradients)
2. Activation functions work better with small inputs
3. Faster convergence (20× faster training!)

**For images:**
```python
X_train = X_train / 255.0  # Scale from 0-255 to 0-1
X_test = X_test / 255.0
```

**Rule:** ALWAYS normalize inputs for neural networks!

---

### One-Hot Encoding
**Definition:** Converting categorical labels to binary vectors.

**Example:**
- Original labels: [0, 1, 2, 3]
- One-hot encoded:
  - 0 → [1, 0, 0, 0]
  - 1 → [0, 1, 0, 0]
  - 2 → [0, 0, 1, 0]
  - 3 → [0, 0, 0, 1]

**When needed:** With `categorical_crossentropy` loss

**When NOT needed:** With `sparse_categorical_crossentropy` (use integer labels directly)

**Keras utility:**
```python
keras.utils.to_categorical(y_train, num_classes=10)
```

---

## Model Evaluation Terms

### Accuracy
**Definition:** Fraction of predictions that are correct.

**Formula:** correct predictions / total predictions

**Example:** 9,750 correct out of 10,000 = 0.975 = 97.5%

**When to use:** Balanced datasets

**When NOT to use:** Imbalanced datasets (use precision/recall instead - Week 2)

---

### Overfitting
**Definition:** When model learns training data too well, including noise.

**Symptoms:**
- High training accuracy
- Low test/validation accuracy
- Gap between training and validation curves

**Causes:** Model too complex, too many epochs, insufficient data

**Solutions:**
- Regularization (Week 7: Dropout)
- Early stopping
- More training data
- Simpler model

---

### Underfitting
**Definition:** When model is too simple to capture patterns in data.

**Symptoms:**
- Low training accuracy
- Low test/validation accuracy
- Both curves plateau early

**Causes:** Model too simple, too few epochs, poor features

**Solutions:**
- More complex model (more layers/neurons)
- Train longer
- Better features

---

### Generalization
**Definition:** Model's ability to perform well on unseen data.

**Goal:** Good generalization (test performance close to training performance)

**How to assess:** Compare training accuracy to test accuracy

**Good generalization:** Small gap (≤ 2-3% difference)
**Poor generalization:** Large gap (overfitting)

---

## MNIST-Specific Terms

### MNIST
**Definition:** Modified National Institute of Standards and Technology database of handwritten digits.

**Details:**
- 70,000 grayscale images of digits 0-9
- 60,000 training images
- 10,000 test images
- Each image: 28×28 pixels
- Pixel values: 0-255 (uint8)

**Why used:** Standard benchmark for image classification. Simple enough to train on CPU.

---

### Pixel
**Definition:** Individual element in an image (picture element).

**For grayscale images:** Value from 0 (black) to 255 (white)

**Example:** 28×28 image = 784 pixels total

**For neural networks:** Each pixel becomes one input feature after flattening.

---

## Common Patterns

### The Keras Workflow
**Pattern:** Build → Compile → Fit → Evaluate → Predict

**Code template:**
```python
# 1. Build
model = keras.Sequential([layers])

# 2. Compile
model.compile(optimizer, loss, metrics)

# 3. Fit
history = model.fit(X_train, y_train, epochs, validation_split)

# 4. Evaluate
test_loss, test_acc = model.evaluate(X_test, y_test)

# 5. Predict
predictions = model.predict(X_new)
```

---

### Choosing Activation Functions

**Pattern:**
- **Hidden layers:** ReLU (default choice)
- **Binary classification output:** Sigmoid
- **Multi-class classification output:** Softmax
- **Regression output:** Linear (no activation)

---

### Choosing Loss Functions

**Pattern:**
- **Binary classification:** `binary_crossentropy`
- **Multi-class (integer labels):** `sparse_categorical_crossentropy`
- **Multi-class (one-hot labels):** `categorical_crossentropy`
- **Regression:** `mse` or `mae`

---

## Quick Reference Tables

### Activation Functions Summary

| Function | Formula | Range | Use Case |
|----------|---------|-------|----------|
| ReLU | max(0, x) | [0, ∞) | Hidden layers |
| Sigmoid | 1/(1+e^-x) | [0, 1] | Binary output |
| Softmax | e^xi / Σe^xj | [0, 1], sum=1 | Multi-class output |
| Tanh | (e^x-e^-x)/(e^x+e^-x) | [-1, 1] | Hidden layers (alt) |

---

### Loss Functions Summary

| Loss | Use Case | Label Format |
|------|----------|--------------|
| binary_crossentropy | Binary classification | 0 or 1 |
| sparse_categorical_crossentropy | Multi-class | Integer (0, 1, 2, ...) |
| categorical_crossentropy | Multi-class | One-hot encoded |
| mse | Regression | Continuous values |

---

### Optimizer Summary

| Optimizer | Best For | Learning Rate |
|-----------|----------|---------------|
| Adam | Most problems (default) | Adaptive |
| SGD | Fine-tuning, simple problems | Fixed |
| RMSprop | Recurrent networks | Adaptive |

---

## Tips for Success

**When building models:**
- ✓ Always set backend before importing Keras
- ✓ Always normalize inputs
- ✓ Always call model.summary() to verify architecture
- ✓ Match loss function to problem type
- ✓ Use validation_split to monitor overfitting

**When stuck:**
- Check if you normalized data
- Check activation functions (ReLU hidden, Softmax/Sigmoid output)
- Check loss function matches label format
- Check model.summary() for parameter counts

---

*Use this glossary as a reference! Bookmark it for quick lookups.*

*Last Updated: 2026-02-02*
