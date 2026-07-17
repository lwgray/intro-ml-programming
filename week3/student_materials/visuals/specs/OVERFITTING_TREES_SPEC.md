# Visual Specification: Overfitting Trees

## Purpose

Compare shallow tree (good generalization) vs deep tree (overfitting) with decision boundaries.

---

## Specifications

**Filename:** `overfitting_trees.png`
**Dimensions:** 1920 x 1080 pixels
**Format:** PNG, white background

---

## Visual Layout

```
┌─────────────────────────────────────────────────────────────┐
│        Decision Tree Overfitting: Depth Comparison           │
├──────────────────────────┬──────────────────────────────────┤
│                          │                                   │
│  SHALLOW TREE            │       DEEP TREE                   │
│  (max_depth=3)           │       (max_depth=15)              │
│  ✓ Good Generalization   │       ✗ Overfitting              │
│                          │                                   │
│  [Decision boundary plot]│       [Decision boundary plot]    │
│  Smooth, simple regions  │       Jagged, complex regions     │
│                          │                                   │
│  Train Accuracy: 82%     │       Train Accuracy: 100%        │
│  Test Accuracy: 80%      │       Test Accuracy: 65%          │
│  ✓ Minimal gap           │       ✗ Large gap (overfitting!)  │
└──────────────────────────┴───────────────────────────────────┘
```

---

## Detailed Specifications

### Title
- Text: "Decision Tree Overfitting: Depth Comparison"
- Font: Bold, 24pt, #003366
- Position: Top center, 30px from edge

### Left Panel: Shallow Tree (Good)

**Decision Boundary Plot:**
- 2D scatter plot with decision boundaries
- X-axis: Feature 1, Y-axis: Feature 2
- Data points:
  - Class A: Blue circles (●), 100 points
  - Class B: Red triangles (▲), 100 points
- Decision boundaries:
  - Style: Thick black lines (3px)
  - Pattern: Rectangular regions (axis-aligned)
  - Number of regions: ~8 regions
  - Smooth, simple boundaries

**Labels:**
- Title: "Shallow Tree (max_depth=3)"
- Subtitle: "✓ Good Generalization"
- Font: Bold, 18pt for title, 14pt for subtitle
- Color: Green #00AA00 for checkmark

**Metrics Box (bottom of plot):**
```
Training Accuracy: 82%
Test Accuracy: 80%
Gap: 2% ✓
```
- Background: Light green #CCFFEE
- Border: 2px solid #00AA00
- Font: 12pt, monospace

### Right Panel: Deep Tree (Overfitting)

**Decision Boundary Plot:**
- Same data points as left panel
- Decision boundaries:
  - Style: Thin lines (1px) because many boundaries
  - Pattern: Highly fragmented regions
  - Number of regions: ~50+ tiny regions
  - Jagged, complex boundaries
  - Some regions contain only 1-2 points (overfitting!)

**Labels:**
- Title: "Deep Tree (max_depth=15)"
- Subtitle: "✗ Overfitting!"
- Font: Bold, 18pt for title, 14pt for subtitle
- Color: Red #CC0000 for X mark

**Metrics Box (bottom of plot):**
```
Training Accuracy: 100%
Test Accuracy: 65%
Gap: 35% ✗ OVERFITTING!
```
- Background: Light red #FFCCCC
- Border: 2px solid #CC0000
- Font: 12pt, monospace
- "OVERFITTING!" in bold red

### Bottom Comparison

**Text Box:**
```
KEY DIFFERENCE:
Shallow tree creates smooth, general decision boundaries
Deep tree memorizes training points with complex boundaries
→ Shallow tree generalizes better to new data!
```
- Position: Bottom center, below both plots
- Background: Light yellow #FFFACD
- Border: 3px solid #FF9900
- Font: Bold, 14pt

---

## Color Scheme

- Class A: Blue #0066CC
- Class B: Red #CC0000
- Shallow tree (good): Green accents #00AA00
- Deep tree (bad): Red accents #CC0000
- Background: White #FFFFFF
- Decision boundaries: Black #000000

---

## Creation Code

