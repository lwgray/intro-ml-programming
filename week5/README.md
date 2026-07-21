# Week 5 — Unsupervised Learning: K-Means & PCA

Welcome to the midpoint of the course — and a genuine paradigm shift. Weeks 1–4 were supervised learning: features **and** labels, predict y, check accuracy. This week the labels disappear, and the algorithms discover structure on their own: K-Means finds natural customer segments, and PCA compresses 64-dimensional handwritten digits down to a 2D picture you can actually see. The week's defining skill is interpretation — evaluating and explaining results when there is no ground truth to check against.

## At a Glance

| | |
| --- | --- |
| **Topic** | Unsupervised learning: K-Means clustering & PCA dimensionality reduction |
| **Datasets** | Mall Customers (K-Means segmentation), sklearn digits (PCA 64D → 2D — `load_digits`, not full MNIST), Wine (pair programming and Day 2), Iris (homework) |
| **Frameworks** | scikit-learn, pandas, NumPy, matplotlib/seaborn (plus Yellowbrick for cluster visuals) |
| **Structure** | Pre-class (~30 min) - Day 1 live session (3 hr) - Day 2 guided deep dive - Post-class exercise (~90–120 min) |
| **Compute** | Brev CPU tier (4 vCPU / 16 GB) or any laptop — no GPU needed (Weeks 1–7) |

## Quick Start

### Students — your path through the week

1. Before Day 1: read the [Pre-Class Study Guide](student_materials/pre_class/Week5_Pre_Class_Study_Guide.md) and run the [pre-class practice notebook](student_materials/pre_class/week5_preclass_practice.ipynb)
2. Day 1: follow along in [`week5_live_session_kmeans.ipynb`](student_materials/day1_live_session/week5_live_session_kmeans.ipynb) and [`week5_live_session_pca.ipynb`](student_materials/day1_live_session/week5_live_session_pca.ipynb), then pair up for the ["Cluster Detective"](student_materials/day1_pair_programming/week5_pair_programming.ipynb)
3. Day 2: work through the [Wine guided notebook](student_materials/day2_guided_practice/week5_wine_guided.ipynb)
4. After class: complete the [homework notebook](student_materials/post_class/week5_postclass_exercise.ipynb) and the [self-assessment](student_materials/post_class/Week5_Self_Assessment.md)

## What Students Learn

- Articulate the difference between supervised and unsupervised learning, and spot scenarios where unsupervised is the **only** option (no labels exist)
- Understand K-Means intuitively — Initialize → Assign → Update → Repeat — including k-means++ initialization and the algorithm's limitations (spherical clusters, outlier sensitivity, K chosen upfront)
- Choose the number of clusters using the elbow method, silhouette score, and business judgment — and handle the case where they disagree
- Build PCA intuition ("directions of maximum variance") and its three main use cases: visualization, preprocessing, compression
- Interpret explained variance ratios and scree plots to decide how many components to keep
- Always scale features before K-Means and PCA — distance-based methods break without it
- Interpret clusters without ground truth: translate technical output into business-friendly segment names and actionable insights

## Day 1 — Live Session (3 hours)

| Time | Segment | What happens |
| --- | --- | --- |
| 0:00–0:15 | Segment 1 — Week 4 Recap & Welcome | Recap validation methodology, introduce the "no labels" paradigm shift, preview today's two datasets |
| 0:15–0:35 | Segment 2 — Unsupervised vs Supervised | THE foundational moment: when unsupervised is the only option; customer-segmentation metaphor for the week |
| 0:35–1:10 | Segment 3 — K-Means Deep Dive | Visual algorithm walkthrough, k-means++ vs random init, limitations, why scaling is critical |
| 1:10–1:25 | Segment 4 — Break | 15-minute reset with optional informal Q&A |
| 1:25–1:55 | Segment 5 — PCA Theory | Maximum-variance intuition (no eigenvector derivations), use cases, explained variance, scree plots |
| 1:55–2:15 | Segment 6 — Live Coding: Mall Customers | Full K-Means workflow live: load → scale → cluster → elbow/silhouette → interpret segments in business terms |
| 2:15–2:35 | Segment 7 — Live Coding: MNIST PCA | Full PCA workflow live: 64 dimensions → 2D scatter of digits (sklearn `load_digits`, not full 784D MNIST), variance explained, the "wow" visualization |
| 2:35–2:55 | Segment 8 — Pair Programming: "Cluster Detective" | Pairs analyze pre-computed Wine clusters and propose business interpretations — diagnostic practice, not implementation |
| 2:55–3:00 | Segment 9 — Wrap-Up & Preview Week 6 | Recap the three big takeaways, assign the post-class homework, preview neural networks |

