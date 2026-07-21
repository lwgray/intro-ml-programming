# Week 2 — Classification Fundamentals

Week 1 taught the ML pipeline through regression — predicting continuous values like housing prices. Week 2 keeps the exact same sklearn pattern (load, split, fit, predict, evaluate) and flips the target: students predict *categories*, building a logistic-regression cancer classifier on real medical data. The star of the week is the confusion matrix — the little 2x2 grid behind every classification metric, and per the wrap-up "the single most valuable skill from today": if you can create and interpret one, you can debug any classifier.

## At a Glance

| | |
| --- | --- |
| **Topic** | Binary classification with logistic regression; confusion matrix, precision/recall, ROC/AUC, and threshold tuning |
| **Datasets** | Breast Cancer Wisconsin (Day 1 live coding + pair programming), Heart Disease (Day 2 guided practice), Iris (pre-class practice), Titanic (post-class exercise) |
| **Frameworks** | scikit-learn, pandas, NumPy, Matplotlib, seaborn |
| **Structure** | Pre-class (~30 min) - Day 1 live session (3 hr) - Day 2 deep dive + guided practice (1 hr) - Post-class (~30–45 min + bonus) |
| **Compute** | Brev CPU tier (4 vCPU / 16 GB) or any laptop — no GPU needed (Weeks 1–7) |

## What Students Learn

- Distinguish classification from regression, recognize binary vs. multiclass problems, and understand decision boundaries (linear vs. nonlinear) conceptually
- Understand logistic regression visually as linear regression + a sigmoid "squashing" function that outputs probabilities — and use `predict()` vs. `predict_proba()` appropriately
- Build and interpret the confusion matrix (TP, TN, FP, FN) — the week's most important skill and the foundation of all classification metrics
- Calculate precision, recall, F1, and accuracy by hand and in sklearn — and explain when accuracy is misleading (class imbalance)
- Read ROC curves and AUC as performance visualizations
- Tune the decision threshold (0.5 is arbitrary!) and choose it based on business costs of false negatives vs. false positives
- Diagnose a broken classifier using confusion-matrix analysis — a real-world debugging skill, not just implementation

## The Week in Two Drawings

The whole week hangs on two whiteboard sketches from Segment 1. First, the pipeline students already know from Week 1 — unchanged for classification:

```text
Data → Train/Test Split → Model.fit() → Model.predict() → Evaluate
```

Second, the 2x2 grid that gets drawn "about 10 times" over the session, until it feels natural:

```text
                 Predicted
                 Neg    Pos
              ┌─────┬─────┐
Actual    Neg │ TN  │ FP  │
              ├─────┼─────┤
          Pos │ FN  │ TP  │
              └─────┴─────┘
```

**Why the Breast Cancer dataset?** Per Segment 1: the medical context makes metrics *matter* (missing a cancer diagnosis is very different from a false alarm), binary classification is the simplest starting point, and the data is clean — so class time goes to classification concepts, not data cleaning. Medical metaphors also double as stakeholder-communication practice.

**Teaching approach:** concrete before abstract. Students see a working classifier (Segment 2) before any theory (Segments 3–4) — the same pattern that worked in Week 1.

## Day 1 — Live Session (3 hours)

| Time | Segment | What happens |
| --- | --- | --- |
| 0:00–0:15 | Segment 1 — Week 1 Recap & Welcome | Interactive Week 1 recall (regression, split, metrics), today's agenda, Breast Cancer dataset preview, confusion-matrix teaser |
| 0:15–0:45 | Segment 2 — Quick Classification Demo | Concrete-before-abstract: a full classification pipeline runs live before any theory — same sklearn API, new outputs |
| 0:45–1:15 | Segment 3 — Classification Concepts | Classification vs. regression, binary vs. multiclass, decision boundaries, confusion-matrix structure preview |
| 1:15–1:30 | Segment 4 — Logistic Regression Theory | The sigmoid function visually — how linear predictions become probabilities (intuition, not derivations) |
| 1:30–1:45 | Segment 5 — Break | 15-minute reset with informal Q&A |
| 1:45–2:00 | Segment 6 — Metrics Deep Dive & Coding | THE critical segment: master the confusion matrix, hand-calculate precision/recall, learn when accuracy lies |
| 2:00–2:30 | Segment 7 — Live Coding Demo | Full pipeline coded step-by-step: confusion matrix, classification report, ROC curve, threshold tuning in sklearn |
| 2:30–2:50 | Segment 8 — Pair Programming: Classifier Diagnostics | Partners diagnose a poorly performing pre-trained classifier using metrics — diagnostic practice, not from-scratch coding |
| 2:50–3:00 | Segment 9 — Wrap-Up & Preview Week 3 | Recap, homework assignments, Week 3 (Trees & Ensembles) teaser |