```python
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_moons
from sklearn.tree import DecisionTreeClassifier
from matplotlib.colors import ListedColormap

# Generate data
X, y = make_moons(n_samples=200, noise=0.2, random_state=42)
X_train, X_test = X[:150], X[150:]
y_train, y_test = y[:150], y[150:]

# Create meshgrid for decision boundary
h = 0.02
x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

# Create figure
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(19.2, 10.8))

# Colors
cmap_light = ListedColormap(['#FFCCCC', '#CCCCFF'])
cmap_bold = ['#CC0000', '#0066CC']

# LEFT: Shallow tree
tree_shallow = DecisionTreeClassifier(max_depth=3, random_state=42)
tree_shallow.fit(X_train, y_train)

Z1 = tree_shallow.predict(np.c_[xx.ravel(), yy.ravel()])
Z1 = Z1.reshape(xx.shape)
ax1.contourf(xx, yy, Z1, alpha=0.3, cmap=cmap_light)
ax1.contour(xx, yy, Z1, colors='black', linewidths=3, alpha=0.8)

# Plot points
ax1.scatter(X_train[y_train==0, 0], X_train[y_train==0, 1],
           c='#0066CC', marker='o', s=100, edgecolors='black',
           linewidth=1.5, label='Class A', alpha=0.8)
ax1.scatter(X_train[y_train==1, 0], X_train[y_train==1, 1],
           c='#CC0000', marker='^', s=100, edgecolors='black',
           linewidth=1.5, label='Class B', alpha=0.8)

train_acc = tree_shallow.score(X_train, y_train) * 100
test_acc = tree_shallow.score(X_test, y_test) * 100

ax1.set_title('Shallow Tree (max_depth=3)\n✓ Good Generalization',
             fontsize=18, fontweight='bold', color='#00AA00', pad=15)
ax1.set_xlabel('Feature 1', fontsize=14)
ax1.set_ylabel('Feature 2', fontsize=14)
ax1.legend(loc='upper right', fontsize=12)
ax1.grid(alpha=0.3)

# Add metrics
metrics_text = f"Training Acc: {train_acc:.0f}%\nTest Acc: {test_acc:.0f}%\nGap: {train_acc-test_acc:.0f}% ✓"
ax1.text(0.5, -0.15, metrics_text, transform=ax1.transAxes,
        ha='center', fontsize=12, family='monospace',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#CCFFEE',
                 edgecolor='#00AA00', linewidth=2))

# RIGHT: Deep tree
tree_deep = DecisionTreeClassifier(max_depth=15, random_state=42)
tree_deep.fit(X_train, y_train)

Z2 = tree_deep.predict(np.c_[xx.ravel(), yy.ravel()])
Z2 = Z2.reshape(xx.shape)
ax2.contourf(xx, yy, Z2, alpha=0.3, cmap=cmap_light)
ax2.contour(xx, yy, Z2, colors='black', linewidths=1, alpha=0.8)

# Plot points
ax2.scatter(X_train[y_train==0, 0], X_train[y_train==0, 1],
           c='#0066CC', marker='o', s=100, edgecolors='black',
           linewidth=1.5, label='Class A', alpha=0.8)
ax2.scatter(X_train[y_train==1, 0], X_train[y_train==1, 1],
           c='#CC0000', marker='^', s=100, edgecolors='black',
           linewidth=1.5, label='Class B', alpha=0.8)

train_acc_deep = tree_deep.score(X_train, y_train) * 100
test_acc_deep = tree_deep.score(X_test, y_test) * 100

ax2.set_title('Deep Tree (max_depth=15)\n✗ Overfitting!',
             fontsize=18, fontweight='bold', color='#CC0000', pad=15)
ax2.set_xlabel('Feature 1', fontsize=14)
ax2.set_ylabel('Feature 2', fontsize=14)
ax2.legend(loc='upper right', fontsize=12)
ax2.grid(alpha=0.3)

# Add metrics
metrics_text = f"Training Acc: {train_acc_deep:.0f}%\nTest Acc: {test_acc_deep:.0f}%\nGap: {train_acc_deep-test_acc_deep:.0f}% ✗ OVERFITTING!"
ax2.text(0.5, -0.15, metrics_text, transform=ax2.transAxes,
        ha='center', fontsize=12, family='monospace',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#FFCCCC',
                 edgecolor='#CC0000', linewidth=2))

# Overall title
fig.suptitle('Decision Tree Overfitting: Depth Comparison',
            fontsize=24, fontweight='bold', color='#003366', y=0.98)

# Bottom comparison text
comparison = ("KEY DIFFERENCE:\n"
              "Shallow tree creates smooth, general decision boundaries\n"
              "Deep tree memorizes training points with complex boundaries\n"
              "→ Shallow tree generalizes better to new data!")
fig.text(0.5, 0.02, comparison, ha='center', fontsize=14, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.8', facecolor='#FFFACD',
                 edgecolor='#FF9900', linewidth=3))

plt.tight_layout(rect=[0, 0.08, 1, 0.96])
plt.savefig('overfitting_trees.png', dpi=150, bbox_inches='tight',
            facecolor='white', edgecolor='none')
plt.show()
```

---

## Usage

**When:** Segment 2 (0:32) - Overfitting warning

**Script:**
> "Look at these two trees trained on the same data. Left: max_depth=3, creates 8 simple regions. Right: max_depth=15, creates 50+ tiny regions. The deep tree gets 100% training accuracy - perfect! But test accuracy is only 65%. The shallow tree gets 82% training, 80% test - much better generalization. The deep tree memorized instead of learning."

---

## Version

Overfitting Trees Visual v1.0 | January 24, 2026
