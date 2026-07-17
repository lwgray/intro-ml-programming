# Week 6: Student Workbook - Neural Networks & Keras

**Session:** Week 6 - Neural Network Fundamentals
**Purpose:** Note-taking guide for live session

---

## 📝 How to Use This Workbook

**During the live session:**
- Fill in blanks as concepts are explained
- Sketch diagrams when shown
- Note questions in the margins
- Write code snippets you want to remember

**After the live session:**
- Review your notes
- Complete any blank sections
- Compare with classmates
- Use as study guide for post-class work

---

## Section 1: Neural Network Concepts (Segment 2)

### What is a Neural Network?

**Definition:** A neural network is _______________________________________________

**Structure:**
```
___________ Layer → ___________ Layer(s) → ___________ Layer
```

**How it learns:** By adjusting ___________ and ___________ to minimize ___________

---

### Neurons and Layers

**What does a neuron do?**

1. Takes ___________ from previous layer
2. Multiplies each input by a ___________
3. Adds a ___________
4. Passes through ___________ function
5. Sends output to ___________

**Diagram: Draw a single neuron**

```
[Space for your drawing]






```

---

### Activation Functions

**Why do we need activation functions?**

___________________________________________________________________

**Fill in the table:**

| Activation | Formula | When to Use | Range |
|------------|---------|-------------|-------|
| ReLU | max(0, x) | ____________ layers | [0, ∞) |
| Sigmoid | ____________ | Binary classification ____________ | [__, __] |
| Softmax | ____________ | Multi-class classification ____________ | Probabilities sum to __ |

**Sketch the activation functions:**

```
ReLU:          Sigmoid:        Softmax:
                                (concept)





```

---

### Forward and Backward Propagation

**Forward propagation:**
- Input flows through network → produces ___________
- Each layer applies: ___________ → ___________ → ___________

**Backward propagation (backprop):**
- Calculates how to adjust ___________ based on ___________
- Error flows ___________ through layers
- Keras handles this automatically when you call ___________

**Key insight:** You don't need to implement backprop! Just understand it adjusts weights to reduce ___________

---

## Section 2: Keras Fundamentals (Segment 3)

### The Sequential API

**What is Sequential?**

___________________________________________________________________

**Basic pattern:**
```python
model = keras.Sequential([
    layers._____(units, activation='____'),
    layers._____(units, activation='____'),
    layers._____(units, activation='____')
])
```

---

### Dense Layers

**What is a Dense layer?**

___________________________________________________________________

**Parameters:**
- `units`: Number of ___________
- `activation`: ___________ function to apply
- `input_shape`: Required only for ___________ layer

**Example:**
```python
# Your notes from demo:




```

---

### model.summary()

**What does it show?**

1. ___________________________________________
2. ___________________________________________
3. ___________________________________________

**How to calculate parameters:**

First Dense layer (assuming 784 inputs, 128 neurons):
- Parameters = (___ × ___) + ___ = _________

**Why always call summary()?**

___________________________________________________________________

---

### Compiling a Model

**What does compile do?**

___________________________________________________________________

**Three required arguments:**

1. **optimizer** = '___________' (default choice: _________)
   - Purpose: ___________________________________________

2. **loss** = '___________'
   - For binary classification: ___________________________
   - For multi-class with integer labels: _________________
   - For multi-class with one-hot labels: _________________

3. **metrics** = ['___________']
   - Purpose: ___________________________________________

**Code snippet:**
```python
model.compile(
    optimizer='____',
    loss='____',
    metrics=['____']
)
```

---

## Section 3: Training a Network (Segment 6)

### MNIST Dataset

**What is MNIST?**

___________________________________________________________________

**Dataset stats:**
- Training images: ___________
- Test images: ___________
- Image size: ___ × ___ pixels
- Number of classes: _____ (digits ___ to ___)
- Data type: uint8 (values ___ to ___)

---

### Data Normalization ⭐ CRITICAL!

**Why normalize pixel values?**

1. ___________________________________________________________________
2. ___________________________________________________________________
3. ___________________________________________________________________

**How to normalize:**
```python
X_train = ___________
X_test = ___________
```

**Before normalization:** Values are [___, ___]
**After normalization:** Values are [___, ___]

**🔑 Key reminder:** ALWAYS ___________ inputs for neural networks!

---

### Building the MNIST Model

**Architecture:**
```
Input: ___ × ___ pixels = ____ values (after Flatten)
    ↓
Hidden Layer 1: ___ neurons, ___ activation
    ↓
Hidden Layer 2: ___ neurons, ___ activation
    ↓
Output Layer: ___ neurons, ___ activation
```

**Code:**
```python
model = keras.Sequential([
    layers._________(input_shape=(__, __)),
    layers._________(__, activation='___'),
    layers._________(__, activation='___'),
    layers._________(__, activation='___')
])
```

**Total parameters:** ~___________

---

### Training Configuration

**model.fit() arguments:**