The two live-coding segments map to two separate student notebooks: [`week5_live_session_kmeans.ipynb`](student_materials/day1_live_session/week5_live_session_kmeans.ipynb) and [`week5_live_session_pca.ipynb`](student_materials/day1_live_session/week5_live_session_pca.ipynb).

## Day 2 — Choosing K + PCA Mathematics

A 20-minute instructor-led deep dive (two 10-minute parts) into the two topics students find hardest on Day 1: methods for choosing K beyond the elbow (silhouette analysis, domain knowledge) and an intuitive walk through how PCA actually works. Philosophy: intuition over proofs, visual explanations, and practical decision-making frameworks that address Day 1 confusions head-on.

- Guided notebooks: [`week5_wine_guided.ipynb`](student_materials/day2_guided_practice/week5_wine_guided.ipynb) / [solutions](student_materials/day2_guided_practice/week5_wine_guided_solutions.ipynb)

## Materials Map

### For Students

#### Pre-class (~30 min)

- [Pre-Class Study Guide](student_materials/pre_class/Week5_Pre_Class_Study_Guide.md) ([PDF](student_materials/pre_class/Week5_Pre_Class_Study_Guide.pdf))
- [Pre-class practice notebook](student_materials/pre_class/week5_preclass_practice.ipynb)

#### Day 1 live session

- [K-Means live-coding notebook](student_materials/day1_live_session/week5_live_session_kmeans.ipynb) (Segment 6)
- [PCA live-coding notebook](student_materials/day1_live_session/week5_live_session_pca.ipynb) (Segment 7)
- [Student Workbook](student_materials/day1_live_session/Week5_Student_Workbook.md)

#### Day 1 pair programming

- ["Cluster Detective" notebook](student_materials/day1_pair_programming/week5_pair_programming.ipynb) (Segment 8)

#### Day 2 guided practice

- [Wine guided notebook](student_materials/day2_guided_practice/week5_wine_guided.ipynb) / [solutions](student_materials/day2_guided_practice/week5_wine_guided_solutions.ipynb)

#### Post-class

- [Homework notebook](student_materials/post_class/week5_postclass_exercise.ipynb) (Iris clustering + PCA, ~90–120 min) / [solutions](student_materials/post_class/week5_postclass_solutions.ipynb)
- [Self-Assessment checklist](student_materials/post_class/Week5_Self_Assessment.md)

#### Data & visuals

- `Mall_Customers.csv` lives in [student_materials/data/](student_materials/data/); the digits, Wine, and Iris datasets load directly from scikit-learn
- Student-facing figures and the K-Means animation: [student_materials/visuals/](student_materials/visuals/) (index: [QUICK_VISUAL_REFERENCE.md](student_materials/visuals/QUICK_VISUAL_REFERENCE.md))
- Orientation doc: [Week5_Student_Materials_Guide.md](student_materials/Week5_Student_Materials_Guide.md)
- Reference reading: [Appendix_Unsupervised_Learning_Guide.md](appendices/Appendix_Unsupervised_Learning_Guide.md)

## Where This Week Fits

- **Builds on:** Week 4 — validation methodology (train/validation/test, cross-validation, preventing leakage) for supervised models; the sklearn fit/predict pattern carries straight over, but the labels are gone
- **Sets up:** Week 6 — Neural Network Fundamentals: the same MNIST digits explored with PCA today get *classified* by your first neural network next week

---

*Introduction to ML Programming — Week 5 of 12 - Instructor: Dr. Lawrence Gray*
