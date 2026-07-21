# Week 3 — Trees & Ensembles: The Tabular Data Workhorses

Week 2 left students with exactly one classifier — logistic regression. Week 3 triples the toolkit in a single session: Decision Trees ("20 Questions"), Random Forests ("Committee Decision"), and XGBoost ("Learning from Mistakes") — the three algorithms that dominate tabular data in industry. The real deliverable is the reusable skill underneath: systematic algorithm comparison — train several models, compare metrics, and choose based on business tradeoffs, not hype.

## At a Glance

| | |
| --- | --- |
| **Topic** | Tree-based ensemble methods and systematic algorithm comparison |
| **Datasets** | Adult Income / Census (Day 1 live session) · Wine (pre-class + pair programming) · Heart Disease (Day 2) · Iris & Digits (post-class) |
| **Frameworks** | scikit-learn, XGBoost, pandas, matplotlib |
| **Structure** | Pre-class (~30 min) · Day 1 live session (3 hr) · Day 2 deep dive + guided practice (1 hr) · Post-class homework (2–3 hr) |
| **Compute** | Brev CPU tier (4 vCPU / 16 GB) or any laptop — no GPU needed (Weeks 1–7) |

## What Students Learn

- How decision trees split data with binary questions (information-gain intuition, not math) and why deep trees overfit
- How bagging builds Random Forests — bootstrap samples + voting — and why ensembles reduce error
- How boosting builds XGBoost — sequential trees that fix previous errors — and its key hyperparameters (`n_estimators`, `learning_rate`, `max_depth`)
- The core skill: systematic algorithm comparison — train all three on one dataset, compare accuracy/precision/recall/F1 in a single table
- How to extract, interpret, and compare feature importance — and communicate it to stakeholders
- An algorithm selection framework: interpretability vs performance vs speed, applied to real business scenarios
- (Day 2) Diagnosing overfitting from the train/test gap and controlling it with `max_depth`; bagging vs boosting side by side

### The Three Algorithms in One Table

| Algorithm | Metaphor | Pro | Con |
| --- | --- | --- | --- |
| Decision Tree | "20 Questions Game" — one tree, yes/no splits | Interpretable, fast, visualizable | Limited accuracy, overfits easily |
| Random Forest | "Committee Decision" — parallel trees vote (bagging) | Robust, good accuracy, hard to screw up | Slower than one tree, less interpretable |
| XGBoost | "Learning from Mistakes" — sequential trees fix errors (boosting) | Highest accuracy, wins competitions | Slower training, more tuning, least interpretable |

**When to use:** need interpretability → Decision Tree · want a robust default → Random Forest · need max accuracy (and time to tune) → XGBoost.

## Day 1 — Live Session (3 hours)

| Time | Segment | What happens |
| --- | --- | --- |
| 0:00–0:15 | Segment 1 — Week 2 Recap & Welcome | Interactive Week 2 recall, today's agenda, Adult Income dataset preview, tradeoffs theme |
| 0:15–0:45 | Segment 2 — Decision Trees | Concrete-first demo, "20 Questions" metaphor, splits and overfitting risk |
| 0:45–1:10 | Segment 3 — Random Forests | "Committee Decision" metaphor, bagging, feature importance, the robust default |
| 1:10–1:25 | Segment 4 — Break | 15-minute recharge with a preview of the second half |
| 1:25–1:55 | Segment 5 — XGBoost | "Learning from Mistakes" metaphor, bagging vs boosting, key hyperparameters |
| 1:55–2:30 | Segment 6 — Live Coding: Systematic Algorithm Comparison | The critical segment: code-along comparing all three algorithms on Adult Income |
| 2:25–2:35 | Segment 6b — Feature Importance Interpretation | Extract, interpret, and compare importance across models |
| 2:35–2:45 | Segment 6c — Algorithm Selection Framework | Which model ships to production? Decision framework + scenarios |
| 2:30–2:50 | Segment 7 — Pair Programming: Algorithm Showdown | Pairs explain predictions, compare importance, pick algorithms for business scenarios |
| 2:50–3:00 | Segment 8 — Wrap-Up & Week 4 Preview | Consolidate the three algorithms, homework overview, Week 4 teaser |