Two optional interpretation modules extend the back half of the session: Segment 6b — Threshold Tuning (0.5 is arbitrary — pick thresholds by business context) and Segment 6c — Business Cost Analysis (assign dollar costs to FN/FP and justify the threshold).

## Day 2 — Deep Dive & Guided Practice (1 hour)

Day 1 built a breast cancer classifier; Day 2 goes deeper on the two questions that follow: what happens when classes are imbalanced, and how do you choose the RIGHT metric? Two whiteboard deep dives (class imbalance strategies, metric selection framework) lead into 20 minutes of guided practice on a new dataset — Heart Disease — followed by an 8-question quiz and the Week 3 transition.

- Guided notebooks: [week2_heart_disease_guided.ipynb](student_materials/day2_guided_practice/week2_heart_disease_guided.ipynb) - [solutions](student_materials/day2_guided_practice/week2_heart_disease_guided_solutions.ipynb)

## Materials Map

### For Students

Start with the [Student Materials Guide](student_materials/Week2_Student_Materials_Guide.md) — it explains when to use each notebook.

#### Pre-class (~30 min)

- [Pre-Class Study Guide](student_materials/pre_class/Week2_Pre_Class_Study_Guide.md) ([PDF](student_materials/pre_class/Week2_Pre_Class_Study_Guide.pdf))
- [week2_preclass_practice.ipynb](student_materials/pre_class/week2_preclass_practice.ipynb) — warm-up on the Iris dataset

#### Day 1 live session

- [week2_live_session.ipynb](student_materials/day1_live_session/week2_live_session.ipynb) — primary follow-along notebook ([solution](student_materials/day1_live_session/week2_live_session_solution.ipynb))
- [Student Workbook](student_materials/day1_live_session/Week2_Student_Workbook.md) - [Glossary](student_materials/day1_live_session/Week2_Glossary.md) - [sklearn Cheat Sheet](student_materials/day1_live_session/Week2_sklearn_cheat_sheet.md)
- ["Chef Learning to Season Chicken" logistic regression story](student_materials/day1_live_session/The-Chef-Learning-to-Season-Chicken.pptx) (also as [interactive HTML](student_materials/day1_live_session/Logistic_regression_Story.html))

#### Day 1 pair programming

Both STUDENT and SOLUTION notebooks live here:

- [week2_pair_programming_STUDENT.ipynb](student_materials/day1_pair_programming/week2_pair_programming_STUDENT.ipynb) — classifier diagnostics challenge
- [week2_pair_programming_SOLUTION.ipynb](student_materials/day1_pair_programming/week2_pair_programming_SOLUTION.ipynb)

#### Day 2 guided practice

- [week2_heart_disease_guided.ipynb](student_materials/day2_guided_practice/week2_heart_disease_guided.ipynb) ([solutions](student_materials/day2_guided_practice/week2_heart_disease_guided_solutions.ipynb))

#### Post-class (~30–45 min)

- [week2_postclass_exercise.ipynb](student_materials/post_class/week2_postclass_exercise.ipynb) — full pipeline on the Titanic dataset ([solutions](student_materials/post_class/week2_postclass_solutions.ipynb))
- Bonus: [week2_bonus_threshold_tuning.ipynb](student_materials/post_class/week2_bonus_threshold_tuning.ipynb) ([solution](student_materials/post_class/week2_bonus_threshold_tuning_SOLUTION.ipynb))
- [Self-Assessment checklist](student_materials/post_class/Week2_Self_Assessment.md)

## Where This Week Fits

- **Builds on:** Week 1 — the same load → split → fit → predict → evaluate pipeline, now predicting categories instead of continuous values
- **Sets up:** Week 3 — Trees & Ensembles: the same metrics learned this week evaluate decision trees, random forests, and XGBoost on messier data with complex decision boundaries
