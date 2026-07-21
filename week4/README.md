# Week 4 — Model Selection & Avoiding Pitfalls

Weeks 1–3 taught you to *build* models. Week 4 teaches you to build models you can *trust*. No new algorithms this week — instead, the four pillars of production ML methodology: cross-validation, systematic hyperparameter tuning, regularization, and data-leakage prevention, all wired together into one leak-proof scikit-learn Pipeline. It's the difference between "my model got 85%!" and "my model gets 84.2% ± 1.3% across 5 folds with zero leakage."

## At a Glance

| | |
|---|---|
| **Topic** | Production ML methodology: cross-validation, GridSearchCV, regularization, data leakage & Pipelines |
| **Datasets** | Adult Income (main, carried over from Week 3) · Breast Cancer (quick CV demo) · Wine Quality UCI (Day 2 guided practice) · Titanic (homework) |
| **Frameworks** | scikit-learn (Pipeline, ColumnTransformer, GridSearchCV), pandas, NumPy, matplotlib/seaborn, joblib |
| **Structure** | Pre-class (~30 min) · Day 1 live session (3 hr) + separate 90-min pair programming · Day 2 deep dive + guided practice (1 hr) · Post-class self-assessment |
| **Compute** | Brev CPU tier (4 vCPU / 16 GB) or any laptop — no GPU needed (Weeks 1–7) |

## What Students Learn

- Why a single train/test split is unreliable, and how k-fold cross-validation (plain and stratified) yields mean ± std performance estimates
- The parameters-vs-hyperparameters distinction, and systematic tuning with GridSearchCV and RandomizedSearchCV (`best_params_`, `best_score_`, `cv_results_`, coarse-to-fine search)
- How L1 (Lasso), L2 (Ridge), and Elastic Net regularization prevent overfitting, and how alpha tuning shapes coefficients
- What data leakage is, how to spot it in code (scaler leakage, feature-selection leakage), and why it's the #1 silent killer of production ML
- Building a complete leak-free pipeline: ColumnTransformer + Pipeline + GridSearchCV, validated against a production checklist
- The bias-variance tradeoff and how the Week 4 toolkit manages it (Day 2)
- Reporting results professionally: "84.2% ± 0.9% across 5-fold CV, tuned via GridSearchCV, no leakage" instead of a single lucky number

## Day 1 — Live Session (3 hours)

| Time | Segment | What happens |
|---|---|---|
| 0:00–0:15 | Segment 1 — Week 3 Recap & Preview | Recall Week 3 (trees, forests, Adult Income baseline); frame the shift from algorithms to methodology |
| 0:15–0:45 | Segment 2 — Cross-Validation Deep Dive | Whiteboard + demo hybrid: why single splits lie, k-fold mechanics, stratified CV, mean ± std |
| 0:45–1:15 | Segment 3 — Hyperparameter Tuning | GridSearchCV and RandomizedSearchCV on Adult Income; interpreting search results |
| 1:15–1:30 | Segment 4 — Break | 15-minute reset; instructor preps second-half demos |
| 1:30–2:00 | Segment 5 — Regularization | The "speed limit" for model complexity: L1, L2, Elastic Net with alpha tuning |
| 2:00–2:25 | Segment 6 — Data Leakage | The time-travel paradox; spotting leaky code; Pipeline as the fix |
| 2:25–2:50 | Segment 7 — Live Coding: Complete Pipeline | Students dictate, instructor types: ColumnTransformer + Pipeline + GridSearchCV from scratch |
| 2:50–3:00 | Segment 9 — Wrap-Up & Preview | Four Pillars recap, Titanic homework launch, Day 2 preview |
| Separate 90 min | Segment 8 — Pair Programming: Data Leakage Detective | Pairs detect, diagnose, and fix leakage in 6 realistic code scenarios |

### Homework (assigned in Segment 9)

Students independently rebuild the full methodology on a new dataset — Titanic survival prediction:

- Complete Pipeline with ColumnTransformer (impute + scale numerics, impute + encode categoricals)
- GridSearchCV over at least 3 hyperparameters × 3 values with cv=5
- Regularization comparison (L1 / L2 / Elastic Net for linear models)
- Written explanation of how the Pipeline prevents leakage, plus a saved `.pkl` pipeline

## Day 2 — Deep Dive: Bias-Variance & Data Leakage in Production

A 1-hour session that digs into *why* Day 1's tools matter. Two whiteboard deep dives — the bias-variance tradeoff (dartboard metaphor; how CV, GridSearch, and regularization strike the balance) and data leakage in production (three leakage types; Pipeline as the guarantee) — followed by a 20-minute guided Wine Quality pipeline build and an 8-question quiz.

- Guided notebooks:
  - [week4_wine_quality_guided.ipynb](student_materials/day2_guided_practice/week4_wine_quality_guided.ipynb) — student version (70% scaffolded)
  - [week4_wine_quality_guided_solutions.ipynb](student_materials/day2_guided_practice/week4_wine_quality_guided_solutions.ipynb) — solutions
  - [week4_instructor_demos.ipynb](student_materials/day2_guided_practice/week4_instructor_demos.ipynb) — instructor demos

## Materials Map

### For Students

Start with the [Student Materials Guide](student_materials/Week4_Student_Materials_Guide.md).

#### Pre-class ([pre_class/](student_materials/pre_class/))

- [Week4_Pre_Class_Study_Guide.md](student_materials/pre_class/Week4_Pre_Class_Study_Guide.md) (also as [PDF](student_materials/pre_class/Week4_Pre_Class_Study_Guide.pdf))
- [week4_preclass_practice.ipynb](student_materials/pre_class/week4_preclass_practice.ipynb)

#### Day 1 live session ([day1_live_session/](student_materials/day1_live_session/))

- [week4_live_session.ipynb](student_materials/day1_live_session/week4_live_session.ipynb) — main notebook (Adult Income), used in Segments 3–7
- [week4_cv_demo.ipynb](student_materials/day1_live_session/week4_cv_demo.ipynb) — Segment 2 cross-validation demo
- [Week4_Student_Workbook.md](student_materials/day1_live_session/Week4_Student_Workbook.md)
- [Week4_Glossary.md](student_materials/day1_live_session/Week4_Glossary.md)
- [Week4_sklearn_cheat_sheet.md](student_materials/day1_live_session/Week4_sklearn_cheat_sheet.md)

#### Day 1 pair programming ([day1_pair_programming/](student_materials/day1_pair_programming/))

- [week4_pair_programming.ipynb](student_materials/day1_pair_programming/week4_pair_programming.ipynb) — Data Leakage Detective scenarios
- [week4_pair_programming_solutions.ipynb](student_materials/day1_pair_programming/week4_pair_programming_solutions.ipynb)

#### Day 2 guided practice ([day2_guided_practice/](student_materials/day2_guided_practice/))

- Wine Quality notebooks listed under Day 2 above, plus the saved [wine_quality_pipeline.pkl](student_materials/day2_guided_practice/wine_quality_pipeline.pkl)

#### Day 2 post-class ([day2_post_class/](student_materials/day2_post_class/))

- [Week4_Self_Assessment.md](student_materials/day2_post_class/Week4_Self_Assessment.md)

#### Reference reading ([appendices/](appendices/))

- [Appendix C: Cross-validation implementation guide](appendices/Appendix_C_CrossValidation_Implementation_Guide.md)
- [Appendix D: Data leakage detection checklist](appendices/Appendix_D_Data_Leakage_Detection_Checklist.md)

## Where This Week Fits

- **Builds on:** Week 3 — Decision Trees and Random Forests on Adult Income, where students observed overfitting but lacked the tools to prevent it; Week 4 reuses the same dataset with rigorous methodology.
- **Sets up:** Week 5 — new algorithms return, now practiced with CV, tuning, regularization, and Pipelines as the default workflow that transfers to every model in the rest of the course.