```python
history = model.fit(
    X_train, y_train,
    epochs=____,              # Meaning: ________________
    batch_size=____,          # Meaning: ________________
    validation_split=____,    # Meaning: ________________
    verbose=____              # Meaning: ________________
)
```

**What is an epoch?**

___________________________________________________________________

**What is batch size?**

___________________________________________________________________

**What is validation_split?**

___________________________________________________________________

---

### Training History

**What does the history object contain?**

___________________________________________________________________

**Four keys:**
- history.history['___________']
- history.history['___________']
- history.history['___________']
- history.history['___________']

**Sketch: Draw example training curves**

```
Accuracy over time:          Loss over time:





```

---

### Interpreting Training Curves

**Healthy learning:**
- Training accuracy: ___________
- Validation accuracy: ___________
- Gap between them: ___________

**Overfitting:**
- Training accuracy: ___________
- Validation accuracy: ___________
- Symptom: ___________

**Underfitting:**
- Training accuracy: ___________
- Validation accuracy: ___________
- Solution: ___________

---

## Section 4: Model Evaluation (Segment 6)

### Test Set Performance

**Why use a test set?**

___________________________________________________________________

**How to evaluate:**
```python
test_loss, test_accuracy = model._____(X_test, y_test)
```

**Expected MNIST accuracy:** ~___________

---

### Making Predictions

**How to predict:**
```python
predictions = model._____(X_new)
```

**For multi-class classification:**
- Output shape: (num_samples, num_classes)
- Each row: ___________ for each class
- Sum of probabilities: ___
- To get predicted class: np._____(predictions, axis=1)

**Example prediction:**
```
Probabilities: [0.01, 0.02, 0.05, 0.85, 0.03, 0.01, 0.01, 0.01, 0.00, 0.01]
Predicted class: ____
Confidence: ____%
```

---

## Section 5: Pair Programming (Segment 7)

### Experiments

**Experiment 1: Add a third hidden layer**
- Architecture change: ___________________________________________
- Result: Accuracy __________, Training time __________
- Observation: ___________________________________________

**Experiment 2: Remove a hidden layer**
- Architecture change: ___________________________________________
- Result: Accuracy __________, Training time __________
- Observation: ___________________________________________

**Experiment 3: Change neuron counts**
- Architecture change: ___________________________________________
- Result: Accuracy __________, Training time __________
- Observation: ___________________________________________

**Experiment 4: Try different activation**
- Change: Use '___________' instead of 'relu'
- Result: Accuracy __________, Training time __________
- Observation: ___________________________________________

---

### Key Insights from Experimentation

**What happened when you made the network deeper?**

___________________________________________________________________

**What happened when you made it shallower?**

___________________________________________________________________

**What happened when you changed activations?**

___________________________________________________________________

**What's the tradeoff between model size and performance?**

___________________________________________________________________

---

## Section 6: Key Takeaways

### The Keras Workflow

**Five steps:**
1. ___________: `keras.Sequential()` + layers
2. ___________: optimizer, loss, metrics
3. ___________: `model.fit()`
4. ___________: `model.evaluate()`
5. ___________: `model.predict()`

---

### Critical Concepts to Remember

1. **Normalization is essential** because:
   ___________________________________________________________________

2. **Activation functions enable** _________________________________
   ___________________________________________________________________

3. **Deeper networks can** ________________________________________
   ___________________________________________________________________

4. **Validation data helps** _______________________________________
   ___________________________________________________________________

5. **Training curves diagnose** ____________________________________
   ___________________________________________________________________

---

## Section 7: Questions and Confusion

**Questions I still have:**

1. ___________________________________________________________________

2. ___________________________________________________________________

3. ___________________________________________________________________

**Concepts I'm fuzzy on:**

1. ___________________________________________________________________

2. ___________________________________________________________________

**What I want to practice more:**

1. ___________________________________________________________________

2. ___________________________________________________________________

---

## Section 8: Action Items

**To do before next week:**
- [ ] Complete post-class exercise (build MNIST from scratch)
- [ ] Review training curve interpretation
- [ ] Experiment with bonus activation exploration (optional)
- [ ] Read Keras documentation (Sequential API)
- [ ] Review pre-class videos if needed

**Personal learning goals:**
- [ ] ___________________________________________________________
- [ ] ___________________________________________________________
- [ ] ___________________________________________________________

---

## Architecture Diagram Space

**Draw the MNIST network architecture:**

```
[Space for drawing the full network with all layers, neurons, and connections]















```

---

## Code Snippets to Remember

**Snippet 1: Complete MNIST pipeline**
```python
# Your condensed version of the key code:















```

**Snippet 2: Training and visualization**
```python
# Key patterns for training and plotting:







```

---

## Reflection

**What was the "aha!" moment for you today?**

___________________________________________________________________
___________________________________________________________________

**What was most challenging?**

___________________________________________________________________
___________________________________________________________________

**How does this connect to your project/work?**

___________________________________________________________________
___________________________________________________________________

---

*Use this workbook as a study guide! Review before next session.*

*Last Updated: 2026-02-02*
