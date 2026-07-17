# Week 5: Unsupervised Learning - Student Workbook

**Date:** ________________
**Name:** ________________

**Purpose:** Note-taking template for today's live session
**How to use:** Fill in the blanks as the instructor explains each concept

---

## 📋 Session Overview

**Today's Topic:** K-Means Clustering and PCA (Principal Component Analysis)
**Time:** 3 hours (0:00 - 3:00)
**Goal:** Master unsupervised learning - discover patterns without labels!

---

## 🎯 Learning Objectives (Check off as you learn!)

By the end of today, I will be able to:

- [ ] Explain the difference between supervised and unsupervised learning
- [ ] Build a complete K-Means clustering pipeline
- [ ] Use the elbow method to choose optimal K
- [ ] Calculate and interpret silhouette scores
- [ ] Interpret clusters in business terms
- [ ] Understand when to scale features for K-Means
- [ ] Apply PCA for dimensionality reduction
- [ ] Interpret explained variance ratios
- [ ] Create and interpret scree plots
- [ ] Visualize high-dimensional data in 2D

---

## Part 1: Week 4 Recap & Week 5 Preview (0:00 - 0:10)

### Quick Wins from Week 4

What was the most important lesson from Week 4?

____________________________________________________________________

____________________________________________________________________

### Supervised vs Unsupervised Learning

**Fill in the table:**

| Aspect | Supervised Learning | Unsupervised Learning |
|--------|--------------------|-----------------------|
| **Has labels?** | Yes (y exists) | _________________ |
| **Goal** | Predict target | _________________ |
| **Example algorithms** | Linear Regression, Logistic Regression | _________________ |
| **Evaluation** | Accuracy, RMSE, etc. | _________________ |
| **Example task** | Predict house price | _________________ |

---

## Part 2: Quick Demo - Customer Segmentation (0:10 - 0:25)

### The Business Problem

**Scenario:** You're a mall marketing manager with 200 customers.

**Question:** How do you group them for targeted marketing?

____________________________________________________________________

____________________________________________________________________

### First K-Means Results

**Accuracy:** Not applicable! (Why?) ________________________________

**Number of clusters found:** _______

**Key observation:**

____________________________________________________________________

____________________________________________________________________

---

## Part 3: Unsupervised Learning Concepts (0:25 - 0:45)

### What is Unsupervised Learning?

**Definition:** Finding _____________ in data without _____________

**No labels means:**
- No train/test split needed
- No accuracy metric
- Evaluation is _____________ (interpretative)

**Real-world examples:**
- Customer segmentation: _______________________________________
- Document clustering: _______________________________________
- Anomaly detection: _______________________________________

### Types of Unsupervised Learning

**Clustering:**
- Groups similar data points together
- Algorithms: _____________, Hierarchical, DBSCAN

**Dimensionality Reduction:**
- Reduces number of features
- Algorithms: _____________, t-SNE, UMAP

**Today's focus:** K-Means (clustering) and PCA (dimensionality reduction)

---

## Part 4: K-Means Theory (0:55 - 1:15)

### The K-Means Algorithm

**Step 1:** Choose K (number of clusters)

**Step 2:** _________________________ (Place K random centroids)

**Step 3:** _________________________ (Assign each point to nearest centroid)

**Step 4:** _________________________ (Update centroids to mean of assigned points)

**Step 5:** Repeat steps 3-4 until _________________________

**Draw the K-Means process:** (Sketch as instructor explains)

```
Iteration 1:          Iteration 2:          Final:
  ●  ●               ●  ●                ●  ●
 ●  ●               ●  ●                ●  ●
  ✕                  ✕                   ✕
   ●  ●               ●  ●                ●  ●
  ●  ●               ●  ●                ●  ●
```

### Key K-Means Concepts

**Centroid:** _____________________________________________________

**Inertia:** Sum of squared _____________ from points to their centroids
- Lower inertia = _____________ clusters
- But K=1000 has very low inertia (overfitting!)

**Distance metric:** K-Means uses _____________ distance
- Why scaling matters: Features must be on _____________ scale
- Without scaling: Large-range features _____________ clustering

### The K-Means Challenge

**Big question:** How do we choose K?

**Problem:** Can't try K=1, 2, 3, ..., 200 and pick best - would overfit!

**Solution:** The _____________ method

---

## Part 5: Choosing K - The Elbow Method (1:15 - 1:30)

### Elbow Method Steps

1. Try different K values (e.g., K = 2, 3, 4, 5, ..., 10)
2. For each K, calculate _____________
3. Plot K vs inertia
4. Look for the "_____________" - where curve flattens

**Draw the elbow plot:** (Sketch as instructor explains)

```
Inertia
    │ ●
    │  \
    │   \
    │    ●___     ← ELBOW here
    │        \___●___●
    └──────────────────> K
      2  3  4  5  6  7  8

Choose K at the elbow: K = _____
```

### Silhouette Score

**What it measures:** How similar points are to their own cluster vs other clusters

**Range:** _____ (worst) to _____ (best)

