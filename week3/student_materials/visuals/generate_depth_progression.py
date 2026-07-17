"""
Decision Tree Depth Progression: Underfitting -> Good Fit -> Overfitting

Shows decision boundaries across a range of max_depth values on the same
two-moons dataset so students can watch the boundary go from too-simple
(underfit) to just-right to memorized/jagged (overfit). Each panel reports
train and test accuracy and the gap between them.

Companion to overfitting_trees.png (which shows only depth 3 vs 15).
Non-destructive: writes a new file, depth_progression.png.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.datasets import make_moons
from sklearn.tree import DecisionTreeClassifier

# Data (same generator/style as overfitting_trees.png)
X, y = make_moons(n_samples=200, noise=0.2, random_state=42)
X_train, X_test = X[:150], X[150:]
y_train, y_test = y[:150], y[150:]

# Meshgrid for decision boundary
h = 0.02
x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

cmap_light = ListedColormap(['#FFCCCC', '#CCCCFF'])

depths = [1, 2, 3, 5, 8, 20]
labels = {
    1: ('Underfitting', '#CC0000'),
    2: ('Underfitting', '#CC0000'),
    3: ('Good Fit', '#00AA00'),
    5: ('Good Fit', '#00AA00'),
    8: ('Starting to Overfit', '#FF9900'),
    20: ('Overfitting', '#CC0000'),
}

fig, axes = plt.subplots(2, 3, figsize=(19.2, 11.5))

for ax, depth in zip(axes.ravel(), depths):
    tree = DecisionTreeClassifier(max_depth=depth, random_state=42)
    tree.fit(X_train, y_train)

    Z = tree.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
    ax.contourf(xx, yy, Z, alpha=0.3, cmap=cmap_light)
    ax.contour(xx, yy, Z, colors='black', linewidths=1.5, alpha=0.8)

    ax.scatter(X_train[y_train == 0, 0], X_train[y_train == 0, 1],
               c='#0066CC', marker='o', s=60, edgecolors='black',
               linewidth=1, alpha=0.8)
    ax.scatter(X_train[y_train == 1, 0], X_train[y_train == 1, 1],
               c='#CC0000', marker='^', s=60, edgecolors='black',
               linewidth=1, alpha=0.8)

    train_acc = tree.score(X_train, y_train) * 100
    test_acc = tree.score(X_test, y_test) * 100
    gap = train_acc - test_acc

    verdict, color = labels[depth]
    ax.set_title(f'max_depth = {depth}  ({verdict})',
                 fontsize=16, fontweight='bold', color=color, pad=10)
    ax.set_xlabel('Feature 1', fontsize=11)
    ax.set_ylabel('Feature 2', fontsize=11)
    ax.grid(alpha=0.3)

    metrics = (f"Train: {train_acc:.0f}%   Test: {test_acc:.0f}%   "
               f"Gap: {gap:.0f}%")
    facecolor = '#CCFFEE' if gap <= 6 else ('#FFE8CC' if gap <= 12 else '#FFCCCC')
    ax.text(0.5, -0.18, metrics, transform=ax.transAxes, ha='center',
            fontsize=12, family='monospace',
            bbox=dict(boxstyle='round,pad=0.4', facecolor=facecolor,
                      edgecolor=color, linewidth=2))

fig.suptitle('Decision Tree Depth Progression: Underfitting -> Good Fit -> Overfitting',
             fontsize=22, fontweight='bold', color='#003366', y=0.99)

takeaway = ("AS DEPTH INCREASES: training accuracy keeps climbing toward 100%, "
            "but test accuracy peaks then falls.\n"
            "The widening Train-Test gap is the signature of overfitting -> "
            "pick the depth where TEST accuracy is best.")
fig.text(0.5, 0.01, takeaway, ha='center', fontsize=13, fontweight='bold',
         bbox=dict(boxstyle='round,pad=0.7', facecolor='#FFFACD',
                   edgecolor='#FF9900', linewidth=3))

plt.tight_layout(rect=[0, 0.06, 1, 0.96])
plt.savefig('depth_progression.png', dpi=150, bbox_inches='tight',
            facecolor='white', edgecolor='none')
plt.close()
print("Created depth_progression.png")
