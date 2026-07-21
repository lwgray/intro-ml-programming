# Week 9 — Transfer Learning & Modern Computer Vision

Week 8's CNN worked because CIFAR-10 handed you 50,000 labeled images — this week asks the question that defines real-world computer vision: **what if you only had 500?** Students borrow a MobileNetV2 backbone pretrained on ImageNet ("borrow the features, train only the decision"), freeze it, fine-tune it, and ship a ~95% five-class flower classifier on a dataset that *should* have been impossible. It's the single most-employable CV skill in the course — and the same pretrain-and-adapt idea carries straight into Week 10's transformers.

## At a Glance

| | |
|---|---|
| **Topic** | Transfer learning with pretrained CNNs: frozen-base feature extraction, fine-tuning + augmentation, and a tour of modern CV (detection, segmentation, CLIP) |
| **Datasets** | 5-class Oxford Flowers-102 subset (foxglove, passion_flower, petunia, rose, water_lily; ~500 images, loaded via PIL/NumPy) — Day 1, pair programming, from-scratch control · cats vs dogs (filtered) — Phase 2 companion notebook · CIFAR-10 & Fashion-MNIST — Day 2 domain-shift demos · your own 5-class image set — post-class |
| **Frameworks** | Keras 3.x (PyTorch backend) + `keras.applications` (MobileNetV2, ResNet50, EfficientNetB0); pretrained YOLO / DeepLabV3 / CLIP in the Day 2 and post-class playground notebooks |
| **Structure** | Pre-class (~30 min) - Day 1 live session (3 hr) - Day 1 pair programming (25 min) - Day 2 guided deep dive (90-min lecture + ~20-min notebook) - Post-class (60–90 min) |
| **Compute** | Brev GPU tier — NVIDIA L4 22 GB (T4 floor, L40S stretch); CPU fallback workable but slow (Weeks 8–11) |

## Quick Start

### Students

1. Before class: run [pre_class/pre_class.ipynb](student_materials/pre_class/pre_class.ipynb) and skim the [Pre-Class Study Guide](student_materials/pre_class/Week9_Pre_Class_Study_Guide.md) (~30 min)
2. Day 1: have [week9_live_session.ipynb](student_materials/day1_live_session/week9_live_session.ipynb) open — it's a watch-first session; you code along in [pair programming](student_materials/day1_pair_programming/week9_pair_programming.ipynb)
3. Day 2: work through the [transfer-limits guided notebook](student_materials/day2_guided_practice/week9_day2_transfer_limits_guided.ipynb)
4. After class: [fine-tune your own 5-class dataset](student_materials/post_class/week9_postclass_exercise.ipynb), then fill out the [self-assessment](student_materials/post_class/Week9_Self_Assessment.md) — including the **create-a-Hugging-Face-account checkbox** (required for Week 10)

## What Students Learn

- Why from-scratch CNNs **catastrophically overfit** on small datasets (train 100%, test ~50%) — and why the fix is to *borrow* pretrained features rather than train your own
- The pretrained ecosystem: ImageNet's "general visual vocabulary," the `keras.applications` zoo, and the three load arguments (`input_shape`, `include_top=False`, `weights='imagenet'`)
- **Phase 1 — feature extraction:** `base_model.trainable = False` (stops backprop, not the forward pass), a small `GlobalAveragePooling2D → Dense` head, and ~90% on 500 images with no overfitting
- **Phase 2 — fine-tuning craft:** unfreeze only the top ~30 layers, add flip/rotate/zoom augmentation, recompile at a **100×-lower learning rate** (1e-5), and keep `base_model(x, training=False)` — the BatchNorm inference-mode gotcha
- The #1 error of the week: forgetting `preprocess_input` — and how to read `model.summary()`'s trainable-vs-frozen parameter split
- How all of modern CV — object detection (YOLO), segmentation (U-Net / Mask R-CNN), zero-shot CLIP — sits on the same pretrained-backbone principle
- (Day 2) **Judgment**, not just recipe: what pretrained features actually are, when they stop transferring (domain shift), and how to decide how much to unfreeze

## Day 1 — Live Session (3 hours)

| Time | Segment | What happens |
|---|---|---|
| 0:00–0:15 | Segment 1 — Recap + Motivation | Week 8 building blocks carry over; the small-data hook ("what if you only had 500?"); catastrophic overfitting named |
| 0:15–0:45 | Segment 2 — Pretrained Model Ecosystem | ImageNet, the general-visual-vocabulary story, the `keras.applications` zoo, MobileNetV2 loaded live |
| 0:45–1:20 | Segment 3 — Feature Extraction vs Fine-Tuning | The mechanism: freezing stops backprop, the two regimes, the 100×-lower-LR rule, the BatchNorm gotcha |
| 1:20–1:35 | Segment 4 — Break | Students rest; instructor smoke-tests the Phase 1 build and stages the Phase 2 backup checkpoint |
| 1:35–2:00 | Segment 5 — Live Coding Phase 1: Frozen Base | The payoff: frozen-base model built and trained live to ~90% on 500 flower images |
| 2:00–2:25 | Segment 6 — Live Coding Phase 2: Fine-Tune + Augmentation | Unfreeze the top 30 layers, add augmentation, recompile at 1e-5, squeeze out the last points |
| 2:25–2:55 | Segment 7 — Modern CV Applications Tour | Detection, segmentation, CLIP zero-shot — all on pretrained backbones; the session's time-recovery valve |
| 2:55–3:00 | Segment 8 — Wrap-Up | Three-beat recap, post-class assignment, Week 10 hook — and the hard prerequisite: create a free Hugging Face account |

