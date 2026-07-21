# Week 1 — The ML Pipeline & Linear Regression

Every ML project — predicting crop yields, detecting fraud, recommending products — follows the same 6-step pipeline, and this week students learn it by building a complete, working model on real housing data. The course philosophy is set from minute one: intuition first, math later; production patterns over theory; learning by doing. By the 3-hour mark, every student has trained, evaluated, and interpreted their first ML model — the foundation that logistic regression, trees, and neural networks all build on.

## At a Glance

| | |
| --- | --- |
| **Topic** | The 6-step ML pipeline, data leakage, and linear regression with scikit-learn |
| **Datasets** | California Housing (live coding), Diabetes (pair programming), Boston Housing (Day 2), Auto MPG (post-class) |
| **Frameworks** | scikit-learn, pandas, NumPy, matplotlib |
| **Structure** | Pre-class (~30 min) · Day 1 live session (3 hr) · Day 2 deep dive (1 hr) · Post-class (~30 min) |
| **Compute** | Brev CPU tier (4 vCPU / 16 GB) or any laptop — no GPU needed (Weeks 1–7) |

## Quick Start

**Student path:** pre-class study guide → Day 1 live session + pair programming → Day 2 guided Boston Housing notebook → post-class Auto MPG practice.

## What Students Learn

- Execute a complete ML pipeline — load, explore, split, train, predict, evaluate — on real data
- Why data splitting must happen **before** preprocessing: data leakage as the #1 cause of production failures (the "locked vault" concept)
- Linear regression as "finding the best line" by minimizing MSE — and that sklearn solves it exactly with the Normal Equation, no gradient descent
- The universal sklearn API pattern: Create → Fit → Predict
- Evaluating regression models with R², MSE, and RMSE
- Reading residual plots as a diagnostic tool: random scatter (good) vs. funnel and curve patterns (trouble)
- Interpreting coefficients with "holding all else constant" language and summarizing a model for stakeholders

## Day 1 — Live Session (3 hours)

| Time | Segment | What happens |
| --- | --- | --- |
| 0:00–0:15 | Segment 1 — Welcome & Course Roadmap | Course arc, philosophy (intuition > math), Week 1 objectives, "questions are gifts" |
| 0:15–0:40 | Segment 2 — ML Pipeline Concepts | Whiteboard-only: the 6 steps, data leakage and the locked vault, sklearn API pattern |
| 0:40–1:00 | Segment 3 — Linear Regression Theory | Best line, MSE as loss, closed-form solution, coefficient intuition — no derivations |
| 1:00–1:15 | Segment 4 — Residual Plots Preview | What residuals are and which patterns to look for, before students see real ones |
| 1:15–1:30 | Segment 5 — Break | Instructor pre-flight: run all notebook cells, prep for coding |
| 1:30–2:25 | Segment 6 — Live Coding: California Housing | The full pipeline coded end-to-end in `week1_live_session.ipynb`, with the WHY behind every line |
| ↳ 2:15–2:25 | Segment 6b — Coefficient Interpretation | What `model.coef_` numbers actually mean, in business language |
| ↳ 2:25–2:35 | Segment 6c — Reading Residual Plots | Pattern recognition on the plots students just made: scatter vs. funnel vs. curve |
| ↳ 2:35–2:40 | Segment 6d — Interpreting Your Model | Synthesis: coefficients + diagnostics → a stakeholder-ready model summary |
| 2:25–2:55 | Segment 7 — Pair Programming | Navigator/driver pairs build the pipeline on the Diabetes dataset |
| 2:55–3:00 | Segment 8 — Wrap-Up & Preview | Recap checklist, homework, Week 2 (classification) preview |

*The 6b–6d interpretation mini-segments are woven into the back half of the session; their clock ranges overlap slightly with Segments 6–7.*

## Day 2 — Deep Dive: Statistical Foundations & Guided Practice

A 1-hour synchronous session on the statistical foundations behind Day 1's code: the 4 assumptions underlying linear regression, how specific residual patterns map to specific assumption violations, and what to do about each. Students then complete a full regression pipeline independently (with guidance) on the Boston Housing dataset and self-assess with a quiz.

