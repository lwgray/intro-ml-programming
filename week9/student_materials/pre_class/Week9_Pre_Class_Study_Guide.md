# Week 9 Pre-Class Study Guide
## Transfer Learning & Modern Computer Vision

**Time required:** 30 minutes
**Goal:** Arrive understanding why transfer learning is the production-default for CV

---

## Where you are in the course

| Week | What you learned | Connection to Week 9 |
|---|---|---|
| 7 | Dropout, EarlyStopping, model.save | All callbacks reused today |
| 8 | CNN architecture from scratch | Today: someone ELSE's pretrained CNN |
| **9** | **Transfer learning — the production pattern** | **NEW: keras.applications, fine-tuning** |

Last week you trained a CNN on 60K images. Today's question: what if you only have 500?

---

## What to do (30 minutes)

### Part 1: Try Teachable Machine (10 minutes)

**Google Teachable Machine:** https://teachablemachine.withgoogle.com/

This is the magic of transfer learning, made interactive. Anyone can train an image classifier in 2 minutes.

**Tasks:**
1. Click "Get started" → "Image Project" → "Standard image model"
2. Use your webcam (or upload images) to create 3-4 classes — could be hand poses, household objects, or anything visually distinct
3. Click "Train Model"
4. Click "Preview" and test your model live

**Notice:** Did you provide thousands of training images? No — probably 30-50 per class. And it works. **That's transfer learning.** Behind the scenes, Teachable Machine is using a pretrained model and just training a new classifier head on your data.

### Part 2: Read the Keras Transfer Learning guide intro (10 minutes)

**Keras guide:** https://keras.io/guides/transfer_learning/

Read the introduction and "The typical transfer-learning workflow" sections. Skip the code details — focus on the conceptual workflow.

**Key concepts to extract:**
- What does "freezing" a layer mean?
- What's the difference between feature extraction and fine-tuning?
- Why use a low learning rate when fine-tuning?

### Part 3: Watch a transfer learning explainer (10 minutes)

Any one of:
- Andrew Ng's transfer learning lecture (~10 min): https://www.youtube.com/watch?v=yofjFQddwHE
- Sentdex transfer learning intro
- DeepLearning.AI transfer learning short

**While watching, listen for:**
- Why we don't usually train from scratch
- The relationship between source task and target task
- When transfer learning works well vs poorly

---

## Concepts to arrive with

By the time you log in for live class, you should be able to answer:

### Q1: What does it mean to "freeze" a layer?
**Answer:** Setting `layer.trainable = False` so its weights don't update during training. Forward pass still happens — the layer still computes its output — but backprop doesn't change its weights.

### Q2: Why does transfer learning work?
**Answer:** A model trained on a large dataset (ImageNet, 1.4M images) has learned a general visual vocabulary — edges, textures, shapes, object parts. Most of that vocabulary is useful for ANY image classification task. We only need to train a new classifier on top of those features for our specific classes.

### Q3: What's the difference between "feature extraction" and "fine-tuning"?
**Answer:**
- **Feature extraction:** Freeze the entire pretrained base. Train ONLY a new classifier head. Fast, works with very small data.
- **Fine-tuning:** Also unfreeze the TOP layers of the base and train them with a low learning rate. Slower, needs slightly more data, can yield higher accuracy.

### Q4: When would transfer learning NOT work well?
**Answer:** When your target domain is very different from the source domain. ImageNet-pretrained models work great on natural photos; less well on medical X-rays, satellite imagery, or microscope images. The features the base learned might not transfer.

### Q5: What's `keras.applications`?
**Answer:** A Keras module containing dozens of CNN architectures pretrained on ImageNet — MobileNetV2, ResNet50, VGG16, EfficientNet, etc. You can load any of them with `keras.applications.MobileNetV2(weights='imagenet')`.

---

## What you'll do in class

1. **Recap:** Quick review of Week 8 CNN, set up the "small data" problem
2. **Tour:** keras.applications ecosystem; the foundation model concept
3. **Theory:** Feature extraction vs fine-tuning; when to use each
4. **Live coding Phase 1:** Frozen-base transfer learning on 5-class flowers (~30 sec on GPU)
5. **Live coding Phase 2:** Unfreeze + fine-tune + augmentation (~3 min on GPU)
6. **Concept tour:** Object detection, segmentation, CLIP
7. **Wrap-up:** Foreshadow Week 10 (transformers + Hugging Face)

---

## Common student questions before class

**"Will I need to download a big pretrained model?"**
Yes — MobileNetV2 weights are ~14MB. The download happens automatically on first use.

**"Can I use my own dataset?"**
For class, we use a pre-bundled flowers dataset. For post-class, you'll fine-tune on your own data. Save photos in folders by class (one folder per class).

**"What if I don't have GPU access?"**
Phase 1 (frozen base) works fine on CPU — only the small head trains. Phase 2 (fine-tuning) is significantly slower on CPU; we'll do that on the GPU platform during class.

**"Why are we still using Keras for this when transformers use Hugging Face?"**
For images, Keras + `keras.applications` is the cleanest API. Hugging Face also has CV models, but `keras.applications` is more idiomatic for our setup. Next week (Week 10), we switch frameworks for transformers.

---

## Things you absolutely cannot skip

- **Trying Teachable Machine.** 5 minutes. Feel the magic before you understand the mechanism.
- **Skimming the Keras transfer learning guide.** The vocabulary will be important during class.

---

## Optional: deeper reading

- **The original VGG paper** (skim Table 1 — the famous column-per-network architecture comparison): <https://arxiv.org/abs/1409.1556> — for the beautiful 3D architecture diagram everyone associates with VGG16, see this blog post: <https://www.cs.toronto.edu/~frossard/post/vgg16/>
- **Stanford CS231n notes on transfer learning:** https://cs231n.github.io/transfer-learning/
- **A practical guide to data augmentation:** https://github.com/aleju/imgaug

---

## Pre-class checklist

- [ ] Played with Teachable Machine for 5+ minutes
- [ ] Skimmed the Keras transfer learning guide intro
- [ ] Watched at least one transfer learning explainer video
- [ ] Can explain (in plain English) what "freezing" does
- [ ] Have your dev environment from Week 8 still working
- [ ] Verified GPU access on the course-provided platform

---

**Looking ahead to Week 10:** Pre-class for Week 10 will require a free Hugging Face account. **Sign up now at** https://huggingface.co — takes 2 minutes, free, no credit card.

See you in class.
