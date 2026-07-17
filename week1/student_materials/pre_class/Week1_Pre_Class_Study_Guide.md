# Week 1 Pre-Class Study Guide: Linear Regression

**Time Required:** 30 minutes
**Complete By:** Before Week 1 live session

---

## 🎯 Learning Objectives

By completing this pre-class work, you will:

- [ ] Understand what linear regression is and when to use it
- [ ] Grasp the intuition behind gradient descent
- [ ] Recognize the sklearn API pattern (fit/predict)
- [ ] Be familiar with basic terminology (features, target, training, testing)
- [ ] Come to class ready to code, not learn from scratch

---

## 📺 Required Videos (43 minutes total)

### Video 0: StatQuest - Best Fit Line (9 minutes)

**Link:** https://www.youtube.com/watch?v=PaFPbb66DxQ


### Video 1: StatQuest - Linear Regression (Stop at 12 minutes 10 secs)

**Link:** https://www.youtube.com/watch?v=7ArmBVF2dCs

**What to watch for:**

- 0:00-2:00: What is linear regression? (The "line of best fit")
- 2:00-5:00: Least squares method (minimizing squared errors)
- 5:00-8:00: R-squared interpretation
- 8:00-12:00: Multiple regression (more than one feature)

**Key Questions to Answer While Watching:**

1. What does the "best fit line" minimize?
2. What does R² tell you?
3. Can linear regression handle multiple features (not just one)?

**Your Notes:**

```
[Space for your notes]




```

---

### Video 2.0: Google ML - Gradient Descent (less math) (2 minutes)

**Link:** https://www.youtube.com/watch?v=QoK1nNAURw4

### Video 2.1: StatQuest - Gradient Descent (more math) (22 minutes)

**Link:** https://www.youtube.com/watch?v=sDv4f4s2SB8

**Key Questions to Answer While Watching:**

1. What is gradient descent trying to find?
2. What happens if the learning rate is too large?
3. What happens if the learning rate is too small?

**Your Notes:**

```
[Space for your notes]




```

---

## 📖 Required Reading (8 minutes)

### Reading 1: sklearn Linear Models Documentation

**Link:** https://scikit-learn.org/stable/modules/linear_model.html

**What to read:** Sections 1.1.1 through 1.1.3 only

**Focus on:**

- ✅ The basic `LinearRegression` class
- ✅ `.fit()` and `.predict()` methods
- ✅ What coefficients represent
- ❌ Skip: Advanced topics like Ridge, Lasso (we'll cover in Week 4)

**Skim vs. Read Carefully:**

- **Read carefully:** Section 1.1.1 (Ordinary Least Squares)
- **Skim:** Examples and mathematical formulations
- **Skip:** Everything after section 1.1.3

**Key Concepts to Extract:**

1. How do you create a LinearRegression model?
2. What does `.fit(X, y)` do?
3. What does `.predict(X)` return?

**Your Notes:**

```
[Space for your notes]




```

---

## ✅ Pre-Class Self-Check Quiz

Test your understanding before class. **Don't worry if you can't answer everything perfectly** - we'll cover it all in detail during the live session!

### Question 1
**What is the goal of linear regression?**

- [ ] a) To classify data into categories
- [ ] b) To find the line that minimizes the sum of squared errors
- [ ] c) To cluster similar data points
- [ ] d) To reduce the number of features

<details>
<summary>Click to reveal answer</summary>

**Answer: b)** Linear regression finds the line (or hyperplane) that minimizes the sum of squared errors between predictions and actual values.
</details>

---

### Question 2
**What does R² = 0.8 mean?**

- [ ] a) 80% of predictions are correct
- [ ] b) The model explains 80% of the variance in the data
- [ ] c) 80% of the data was used for training
- [ ] d) There's an 80% error rate

<details>
<summary>Click to reveal answer</summary>

**Answer: b)** R² (coefficient of determination) represents the proportion of variance in the target variable explained by the model. R² = 0.8 means 80% of variance is explained.
</details>

---

### Question 3
**In sklearn, what does `model.fit(X_train, y_train)` do?**

- [ ] a) Makes predictions
- [ ] b) Trains the model by learning from the training data
- [ ] c) Splits the data into train and test sets
- [ ] d) Evaluates the model's performance

<details>
<summary>Click to reveal answer</summary>

**Answer: b)** `.fit()` trains the model by learning the best parameters (coefficients) from the training data.
</details>

---

### Question 4
**What happens if the gradient descent learning rate is too large?**

- [ ] a) Training is very slow
- [ ] b) The model might overshoot the minimum and diverge
- [ ] c) The model will always find the global minimum
- [ ] d) Nothing - learning rate doesn't matter

<details>
<summary>Click to reveal answer</summary>

