# Visual Specification: Tree Splitting Animation

## Purpose

Show the before/after of a tree split to illustrate information gain. Demonstrates how a good split creates pure groups while a bad split leaves groups mixed.

---

## Specifications

**Filename:** `tree_splitting_animation.png` (or `tree_splitting_before_after.png`)

**Dimensions:** 1600 x 900 pixels (16:9 aspect ratio)

**Format:** PNG with white background

**Layout:** Side-by-side comparison (Before → After)

---

## Visual Layout

### Overall Structure

```
┌──────────────────────────────────────────────────────────────────┐
│         Tree Splitting: How Information Gain Works               │
├─────────────────────────────┬────────────────────────────────────┤
│                             │                                    │
│     BEFORE SPLIT            │        AFTER SPLIT                 │
│                             │                                    │
│  ┌─────────────────────┐    │   ┌──────────┐  ┌──────────┐      │
│  │  [All Data Mixed]   │    │   │ Left     │  │ Right    │      │
│  │  ● ● ○ ○ ● ○       │    │   │ Group    │  │ Group    │      │
│  │  ○ ● ● ○ ● ○       │    │   │ ● ● ●    │  │ ○ ○ ○    │      │
│  │  ● ○ ● ● ○ ○       │    │   │ ● ●      │  │ ○ ○      │      │
│  │                     │    │   └──────────┘  └──────────┘      │
│  │  Impurity: 0.50     │    │   Impurity:       Impurity:       │
│  │  (Very Mixed)       │    │   0.12            0.08             │
│  └─────────────────────┘    │   (Mostly Pure)   (Mostly Pure)   │
│                             │                                    │
│                             │   Information Gain = 0.30          │
│                             │   (Good Split!)                    │
└─────────────────────────────┴────────────────────────────────────┘
```

---

## Detailed Specifications

### Left Panel: BEFORE SPLIT

