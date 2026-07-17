# Week 5: Unsupervised Learning - Pre-Class Study Guide

**Time Required:** 30 minutes
**Purpose:** Prime your understanding of unsupervised learning before the live session

---

## Welcome to Week 5!

You've mastered **supervised learning** (Weeks 1-4) - predicting targets when you have labels. This week we're tackling **unsupervised learning** - finding patterns when you DON'T have labels!

**The shift:** No more "y" column. No ground truth. The algorithm discovers hidden structure in data.

**Real-world examples:**
- Customer segmentation (no pre-labeled customer types)
- Document clustering (group similar articles automatically)
- Dimensionality reduction (visualize 100D data in 2D)

---

## Pre-Class Activities (Complete Before Live Session)

### Part 1: Watch These Videos (26 minutes total)

Watch in this order:

1. **StatQuest - K-Means Clustering** (9 min)
   https://www.youtube.com/watch?v=4b5d3muPQmA

   **What to focus on:**

   - The 4 steps: Initialize → Assign → Update → Repeat
   - How centroids "move" toward cluster centers
   - Why it's called K-**Means**

2. **StatQuest - PCA Main Ideas in Only 5 Minutes** (5 min)
   https://www.youtube.com/watch?v=HMOI_lkzW08

   **What to focus on:**

   - PCA finds "directions of maximum variance"
   - Dimensionality reduction: 100 features → 2 features
   - Why we need this (can't visualize 100 dimensions!)

3. **StatQuest - PCA Step-by-Step** (12 min)
   https://www.youtube.com/watch?v=FgakZw6K1QQ

   **What to focus on:**

   - How PCA rotates data
   - Variance explained ratio
   - Scree plots for choosing components
   - You DON'T need to understand eigenvectors mathematically!

4. **Numiqo -- PCA** (18 mins)
   https://www.youtube.com/watch?v=_6UjscCJrYE&t=228s

   **Interactive**
   https://numiqo.com/lab/pca

   **What to focus on:**
   -- The same as seen in the above videos just presented differently (It is really good!)
---

## Part 2: Key Concepts to Understand

By the end of the videos, you should have a basic understanding of:

### Supervised vs Unsupervised Learning

| Supervised Learning | Unsupervised Learning |
|---------------------|----------------------|
| Training data: **X + y** (features + labels) | Training data: **X only** (features, no labels) |
| Goal: Predict y from X | Goal: Find patterns/structure in X |
| Examples: Regression, Classification | Examples: Clustering, Dimensionality Reduction |
| Evaluation: Compare to true labels | Evaluation: **No ground truth!** Use quality metrics |
| Weeks 1-4 | Week 5 |

### When to Use Unsupervised Learning

**Scenario 1: No Labels Available**

- Customer segmentation (no pre-labeled segments)
- Discovering news article topics
- Why: Creating labels is expensive or impossible

**Scenario 2: Pattern Discovery**

- Anomaly detection (unusual network traffic)
- Market basket analysis (what products are bought together?)
- Why: Don't know what patterns exist beforehand

**Scenario 3: Dimensionality Reduction**

- Visualize high-dimensional data (1000 features → 2D plot)
- Preprocessing for supervised learning (reduce noise)
- Why: Can't visualize or compute efficiently with too many features

---

### K-Means Clustering (Preview)

**What it does:** Groups similar data points into K clusters

**The algorithm (intuitive):**

1. **Initialize:** Place K random cluster centers (centroids)
2. **Assign:** Each point joins its nearest centroid's cluster
3. **Update:** Move centroids to the mean of their cluster members
4. **Repeat:** Steps 2-3 until centroids stop moving (convergence)

**Key questions we'll answer:**

- How do we choose K (number of clusters)?
- How do we evaluate if clustering is good? (No labels to compare!)
- What makes K-Means different from classification?

**This week's example:** Clustering mall customers by income and spending habits to discover customer segments (Budget Shoppers, High Rollers, etc.)

---

### PCA - Principal Component Analysis (Preview)

**What it does:** Reduces dimensions while preserving information

**Intuition:**

- Imagine 784 features (MNIST: 28x28 pixel images)
- PCA finds the "best viewing angle" - directions with most variance
- Projects data onto these directions (principal components)
- Result: 784 dimensions → 2 dimensions (for visualization!)

**Key concepts:**

- **PC1 (Principal Component 1):** Direction with MOST variance
- **PC2:** Second most variance (perpendicular to PC1)
- **Variance explained:** How much information each component captures
- **Scree plot:** Helps choose how many components to keep

**This week's example:** Visualizing MNIST handwritten digits (64D → 2D scatter plot where similar digits cluster together!)

---

## Part 3: Vocabulary Pre-Reading

These terms will appear frequently in Week 5. You don't need to memorize them now - just get familiar:

| Term | Quick Definition |
|------|------------------|
| **Unsupervised Learning** | ML when training data has features (X) but no labels (y) |
| **Clustering** | Grouping similar data points together |
| **Centroid** | Center of a cluster (mean position of all cluster members) |
| **K-Means** | Clustering algorithm that finds K cluster centers iteratively |
| **Inertia (WCSS)** | Sum of squared distances from points to their centroid (lower = tighter clusters) |
| **Elbow Method** | Plot inertia vs K, look for "elbow" to choose optimal K |
| **Silhouette Score** | Metric for cluster quality (range: -1 to 1, higher = better separation) |
| **Dimensionality Reduction** | Reducing number of features while preserving information |
| **PCA** | Principal Component Analysis - finds directions of maximum variance |
| **Principal Components (PC)** | New axes found by PCA, ordered by variance explained |
| **Variance Explained** | Percentage of total variance captured by each component |
| **Scree Plot** | Plot of variance vs component number, shows how many components to keep |
| **Feature Scaling** | Standardizing features to mean=0, std=1 (CRITICAL for K-Means and PCA!) |

---

## Part 4: Connection to Weeks 1-4

**What stays the same:**

- sklearn API pattern (create model → fit → predict/transform)
- Feature scaling with `StandardScaler`
- Data exploration and visualization
- Train/test splits (for supervised tasks AFTER clustering)

**What's new:**

- No labels (y) during training
- Can't evaluate with accuracy/RMSE (no ground truth!)
- Interpretation is subjective ("What does Cluster 2 represent?")
- Different sklearn methods:
  - `fit()` still trains the model
  - `predict()` assigns clusters (K-Means)
  - `transform()` projects data (PCA)

**The pattern you know still works!**

```python
# Week 1-4: Supervised
model = LogisticRegression()
model.fit(X_train, y_train)          # Train with labels
y_pred = model.predict(X_test)

# Week 5: Unsupervised
model = KMeans(n_clusters=3)
model.fit(X)                         # Train WITHOUT labels!
clusters = model.predict(X)          # Assign cluster labels
```

---

## Part 5: Questions to Think About

Come to the live session with thoughts on these questions:

1. **Customer Segmentation:** A retail company has 10,000 customers with data on age, income, and purchase frequency. They want to create targeted marketing campaigns. Why is this an unsupervised learning problem? (Hint: Do they have pre-labeled customer types?)

2. **Choosing K:** If you're clustering customers, would you prefer K=2 (two segments) or K=100 (one hundred segments)? What are the tradeoffs?

3. **Interpretation:** K-Means assigns customer 1234 to Cluster 3. What does "Cluster 3" mean? How would you explain it to a marketing manager who doesn't know ML?

4. **PCA for Visualization:** You have a dataset with 50 features. You want to visualize it in a 2D scatter plot. Why can't you just pick 2 random features? What does PCA offer?

**These questions have nuanced answers - we'll explore them during the live session!**

---

## Part 6: Pre-Class Practice (Optional but Recommended)

If you have an extra 10-15 minutes, try this quick mental exercise:

**Clustering Exercise:**

Imagine clustering these 9 customers by income and spending:

```
Customer  Income  Spending
   A        Low      Low
   B        Low      Low
   C        Low     High
   D       High      Low
   E       High      Low
   F       High     High
   G      Medium   Medium
   H       High     High
   I        Low     High
```

**Questions:**

1. If K=2, how might K-Means group them?
2. If K=3, what three segments might emerge?
3. Give each cluster a business-friendly name (e.g., "Budget Shoppers")

**Possible K=3 solution:**

- Cluster 0: A, B (Low/Low) → "Budget Shoppers"
- Cluster 1: D, E (High/Low) → "Conservative Wealthy"
- Cluster 2: C, F, H, I (High spending) → "Big Spenders"
- G: Could go to any cluster (it's in the middle!)

**Note:** There's no "right answer"! K-Means might group differently. That's the nature of unsupervised learning!

---

## What to Expect in the Live Session

**Schedule:**

- 0:00-0:15: Week 4 recap & Unsupervised vs Supervised
- 0:15-0:35: Customer segmentation metaphor (the guiding example!)
- 0:35-1:10: K-Means deep dive (algorithm, elbow method, silhouette)
- 1:10-1:25: **BREAK**
- 1:25-1:55: PCA theory (variance explained, scree plots)
- 1:55-2:15: Live coding - Mall Customers K-Means clustering
- 2:15-2:35: Live coding - MNIST PCA visualization (stunning!)
- 2:35-2:55: Pair programming - "Cluster Detective" exercise
- 2:55-3:00: Wrap-up & Week 6 preview

**What to bring:**

- Questions from the videos
- Your Week 4 homework (we'll discuss validation methodology)
- Notebook for taking notes
- Curiosity about pattern discovery!

---

## Success Checklist

Before the live session, you should:

- [ ] Watched StatQuest K-Means video (9 min)
- [ ] Watched StatQuest PCA videos (5 min + 12 min)
- [ ] Reviewed vocabulary list
- [ ] Thought about the discussion questions
- [ ] (Optional) Tried the mental clustering exercise
- [ ] Ready to explore unsupervised learning!

---

## If You're Feeling Overwhelmed

**Don't worry!** Unsupervised learning feels abstract at first because there's no "correct answer" to check against. The live session is designed to make everything concrete through:

- Customer segmentation example (real business application)
- Visual demonstrations (see clusters form!)
- Live coding with Mall Customers data
- Stunning MNIST visualization (you'll SEE why PCA works)
- Pair programming practice

**Remember:** You don't need to master these concepts before class. The pre-work primes your brain. The real learning happens during the live session with hands-on practice!

**The mindset shift:** In supervised learning, we ask "Is my prediction correct?" In unsupervised learning, we ask "Do these patterns make sense for my problem?" This feels uncomfortable at first - that's normal!

---

## Questions Before Class?

If anything is unclear, don't stress! The live session will bring it all together.

**Common questions we'll answer:**

- "How is clustering different from classification?"
- "How do I know if my clusters are good with no labels?"
- "What's the 'right' number of clusters?"
- "Can I use PCA before supervised learning?"
- "Why do we need to scale features for K-Means and PCA?"

---

## Week 5 Datasets (Preview)

**Mall Customers** (Pre-class, Live session K-Means, Pair programming)

- 200 customers
- Features: CustomerID, Gender, Age, Annual Income, Spending Score
- Goal: Discover customer segments for marketing

**MNIST Digits** (Live session PCA)

- 1,797 handwritten digits (0-9)
- 64 features (8x8 pixel images)
- Goal: Visualize high-dimensional data in 2D

**Wine** (Post-class homework)

- 178 wine samples
- 13 chemical features (alcohol, acidity, sugar, etc.)
- Goal: Cluster wines by chemical properties, interpret segments

**Iris** (Bonus exercise - PCA + supervised pipeline)

- 150 flowers, 4 features
- Goal: Use PCA for preprocessing before classification

---

**See you in the live session!**

---

*Week 5 Pre-Class Study Guide v1.0 | January 2026*
