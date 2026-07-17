# Week 6: Self-Assessment Checklist

**Purpose:** Verify you've mastered Week 6 concepts
**How to use:** Check off each skill honestly. If you can't check it, review that topic!

---

## ✅ Neural Network Concepts

**I can explain:**

- [ ] What a neural network is (in simple terms, to a non-technical person)
- [ ] How neurons work (weighted sum + bias + activation → output)
- [ ] Why we need activation functions (introduce non-linearity)
- [ ] The difference between shallow and deep networks
- [ ] What forward propagation means (data flowing through network)
- [ ] What backpropagation does (conceptually, not mathematically)
- [ ] How neural networks learn (adjust weights to minimize loss)

**Reflection:** Which concept is still fuzzy? ________________________________

---

## ✅ Activation Functions

**I can:**

- [ ] Name at least 3 activation functions (ReLU, Sigmoid, Softmax)
- [ ] Explain when to use ReLU (hidden layers - default choice)
- [ ] Explain when to use Sigmoid (binary classification output)
- [ ] Explain when to use Softmax (multi-class classification output)
- [ ] Describe what ReLU does mathematically (max(0, x))
- [ ] Understand why sigmoid in hidden layers causes problems (vanishing gradients)

**Test yourself:** For MNIST, which activations would you use?
- Hidden layers: ___________
- Output layer: ___________

---

## ✅ Keras API - Building Models

**I can:**

- [ ] Set the PyTorch backend before importing Keras
- [ ] Import Keras and layers correctly
- [ ] Create a Sequential model
- [ ] Add Dense layers with specified neurons and activations
- [ ] Add a Flatten layer for image data
- [ ] Call `model.summary()` and interpret the output
- [ ] Calculate parameter counts for a layer (manually or conceptually)

**Practical test:** Without looking, write the code to create a model with:
- Flatten layer (28×28 input)
- Hidden layer: 64 neurons, ReLU
- Output layer: 10 neurons, Softmax

```python
# Try writing it here:




```

---

## ✅ Keras API - Compiling

**I can:**

- [ ] Compile a model with optimizer, loss, and metrics
- [ ] Choose the correct optimizer (usually 'adam')
- [ ] Choose the correct loss function for my problem type
- [ ] Explain the difference between `sparse_categorical_crossentropy` and `categorical_crossentropy`
- [ ] Add appropriate metrics (['accuracy'] most common)

**Test yourself:** What loss function for:
- Binary classification: ___________
- Multi-class with integer labels (0, 1, 2, ...): ___________
- Multi-class with one-hot labels: ___________

---

## ✅ Keras API - Training

**I can:**

- [ ] Train a model using `model.fit()`
- [ ] Set the number of epochs appropriately
- [ ] Set batch_size (understand what it does)
- [ ] Use validation_split to monitor overfitting
- [ ] Interpret training output (loss and accuracy improving)
- [ ] Access training history after training

**Practical test:** Fill in the blanks:
```python
history = model.fit(
    X_train, y_train,
    epochs=____,           # How many complete passes through data?
    validation_split=____  # What fraction for validation?
)
```

---

## ✅ Keras API - Evaluation & Prediction

**I can:**

- [ ] Evaluate a model on test data using `model.evaluate()`
- [ ] Make predictions using `model.predict()`
- [ ] Convert probabilities to predicted classes (np.argmax)
- [ ] Interpret prediction probabilities
- [ ] Understand the difference between training, validation, and test sets

**Test yourself:** What does `model.predict()` return for multi-class classification?

Answer: _______________________________________________________________

---

## ✅ Data Preprocessing

**I can:**

- [ ] Normalize image data (divide by 255.0)
- [ ] Explain WHY normalization is critical (training stability, activation functions work better)
- [ ] Remember to normalize BOTH training and test data
- [ ] Verify normalization worked (check min/max values)
- [ ] Load MNIST dataset using Keras

**Critical question:** What happens if you forget to normalize?

Answer: _______________________________________________________________

---

## ✅ Training History Visualization

**I can:**

- [ ] Access training metrics from history object
- [ ] Plot accuracy curves (training and validation)
- [ ] Plot loss curves (training and validation)
- [ ] Interpret training curves (identify healthy learning)
- [ ] Identify overfitting from curves (train improving, validation worsening)
- [ ] Identify underfitting from curves (both plateau early)

**Visual test:** Sketch what overfitting looks like:
```
Accuracy curves:         Loss curves:




```

---

## ✅ Model Architecture Decisions

**I can:**

- [ ] Choose an appropriate number of layers (start with 1-2 hidden)
- [ ] Choose neuron counts (64-128 is common starting point)
- [ ] Design architecture for binary classification (1 output, sigmoid)
- [ ] Design architecture for multi-class classification (N outputs, softmax)
- [ ] Understand tradeoffs: deeper vs. shallower, wider vs. narrower
- [ ] Experiment with architectures and observe effects

**Scenario:** You're building a 5-class classifier. Design the architecture:
- Input shape: (20,) features
- Your architecture:
  ```



  ```

---

## ✅ Troubleshooting Common Issues

**I can:**

