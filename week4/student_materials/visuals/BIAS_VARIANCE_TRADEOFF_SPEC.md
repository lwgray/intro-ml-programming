# Visual Specification: Bias-Variance Tradeoff Curve

**Purpose:** Classic U-shaped curve showing training error, test error, and the optimal model complexity.

**File name:** `bias_variance_tradeoff.png`

**Usage:** Display when explaining regularization and model complexity (Segment 5, Minute 80)

---

## Visual Layout

**Dimensions:** 1000px × 700px
**Background:** White (#FFFFFF)
**Font:** Sans-serif

---

## Title

**Text:** "Bias-Variance Tradeoff"
**Position:** Top center, 30px from top
**Font size:** 30pt
**Font weight:** Bold
**Color:** Dark blue (#1f4788)

**Subtitle:**
**Text:** "Finding the Sweet Spot of Model Complexity"
**Position:** 70px from top
**Font size:** 16pt
**Color:** Gray (#666666)

---

## Graph Area

**Position:** Centered, 130px from top
**Size:** 800px width × 500px height
**Border:** 2px solid black (#000000)
**Background:** White (#FFFFFF)

---

## Axes

### X-Axis (Model Complexity)

**Position:** Bottom of graph area
**Range:** 0 to 100 (represents complexity scale)
**Color:** Black (#000000)
**Width:** 2px

**Label:**
- Text: "Model Complexity →"
- Position: Below axis, centered
- Font size: 18pt
- Font weight: Bold
- Color: Black (#000000)

**Tick labels (left to right):**
- Position 10: "Simple\n(High Bias)" - 12pt, gray (#666666)
- Position 50: "Optimal" - 14pt, bold, green (#27ae60)
- Position 90: "Complex\n(High Variance)" - 12pt, gray (#666666)

---

### Y-Axis (Error)

**Position:** Left of graph area
**Range:** 0 to 100 (represents error percentage)
**Color:** Black (#000000)
**Width:** 2px

**Label:**
- Text: "← Error (Lower is Better)"
- Position: Left of axis, rotated 90° counter-clockwise
- Font size: 18pt
- Font weight: Bold
- Color: Black (#000000)

**Tick labels:**
- 0%, 10%, 20%, 30%, 40%, 50%
- Font size: 12pt
- Color: Gray (#666666)

---

## Curves

### Curve 1: Training Error (Blue)

**Type:** Decreasing curve (logarithmic decay)
**Color:** Blue (#3498db)
**Line width:** 4px
**Style:** Solid

**Data points (example):**
- (10, 45) - High error for simple models
- (20, 32)
- (30, 22)
- (40, 15)
- (50, 10) - Optimal point
- (60, 7)
- (70, 5)
- (80, 3)
- (90, 2) - Very low error for complex models

**Curve behavior:**
- Starts high (left side - simple models)
- Decreases steadily as complexity increases
- Approaches near-zero error (right side - complex models)

**Label:**
- Text: "Training Error"
- Position: Near end of curve (80, 5)
- Font size: 14pt, Bold
- Color: Blue (#2874a6)
- Background: White semi-transparent box

---

### Curve 2: Test Error (Red) - U-Shaped

**Type:** U-shaped curve (quadratic)
**Color:** Red (#e74c3c)
**Line width:** 4px
**Style:** Solid

**Data points (example):**
- (10, 42) - High error (underfitting)
- (20, 28)
- (30, 18)
- (40, 12)
- (50, 10) - **MINIMUM** (optimal point)
- (60, 12)
- (70, 18)
- (80, 28)
- (90, 42) - High error again (overfitting)

**Curve behavior:**
- Starts high (left side - underfitting/high bias)
- Decreases to minimum around complexity = 50
- Increases again (right side - overfitting/high variance)

**Label:**
- Text: "Test Error (Validation)"
- Position: Near middle of curve (50, 15)
- Font size: 14pt, Bold
- Color: Red (#c0392b)
- Background: White semi-transparent box

---

## Optimal Point Marker

**Position:** Where test error is minimum (50, 10)

**Marker:**
- Type: Large circle
- Size: 16px diameter
- Fill: Green (#27ae60)
- Border: White (#FFFFFF), 3px width

**Vertical line (dashed):**
- From: Optimal point down to x-axis
- Style: Dashed line, green (#27ae60), 2px
- Label at bottom: "Optimal Complexity" (14pt, bold, green)

**Annotation box (near optimal point):**
- Position: Above optimal point
- Size: 200px × 60px
- Border: 2px solid green (#27ae60)
- Fill: Light green (#d5f4e6)

**Text in box:**
- Line 1: "⭐ Sweet Spot"
  - Font size: 14pt, Bold, Green (#1e8449)
- Line 2: "Lowest test error"
  - Font size: 11pt

---

## Region Annotations

### Left Region: Underfitting (High Bias)

**Position:** Left side of graph (x = 0 to 30)

**Shaded area:**
- Fill: Light yellow (#fffacd, 30% opacity)
- Border: None

**Label box:**
- Position: Top of region (15, 50)
- Size: 180px × 80px
- Border: 2px solid yellow (#f39c12)
- Fill: Light yellow (#fcf3cf)

**Text:**
- Line 1: "⚠️ Underfitting"
  - Font size: 14pt, Bold, Orange (#d68910)
- Line 2: "High Bias"
  - Font size: 12pt
- Line 3: "Too Simple"
  - Font size: 11pt
- Line 4: "Can't capture patterns"
  - Font size: 10pt, Italic, Gray

---

### Middle Region: Just Right

**Position:** Middle of graph (x = 40 to 60)

**Shaded area:**
- Fill: Light green (#d5f4e6, 30% opacity)
- Border: None

**Label box:**
- Position: Top of region (50, 55)
- Size: 160px × 60px
- Border: 2px solid green (#27ae60)
- Fill: Light green (#d5f4e6)

**Text:**
- Line 1: "✅ Good Fit"
  - Font size: 14pt, Bold, Green (#1e8449)
- Line 2: "Balanced"
  - Font size: 12pt
- Line 3: "Generalizes well"
  - Font size: 10pt, Italic, Gray

---

### Right Region: Overfitting (High Variance)

**Position:** Right side of graph (x = 70 to 100)

**Shaded area:**
- Fill: Light red (#fadbd8, 30% opacity)
- Border: None

**Label box:**
- Position: Top of region (85, 50)
- Size: 180px × 80px
- Border: 2px solid red (#e74c3c)
- Fill: Light red (#fadbd8)

**Text:**
- Line 1: "❌ Overfitting"
  - Font size: 14pt, Bold, Red (#c0392b)
- Line 2: "High Variance"
  - Font size: 12pt
- Line 3: "Too Complex"
  - Font size: 11pt
- Line 4: "Memorizes noise"
  - Font size: 10pt, Italic, Gray

---

## Gap Between Curves Annotation

**Arrow:**
- From: Training error curve at x=90
- To: Test error curve at x=90
- Style: Double-headed arrow, 2px, dark gray (#666666)

**Label:**
- Text: "Overfitting Gap"
- Position: Midpoint of arrow
- Font size: 11pt
- Color: Dark gray (#333333)

---

## Legend

**Position:** Top right corner, inside graph area (680, 180)

**Box:**
- Size: 250px × 100px
- Border: 1px solid gray (#cccccc)
- Fill: White (#FFFFFF)
- Corner radius: 4px

**Entries:**

**Row 1:**
- Line (30px, blue #3498db, 3px thick)
- Text: "Training Error" (12pt)

**Row 2:**
- Line (30px, red #e74c3c, 3px thick)
- Text: "Test/Validation Error" (12pt)

**Row 3:**
- Circle (12px, green #27ae60)
- Text: "Optimal Point" (12pt)

---

## Bottom Insight Box

**Position:** Below graph, centered, 650px from top

**Box:**
- Width: 800px, Height: 100px
- Border: 2px solid dark blue (#1f4788)
- Fill: Light blue (#e3f2fd)
- Corner radius: 8px

**Content:**

**Line 1:**
- Text: "💡 Key Insight: Regularization Controls Complexity"
- Font size: 16pt, Bold
- Color: Dark blue (#1f4788)

**Line 2:**
- Text: "• Increase regularization → Move left (simpler model)"
- Font size: 13pt

**Line 3:**
- Text: "• Decrease regularization → Move right (more complex model)"
- Font size: 13pt

**Line 4:**
- Text: "• Use cross-validation to find the sweet spot!"
- Font size: 13pt

---

## Color Palette

| Element | Color | Hex Code |
|---------|-------|----------|
| Training error curve | Blue | #3498db |
| Test error curve | Red | #e74c3c |
| Optimal point | Green | #27ae60 |
| Underfitting region | Light yellow | #fffacd |
| Good fit region | Light green | #d5f4e6 |
| Overfitting region | Light red | #fadbd8 |
| Title | Dark blue | #1f4788 |
| Axes | Black | #000000 |
| Text (primary) | Black | #000000 |
| Text (secondary) | Gray | #666666 |

---

## Example Python Code

```python
import matplotlib.pyplot as plt
import numpy as np

# Model complexity range
complexity = np.linspace(10, 90, 100)

# Training error (decreases with complexity)
training_error = 50 * np.exp(-0.04 * complexity) + 2

# Test error (U-shaped)
test_error = 0.015 * (complexity - 50)**2 + 10

# Find optimal point
optimal_idx = np.argmin(test_error)
optimal_complexity = complexity[optimal_idx]
optimal_error = test_error[optimal_idx]

# Create plot
fig, ax = plt.subplots(figsize=(10, 7))

# Plot curves
ax.plot(complexity, training_error, linewidth=4, color='#3498db',
       label='Training Error')
ax.plot(complexity, test_error, linewidth=4, color='#e74c3c',
       label='Test/Validation Error')

# Mark optimal point
ax.plot(optimal_complexity, optimal_error, 'o', markersize=16,
       color='#27ae60', markeredgecolor='white', markeredgewidth=3,
       label='Optimal Point')

# Vertical line at optimal
ax.axvline(optimal_complexity, linestyle='--', color='#27ae60',
          linewidth=2, alpha=0.7)

# Shade regions
ax.axvspan(10, 30, alpha=0.2, color='#f39c12', label='Underfitting')
ax.axvspan(40, 60, alpha=0.2, color='#27ae60', label='Good Fit')
ax.axvspan(70, 90, alpha=0.2, color='#e74c3c', label='Overfitting')

# Labels and title
ax.set_xlabel('Model Complexity →', fontsize=18, weight='bold')
ax.set_ylabel('← Error (Lower is Better)', fontsize=18, weight='bold')
ax.set_title('Bias-Variance Tradeoff\nFinding the Sweet Spot of Model Complexity',
            fontsize=24, weight='bold', pad=20)

# Set limits
ax.set_xlim(10, 90)
ax.set_ylim(0, 50)

# Grid
ax.grid(True, alpha=0.3, linestyle='--')

# Legend
ax.legend(loc='upper right', fontsize=12, frameon=True, shadow=True)

# Annotations
ax.text(20, 45, 'Underfitting\nHigh Bias\nToo Simple',
       fontsize=12, ha='center', bbox=dict(boxstyle='round',
       facecolor='#fcf3cf', edgecolor='#f39c12', linewidth=2))

ax.text(50, 55, 'Good Fit\nBalanced',
       fontsize=12, ha='center', bbox=dict(boxstyle='round',
       facecolor='#d5f4e6', edgecolor='#27ae60', linewidth=2))

ax.text(80, 45, 'Overfitting\nHigh Variance\nToo Complex',
       fontsize=12, ha='center', bbox=dict(boxstyle='round',
       facecolor='#fadbd8', edgecolor='#e74c3c', linewidth=2))

plt.tight_layout()
plt.savefig('bias_variance_tradeoff.png', dpi=300, bbox_inches='tight',
           facecolor='white')
plt.show()
```

---

## Validation Checklist

- ✓ Training error curve decreases monotonically (blue)
- ✓ Test error curve is U-shaped (red)
- ✓ Optimal point marked at minimum of test error (green)
- ✓ Three regions shaded: underfitting, good fit, overfitting
- ✓ Vertical dashed line at optimal complexity
- ✓ Gap between curves shown at high complexity (overfitting gap)
- ✓ Legend present
- ✓ Axes labeled clearly
- ✓ Bottom insight box explaining regularization
- ✓ Annotations explain each region

---

**This classic visualization helps students understand why both too-simple and too-complex models fail, and why cross-validation is needed to find the optimal complexity.**
