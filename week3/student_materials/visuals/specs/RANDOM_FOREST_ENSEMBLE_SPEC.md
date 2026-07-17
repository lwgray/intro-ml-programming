# Visual Specification: Random Forest Ensemble

## Purpose

Illustrate the "Committee Decision" metaphor showing multiple trees voting in parallel.

---

## Specifications

**Filename:** `random_forest_ensemble.png`
**Dimensions:** 1920 x 1080 pixels
**Format:** PNG, white background

---

## Visual Layout

```
┌────────────────────────────────────────────────────────────────┐
│         Random Forest: The "Committee Decision"                │
├────────────────────────────────────────────────────────────────┤
│                                                                 │
│                    TRAINING DATA                                │
│                    [All Examples]                               │
│                          │                                      │
│        ┌─────────────────┼─────────────────┬────────────┐      │
│        │                 │                 │            │      │
│    Bootstrap         Bootstrap        Bootstrap    ... (97)   │
│    Sample 1          Sample 2         Sample 3                │
│    [1,1,3,5,5]      [2,2,3,4,4]      [1,2,2,3,5]             │
│        │                 │                 │                   │
│        ▼                 ▼                 ▼                   │
│   ┌────────┐        ┌────────┐       ┌────────┐              │
│   │ TREE 1 │        │ TREE 2 │       │ TREE 3 │   ... 100    │
│   └────────┘        └────────┘       └────────┘              │
│        │                 │                 │                   │
│   Predict: A        Predict: A        Predict: B              │
│        │                 │                 │                   │
│        └─────────────────┴─────────────────┘                  │
│                          │                                      │
│                          ▼                                      │
│                  ┌─────────────┐                               │
│                  │  MAJORITY   │                               │
│                  │    VOTE     │                               │
│                  └─────────────┘                               │
│                   73 votes: A                                  │
│                   27 votes: B                                  │
│                          │                                      │
│                          ▼                                      │
│                 FINAL PREDICTION: A                            │
└────────────────────────────────────────────────────────────────┘
```

---

## Detailed Specifications

### Title
- Text: "Random Forest: The 'Committee Decision'"
- Font: Bold, 28pt, #003366
- Position: Top center, 30px from edge

### Training Data (Top)
- Box: 300 x 100px, dashed border #666666
- Label: "TRAINING DATA\n(All Examples)"
- Icon: Database symbol or data table icon
- Color: Light gray background #F0F0F0

### Bootstrap Samples (Row 2)
- 3 visible boxes + "... (97 more)"
- Each box: 200 x 120px
- Border: 2px solid #3366CC
- Background: Light blue #E6F2FF
- Labels: "Bootstrap Sample 1", "Sample 2", "Sample 3"
- Example data shown: [1, 1, 3, 5, 5] etc.
- Font: Monospace, 10pt for data

### Arrows from Data to Samples
- Style: Curved arrows
- Color: #FF9900 (orange)
- Width: 3px
- Label on first arrow: "Random sampling\nwith replacement"