- [ ] Diagnose "low accuracy" (forgot to normalize? wrong loss function?)
- [ ] Diagnose "NaN loss" (didn't normalize? learning rate too high?)
- [ ] Diagnose overfitting (large train-val gap → need regularization)
- [ ] Diagnose underfitting (both accuracies low → need more capacity)
- [ ] Read and fix error messages from Keras

**Common errors - can you fix them?**

Problem: Accuracy stuck at ~10% for MNIST
- Likely cause: ___________
- Solution: ___________

---

## ✅ MNIST Specifics

**I can:**

- [ ] Load MNIST dataset
- [ ] Describe MNIST (70,000 handwritten digits, 28×28 pixels)
- [ ] Build a classifier for MNIST
- [ ] Achieve >95% accuracy on MNIST
- [ ] Normalize MNIST correctly (0-255 → 0-1)
- [ ] Use Flatten layer to convert 28×28 to 784 inputs

**Performance check:** What accuracy did you achieve on MNIST?
- My test accuracy: ___________%
- Is it >95%? _____ (If not, review your architecture/normalization)

---

## ✅ Conceptual Understanding

**I can explain to a colleague:**

- [ ] How neural networks are different from logistic regression
- [ ] When to use neural networks vs. XGBoost
- [ ] Why neural networks need more data than traditional ML
- [ ] Why we use epochs (network needs multiple passes to learn)
- [ ] Why we use validation split (monitor overfitting)
- [ ] What "learning" means in neural networks (adjusting weights)

**Explain in one sentence:** How does a neural network learn?

Your answer: _______________________________________________________________

---

## ✅ Practical Skills

**I can:**

- [ ] Build a neural network from scratch in Keras
- [ ] Train it on real data (MNIST)
- [ ] Visualize training progress
- [ ] Evaluate performance
- [ ] Experiment with different architectures
- [ ] Debug common issues

**Final test:** Could you build a digit classifier for a friend?
- [ ] Yes, confidently
- [ ] Yes, with some reference to notes
- [ ] Not yet - need more practice

---

## 📊 Overall Self-Assessment

### Count your checks:

**Total items:** 83
**Items checked:** _____
**Percentage mastery:** _____%

### Scoring Guide:

- **90-100% (75+ checks):** Excellent! You've mastered Week 6. Ready for Week 7!
- **75-89% (62-74 checks):** Good progress. Review unchecked items before next week.
- **60-74% (50-61 checks):** Decent foundation. Spend extra time on weak areas.
- **Below 60% (<50 checks):** Need more practice. Revisit materials and exercises.

---

## 🎯 Action Plan

Based on unchecked items, what should you focus on?

### Top 3 topics to review:

1. ___________________________________________________________________

2. ___________________________________________________________________

3. ___________________________________________________________________

### How will you review them?

- [ ] Re-watch relevant video segments
- [ ] Re-do practice exercises
- [ ] Review glossary for definitions
- [ ] Ask questions in discussion forum
- [ ] Practice building models from scratch
- [ ] Work through bonus exercises

---

## 📚 Recommended Review Materials

**If you're weak on Concepts:**
- Re-watch 3Blue1Brown videos
- Review Week6_Glossary.md
- Read Keras documentation

**If you're weak on Code:**
- Redo week6_preclass_practice.ipynb
- Redo week6_postclass_exercise.ipynb
- Try week6_bonus_activation_exploration.ipynb

**If you're weak on Architecture Design:**
- Redo week6_pair_programming.ipynb
- Experiment more with different architectures
- Review Keras Cheat Sheet decision trees

---

## ✅ Week 6 Skills - Can You?

**Rapid-fire checklist:**

- [ ] Build a Sequential model
- [ ] Add Dense layers
- [ ] Compile with correct loss function
- [ ] Train for multiple epochs
- [ ] Monitor validation performance
- [ ] Plot training curves
- [ ] Evaluate on test set
- [ ] Make predictions
- [ ] Normalize data before training
- [ ] Choose ReLU for hidden layers
- [ ] Choose Softmax for multi-class output
- [ ] Interpret model.summary()
- [ ] Diagnose overfitting
- [ ] Experiment with architectures

**All checked?** You're ready for Week 7! 🎉

---

## 🚀 Looking Ahead to Week 7

**Week 7 Preview:** Deep Learning Best Practices

**You'll learn:**
- Dropout (regularization technique)
- Early stopping (callbacks)
- Model saving and loading
- Fashion-MNIST (slightly harder dataset)
- More advanced techniques

**To prepare:**
- Make sure you're solid on Week 6 basics
- Understand overfitting well
- Be comfortable with Keras API

---

## 💭 Reflection Questions

**Answer honestly:**

### What was your biggest "aha!" moment this week?

___________________________________________________________________

### What's still confusing?

___________________________________________________________________

### How confident are you building neural networks? (1-10)

_____ / 10

### What will you do to improve before Week 7?

___________________________________________________________________

---

## ✅ Final Checklist

**Before moving to Week 7, ensure:**

- [ ] I can build a Keras Sequential model from scratch
- [ ] I understand normalization and always remember to do it
- [ ] I can compile with appropriate optimizer, loss, and metrics
- [ ] I can train with validation monitoring
- [ ] I can plot and interpret training curves
- [ ] I can evaluate model performance
- [ ] I achieved >95% on MNIST
- [ ] I experimented with different architectures
- [ ] I understand when to use neural networks vs. traditional ML

**All checked?** Congratulations! You've mastered Week 6! 🎓

---

*Use this self-assessment honestly to guide your learning.*
*Revisit unchecked items before Week 7!*

*Last Updated: 2026-02-02*
