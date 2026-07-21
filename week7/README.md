# Week 7 — Deep Learning Best Practices with Keras

Week 6 was "make it work" — this week is "make it production-ready." Students learn the four skills that separate hobby projects from production systems: diagnosing overfitting from training curves, preventing it with Dropout and EarlyStopping, splitting data three ways (train/validation/test), and saving trained models for deployment. Everything is practiced live on Fashion-MNIST, then pushed further on CIFAR-10 in Day 2's guided practice.

## At a Glance

| | |
|---|---|
| **Topic** | Production practices for neural networks: overfitting diagnosis, regularization (Dropout + EarlyStopping), three-way data splits, model persistence |
| **Datasets** | Fashion-MNIST (Day 1 live session, pair programming, post-class) · CIFAR-10 (Day 2 guided practice) |
| **Frameworks** | Keras, Matplotlib (training-curve plots) |
| **Structure** | Pre-class (~30 min) · Day 1 live session (3 hr) · Day 2 guided deep dive · Post-class (~30 min) |
| **Compute** | Brev CPU tier (4 vCPU / 16 GB) or any laptop — no GPU needed (Weeks 1–7) |

## Quick Start

### Students

1. Before class: work through the [Pre-Class Study Guide](student_materials/pre_class/Week7_Pre_Class_Study_Guide.md) and [practice notebook](student_materials/pre_class/week7_preclass_practice.ipynb) (~30 min)
2. In class: follow along in [week7_live_session.ipynb](student_materials/day1_live_session/week7_live_session.ipynb) with the [Keras Cheat Sheet](student_materials/day1_live_session/Week7_Keras_Cheat_Sheet.md) at hand
3. After class: complete [week7_postclass_exercise.ipynb](student_materials/post_class/week7_postclass_exercise.ipynb) and the [Self-Assessment](student_materials/post_class/Week7_Self_Assessment.md)

## The Week in Three Metaphors

| Metaphor | Technique | The idea |
|---|---|---|
| "Overfitting Detective" | Training-curve diagnosis | The curves are your clues — spot memorization before it ships |
| "Network on a Diet" | Dropout | Random players skip practice, so the team never relies on one star |
| "Validation Alarm" | EarlyStopping | Validation loss rings the bell when it's time to stop training |

## What Students Learn

- Recognize overfitting in training-vs-validation curves and name the four patterns: healthy, beginning overfit, overfitting, underfitting (the "Overfitting Detective" skill)
- Explain *why* overfitting happens — memorization vs. generalization, and the bias-variance tradeoff behind it (Day 2)
- Implement a three-way train/validation/test split and normalize image data for neural network training
- Prevent overfitting with Dropout layers ("Network on a Diet") and know when and where to add them
- Configure the EarlyStopping callback ("Validation Alarm") — monitor, patience, `restore_best_weights` — and tune its parameters
- Save and load trained models with `model.save()` / `load_model()` so work survives the notebook
- Apply the full workflow end-to-end: diagnose a deliberately bad Fashion-MNIST model, fix it with regularization, and verify the improvement

## Day 1 — Live Session (3 hours)

| Time | Segment | What happens |
|---|---|---|
| 0:00–0:15 | Segment 1 — Week 6 Recap | Rapid-fire Keras review (Sequential, Dense, compile, fit) and preview of the four Week 7 production skills |
| 0:15–0:45 | Segment 2 — Data Pipeline & Three-Way Split | Load and visualize Fashion-MNIST; why validation sets exist; implement train/val/test split and normalization |
| 0:45–1:15 | Segment 3 — Overfitting Deep Dive | THE critical segment: read training curves like a detective and master the four curve patterns |
| 1:15–1:30 | Segment 4 — Break | 15-minute break; Training Curves Patterns visual stays up for review |
| 1:30–2:00 | Segment 5 — Regularization Techniques | Dropout ("Network on a Diet") and EarlyStopping ("Validation Alarm"): how each works and when to use it |
| 2:00–2:35 | Segment 6 — Live Coding Fashion-MNIST | Longest coding segment: build the full classifier with Dropout + EarlyStopping, plot curves, save/load, evaluate on test |
| 2:35–3:05 | Segment 7 — Pair Programming: "Regularization Detective" | Pairs diagnose an intentionally overfitting model, fix it with Dropout + EarlyStopping, and compare before/after |
| 3:05–3:10 | Segment 8 — Wrap-Up & Next Steps | Recap the four skills, homework instructions, Week 8 preview |

