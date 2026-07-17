"""
K-Means Animation Generator - Step-by-Step Version
Shows the algorithm measuring distances point-by-point, then moving centroids.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from sklearn.datasets import make_blobs

# Set random seed for reproducibility
np.random.seed(42)

# Generate data
n_samples = 300
n_features = 2
n_clusters = 4

X, y_true = make_blobs(n_samples=n_samples,
                       n_features=n_features,
                       centers=n_clusters,
                       cluster_std=2.5,
                       center_box=(-10, 10),
                       random_state=123)

class KMeansStepByStepAnimator:
    def __init__(self, X, n_clusters=3):
        self.X = X
        self.n_clusters = n_clusters
        self.n_samples = X.shape[0]

        # Initialize centroids at corners (bad initialization for dramatic effect)
        x_min, x_max = X[:, 0].min(), X[:, 0].max()
        y_min, y_max = X[:, 1].min(), X[:, 1].max()
        x_range = x_max - x_min
        y_range = y_max - y_min

        if n_clusters == 4:
            self.centroids = np.array([
                [x_min - 0.4*x_range, y_min - 0.4*y_range],
                [x_max + 0.4*x_range, y_min - 0.4*y_range],
                [x_min - 0.4*x_range, y_max + 0.4*y_range],
                [x_max + 0.4*x_range, y_max + 0.4*y_range],
            ])
        else:
            self.centroids = np.random.uniform(
                low=[x_min - 0.5*x_range, y_min - 0.5*y_range],
                high=[x_max + 0.5*x_range, y_max + 0.5*y_range],
                size=(n_clusters, 2)
            )

        self.history = []
        self.labels = np.full(self.n_samples, -1)  # -1 means "gray/unassigned"

        # Store initial state - all points gray, centroids visible
        self.history.append({
            'centroids': self.centroids.copy(),
            'labels': self.labels.copy(),
            'step_type': 'initialization',
            'iteration': 0,
            'description': 'Initial Setup: Centroids placed, all points unassigned'
        })

    def fit_with_detailed_history(self, max_iterations=10):
        """Run k-means with detailed frame-by-frame history"""

        for iteration in range(max_iterations):
            old_centroids = self.centroids.copy()

            # ASSIGNMENT PHASE - point by point
            # First, reset all points to gray
            self.labels = np.full(self.n_samples, -1)
            self.history.append({
                'centroids': self.centroids.copy(),
                'labels': self.labels.copy(),
                'step_type': 'reset_to_gray',
                'iteration': iteration + 1,
                'description': f'Iteration {iteration + 1}: Reset points to measure distances'
            })

            # Calculate distances for all points
            distances = np.zeros((self.n_samples, self.n_clusters))
            for k in range(self.n_clusters):
                distances[:, k] = np.linalg.norm(self.X - self.centroids[k], axis=1)

            new_labels = np.argmin(distances, axis=1)

            # Assign points one by one (show every 10th point to keep frame count reasonable)
            points_to_show = list(range(0, self.n_samples, max(1, self.n_samples // 40)))
            if self.n_samples - 1 not in points_to_show:
                points_to_show.append(self.n_samples - 1)  # Always show the last point

            for point_idx in points_to_show:
                # Update labels up to this point
                self.labels[:point_idx + 1] = new_labels[:point_idx + 1]

                self.history.append({
                    'centroids': self.centroids.copy(),
                    'labels': self.labels.copy(),
                    'step_type': 'assigning_points',
                    'iteration': iteration + 1,
                    'progress': (point_idx + 1) / self.n_samples,
                    'description': f'Measuring distances: {point_idx + 1}/{self.n_samples} points assigned'
                })

            # All points assigned - show complete assignment
            self.labels = new_labels
            self.history.append({
                'centroids': self.centroids.copy(),
                'labels': self.labels.copy(),
                'step_type': 'assignment_complete',
                'iteration': iteration + 1,
                'description': f'All points assigned to nearest centroid'
            })

            # UPDATE PHASE - move centroids
            new_centroids = np.zeros((self.n_clusters, 2))
            for k in range(self.n_clusters):
                points_in_cluster = self.X[self.labels == k]
                if len(points_in_cluster) > 0:
                    new_centroids[k] = points_in_cluster.mean(axis=0)
                else:
                    new_centroids[k] = self.centroids[k]

            self.centroids = new_centroids

            self.history.append({
                'centroids': self.centroids.copy(),
                'labels': self.labels.copy(),
                'step_type': 'centroids_updated',
                'iteration': iteration + 1,
                'description': f'Centroids moved to cluster centers'
            })

            # Check convergence
            if np.allclose(old_centroids, self.centroids, atol=0.01):
                print(f"Converged after {iteration + 1} iterations")
                break

        return self

# Create animator and run
print("Running K-Means with detailed step-by-step tracking...")
kmeans = KMeansStepByStepAnimator(X, n_clusters=n_clusters)
kmeans.fit_with_detailed_history(max_iterations=10)
print(f"Total animation frames: {len(kmeans.history)}")

# Create animation
fig, ax = plt.subplots(figsize=(14, 9))

# Centroid colors - these stay consistent
centroid_colors = ['#E63946', '#2A9D8F', '#F4A261', '#8338EC', '#06D6A0']
gray_color = '#CCCCCC'

def init():
    ax.clear()
    return []

def animate(frame_idx):
    ax.clear()

    # Set plot limits
    x_range = X[:, 0].max() - X[:, 0].min()
    y_range = X[:, 1].max() - X[:, 1].min()
    ax.set_xlim(X[:, 0].min() - 0.6*x_range, X[:, 0].max() + 0.6*x_range)
    ax.set_ylim(X[:, 1].min() - 0.6*y_range, X[:, 1].max() + 0.6*y_range)
    ax.set_xlabel('Feature 1', fontsize=14, fontweight='bold')
    ax.set_ylabel('Feature 2', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)

    # Get current state
    state = kmeans.history[frame_idx]
    centroids = state['centroids']
    labels = state['labels']
    step_type = state['step_type']
    iteration = state['iteration']
    description = state['description']

    # Plot points
    # Gray (unassigned) points
    gray_mask = labels == -1
    if np.any(gray_mask):
        ax.scatter(X[gray_mask, 0], X[gray_mask, 1],
                  c=gray_color, s=50, alpha=0.4,
                  edgecolors='black', linewidth=0.5)

    # Colored (assigned) points
    for k in range(n_clusters):
        cluster_mask = labels == k
        if np.any(cluster_mask):
            ax.scatter(X[cluster_mask, 0], X[cluster_mask, 1],
                      c=centroid_colors[k], s=50, alpha=0.7,
                      edgecolors='black', linewidth=0.5,
                      label=f'Cluster {k+1}')

    # Plot centroids as colored X's
    for k in range(n_clusters):
        ax.scatter(centroids[k, 0], centroids[k, 1],
                  c=centroid_colors[k], s=500, alpha=0.95,
                  marker='X', edgecolors='white', linewidth=3,
                  zorder=10)

        # Add centroid number
        ax.text(centroids[k, 0], centroids[k, 1], str(k+1),
               ha='center', va='center', color='white',
               fontsize=14, fontweight='bold', zorder=11)

    # Title based on step type
    if step_type == 'initialization':
        title = 'K-Means Initialization\nCentroids placed (colored X), Points unassigned (gray)'
    elif step_type == 'reset_to_gray':
        title = f'Iteration {iteration}\nReset: Ready to measure distances to centroids'
    elif step_type == 'assigning_points':
        progress = state.get('progress', 0) * 100
        title = f'Iteration {iteration}: Assignment Phase\nMeasuring distances... {progress:.0f}% complete'
    elif step_type == 'assignment_complete':
        title = f'Iteration {iteration}: Assignment Complete\nAll points assigned to nearest centroid'
    elif step_type == 'centroids_updated':
        title = f'Iteration {iteration}: Update Phase\nCentroids moved to cluster means'
    else:
        title = description

    ax.set_title(title, fontsize=16, fontweight='bold', pad=20)

    # Info box
    assigned_count = np.sum(labels >= 0)
    textstr = f'Clusters (k): {n_clusters}\nPoints: {n_samples}\nAssigned: {assigned_count}'
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.85)
    ax.text(0.02, 0.98, textstr, transform=ax.transAxes, fontsize=11,
            verticalalignment='top', bbox=props)

    # Legend
    if np.any(labels >= 0):  # Only show legend if some points are assigned
        ax.legend(loc='upper right', fontsize=10, framealpha=0.9)

    return []

# Create animation
print("Creating animation...")
anim = FuncAnimation(fig, animate, init_func=init,
                    frames=len(kmeans.history),
                    interval=500,  # 0.5 seconds per frame
                    repeat=True, blit=True)

# Save as GIF
print("Saving animation as GIF...")
writer = PillowWriter(fps=4)  # 4 frames per second (2x speed)
anim.save('kmeans_animation.gif', writer=writer, dpi=100)
print("✓ Animation saved as 'kmeans_animation.gif'")

# Save as MP4
try:
    from matplotlib.animation import FFMpegWriter
    print("Saving animation as MP4...")
    writer_mp4 = FFMpegWriter(fps=4, bitrate=2000)  # 4 fps (2x speed)
    anim.save('kmeans_animation.mp4', writer=writer_mp4, dpi=100)
    print("✓ Animation saved as 'kmeans_animation.mp4'")
except Exception as e:
    print(f"Could not save MP4: {e}")
    print("GIF version is available.")

plt.close()
print("\nAnimation complete!")
print(f"Total frames: {len(kmeans.history)}")
print("\nAnimation shows:")
print("  • Initialization: Colored centroids (X), gray points")
print("  • Each iteration:")
print("    1. Reset points to gray")
print("    2. Points change color one-by-one as assigned")
print("    3. Centroids move to cluster centers")
print("    4. Repeat until convergence")