By the end of Day 2, students can:

- Name the 4 assumptions underlying linear regression
- Map each residual pattern to the specific assumption it violates, and know the fix for each
- Recognize when linear regression is inappropriate for a problem
- Complete a full regression pipeline independently and assess their understanding via quiz

- Guided notebooks: [week1_boston_housing_guided.ipynb](student_materials/day2_guided_practice/week1_boston_housing_guided.ipynb) · [solutions](student_materials/day2_guided_practice/week1_boston_housing_guided_solutions.ipynb)

## Materials Map

### For Students

**Pre-class** — [student_materials/pre_class/](student_materials/pre_class/)

- [Week1_Pre_Class_Study_Guide.md](student_materials/pre_class/Week1_Pre_Class_Study_Guide.md) (also as [PDF](student_materials/pre_class/Week1_Pre_Class_Study_Guide.pdf))
- [week1_preclass_practice.ipynb](student_materials/pre_class/week1_preclass_practice.ipynb)

**Day 1 live session** — [student_materials/day1_live_session/](student_materials/day1_live_session/) ([README](student_materials/day1_live_session/README.md))

- [week1_live_session.ipynb](student_materials/day1_live_session/week1_live_session.ipynb) — California Housing, coded together in Segment 6
- [week1_pair_programming.ipynb](student_materials/day1_live_session/week1_pair_programming.ipynb) — Diabetes dataset, Segment 7
- [Week1_Student_Workbook.md](student_materials/day1_live_session/Week1_Student_Workbook.md) · [Week1_Glossary.md](student_materials/day1_live_session/Week1_Glossary.md) · [Week1_sklearn_cheat_sheet.md](student_materials/day1_live_session/Week1_sklearn_cheat_sheet.md)
- [mse_linear_regression_demo.html](student_materials/day1_live_session/mse_linear_regression_demo.html) — interactive MSE demo

**Day 2 guided practice** — [student_materials/day2_guided_practice/](student_materials/day2_guided_practice/) ([README](student_materials/day2_guided_practice/README.md))

- [week1_boston_housing_guided.ipynb](student_materials/day2_guided_practice/week1_boston_housing_guided.ipynb) + [solutions](student_materials/day2_guided_practice/week1_boston_housing_guided_solutions.ipynb)
- [Week1_Self_Assessment.md](student_materials/day2_guided_practice/Week1_Self_Assessment.md)

**Post-class** — [student_materials/post_class/](student_materials/post_class/)

- [week1_auto_mpg_practice.ipynb](student_materials/post_class/week1_auto_mpg_practice.ipynb) + [solutions](student_materials/post_class/week1_auto_mpg_practice_SOLUTIONS.ipynb)
- [week1_bonus_polynomial.ipynb](student_materials/post_class/week1_bonus_polynomial.ipynb) + [solutions](student_materials/post_class/week1_bonus_polynomial_SOLUTIONS.ipynb) — optional stretch

The homework arc: ~30 minutes — rebuild the pipeline on a fresh dataset (Auto MPG), create and interpret a residual plot, compute R², and post your score to the course forum. (If a Diabetes homework exercise was mentioned in class, note that the Auto MPG notebook above is the actual homework.) The bonus polynomial-features notebook is optional for students who want a challenge.

**Reference visuals** — [student_materials/residual_plots/](student_materials/residual_plots/) — good/funnel/curve residual plot images used in Segments 4 and 6c

## Where This Week Fits

- **Builds on:** The data-science prerequisite course — segments explicitly connect back to students' prior exposure to Q-Q plots and coefficient outputs (DS Weeks 1B and 5)
- **Sets up:** Week 2 — Classification: linear regression transforms into logistic regression ("just add a sigmoid"), bringing precision, recall, F1, and confusion matrices
- **Course-wide throughline:** the Create → Fit → Predict pattern and the split-before-preprocessing rule introduced this week recur in every model students build afterward