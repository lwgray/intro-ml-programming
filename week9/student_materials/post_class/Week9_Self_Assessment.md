# Week 9 Self-Assessment

Complete after the live session AND your custom-data fine-tuning exercise.

---

## Part 1: Conceptual Understanding (1=lost, 4=could teach it)

| Statement | 1-4 |
|---|---|
| I can explain why transfer learning is the production-default for CV | |
| I understand the difference between feature extraction and fine-tuning | |
| I know why we use a low learning rate when fine-tuning (1e-5 vs 1e-3) | |
| I can explain what `preprocess_input` does and why it's model-specific | |
| I understand why we use `training=False` on the base during fine-tuning | |
| I know when to use `Flatten` vs `GlobalAveragePooling2D` | |
| I can describe how data augmentation helps with small datasets | |
| I can identify when transfer learning would NOT work well | |

---

## Part 2: Practical Skills

| Skill | Done? |
|---|---|
| Loaded a pretrained model from `keras.applications` | ☐ |
| Built a frozen-base transfer learning model | ☐ |
| Added a classifier head with `GlobalAveragePooling2D + Dropout + Dense` | ☐ |
| Used model-specific `preprocess_input` correctly | ☐ |
| Performed Phase 2 fine-tuning with low learning rate | ☐ |
| Added Keras data augmentation layers | ☐ |
| Compared multiple backbones in pair programming | ☐ |
| Fine-tuned on YOUR own dataset (post-class) | ☐ |
| **Created a Hugging Face account** (for Week 10) | ☐ |

---

## Part 3: Reflection Questions

### 1. Phase 1 vs Phase 2 results
- Live session Phase 1 (frozen): ___________
- Live session Phase 2 (fine-tuned): ___________
- Improvement: ___________

### 2. Your custom dataset
- **Dataset:** ___________ (5 classes of: ___________)
- **Training images per class:** ___________
- **Phase 1 accuracy:** ___________
- **Phase 2 accuracy:** ___________

### 3. At what training set size did accuracy plateau?
*Estimate based on your post-class experiment:*
___________________________________________

### 4. Where does your model fail?
*Look at misclassifications. List 2-3 patterns you noticed:*
1. ___________________________________________
2. ___________________________________________
3. ___________________________________________

### 5. Pair programming: best backbone choice
*For your specific dataset, which backbone won? Why?*
___________________________________________
___________________________________________

### 6. Domain shift question
*Imagine you wanted to apply transfer learning to MEDICAL X-RAY images. Would ImageNet-pretrained features still work? What would you do differently?*
___________________________________________
___________________________________________

### 7. Production deployment question
*If you were deploying your custom classifier to a mobile app, which backbone would you use? What other considerations matter for production?*
___________________________________________
___________________________________________

---

## Part 4: Forward Look

### What does "transformer" mean to you right now?
*Take a guess. Don't worry about being right.*
___________________________________________

### What's the connection between Week 9 and what's coming in Week 10?
*One sentence:*
___________________________________________

### Did you create your Hugging Face account?
☐ Yes — username: ___________
☐ Not yet — **do this before Week 10!**

---

## Part 5: Self-Score

Add up your conceptual scores from Part 1 (max 32):
- 28-32: Solid — ready for Week 10
- 22-27: Mostly there — review Glossary and Cheat Sheet
- 16-21: Some gaps — re-watch the Keras transfer learning guide
- < 16: Schedule office hours

**My score:** ___________ / 32

---

## Continued Resources

- **Keras transfer learning guide:** https://keras.io/guides/transfer_learning/
- **CS231n transfer learning notes:** https://cs231n.github.io/transfer-learning/
- **Modern CV tour videos:** Search YouTube for "YOLO explained," "U-Net explained," "CLIP explained"

---

**See you in Week 10. The framework changes — Hugging Face takes over for transformers.**
