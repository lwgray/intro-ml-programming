"""
Visual Generation Master Script for Week 5 - Unsupervised Learning
===================================================================

This script generates all 8 visual PNG files for Week 5 teaching materials.

Usage:
    python generate_all_visuals.py

Requirements:
    pip install matplotlib numpy pandas scikit-learn seaborn

Output:
    - elbow_method.png
    - kmeans_animation.png
    - mall_customers_clusters.png
    - mnist_2d_pca.png
    - pca_scree_plot.png
    - pca_variance_explained.png
    - silhouette_plot.png
    - supervised_vs_unsupervised.png

Time: ~5 minutes to generate all visuals
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle, FancyArrowPatch, Ellipse
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris, load_digits, make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_samples, silhouette_score
import sys

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

print("="*70)
print("Week 5 Unsupervised Learning - Visual Generation Script")
print("="*70)
print()

# =============================================================================
# Visual 1: Elbow Method
# =============================================================================
print("[1/8] Creating elbow_method.png...")
try:
    # Generate sample data
    X, _ = make_blobs(n_samples=300, centers=4, n_features=2, random_state=42)

    # Calculate inertias
    inertias = []
    K_range = range(1, 11)
    for k in K_range:
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        kmeans.fit(X)
        inertias.append(kmeans.inertia_)

    # Create figure
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # Left: Clear elbow
    ax1.plot(K_range, inertias, marker='o', linewidth=2, markersize=10, color='#2196F3')
    ax1.set_xlabel('Number of Clusters (K)', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Inertia (Within-Cluster Sum of Squares)', fontsize=12, fontweight='bold')
    ax1.set_title('Elbow Method - Clear Elbow at K=4', fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.axvline(x=4, color='red', linestyle='--', linewidth=2, label='Elbow at K=4')
    ax1.legend(fontsize=11)

    # Add annotation
    ax1.annotate('Elbow Point\n(Optimal K)', xy=(4, inertias[3]), xytext=(6, inertias[3] + 200),
                arrowprops=dict(arrowstyle='->', color='red', lw=2),
                fontsize=11, fontweight='bold', color='red')

    # Right: Explanation
    ax2.axis('off')
    ax2.text(0.1, 0.9, 'How to Use the Elbow Method:', fontsize=14, fontweight='bold',
            transform=ax2.transAxes)

    explanation = """
    1. Plot inertia vs K (1 to 10 clusters)

    2. Look for the "elbow" bend in the curve
       - Sharp bend = clear optimal K
       - Gradual curve = subjective choice

    3. Elbow = diminishing returns point
       - Adding more clusters doesn't help much

    4. Inertia always decreases with more K
       - K=N (one cluster per point) gives 0
       - That's not useful clustering!

    5. Combine with silhouette score
       - Elbow gives range (e.g., K=3-5)
       - Silhouette ranks quality

    ⚠️ Limitation: Elbow may not exist or
       may be ambiguous for some datasets
    """

    ax2.text(0.05, 0.05, explanation, fontsize=10, transform=ax2.transAxes,
            verticalalignment='bottom',
            bbox=dict(boxstyle='round,pad=1', facecolor='#FFF9C4', edgecolor='#F57F17', linewidth=2))

    plt.tight_layout()
    plt.savefig('elbow_method.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("   ✓ elbow_method.png created")
except Exception as e:
    print(f"   ✗ Error: {e}")

# =============================================================================
# Visual 2: K-Means Animation (4 frames)
# =============================================================================
print("[2/8] Creating kmeans_animation.png...")
try:
    # Generate data
    np.random.seed(42)
    X, _ = make_blobs(n_samples=150, centers=3, n_features=2, cluster_std=0.6, random_state=42)

    fig, axes = plt.subplots(2, 2, figsize=(14, 12))
    axes = axes.flatten()

    # Initial random centroids
    init_centroids = np.array([[0, 0], [2, 2], [-2, 2]])

    titles = [
        'Step 1: Initialize K=3 Random Centroids',
        'Step 2: Assign Points to Nearest Centroid',
        'Step 3: Recompute Centroids (Means)',
        'Step 4: Converged - Final Clusters'
    ]

    for step in range(4):
        ax = axes[step]

        if step == 0:
            # Initial state
            ax.scatter(X[:, 0], X[:, 1], c='gray', s=50, alpha=0.5)
            ax.scatter(init_centroids[:, 0], init_centroids[:, 1],
                      c='red', s=300, marker='X', edgecolors='black', linewidth=2,
                      label='Initial Centroids')
            ax.legend(fontsize=10)

        elif step == 1:
            # First assignment
            kmeans = KMeans(n_clusters=3, init=init_centroids, n_init=1, max_iter=1, random_state=42)
            labels = kmeans.fit_predict(X)
            ax.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', s=50, alpha=0.6)
            ax.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
                      c='red', s=300, marker='X', edgecolors='black', linewidth=2)

        elif step == 2:
            # After recomputation
            kmeans = KMeans(n_clusters=3, init=init_centroids, n_init=1, max_iter=2, random_state=42)
            labels = kmeans.fit_predict(X)
            ax.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', s=50, alpha=0.6)
            ax.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
                      c='red', s=300, marker='X', edgecolors='black', linewidth=2,
                      label='Updated Centroids')
            ax.legend(fontsize=10)

        else:
            # Final converged state
            kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
            labels = kmeans.fit_predict(X)
            ax.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', s=50, alpha=0.6, edgecolors='k')
            ax.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
                      c='red', s=300, marker='X', edgecolors='black', linewidth=2,
                      label='Final Centroids')
            ax.legend(fontsize=10)

        ax.set_title(titles[step], fontsize=12, fontweight='bold')
        ax.set_xlabel('Feature 1', fontsize=10)
        ax.set_ylabel('Feature 2', fontsize=10)
        ax.grid(True, alpha=0.3)

    plt.suptitle('K-Means Algorithm: Lloyd\'s Method', fontsize=16, fontweight='bold', y=0.995)
    plt.tight_layout()
    plt.savefig('kmeans_animation.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("   ✓ kmeans_animation.png created")
except Exception as e:
    print(f"   ✗ Error: {e}")

# =============================================================================
# Visual 3: Mall Customers Clusters (Example)
# =============================================================================
print("[3/8] Creating mall_customers_clusters.png...")
try:
    # Generate synthetic customer data
    np.random.seed(42)

    # 3 customer segments
    budget = np.random.multivariate_normal([30, 30], [[50, 10], [10, 50]], 60)
    middle = np.random.multivariate_normal([50, 50], [[50, 10], [10, 50]], 70)
    premium = np.random.multivariate_normal([70, 75], [[40, 15], [15, 40]], 70)

    X = np.vstack([budget, middle, premium])
    true_labels = np.array([0]*60 + [1]*70 + [2]*70)

    # Fit K-Means
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    clusters = kmeans.fit_predict(X)

    # Create visualization
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Left: Clusters
    scatter = axes[0].scatter(X[:, 0], X[:, 1], c=clusters, cmap='viridis', s=80, alpha=0.6, edgecolors='k')
    axes[0].scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
                   c='red', s=400, marker='X', edgecolors='black', linewidth=3, label='Centroids')
    axes[0].set_xlabel('Age', fontsize=12, fontweight='bold')
    axes[0].set_ylabel('Spending Score', fontsize=12, fontweight='bold')
    axes[0].set_title('Mall Customer Segmentation (K=3)', fontsize=14, fontweight='bold')
    axes[0].legend(fontsize=11)
    axes[0].grid(True, alpha=0.3)
    plt.colorbar(scatter, ax=axes[0], label='Cluster')

    # Right: Interpretation
    axes[1].axis('off')
    axes[1].text(0.1, 0.9, 'Cluster Interpretation:', fontsize=14, fontweight='bold',
                transform=axes[1].transAxes)

    interpretation = """
    Cluster 0 (Purple): "Budget Shoppers"
    • Younger customers (age ~30)
    • Low spending scores (~30)
    • Target: Discount campaigns, loyalty rewards

    Cluster 1 (Green): "Middle Class"
    • Middle-aged (age ~50)
    • Moderate spending (~50)
    • Target: Value-for-money promotions

    Cluster 2 (Yellow): "Premium Customers"
    • Older, affluent (age ~70)
    • High spending scores (~75)
    • Target: Premium products, VIP programs

    📊 Business Action:
    Marketing can now create 3 targeted
    campaigns instead of one-size-fits-all!

    💡 Key Insight:
    Unsupervised learning discovered these
    segments WITHOUT predefined labels.
    """

    axes[1].text(0.05, 0.05, interpretation, fontsize=10, transform=axes[1].transAxes,
                verticalalignment='bottom',
                bbox=dict(boxstyle='round,pad=1', facecolor='#E8F5E9', edgecolor='#4CAF50', linewidth=2))

    plt.tight_layout()
    plt.savefig('mall_customers_clusters.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("   ✓ mall_customers_clusters.png created")
except Exception as e:
    print(f"   ✗ Error: {e}")

# =============================================================================
# Visual 4: MNIST 2D PCA
# =============================================================================
print("[4/8] Creating mnist_2d_pca.png...")
try:
    # Load digits dataset (lightweight version of MNIST)
    digits = load_digits()
    X = digits.data
    y = digits.target

    # Apply PCA
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X)

    # Create visualization
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Left: PCA visualization
    scatter = axes[0].scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='tab10', s=20, alpha=0.6, edgecolors='none')
    axes[0].set_xlabel(f'PC1 ({pca.explained_variance_ratio_[0]:.1%} variance)', fontsize=12, fontweight='bold')
    axes[0].set_ylabel(f'PC2 ({pca.explained_variance_ratio_[1]:.1%} variance)', fontsize=12, fontweight='bold')
    axes[0].set_title('MNIST Digits: 64D → 2D via PCA', fontsize=14, fontweight='bold')
    axes[0].grid(True, alpha=0.3)
    plt.colorbar(scatter, ax=axes[0], label='Digit', ticks=range(10))

    # Right: Interpretation
    axes[1].axis('off')
    axes[1].text(0.1, 0.9, 'What Does This Show?', fontsize=14, fontweight='bold',
                transform=axes[1].transAxes)

    interpretation = """
    Original: 64 features (8x8 pixel values)
    Reduced: 2 principal components

    Variance Explained:
    • PC1: {:.1f}%
    • PC2: {:.1f}%
    • Total: {:.1f}%

    Observations:
    ✓ Some digits cluster well (0, 1, 6)
    ✓ Others overlap (4 vs 9, 3 vs 8)
    ✓ PCA found 2 "directions" capturing
      most variance in 64-dimensional space

    Use Case:
    • Visualization (2D/3D)
    • Preprocessing before clustering
    • Compression (64 → 20 features)

    ⚠️ Note:
    Lost {:.1f}% of information!
    Trade-off: Interpretability vs accuracy
    """.format(pca.explained_variance_ratio_[0]*100,
              pca.explained_variance_ratio_[1]*100,
              pca.explained_variance_ratio_.sum()*100,
              (1 - pca.explained_variance_ratio_.sum())*100)

    axes[1].text(0.05, 0.05, interpretation, fontsize=9.5, transform=axes[1].transAxes,
                verticalalignment='bottom', family='monospace',
                bbox=dict(boxstyle='round,pad=1', facecolor='#E3F2FD', edgecolor='#2196F3', linewidth=2))

    plt.tight_layout()
    plt.savefig('mnist_2d_pca.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("   ✓ mnist_2d_pca.png created")
except Exception as e:
    print(f"   ✗ Error: {e}")

# =============================================================================
# Visual 5: PCA Scree Plot
# =============================================================================
print("[5/8] Creating pca_scree_plot.png...")
try:
    # Use digits dataset
    digits = load_digits()
    X = digits.data

    # Apply PCA with all components
    pca = PCA()
    pca.fit(X)

    # Create figure
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # Left: Scree plot
    ax1.plot(range(1, len(pca.explained_variance_ratio_)+1), pca.explained_variance_ratio_,
            marker='o', linewidth=2, markersize=6, color='#FF5722')
    ax1.set_xlabel('Principal Component', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Variance Explained Ratio', fontsize=12, fontweight='bold')
    ax1.set_title('Scree Plot - Variance per Component', fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.axvline(x=10, color='green', linestyle='--', linewidth=2, label='Elbow ~10 components')
    ax1.legend(fontsize=10)
    ax1.set_xlim(0, 40)

    # Right: Cumulative variance
    cumulative_variance = np.cumsum(pca.explained_variance_ratio_)
    ax2.plot(range(1, len(cumulative_variance)+1), cumulative_variance,
            marker='o', linewidth=2, markersize=4, color='#4CAF50')
    ax2.axhline(y=0.8, color='orange', linestyle='--', linewidth=2, label='80% variance')
    ax2.axhline(y=0.95, color='red', linestyle='--', linewidth=2, label='95% variance')
    ax2.set_xlabel('Number of Components', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Cumulative Variance Explained', fontsize=12, fontweight='bold')
    ax2.set_title('Cumulative Variance Explained', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.legend(fontsize=10)
    ax2.set_xlim(0, 40)
    ax2.set_ylim(0, 1.05)

    # Add text box
    n_80 = np.argmax(cumulative_variance >= 0.8) + 1
    n_95 = np.argmax(cumulative_variance >= 0.95) + 1

    textstr = f'Original: 64 features\n80% variance: {n_80} components\n95% variance: {n_95} components'
    ax2.text(0.6, 0.2, textstr, transform=ax2.transAxes, fontsize=11,
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

    plt.suptitle('How Many Principal Components to Keep?', fontsize=16, fontweight='bold', y=0.98)
    plt.tight_layout()
    plt.savefig('pca_scree_plot.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("   ✓ pca_scree_plot.png created")
except Exception as e:
    print(f"   ✗ Error: {e}")

# =============================================================================
# Visual 6: PCA Variance Explained
# =============================================================================
print("[6/8] Creating pca_variance_explained.png...")
try:
    # Generate example data
    digits = load_digits()
    X = digits.data

    pca = PCA(n_components=10)
    pca.fit(X)

    # Create visualization
    fig, ax = plt.subplots(figsize=(12, 6))

    components = range(1, 11)
    variance_ratios = pca.explained_variance_ratio_

    bars = ax.bar(components, variance_ratios, color=['#2196F3', '#4CAF50', '#FF9800', '#9C27B0', '#F44336'] + ['#757575']*5,
                 edgecolor='black', linewidth=1.5, alpha=0.8)

    ax.set_xlabel('Principal Component', fontsize=14, fontweight='bold')
    ax.set_ylabel('Variance Explained Ratio', fontsize=14, fontweight='bold')
    ax.set_title('PCA: Variance Explained by Each Component', fontsize=16, fontweight='bold')
    ax.set_xticks(components)
    ax.grid(axis='y', alpha=0.3)

    # Add percentage labels on bars
    for i, (bar, val) in enumerate(zip(bars, variance_ratios)):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
               f'{val:.1%}',
               ha='center', va='bottom', fontsize=10, fontweight='bold')

    # Add cumulative line
    ax2 = ax.twinx()
    cumsum = np.cumsum(variance_ratios)
    ax2.plot(components, cumsum, color='red', marker='D', linewidth=3, markersize=8, label='Cumulative')
    ax2.set_ylabel('Cumulative Variance Explained', fontsize=14, fontweight='bold', color='red')
    ax2.tick_params(axis='y', labelcolor='red')
    ax2.set_ylim(0, 1.1)
    ax2.legend(loc='lower right', fontsize=12)

    # Add interpretation box
    textstr = f"""
    Key Insights:
    • PC1 captures {variance_ratios[0]:.1%} of variance
    • First 3 PCs capture {cumsum[2]:.1%}
    • First 10 PCs capture {cumsum[9]:.1%}

    Rule of Thumb:
    • Visualization: 2-3 components
    • Preprocessing: 80-90% variance
    • Choose based on use case!
    """

    ax.text(0.65, 0.6, textstr, transform=ax.transAxes, fontsize=10,
           verticalalignment='top',
           bbox=dict(boxstyle='round,pad=0.8', facecolor='#FFF59D', edgecolor='#F57F17', linewidth=2))

    plt.tight_layout()
    plt.savefig('pca_variance_explained.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("   ✓ pca_variance_explained.png created")
except Exception as e:
    print(f"   ✗ Error: {e}")

# =============================================================================
# Visual 7: Silhouette Plot
# =============================================================================
print("[7/8] Creating silhouette_plot.png...")
try:
    # Generate sample data
    X, _ = make_blobs(n_samples=150, centers=3, n_features=2, random_state=42)

    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    for idx, K in enumerate([2, 3, 4]):
        ax = axes[idx]

        # Fit K-Means
        kmeans = KMeans(n_clusters=K, random_state=42, n_init=10)
        labels = kmeans.fit_predict(X)

        # Calculate silhouette
        silhouette_vals = silhouette_samples(X, labels)
        silhouette_avg = silhouette_score(X, labels)

        # Plot
        y_lower = 10
        for i in range(K):
            cluster_silhouette_vals = silhouette_vals[labels == i]
            cluster_silhouette_vals.sort()

            size_cluster_i = cluster_silhouette_vals.shape[0]
            y_upper = y_lower + size_cluster_i

            color = plt.cm.viridis(float(i) / K)
            ax.fill_betweenx(np.arange(y_lower, y_upper),
                           0, cluster_silhouette_vals,
                           facecolor=color, edgecolor=color, alpha=0.7)

            ax.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))
            y_lower = y_upper + 10

        ax.axvline(x=silhouette_avg, color="red", linestyle="--", linewidth=2,
                  label=f'Avg: {silhouette_avg:.3f}')
        ax.set_xlabel("Silhouette Coefficient", fontsize=11, fontweight='bold')
        ax.set_ylabel("Cluster", fontsize=11, fontweight='bold')
        ax.set_title(f'K={K} (Score: {silhouette_avg:.3f})', fontsize=13, fontweight='bold')
        ax.set_xlim([-0.2, 1])
        ax.legend(fontsize=9)
        ax.grid(axis='x', alpha=0.3)

    plt.suptitle('Silhouette Analysis for Different K Values', fontsize=16, fontweight='bold', y=0.98)
    plt.tight_layout()
    plt.savefig('silhouette_plot.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("   ✓ silhouette_plot.png created")
except Exception as e:
    print(f"   ✗ Error: {e}")

# =============================================================================
# Visual 8: Supervised vs Unsupervised
# =============================================================================
print("[8/8] Creating supervised_vs_unsupervised.png...")
try:
    fig, axes = plt.subplots(1, 2, figsize=(16, 8))

    # Left: Supervised Learning
    ax = axes[0]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    ax.text(5, 9.5, 'SUPERVISED LEARNING', ha='center', fontsize=18, fontweight='bold',
           color='#1976D2', bbox=dict(boxstyle='round,pad=0.5', facecolor='#BBDEFB', edgecolor='#1976D2', linewidth=2))

    # Input box
    input_box = FancyBboxPatch((0.5, 7), 4, 1.5, boxstyle="round,pad=0.1",
                              facecolor='#E8F5E9', edgecolor='#4CAF50', linewidth=2)
    ax.add_patch(input_box)
    ax.text(2.5, 7.75, 'Input: X (features) + y (labels)', ha='center', fontsize=11, fontweight='bold')
    ax.text(2.5, 7.3, 'Example: Images + "cat/dog"', ha='center', fontsize=9, style='italic')

    # Arrow
    arrow1 = FancyArrowPatch((2.5, 6.8), (2.5, 6), arrowstyle='->', mutation_scale=30,
                           linewidth=3, color='#333333')
    ax.add_patch(arrow1)
    ax.text(3.5, 6.4, 'Learn\nMapping', ha='left', fontsize=9, fontweight='bold')

    # Model box
    model_box = FancyBboxPatch((0.5, 4), 4, 1.5, boxstyle="round,pad=0.1",
                              facecolor='#FFF9C4', edgecolor='#F57F17', linewidth=2)
    ax.add_patch(model_box)
    ax.text(2.5, 4.75, 'Model: Learn f(X) = y', ha='center', fontsize=11, fontweight='bold')
    ax.text(2.5, 4.3, 'Goal: Predict labels', ha='center', fontsize=9, style='italic')

    # Arrow
    arrow2 = FancyArrowPatch((2.5, 3.8), (2.5, 3), arrowstyle='->', mutation_scale=30,
                           linewidth=3, color='#333333')
    ax.add_patch(arrow2)
    ax.text(3.5, 3.4, 'Predict', ha='left', fontsize=9, fontweight='bold')

    # Output box
    output_box = FancyBboxPatch((0.5, 1), 4, 1.5, boxstyle="round,pad=0.1",
                               facecolor='#F3E5F5', edgecolor='#9C27B0', linewidth=2)
    ax.add_patch(output_box)
    ax.text(2.5, 1.75, 'Output: Predicted labels', ha='center', fontsize=11, fontweight='bold')
    ax.text(2.5, 1.3, 'Evaluate: Accuracy, F1', ha='center', fontsize=9, style='italic')

    # Examples
    examples_sup = """
    Examples:
    • Classification (spam/not spam)
    • Regression (predict price)
    • Weeks 1-4 of this course!

    Key: HAVE labels (ground truth)
    """
    ax.text(6, 5, examples_sup, fontsize=10, verticalalignment='center',
           bbox=dict(boxstyle='round,pad=0.8', facecolor='#E1F5FE', edgecolor='#0288D1', linewidth=2))

    # Right: Unsupervised Learning
    ax = axes[1]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    ax.text(5, 9.5, 'UNSUPERVISED LEARNING', ha='center', fontsize=18, fontweight='bold',
           color='#E64A19', bbox=dict(boxstyle='round,pad=0.5', facecolor='#FFCCBC', edgecolor='#E64A19', linewidth=2))

    # Input box
    input_box = FancyBboxPatch((0.5, 7), 4, 1.5, boxstyle="round,pad=0.1",
                              facecolor='#E8F5E9', edgecolor='#4CAF50', linewidth=2)
    ax.add_patch(input_box)
    ax.text(2.5, 7.75, 'Input: X only (NO labels)', ha='center', fontsize=11, fontweight='bold')
    ax.text(2.5, 7.3, 'Example: Customer data', ha='center', fontsize=9, style='italic')

    # Arrow
    arrow1 = FancyArrowPatch((2.5, 6.8), (2.5, 6), arrowstyle='->', mutation_scale=30,
                           linewidth=3, color='#333333')
    ax.add_patch(arrow1)
    ax.text(3.5, 6.4, 'Find\nPatterns', ha='left', fontsize=9, fontweight='bold')

    # Model box
    model_box = FancyBboxPatch((0.5, 4), 4, 1.5, boxstyle="round,pad=0.1",
                              facecolor='#FFF9C4', edgecolor='#F57F17', linewidth=2)
    ax.add_patch(model_box)
    ax.text(2.5, 4.75, 'Model: Discover structure', ha='center', fontsize=11, fontweight='bold')
    ax.text(2.5, 4.3, 'Goal: Group/Reduce/Discover', ha='center', fontsize=9, style='italic')

    # Arrow
    arrow2 = FancyArrowPatch((2.5, 3.8), (2.5, 3), arrowstyle='->', mutation_scale=30,
                           linewidth=3, color='#333333')
    ax.add_patch(arrow2)
    ax.text(3.5, 3.4, 'Interpret', ha='left', fontsize=9, fontweight='bold')

    # Output box
    output_box = FancyBboxPatch((0.5, 1), 4, 1.5, boxstyle="round,pad=0.1",
                               facecolor='#F3E5F5', edgecolor='#9C27B0', linewidth=2)
    ax.add_patch(output_box)
    ax.text(2.5, 1.75, 'Output: Patterns/Groups', ha='center', fontsize=11, fontweight='bold')
    ax.text(2.5, 1.3, 'Evaluate: Interpretation!', ha='center', fontsize=9, style='italic')

    # Examples
    examples_unsup = """
    Examples:
    • K-Means (customer segments)
    • PCA (dimensionality reduction)
    • Week 5 of this course!

    Key: NO labels (discover patterns)
    """
    ax.text(6, 5, examples_unsup, fontsize=10, verticalalignment='center',
           bbox=dict(boxstyle='round,pad=0.8', facecolor='#FCE4EC', edgecolor='#C2185B', linewidth=2))

    plt.suptitle('Supervised vs Unsupervised Learning', fontsize=20, fontweight='bold', y=0.98)
    plt.tight_layout()
    plt.savefig('supervised_vs_unsupervised.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("   ✓ supervised_vs_unsupervised.png created")
except Exception as e:
    print(f"   ✗ Error: {e}")

# =============================================================================
# Summary
# =============================================================================
print()
print("="*70)
print("Visual Generation Complete!")
print("="*70)
print()
print("Generated files:")
print("  1. ✓ elbow_method.png")
print("  2. ✓ kmeans_animation.png")
print("  3. ✓ mall_customers_clusters.png")
print("  4. ✓ mnist_2d_pca.png")
print("  5. ✓ pca_scree_plot.png")
print("  6. ✓ pca_variance_explained.png")
print("  7. ✓ silhouette_plot.png")
print("  8. ✓ supervised_vs_unsupervised.png")
print()
print("All visuals saved in current directory.")
print("Ready for use in Week 5 teaching materials!")
print("="*70)