### Decision Trees (Row 3)
- 3 visible trees + "... + 97 more"
- Each tree: Simple 3-level tree icon
- Dimensions: 180 x 200px per tree
- Color: Green (#00AA00) for leaves, blue (#3366CC) for nodes
- Labels: "TREE 1", "TREE 2", "TREE 3", "... TREE 100"
- Font: Bold, 14pt

### Individual Predictions (Below trees)
- Text boxes showing each tree's vote
- "Predict: A", "Predict: A", "Predict: B"
- Font: Bold, 12pt
- Color: Class A votes in blue, Class B in red
- Background: Light yellow highlight

### Aggregation Box (Center Bottom)
- Dimension: 300 x 150px
- Shape: Rounded rectangle
- Border: 4px solid #006600 (dark green)
- Background: Light green gradient
- Title: "MAJORITY VOTE"
- Content: "73 votes: Class A\n27 votes: Class B"
- Font: Bold, 16pt

### Final Prediction (Bottom)
- Large text: "FINAL PREDICTION: Class A"
- Font: Very bold, 24pt
- Color: #006600 (dark green)
- Background: Light green highlight #CCFFCC
- Border: 3px solid #006600

### Side Annotations

**Left annotation (pointing to bootstrap):**
```
Each tree sees
different data
(~63% of examples)
```
- Callout box with arrow
- Font: Italic, 11pt

**Right annotation (pointing to votes):**
```
Wisdom of Crowds:
Individual mistakes
cancel out!
```
- Callout box with arrow
- Font: Italic, 11pt

---

## Color Scheme

- Training data: Gray (#F0F0F0)
- Bootstrap samples: Blue (#E6F2FF border)
- Decision trees: Green (#00AA00) and blue (#3366CC)
- Aggregation: Dark green (#006600)
- Arrows: Orange (#FF9900)
- Text: Dark gray (#333333)

---

## Creation Code

```python
# Use draw.io, PowerPoint, or code with matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(figsize=(19.2, 10.8))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(5, 9.5, "Random Forest: The 'Committee Decision'",
        ha='center', fontsize=28, fontweight='bold', color='#003366')

# Training Data (top)
data_box = FancyBboxPatch((4, 8), 2, 0.8, boxstyle="round,pad=0.05",
                          edgecolor='#666666', facecolor='#F0F0F0',
                          linewidth=2, linestyle='dashed')
ax.add_patch(data_box)
ax.text(5, 8.4, 'TRAINING DATA', ha='center', fontsize=14, fontweight='bold')

# Bootstrap samples
for i, x in enumerate([1.5, 4.5, 7.5]):
    sample_box = FancyBboxPatch((x-0.6, 6.2), 1.2, 1,
                                boxstyle="round,pad=0.05",
                                edgecolor='#3366CC', facecolor='#E6F2FF',
                                linewidth=2)
    ax.add_patch(sample_box)
    ax.text(x, 7, f'Sample {i+1}', ha='center', fontsize=12, fontweight='bold')
    ax.text(x, 6.5, '[1,1,3,5,5]', ha='center', fontsize=9, family='monospace')

    # Arrow from data to sample
    arrow = FancyArrowPatch((5, 8), (x, 7.2),
                           arrowstyle='->', lw=2, color='#FF9900')
    ax.add_patch(arrow)

# Trees
for i, x in enumerate([1.5, 4.5, 7.5]):
    # Simple triangle for tree
    tree = mpatches.Polygon([[x, 5.5], [x-0.4, 4.5], [x+0.4, 4.5]],
                           closed=True, fc='#00AA00', ec='#003366', linewidth=2)
    ax.add_patch(tree)
    ax.text(x, 4.2, f'TREE {i+1}', ha='center', fontsize=12, fontweight='bold')
    ax.text(x, 3.8, f'Vote: {"A" if i < 2 else "B"}', ha='center',
            fontsize=11, bbox=dict(boxstyle='round', facecolor='#FFFFCC'))

# More trees indicator
ax.text(9, 5, '... + 97 more\ntrees', ha='center', fontsize=11, style='italic')

# Voting box
vote_box = FancyBboxPatch((3.5, 1.5), 3, 1.5, boxstyle="round,pad=0.1",
                          edgecolor='#006600', facecolor='#CCFFEE',
                          linewidth=4)
ax.add_patch(vote_box)
ax.text(5, 2.5, 'MAJORITY VOTE', ha='center', fontsize=16, fontweight='bold')
ax.text(5, 2.1, '73 votes: Class A', ha='center', fontsize=14)
ax.text(5, 1.8, '27 votes: Class B', ha='center', fontsize=14)

# Final prediction
ax.text(5, 0.8, 'FINAL PREDICTION: Class A', ha='center',
        fontsize=24, fontweight='bold', color='#006600',
        bbox=dict(boxstyle='round', facecolor='#CCFFCC',
                 edgecolor='#006600', linewidth=3))

plt.savefig('random_forest_ensemble.png', dpi=150, bbox_inches='tight',
            facecolor='white', edgecolor='none')
plt.show()
```

---

## Usage During Teaching

**When:** Segment 3 (0:50) - "Committee Decision" metaphor

**Script:**
> "This is Random Forest in action. We start with our training data at the top. We create 100 bootstrap samples - each tree sees slightly different data. Each tree makes an independent prediction. Then we VOTE - 73 trees say Class A, 27 say Class B. Majority wins! That's the committee decision."

---

## Version

Random Forest Ensemble Visual v1.0 | January 24, 2026
