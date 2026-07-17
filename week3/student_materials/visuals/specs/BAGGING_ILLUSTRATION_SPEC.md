# Visual Specification: Bagging Illustration

## Purpose

Illustrate the bagging (Bootstrap Aggregating) process step-by-step.

---

## Specifications

**Filename:** `bagging_illustration.png`
**Dimensions:** 1600 x 900 pixels
**Format:** PNG, white background

---

## Visual Layout

```
BAGGING: Bootstrap Aggregating

Step 1: BOOTSTRAP          Step 2: TRAIN          Step 3: AGGREGATE
──────────────────────     ─────────────────      ──────────────────

Original Data:             Each tree trains        Combine predictions:
[1,2,3,4,5,6,7,8,9,10]    independently
                                                   Classification: VOTE
Sample 1:   [1,1,3,5,7,9]  → Tree 1               Regression: AVERAGE
Sample 2:   [2,2,4,6,8,10] → Tree 2
Sample 3:   [1,3,5,5,9,10] → Tree 3
...                         ...
Sample 100: [2,4,6,7,8,9]  → Tree 100

(Sampling WITH               (PARALLEL training)   (Aggregation reduces
 replacement)                                       variance)
```

---

## Detailed Elements

### Step 1: Bootstrap (Left Third)

**Original Data Box:**
- 250 x 150px, solid border #333333
- Background: Light gray #F0F0F0
- Label: "Original Training Data (n=10,000)"
- Show array: [1, 2, 3, ..., 10000]
- Font: Monospace, 12pt

**Bootstrap Arrows:**
- 4-5 arrows pointing from original to samples
- Curved arrows, orange #FF9900, 3px wide
- Label on arrow: "Sample with replacement"

**Bootstrap Samples (4 shown):**
- Each: 200 x 100px box
- Border: 2px dashed #3366CC
- Background: Light blue #E6F2FF
- Labels: "Sample 1 (~63% unique)", "Sample 2", etc.
- Show example: [1, 1, 3, 5, 7, 9] (with repeats highlighted)
- Note: "~37% not included (Out-of-Bag)"

### Step 2: Train (Middle Third)

**Training Indicators:**
- 4 tree icons (simple triangular shapes)
- Each tree: 120 x 150px
- Green #00AA00 with blue nodes #3366CC
- Labels: "Tree 1", "Tree 2", "Tree 3", "... Tree 100"
- Font: Bold, 14pt

**Parallel Training Emphasis:**
- Horizontal lines connecting all trees
- Label: "TRAINED IN PARALLEL"
- Icon: Parallel lines symbol ||
- Background: Light yellow highlight #FFFACD

**Key Point Box:**
```
Trees are INDEPENDENT
Each sees different data
No communication between trees
```
- Italic font, 11pt
- Light green background #E8F5E9

### Step 3: Aggregate (Right Third)

**Aggregation Methods:**

**For Classification (top half):**
```
Tree 1: Class A
Tree 2: Class A
Tree 3: Class B
...
Tree 100: Class A

→ VOTE → Class A (73%)
```
- Ballot box icon
- Green checkmark for majority

**For Regression (bottom half):**
```
Tree 1: 125.3
Tree 2: 130.7
Tree 3: 128.1
...
Tree 100: 127.9

→ AVERAGE → 127.5
```
- Calculator icon
- Blue for average result

---

## Color Scheme

- Original data: Gray #F0F0F0
- Bootstrap samples: Light blue #E6F2FF
- Trees: Green #00AA00, Blue nodes #3366CC
- Arrows: Orange #FF9900
- Aggregation: Green #CCFFEE (classification), Blue #E6F2FF (regression)

---

## Creation Code

