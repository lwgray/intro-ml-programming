# Week 5 Self-Assessment

**Check your understanding of Unsupervised Learning (K-Means & PCA)**

---

## How to Use This Self-Assessment

1. **Answer each question** honestly without looking at notes first
2. **Check your answers** against the answer key at the bottom
3. **Revisit materials** for any topics you struggled with
4. **Target:** 80%+ correct on each section before moving to Week 6

---

## Section 1: Unsupervised vs Supervised Learning (5 questions)

### Question 1.1
**What's the key difference between supervised and unsupervised learning?**

A) Supervised is faster
B) Supervised has labeled data (y), unsupervised doesn't
C) Unsupervised is more accurate
D) Supervised only works on small datasets

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 1.2
**Which task is unsupervised learning?**

A) Predicting house prices
B) Classifying emails as spam/not spam
C) Grouping customers by purchasing behavior
D) Predicting student grades

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 1.3
**Why can't you use accuracy for unsupervised learning?**

A) It's too slow to compute
B) There are no true labels to compare against
C) sklearn doesn't support it
D) Unsupervised models are always 100% accurate

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 1.4
**True or False: In unsupervised learning, there's always one "correct" answer.**

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 1.5
**Which evaluation approach is valid for unsupervised learning?**

A) Test set accuracy
B) Precision and recall
C) Silhouette score + visualization + domain expert review
D) Confusion matrix

<details>
<summary>Your Answer: _____</summary>
</details>

---

## Section 2: K-Means Clustering (10 questions)

### Question 2.1
**What does K represent in K-Means?**

A) Number of features
B) Number of clusters
C) Number of samples
D) Number of iterations

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 2.2
**How does K-Means assign data points to clusters?**

A) Randomly
B) Based on labels
C) By distance to nearest centroid
D) By feature importance

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 2.3
**What is a centroid?**

A) The first data point in a cluster
B) The mean position of all points in a cluster
C) The most common data point
D) The cluster with the most points

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 2.4
**What is inertia in K-Means?**

A) Training speed
B) Sum of squared distances from points to their nearest centroid
C) Number of iterations
D) Cluster purity

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 2.5
**Why is feature scaling CRITICAL for K-Means?**

A) It makes training faster
B) K-Means uses distances; different scales would bias clustering
C) sklearn requires it
D) It prevents overfitting

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 2.6
**Complete this K-Means code:**
```python
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=_____, random_state=42)
clusters = kmeans.______(X_scaled)  # fit_predict
```

<details>
<summary>Your Answer:</summary>
</details>

---

### Question 2.7
**What does `random_state=42` do in K-Means?**

A) Sets the number of clusters
B) Ensures reproducible initialization of centroids
C) Controls training speed
D) Nothing - it's optional

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 2.8
**True or False: K-Means always converges to the global optimal solution.**

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 2.9
**What does `n_init=10` in KMeans do?**

A) Runs K-Means 10 times with different initializations and picks the best
B) Uses 10 clusters
C) Trains for 10 iterations
D) Uses 10% of the data

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 2.10
**How do you interpret clusters after fitting K-Means?**

A) Check accuracy
B) Calculate cluster means and look for distinguishing features
C) Use a confusion matrix
D) Clusters are not interpretable

<details>
<summary>Your Answer: _____</summary>
</details>

---

## Section 3: PCA (Principal Component Analysis) (10 questions)

### Question 3.1
**What does PCA do?**

A) Classifies data into categories
B) Reduces dimensionality by creating new uncorrelated features that capture variance
C) Scales features
D) Clusters data

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 3.2
**What are principal components?**

A) The most important original features
B) New axes that capture maximum variance
C) Cluster centers
D) Feature means

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 3.3
**What does `explained_variance_ratio_` tell you?**

A) How many features to keep
B) What percentage of total variance each PC captures
C) The accuracy of PCA
D) The number of clusters

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 3.4
**If PC1 explains 72% and PC2 explains 23%, what's the total variance captured by 2D PCA?**

A) 72%
B) 95%
C) 49%
D) 100%

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 3.5
**Why use PCA?**

A) To increase accuracy
B) To visualize high-D data in 2D/3D, remove noise, or speed up models
C) To scale features
D) To create clusters

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 3.6
**Complete this PCA code:**
```python
from sklearn.decomposition import PCA

pca = PCA(n_components=_____)
X_pca = pca.______(X_scaled)  # fit_transform
```

<details>
<summary>Your Answer:</summary>
</details>

---

### Question 3.7
**Should you scale features before PCA?**

A) No, PCA doesn't care about scale
B) Yes! PCA finds directions of maximum variance - scale affects variance
C) Only for classification
D) Only if you have missing data

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 3.8
**What's the difference between PCA and K-Means?**

