# Week 8 Self-Assessment

Complete this after finishing the live session AND the post-class CIFAR-10 exercise. Honest answers help you (and your instructor) identify gaps.

---

## Part 1: Conceptual Understanding

For each statement, mark your level: 1 (lost) | 2 (shaky) | 3 (solid) | 4 (could teach it)

| Statement | Level (1-4) |
|---|---|
| I can explain why MLPs are inefficient on images | |
| I understand what a convolution filter does (slides + dot product) | |
| I can describe what pooling does and why we use it | |
| I understand parameter sharing and why it matters | |
| I can explain the "patterns of patterns" hierarchy across CNN layers | |
| I know the canonical CNN architecture (Conv → Pool → ... → Flatten → Dense) | |
| I understand the difference between `padding='same'` and `padding='valid'` | |
| I can read `model.summary()` and understand the parameter counts | |

If anything is at level 1 or 2, **review** before moving to Week 9. The Glossary, Cheat Sheet, and pre-class study guide are good places to start.

---

## Part 2: Practical Skills

For each, did you do it?

| Skill | Done? |
|---|---|
| Built a CNN from scratch in Keras | ☐ |
| Trained on Fashion-MNIST and beat the Week 7 MLP baseline | ☐ |
| Visualized first-layer filters | ☐ |
| Visualized feature maps for one image | ☐ |
| Inspected misclassifications | ☐ |
| Saved and loaded a CNN | ☐ |
| Tried at least 3 architecture variants in pair programming | ☐ |
| Trained a CNN on CIFAR-10 (post-class exercise) | ☐ |
| Compared Fashion-MNIST and CIFAR-10 difficulty | ☐ |

---

## Part 3: Reflection Questions

### 1. What test accuracy did you achieve?
- Live session CNN on Fashion-MNIST: ___________
- Post-class CNN on CIFAR-10: ___________

### 2. CIFAR-10 was harder. Why?
*Write 2-3 sentences. Consider: visual complexity, intra-class variation, color, image resolution.*

___________________________________________
___________________________________________
___________________________________________

### 3. Did your CIFAR-10 model overfit?
*Look at the training curves you generated. If yes, how could you tell? If no, what would overfitting look like?*

___________________________________________
___________________________________________

### 4. The deepest variant in pair programming
*Did adding a third Conv block help on Fashion-MNIST? Why or why not?*

___________________________________________
___________________________________________

### 5. If you had only 200 CIFAR-10 images
*Predict what would happen if you trained your CNN on only 200 images per class instead of the full 5,000. Don't run the experiment — just predict.*

___________________________________________
___________________________________________

*This is the question Week 9 will answer. Hold onto your prediction.*

### 6. What surprised you most this week?
*One sentence:*

___________________________________________

### 7. What's still unclear?
*List 1-2 things you want to revisit. Bring them to office hours or post in the channel.*

1. ___________________________________________
2. ___________________________________________

---

## Part 4: Architecture Tradeoffs (Pair Programming)

Fill in your variant comparison table from `week8_pair_programming.ipynb`:

| Variant | Parameters | Test Accuracy | Notes |
|---|---|---|---|
| Baseline | | | |
| Deeper | | | |
| Wider | | | |
| 5×5 kernels | | | |
| Avg pooling | | | |

### Which variant gave the best parameters-per-accuracy tradeoff?
___________________________________________

### Which variant did you NOT expect to perform well that did?
___________________________________________

### Which variant did you expect to perform well that didn't?
___________________________________________

---

## Part 5: Forward Look

### What do you predict "transfer learning" means?
*Take a guess (don't worry about being right):*
___________________________________________

### What's the first thing you'll try in Week 9?
___________________________________________

---

## Self-Score

Add up your conceptual scores from Part 1 (max 32 points):
- 28-32: Solid foundation — you're ready for Week 9
- 22-27: Mostly there — review the Glossary and Cheat Sheet
- 16-21: Some gaps — re-watch the pre-class video and re-run the live session notebook
- < 16: Schedule office hours or pair with a classmate to walk through the basics again

**My score:** ___________ / 32

---

## Submission

Save this filled-in workbook as `Week8_Self_Assessment_<your_name>.md` and submit per course instructions (or just keep it for yourself if no formal submission required).

The reflection is the most valuable part — even if no one reads it, writing it makes the material stick.

---

**See you in Week 9. Pretrained models await.**
