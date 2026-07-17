# Week 5 Student Materials Guide

**Topic:** Unsupervised Learning (K-Means Clustering + PCA)
**Last Updated:** 2026-03-04

---

## 📁 Where to Find Everything

```
week5/student_materials/
├── pre_class/                    👉 Do BEFORE Day 1
│   ├── Week5_Pre_Class_Study_Guide.md
│   └── week5_preclass_practice.ipynb
│
├── day1_live_session/            👉 Use DURING Day 1
│   ├── week5_live_session_kmeans.ipynb
│   ├── week5_live_session_pca.ipynb
│   ├── Week5_Student_Workbook.md
│   ├── Week5_Glossary.md
│   └── Week5_sklearn_cheat_sheet.md
│
├── day1_pair_programming/        👉 Day 1 practice (20 min)
│   └── week5_pair_programming.ipynb
│
├── day2_guided_practice/         👉 Use DURING Day 2
│   ├── week5_wine_guided.ipynb
│   └── week5_wine_guided_solutions.ipynb
│
└── post_class/                   👉 Do AFTER Day 2
    ├── week5_postclass_exercise.ipynb
    ├── week5_postclass_solutions.ipynb
    ├── week5_bonus_pca_preprocessing.ipynb
    ├── week5_bonus_pca_preprocessing_SOLUTION.ipynb
    └── Week5_Self_Assessment.md
```

---

## 🗓️ Week 5 Schedule

### Before Day 1 (Pre-Class)
**Time:** 60-90 minutes
**Goal:** Understand unsupervised learning concepts + practice K-Means

✅ **Step 1:** Read `pre_class/Week5_Pre_Class_Study_Guide.md`
- What is unsupervised learning?
- K-Means intuition
- PCA basics

✅ **Step 2:** Complete `pre_class/week5_preclass_practice.ipynb`
- Run K-Means on sample data
- Practice elbow method
- Get familiar with sklearn API

---

### Day 1 (Live Session - 3 Hours)

**Bring to session:**
- `day1_live_session/week5_live_session_kmeans.ipynb` (open before class)
- `day1_live_session/week5_live_session_pca.ipynb` (open before class)
- `Week5_Student_Workbook.md` (for notes)

**Session Flow:**

| Time | Activity | Your Role |
|------|----------|-----------|
| 0:00-0:15 | Week 4 Recap | Listen + Answer questions |
| 0:15-0:35 | Unsupervised vs Supervised (Whiteboard) | Take notes |
| 0:35-1:10 | K-Means Theory | Understand concepts |
| 1:10-1:25 | BREAK | ☕ |
| 1:25-1:55 | PCA Theory | Understand concepts |
| 1:55-2:15 | Live Coding: K-Means (Mall Customers) | **CODE ALONG** in week5_live_session_kmeans.ipynb |
| 2:15-2:35 | Live Coding: PCA (MNIST) | **CODE ALONG** in week5_live_session_pca.ipynb |
| 2:35-2:55 | Pair Programming (Wine) | **WORK IN PAIRS** on week5_pair_programming.ipynb |
| 2:55-3:00 | Wrap-Up | Ask final questions |

**During Live Coding:**
- **IMPORTANT:** Code ALONG with instructor, don't just watch!
- Run each cell as instructor explains
- Ask questions if you get stuck

**During Pair Programming:**
- Work with a partner (assigned breakout room)
- Focus on **interpreting** clusters, not building K-Means
- Name clusters based on chemical properties

**Reference Materials (use as needed):**
- `Week5_Glossary.md` - Definitions of technical terms
- `Week5_sklearn_cheat_sheet.md` - Quick sklearn syntax reference

---

### Day 2 (Deep Dive & Guided Practice - 1 Hour)

**Bring to session:**
- `day2_guided_practice/week5_wine_guided.ipynb` (open before session)

**Session Flow:**

