"""
Bias-Variance Tradeoff Dartboard Metaphor Visual
Generates a 2x2 grid of dartboards illustrating the four scenarios.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

np.random.seed(42)


def draw_dartboard(ax, title, subtitle, darts_x, darts_y, title_color='#2c3e50'):
    """Draw a single dartboard with darts."""
    # Draw rings (outermost to innermost)
    ring_colors = ['#ecf0f1', '#d5dbdb', '#bdc3c7', '#aab7b8', '#95a5a6']
    ring_radii = [1.0, 0.8, 0.6, 0.4, 0.2]
    for r, c in zip(ring_radii, ring_colors):
        circle = plt.Circle((0, 0), r, facecolor=c, edgecolor='#7f8c8d',
                             linewidth=1.5)
        ax.add_patch(circle)

    # Bullseye
    bullseye = plt.Circle((0, 0), 0.08, facecolor='#e74c3c', edgecolor='#c0392b',
                           linewidth=2)
    ax.add_patch(bullseye)

    # Crosshairs
    ax.plot([-1.05, 1.05], [0, 0], 'k-', linewidth=0.5, alpha=0.2)
    ax.plot([0, 0], [-1.05, 1.05], 'k-', linewidth=0.5, alpha=0.2)

    # Darts
    ax.scatter(darts_x, darts_y, s=80, c='#2c3e50', marker='o',
               edgecolors='white', linewidth=1.5, zorder=5)

    # Title
    ax.set_title(title, fontsize=15, fontweight='bold', color=title_color, pad=10)
    ax.text(0, -1.3, subtitle, fontsize=11, ha='center', style='italic',
            color='#555555')

    ax.set_xlim(-1.3, 1.3)
    ax.set_ylim(-1.5, 1.3)
    ax.set_aspect('equal')
    ax.axis('off')


fig, axes = plt.subplots(2, 2, figsize=(12, 13), facecolor='white')
fig.suptitle('Bias-Variance Tradeoff: The Dartboard Metaphor',
             fontsize=20, fontweight='bold', color='#2c3e50', y=0.97)

# 1. High Bias, Low Variance (Underfitting) — clustered but off-center
darts_x = np.random.normal(0.55, 0.06, 8)
darts_y = np.random.normal(0.5, 0.06, 8)
draw_dartboard(axes[0, 0],
               'High Bias, Low Variance',
               'UNDERFITTING — consistent but wrong',
               darts_x, darts_y, title_color='#e67e22')

# 2. Low Bias, Low Variance (Ideal) — clustered on bullseye
darts_x = np.random.normal(0, 0.06, 8)
darts_y = np.random.normal(0, 0.06, 8)
draw_dartboard(axes[0, 1],
               'Low Bias, Low Variance',
               'IDEAL — accurate and consistent',
               darts_x, darts_y, title_color='#27ae60')

# 3. High Bias, High Variance (Worst) — scattered and off-center
darts_x = np.random.normal(0.45, 0.3, 8)
darts_y = np.random.normal(0.4, 0.3, 8)
draw_dartboard(axes[1, 0],
               'High Bias, High Variance',
               'WORST CASE — wrong and inconsistent',
               darts_x, darts_y, title_color='#e74c3c')

# 4. Low Bias, High Variance (Overfitting) — scattered around bullseye
angles = np.random.uniform(0, 2 * np.pi, 8)
radii = np.random.uniform(0.15, 0.7, 8)
darts_x = radii * np.cos(angles)
darts_y = radii * np.sin(angles)
draw_dartboard(axes[1, 1],
               'Low Bias, High Variance',
               'OVERFITTING — accurate on avg, but scatters',
               darts_x, darts_y, title_color='#8e44ad')

# Annotation row at bottom
fig.text(0.5, 0.02,
         'Bias = how far off-center (systematic error)    |    '
         'Variance = how spread out (sensitivity to training data)',
         fontsize=12, ha='center', fontweight='bold', color='#2c3e50',
         bbox=dict(boxstyle='round,pad=0.5', facecolor='#eaf2f8',
                   edgecolor='#2c3e50', linewidth=1.5))

plt.tight_layout(rect=[0, 0.05, 1, 0.94])
plt.savefig('bias_variance_dartboard.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("✓ Created bias_variance_dartboard.png")
