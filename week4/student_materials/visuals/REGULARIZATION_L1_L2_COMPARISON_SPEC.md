# Visual Specification: L1 vs L2 Regularization Comparison

**Purpose:** Geometric visualization comparing L1 (Lasso) and L2 (Ridge) regularization constraints.

**File name:** `regularization_l1_l2_comparison.png`

**Usage:** Display when explaining regularization (Segment 5, Minute 82)

---

## Visual Layout

**Dimensions:** 1400px × 700px
**Background:** White (#FFFFFF)
**Font:** Sans-serif

---

## Overall Structure

**Two panels side-by-side:**
- Left: L1 Regularization (Lasso) - Diamond constraint
- Right: L2 Regularization (Ridge) - Circle constraint

**Center divider:**
- Vertical dashed line (x = 700px)
- Color: Gray (#cccccc), 2px width

---

## Main Title

**Text:** "L1 vs L2 Regularization: Geometric Interpretation"
**Position:** Top center, 30px from top
**Font size:** 28pt
**Font weight:** Bold
**Color:** Dark blue (#1f4788)

---

## LEFT PANEL: L1 (Lasso)

### Panel Title

**Text:** "L1 Regularization (Lasso)"
**Position:** Centered in left panel, 80px from top
**Font size:** 22pt
**Font weight:** Bold
**Color:** Red (#e74c3c)

**Formula below title:**
**Text:** "Penalty = Σ|w_i|"
**Position:** 115px from top
**Font size:** 16pt
**Style:** Italic
**Color:** Black (#000000)

---

### 2D Coordinate System

**Origin:** (250, 400) - center of left panel
**Axes:**
- X-axis (w₁): Horizontal, length 200px in each direction
- Y-axis (w₂): Vertical, length 200px in each direction
- Color: Black (#000000), 2px width
- Arrows at ends

**Axis labels:**
- X-axis: "w₁" at (470, 410), 14pt
- Y-axis: "w₂" at (240, 180), 14pt

**Grid:**
- Dashed lines at ±100px intervals
- Color: Light gray (#e0e0e0)
- Width: 1px

---

### L1 Constraint Region (Diamond)

**Shape:** Diamond (rotated square)
- Center: Origin (250, 400)
- Vertices:
  - Top: (250, 250)
  - Right: (400, 400)
  - Bottom: (250, 550)
  - Left: (100, 400)
- Size: 300px from center to vertex

**Styling:**
- Fill: Light red with transparency (#e74c3c, 20% opacity)
- Border: Solid red (#e74c3c), 3px width
- Border style: Solid

**Label inside:**
- Text: "Constraint Region\n|w₁| + |w₂| ≤ C"
- Position: Center of diamond
- Font size: 12pt
- Color: Red (#c0392b)
- Font weight: Bold

---

### Contour Lines (Error Surface)

**Elliptical contours (3-4 ellipses):**
- Centers: Slightly offset from origin, e.g., (320, 330)
- Representing: RSS (Residual Sum of Squares)
- Colors: Gradient from light blue (#3498db, outer) to dark blue (#1f4788, inner)
- Width: 2px
- Style: Solid

**Ellipse specifications:**
- Ellipse 1 (outer): Semi-major 250px, semi-minor 150px
- Ellipse 2 (middle): Semi-major 180px, semi-minor 110px
- Ellipse 3 (inner): Semi-major 120px, semi-minor 70px

**Ellipse labels:**
- Text: "RSS contours" with arrow pointing to outer ellipse
- Font size: 10pt
- Color: Blue (#3498db)

---

### Optimal Point (where contour touches diamond)

**Location:** Top vertex of diamond (250, 250)
- This is where an ellipse is tangent to the diamond

**Marker:**
- Large dot, 12px radius
- Fill: Green (#27ae60)
- Border: White (#FFFFFF), 2px

**Label:**
- Text: "Optimal Solution\n(w₁=0, w₂≠0)"
- Position: Above and right of point
- Font size: 12pt
- Color: Green (#27ae60)
- Font weight: Bold

**Arrow:**
- From label to point
- Color: Green (#27ae60)
- Style: Solid arrow

---

### Key Feature Annotation

**Box:**
- Position: Bottom left of left panel
- Width: 180px, Height: 80px
- Border: 2px solid red (#e74c3c)
- Fill: Light red (#fadbd8)

**Text:**
- Line 1: "✓ Sparse Solution"
  - Font size: 14pt, Bold, Red (#c0392b)
- Line 2: "Some weights → 0"
  - Font size: 11pt, Black
- Line 3: "Feature selection"
  - Font size: 11pt, Black

---

## RIGHT PANEL: L2 (Ridge)

### Panel Title

**Text:** "L2 Regularization (Ridge)"
**Position:** Centered in right panel, 80px from top
**Font size:** 22pt
**Font weight:** Bold
**Color:** Blue (#3498db)

**Formula below title:**
**Text:** "Penalty = Σw_i²"
**Position:** 115px from top
**Font size:** 16pt
**Style:** Italic
**Color:** Black (#000000)

---

### 2D Coordinate System

**Same as left panel:**
**Origin:** (950, 400) - center of right panel
**Axes:** Identical to left panel

---

### L2 Constraint Region (Circle)

**Shape:** Circle
- Center: Origin (950, 400)
- Radius: 150px

**Styling:**
- Fill: Light blue with transparency (#3498db, 20% opacity)
- Border: Solid blue (#3498db), 3px width

**Label inside:**
- Text: "Constraint Region\nw₁² + w₂² ≤ C"
- Position: Center of circle
- Font size: 12pt
- Color: Blue (#2874a6)
- Font weight: Bold

---

### Contour Lines (Error Surface)

**Same elliptical contours as left panel:**
- Same ellipse sizes and positions (adjusted for right panel origin)
- Same colors and styling

---

### Optimal Point (where contour touches circle)

**Location:** Point where ellipse is tangent to circle
- Example: (1020, 330) - on circle boundary, not on axis

**Marker:**
- Large dot, 12px radius
- Fill: Orange (#f39c12)
- Border: White (#FFFFFF), 2px

**Label:**
- Text: "Optimal Solution\n(w₁≠0, w₂≠0)"
- Position: Above and right of point
- Font size: 12pt
- Color: Orange (#d68910)
- Font weight: Bold

**Arrow:**
- From label to point
- Color: Orange (#f39c12)
- Style: Solid arrow

---

### Key Feature Annotation

**Box:**
- Position: Bottom right of right panel
- Width: 180px, Height: 80px
- Border: 2px solid blue (#3498db)
- Fill: Light blue (#d6eaf8)

**Text:**
- Line 1: "✓ Dense Solution"
  - Font size: 14pt, Bold, Blue (#2874a6)
- Line 2: "All weights shrunk"
  - Font size: 11pt, Black
- Line 3: "No feature selection"
  - Font size: 11pt, Black

---

## Comparison Table

**Position:** Bottom center, spanning both panels, 600px from top

**Table:**
- Width: 1200px, Height: 80px
- Border: 2px solid dark blue (#1f4788)
- Header background: Dark blue (#1f4788)

| Feature | L1 (Lasso) | L2 (Ridge) |
|---------|------------|------------|
| **Constraint shape** | Diamond | Circle |
| **Sparsity** | Yes (some w=0) | No (all w≠0) |
| **Feature selection** | ✓ Yes | ✗ No |
| **Use when** | Many irrelevant features | All features useful |

**Table styling:**
- Header row: White text on dark blue (#1f4788)
- Data rows: Alternating white/light gray (#f5f5f5)
- Font size: 12pt
- Cell padding: 10px

---

## Color Palette

| Element | Color | Hex Code |
|---------|-------|----------|
| L1 constraint | Red | #e74c3c |
| L1 fill | Light red (20% opacity) | #e74c3c33 |
| L2 constraint | Blue | #3498db |
| L2 fill | Light blue (20% opacity) | #3498db33 |
| Contour lines (outer) | Light blue | #3498db |
| Contour lines (inner) | Dark blue | #1f4788 |
| L1 optimal point | Green | #27ae60 |
| L2 optimal point | Orange | #f39c12 |
| Axes | Black | #000000 |
| Grid | Light gray | #e0e0e0 |
| Title | Dark blue | #1f4788 |

---

## Mathematical Annotations

**Annotation 1 (on L1 diamond vertices):**
- At top vertex (250, 250): Label "(0, C)"
- At right vertex (400, 400): Label "(C, 0)"
- Font size: 10pt, Color: Gray (#666666)

**Annotation 2 (on L2 circle):**
- At right edge: Label "(C, 0)"
- At top edge: Label "(0, C)"
- Font size: 10pt, Color: Gray (#666666)

---

## Key Insight Box

**Position:** Bottom, centered, 20px from bottom

**Box:**
- Width: 800px, Height: 60px
- Border: 2px solid green (#27ae60)
- Fill: Light yellow (#fff9e6)

**Text:**
- Line 1: "💡 Key Difference"
  - Font size: 14pt, Bold, Green (#27ae60)
- Line 2: "L1 hits axes (sparse) due to diamond corners. L2 approaches axes smoothly (dense)."
  - Font size: 12pt, Black

---

## Example Python Code

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon, Circle, Ellipse

fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(14, 7))

# Configure axes
for ax in [ax_left, ax_right]:
    ax.set_xlim(-200, 200)
    ax.set_ylim(-200, 200)
    ax.set_aspect('equal')
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.set_xlabel('$w_1$', fontsize=14)
    ax.set_ylabel('$w_2$', fontsize=14)
    ax.grid(True, linestyle='--', alpha=0.3)

# LEFT: L1 (Diamond)
ax_left.set_title('L1 Regularization (Lasso)\nPenalty = Σ|$w_i$|',
                 fontsize=18, weight='bold', color='#e74c3c')

# L1 constraint (diamond)
diamond = Polygon([
    (0, 150),   # top
    (150, 0),   # right
    (0, -150),  # bottom
    (-150, 0)   # left
], closed=True, fill=True, facecolor='#e74c3c', alpha=0.2,
   edgecolor='#e74c3c', linewidth=3)
ax_left.add_patch(diamond)

# Contour ellipses (RSS)
for size in [(250, 150), (180, 110), (120, 70)]:
    ellipse = Ellipse((70, -70), size[0], size[1], angle=30,
                     fill=False, edgecolor='#3498db', linewidth=2, alpha=0.6)
    ax_left.add_patch(ellipse)

# Optimal point (L1 - on axis)
ax_left.plot(0, 150, 'go', markersize=12, markeredgecolor='white',
            markeredgewidth=2, label='Optimal (sparse)')
ax_left.annotate('Optimal Solution\n($w_1$=0, $w_2$≠0)',
                xy=(0, 150), xytext=(50, 180),
                fontsize=12, color='#27ae60', weight='bold',
                arrowprops=dict(arrowstyle='->', color='#27ae60'))

# RIGHT: L2 (Circle)
ax_right.set_title('L2 Regularization (Ridge)\nPenalty = Σ$w_i^2$',
                  fontsize=18, weight='bold', color='#3498db')

# L2 constraint (circle)
circle = Circle((0, 0), 150, fill=True, facecolor='#3498db', alpha=0.2,
               edgecolor='#3498db', linewidth=3)
ax_right.add_patch(circle)

# Contour ellipses (same as left)
for size in [(250, 150), (180, 110), (120, 70)]:
    ellipse = Ellipse((70, -70), size[0], size[1], angle=30,
                     fill=False, edgecolor='#3498db', linewidth=2, alpha=0.6)
    ax_right.add_patch(ellipse)

# Optimal point (L2 - not on axis)
optimal_x, optimal_y = 106, 106  # On circle, not on axis
ax_right.plot(optimal_x, optimal_y, 'o', color='#f39c12', markersize=12,
             markeredgecolor='white', markeredgewidth=2, label='Optimal (dense)')
ax_right.annotate('Optimal Solution\n($w_1$≠0, $w_2$≠0)',
                 xy=(optimal_x, optimal_y), xytext=(optimal_x+40, optimal_y+50),
                 fontsize=12, color='#d68910', weight='bold',
                 arrowprops=dict(arrowstyle='->', color='#f39c12'))

plt.tight_layout()
plt.savefig('regularization_l1_l2_comparison.png', dpi=300,
           bbox_inches='tight', facecolor='white')
plt.show()
```

---

## Validation Checklist

- ✓ L1 constraint shown as diamond (rotated square)
- ✓ L2 constraint shown as circle
- ✓ Both panels have elliptical contour lines
- ✓ L1 optimal point hits axis (sparse solution)
- ✓ L2 optimal point does NOT hit axis (dense solution)
- ✓ Formulas displayed correctly (|w| vs w²)
- ✓ Key features annotated (sparse vs dense)
- ✓ Comparison table present
- ✓ Colors match specification
- ✓ Mathematical notation correct

---

**This visualization clearly shows WHY L1 produces sparse solutions (diamond has corners that align with axes) while L2 does not (circle is smooth).**