**Background:** Light gray (#F5F5F5)

**Main Box:**
- Dimensions: 600 x 600 pixels
- Border: 3px dashed, #999999
- Background: White
- Position: Centered in left half

**Data Points:**
- Scatter plot showing mixed classes
- Class A (●): Blue circles, 60 points
- Class B (○): Red circles, 60 points
- Point size: 15px diameter
- Random distribution (mixed together)

**Labels:**
```
All Data (n=120)
Class A: 60 points (50%)
Class B: 60 points (50%)

Gini Impurity: 0.50
(Maximum mixing)
```
- Font: Sans-serif, 16pt for main label, 14pt for details
- Position: Below the box

**No Split Line** - Just mixed points

---

### Right Panel: AFTER GOOD SPLIT

**Background:** Light green (#E8F5E9)

**Two Boxes (Left and Right Groups):**

**Left Group Box:**
- Dimensions: 350 x 500 pixels
- Border: 3px solid, #00AA00 (green)
- Background: #F1F8F1 (very light green)
- Position: Left side of right panel

**Data Points in Left Group:**
- Class A (●): Blue, 55 points
- Class B (○): Red, 5 points
- Clearly dominated by Class A

**Labels:**
```
Left Group (n=60)
Age <= 30
Class A: 55 (92%)
Class B: 5 (8%)

Gini Impurity: 0.15
(Mostly pure)
```

**Right Group Box:**
- Dimensions: 350 x 500 pixels
- Border: 3px solid, #0066CC (blue)
- Background: #F1F6FB (very light blue)
- Position: Right side of right panel

**Data Points in Right Group:**
- Class A (●): Blue, 5 points
- Class B (○): Red, 55 points
- Clearly dominated by Class B

**Labels:**
```
Right Group (n=60)
Age > 30
Class A: 5 (8%)
Class B: 55 (92%)

Gini Impurity: 0.15
(Mostly pure)
```

**Split Indicator:**
Between the two groups, show a vertical line/arrow with label:
```
Split on: Age > 30?
```
- Font: Bold, 18pt
- Color: #333333

**Information Gain Callout:**
At the bottom of right panel:
```
Information Gain = 0.20
(Impurity decreased from 0.50 to 0.15 average)
✓ Good Split!
```
- Font: Bold, 20pt
- Color: #00AA00 (green)
- Background: Light yellow highlight (#FFFACD)

---

### Arrow Between Panels

**Large Arrow:**
- From center of left panel to center of right panel
- Width: 60px
- Color: #FF9900 (orange)
- Style: Solid with arrowhead
- Label on arrow: "SPLIT" (white text, bold, 24pt)

---

## Example Values to Use

**Scenario: Age-based split for income prediction**

BEFORE:
- 120 people total
- 60 high income (Class A, blue)
- 60 low income (Class B, red)
- Mixed ages (20-60 years old)
- Gini impurity: 0.50

AFTER SPLIT on Age > 30:
- Left group (Age <= 30): 60 people
  - 5 high income, 55 low income
  - Gini: 0.15
- Right group (Age > 30): 60 people
  - 55 high income, 5 low income
  - Gini: 0.15
- Information gain: 0.50 - 0.15 = 0.35 (excellent split!)

---

## Color Scheme

**Class Colors:**
- Class A (high income): Blue #0066CC
- Class B (low income): Red #CC0000

**Panel Backgrounds:**
- Before panel: Light gray #F5F5F5
- After panel: Light green #E8F5E9 (indicates improvement)

**Group Boxes:**
- Left group: Green border #00AA00, very light green fill
- Right group: Blue border #0066CC, very light blue fill

**Highlights:**
- Information gain callout: Yellow highlight #FFFACD
- Good split indicator: Green checkmark #00AA00

---

## Creation Code

### Option 1: Matplotlib (Recommended)

```python
import matplotlib.pyplot as plt
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Create figure with 2 subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 9))

# BEFORE: Mixed data
n_points = 60
# Class A (blue) - will be mostly in right group after split
class_a_x = np.random.uniform(20, 60, n_points)
class_a_y = np.random.uniform(0, 100, n_points)
# Class B (red) - will be mostly in left group after split
class_b_x = np.random.uniform(20, 60, n_points)
class_b_y = np.random.uniform(0, 100, n_points)

# Plot BEFORE
ax1.scatter(class_a_x, class_a_y, c='#0066CC', s=150, alpha=0.7,
            edgecolors='black', linewidth=1.5, label='Class A (High Income)')
ax1.scatter(class_b_x, class_b_y, c='#CC0000', s=150, alpha=0.7,
            edgecolors='black', linewidth=1.5, label='Class B (Low Income)')
ax1.set_xlim(15, 65)
ax1.set_ylim(-10, 110)
ax1.set_xlabel('Age', fontsize=16, fontweight='bold')
ax1.set_ylabel('Arbitrary Y (for visualization)', fontsize=14)
ax1.set_title('BEFORE SPLIT\nAll Data Mixed', fontsize=20, fontweight='bold', pad=20)
ax1.legend(loc='upper right', fontsize=12)
ax1.set_facecolor('#F5F5F5')
ax1.grid(alpha=0.3)

# Add impurity text
ax1.text(40, -5, 'Gini Impurity: 0.50\n(Maximum Mixing)',
         ha='center', fontsize=14, bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# AFTER: Split data
# Split at age 30
left_a = class_a_x[class_a_x <= 30]
left_b = class_b_x[class_b_x <= 30]
right_a = class_a_x[class_a_x > 30]
right_b = class_b_x[class_b_x > 30]

# Plot AFTER (manipulate for clear split)
# Left group: mostly Class B (red)
left_x = np.concatenate([np.full(5, 25), np.full(55, 25)])
left_y = np.concatenate([np.random.uniform(60, 90, 5), np.random.uniform(10, 80, 55)])
left_colors = ['#0066CC']*5 + ['#CC0000']*55

ax2.scatter(left_x, left_y, c=left_colors, s=150, alpha=0.7,
            edgecolors='black', linewidth=1.5)

# Right group: mostly Class A (blue)
right_x = np.concatenate([np.full(55, 50), np.full(5, 50)])
right_y = np.concatenate([np.random.uniform(10, 90, 55), np.random.uniform(10, 40, 5)])
right_colors = ['#0066CC']*55 + ['#CC0000']*5

ax2.scatter(right_x, right_y, c=right_colors, s=150, alpha=0.7,
            edgecolors='black', linewidth=1.5)

# Split line
ax2.axvline(x=37.5, color='#FF9900', linewidth=4, linestyle='--', label='Split Line')
ax2.text(37.5, 105, 'Split: Age > 30?', ha='center', fontsize=16,
         fontweight='bold', bbox=dict(boxstyle='round', facecolor='#FF9900', alpha=0.8))

ax2.set_xlim(15, 65)
ax2.set_ylim(-10, 110)
ax2.set_xlabel('Age', fontsize=16, fontweight='bold')
ax2.set_ylabel('Arbitrary Y (for visualization)', fontsize=14)
ax2.set_title('AFTER SPLIT\nTwo Pure Groups', fontsize=20, fontweight='bold', pad=20)
ax2.set_facecolor('#E8F5E9')
ax2.grid(alpha=0.3)

# Add group labels
ax2.text(25, -5, 'Left Group (n=60)\nClass A: 5 (8%)\nClass B: 55 (92%)\nGini: 0.15',
         ha='center', fontsize=12, bbox=dict(boxstyle='round', facecolor='#F1F8F1',
         edgecolor='#00AA00', linewidth=2))
ax2.text(50, -5, 'Right Group (n=60)\nClass A: 55 (92%)\nClass B: 5 (8%)\nGini: 0.15',
         ha='center', fontsize=12, bbox=dict(boxstyle='round', facecolor='#F1F6FB',
         edgecolor='#0066CC', linewidth=2))

# Add information gain
fig.text(0.75, 0.05, 'Information Gain = 0.35\n✓ Good Split!',
         ha='center', fontsize=18, fontweight='bold', color='#00AA00',
         bbox=dict(boxstyle='round', facecolor='#FFFACD', linewidth=2))

plt.tight_layout(rect=[0, 0.08, 1, 1])
plt.savefig('tree_splitting_animation.png', dpi=150, bbox_inches='tight',
            facecolor='white', edgecolor='none')
plt.show()
```

### Option 2: PowerPoint/Slides

1. Create two side-by-side frames
2. Left frame: Scatter plot with mixed blue/red dots
3. Right frame: Two groups separated by vertical line
4. Add labels, annotations, and arrow between frames
5. Export as PNG

---

## Quality Checklist

- [ ] Both panels clearly visible
- [ ] Data points are large enough to see (15px minimum)
- [ ] Colors are distinct (blue vs red)
- [ ] Gini impurity values are accurate
- [ ] Information gain calculation is shown
- [ ] Labels are legible (14pt minimum)
- [ ] Arrow between panels is prominent
- [ ] Split line is clearly visible
- [ ] Background colors differentiate before/after

---

## Usage During Teaching

**When to Show:**
- Segment 2 (0:25): When explaining information gain

**Teaching Script:**
> "Let's see what a good split looks like. On the left, we have all our data mixed together - 50% Class A, 50% Class B. Gini impurity is 0.50, which means maximum mixing. Now watch what happens when we split on 'Age > 30'..."

> [Point to right panel]

> "After the split, we have two groups. Left group: mostly young people with low income. Right group: mostly older people with high income. Each group's Gini impurity dropped to 0.15 - much purer! This split has high information gain (0.35) because it separated the classes well."

> "This is what decision trees do automatically - they try every possible split and choose the one with highest information gain."

---

## Alternative Versions

**Version 1: Bad Split (for comparison)**
- After split, both groups still mixed (Gini ~0.48 each)
- Information gain = 0.02 (very low)
- Label: "Bad Split - Didn't help!"

**Version 2: Animated GIF**
- Show split line moving from left to right
- Update information gain in real-time
- Highlight when gain is maximized

**Version 3: Multiple Splits**
- Show 3 different split options side-by-side
- Compare information gain of each
- Highlight the best one

---

## Version

Tree Splitting Animation Specification v1.0 | January 24, 2026