**Interpretation guide:**

| Score | Interpretation |
|-------|----------------|
| > 0.7 | _________________ |
| 0.5 - 0.7 | _________________ |
| 0.25 - 0.5 | _________________ |
| < 0.25 | _________________ |

**Formula (high-level):**
```
Silhouette = (b - a) / max(a, b)

where:
  a = average distance to points in same cluster
  b = average distance to points in nearest other cluster
```

---

## Part 6: Live Coding - Mall Customers K-Means (1:55 - 2:15)

### Dataset: Mall Customers

- **Features:** Age, Annual Income, Spending Score
- **Samples:** _____ customers
- **Goal:** Find customer segments for targeted marketing

### K-Means Workflow (Fill in as we code!)

```python
# Step 1: Load data
df = pd.read_csv('_____________')

# Step 2: Select features
X = df[['Annual Income (k$)', '_____________']].values

# Step 3: Scale features (CRITICAL!)
scaler = _____________
X_scaled = scaler._____________

# Step 4: Elbow method
inertias = []
for k in range(2, 9):
    kmeans = KMeans(n_clusters=_____, random_state=_____)
    kmeans._____________
    inertias.append(_____)

# Step 5: Plot elbow
plt.plot(K_range, inertias, '_____')

# Step 6: Fit K-Means with optimal K
kmeans_final = KMeans(n_clusters=_____, random_state=42)
clusters = kmeans_final._____________

# Step 7: Calculate silhouette score
sil_score = silhouette_score(_____, _____)

# Step 8: Visualize clusters
plt.scatter(df['Income'], df['Spending'], c=_____, cmap='viridis')
```

### Cluster Interpretation ⭐ **CRITICAL**

**This is THE most important skill!**

**For each cluster, identify:**

**Cluster 0:**
- Income: _______ (Low/Medium/High)
- Spending: _______ (Low/Medium/High)
- **Business name:** "_____________________"
- **Marketing strategy:** _____________________________________

**Cluster 1:**
- Income: _______ 
- Spending: _______
- **Business name:** "_____________________"
- **Marketing strategy:** _____________________________________

**Cluster 2:**
- Income: _______ 
- Spending: _______
- **Business name:** "_____________________"
- **Marketing strategy:** _____________________________________

**Cluster 3:**
- Income: _______ 
- Spending: _______
- **Business name:** "_____________________"
- **Marketing strategy:** _____________________________________

**Cluster 4:**
- Income: _______ 
- Spending: _______
- **Business name:** "_____________________"
- **Marketing strategy:** _____________________________________

**The lesson:**

Clustering finds patterns, but ______ interpret what they mean!

---

## Part 7: PCA Theory (2:15 - 2:35)

### Understanding Variance First

**Variance = spread of data**

Dataset with LOW variance:
```
Heights: [65, 67, 68, 70, 71, 72, 73]
→ Clustered together (similar values)
```

Dataset with HIGH variance:
```
Heights: [5, 12, 25, 35, 45, 62, 88]
→ Spread out (diverse values)
```

**Key insight:** High variance = _____________ information

---

### Direction in 2D Data

**[Sketch as instructor draws on whiteboard]**

```
    Weight
    │   ●●
    │  ●●●●
    │ ●●●●●●
    │●●●●●●
    │ ●●●
    └────────── Height

[Three arrows to draw:]
→ Horizontal: _____________
↑ Vertical: _____________
↗ Diagonal: _____________ ← This is PC1!
```

Question: Which DIRECTION are points most spread out?

Answer: _____________ direction has maximum variance

---

### What is PCA?

**PCA = Principal Component Analysis**

**Goal:** Find direction of maximum _____________ to preserve most _____________

**How it works:**
1. Find direction of maximum _____________  (PC1)
2. Find second direction orthogonal to PC1 with max variance (PC2)
3. Continue for PC3, PC4, ...

**Draw PCA projection:** (Sketch as instructor explains)

```
Original 2D:              After PCA:

   ●   ●                    ●●●●●
  ●   ●      →              (compressed to 1D)
   ●   ●
```

### Key PCA Concepts

**Principal Component (PC):**
- A new feature that's a linear combination of original features
- PC1 = direction of _____________ variance
- PC2 = second highest variance (orthogonal to PC1)

**Explained Variance Ratio:**
- % of total variance captured by each PC
- PC1 explains the most (e.g., 15%)
- All PCs sum to _______

**Example:**
```
PC1: 15% variance
PC2: 10% variance
PC3: 8% variance
...
PC64: 0.1% variance

Total: 100%
```

### PCA Use Cases

**Use Case #1: Visualization**
- High-dimensional data → 2D or 3D
- Today's focus: MNIST 64D → 2D

**Use Case #2: Preprocessing**
- Reduce features before supervised learning
- Example: 100 features → 20 PCs → faster training

**Use Case #3: Noise Reduction**
- Keep top PCs, discard noisy low-variance PCs

**Use Case #4: Data Compression**
- Store fewer features, save space

---

## Part 8: Live Coding - MNIST PCA (2:15 - 2:35)