A) They're the same
B) PCA reduces dimensions, K-Means groups data
C) PCA is supervised, K-Means is unsupervised
D) K-Means reduces dimensions, PCA groups data

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 3.9
**Can you use PCA BEFORE K-Means clustering?**

A) No, they're incompatible
B) Yes! Reduce dimensions with PCA, then cluster in lower-D space
C) Only for visualization
D) Only if you have >1000 features

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 3.10
**True or False: PCA always improves model performance.**

<details>
<summary>Your Answer: _____</summary>
</details>

---

## Section 4: Choosing K (7 questions)

### Question 4.1
**What is the elbow method?**

A) A way to scale features
B) Plot K vs inertia; choose K where the curve "bends" (diminishing returns)
C) A clustering algorithm
D) A type of cross-validation

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 4.2
**What is the silhouette score?**

A) A measure of cluster cohesion and separation (range: -1 to +1)
B) The accuracy of clustering
C) The number of clusters
D) The distance between centroids

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 4.3
**What does a silhouette score of 0.7 mean?**

A) 70% accuracy
B) Well-defined clusters (good separation and cohesion)
C) 7 clusters
D) Poor clustering

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 4.4
**Which K is better: silhouette = 0.3 or silhouette = 0.6?**

A) 0.3 (lower is better)
B) 0.6 (higher is better, up to +1)
C) They're equally good
D) Need more information

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 4.5
**What if the elbow method shows K=3 but silhouette is highest at K=2?**

A) Always choose the elbow
B) Always choose highest silhouette
C) Consider both + domain knowledge; there's no single right answer
D) Average them (K=2.5)

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 4.6
**Complete this silhouette score code:**
```python
from sklearn.metrics import silhouette_score

score = silhouette_score(_____, _____)  # X_scaled, labels
```

<details>
<summary>Your Answer:</summary>
</details>

---

### Question 4.7
**True or False: There's always a single "correct" K value.**

<details>
<summary>Your Answer: _____</summary>
</details>

---

## Section 5: Interpretation & Evaluation (8 questions)

### Question 5.1
**How do you name/describe clusters after K-Means?**

A) Clusters are numbered, no need to name them
B) Calculate cluster means and identify distinguishing features
C) Use accuracy to label them
D) Clusters can't be interpreted

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 5.2
**What does `df.groupby('cluster').mean()` tell you?**

A) The number of points in each cluster
B) The mean feature values for each cluster (helps interpret characteristics)
C) The cluster accuracy
D) The silhouette score

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 5.3
**Why visualize clusters in PCA space?**

A) To calculate accuracy
B) To see cluster separation in 2D when original data is high-dimensional
C) PCA is required for K-Means
D) To choose K

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 5.4
**You visualize clusters in 2D PCA space that captures 45% variance. Clusters look overlapping. What does this mean?**

A) K-Means failed
B) Choose a different K
C) Clusters might be more separated in the full D-dimensional space; 55% variance is hidden
D) Always use 3D PCA instead

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 5.5
**Which is NOT a valid way to evaluate unsupervised clustering?**

A) Silhouette score
B) Test set accuracy
C) Visualization
D) Domain expert review

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 5.6
**True or False: Inertia decreases as K increases.**

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 5.7
**What's a "good" silhouette score?**

A) > 0.5 (generally good), > 0.7 (strong)
B) > 0.9 only
C) < 0.5
D) Exactly 1.0

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 5.8
**How do you decide if clustering results are "useful"?**

A) Check test accuracy
B) Ask: Do clusters match business needs? Do they tell a meaningful story?
C) Check R² score
D) Clustering is always useful

<details>
<summary>Your Answer: _____</summary>
</details>

---

## Section 6: Practical Application (5 questions)

### Question 6.1
**You have customer data with features: age, income, purchase_frequency. Before K-Means, what MUST you do?**

A) PCA
B) Scale features with StandardScaler
C) Remove outliers
D) Nothing

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 6.2
**What's the correct unsupervised workflow?**

A) Fit K-Means → Evaluate accuracy
B) Scale → Choose K (elbow/silhouette) → Fit K-Means → Interpret → Validate with domain expert
C) PCA → K-Means → Test set
D) Train/test split → K-Means → Accuracy

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 6.3
**You have a 100-dimensional dataset. You want to visualize it. What's the best approach?**

A) K-Means only
B) PCA to 2D, then visualize
C) Plot all 100 features
D) Unsupervised learning can't visualize high-D data

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 6.4
**When would you apply PCA BEFORE K-Means?**