## Day 2 — "When It Works, When It Breaks": The Limits AND Superpowers of Transfer Learning

Day 1 taught the recipe; Day 2 turns it into judgment. One continuous 90-minute story — what pretrained features really are (a hierarchy, generic at the bottom, ImageNet-specific at the top) → when they *don't* transfer (domain shift) → a two-dial decision framework for how much to unfreeze → why augmentation saves small data → the "backbone + head" mental model that runs modern AI → the no-training superpower (CLIP zero-shot). A ~20-minute guided notebook runs four demos: visualize the features, measure close-vs-far domain shift on CIFAR-10 vs Fashion-MNIST, turn the unfreeze knob, and zero-shot with CLIP.

- Guided notebooks: [week9_day2_transfer_limits_guided.ipynb](student_materials/day2_guided_practice/week9_day2_transfer_limits_guided.ipynb) · [solutions](student_materials/day2_guided_practice/week9_day2_transfer_limits_guided_solutions.ipynb)

## Materials Map

### For Students

#### Pre-class (~30 min) — [pre_class/](student_materials/pre_class/)

- [pre_class.ipynb](student_materials/pre_class/pre_class.ipynb) — environment / dataset warm-up before the live session
- [Week9_Pre_Class_Study_Guide.md](student_materials/pre_class/Week9_Pre_Class_Study_Guide.md)

#### Day 1 live session — [day1_live_session/](student_materials/day1_live_session/)

- [week9_live_session.ipynb](student_materials/day1_live_session/week9_live_session.ipynb) — **the primary session notebook**: ecosystem tour → Phase 1 frozen base → Phase 2 fine-tune + augmentation on the 5-class flowers dataset
- [week9_from_scratch_vs_transfer.ipynb](student_materials/day1_live_session/week9_from_scratch_vs_transfer.ipynb) — the **control experiment**: same architecture, same 500 flower images, random vs pretrained weights — shows from-scratch actually failing
- [week9_live_session_phase2.ipynb](student_materials/day1_live_session/week9_live_session_phase2.ipynb) — companion: *when does fine-tuning actually help?* Uses cats vs dogs (where Phase 1 leaves headroom) to show a real, reproducible fine-tuning gain
- [Week9_Glossary.md](student_materials/day1_live_session/Week9_Glossary.md) · [Week9_Student_Workbook.md](student_materials/day1_live_session/Week9_Student_Workbook.md) · [Week9_Transfer_Learning_Cheat_Sheet.md](student_materials/day1_live_session/Week9_Transfer_Learning_Cheat_Sheet.md)
- Local data/checkpoints: `flowers/` (Oxford Flowers-102 5-class subset), `cats_and_dogs_filtered/`, `week9_flowers_finetuned.keras` (fallback checkpoint)

#### Day 1 pair programming (25 min) — [day1_pair_programming/](student_materials/day1_pair_programming/)

- [week9_pair_programming.ipynb](student_materials/day1_pair_programming/week9_pair_programming.ipynb) — compare three backbones (MobileNetV2, ResNet50, EfficientNetB0) on the same flowers dataset: accuracy vs parameters vs speed

#### Day 2 guided practice — [day2_guided_practice/](student_materials/day2_guided_practice/)

- [week9_day2_transfer_limits_guided.ipynb](student_materials/day2_guided_practice/week9_day2_transfer_limits_guided.ipynb) + [solutions](student_materials/day2_guided_practice/week9_day2_transfer_limits_guided_solutions.ipynb)

#### Post-class (60–90 min) — [post_class/](student_materials/post_class/)

- [week9_postclass_exercise.ipynb](student_materials/post_class/week9_postclass_exercise.ipynb) — apply the same Phase 1 + Phase 2 pipeline to **your own** 5-class dataset (swap the data, not the architecture) · [solutions](student_materials/post_class/week9_postclass_solutions.ipynb)
- [week9_postclass_cv_playground.ipynb](student_materials/post_class/week9_postclass_cv_playground.ipynb) — actually run YOLO detection, DeepLabV3 segmentation, and CLIP zero-shot on your own photos (no training)
- [Week9_Self_Assessment.md](student_materials/post_class/Week9_Self_Assessment.md) — reflection + the ⚠️ Hugging Face account checkbox (hard prerequisite for Week 10)

#### Student visuals — [student_materials/visuals/](student_materials/visuals/) (backbone/head diagram, frozen-vs-trainable layers, augmentation gallery, LR basin, modern CV tour, and more)

#### Reference reading

- [Appendix H — Keras Applications Reference](appendices/Appendix_H_Keras_Applications_Reference.md)

## Where This Week Fits

- **Builds on:** Week 8 — from-scratch CNNs on CIFAR-10; every building block (`Conv2D`, pooling, `Dense` head, reading curves, save/load) carries over — the only new idea is borrowing pretrained conv blocks
- **Sets up:** Week 10 — the same pretrain-and-adapt idea pointed at **text**: transformers + Hugging Face ("Attention Is All You Need"); students must create a free Hugging Face account before class
- **Course arc:** Weeks 8–11 form the deep-learning block — from-scratch CNNs (8) → transfer learning for vision (9) → transformers for text (10) → multimodal / from demo to product (11); Segment 7's CLIP demo is the deliberate bridge to Week 11
