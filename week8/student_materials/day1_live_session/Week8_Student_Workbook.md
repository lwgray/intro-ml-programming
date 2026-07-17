# Week 8 Student Workbook

Use this alongside `week8_live_session.ipynb`. As you work through each section, fill in the blanks and answer the reflection questions. **You'll thank yourself later.**

---

## Setting up

**Date of session:** ___________
**My GPU compute platform:** ___________
**Did GPU verification succeed?** Yes / No

---

## Section 0: Setup

### What is `KERAS_BACKEND = 'torch'` doing?
*Answer in 1-2 sentences:*
___________________________________________
___________________________________________

### Why do we set a random seed?
*Answer in 1 sentence:*
___________________________________________

---

## Section 1: Loading Fashion-MNIST

### Critical input shape question
| Format | Shape | When to use |
|---|---|---|
| Original | `(60000, 28, 28)` | Just loaded from `load_data()` |
| MLP-ready (Week 7) | `(60000, ____)` | Flattened for Dense layers |
| CNN-ready (Week 8) | `(60000, ____, ____, ____)` | With channel dimension |

### What does `np.expand_dims(X, axis=-1)` do?
*Answer in your own words:*
___________________________________________

---

## Section 2: MLP Baseline (Week 7 Recap)

### Note the parameter count
- MLP total parameters: ___________
- MLP test accuracy: ___________

### Where do most of the MLP parameters live?
*Hint: look at `model.summary()`. Which layer has the most weights?*
___________________________________________

---

## Section 3: Build the CNN

### Architecture diagram (fill in)
```
Input (28, 28, 1)
  ↓
Conv2D( ___ filters, ___ kernel) + ReLU
  ↓
MaxPooling2D(___)
  ↓
Conv2D( ___ filters, ___ kernel) + ReLU
  ↓
MaxPooling2D(___)
  ↓
Flatten
  ↓
Dense( ___ ) + ReLU
  ↓
Dropout(___)
  ↓
Dense( ___ ) + Softmax
```

### Parameter count comparison
- CNN total parameters: ___________
- MLP total parameters: ___________
- CNN test accuracy: ___________
- MLP test accuracy: ___________
- **CNN improvement:** ___________ percentage points

### Reflection: parameter sharing
The first Conv2D layer has 32 filters, each 3×3, applied to 1 input channel. Compute:

`32 × 3 × 3 × 1 + 32 (biases)` = ___________ parameters

Compare to the MLP's first Dense layer:

`784 × 256 + 256 (biases)` = ___________ parameters

**Why such a huge difference?**
___________________________________________

---

## Section 4: Visualizing What CNNs Learn

### First-layer filters
Look at the 32 filter visualizations. **Pick three** and describe what kind of pattern each looks like:

1. Filter # ____ : ___________________________________________
2. Filter # ____ : ___________________________________________
3. Filter # ____ : ___________________________________________

### Feature maps
Compare Conv1 feature maps vs Conv2 feature maps:

- **Conv1 feature maps look:** ___________________________________________
- **Conv2 feature maps look:** ___________________________________________

This is the **patterns of patterns** principle. Layer 1 detects ____________; Layer 2 combines layer 1 outputs into ____________.

---

## Section 5: Misclassifications

### What classes does the model confuse?
List 3 common confusion pairs you observed:
1. ____________ ↔ ____________
2. ____________ ↔ ____________
3. ____________ ↔ ____________

### Why these confusions?
*Pick one pair and explain why the model might confuse them visually:*
___________________________________________
___________________________________________

---

## Section 6: Saving the Model

### Same pattern from Week 7 — fill in
- Save: `model.save('___________________')`
- Load: `loaded = keras.models.___________________('week8_fashion_mnist_cnn.keras')`

---

## Reflection: end of session

### What new vocabulary did you learn this week?
List 5 terms (with one-line meanings):
1. ___________: ___________________________________________
2. ___________: ___________________________________________
3. ___________: ___________________________________________
4. ___________: ___________________________________________
5. ___________: ___________________________________________

### What confused you?
*Note your top 1-2 lingering confusions. Bring them to office hours or post in the course channel.*
___________________________________________
___________________________________________

### What surprised you?
*One sentence:*
___________________________________________

### Connection to Week 7
*How is what you did today similar to / different from Week 7?*
___________________________________________
___________________________________________

### Forward to Week 9
*The instructor said next week is "transfer learning." What do you think that means? (Don't worry about being right — write your guess.)*
___________________________________________
___________________________________________

---

## Pair programming notes

**Partner's name:** ___________

### Variants we tried (note results)
| Variant | Parameters | Test Accuracy | One-line takeaway |
|---|---|---|---|
| Baseline | | | |
| Deeper | | | |
| Wider | | | |
| Larger kernel | | | |
| AvgPool | | | |

### Our winner
___________

### Our biggest learning
*What surprised your pair the most?*
___________________________________________
___________________________________________

---

## Post-class checklist

- [ ] Reviewed your live session notebook
- [ ] Started CIFAR-10 post-class exercise
- [ ] Filled in `Week8_Self_Assessment.md`
- [ ] Identified 1-2 questions to bring to next office hours
- [ ] Pre-class study guide for Week 9 already in calendar (transfer learning)

---

**Keep this workbook.** When Week 9 starts and you need to remember what you did with CNNs, this is faster to skim than the full notebook.
