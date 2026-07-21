# Week 6 — Neural Network Fundamentals with Keras

This is the pivot week of the course: after five weeks of traditional ML with sklearn, students enter deep learning. In one three-hour session they go from "what is a neuron?" to building and training a ~97%-accurate MNIST digit classifier in about 20 lines of Keras — the "Hello World" of deep learning. The workflow they learn here (build → compile → fit → evaluate) carries through every remaining week of the course.

## At a Glance

| &nbsp; | &nbsp; |
| --- | --- |
| **Topic** | Neural network fundamentals: neurons, layers, activations, and the Keras Sequential workflow |
| **Datasets** | MNIST handwritten digits (live demo, pair programming, homework); synthetic sklearn data (`make_classification` warm-up in the Keras intro; `make_moons` in the alternate pair notebook) |
| **Frameworks** | Keras 3 with PyTorch backend (`KERAS_BACKEND=torch`), scikit-learn, NumPy, Matplotlib |
| **Structure** | Pre-class (videos + practice) · Day 1 live session (3 hr) · Post-class homework (~30 min) — **no Day 2 for this week** |
| **Compute** | Brev CPU tier (4 vCPU / 16 GB) or any laptop — no GPU needed (Weeks 1–7) |

## Quick Start

1. Before class: work through the [Pre-Class Study Guide](student_materials/pre_class/Week6_Pre_Class_Study_Guide.md) and [week6_preclass_practice.ipynb](student_materials/pre_class/week6_preclass_practice.ipynb)
2. In class: follow along in [week6_live_session.ipynb](student_materials/live_session/week6_live_session.ipynb) with the [Keras Cheat Sheet](student_materials/live_session/Week6_Keras_Cheat_Sheet.md) at hand
3. After class: complete [week6_postclass_exercise.ipynb](student_materials/post_class/week6_postclass_exercise.ipynb)

**Environment gotcha:** the notebooks set the backend *before* importing Keras —

```python
import os
os.environ['KERAS_BACKEND'] = 'torch'
import keras  # only after the line above
```

If Keras imports with the wrong backend, restart the kernel and see the [Keras 3 Troubleshooting Guide](student_materials/Keras3_Troubleshooting_Guide.md).

## What Students Learn

- What a neural network is, from the ground up: biological neuron → artificial neuron (inputs, weights, activation) → layers → networks, and why depth enables hierarchical feature learning
- The Keras Sequential API — `Dense` layers and the build → compile → fit → evaluate workflow, and how it parallels the sklearn pattern they already know
- What Keras does behind the scenes: the training loop, backpropagation conceptually (no calculus), and why the course uses the PyTorch backend
- How to build a complete MNIST digit classifier end-to-end: load, normalize, flatten, train, evaluate, predict
- How to read `model.summary()` (parameter counts, output shapes) and training-history curves to diagnose what a model is doing
- How architecture choices (depth, neurons per layer) affect results — discovered hands-on through pair-programming experiments
- The top beginner mistakes and how to avoid them: forgetting to normalize, wrong output activation, mismatched loss function

## Day 1 — Live Session (3 hours)

| Time | Segment | What happens |
| --- | --- | --- |
| 0:00–0:15 | Segment 1 — Week 5 Recap & Welcome | Bridge from unsupervised learning to deep learning; why neural networks now; MNIST preview and expectation-setting |
| 0:15–0:50 | Segment 2 — Neural Network Concepts | Biological → artificial neuron metaphor, perceptrons, layers, why depth matters; TensorFlow Playground and MNIST samples |
| 0:50–1:20 | Segment 3 — Keras Fundamentals | Sequential API, Dense layers, compile/fit workflow; simple demo on synthetic data (`week6_keras_intro.ipynb`) |
| 1:20–1:35 | Segment 4 — Break | Recharge; informal Q&A and environment troubleshooting |
| 1:35–2:05 | Segment 5 — Under the Hood | What `model.fit()` actually does; backpropagation intuition (no calculus); why the PyTorch backend |
| 2:05–2:40 | Segment 6 — Live Coding Demo: MNIST Classifier | The main event — build, normalize, train, and evaluate a digit classifier live; interpret `model.summary()` and training curves |
| 2:40–2:55 | Segment 7 — Pair Programming: "Network Architects" | Pairs modify the MNIST architecture (layers, neurons) and compare training results |
| 2:55–3:00 | Segment 8 — Wrap-Up | Key insights, top-3 mistakes, homework, Week 7 preview |

