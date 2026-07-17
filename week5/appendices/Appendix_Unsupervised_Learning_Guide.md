# Appendix: Unsupervised Learning Guide (K-Means & PCA)

**Purpose:** Complete reference for K-Means Clustering and PCA (Principal Component Analysis)

**When to use:** Reference this guide whenever you need detailed explanations, code examples, or troubleshooting help for unsupervised learning

**Standalone:** This appendix is self-contained - use it during the course or in future projects

---

## 📚 Table of Contents

1. [Unsupervised Learning Overview](#unsupervised-learning-overview)
2. [K-Means Clustering](#k-means-clustering)
3. [Choosing K](#choosing-k)
4. [PCA: Principal Component Analysis](#pca-principal-component-analysis)
5. [Feature Scaling](#feature-scaling)
6. [Sklearn Code Examples](#sklearn-code-examples)
7. [Common Pitfalls](#common-pitfalls)
8. [When to Use Each Method](#when-to-use-each-method)
9. [Business Applications](#business-applications)
10. [Troubleshooting Guide](#troubleshooting-guide)

---

## Unsupervised Learning Overview

### What is Unsupervised Learning?

**Definition:** Machine learning with unlabeled data (no target variable y)

**Goal:** Discover hidden patterns, structure, or groupings in data

**Key difference from supervised learning:**

| Aspect | Supervised Learning | Unsupervised Learning |
|--------|---------------------|----------------------|
| **Training data** | X (features) + y (labels) | X (features) only |
| **Goal** | Predict y from X | Find patterns in X |
| **Evaluation** | Compare predictions to true y | No ground truth - use metrics + interpretation |
| **Examples** | Classification, Regression | Clustering, Dimensionality Reduction |

---

### Main Types of Unsupervised Learning

**1. Clustering**
- Group similar data points together
- Algorithms: K-Means, Hierarchical Clustering, DBSCAN
- Use case: Customer segmentation, document grouping

**2. Dimensionality Reduction**
- Reduce number of features while preserving information
- Algorithms: PCA, t-SNE, UMAP
- Use case: Visualization, feature engineering, noise reduction

**3. Anomaly Detection**
- Identify outliers or unusual patterns
- Algorithms: Isolation Forest, One-Class SVM
- Use case: Fraud detection, quality control

**This course focuses on:** K-Means (clustering) and PCA (dimensionality reduction)

---

## K-Means Clustering

### What is K-Means?

**Definition:** Algorithm that groups data into K clusters based on similarity

**How it works:**
1. Choose K (number of clusters)
2. Randomly initialize K centroids (cluster centers)
3. Assign each point to nearest centroid
4. Update centroids to mean of assigned points
5. Repeat steps 3-4 until convergence (centroids stop moving)

**Result:** K clusters where points within each cluster are similar

---

### K-Means Algorithm in Detail

#### Step 1: Initialize Centroids

```
Randomly place K centroids in feature space

Example (K=3, 2D data):
  Centroid 1: (x=2.5, y=7.8)
  Centroid 2: (x=8.1, y=3.2)
  Centroid 3: (x=4.9, y=5.5)
```

**Note:** Random initialization can lead to different results (run multiple times!)

---

#### Step 2: Assign Points to Nearest Centroid

```
For each data point:
  Calculate distance to each centroid
  Assign point to closest centroid

Distance metric: Usually Euclidean distance
  d = sqrt((x1-x2)² + (y1-y2)²)
```

**Example:**
```python
Point A: (3.0, 7.5)
Distance to Centroid 1: 0.58  ← Closest!
Distance to Centroid 2: 5.84
Distance to Centroid 3: 2.62

→ Assign Point A to Cluster 1
```

---

#### Step 3: Update Centroids

```
For each cluster:
  Calculate mean position of all assigned points
  Move centroid to that position

New centroid = (mean of x-coordinates, mean of y-coordinates)
```

**Example:**
```python
Cluster 1 has points: [(3,7), (2,8), (4,6)]

New centroid:
  x = (3 + 2 + 4) / 3 = 3.0
  y = (7 + 8 + 6) / 3 = 7.0

→ Move Centroid 1 to (3.0, 7.0)
```

---

#### Step 4: Repeat Until Convergence

```
Convergence occurs when:
  • Centroids stop moving (or move very little)
  • Cluster assignments don't change
  • Maximum iterations reached

Typical convergence: 5-20 iterations
```

---

### K-Means Objective Function

**What K-Means minimizes:** Within-cluster sum of squares (WCSS) aka Inertia

```
Inertia = Σ (distance from point to its centroid)²

For all clusters:
  For each point in cluster:
    Add squared distance to cluster's centroid

Goal: Make clusters compact (low inertia)
```

**Formula:**
```
Inertia = Σ(k=1 to K) Σ(i in cluster k) ||x_i - μ_k||²

where:
  K = number of clusters
  x_i = data point i
  μ_k = centroid of cluster k
  ||·|| = Euclidean distance
```

**Lower inertia = Better clustering** (more compact clusters)

---

### K-Means in Sklearn

**Basic usage:**

```python
from sklearn.cluster import KMeans

# Create K-Means model
kmeans = KMeans(n_clusters=3, random_state=42)

# Fit to data and predict clusters
clusters = kmeans.fit_predict(X)

# Get cluster centers
centroids = kmeans.cluster_centers_

# Get inertia
inertia = kmeans.inertia_
```

**Key parameters:**

| Parameter | Default | Description |
|-----------|---------|-------------|
| `n_clusters` | 8 | Number of clusters K |
| `init` | 'k-means++' | Centroid initialization method ('k-means++' or 'random') |
| `n_init` | 10 | Number of times to run with different initializations |
| `max_iter` | 300 | Maximum iterations per run |
| `random_state` | None | Seed for reproducibility |

**Recommended settings:**
```python
kmeans = KMeans(
    n_clusters=5,
    init='k-means++',  # Smart initialization (better than random)
    n_init=10,         # Run 10 times, keep best result
    max_iter=300,      # Usually converges before 300
    random_state=42    # For reproducible results
)
```

---

## Choosing K

### The Challenge

**Problem:** K (number of clusters) is a hyperparameter - you must choose it!

**No single "correct" K** - depends on:
- Data structure
- Business goals
- Interpretability needs

**Three methods to choose K:**
1. Elbow Method (visual)
2. Silhouette Analysis (quantitative)
3. Domain Knowledge (practical)

---

### Method 1: Elbow Method

**Concept:** Plot K vs Inertia, look for "elbow" (bend in curve)

**Steps:**
1. Run K-Means for K = 1, 2, 3, ..., 10
2. Record inertia for each K
3. Plot K (x-axis) vs Inertia (y-axis)
4. Find the "elbow" - where curve bends sharply
5. Optimal K is at the elbow

**Why it works:**
- Left of elbow: Adding clusters greatly reduces inertia (good)
- Right of elbow: Adding clusters barely reduces inertia (diminishing returns)
- Elbow = sweet spot (most benefit without overcomplicating)

**Code example:**

```python
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Calculate inertia for different K
inertias = []
K_range = range(1, 11)

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    inertias.append(kmeans.inertia_)

# Plot elbow curve
plt.figure(figsize=(10, 6))
plt.plot(K_range, inertias, 'o-', linewidth=2, markersize=10)
plt.xlabel('Number of Clusters (K)', fontsize=14)
plt.ylabel('Inertia (WCSS)', fontsize=14)
plt.title('Elbow Method for Optimal K', fontsize=16)
plt.grid(True, alpha=0.3)
plt.show()
```

**Interpretation:**
```
Inertia
  │
  │ \
  │  \
  │   \___  ← Elbow at K=3 or K=4
  │       ───___
  │             ───___
  └─────────────────────> K
   1  2  3  4  5  6  7
```

**Limitations:**
- Sometimes no clear elbow exists (smooth curve)
- Subjective (different people see elbow at different K)
- Use silhouette analysis as confirmation

---

### Method 2: Silhouette Analysis

**Concept:** Measure how well each point fits in its cluster

**Silhouette Score** for a single point:
```
s = (b - a) / max(a, b)

where:
  a = mean distance to points in same cluster
  b = mean distance to points in nearest other cluster

Range: -1 to +1
  +1: Point very close to its cluster (perfect fit)
   0: Point on border between clusters (ambiguous)
  -1: Point closer to other cluster (wrong cluster!)
```

**Average Silhouette Score** (for entire clustering):
```
Average all individual silhouette scores

Interpretation:
  > 0.70: Strong clustering
  0.50-0.70: Moderate clustering
  0.25-0.50: Weak clustering
  < 0.25: No natural clusters
```

**Code example:**

```python
from sklearn.metrics import silhouette_score, silhouette_samples
import numpy as np

# Calculate silhouette for different K
silhouette_scores = []
K_range = range(2, 11)  # Note: K=1 undefined for silhouette

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    cluster_labels = kmeans.fit_predict(X)
    score = silhouette_score(X, cluster_labels)
    silhouette_scores.append(score)
    print(f"K={k}: Silhouette Score = {score:.3f}")

# Best K = highest silhouette score
best_k = K_range[np.argmax(silhouette_scores)]
print(f"\nOptimal K: {best_k}")
```

**Silhouette Plot** (visual analysis):

```python
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def plot_silhouette(X, n_clusters):
    """Create silhouette plot for given K"""
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    cluster_labels = kmeans.fit_predict(X)
    silhouette_avg = silhouette_score(X, cluster_labels)
    sample_silhouette_values = silhouette_samples(X, cluster_labels)

    fig, ax = plt.subplots(figsize=(10, 7))
    y_lower = 10

    for i in range(n_clusters):
        # Get silhouette values for cluster i
        ith_cluster_silhouette_values = \
            sample_silhouette_values[cluster_labels == i]
        ith_cluster_silhouette_values.sort()

        size_cluster_i = ith_cluster_silhouette_values.shape[0]
        y_upper = y_lower + size_cluster_i

        color = cm.nipy_spectral(float(i) / n_clusters)
        ax.fill_betweenx(np.arange(y_lower, y_upper),
                         0, ith_cluster_silhouette_values,
                         facecolor=color, edgecolor=color, alpha=0.7)

        ax.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))
        y_lower = y_upper + 10

    ax.set_title(f'Silhouette Plot (K={n_clusters})')
    ax.set_xlabel('Silhouette Coefficient')
    ax.set_ylabel('Cluster')
    ax.axvline(x=silhouette_avg, color="red", linestyle="--",
               label=f'Average = {silhouette_avg:.2f}')
    ax.legend()
    plt.show()

# Compare different K values
for k in [3, 5, 7]:
    plot_silhouette(X, k)
```

**Good clustering:**
- Most bars extend past 0.5
- Similar cluster sizes (balanced)
- No negative values

**Poor clustering:**
- Short bars (below 0.5)
- Some negative bars (misassigned points)
- Very uneven cluster sizes

---

### Method 3: Domain Knowledge

**Use business judgment:**

**Questions to ask:**
- How many customer segments can we realistically target?
- What's interpretable for stakeholders?
- Do clusters align with existing business categories?

**Example: Customer Segmentation**
```
K=3: "High/Medium/Low spenders"
     → Simple but may miss nuances

K=5: "Budget/Careful/Target/Sensible/Cautious"
     → More detailed, still manageable

K=10: Too many segments
      → Hard to create distinct campaigns
```

**Best practice:** Combine all three methods!
1. Use elbow method to narrow range (e.g., K=3 to K=5)
2. Use silhouette to confirm quality
3. Use domain knowledge to make final decision

---

## PCA: Principal Component Analysis

### What is PCA?

**Definition:** Dimensionality reduction technique that finds "best viewing angles" in high-dimensional data

**Goal:** Reduce number of features while preserving most information

**How it works:**
1. Find direction of maximum variance (PC1)
2. Find next orthogonal direction of maximum variance (PC2)
3. Continue for PC3, PC4, ..., up to # of original features
4. Keep first few PCs (typically 2-10) for visualization or modeling

**Result:** Transform data from high dimensions to low dimensions

---

### PCA Intuition

**Analogy:** Taking photographs of a 3D sculpture

```
3D sculpture (original data):
  • Can't see all details from one angle
  • Need multiple photos to understand shape

PCA finds best camera angles:
  • PC1: Best single photo (captures most variation)
  • PC2: Second-best angle (orthogonal to PC1)
  • PC3: Third-best angle
  • etc.

2-3 photos (PCs) capture essence of sculpture!
```

**Mathematical view:**

```
Original data: X (n_samples × d_features)

PCA transformation:
  1. Center data (subtract mean)
  2. Find eigenvectors of covariance matrix
  3. Sort eigenvectors by eigenvalue (variance)
  4. Project data onto top k eigenvectors

Result: X_pca (n_samples × k_components)
```

---

### Principal Components Explained

**Principal Component (PC):**
- Linear combination of original features
- Orthogonal to other PCs (uncorrelated)
- Captures maximum remaining variance

**Example: 2D → 1D projection**

```
Original features: Height (x1), Weight (x2)

PC1 = 0.7 × Height + 0.7 × Weight
      → Direction of maximum variance
      → "General body size"

If we keep only PC1:
  • Lose some information
  • But capture main pattern (size variation)
```

**3D → 2D example:**

```
Original: Height, Weight, Age

PC1 = 0.6 × Height + 0.6 × Weight + 0.2 × Age
      → "Physical size"

PC2 = 0.1 × Height + 0.1 × Weight + 0.9 × Age
      → "Age dimension"

Reduce to 2D: Keep PC1 and PC2
```

---

### Variance Explained

**Key concept:** Each PC captures a % of total variance

**Example: MNIST digits (784 features)**

```
PC1 explains: 12% of variance
PC2 explains: 8% of variance
PC3 explains: 5% of variance
...
PC20 explains: 0.5% of variance

Cumulative:
  First 2 PCs: 20% of variance
  First 10 PCs: 50% of variance
  First 50 PCs: 80% of variance
  First 200 PCs: 95% of variance
  All 784 PCs: 100% of variance
```

**Choosing number of components:**

1. **For visualization:** Keep 2-3 components
2. **For modeling:** Keep enough for 80-90% variance
3. **Scree plot:** Look for "elbow" (like K-Means)
4. **Kaiser rule:** Keep components with eigenvalue > 1

---

### PCA in Sklearn

**Basic usage:**

```python
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# IMPORTANT: Standardize first!
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply PCA
pca = PCA(n_components=2)  # Reduce to 2 dimensions
X_pca = pca.fit_transform(X_scaled)

# Check variance explained
print(f"Explained variance ratio: {pca.explained_variance_ratio_}")
print(f"Total variance explained: {pca.explained_variance_ratio_.sum():.2%}")

# Get principal components (loadings)
components = pca.components_
```

**Key parameters:**

| Parameter | Description |
|-----------|-------------|
| `n_components` | Number of components to keep (int or float 0-1) |
| `whiten` | Whether to whiten data (normalize variance) |
| `svd_solver` | Algorithm ('auto', 'full', 'arpack', 'randomized') |
| `random_state` | Seed for reproducibility |

**Common patterns:**

```python
# Pattern 1: Keep specific number of components
pca = PCA(n_components=2)  # For visualization

# Pattern 2: Keep enough for X% variance
pca = PCA(n_components=0.95)  # Keep 95% of variance

# Pattern 3: Keep all, then analyze
pca = PCA()  # Keep all components
pca.fit(X_scaled)
# Then plot variance explained to decide how many to use
```

---

### PCA Variance Explained Analysis

**Code example:**

```python
import matplotlib.pyplot as plt
import numpy as np

# Fit PCA with all components
pca = PCA()
pca.fit(X_scaled)

# Get explained variance
explained_var = pca.explained_variance_ratio_
cumulative_var = np.cumsum(explained_var)

# Plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Bar plot: Individual variance
ax1.bar(range(1, len(explained_var) + 1), explained_var)
ax1.set_xlabel('Principal Component')
ax1.set_ylabel('Explained Variance Ratio')
ax1.set_title('Variance Explained by Each PC')

# Line plot: Cumulative variance
ax2.plot(range(1, len(cumulative_var) + 1), cumulative_var, 'o-')
ax2.axhline(y=0.90, color='r', linestyle='--', label='90% threshold')
ax2.set_xlabel('Number of Components')
ax2.set_ylabel('Cumulative Explained Variance')
ax2.set_title('Cumulative Variance Explained')
ax2.legend()

plt.tight_layout()
plt.show()

# How many components for 90% variance?
n_components_90 = np.argmax(cumulative_var >= 0.90) + 1
print(f"Components needed for 90% variance: {n_components_90}")
```

---

### PCA Scree Plot

**Purpose:** Visual method to choose number of components (like elbow plot for K-Means)

**Code example:**

```python
# Fit PCA with all components
pca = PCA()
pca.fit(X_scaled)

# Get eigenvalues (explained variance)
eigenvalues = pca.explained_variance_

# Scree plot
plt.figure(figsize=(10, 6))
plt.plot(range(1, len(eigenvalues) + 1), eigenvalues, 'o-')
plt.xlabel('Component Number')
plt.ylabel('Eigenvalue (Explained Variance)')
plt.title('PCA Scree Plot')
plt.axhline(y=1, color='r', linestyle='--', label='Kaiser criterion (eigenvalue=1)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

**Interpretation:**
- Look for "elbow" where curve flattens
- Kaiser rule: Keep components with eigenvalue > 1
- Typically: 2-10 components for most datasets

---

## Feature Scaling

### Why Scaling is Critical

**Problem:** Features with different scales dominate the algorithm

**Example:**
```
Feature 1: Annual Income ($15,000 - $140,000)
Feature 2: Spending Score (1 - 100)

Without scaling:
  Income has 1000× larger range than spending score
  K-Means will cluster primarily based on income
  Spending score barely matters!
```

**Solution:** Standardize features to same scale

---

### StandardScaler (Z-score normalization)

**Formula:**
```
z = (x - mean) / std_dev

Result:
  • Mean = 0
  • Standard deviation = 1
  • Range: typically -3 to +3
```

**Code:**

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Check: Mean should be ~0, std should be ~1
print(f"Mean: {X_scaled.mean(axis=0)}")
print(f"Std: {X_scaled.std(axis=0)}")
```

**When to use:** Default choice for K-Means and PCA

---

### MinMaxScaler (Range normalization)

**Formula:**
```
x_scaled = (x - min) / (max - min)

Result:
  • Range: [0, 1]
```

**Code:**

```python
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
```

**When to use:** When you need values in specific range [0, 1]

---

### When NOT to Scale

**Don't scale:**
- Tree-based models (Decision Trees, Random Forests) - they don't care about scale
- Already normalized features (e.g., percentages)

**Always scale:**
- K-Means (distance-based)
- PCA (variance-based)
- Neural networks
- SVM
- Any algorithm using distance or gradients

---

## Sklearn Code Examples

### Complete K-Means Pipeline

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# 1. Load data
df = pd.read_csv('mall_customers.csv')
X = df[['Annual Income (k$)', 'Spending Score (1-100)']].values

# 2. Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. Choose K using elbow method
inertias = []
silhouette_scores = []
K_range = range(2, 11)

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    inertias.append(kmeans.inertia_)
    score = silhouette_score(X_scaled, kmeans.labels_)
    silhouette_scores.append(score)

# Plot elbow
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(K_range, inertias, 'o-')
plt.xlabel('K')
plt.ylabel('Inertia')
plt.title('Elbow Method')

plt.subplot(1, 2, 2)
plt.plot(K_range, silhouette_scores, 'o-')
plt.xlabel('K')
plt.ylabel('Silhouette Score')
plt.title('Silhouette Analysis')
plt.tight_layout()
plt.show()

# 4. Fit final model with optimal K
optimal_k = 5  # Based on elbow and silhouette
kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
df['Cluster'] = kmeans.fit_predict(X_scaled)

# 5. Get centroids (in original scale for interpretation)
centroids_scaled = kmeans.cluster_centers_
centroids = scaler.inverse_transform(centroids_scaled)

# 6. Visualize clusters
plt.figure(figsize=(10, 6))
for i in range(optimal_k):
    cluster_data = df[df['Cluster'] == i]
    plt.scatter(cluster_data['Annual Income (k$)'],
                cluster_data['Spending Score (1-100)'],
                label=f'Cluster {i}', s=50)

plt.scatter(centroids[:, 0], centroids[:, 1], marker='X',
            s=300, c='red', edgecolors='black', linewidths=2,
            label='Centroids')

plt.xlabel('Annual Income ($k)')
plt.ylabel('Spending Score')
plt.title('Customer Segmentation')
plt.legend()
plt.show()

# 7. Analyze clusters
for i in range(optimal_k):
    cluster_data = df[df['Cluster'] == i]
    print(f"\nCluster {i}:")
    print(f"  Size: {len(cluster_data)}")
    print(f"  Mean Income: ${cluster_data['Annual Income (k$)'].mean():.0f}k")
    print(f"  Mean Spending: {cluster_data['Spending Score (1-100)'].mean():.1f}")
```

---

### Complete PCA Pipeline

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# 1. Load data (MNIST-like digits)
digits = load_digits()
X = digits.data  # 1797 samples, 64 features (8x8 images)
y = digits.target  # Digit labels (0-9)

# 2. Standardize
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. Determine optimal number of components
pca_full = PCA()
pca_full.fit(X_scaled)

# Plot variance explained
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.bar(range(1, len(pca_full.explained_variance_ratio_) + 1),
        pca_full.explained_variance_ratio_)
plt.xlabel('Component')
plt.ylabel('Variance Explained')
plt.title('Individual Variance')

plt.subplot(1, 2, 2)
cumulative_var = np.cumsum(pca_full.explained_variance_ratio_)
plt.plot(range(1, len(cumulative_var) + 1), cumulative_var, 'o-')
plt.axhline(y=0.90, color='r', linestyle='--')
plt.xlabel('Number of Components')
plt.ylabel('Cumulative Variance')
plt.title('Cumulative Variance Explained')
plt.tight_layout()
plt.show()

# How many components for 90% variance?
n_components_90 = np.argmax(cumulative_var >= 0.90) + 1
print(f"Components for 90% variance: {n_components_90}")

# 4. Apply PCA with 2 components (for visualization)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

print(f"\nReduced from {X.shape[1]} to {X_pca.shape[1]} dimensions")
print(f"Variance explained: {pca.explained_variance_ratio_.sum():.2%}")

# 5. Visualize in 2D
plt.figure(figsize=(10, 8))
scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='tab10',
                     s=20, alpha=0.7)
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.title('MNIST Digits in 2D (via PCA)')
plt.colorbar(scatter, label='Digit')
plt.show()

# 6. Interpret principal components
print("\nFirst PC (most important direction):")
print(pca.components_[0])  # Loadings on original features

# 7. Reconstruct data (inverse transform)
X_reconstructed = pca.inverse_transform(X_pca)
X_reconstructed = scaler.inverse_transform(X_reconstructed)

# Show original vs reconstructed
idx = 0
original = X[idx].reshape(8, 8)
reconstructed = X_reconstructed[idx].reshape(8, 8)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
ax1.imshow(original, cmap='gray')
ax1.set_title('Original')
ax2.imshow(reconstructed, cmap='gray')
ax2.set_title('Reconstructed (2 PCs)')
plt.show()
```

---

## Common Pitfalls

### Pitfall 1: Forgetting to Scale

**Problem:**
```python
# BAD: No scaling
kmeans = KMeans(n_clusters=3)
clusters = kmeans.fit_predict(X)  # Wrong results!
```

**Solution:**
```python
# GOOD: Scale first
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
kmeans = KMeans(n_clusters=3)
clusters = kmeans.fit_predict(X_scaled)
```

**Why:** K-Means uses Euclidean distance. Features with larger scales dominate clustering.

---

### Pitfall 2: Using Wrong K

**Problem:**
```python
# BAD: Arbitrary K
kmeans = KMeans(n_clusters=3)  # Why 3? No justification!
```

**Solution:**
```python
# GOOD: Use elbow + silhouette to choose K
# [Run elbow method and silhouette analysis first]
optimal_k = 5  # Based on analysis
kmeans = KMeans(n_clusters=optimal_k)
```

---

### Pitfall 3: Not Using Multiple Initializations

**Problem:**
```python
# BAD: Single initialization
kmeans = KMeans(n_clusters=3, n_init=1)  # Might get stuck in local optimum
```

**Solution:**
```python
# GOOD: Multiple initializations
kmeans = KMeans(n_clusters=3, n_init=10)  # Runs 10 times, keeps best
```

**Why:** Random initialization can lead to different results. Run multiple times!

---

### Pitfall 4: Not Setting random_state

**Problem:**
```python
# BAD: Results change every run
kmeans = KMeans(n_clusters=3)
clusters1 = kmeans.fit_predict(X)
clusters2 = kmeans.fit_predict(X)  # Different results!
```

**Solution:**
```python
# GOOD: Reproducible results
kmeans = KMeans(n_clusters=3, random_state=42)
clusters1 = kmeans.fit_predict(X)
clusters2 = kmeans.fit_predict(X)  # Same results!
```

---

### Pitfall 5: Ignoring Business Interpretation

**Problem:**
```python
# BAD: Just accept cluster numbers
clusters = kmeans.fit_predict(X)
# "Okay, we have 5 clusters. Done!" ← Wrong!
```

**Solution:**
```python
# GOOD: Interpret and name clusters
clusters = kmeans.fit_predict(X)

# Analyze cluster characteristics
for i in range(5):
    cluster_data = df[clusters == i]
    print(f"Cluster {i}:")
    print(f"  Mean income: ${cluster_data['income'].mean():.0f}")
    print(f"  Mean spending: {cluster_data['spending'].mean():.1f}")
    # Give business name based on patterns

# Name clusters: "Budget Shoppers", "Target Customers", etc.
```

---

### Pitfall 6: PCA Before Train/Test Split

**Problem:**
```python
# BAD: PCA on entire dataset (data leakage!)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)
X_train, X_test = train_test_split(X_pca)  # Test data "saw" training data via PCA!
```

**Solution:**
```python
# GOOD: Split first, then PCA
X_train, X_test = train_test_split(X)

pca = PCA(n_components=2)
X_train_pca = pca.fit_transform(X_train)  # Fit on train only
X_test_pca = pca.transform(X_test)         # Transform test (don't fit!)
```

**Note:** For Week 5 exploratory analysis (no train/test split), this isn't an issue. But crucial for supervised learning!

---

## When to Use Each Method

### Use K-Means When:

✅ **You want to find natural groups in data**
- Customer segmentation
- Document clustering
- Image compression

✅ **Clusters are spherical (circular) and similar size**
- K-Means assumes clusters are compact and roughly equal

✅ **You can specify K (or determine it via elbow/silhouette)**
- Need to know approximate number of groups

✅ **Features are continuous (numeric)**
- K-Means uses Euclidean distance

---

### DON'T Use K-Means When:

❌ **Clusters have irregular shapes**
- Use DBSCAN or Hierarchical Clustering instead

❌ **Clusters have very different sizes**
- K-Means struggles with one large cluster and several tiny ones

❌ **You have categorical features**
- K-Means requires numeric features (use K-Modes for categorical)

❌ **You need hierarchical relationships**
- Use Hierarchical Clustering

---

### Use PCA When:

✅ **You need to visualize high-dimensional data**
- 10+ features → reduce to 2-3 for plotting

✅ **You want to reduce dimensionality for modeling**
- Speed up training (fewer features)
- Reduce overfitting
- Remove noise

✅ **Features are correlated**
- PCA creates uncorrelated components

✅ **You need feature engineering**
- Create new features that capture variance

---

### DON'T Use PCA When:

❌ **Interpretability is critical**
- PCs are linear combinations (hard to interpret)
- Use feature selection instead

❌ **Features are already low-dimensional (< 10)**
- May not gain much benefit

❌ **You need nonlinear dimensionality reduction**
- Use t-SNE or UMAP instead

❌ **Features are not numeric**
- PCA requires continuous features

---

## Business Applications

### Customer Segmentation (K-Means)

**Problem:** Retail company has 100,000 customers, wants to tailor marketing

**Solution:**
```python
# Features: Age, Income, Spending, Frequency
X = df[['age', 'income', 'spending', 'frequency']].values

# Standardize and cluster
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=5, random_state=42)
df['segment'] = kmeans.fit_predict(X_scaled)

# Interpret clusters
# Segment 0: "Budget Conscious" → Send discount coupons
# Segment 1: "High Value" → VIP programs
# Segment 2: "Occasional Shoppers" → Re-engagement campaigns
# etc.
```

**Business value:**
- Targeted marketing (20-40% higher response rates)
- Reduced marketing costs (don't spam wrong segments)
- Increased customer lifetime value

---

### Anomaly Detection (K-Means)

**Problem:** Bank wants to detect fraudulent transactions

**Solution:**
```python
# Features: Transaction amount, time, location, etc.
kmeans = KMeans(n_clusters=10)
kmeans.fit(X_scaled)

# Calculate distance to nearest cluster center
distances = kmeans.transform(X_scaled).min(axis=1)

# Flag transactions far from any cluster (outliers)
threshold = np.percentile(distances, 95)
is_anomaly = distances > threshold

# Review flagged transactions
```

**Business value:**
- Early fraud detection
- Reduced financial losses
- Improved customer trust

---

### Dimensionality Reduction for Visualization (PCA)

**Problem:** Genomics dataset with 20,000 gene expression features - can't visualize

**Solution:**
```python
# 20,000 features → 2 components for visualization
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Plot patients in 2D, colored by disease
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=disease_labels)
```

**Business value:**
- Identify patient subgroups visually
- Discover new disease patterns
- Communicate findings to non-technical stakeholders

---

### Feature Engineering for Supervised Learning (PCA)

**Problem:** High-dimensional dataset (1000 features) causes overfitting

**Solution:**
```python
# Reduce 1000 features → 50 components (preserving 90% variance)
pca = PCA(n_components=0.90)
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)

# Train supervised model on reduced features
model = RandomForestClassifier()
model.fit(X_train_pca, y_train)
```

**Business value:**
- Faster training
- Better generalization (less overfitting)
- Reduced computational costs

---

## Troubleshooting Guide

### Problem: Elbow plot has no clear elbow

**Symptoms:** Smooth curve, hard to identify optimal K

**Solutions:**
1. Use silhouette analysis (more objective)
2. Try domain knowledge (how many segments make business sense?)
3. Test multiple K values and compare interpretability
4. Data may not have natural clusters (try other algorithms)

---

### Problem: K-Means produces unequal cluster sizes

**Symptoms:** One huge cluster, others very small

**Possible causes:**
1. Data doesn't cluster naturally (force-fitting)
2. Features not scaled properly
3. K is too high (creating artificial splits)
4. Outliers affecting centroids

**Solutions:**
- Check if data truly clusters (silhouette scores)
- Verify scaling (StandardScaler applied?)
- Try different K
- Remove outliers or use DBSCAN

---

### Problem: Clusters change every time I run K-Means

**Symptoms:** Different results despite same code

**Cause:** Random initialization without fixing random_state

**Solution:**
```python
# Fix random seed
kmeans = KMeans(n_clusters=5, random_state=42)

# Also run multiple times and keep best
kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
```

---

### Problem: PCA components are hard to interpret

**Symptoms:** Can't explain what PC1 or PC2 means to business

**Cause:** PCs are linear combinations of all features

**Solutions:**
1. Examine loadings (pca.components_) to see which original features contribute most
2. Use feature selection instead of PCA (if interpretability critical)
3. Create business-friendly names based on dominant features
4. Accept that PCA is exploratory (not always interpretable)

---

### Problem: PCA doesn't seem to help

**Symptoms:** 2 PCs capture < 50% variance, visualization not useful

**Possible causes:**
1. Data is already low-dimensional (< 10 features)
2. Features are not correlated (PCA works best with correlation)
3. Need nonlinear dimensionality reduction (try t-SNE)

**Solutions:**
- Check cumulative variance plot - how many PCs for 90%?
- If need many PCs, data may be truly high-dimensional
- Try t-SNE or UMAP for nonlinear structures

---

### Problem: Silhouette scores are all low (< 0.3)

**Symptoms:** Poor clustering regardless of K

**Cause:** Data may not have natural clusters

**Solutions:**
1. Visualize data (PCA to 2D) - do you see distinct groups?
2. Check if features are meaningful for clustering
3. Try hierarchical clustering or DBSCAN
4. Consider that data may not cluster (not all data does!)

---

### Problem: K-Means is slow on large datasets

**Symptoms:** Takes minutes/hours to run

**Solutions:**
1. Use MiniBatchKMeans (faster approximation)
2. Subsample data for initial exploration
3. Reduce dimensionality with PCA first (fewer features)
4. Use fewer n_init runs (trade speed for stability)

```python
from sklearn.cluster import MiniBatchKMeans

# Faster on large datasets
kmeans = MiniBatchKMeans(n_clusters=5, batch_size=1000, random_state=42)
```

---

## Key Takeaways

### K-Means Clustering

1. **Unsupervised:** No labels needed, discovers natural groups
2. **Choose K:** Use elbow method + silhouette analysis + domain knowledge
3. **Always scale:** StandardScaler before K-Means
4. **Interpret clusters:** Give business-friendly names, create actionable strategies
5. **Run multiple times:** Use n_init=10, set random_state for reproducibility

---

### PCA

1. **Dimensionality reduction:** High-D → Low-D while preserving information
2. **Variance explained:** Keep enough PCs for 80-90% variance (or 2-3 for visualization)
3. **Always scale:** StandardScaler before PCA
4. **PCs are uncorrelated:** Orthogonal components
5. **Use for:** Visualization, noise reduction, feature engineering

---

### General Unsupervised Learning

1. **No ground truth:** Evaluation is different (no accuracy metric)
2. **Business interpretation:** Critical skill - turn clusters into action
3. **Exploratory:** Often first step in analysis (discover patterns)
4. **Combine with supervised:** Use clustering as feature, PCA before classification
5. **Domain knowledge:** Essential for validating results

---

## Additional Resources

**Scikit-learn Documentation:**
- K-Means: https://scikit-learn.org/stable/modules/clustering.html#k-means
- PCA: https://scikit-learn.org/stable/modules/decomposition.html#pca

**Tutorials:**
- Scikit-learn clustering tutorial
- PCA step-by-step guide
- Customer segmentation case studies

**Books:**
- "Hands-On Machine Learning" by Aurélien Géron (Chapter 9: Unsupervised Learning)
- "Introduction to Statistical Learning" (Chapter 10: Unsupervised Learning)

---

**Bookmark this appendix - you'll reference it throughout your career as a data scientist!**
