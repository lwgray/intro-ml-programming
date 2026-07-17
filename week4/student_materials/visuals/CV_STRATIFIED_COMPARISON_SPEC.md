# Visual Specification: Stratified vs Regular K-Fold Comparison

**Purpose:** Show the difference between regular K-Fold and Stratified K-Fold cross-validation for imbalanced datasets.

**File name:** `cv_stratified_comparison.png`

**Usage:** Display when explaining stratified cross-validation (Segment 2, Minute 35)

---

## Visual Layout

**Dimensions:** 1400px × 900px
**Background:** White (#FFFFFF)
**Font:** Sans-serif (Arial, Helvetica)

---

## Overall Structure

**Split into two panels (side-by-side comparison):**
- Left panel: Regular K-Fold (WRONG for imbalanced data)
- Right panel: Stratified K-Fold (CORRECT)

**Divider:**
- Vertical dashed line down the center (x = 700px)
- Color: Gray (#cccccc)
- Width: 2px

---

## Component Specifications

### 1. Main Title

**Text:** "Regular vs Stratified K-Fold Cross-Validation"
**Position:** Top center, 40px from top
**Font size:** 32pt
**Font weight:** Bold
**Color:** Dark blue (#1f4788)
**Alignment:** Center

---

### 2. Subtitle (Dataset Information)

**Text:** "Dataset: Adult Income (90% Class 0, 10% Class 1)"
**Position:** Below title, centered, 90px from top
**Font size:** 18pt
**Color:** Gray (#666666)

---

## LEFT PANEL: Regular K-Fold

### Panel Title

**Text:** "❌ Regular K-Fold"
**Position:** 350px from left (centered in left panel), 140px from top
**Font size:** 24pt
**Font weight:** Bold
**Color:** Red (#e74c3c)

**Subtitle:**
**Text:** "(Random split - Unbalanced folds)"
**Position:** Below title, 170px from top
**Font size:** 14pt
**Color:** Gray (#666666)
**Style:** Italic

---

### Fold Visualizations (5 rows)

**Starting position:** 220px from top
**Spacing:** 120px vertical between folds

**Each fold shows:**

#### Fold Structure

**Rectangle dimensions:**
- Width: 500px
- Height: 80px
- X position: 75px from left edge
- Border: 2px solid black (#000000)
- Corner radius: 4px

**Fill (split into two sections):**
- Left section: Class 0 (blue background)
- Right section: Class 1 (orange background)
- Sections proportional to class distribution in that fold

**Colors:**
- Class 0: Light blue (#3498db)
- Class 1: Orange (#e67e22)

**Labels inside rectangle:**
- Class 0 percentage (left side, white text, 16pt)
- Class 1 percentage (right side, white text, 16pt)

#### Fold 1
- Class 0: 92% (460px width)
- Class 1: 8% (40px width)
- Label: "Fold 1: 92% / 8%" (above rectangle)
- Warning icon: ⚠️ (to the right, yellow #f39c12)

#### Fold 2
- Class 0: 88% (440px width)
- Class 1: 12% (60px width)
- Label: "Fold 2: 88% / 12%"
- Warning icon: ⚠️

#### Fold 3
- Class 0: 95% (475px width)
- Class 1: 5% (25px width)
- Label: "Fold 3: 95% / 5%"
- Warning icon: ⚠️⚠️ (two warnings - very imbalanced!)
- Additional note: "Very few Class 1!" (red text, 12pt)

#### Fold 4
- Class 0: 87% (435px width)
- Class 1: 13% (65px width)
- Label: "Fold 4: 87% / 13%"
- Warning icon: ⚠️

#### Fold 5
- Class 0: 93% (465px width)
- Class 1: 7% (35px width)
- Label: "Fold 5: 93% / 7%"
- Warning icon: ⚠️

---

### Problem Annotation (Left Panel)

**Position:** Bottom of left panel, 800px from top
**Box:**
- Width: 550px
- Height: 80px
- Border: 2px solid red (#e74c3c)
- Fill: Light red (#fadbd8)
- Corner radius: 6px

**Text inside:**
- Line 1: "⚠️ Problem: Imbalanced folds!"
  - Font size: 18pt
  - Font weight: Bold
  - Color: Red (#c0392b)

- Line 2: "Each fold has different class distributions"
  - Font size: 14pt
  - Color: Black (#000000)

- Line 3: "Fold 3 barely saw Class 1 (only 5%!)"
  - Font size: 12pt
  - Color: Gray (#666666)

---

## RIGHT PANEL: Stratified K-Fold

### Panel Title

**Text:** "✓ Stratified K-Fold"
**Position:** 1050px from left (centered in right panel), 140px from top
**Font size:** 24pt
**Font weight:** Bold
**Color:** Green (#27ae60)

**Subtitle:**
**Text:** "(Preserves class distribution)"
**Position:** Below title, 170px from top
**Font size:** 14pt
**Color:** Gray (#666666)
**Style:** Italic

---

### Fold Visualizations (5 rows)

**Same vertical positions as left panel (220px start, 120px spacing)**

**Each fold shows:**

#### Fold Structure (same as left panel)

**All 5 folds have IDENTICAL distributions:**

#### Folds 1-5 (all the same)
- Class 0: 90% (450px width)
- Class 1: 10% (50px width)
- Label: "Fold X: 90% / 10%" (where X = fold number)
- Checkmark icon: ✓ (to the right, green #27ae60)

**Specific labels:**
- "Fold 1: 90% / 10%" ✓
- "Fold 2: 90% / 10%" ✓
- "Fold 3: 90% / 10%" ✓
- "Fold 4: 90% / 10%" ✓
- "Fold 5: 90% / 10%" ✓

---

### Solution Annotation (Right Panel)

**Position:** Bottom of right panel, 800px from top
**Box:**
- Width: 550px
- Height: 80px
- Border: 2px solid green (#27ae60)
- Fill: Light green (#d5f4e6)
- Corner radius: 6px

**Text inside:**
- Line 1: "✓ Solution: Balanced folds!"
  - Font size: 18pt
  - Font weight: Bold
  - Color: Green (#27ae60)

- Line 2: "Each fold represents the true population"
  - Font size: 14pt
  - Color: Black (#000000)

- Line 3: "All folds have 90% Class 0, 10% Class 1"
  - Font size: 12pt
  - Color: Gray (#666666)

---

## Additional Visual Elements

### Comparison Arrows

**Between panels (centered on divider):**

**Arrow 1 (pointing from left to right):**
- Position: 450px from top
- Start: End of Fold 3 (left panel)
- End: Start of Fold 3 (right panel)
- Color: Dark blue (#1f4788)
- Style: Dashed arrow
- Label above: "Stratification fixes imbalance" (12pt, dark blue)

---

### Legend

**Position:** Bottom center, 50px from bottom, centered

**Box:**
- Width: 300px
- Height: 60px
- Border: 1px solid gray (#999999)
- Fill: White (#FFFFFF)

**Content:**

**Row 1:**
- Small rectangle (40px × 20px), fill light blue (#3498db)
- Text: "Class 0 (Majority - 90%)" (12pt, black)

**Row 2:**
- Small rectangle (40px × 20px), fill orange (#e67e22)
- Text: "Class 1 (Minority - 10%)" (12pt, black)

---

## Color Palette

| Element | Color | Hex Code |
|---------|-------|----------|
| Class 0 (Majority) | Light blue | #3498db |
| Class 1 (Minority) | Orange | #e67e22 |
| Regular K-Fold title | Red | #e74c3c |
| Stratified K-Fold title | Green | #27ae60 |
| Problem box border | Red | #e74c3c |
| Problem box fill | Light red | #fadbd8 |
| Solution box border | Green | #27ae60 |
| Solution box fill | Light green | #d5f4e6 |
| Warning icon | Yellow | #f39c12 |
| Checkmark icon | Green | #27ae60 |
| Main title | Dark blue | #1f4788 |
| Text (primary) | Black | #000000 |
| Text (secondary) | Gray | #666666 |
| Divider | Gray | #cccccc |
| Background | White | #FFFFFF |

---

## Annotations

### Key Insight Box (Top Right)

**Position:** Top right corner, 50px from top, 50px from right

**Box:**
- Width: 250px
- Height: 60px
- Border: 2px solid dark blue (#1f4788)
- Fill: Light yellow (#fff9e6)

**Text:**
- Line 1: "💡 Key Insight"
  - Font size: 14pt
  - Font weight: Bold
  - Color: Dark blue (#1f4788)

- Line 2: "Use StratifiedKFold for classification with imbalanced classes"
  - Font size: 11pt
  - Color: Black (#000000)

---

## Code Example Box (Bottom)

**Position:** Very bottom, centered, 20px from bottom (optional, can be separate slide)

**Box:**
- Width: 1300px
- Height: 100px
- Border: 1px solid gray (#cccccc)
- Fill: Light gray (#f5f5f5)
- Corner radius: 4px

**Content (code snippet):**

```python
from sklearn.model_selection import KFold, StratifiedKFold

# ❌ Regular K-Fold (might get imbalanced folds)
kfold = KFold(n_splits=5, shuffle=True)

# ✓ Stratified K-Fold (preserves class distribution)
stratified_kfold = StratifiedKFold(n_splits=5, shuffle=True)
```

**Font:** Monospace (Courier New, 12pt)
**Syntax highlighting:**
- Keywords: Blue (#0066cc)
- Comments: Green (#27ae60)
- Strings: Orange (#e67e22)

---

## Design Notes

### Important Details:

1. **Proportional bars:** Class distribution bars must be proportional to percentages
2. **Visual contrast:** Left panel (chaotic/red) vs Right panel (uniform/green)
3. **Alignment:** Folds must align vertically across both panels for easy comparison
4. **Icons:** Use actual warning (⚠️) and checkmark (✓) symbols or icon equivalents

### Accessibility:

- Use patterns in addition to colors:
  - Class 0: Blue with horizontal lines
  - Class 1: Orange with dots
- Ensure all text has sufficient contrast

### Teaching Tip:

Point out Fold 3 on the left (95%/5%) and emphasize: "This fold barely saw Class 1! Model trained on this fold won't generalize well to minority class."

---

## Example Python Code for Creation

```python
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(14, 9))

# Configure axes
for ax in [ax_left, ax_right]:
    ax.set_xlim(0, 700)
    ax.set_ylim(0, 900)
    ax.axis('off')

# Main title (centered across both panels)
fig.suptitle('Regular vs Stratified K-Fold Cross-Validation',
            fontsize=32, weight='bold', color='#1f4788')

# LEFT PANEL: Regular K-Fold
ax_left.text(350, 850, '❌ Regular K-Fold',
            fontsize=24, weight='bold', ha='center', color='#e74c3c')
ax_left.text(350, 820, '(Random split - Unbalanced folds)',
            fontsize=14, ha='center', color='#666666', style='italic')

# Regular K-Fold distributions (example values)
regular_distributions = [
    (92, 8),   # Fold 1
    (88, 12),  # Fold 2
    (95, 5),   # Fold 3 - very imbalanced!
    (87, 13),  # Fold 4
    (93, 7)    # Fold 5
]

y_positions = [700, 580, 460, 340, 220]

for i, (class0_pct, class1_pct) in enumerate(regular_distributions):
    y = y_positions[i]

    # Class 0 bar
    class0_width = 5 * class0_pct
    rect0 = patches.Rectangle((75, y), class0_width, 80,
                              facecolor='#3498db', edgecolor='black', linewidth=2)
    ax_left.add_patch(rect0)
    ax_left.text(75 + class0_width/2, y + 40, f'{class0_pct}%',
                ha='center', va='center', fontsize=16, color='white', weight='bold')

    # Class 1 bar
    class1_width = 5 * class1_pct
    rect1 = patches.Rectangle((75 + class0_width, y), class1_width, 80,
                              facecolor='#e67e22', edgecolor='black', linewidth=2)
    ax_left.add_patch(rect1)
    ax_left.text(75 + class0_width + class1_width/2, y + 40, f'{class1_pct}%',
                ha='center', va='center', fontsize=16, color='white', weight='bold')

    # Label
    ax_left.text(50, y + 40, f'Fold {i+1}:', fontsize=14, ha='right', va='center')

    # Warning icon
    ax_left.text(600, y + 40, '⚠️', fontsize=20, ha='center', va='center')

# Problem box (left panel)
problem_box = patches.FancyBboxPatch((75, 80), 550, 80,
                                    boxstyle="round,pad=5",
                                    linewidth=2, edgecolor='#e74c3c',
                                    facecolor='#fadbd8')
ax_left.add_patch(problem_box)
ax_left.text(350, 145, '⚠️ Problem: Imbalanced folds!',
            fontsize=18, weight='bold', ha='center', color='#c0392b')
ax_left.text(350, 115, 'Each fold has different class distributions',
            fontsize=14, ha='center')
ax_left.text(350, 95, 'Fold 3 barely saw Class 1 (only 5%!)',
            fontsize=12, ha='center', color='#666666')

# RIGHT PANEL: Stratified K-Fold
ax_right.text(350, 850, '✓ Stratified K-Fold',
             fontsize=24, weight='bold', ha='center', color='#27ae60')
ax_right.text(350, 820, '(Preserves class distribution)',
             fontsize=14, ha='center', color='#666666', style='italic')

# Stratified K-Fold - all folds have same distribution
for i, y in enumerate(y_positions):
    # Class 0 bar (90%)
    rect0 = patches.Rectangle((75, y), 450, 80,
                              facecolor='#3498db', edgecolor='black', linewidth=2)
    ax_right.add_patch(rect0)
    ax_right.text(75 + 225, y + 40, '90%',
                 ha='center', va='center', fontsize=16, color='white', weight='bold')

    # Class 1 bar (10%)
    rect1 = patches.Rectangle((525, y), 50, 80,
                              facecolor='#e67e22', edgecolor='black', linewidth=2)
    ax_right.add_patch(rect1)
    ax_right.text(550, y + 40, '10%',
                 ha='center', va='center', fontsize=16, color='white', weight='bold')

    # Label
    ax_right.text(50, y + 40, f'Fold {i+1}:', fontsize=14, ha='right', va='center')

    # Checkmark icon
    ax_right.text(600, y + 40, '✓', fontsize=20, ha='center', va='center', color='#27ae60')

# Solution box (right panel)
solution_box = patches.FancyBboxPatch((75, 80), 550, 80,
                                     boxstyle="round,pad=5",
                                     linewidth=2, edgecolor='#27ae60',
                                     facecolor='#d5f4e6')
ax_right.add_patch(solution_box)
ax_right.text(350, 145, '✓ Solution: Balanced folds!',
             fontsize=18, weight='bold', ha='center', color='#27ae60')
ax_right.text(350, 115, 'Each fold represents the true population',
             fontsize=14, ha='center')
ax_right.text(350, 95, 'All folds have 90% Class 0, 10% Class 1',
             fontsize=12, ha='center', color='#666666')

plt.tight_layout()
plt.savefig('cv_stratified_comparison.png', dpi=300, bbox_inches='tight',
           facecolor='white')
plt.show()
```

---

## Validation Checklist

Before finalizing:

- ✓ Left panel shows varying class distributions across folds
- ✓ Right panel shows consistent 90/10 distribution across all folds
- ✓ Fold 3 on left is highlighted as problematic (95/5)
- ✓ Visual difference between panels is obvious (chaos vs uniformity)
- ✓ Colors match specification
- ✓ Icons (warning/checkmark) are visible
- ✓ Problem and solution boxes are present
- ✓ Legend explains colors
- ✓ Text is readable on colored backgrounds
- ✓ Proportions are accurate

---

**This specification allows a designer to create the visual showing the clear advantage of stratified cross-validation for imbalanced datasets.**