**Answer: b)** If the learning rate is too large, gradient descent takes steps that are too big, potentially overshooting the minimum and causing the loss to increase or oscillate wildly.
</details>

---

### Question 5
**Why do we square the errors in "sum of squared errors"?**

- [ ] a) To make the math harder
- [ ] b) So positive and negative errors don't cancel out
- [ ] c) Because sklearn requires it
- [ ] d) To increase model accuracy

<details>
<summary>Click to reveal answer</summary>

**Answer: b)** Squaring errors ensures they're all positive, preventing positive errors from canceling out negative ones. It also penalizes large errors more than small ones.
</details>

---

## 📊 Score Your Pre-Class Quiz

**How many did you get right?**

- **5/5:** Excellent! You're well-prepared.
- **3-4/5:** Good foundation. Pay extra attention during class to concepts you missed.
- **1-2/5:** That's okay! The videos and reading are dense. The live session will clarify everything.
- **0/5:** No problem! Come to class ready to learn. The instructor will explain from scratch.

**Remember:** This quiz is for YOU to gauge your preparation, not for a grade!

---

## 🗺️ What to Expect in the Live Session

**Segment 1 (0:00-0:20): Welcome & Course Overview**

- You'll learn where Week 1 fits in the 8-week journey
- The "big picture" of machine learning

**Segment 2 (0:20-0:50): The ML Pipeline**

- Step-by-step workflow used in ALL ML projects
- Critical concept: Why we split data before preprocessing

**Segment 3 (0:50-1:20): Linear Regression Deep Dive**

- Building on what you watched in StatQuest videos
- Loss functions, gradient descent, intuitive explanations (no heavy math!)

**BREAK** (1:20-1:35)

**Segment 4 (1:35-2:15): Live Coding Demo**

- **You'll follow along and RUN code** (not type from scratch!)
- California Housing dataset
- Complete pipeline: load → split → train → evaluate → visualize

**Segment 5 (2:15-2:45): Pair Programming**

- Your turn! Apply what you learned to a new dataset
- Work with a partner

**Segment 6 (2:45-3:00): Wrap-up & Homework Preview**

---

## 🎒 What to Bring to Class

**Required:**

- [ ] Laptop with Python and Jupyter installed (or Google Colab access)
- [ ] This study guide (your notes)
- [ ] Curiosity and questions!

**Optional but helpful:**

- [ ] Notebook/paper for additional notes
- [ ] Second screen (if virtual) to have docs open alongside code

---

## 💡 Tips for Success

### Before the Live Session

1. ✅ Watch videos in order (Linear Regression, then Gradient Descent)
2. ✅ Take notes while watching - pause and rewind as needed
3. ✅ Skim the sklearn docs (don't need to memorize!)
4. ✅ Complete the self-check quiz
5. ✅ Prepare your environment (test that Jupyter/Colab works)

### During the Live Session

1. 👂 Focus on understanding concepts during demos (you won't type during live coding)
2. ❓ Ask questions when confused - if you're confused, others probably are too!
3. 📝 Take notes on patterns you see
4. 🤝 Engage actively during pair programming

### After the Live Session

1. ✅ Complete the post-class homework (30 min)
2. 🔄 Review concepts that were unclear
3. 📖 Compare your solution to the provided solution notebook

---

## 🔗 Additional Resources (Optional)

If you want to dive deeper BEFORE class (completely optional):

**Interactive Tutorials:**

- Google ML Crash Course - Linear Regression: https://developers.google.com/machine-learning/crash-course/descending-into-ml/video-lecture
- Kaggle Learn - Intro to ML: https://www.kaggle.com/learn/intro-to-machine-learning

**Visual Explanations:**

- 3Blue1Brown - Gradient Descent: https://www.youtube.com/watch?v=IHZwWFHWa-w
- Seeing Theory - Regression: https://seeing-theory.brown.edu/regression-analysis/index.html

**Reading:**

- [Appendix A: ML Pipeline Template](../../appendices/Appendix_A_ML_Pipeline_Template.md) - Preview the code structure you'll use

---

## ✅ Pre-Class Completion Checklist

Before the live session, make sure you:

- [ ] Watched StatQuest Best Fit Line (9 min)
- [ ] Watched StatQuest Linear Regression (12 min)
- [ ] Watched StatQuest Gradient Descent (22 min)
- [ ] Watched Google ML Gradient Descent (2 min)
- [ ] Skimmed sklearn Linear Models docs (sections 1.1.1-1.1.3)
- [ ] Completed the 5-question self-check quiz
- [ ] Tested your Python/Jupyter environment
- [ ] Reviewed learning objectives

**Estimated total time:** 30 minutes

---

## ❓ Questions Before Class?

If anything is unclear, don't stress! The live session will bring it all together.

---

**See you in class! 🚀**
