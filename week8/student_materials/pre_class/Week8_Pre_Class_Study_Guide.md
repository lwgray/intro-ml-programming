# Week 8 Pre-Class Study Guide
## Computer Vision with Convolutional Neural Networks

**Time required:** 30 minutes
**Goal:** Arrive at class with intuition for what convolution does and why CNNs exist

---

## Where you are in the course

| Week | What you learned | Connection to Week 8 |
|---|---|---|
| 1-5 | Classical ML, sklearn pipelines, evaluation | Same eval discipline (train/val/test, metrics) applies |
| 6 | Built your first MLP with Keras Sequential | Same `compile/fit/evaluate` API today |
| 7 | Dropout, EarlyStopping, model.save | All callbacks and persistence carry over |
| **8** | **CNNs — your first architecture designed for the data** | **NEW: Conv2D, MaxPooling2D, spatial structure** |

In Week 7 you got ~89% on Fashion-MNIST with an MLP. Today you'll beat that with a CNN — and understand WHY it beats it.

---

## What to do (30 minutes)

### Part 1: Watch one video (15 minutes)

**3Blue1Brown — But what is a Convolution?**
https://www.youtube.com/watch?v=KuXjwB4LzSA

Watch through the image-processing section (~10-15 min mark). You can stop when it gets to Fourier transforms — that part is not needed for class.

**While watching, look for:**
- A small "filter" (also called kernel) sliding across an image
- The dot product computation at each position
- How the output is a new "image" (called a feature map)
- The intuition that each filter detects ONE specific local pattern

### Part 2: Play with CNN Explainer (10 minutes)

**Poloclub CNN Explainer:** https://poloclub.github.io/cnn-explainer/

This is an interactive in-browser visualization of a CNN classifying real images.

**Tasks while exploring:**
1. Click on any neuron in the first conv layer — see the kernel that was learned
2. Hover over the feature maps in different layers — observe how detail changes from layer to layer
3. Try a different input image (top-left dropdown) — see how the same filters produce different feature maps
4. Notice that the deeper layers have smaller spatial resolution but more channels

### Part 3: Light reading (5 minutes)

**Optional refresher:** If your Week 7 understanding of "neural network learns by adjusting weights to minimize loss" is shaky, re-watch the first 5 minutes of [3Blue1Brown — Gradient Descent](https://www.youtube.com/watch?v=IHZwWFHWa-w).

---

## Concepts to arrive with

By the time you log in for live class, you should be able to answer:

### Q1: Why don't MLPs work well on images?
**Answer to anchor on:** MLPs flatten an image into one long vector of pixel values. They have no awareness that pixel (5, 5) is next to pixel (5, 6). They also need a parameter for every input-pixel-to-neuron connection, which is wasteful when nearby pixels are highly correlated.

### Q2: What does a single convolution filter do?
**Answer to anchor on:** A filter (e.g., 3×3 weights) slides across the image. At each position, it computes the dot product of the filter with the underlying image patch. High values mean "this filter's pattern was detected here." The output is a 2D feature map showing where the filter's pattern occurred in the input.

### Q3: What is pooling?
**Answer to anchor on:** Pooling downsamples the feature map. Max pooling takes the maximum value in each small region (e.g., 2×2). It encodes "I don't care WHERE in this region — only WHETHER the pattern was there." This makes the network roughly translation-invariant.

### Q4: What is "parameter sharing"?
**Answer to anchor on:** The same filter is applied at every spatial position in the image. Instead of learning separate weights for each location (like an MLP would), the filter shares weights across positions. One 3×3 filter has 9 weights and can be applied to any size image. This makes CNNs very parameter-efficient.

### Q5: Why use multiple layers?
**Answer to anchor on:** Each conv layer combines outputs of the previous layer. Layer 1 detects edges; layer 2 combines edges into textures; layer 3 combines textures into parts; layer 4 combines parts into objects. Stacking creates a hierarchy of increasingly complex features.

---

## What you'll do in class

1. **Recap:** Quick reminder of where Week 7's MLP topped out on Fashion-MNIST (~89% accuracy)
2. **Story:** The 2012 ImageNet moment — when CNNs cut error rates in half overnight
3. **Whiteboard:** Convolution and pooling intuition with hand-worked examples
4. **Live coding:** Build a CNN, train it on Fashion-MNIST, compare to your Week 7 MLP
5. **Visualization:** Plot what the network's filters learned to detect
6. **Pair programming:** Try architecture variants (deeper, wider, different kernel sizes)
7. **Wrap-up:** Foreshadow Week 9 (transfer learning) — what if you only have 200 images?

---

## Common student questions before class

**"Do I need to know the math behind convolution?"**
No. You need to understand what the filter does (slides + dot product) and what it produces (a feature map). The actual gradient computation is handled by Keras.

**"Why are we still using Keras instead of switching to PyTorch directly?"**
Same reason as Weeks 6-7: Keras lets you focus on architecture and concepts. PyTorch runs underneath. We're in the dominant ecosystem.

**"Will my laptop be fast enough?"**
For Fashion-MNIST: yes (CPU works in under a minute per epoch). For the post-class CIFAR-10 extension: GPU helps a lot. Class will use the course-provided GPU compute platform.

**"How is this different from Week 7?"**
Week 7 made MLPs train better (Dropout, EarlyStopping). Week 8 introduces a fundamentally DIFFERENT kind of layer (Conv2D) designed specifically for spatial data. Same Keras API, new building blocks.

---

## Things you absolutely cannot skip

- **Watching the 3B1B convolution video.** If you skip nothing else, watch this. Class will assume the visual intuition.
- **Playing with CNN Explainer for 5+ minutes.** Reading about CNNs is not the same as seeing one work.

---

## Optional: deeper reading

If you finish the assigned material early and want more:

- **StatQuest CNN Part 1:** https://www.youtube.com/watch?v=HGwBXDKFk9I (you may have watched this for Week 7 — re-watching helps)
- **Stanford CS231n Lecture 5 — Convolutional Neural Networks:** https://www.youtube.com/watch?v=bNb2fEVKeEo (advanced; very detailed)
- **A historical note: AlexNet (2012)** — the paper that started the CNN revolution: https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks (skim only — math is dense)

---

## Pre-class checklist

Before class starts, confirm:

- [ ] Watched the 3B1B convolution video
- [ ] Spent 10+ minutes with CNN Explainer
- [ ] Can explain (in plain English) what a conv filter does
- [ ] Have your dev environment from Week 7 still working (`import keras` succeeds)
- [ ] Verified GPU access on the course-provided platform (instructor will share access details)

---

**See you in class.** Bring your Week 7 questions about overfitting/regularization too — Dropout shows up again in Week 8 architectures.
