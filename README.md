# Introduction to Machine Learning Programming

**A 12-week practical ML course — from fitting a line through points to calling models that paint pictures and write essays.** Both are "just" minimizing a loss function with gradient descent; the course is the journey between those two sentences.

Built for **domain experts building proof-of-concept ML applications**: production-ready code over theoretical depth, intuition-first math (visual, no derivations), and the judgment to know when each tool works — and when it breaks.

---

## Course at a Glance

| | |
|---|---|
| **Audience** | Domain experts / ML Ambassador Program (ML Engineer track) — no prior ML required |
| **Length** | 12 weeks · ~4 contact hours per week |
| **Weekly rhythm** | Pre-class (~30 min) → **Day 1 live session (3 hr)** → **Day 2 guided deep dive (~1 hr)** → Post-class (~30 min) |
| **Frameworks** | sklearn (Weeks 1–5) → Keras 3.x on the PyTorch backend (Weeks 6–9) → Hugging Face `transformers` + `diffusers` (Weeks 10–11) |
| **Compute** | Weeks 1–7: Brev CPU tier (4 vCPU / 16 GB) or any laptop · Weeks 8–11: Brev GPU tier — NVIDIA L4 22 GB (T4 floor, L40S stretch); students' RTX 2000 8 GB laptops are the local fallback |
| **Accounts** | Free Hugging Face account required by Week 10; Week 11 models pre-downloaded in Week 10 post-class |

---

## The 12-Week Arc

Every week links to its own README — the front door for that week's objectives, session timeline, and materials map.

### Part I — Classical ML Fundamentals (sklearn)

| Week | Topic | Core data | Day 2 deep dive |
|---|---|---|---|
| [1](week1/README.md) | The ML Pipeline & Linear Regression | California Housing | Guided practice: Boston Housing |
| [2](week2/README.md) | Classification Fundamentals | Breast Cancer Wisconsin | Guided practice: Heart Disease |
| [3](week3/README.md) | Trees & Ensembles — the Tabular Workhorses | Adult Income | Overfitting in trees; bagging vs boosting |
| [4](week4/README.md) | Model Selection & Avoiding Pitfalls | Adult Income | Bias-variance & data leakage in production |
| [5](week5/README.md) | Unsupervised Learning — K-Means & PCA | Mall Customers + MNIST | Choosing K + PCA mathematics |

### Part II — Neural Network Foundations (Keras 3.x, PyTorch backend)

| Week | Topic | Core data | Day 2 deep dive |
|---|---|---|---|
| [6](week6/README.md) | Neural Network Fundamentals with Keras | MNIST | *(single-day week — see note below)* |
| [7](week7/README.md) | Deep Learning Best Practices | Fashion-MNIST | Bias-variance + EarlyStopping tuning (CIFAR-10) |

### Part III — The Deep Neural Networks Block (the four inflections of modern AI)

| Week | Topic · Inflection | Core data / models | Day 2 deep dive |
|---|---|---|---|
| [8](week8/README.md) | CNNs · *ImageNet 2012* | Fashion-MNIST, CIFAR-10 | "Becoming the Architect" — how real CNNs are designed |
| [9](week9/README.md) | Transfer Learning · *nobody trains from scratch* | Oxford Flowers-102 (5-class subset), MobileNetV2 | "When It Works, When It Breaks" — limits & superpowers |
| [10](week10/README.md) | Attention & Transformers · *"Attention Is All You Need" (2017)* | AG News, DistilBERT | "Inside the Transformer" — SEE attention, meet the decoder |
| [11](week11/README.md) | Generative AI · *ChatGPT + Stable Diffusion (2022)* | Phi-3-mini, Stable Diffusion 1.5 | "From Demo to Product" — composing classic + generative ML |

### Part IV — Capstone

| Week | Topic | Notes |
|---|---|---|
| 12 | GitHub Copilot Workshop | Materials are maintained **outside this repository** (existing workshop, moved from Week 8 of the old 8-week structure). |

By course end, every student has: built an end-to-end sklearn pipeline, trained and regularized neural networks, built a CNN and beaten an MLP baseline at a matched parameter budget, fine-tuned a pretrained image model on ~500 images, fine-tuned DistilBERT on text, prompted a local LLM, generated images with Stable Diffusion, and composed a classic + generative model into a tiny working app.

---

## How Each Week Folder Is Organized

The canonical layout (Weeks 1–5, 7–11):

```
weekN/
├── README.md                          ← start here
├── student_materials/
│   ├── pre_class/                     ← ~30-min primer notebook
│   ├── day1_live_session/             ← the live-coding notebook(s)
│   ├── day1_pair_programming/         ← scaffolded pair exercise (+ solutions)
│   ├── day2_guided_practice/          ← Day 2 guided notebook + solutions
│   └── post_class/                    ← ~30-min reinforcement exercise + solutions
```

---

## Compute & External Dependencies

- **Weeks 1–7** run anywhere — CPU only.
- **Weeks 8–11** assume the Brev **L4 22 GB** GPU tier. CPU works with degraded pacing everywhere except Week 11's Stable Diffusion, where GPU is effectively required.
- **Pre-downloads matter.** The heavy models (DistilBERT ~250 MB in Week 10; Phi-3-mini ~2 GB and Stable Diffusion ~4 GB for Week 11) are downloaded in the *prior* week's post-class, not on class day. Each GPU week's README and technical-setup doc carries the checklist and the fallback ladder (reduced steps → cached checkpoint → pre-generated gallery → HF Inference API).
- **Model IDs that bite:** Stable Diffusion is `sd-legacy/stable-diffusion-v1-5` (the `runwayml/` repo no longer exists), and the notebooks target **transformers v5** (several `pipeline()` shortcuts are gone; seq2seq tasks use `AutoModelForSeq2SeqLM` + `.generate()`).

---

## Maintenance Notes (June 2026)

Known drift the README pass surfaced but did not fix (source files, out of README scope):

- **Week 1:** `Segment7`/`Segment8` scripts cite a Boston pair exercise and a nonexistent `week1_postclass_exercise.ipynb`; the real notebooks are Diabetes (pair) and Auto MPG (post-class).
- **Week 3:** `Segment8` promises a Titanic homework; the real post-class notebooks are Iris and Digits.
- **Week 5:** master script says K=4 for Mall Customers, Segment 6 says K=5; segment files also cite pre-restructure `student_materials/` paths.
- **Week 6:** flat layout pending restructure; master script still references Fashion-MNIST homework (real: MNIST); zero-byte `layers.ipynb` in post_class.
- **Weeks 1–3:** sub-segment (6b/6c/6d) time headers overlap adjacent segments — the master scripts are the timing authority.

---

*Course by Dr. Lawrence Gray. Version 2.0 course design (April 2026); per-week READMEs generated from the live teaching materials, June 2026.*