| Time | Activity | Your Role |
|------|----------|-----------|
| 0:00-0:05 | Day 1 Recap | Review concepts |
| 0:05-0:25 | Deep Dive (Choosing K + PCA Math) | Take notes |
| 0:25-0:45 | Guided Practice (Wine Dataset) | **FILL IN TODOS** (instructor-led) |
| 0:45-0:55 | Quiz (8 questions) | **INDIVIDUAL WORK** |
| 0:55-1:00 | Week 6 Preview | Learn what's next |

**Guided Practice:**
- Instructor will walk through `week5_wine_guided.ipynb`
- You fill in TODOs as we go
- Ask questions during PAUSE moments
- Solutions provided after session

**Quiz:**
- 8 multiple-choice questions
- 10 minutes
- 60% to pass (5/8 correct)
- Covers ALL of Week 5 (Day 1 + Day 2)

---

### After Day 2 (Post-Class)

**Time:** 90-120 minutes
**Goal:** Practice unsupervised learning independently

✅ **Required:** Complete `post_class/week5_postclass_exercise.ipynb`
- NEW dataset (Iris) - different from class
- 50% scaffolding (you write more code than Day 1/Day 2)
- Apply K-Means + PCA on your own
- Solutions provided (`week5_postclass_solutions.ipynb`)

✅ **Bonus (Optional):** `week5_bonus_pca_preprocessing.ipynb`
- Use PCA BEFORE supervised learning
- Compare performance: raw features vs PCA-reduced
- See how PCA fits into ML pipelines

✅ **Reflection:** Fill out `Week5_Self_Assessment.md`
- Rate your understanding (1-5 scale)
- Reflect on Day 2 deep dive
- Identify topics for office hours

---

## 📊 Datasets Used in Week 5

| Dataset | Where Used | Samples | Features | Purpose |
|---------|------------|---------|----------|---------|
| **Mall Customers** | Day 1 live coding (K-Means) | 200 | 5 | Customer segmentation |
| **MNIST Digits** | Day 1 live coding (PCA) | 1,797 | 64 | Dimensionality reduction viz |
| **Wine** | Day 1 pair programming + Day 2 guided | 178 | 13 | Practice both K-Means & PCA |
| **Iris** | Post-class exercise | 150 | 4 | Solo practice |

**Why different datasets?**
- Day 1 live: Learn concepts
- Day 1 pair programming: Practice with support
- Day 2 guided: Practice with instructor
- Post-class: Apply independently

---

## 🎯 Learning Objectives by Material

### Pre-Class Practice
**You'll learn:**
- Difference between supervised vs unsupervised
- K-Means basic workflow (fit, predict, interpret)
- Elbow method intuition

**Scaffolding:** 70% (mostly code provided)

---

### Day 1 Live Session Notebooks

**week5_live_session_kmeans.ipynb:**
- Customer segmentation use case
- Elbow method + silhouette scores
- Cluster interpretation
- **Scaffolding:** 60% (you fill in key calls + analysis)

**week5_live_session_pca.ipynb:**
- MNIST dimensionality reduction
- Variance explained interpretation
- Scree plots
- **Scaffolding:** 60%

---

### Day 1 Pair Programming

**week5_pair_programming.ipynb:**
- "Cluster Detective" exercise
- Focus on INTERPRETATION (not coding)
- Name clusters based on features
- **Scaffolding:** 80% (most code provided)

---

### Day 2 Guided Practice

**week5_wine_guided.ipynb:**
- Complete workflow: K-Means + PCA
- Choosing K (elbow + silhouette)
- Visualize clusters in PCA space
- **Scaffolding:** 70% (fill in key steps)

---

### Post-Class Exercise

**week5_postclass_exercise.ipynb:**
- Apply to NEW dataset (Iris)
- More independence than class
- Test your understanding
- **Scaffolding:** 50% (you write significant code)

---

## 🤔 Common Student Questions

### "Which notebook should I use when?"

