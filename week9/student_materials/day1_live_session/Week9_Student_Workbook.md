# Week 9 Student Workbook

Use alongside `week9_live_session.ipynb`. Fill in the blanks as you go.

---

## Setup

**Date:** ___________
**My GPU compute platform:** ___________
**Phase 2 training time:** ___________ (will fill during class)

---

## Section 1: Pretrained Model Tour

### What does `keras.applications` provide?
*One sentence:*
___________________________________________

### Why is `include_top=False`?
___________________________________________

### What does ImageNet pretraining "know"?
*Layer 1 detects:* ___________
*Layer 2 detects:* ___________
*Layer 3 detects:* ___________
*Top layers detect:* ___________

---

## Section 2: Dataset

**Number of classes:** ___________
**Total training images:** ___________
**Images per class:** ___________

### Why is this much smaller than Fashion-MNIST?
*One sentence — what real-world situation does this simulate?*
___________________________________________

---

## Section 3: Phase 1 — Frozen Base

### Architecture (fill in)
```
Input (160, 160, 3)
  ↓
preprocess_input (model-specific normalization)
  ↓
MobileNetV2 base [FROZEN] — ___________ parameters
  ↓
GlobalAveragePooling2D
  ↓
Dropout(___)
  ↓
Dense(___, activation='___') — TRAINABLE
```

### Parameter breakdown
- Total params: ___________
- Trainable params (head only): ___________
- Non-trainable (frozen base): ___________

### Why so few trainable parameters?
*One sentence:*
___________________________________________

### Phase 1 test accuracy: ___________

### Compare to from-scratch CNN
*If you trained the Week 8 CNN from scratch on these 500 images, what would happen?*
___________________________________________

---

## Section 4: Phase 2 — Fine-Tuning + Augmentation

### What changed
**Unfroze:** ___________ layers (out of how many?)
**Learning rate:** ___________ (compare to default ___________)
**Why low LR?** ___________________________________________

### Augmentation layers added
- ___________
- ___________
- ___________

### Why does augmentation help here?
*One sentence:*
___________________________________________

### Phase 2 test accuracy: ___________

### Improvement over Phase 1: ___________ percentage points

---

## Section 5: Modern CV Applications Tour

### Object detection
*What's the input?* ___________
*What's the output?* ___________
*Library to use:* ___________

### Segmentation
*What's the input?* ___________
*What's the output?* ___________
*Library to use:* ___________

### CLIP
*What does CLIP do?* ___________________________________________
*Why is it special?* ___________________________________________

---

## Reflection

### What new vocabulary did you learn?
1. ___________ : ___________________________________________
2. ___________ : ___________________________________________
3. ___________ : ___________________________________________
4. ___________ : ___________________________________________
5. ___________ : ___________________________________________

### What surprised you?
*One sentence:*
___________________________________________

### Connection to Week 8
*How is what you did today similar to / different from Week 8?*
___________________________________________
___________________________________________

### Foreshadow Week 10
*Next week: same idea (pretrained models) but for text. What's your prediction about how it will be different?*
___________________________________________

---

## Pair Programming Notes

**Partner:** ___________

### Backbones tried
| Backbone | Total Params | Test Acc | Train Time | Inference Time |
|---|---|---|---|---|
| MobileNetV2 | | | | |
| ResNet50 | | | | |
| EfficientNetB0 | | | | |

### Our pick for...
- Mobile deployment: ___________
- Server: ___________
- Research / experimentation: ___________

### Biggest learning from pair programming
___________________________________________

---

## Post-class checklist

- [ ] Live session notebook reviewed
- [ ] Started custom-data fine-tuning exercise
- [ ] Self-assessment filled in
- [ ] **Hugging Face account created** (needed for Week 10)
- [ ] Identified 1-2 questions for next office hours

---

**See you in Week 10. The framework changes — Hugging Face takes over for transformers — but the pretrained-model pattern stays.**