```python
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patches as mpatches

fig = plt.figure(figsize=(16, 9))
ax = plt.subplot(111)
ax.set_xlim(0, 15)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(7.5, 9.5, 'BAGGING: Bootstrap Aggregating',
        ha='center', fontsize=26, fontweight='bold', color='#003366')

# Step headers
for i, (x, step) in enumerate([(2.5, 'BOOTSTRAP'), (7.5, 'TRAIN'),
                                 (12.5, 'AGGREGATE')]):
    ax.text(x, 8.5, f'Step {i+1}: {step}', ha='center',
            fontsize=18, fontweight='bold', color='#003366')

# Step 1: Bootstrap
orig_box = FancyBboxPatch((1.5, 6.5), 2, 1.2, boxstyle="round,pad=0.05",
                          edgecolor='#333333', facecolor='#F0F0F0', linewidth=2)
ax.add_patch(orig_box)
ax.text(2.5, 7.5, 'Original Data', ha='center', fontsize=12, fontweight='bold')
ax.text(2.5, 7.1, '[1,2,3,...,10000]', ha='center', fontsize=10, family='monospace')

for i, y in enumerate([5.5, 4.5, 3.5, 2.5]):
    sample_box = FancyBboxPatch((1.2, y), 2.6, 0.7, boxstyle="round,pad=0.03",
                                edgecolor='#3366CC', facecolor='#E6F2FF',
                                linewidth=2, linestyle='dashed')
    ax.add_patch(sample_box)
    ax.text(2.5, y+0.35, f'Sample {i+1}: [1,1,3,5,...]', ha='center', fontsize=9)
    # Arrow
    arrow = FancyArrowPatch((2.5, 6.5), (2.5, y+0.7), arrowstyle='->',
                           lw=2, color='#FF9900')
    ax.add_patch(arrow)

ax.text(2.5, 1.8, '(Sampling with\nreplacement)', ha='center',
        fontsize=10, style='italic')

# Step 2: Train
for i, y in enumerate([6, 4.8, 3.6, 2.4]):
    # Tree triangle
    tree = mpatches.Polygon([[7.5, y], [7.2, y-0.8], [7.8, y-0.8]],
                           closed=True, fc='#00AA00', ec='#003366', linewidth=2)
    ax.add_patch(tree)
    if i < 3:
        ax.text(7.5, y-1.1, f'Tree {i+1}', ha='center', fontsize=11, fontweight='bold')
    else:
        ax.text(7.5, y-1.1, '... Tree 100', ha='center', fontsize=11, style='italic')

ax.text(7.5, 1.5, 'TRAINED IN PARALLEL\n(Independent trees)',
        ha='center', fontsize=12, fontweight='bold',
        bbox=dict(boxstyle='round', facecolor='#FFFACD'))

# Step 3: Aggregate
vote_box = FancyBboxPatch((11, 5.5), 3, 2.5, boxstyle="round,pad=0.1",
                          edgecolor='#006600', facecolor='#CCFFEE', linewidth=3)
ax.add_patch(vote_box)
ax.text(12.5, 7.5, 'CLASSIFICATION', ha='center', fontsize=14, fontweight='bold')
ax.text(12.5, 7, 'Tree predictions:', ha='center', fontsize=11)
ax.text(12.5, 6.6, 'A, A, B, A, A, ...', ha='center', fontsize=10)
ax.text(12.5, 6.2, '↓ VOTE ↓', ha='center', fontsize=12, fontweight='bold')
ax.text(12.5, 5.8, 'Class A (73%)', ha='center', fontsize=12,
        bbox=dict(boxstyle='round', facecolor='#CCFFCC'))

avg_box = FancyBboxPatch((11, 2.5), 3, 2.5, boxstyle="round,pad=0.1",
                         edgecolor='#003366', facecolor='#E6F2FF', linewidth=3)
ax.add_patch(avg_box)
ax.text(12.5, 4.5, 'REGRESSION', ha='center', fontsize=14, fontweight='bold')
ax.text(12.5, 4, 'Tree predictions:', ha='center', fontsize=11)
ax.text(12.5, 3.6, '125, 130, 128, ...', ha='center', fontsize=10)
ax.text(12.5, 3.2, '↓ AVERAGE ↓', ha='center', fontsize=12, fontweight='bold')
ax.text(12.5, 2.8, '127.5', ha='center', fontsize=12,
        bbox=dict(boxstyle='round', facecolor='#CCE5FF'))

plt.savefig('bagging_illustration.png', dpi=150, bbox_inches='tight',
            facecolor='white', edgecolor='none')
plt.show()
```

---

## Usage

**When:** Segment 3 (0:52) - Explaining bagging

**Script:**
> "Bagging has three steps. First, BOOTSTRAP - we create random samples with replacement. Each tree sees different data. Second, TRAIN - we train all trees in parallel, independently. Third, AGGREGATE - for classification we vote, for regression we average. This reduces variance because errors cancel out across trees."

---

## Version

Bagging Illustration v1.0 | January 24, 2026