A) Never
B) Always
C) When you have many features (>20) to reduce noise and dimensionality
D) Only for visualization

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 6.5
**How much variance should you retain when using PCA for preprocessing (before K-Means)?**

A) 50% is enough
B) 90-95%+ to preserve most information
C) 100% (defeats the purpose)
D) Exactly 2 components always

<details>
<summary>Your Answer: _____</summary>
</details>

---

## Section 7: Code Debugging (3 questions)

### Question 7.1
**What's wrong with this code?**
```python
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=3)
clusters = kmeans.fit_predict(X)  # X is NOT scaled!
```

<details>
<summary>Your Answer:</summary>
</details>

---

### Question 7.2
**What's wrong with this code?**
```python
pca = PCA(n_components=2)
X_pca = pca.transform(X_scaled)  # Before fitting!
```

<details>
<summary>Your Answer:</summary>
</details>

---

### Question 7.3
**What's wrong with this code?**
```python
# Trying to calculate accuracy for K-Means
from sklearn.metrics import accuracy_score

kmeans = KMeans(n_clusters=3)
clusters = kmeans.fit_predict(X_scaled)

accuracy = accuracy_score(y_true, clusters)  # What's y_true?
```

<details>
<summary>Your Answer:</summary>
</details>

---

## Section 8: Day 2 Deep Dive Reflection (7 questions)

### Question 8.1
**From Day 2 Deep Dive: Why is choosing K challenging?**

A) It's always K=3
B) No ground truth; must balance elbow, silhouette, and domain knowledge
C) sklearn chooses it automatically
D) It doesn't matter

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 8.2
**What's the "elbow" in the elbow method?**

A) The K with highest inertia
B) The point where inertia decrease slows (diminishing returns)
C) Always K=5
D) The K with lowest silhouette

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 8.3
**How does PCA relate to eigenvectors (from Day 2 deep dive)?**

A) Principal components ARE the eigenvectors of the covariance matrix
B) They're unrelated
C) Eigenvectors are only for supervised learning
D) PCA avoids eigenvectors

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 8.4
**From the deep dive: What does "variance explained" mean in PCA?**

A) The accuracy of PCA
B) How much of the data's spread/variability each PC captures
C) The number of clusters
D) The distance between points

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 8.5
**From Day 2: Is 55% variance explained "good" for visualization?**

A) No, always need 95%+
B) Yes for quick exploration, but acknowledge you're losing 45% of information
C) Perfect - exactly what you need
D) Variance doesn't matter for visualization

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 8.6
**From the deep dive: Can domain knowledge override silhouette scores when choosing K?**

A) No, always trust silhouette
B) Yes! If K=4 makes business sense but K=3 has higher silhouette, K=4 might still be better
C) Domain knowledge is irrelevant
D) Only if silhouette < 0.3

<details>
<summary>Your Answer: _____</summary>
</details>

---

### Question 8.7
**True or False (from Day 2): PCA finds linear combinations of original features that maximize variance.**

<details>
<summary>Your Answer: _____</summary>
</details>

---

## Scoring Guide

**Section 1 (Supervised vs Unsupervised):** _____ / 5
**Section 2 (K-Means):** _____ / 10
**Section 3 (PCA):** _____ / 10
**Section 4 (Choosing K):** _____ / 7
**Section 5 (Interpretation):** _____ / 8
**Section 6 (Practical):** _____ / 5
**Section 7 (Debugging):** _____ / 3
**Section 8 (Day 2 Deep Dive):** _____ / 7

**Total:** _____ / 55

**Percentage:** _____ %

---

## Interpretation

- **90-100%:** Excellent! You're ready for Week 6 (Neural Networks)
- **80-89%:** Good! Review topics you missed
- **70-79%:** Decent foundation, but review weak areas before Week 6
- **Below 70%:** Revisit Week 5 materials and exercises before continuing

---

# Answer Key

<details>
<summary>Click to reveal answers (only after attempting all questions!)</summary>

## Section 1: Unsupervised vs Supervised Learning

1.1: **B** - Supervised has labels (y), unsupervised doesn't
1.2: **C** - Grouping customers (clustering)
1.3: **B** - No true labels to compare against
1.4: **False** - Interpretation is subjective; no single "correct" answer
1.5: **C** - Silhouette + visualization + domain expert

## Section 2: K-Means Clustering

