# Week 8 — Computer Vision with Convolutional Neural Networks

In 2012, one submission dropped ImageNet's error rate from 26% to 15% and started the modern deep-learning era. This week students build that idea for themselves: a CNN that beats last week's MLP on the same Fashion-MNIST data at a **matched ~110K parameter budget** — proof of the week's headline thesis, *"it's the architecture that wins, not the size."* Then they open the network up, plot the filters it invented on its own, and leave primed for transfer learning in Week 9.

## At a Glance

| | |
|---|---|
| **Topic** | Convolutional neural networks — convolution, pooling, architecture over size, seeing what CNNs learn |
| **Datasets** | Fashion-MNIST (Day 1 live session, pair programming, Day 2), CIFAR-10 (post-class) |
| **Frameworks** | Keras 3.x on the PyTorch backend, NumPy, Matplotlib |
| **Structure** | Pre-class (~30 min) - Day 1 live session (3 hr) - Day 2 deep dive (90-min lecture + 20-min guided notebook) - Post-class (CIFAR-10 exercise + self-assessment) |
| **Compute** | Brev GPU tier — NVIDIA L4 22 GB (T4 floor, L40S stretch); CPU fallback workable but slow (Weeks 8–11) |

### Key numbers to have on a sticky note

| Number | What it is |
|---|---|
| 26% → 15% | ImageNet top-5 error, pre-2012 best → AlexNet 2012 — the week's hook |
| ~89% | The Week 7 MLP baseline on Fashion-MNIST |
| ~88% → ~91% | MLP vs CNN in the live head-to-head, same data |
| ~110K | The matched parameter budget (CNN: 110,634) — same budget, smarter spending |
| 9,568 vs 101,066 | Where the CNN's parameters live: conv layers vs the Flatten head (~91% of the model) |
| 32 | First-layer filters students plot in Segment 6 |
| 75%+ | The realistic CIFAR-10 post-class target — not 92% |

### Compute notes

- Day 1 Fashion-MNIST work is workable on CPU (the CNN trains in a few minutes vs ~30 s on GPU).
- The **CIFAR-10 post-class requires GPU** — color images triple the input; make sure students can reach the Brev platform before they start.
- Pretrained `.keras` checkpoints ship in `day1_live_session/` as the fallback if live training misbehaves.

## What Students Learn

- Why a plain MLP is structurally wrong for images — the parameter explosion *and* the loss of spatial structure lost by flattening to 784 numbers
- Convolution as a small filter of shared weights sliding over the image — one 3×3 filter (9 weights) reused everywhere, producing one feature map per filter
- Max pooling as downsizing that buys translation invariance, and the canonical Conv → ReLU → Pool pattern learning "patterns of patterns" (edges → shapes → parts)
- The full Keras workflow carries over from Week 7 unchanged — `Sequential`, `Dense`, `Dropout`, `EarlyStopping`, save/load — with exactly one new layer type: `Conv2D` (plus the 4D channel-dimension gotcha, `np.expand_dims(X, -1)`)
- The week's headline result: the CNN beats the Week 7 MLP (~88% → ~91%) on the same data at a matched ~110K parameter count — architecture, not size
- CNNs are not black boxes — students plot the 32 learned first-layer filters and feature maps, and inspect misclassifications (T-shirt ↔ Shirt)
- Architecture judgment from experiment: deeper/wider/bigger-kernel variants are *not* automatically better; the params-vs-accuracy tradeoff decides what you'd ship
- The five landmark architectures by name (LeNet, AlexNet, VGG, ResNet, EfficientNet) and the 2012 ImageNet inflection point behind them

## Day 1 — Live Session (3 hours)

