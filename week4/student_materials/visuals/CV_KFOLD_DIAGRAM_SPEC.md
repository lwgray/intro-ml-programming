# Visual Specification: K-Fold Cross-Validation Diagram

**Purpose:** Illustrate how 5-fold cross-validation rotates through the dataset, using each fold as test set once.

**File name:** `cv_kfold_diagram.png`

**Usage:** Display when introducing cross-validation concept (Segment 2, Minute 20)

---

## Visual Layout

**Dimensions:** 1200px × 800px
**Background:** White (#FFFFFF)
**Font:** Sans-serif (e.g., Arial, Helvetica)

---

## Component Specifications

### 1. Title

**Text:** "5-Fold Cross-Validation"
**Position:** Top center, 50px from top
**Font size:** 32pt
**Font weight:** Bold
**Color:** Dark blue (#1f4788)

---

### 2. Dataset Representation (Top)

**Position:** Below title, centered horizontally, 120px from top

**Visual:**
- Five equal-width rectangles side by side
- Each rectangle represents one fold
- Total width: 1000px (200px per fold)
- Height: 60px

**Rectangle styling:**
- Border: 2px solid black (#000000)
- Fill: Light gray (#e0e0e0)
- Corner radius: 4px
- 5px spacing between rectangles

**Labels (inside each rectangle):**
- Text: "Fold 1", "Fold 2", "Fold 3", "Fold 4", "Fold 5"
- Font size: 16pt
- Color: Black (#000000)
- Centered vertically and horizontally

**Annotation (below):**
- Text: "Complete Dataset (100% of data)"
- Position: Centered, 10px below rectangles
- Font size: 14pt
- Color: Gray (#666666)

---

### 3. Iteration Visualizations (5 rows)

**Position:** Below dataset representation, starting at 220px from top
**Spacing:** 100px vertical spacing between iterations

**Each iteration shows:**

#### Iteration 1

**Label (left side):**
- Text: "Iteration 1:"
- Position: 50px from left edge
- Font size: 18pt
- Font weight: Bold
- Color: Black (#000000)

**Fold rectangles (same dimensions as top):**
- Fold 1: **Test set**
  - Fill: Red (#e74c3c)
  - Label: "TEST" (white text, 16pt, bold)

- Folds 2-5: **Training set**
  - Fill: Green (#27ae60)
  - Label: "TRAIN" (white text, 16pt, bold)

**Score indicator (right side):**
- Text: "→ Score: 0.85"
- Position: 20px to the right of last fold
- Font size: 16pt
- Color: Black (#000000)

#### Iteration 2

**Fold rectangles:**
- Fold 1: **Training** (green)
- Fold 2: **Test** (red)
- Folds 3-5: **Training** (green)

**Score:** "→ Score: 0.83"

#### Iteration 3

**Fold rectangles:**
- Folds 1-2: **Training** (green)
- Fold 3: **Test** (red)
- Folds 4-5: **Training** (green)

**Score:** "→ Score: 0.87"

#### Iteration 4

**Fold rectangles:**
- Folds 1-3: **Training** (green)
- Fold 4: **Test** (red)
- Fold 5: **Training** (green)

**Score:** "→ Score: 0.84"

#### Iteration 5

**Fold rectangles:**
- Folds 1-4: **Training** (green)
- Fold 5: **Test** (red)

**Score:** "→ Score: 0.86"

---

### 4. Final Result Box

**Position:** Bottom of diagram, centered, 50px from bottom

**Box styling:**
- Width: 600px
- Height: 100px
- Border: 3px solid dark blue (#1f4788)
- Fill: Light blue (#d6eaf8)
- Corner radius: 8px

**Content (inside box):**

**Line 1:**
- Text: "Final Cross-Validation Score"
- Font size: 20pt
- Font weight: Bold
- Color: Dark blue (#1f4788)
- Centered, 15px from top of box

**Line 2:**
- Text: "Average: 0.850 ± 0.014"
- Font size: 24pt
- Font weight: Bold
- Color: Black (#000000)
- Centered, 50px from top of box

**Line 3:**
- Text: "(Mean of 5 scores: [0.85, 0.83, 0.87, 0.84, 0.86])"
- Font size: 12pt
- Color: Gray (#666666)
- Centered, 80px from top of box

---

### 5. Legend

**Position:** Bottom right corner, 20px from right edge, 20px from bottom

**Box styling:**
- Width: 200px
- Height: 80px
- Border: 1px solid gray (#999999)
- Fill: White (#FFFFFF)
- Corner radius: 4px

**Content:**

**Row 1:**
- Small rectangle (30px × 20px), fill green (#27ae60)
- Text: "Training Set" (12pt, black)
- Aligned horizontally, 10px spacing

**Row 2:**
- Small rectangle (30px × 20px), fill red (#e74c3c)
- Text: "Test Set" (12pt, black)
- Aligned horizontally, 10px spacing

---

## Color Palette

| Element | Color | Hex Code |
|---------|-------|----------|
| Training Set | Green | #27ae60 |
| Test Set | Red | #e74c3c |
| Dataset background | Light gray | #e0e0e0 |
| Title | Dark blue | #1f4788 |
| Result box border | Dark blue | #1f4788 |
| Result box fill | Light blue | #d6eaf8 |
| Text (primary) | Black | #000000 |
| Text (secondary) | Gray | #666666 |
| Borders | Black | #000000 |
| White background | White | #FFFFFF |

---

## Annotations & Arrows (Optional Enhancements)

**Arrow 1 (after Iteration 1):**
- Curved arrow from "Fold 1" (test) to score
- Label: "Each fold tested once"
- Dashed line, gray (#999999)
- Font size: 12pt

**Arrow 2 (pointing to Final Result Box):**
- Arrow from all 5 scores converging to final box
- Label: "Average across all iterations"
- Dashed line, dark blue (#1f4788)
- Font size: 12pt

---

## Text Annotations

**Annotation 1 (near Iteration 1):**
- Text: "20% of data used for testing"
- Position: To the right of red fold
- Font size: 11pt
- Color: Red (#e74c3c)
- Italic

**Annotation 2 (near Iteration 1):**
- Text: "80% of data used for training"
- Position: Above green folds
- Font size: 11pt
- Color: Green (#27ae60)
- Italic

---

## Design Notes

### Important Details:

1. **Alignment:** All fold rectangles must align vertically across iterations
2. **Spacing:** Consistent spacing between iterations (100px)
3. **Color contrast:** Ensure text is readable on colored backgrounds (white text on red/green)
4. **Visual flow:** Eyes should move top-to-bottom (dataset → iterations → final score)

### Accessibility:

- Use patterns in addition to colors (optional):
  - Test set: Red with diagonal stripes
  - Training set: Green with dots
- Ensure text contrast ratio > 4.5:1 for readability

### Export Settings:

- Format: PNG
- Resolution: 300 DPI (for printing)
- Web resolution: 72 DPI also acceptable
- Transparent background: No (use white)

---

## Example Code for Creation (Python with Matplotlib)

```python
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(12, 8))
ax.set_xlim(0, 1200)
ax.set_ylim(0, 800)
ax.axis('off')

# Title
ax.text(600, 750, '5-Fold Cross-Validation',
        fontsize=32, weight='bold', ha='center', color='#1f4788')

# Dataset representation (top)
fold_width = 200
fold_height = 60
start_x = 100
start_y = 650

for i in range(5):
    rect = patches.Rectangle((start_x + i * (fold_width + 5), start_y),
                             fold_width, fold_height,
                             linewidth=2, edgecolor='black', facecolor='#e0e0e0')
    ax.add_patch(rect)
    ax.text(start_x + i * (fold_width + 5) + fold_width/2, start_y + fold_height/2,
            f'Fold {i+1}', ha='center', va='center', fontsize=16)

# Annotation
ax.text(600, 580, 'Complete Dataset (100% of data)',
        ha='center', fontsize=14, color='#666666')

# Iterations
scores = [0.85, 0.83, 0.87, 0.84, 0.86]
iter_y = 520

for iter_num in range(5):
    # Label
    ax.text(50, iter_y - iter_num * 100 + fold_height/2, f'Iteration {iter_num+1}:',
            fontsize=18, weight='bold', va='center')

    # Folds
    for fold in range(5):
        color = '#e74c3c' if fold == iter_num else '#27ae60'
        label = 'TEST' if fold == iter_num else 'TRAIN'

        rect = patches.Rectangle((start_x + fold * (fold_width + 5),
                                 iter_y - iter_num * 100),
                                fold_width, fold_height,
                                linewidth=2, edgecolor='black', facecolor=color)
        ax.add_patch(rect)
        ax.text(start_x + fold * (fold_width + 5) + fold_width/2,
               iter_y - iter_num * 100 + fold_height/2,
               label, ha='center', va='center',
               fontsize=16, weight='bold', color='white')

    # Score
    ax.text(start_x + 5 * (fold_width + 5) + 20,
           iter_y - iter_num * 100 + fold_height/2,
           f'→ Score: {scores[iter_num]:.2f}',
           fontsize=16, va='center')

# Final result box
result_box = patches.FancyBboxPatch((300, 20), 600, 100,
                                   boxstyle="round,pad=10",
                                   linewidth=3, edgecolor='#1f4788',
                                   facecolor='#d6eaf8')
ax.add_patch(result_box)

ax.text(600, 95, 'Final Cross-Validation Score',
       fontsize=20, weight='bold', ha='center', color='#1f4788')
ax.text(600, 65, f'Average: {sum(scores)/len(scores):.3f} ± 0.014',
       fontsize=24, weight='bold', ha='center')
ax.text(600, 35, f'(Mean of 5 scores: {scores})',
       fontsize=12, ha='center', color='#666666')

# Legend
legend_x, legend_y = 980, 20
legend_box = patches.Rectangle((legend_x, legend_y), 200, 80,
                              linewidth=1, edgecolor='#999999', facecolor='white')
ax.add_patch(legend_box)

# Training legend
train_rect = patches.Rectangle((legend_x + 10, legend_y + 45), 30, 20,
                              facecolor='#27ae60')
ax.add_patch(train_rect)
ax.text(legend_x + 50, legend_y + 55, 'Training Set', fontsize=12, va='center')

# Test legend
test_rect = patches.Rectangle((legend_x + 10, legend_y + 15), 30, 20,
                             facecolor='#e74c3c')
ax.add_patch(test_rect)
ax.text(legend_x + 50, legend_y + 25, 'Test Set', fontsize=12, va='center')

plt.tight_layout()
plt.savefig('cv_kfold_diagram.png', dpi=300, bbox_inches='tight',
           facecolor='white')
plt.show()
```

---

## Alternative Tools

**PowerPoint/Keynote:**
1. Insert shapes (rectangles)
2. Color code as specified
3. Add text boxes
4. Group elements
5. Export as PNG

**Figma/Sketch:**
1. Create artboard (1200×800)
2. Add rectangles with specified colors
3. Add text layers
4. Export as PNG

**Adobe Illustrator:**
1. Create document (1200×800)
2. Draw shapes using rectangle tool
3. Apply colors from palette
4. Add text
5. Export as PNG

---

## Validation Checklist

Before finalizing the visual, verify:

- ✓ All 5 iterations shown
- ✓ Each fold is test set exactly once
- ✓ Training sets are always 4 folds (80%)
- ✓ Test sets are always 1 fold (20%)
- ✓ Scores are displayed for each iteration
- ✓ Final average is calculated correctly
- ✓ Colors match specification (green/red/blue)
- ✓ Text is readable (white on colored backgrounds)
- ✓ Legend is present and clear
- ✓ Dimensions are correct (1200×800)
- ✓ File is saved as PNG with appropriate resolution

---

**This specification should provide enough detail for a designer to create the visual without additional questions.**