## Day 2 — Bias-Variance Tradeoff + EarlyStopping Parameter Tuning

Day 2 deepens two Day 1 topics: the bias-variance tradeoff (the theory behind why overfitting happens) and EarlyStopping parameter tuning (when patience matters and how to choose monitoring metrics). The 20-minute whiteboard-and-discussion deep dive favors intuition over proofs and connects directly to the training curves students saw on Day 1; the guided practice then transfers the whole workflow to CIFAR-10.

- Guided notebooks: [week7_cifar10_guided.ipynb](student_materials/day2_guided_practice/week7_cifar10_guided.ipynb) · [week7_cifar10_guided_solutions.ipynb](student_materials/day2_guided_practice/week7_cifar10_guided_solutions.ipynb)

## Materials Map

### For Students

#### Pre-class — [pre_class/](student_materials/pre_class/)

- [Week7_Pre_Class_Study_Guide.md](student_materials/pre_class/Week7_Pre_Class_Study_Guide.md) (also as [PDF](student_materials/pre_class/Week7_Pre_Class_Study_Guide.pdf))
- [week7_preclass_practice.ipynb](student_materials/pre_class/week7_preclass_practice.ipynb)
- [Architecture Evolution module](student_materials/pre_class/architecture_evolution/README_MODULE.md) — study guide, decision framework, further reading

#### Day 1 live session — [day1_live_session/](student_materials/day1_live_session/)

- [week7_live_session.ipynb](student_materials/day1_live_session/week7_live_session.ipynb) — the notebook students execute along with Segments 2–6
- [Week7_Student_Workbook.md](student_materials/day1_live_session/Week7_Student_Workbook.md)
- [Week7_Keras_Cheat_Sheet.md](student_materials/day1_live_session/Week7_Keras_Cheat_Sheet.md)
- [Week7_Glossary.md](student_materials/day1_live_session/Week7_Glossary.md)

#### Day 1 pair programming — [day1_pair_programming/](student_materials/day1_pair_programming/)

- [week7_pair_programming.ipynb](student_materials/day1_pair_programming/week7_pair_programming.ipynb) — the "Regularization Detective" exercise

#### Day 2 guided practice — [day2_guided_practice/](student_materials/day2_guided_practice/)

- [week7_cifar10_guided.ipynb](student_materials/day2_guided_practice/week7_cifar10_guided.ipynb) + [solutions](student_materials/day2_guided_practice/week7_cifar10_guided_solutions.ipynb)

#### Post-class — [post_class/](student_materials/post_class/)

- [week7_postclass_exercise.ipynb](student_materials/post_class/week7_postclass_exercise.ipynb) (~30 min) + [solutions](student_materials/post_class/week7_postclass_solutions.ipynb)
- [week7_bonus_architecture_experiments.ipynb](student_materials/post_class/week7_bonus_architecture_experiments.ipynb) (optional)
- [Week7_Self_Assessment.md](student_materials/post_class/Week7_Self_Assessment.md)
- [Week7_Training_Curves_Interpretation_Guide.md](student_materials/post_class/Week7_Training_Curves_Interpretation_Guide.md) — the go-to reference when stuck on curve patterns

#### Visuals — [visuals/](student_materials/visuals/)

Training curve patterns, dropout diagram, early stopping flowchart, three-way split, and more

#### Reference reading

- [Appendix F — Model Saving & Loading Guide](appendices/Appendix_F_Model_Saving_Loading_Guide.md)

## Where This Week Fits

- **Builds on:** Week 6 — building and training neural networks with Keras on MNIST (Sequential, Dense, compile, fit)
- **Sets up:** Week 8 — Computer Vision with Convolutional Neural Networks: a CNN beats this week's MLP on the same Fashion-MNIST data at a matched ~110K parameter budget, reusing Week 7's production skills (Dropout, EarlyStopping, three-way splits)