**Dataset note:** the live demo and homework both use **MNIST** (`keras.datasets.mnist`); Fashion-MNIST comes in Week 7.

## Day 2

There are no Day 2 materials for Week 6. This week runs as a single live session plus pre/post-class work — the Day 1 / Day 2 structure used by other weeks does not apply here.

## Materials Map

### For Students

#### Pre-class — [student_materials/pre_class/](student_materials/pre_class/)

- [Week6_Pre_Class_Study_Guide.md](student_materials/pre_class/Week6_Pre_Class_Study_Guide.md) ([PDF](student_materials/pre_class/Week6_Pre_Class_Study_Guide.pdf)) — includes the 3Blue1Brown neural network videos referenced in class
- [week6_preclass_practice.ipynb](student_materials/pre_class/week6_preclass_practice.ipynb)

#### Live session — [student_materials/live_session/](student_materials/live_session/)

- [week6_keras_intro.ipynb](student_materials/live_session/week6_keras_intro.ipynb) — Segment 3 follow-along demo (synthetic data)
- [week6_live_session.ipynb](student_materials/live_session/week6_live_session.ipynb) — Segment 6 MNIST classifier, the primary notebook
- References: [Student Workbook](student_materials/live_session/Week6_Student_Workbook.md) · [Keras Cheat Sheet](student_materials/live_session/Week6_Keras_Cheat_Sheet.md) · [Glossary](student_materials/live_session/Week6_Glossary.md) · [Loss Functions](student_materials/live_session/Week6_Loss_functions.md)

#### Pair programming — [student_materials/pair_programming/](student_materials/pair_programming/)

- [week6_pair_programming.ipynb](student_materials/pair_programming/week6_pair_programming.ipynb) — "Network Architects": modify the MNIST architecture (Segment 7 primary file)
- [week6_network_architects_moons.ipynb](student_materials/pair_programming/week6_network_architects_moons.ipynb) — alternate version on `make_moons`

#### Post-class — [student_materials/post_class/](student_materials/post_class/)

- [week6_postclass_exercise.ipynb](student_materials/post_class/week6_postclass_exercise.ipynb) — scaffolded MNIST classifier homework (~30 min) · [solutions](student_materials/post_class/week6_postclass_solutions.ipynb)
- [week6_bonus_activation_exploration.ipynb](student_materials/post_class/week6_bonus_activation_exploration.ipynb) — optional: compare ReLU / tanh / sigmoid
- [Week6_Self_Assessment.md](student_materials/post_class/Week6_Self_Assessment.md)

#### Keras 3 environment guides — [student_materials/](student_materials/)

- [Keras3_Technical_Setup_Guide.md](student_materials/Keras3_Technical_Setup_Guide.md) ([PDF](student_materials/Keras3_Technical_Setup_Guide.pdf)) — environment setup for Keras 3 + PyTorch backend
- [Keras3_Troubleshooting_Guide.md](student_materials/Keras3_Troubleshooting_Guide.md) ([PDF](student_materials/Keras3_Troubleshooting_Guide.pdf)) — fixes for backend and import issues

#### Extras

- [student_materials/visuals/](student_materials/visuals/) — diagrams and interactive HTML visuals (neuron diagram, Keras workflow, MNIST samples, training history, and more)
- [Neural Network Loss + Activation Cheat Sheet (PDF)](<student_materials/Neural Network Loss + Activation Cheat Sheet.pdf>)
- [Appendix F: Keras Sequential API Guide](appendices/Appendix_F_Keras_Sequential_API_Guide.md) — reference reading

## Where This Week Fits

- **Builds on:** Week 5 — unsupervised learning (K-Means, PCA); Week 6 returns to supervised learning but trades sklearn for Keras and tabular data for images
- **Sets up:** Week 7 — best practices for production-quality networks: overfitting, dropout, early stopping, data augmentation, and Fashion-MNIST