2.1: **B** - Number of clusters
2.2: **C** - By distance to nearest centroid
2.3: **B** - Mean position of all points in cluster
2.4: **B** - Sum of squared distances to centroids
2.5: **B** - K-Means uses distances; different scales bias clustering
2.6: `3` (or your chosen K), `fit_predict`
2.7: **B** - Ensures reproducible centroid initialization
2.8: **False** - Can get stuck in local optima (that's why `n_init` exists)
2.9: **A** - Runs 10 times with different initializations, picks best
2.10: **B** - Calculate cluster means and look for distinguishing features

## Section 3: PCA

3.1: **B** - Reduces dimensionality via uncorrelated features capturing variance
3.2: **B** - New axes that capture maximum variance
3.3: **B** - Percentage of total variance each PC captures
3.4: **B** - 95% (72% + 23%)
3.5: **B** - Visualize high-D data, remove noise, speed up models
3.6: `2` (or your desired number), `fit_transform`
3.7: **B** - Yes! PCA finds max variance - scale affects variance
3.8: **B** - PCA reduces dimensions, K-Means groups data
3.9: **B** - Yes! Reduce dimensions first, then cluster
3.10: **False** - Can hurt performance if you discard informative variance

## Section 4: Choosing K

4.1: **B** - Plot K vs inertia; choose K where curve bends
4.2: **A** - Measure of cluster cohesion/separation (range: -1 to +1)
4.3: **B** - Well-defined clusters
4.4: **B** - 0.6 is better (higher = better)
4.5: **C** - Consider both + domain knowledge
4.6: `X_scaled`, `labels`
4.7: **False** - No single "correct" K

## Section 5: Interpretation & Evaluation

5.1: **B** - Calculate cluster means and identify distinguishing features
5.2: **B** - Mean feature values for each cluster
5.3: **B** - See cluster separation in 2D when original is high-D
5.4: **C** - Clusters might be more separated in full space; 55% variance is hidden
5.5: **B** - Test set accuracy (no labels!)
5.6: **True** - Inertia decreases as K increases (K=N gives inertia=0)
5.7: **A** - >0.5 generally good, >0.7 strong
5.8: **B** - Do clusters match business needs? Tell a meaningful story?

## Section 6: Practical Application

6.1: **B** - Scale features with StandardScaler
6.2: **B** - Scale → Choose K → Fit K-Means → Interpret → Validate
6.3: **B** - PCA to 2D, then visualize
6.4: **C** - When you have many features (>20)
6.5: **B** - 90-95%+ to preserve information

## Section 7: Code Debugging

7.1: X must be scaled before K-Means! Use `X_scaled = StandardScaler().fit_transform(X)` first
7.2: Must call `fit()` or `fit_transform()` before `transform()`. Should be: `X_pca = pca.fit_transform(X_scaled)`
7.3: Unsupervised learning has no `y_true` labels! Can't use accuracy. Use silhouette_score instead.

## Section 8: Day 2 Deep Dive Reflection

8.1: **B** - No ground truth; must balance elbow, silhouette, and domain knowledge
8.2: **B** - Point where inertia decrease slows (diminishing returns)
8.3: **A** - Principal components ARE the eigenvectors of covariance matrix
8.4: **B** - How much of the data's spread/variability each PC captures
8.5: **B** - OK for quick exploration, but acknowledge 45% information loss
8.6: **B** - Yes! Domain knowledge can override metrics
8.7: **True** - PCA finds linear combinations maximizing variance

</details>

---

## Next Steps

Based on your score:

**If you scored 85%+:**
- ✅ Move to Week 6 materials (Neural Networks)
- ✅ Consider the bonus PCA preprocessing notebook
- ✅ Try clustering on your own dataset (Kaggle!)

**If you scored 75-84%:**
- 📚 Review sections where you scored <80%
- 📚 Redo post-class Iris exercise
- 📚 Watch Day 2 deep dive recording again

**If you scored <75%:**
- 📚 Rewatch Day 1 live session recording
- 📚 Redo ALL Week 5 exercises (pre-class, pair programming, post-class)
- 📚 Schedule office hours with instructor
- 📚 Don't move to Week 6 until you hit 80%+

---

## Additional Resources

**StatQuest Videos:**
- K-Means Clustering: https://youtu.be/4b5d3muPQmA
- PCA Main Ideas: https://youtu.be/HMOI_lkzW08
- PCA Step-by-Step: https://youtu.be/FgakZw6K1QQ

**sklearn Documentation:**
- K-Means: https://scikit-learn.org/stable/modules/clustering.html#k-means
- PCA: https://scikit-learn.org/stable/modules/decomposition.html#pca
- Silhouette Score: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html

**Practice:**
- Week 5 post-class Iris exercise
- Week 5 bonus PCA preprocessing notebook
- Kaggle unsupervised learning competitions

---

*This self-assessment covers all Week 5 learning objectives (Day 1 + Day 2). Use it to identify gaps before Week 6!*