**Before Day 1:** `pre_class/week5_preclass_practice.ipynb`
**During Day 1 live coding:** `day1_live_session/week5_live_session_kmeans.ipynb` + `week5_live_session_pca.ipynb`
**During Day 1 pair programming:** `day1_pair_programming/week5_pair_programming.ipynb`
**During Day 2:** `day2_guided_practice/week5_wine_guided.ipynb`
**After Day 2:** `post_class/week5_postclass_exercise.ipynb`

---

### "Do I need to complete pre-class materials?"

**Yes!** Pre-class materials prepare you for Day 1. Without them, live coding will be harder to follow.

---

### "Can I look at solutions during class?"

**No!** Solutions are for AFTER you've attempted the exercise. Use them to check your work, not to copy.

---

### "I didn't finish the post-class exercise. What should I do?"

1. Try for at least 90 minutes on your own
2. If truly stuck, check the solutions for THAT PART only
3. Try to complete the rest yourself
4. Attend office hours if you need help understanding

---

### "The pair programming notebook has too much code provided. Why?"

Pair programming focuses on **interpretation**, not implementation. We provide code so you can focus on:
- Naming clusters
- Understanding what features define each group
- Connecting data science to business decisions

---

### "Can I use different datasets?"

**For practice:** Yes! Try K-Means or PCA on your own data.
**For graded work:** Use the specified datasets (solutions match them).

---

## 📚 Reference Materials

### Week5_Glossary.md
Defines all technical terms:
- Unsupervised learning
- Centroid
- Inertia
- Silhouette score
- Principal component
- Variance explained
- And more!

### Week5_sklearn_cheat_sheet.md
Quick syntax reference:
```python
# K-Means
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3)
labels = kmeans.fit_predict(X)

# PCA
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)
```

### Week5_Student_Workbook.md
Space for notes during Day 1 lecture

---

## ⚠️ Important Reminders

### Feature Scaling is CRITICAL!
K-Means uses distances. **Always** scale features before clustering:
```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

### No "Correct" K
Choosing K is exploratory. Use:
1. Elbow method
2. Silhouette scores
3. Domain knowledge

There's no single right answer!

### PCA Loses Information
When you reduce dimensions, you lose variance. Check `explained_variance_ratio_` to see how much information you retained.

### Unsupervised ≠ No Evaluation
You CAN'T use accuracy (no labels!). Instead:
- K-Means: Inertia, silhouette score
- PCA: Variance explained
- Both: Visualization + interpretation

---

## 🏆 Success Checklist

By the end of Week 5, you should be able to:

- [ ] Explain difference between supervised and unsupervised learning
- [ ] Fit K-Means clustering with sklearn
- [ ] Use elbow method + silhouette scores to choose K
- [ ] Interpret cluster characteristics (feature means)
- [ ] Name clusters based on data patterns
- [ ] Apply PCA for dimensionality reduction
- [ ] Interpret variance explained ratios
- [ ] Visualize high-dimensional data in 2D with PCA
- [ ] Decide when to use K-Means vs PCA
- [ ] Scale features before clustering (ALWAYS!)

**Test yourself:** Complete post-class exercise without looking at solutions!

---

## 🆘 Getting Help

**Stuck on a concept?**
1. Review `Week5_Glossary.md`
2. Re-watch Day 1/Day 2 recordings
3. Check course discussion board
4. Attend office hours

**Code not working?**
1. Check error message carefully
2. Verify you scaled features (`StandardScaler`)
3. Ensure correct sklearn syntax (check cheat sheet)
4. Ask on discussion board with code + error

**Don't understand unsupervised learning?**
→ This is normal! It's a mindset shift from supervised learning.
→ Key: No "right answer" = interpretation matters more than metrics.

---

**Good luck with Week 5! Remember: Unsupervised learning is about discovery, not prediction. 🔍**

---

**Version:** 1.0
**Created:** 2026-03-04
**Restructured following:** WEEK_RESTRUCTURING_METHODOLOGY.md