| Time | Segment | What happens |
|---|---|---|
| 0:00–0:15 | Segment 1 — Recap + Motivation | Week 7 check-in; every Keras pattern carries over, one new thing (`Conv2D`); the 26%→15% teaser; today's four-part promise |
| 0:15–0:45 | Segment 2 — The ImageNet 2012 Moment | The AlexNet story; why MLPs explode on images; parameter sharing; the landmark-architecture tour |
| 0:45–1:15 | Segment 3 — Convolution & Pooling Intuition | CNN Explorer live in the browser; filters → feature maps; `Conv2D`/`MaxPooling2D` syntax preview; the channel-dimension gotcha |
| 1:15–1:30 | Segment 4 — Break | Students rest; instructor de-risks live training and pre-loads visualization fallbacks |
| 1:30–2:10 | Segment 5 — Live Coding: CNN on Fashion-MNIST | Retrain the MLP baseline, build the CNN, train it live, and beat the MLP (~88% → ~91%) at a matched ~110K params |
| 2:10–2:30 | Segment 6 — Visualizing What CNNs Learn | The "wow" moment: plot the 32 learned filters and feature maps; inspect a misclassification |
| 2:30–2:55 | Segment 7 — Pair Programming: Architecture Tour | Pairs run and compare 5 CNN variants (baseline, deeper, wider, kernels, pooling) and argue about which to ship |
| 2:55–3:00 | Segment 8 — Wrap-up | Four-point recap; CIFAR-10 post-class (needs GPU); the "60,000 vs 200 images" transfer-learning hook for Week 9 |

## Day 2 — "Becoming the Architect": How Real CNNs Are Designed

A 90-minute whiteboard-driven story plus a 20-minute guided notebook. One continuous chain of problems — *build a block → shape the net → finish it (the head) → stabilize training → go deep → stay cheap → the famous blueprints* — with two honesty rules: Parts 1–4 are code-it-yourself, Parts 5–7 are recognize-and-understand (Week 9 uses them), and no magic numbers (Global Average Pooling is taught as the real, slightly messy tradeoff it is).

- Guided notebooks: [week8_day2_architecture_guided.ipynb](student_materials/day2_guided_practice/week8_day2_architecture_guided.ipynb) - [solutions](student_materials/day2_guided_practice/week8_day2_architecture_guided_solutions.ipynb)

## Materials Map

### For Students

#### Pre-class (~30 min)

- [Week8_Pre_Class_Study_Guide.md](student_materials/pre_class/Week8_Pre_Class_Study_Guide.md) ([PDF](student_materials/pre_class/Week8_Pre_Class_Study_Guide.pdf))

#### Day 1 — live session

- [week8_live_session.ipynb](student_materials/day1_live_session/week8_live_session.ipynb) — the primary notebook for the build, training, and visualization
- [Week8_Student_Workbook.md](student_materials/day1_live_session/Week8_Student_Workbook.md) - [Week8_CNN_Cheat_Sheet.md](student_materials/day1_live_session/Week8_CNN_Cheat_Sheet.md) - [Week8_Glossary.md](student_materials/day1_live_session/Week8_Glossary.md)
- Pretrained checkpoints: `week8_fashion_mnist_cnn.keras`, `week8_fashion_mnist_cnn_pretrained.keras` (fallbacks if live training fails)

#### Day 1 — pair programming

- [week8_pair_programming.ipynb](student_materials/day1_pair_programming/week8_pair_programming.ipynb) — 5 pre-scaffolded architecture variants with a `train_and_eval` helper

#### Day 2 — guided practice

- [week8_day2_architecture_guided.ipynb](student_materials/day2_guided_practice/week8_day2_architecture_guided.ipynb) and [solutions](student_materials/day2_guided_practice/week8_day2_architecture_guided_solutions.ipynb)

#### Post-class

- [week8_postclass_exercise.ipynb](student_materials/post_class/week8_postclass_exercise.ipynb) — CIFAR-10, target 75%+, **needs GPU** ([solutions](student_materials/post_class/week8_postclass_solutions.ipynb))
- [Week8_Self_Assessment.md](student_materials/post_class/Week8_Self_Assessment.md) — 2–3 sentence reflection, not graded

#### Visuals

- [student_materials/visuals/](student_materials/visuals/) — convolution animation, pooling/receptive-field explainers, architecture diagrams, and interactive HTML explorations

#### Reference reading

- [Appendix G — CNN Architecture Reference](appendices/Appendix_G_CNN_Architecture_Reference.md)

## Where This Week Fits

- **Builds on:** Week 7 — the MLP on Fashion-MNIST (~89%) and the full Keras workflow (`Sequential`, `Dropout`, `EarlyStopping`, curves, save/load), all of which carries over unchanged
- **Sets up:** Week 9 — transfer learning: today you trained on 60,000 labeled images, but most real problems have ~200, so you'll adapt a model someone else trained on millions