*Note: the 6b/6c time windows overlap Segments 6 and 7 — treat 6b and 6c as compressed inserts woven into the back half of the session.*

## Day 2 — Deep Dive: Overfitting in Trees & Bagging vs Boosting

A 1-hour session that goes deeper into WHY the algorithms behave differently: Part 1 unpacks why single trees overfit (train/test gap at depth 1/5/10/None, bias-variance tradeoff); Part 2 contrasts bagging and boosting at the whiteboard. Then students apply everything to a new dataset — Heart Disease — in guided practice, followed by an 8-question quiz.

- Guided notebooks: [week3_heart_disease_guided.ipynb](student_materials/day2_guided_practice/week3_heart_disease_guided.ipynb) · [solutions](student_materials/day2_guided_practice/week3_heart_disease_guided_solutions.ipynb)

## Materials Map

### For Students

Start here: [Week3_Student_Materials_Guide.md](student_materials/Week3_Student_Materials_Guide.md) · [STUDENT_MATERIALS_SUMMARY.md](student_materials/STUDENT_MATERIALS_SUMMARY.md)

**Pre-class** (~30 min)
- [Week3_Pre_Class_Study_Guide.md](student_materials/pre_class/Week3_Pre_Class_Study_Guide.md) ([PDF](student_materials/pre_class/Week3_Pre_Class_Study_Guide.pdf)) — videos + concepts before class
- [week3_preclass_practice.ipynb](student_materials/pre_class/week3_preclass_practice.ipynb) — warm-up on the Wine dataset

**Day 1 live session**
- [week3_live_session.ipynb](student_materials/day1_live_session/week3_live_session.ipynb) — code-along notebook (Adult Income) · [solution](student_materials/day1_live_session/week3_live_session_solution.ipynb)
- [Week3_Student_Workbook.md](student_materials/day1_live_session/Week3_Student_Workbook.md) · [Week3_Glossary.md](student_materials/day1_live_session/Week3_Glossary.md) · [Week3_sklearn_cheat_sheet.md](student_materials/day1_live_session/Week3_sklearn_cheat_sheet.md)

**Day 1 pair programming**
- [week3_pair_programming.ipynb](student_materials/day1_pair_programming/week3_pair_programming.ipynb) — "Algorithm Showdown" (Wine)
- [week3_pair_programmin_solutions.ipynb](student_materials/day1_pair_programming/week3_pair_programmin_solutions.ipynb) — solutions (note: filename typo is in the repo; link is exact)

**Day 2 guided practice**
- [week3_heart_disease_guided.ipynb](student_materials/day2_guided_practice/week3_heart_disease_guided.ipynb) · [solutions](student_materials/day2_guided_practice/week3_heart_disease_guided_solutions.ipynb)

**Post-class**
- [week3_postclass_exercise.ipynb](student_materials/post_class/week3_postclass_exercise.ipynb) (Iris) · [solutions](student_materials/post_class/week3_postclass_solutions.ipynb)
- [week3_postclass_digits_exercise.ipynb](student_materials/post_class/week3_postclass_digits_exercise.ipynb) (Digits) · [solutions](student_materials/post_class/week3_postclass_digits_solutions.ipynb)
- [Week3_Self_Assessment.md](student_materials/post_class/Week3_Self_Assessment.md)

**Interactive references**
- [random-forest-steps.html](student_materials/random-forest-steps.html) · [xgboost-steps.html](student_materials/xgboost-steps.html)

**Reference reading**
- [Appendix C — Tree Ensemble Guide](appendices/Appendix_C_Tree_Ensemble_Guide.md) — reference text on trees and ensembles

## Where This Week Fits

- **Builds on:** Week 2 — classification with logistic regression and metrics (confusion matrix, precision/recall, why accuracy lies); same sklearn fit/predict pattern, new algorithms
- **Sets up:** Week 4 — model validation & hyperparameter tuning: cross-validation, grid/random search, and learning curves to turn today's default-parameter models into tuned ones
