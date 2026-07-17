# Visual Specification: GridSearchCV Heatmap

**Purpose:** Visualize hyperparameter grid search results as a 2D heatmap showing cross-validation scores.

**File name:** `grid_search_visualization.png`

**Usage:** Display when explaining GridSearchCV (Segment 3, Minute 50)

---

## Visual Layout

**Dimensions:** 1000px × 800px
**Background:** White (#FFFFFF)
**Font:** Sans-serif (Arial)

---

## Title

**Text:** "GridSearchCV: Hyperparameter Tuning Results"
**Position:** Top center, 30px from top
**Font size:** 28pt
**Font weight:** Bold
**Color:** Dark blue (#1f4788)

**Subtitle:**
**Text:** "Random Forest on Adult Income Dataset (5-Fold CV)"
**Position:** 70px from top
**Font size:** 16pt
**Color:** Gray (#666666)

---

## Heatmap Grid

### Grid Structure

**Position:** Centered, starting 150px from top
**Grid dimensions:** 3 rows × 3 columns
**Cell size:** 150px × 150px
**Cell spacing:** 10px between cells

**X-axis:** `n_estimators` parameter
- Values: 50, 100, 200
- Position: Bottom of grid
- Labels: 20px below grid

**Y-axis:** `max_depth` parameter
- Values: 10, 20, 30
- Position: Left of grid
- Labels: 20px to the left

---

### Axis Labels

**X-axis title:**
- Text: "n_estimators (Number of Trees)"
- Position: Below x-axis values, centered
- Font size:** 16pt
- Font weight: Bold

**Y-axis title:**
- Text: "max_depth (Tree Depth)"
- Position: Left of y-axis values, rotated 90° counter-clockwise
- Font size: 16pt
- Font weight: Bold

---

### Cell Specifications

**Each cell contains:**
1. Background color (heatmap)
2. CV score (centered text)
3. Border

**Cell styling:**
- Border: 2px solid white (#FFFFFF)
- Corner radius: 4px

---

### Heatmap Colors (Score-based)

**Color scale:** Green (low) → Yellow (medium) → Red (high)

| Score Range | Color | Hex Code |
|-------------|-------|----------|
| 0.80-0.83 | Light green | #d5f4e6 |
| 0.84-0.86 | Green | #52c41a |
| 0.87-0.88 | Yellow-green | #95de64 |
| 0.89-0.90 | Yellow | #fadb14 |
| 0.91+ | Orange | #fa8c16 |

---

### Grid Values (Example Data)

**Row 1 (max_depth=10):**
- (50, 10): 0.822 → #d5f4e6 (light green)
- (100, 10): 0.847 → #52c41a (green)
- (200, 10): 0.851 → #52c41a (green)

**Row 2 (max_depth=20):**
- (50, 20): 0.871 → #95de64 (yellow-green)
- (100, 20): **0.893** → #fadb14 (yellow) **← BEST**
- (200, 20): 0.886 → #95de64 (yellow-green)

**Row 3 (max_depth=30):**
- (50, 30): 0.867 → #95de64 (yellow-green)
- (100, 30): 0.882 → #95de64 (yellow-green)
- (200, 30): 0.878 → #95de64 (yellow-green)

---

### Cell Text

**For each cell:**
- Text: CV score (3 decimal places)
- Font size: 24pt
- Font weight: Bold
- Color: Black (#000000) for light backgrounds, White (#FFFFFF) for dark

**Example:**
- Cell (100, 20): "0.893" in black text on yellow background

---

### Best Parameters Highlight

**Cell (100, 20) - the best:**

**Additional border:**
- Border: 4px solid dark blue (#1f4788)
- Border style: Solid

**Star icon:**
- Position: Top-right corner of cell
- Icon: ⭐ (or gold star)
- Size: 24px

**Label:**
- Text: "BEST"
- Position: Bottom of cell
- Font size: 12pt
- Font weight: Bold
- Color: Dark blue (#1f4788)
- Background: White semi-transparent box

---

## Color Legend

**Position:** Right side of heatmap, 200px from top

**Box:**
- Width: 200px
- Height: 300px
- Border: 1px solid gray (#cccccc)
- Fill: White (#FFFFFF)
- Corner radius: 4px

**Title:**
- Text: "CV Score"
- Font size: 14pt
- Font weight: Bold
- Position: Top of box, centered

**Color scale (vertical gradient):**
- Top: Orange (#fa8c16) - "≥ 0.91 (Best)"
- Middle-top: Yellow (#fadb14) - "0.89-0.90 (Very Good)"
- Middle: Yellow-green (#95de64) - "0.87-0.88 (Good)"
- Middle-bottom: Green (#52c41a) - "0.84-0.86 (Fair)"
- Bottom: Light green (#d5f4e6) - "0.80-0.83 (Poor)"

**Each level:**
- Rectangle: 180px × 40px
- Label to the right: Score range (10pt)

---

## Results Summary Box

**Position:** Bottom, centered, 650px from top

**Box:**
- Width: 700px
- Height: 100px
- Border: 2px solid dark blue (#1f4788)
- Fill: Light blue (#e3f2fd)
- Corner radius: 8px

**Content:**

**Line 1:**
- Text: "Best Hyperparameters Found:"
- Font size: 18pt
- Font weight: Bold
- Color: Dark blue (#1f4788)

**Line 2:**
- Text: "n_estimators=100, max_depth=20"
- Font size: 20pt
- Font weight: Bold
- Color: Black (#000000)

**Line 3:**
- Text: "Cross-Validation Score: 0.893 ± 0.012"
- Font size: 16pt
- Color: Black (#000000)

---

## Annotations

### Annotation 1 (pointing to best cell)

**Arrow:**
- Start: Results summary box
- End: Best cell (100, 20)
- Style: Curved arrow, dark blue (#1f4788)
- Width: 2px

**Label:**
- Text: "Optimal combination"
- Position: Along arrow
- Font size: 12pt
- Color: Dark blue (#1f4788)

---

### Annotation 2 (insight box)

**Position:** Top right corner, 30px from top, 30px from right

**Box:**
- Width: 250px
- Height: 80px
- Border: 2px solid green (#27ae60)
- Fill: Light green (#d5f4e6)

**Content:**
- Line 1: "💡 Insight"
  - Font size: 14pt
  - Font weight: Bold
  - Color: Green (#27ae60)

- Line 2: "More trees (n_estimators) helps, but moderate depth (20) is optimal"
  - Font size: 11pt
  - Color: Black (#000000)

---

## Color Palette

| Element | Color | Hex Code |
|---------|-------|----------|
| Highest scores | Orange | #fa8c16 |
| High scores | Yellow | #fadb14 |
| Good scores | Yellow-green | #95de64 |
| Fair scores | Green | #52c41a |
| Low scores | Light green | #d5f4e6 |
| Best cell border | Dark blue | #1f4788 |
| Title | Dark blue | #1f4788 |
| Results box border | Dark blue | #1f4788 |
| Results box fill | Light blue | #e3f2fd |
| Insight box border | Green | #27ae60 |
| Insight box fill | Light green | #d5f4e6 |
| Text (primary) | Black | #000000 |
| Text (secondary) | Gray | #666666 |
| Cell borders | White | #FFFFFF |

---

## Example Python Code

```python
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Grid search results (example data)
param1_values = [50, 100, 200]  # n_estimators
param2_values = [10, 20, 30]    # max_depth

# CV scores (rows = max_depth, cols = n_estimators)
scores = np.array([
    [0.822, 0.847, 0.851],  # max_depth=10
    [0.871, 0.893, 0.886],  # max_depth=20
    [0.867, 0.882, 0.878]   # max_depth=30
])

# Create figure
fig, ax = plt.subplots(figsize=(10, 8))

# Create heatmap
sns.heatmap(scores, annot=True, fmt='.3f', cmap='RdYlGn_r',
           xticklabels=param1_values, yticklabels=param2_values,
           linewidths=2, linecolor='white', cbar_kws={'label': 'CV Score'},
           vmin=0.80, vmax=0.91, ax=ax, square=True,
           annot_kws={'fontsize': 24, 'weight': 'bold'})

# Labels
ax.set_xlabel('n_estimators (Number of Trees)', fontsize=16, weight='bold')
ax.set_ylabel('max_depth (Tree Depth)', fontsize=16, weight='bold')
ax.set_title('GridSearchCV: Hyperparameter Tuning Results\nRandom Forest on Adult Income Dataset (5-Fold CV)',
            fontsize=22, weight='bold', pad=20)

# Highlight best cell (row=1, col=1)
best_i, best_j = 1, 1
ax.add_patch(plt.Rectangle((best_j, best_i), 1, 1, fill=False,
                          edgecolor='#1f4788', lw=4))

# Add star to best cell
ax.text(best_j + 0.85, best_i + 0.15, '⭐', fontsize=20, ha='right', va='top')

# Results text
plt.figtext(0.5, 0.05, 'Best Hyperparameters: n_estimators=100, max_depth=20\nCV Score: 0.893 ± 0.012',
           ha='center', fontsize=16, bbox=dict(boxstyle='round', facecolor='#e3f2fd',
           edgecolor='#1f4788', linewidth=2))

plt.tight_layout()
plt.savefig('grid_search_visualization.png', dpi=300, bbox_inches='tight',
           facecolor='white')
plt.show()
```

---

## Validation Checklist

- ✓ 3×3 grid shown
- ✓ X-axis: n_estimators (50, 100, 200)
- ✓ Y-axis: max_depth (10, 20, 30)
- ✓ Heatmap colors represent scores (green→yellow→orange)
- ✓ Best cell (100, 20) is highlighted with border and star
- ✓ CV scores displayed in each cell (3 decimals)
- ✓ Color legend present
- ✓ Results summary box shows best parameters
- ✓ Annotations explain insight
- ✓ Axis labels clear

---

**This heatmap provides a clear visual representation of how different hyperparameter combinations affect model performance.**