### Dataset: MNIST Digits

- **Samples:** 1,797 handwritten digits
- **Features:** 8×8 pixels = _____ pixel values
- **Classes:** Digits 0-9
- **Challenge:** Can't visualize 64 dimensions!

### PCA Workflow (Fill in as we code!)

```python
# Step 1: Load MNIST digits
from sklearn.datasets import load_digits
digits = _____________
X, y = digits.data, digits.target

# Step 2: Scale features
scaler = StandardScaler()
X_scaled = scaler._____________

# Step 3: Fit PCA with all components
pca_full = PCA()
pca_full._____________
var_ratio = pca_full.explained_variance_ratio_

# Step 4: Cumulative variance
cum_var = np.cumsum(_____)
print(f"First 2 PCs: {cum_var[1]:.1%}")  # ~20-25%

# Step 5: Create scree plot
plt.plot(range(1, 21), var_ratio[:20], '_____')

# Step 6: Reduce to 2D
pca_2d = PCA(n_components=_____)
X_pca_2d = pca_2d._____________

# Step 7: Visualize in 2D
plt.scatter(X_pca_2d[:, 0], X_pca_2d[:, 1], c=_____, cmap='tab10')
```

### PCA Results

**Original dimensions:** _______

**After PCA:** 2

**Variance explained by 2 PCs:** ______%

**Variance lost:** ______%

**Key observation:**

Lost 75% of variance, but can still see _____________ in 2D plot!

### Interpreting the 2D Plot

**What we see:**
- Different digits form distinct _____________
- Some digits separate well (e.g., 0, 1, 6)
- Some overlap (e.g., 3, 5, 8) because they're visually _____________

**The tradeoff:**
- More components = more _____________ retained
- Fewer components = easier to _____________

---

## Part 9: Pair Programming - Cluster Detective (2:35 - 2:55)

### The Challenge

**Scenario:** Wine dataset with 3 pre-computed clusters

**Your task:**
1. Analyze cluster characteristics (mean values)
2. Identify distinguishing _____________
3. Name each cluster
4. Propose _____________ uses

### My Findings

**Cluster 0:**
- Characteristics: __________________________________________
- Name: "_______________________"

**Cluster 1:**
- Characteristics: __________________________________________
- Name: "_______________________"

**Cluster 2:**
- Characteristics: __________________________________________
- Name: "_______________________"

**Key features that distinguish clusters:**

1. _____________________________________________________________

2. _____________________________________________________________

3. _____________________________________________________________

---

## Part 10: Wrap-Up (2:55 - 3:00)

### Three Most Important Things I Learned Today

1. ____________________________________________________________________

   ____________________________________________________________________

2. ____________________________________________________________________

   ____________________________________________________________________

3. ____________________________________________________________________

   ____________________________________________________________________

### Questions I Still Have

1. ____________________________________________________________________

2. ____________________________________________________________________

3. ____________________________________________________________________

### Homework Preview

**Post-class exercise:** Wine dataset clustering

**Key differences from live session:**
- ______% scaffolding (less than today!)
- Full K-Means + PCA pipeline
- Cluster interpretation required

**Bonus exercise:** PCA + supervised learning

---

## Quick Reference Card (Keep This Handy!)

### K-Means Workflow
```
1. Scale features (StandardScaler)
2. Choose K (elbow method)
3. Fit K-Means
4. Calculate silhouette score
5. Visualize clusters
6. INTERPRET clusters (business meaning)
```

### PCA Workflow
```
1. Scale features (StandardScaler)
2. Fit PCA with all components
3. Analyze variance explained
4. Create scree plot
5. Choose n_components
6. Reduce dimensionality
7. Visualize in 2D/3D
```

### Key Metrics

**K-Means:**
```
Inertia = sum of squared distances
Silhouette = cluster quality measure
  >0.7: Excellent
  0.5-0.7: Good
  <0.5: Weak
```

**PCA:**
```
Explained variance ratio = % variance per PC
Cumulative variance = total % retained
Aim for 85-95% for preprocessing
Use 2-3 PCs for visualization
```

### sklearn Code Snippets

```python
# K-Means
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=5, random_state=42)
clusters = kmeans.fit_predict(X_scaled)

# Silhouette
from sklearn.metrics import silhouette_score
score = silhouette_score(X_scaled, clusters)

# PCA
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
```

---

## Post-Session Action Items

**Before next week:**
- [ ] Complete post-class exercise (Wine clustering)
- [ ] Review K-Means until you can explain it to a friend
- [ ] Review PCA until you can explain it to a friend
- [ ] Try the bonus PCA + classification exercise
- [ ] Fill out self-assessment
- [ ] Review Week 5 glossary

**For deeper learning:**
- [ ] Watch StatQuest: K-Means Clustering
- [ ] Watch StatQuest: Principal Component Analysis (PCA)
- [ ] Practice interpreting clusters with different datasets

---

**Great work today! You've mastered unsupervised learning basics!** 🎓

---

*Week 5 Student Workbook v1.0 | February 2026*
