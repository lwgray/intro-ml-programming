# Visual Specification: Feature Importance Plot

## Purpose

Show a horizontal bar chart of feature importance from a trained tree-based model (Random Forest or XGBoost) on the Adult Income dataset. Demonstrates which features drive predictions.

---

## Specifications

**Filename:** `feature_importance_plot.png`

**Dimensions:** 1200 x 800 pixels (3:2 aspect ratio)

**Format:** PNG with white background

---

## Visual Layout

```
┌──────────────────────────────────────────────────────────┐
│   Feature Importance: Adult Income Prediction            │
│   (Random Forest Model)                                   │
├──────────────────────────────────────────────────────────┤
│                                                           │
│  capital-gain        ████████████████████ 0.324          │
│  age                 ████████████ 0.156                  │
│  education-num       ███████████ 0.128                   │
│  hours-per-week      ████████ 0.094                      │
│  capital-loss        ██████ 0.071                        │
│  relationship        █████ 0.058                         │
│  occupation          ████ 0.042                          │
│  fnlwgt              ███ 0.036                           │
│  marital-status      ███ 0.034                           │
│  sex                 ██ 0.027                            │
│  ─────────────────────────────────────────────           │
│  (Remaining 4 features with importance < 0.02)           │
│                                                           │
│                0.0    0.1    0.2    0.3    0.4           │
│                      Feature Importance                   │
└──────────────────────────────────────────────────────────┘
```

---

## Detailed Specifications

### Title

**Text:** "Feature Importance: Adult Income Prediction (Random Forest Model)"
- Font: Bold, 20pt, sans-serif
- Color: #003366 (dark blue)
- Alignment: Centered
- Position: 40px from top

### Axes

**Y-Axis (Feature Names):**
- Features listed in descending order of importance
- Font: Regular, 14pt, sans-serif
- Color: #333333 (dark gray)
- Alignment: Right-aligned with bars
- Show top 10 features only (group remaining as "Others < 0.02")

**X-Axis (Importance Values):**
- Range: 0.0 to maximum importance + 10% padding
- Tick marks: Every 0.1 (0.0, 0.1, 0.2, 0.3, 0.4)
- Grid lines: Vertical, light gray (#CCCCCC), dashed
- Label: "Feature Importance" (centered below axis)
- Font: Regular, 14pt

### Bars

**Bar Style:**
- Orientation: Horizontal
- Height: 40px per bar
- Spacing: 10px between bars
- Color gradient: Dark blue (#003366) to light blue (#6699CC)
  - Higher importance → darker blue
  - Lower importance → lighter blue
- Border: 1px solid #003366
- Slight 3D effect (optional): Light shadow below each bar

**Value Labels:**
- Display exact importance value at end of each bar
- Font: Bold, 12pt
- Color: #003366
- Format: Three decimal places (e.g., "0.324")
- Position: 5px to the right of bar end

### Data Values (Example)

Use these realistic values from Adult Income dataset:

| Feature | Importance |
|---------|------------|
| capital-gain | 0.324 |
| age | 0.156 |
| education-num | 0.128 |
| hours-per-week | 0.094 |
| capital-loss | 0.071 |
| relationship | 0.058 |
| occupation | 0.042 |
| fnlwgt | 0.036 |
| marital-status | 0.034 |
| sex | 0.027 |
| native-country | 0.018 |
| workclass | 0.007 |
| race | 0.003 |
| education | 0.002 |

**Note:** Sum should equal 1.0 (or very close due to rounding)

### Annotation

**Top Feature Highlight:**
Add callout box pointing to top bar:
```
"capital-gain is most important:
Investment income strongly
predicts high earnings"
```
- Font: Italic, 12pt
- Background: Light yellow (#FFFACD)
- Border: 2px dashed, #FF9900
- Arrow pointing to "capital-gain" bar

**Warning Box (Bottom):**
```
⚠️ Remember: Importance shows correlation, not causation!
High importance ≠ changing this feature will change the outcome
```
- Font: Bold, 11pt
- Color: #CC0000 (red)
- Background: Light pink (#FFE6E6)
- Border: 2px solid #CC0000
- Position: Bottom of chart, centered

---

## Color Scheme

**Gradient for Bars:**
- Highest importance (0.324): #003366 (dark blue)
- Medium importance (0.15): #336699 (medium blue)
- Low importance (0.05): #6699CC (light blue)
- Very low importance (<0.02): #99CCFF (very light blue)

**Background:**
- Plot area: White (#FFFFFF)
- Grid lines: Light gray (#CCCCCC)

**Text:**
- Title: Dark blue (#003366)
- Axis labels: Dark gray (#333333)
- Value labels: Dark blue (#003366)
- Warning text: Red (#CC0000)

---

## Creation Code

### Option 1: Matplotlib (Recommended)

```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Feature importance data (from trained Random Forest)
features = [
    'capital-gain', 'age', 'education-num', 'hours-per-week',
    'capital-loss', 'relationship', 'occupation', 'fnlwgt',
    'marital-status', 'sex'
]

importances = [0.324, 0.156, 0.128, 0.094, 0.071, 0.058, 0.042,
               0.036, 0.034, 0.027]

# Create DataFrame and sort
importance_df = pd.DataFrame({
    'Feature': features,
    'Importance': importances
}).sort_values('Importance', ascending=True)  # Ascending for horizontal bars

# Create color gradient (darker for higher importance)
colors = plt.cm.Blues(np.linspace(0.4, 0.9, len(importances)))

# Create figure
fig, ax = plt.subplots(figsize=(12, 8))

# Create horizontal bars
bars = ax.barh(importance_df['Feature'], importance_df['Importance'],
               color=colors, edgecolor='#003366', linewidth=1.5)

# Add value labels
for i, (feature, importance) in enumerate(zip(importance_df['Feature'],
                                                importance_df['Importance'])):
    ax.text(importance + 0.01, i, f'{importance:.3f}',
            va='center', fontsize=12, fontweight='bold', color='#003366')

# Formatting
ax.set_xlabel('Feature Importance', fontsize=14, fontweight='bold')
ax.set_title('Feature Importance: Adult Income Prediction\n(Random Forest Model)',
             fontsize=20, fontweight='bold', pad=20, color='#003366')
ax.set_xlim(0, max(importances) * 1.15)
ax.grid(axis='x', alpha=0.3, linestyle='--', color='#CCCCCC')
ax.set_axisbelow(True)

# Highlight top feature
ax.annotate('capital-gain is most important:\nInvestment income strongly\npredicts high earnings',
            xy=(importances[0], len(features)-1),
            xytext=(importances[0] + 0.08, len(features)-1.5),
            fontsize=11, style='italic',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#FFFACD',
                     edgecolor='#FF9900', linestyle='dashed', linewidth=2),
            arrowprops=dict(arrowstyle='->', lw=2, color='#FF9900'))

# Warning
fig.text(0.5, 0.05,
         '⚠️  Remember: Importance shows correlation, not causation!\n' +
         'High importance ≠ changing this feature will change the outcome',
         ha='center', fontsize=11, fontweight='bold', color='#CC0000',
         bbox=dict(boxstyle='round', facecolor='#FFE6E6',
                  edgecolor='#CC0000', linewidth=2))

plt.tight_layout(rect=[0, 0.08, 1, 1])
plt.savefig('feature_importance_plot.png', dpi=150, bbox_inches='tight',
            facecolor='white', edgecolor='none')
plt.show()
```

### Option 2: From Actual Model

```python
# After training Random Forest on Adult Income data
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import matplotlib.pyplot as plt

# Train model (assuming X_train, y_train are loaded)
rf = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
rf.fit(X_train, y_train)

# Extract importances
importances = rf.feature_importances_
feature_names = X_train.columns

# Create DataFrame
importance_df = pd.DataFrame({
    'Feature': feature_names,
    'Importance': importances
}).sort_values('Importance', ascending=False)

# Plot top 10
top_10 = importance_df.head(10).sort_values('Importance', ascending=True)

# (Use plotting code from Option 1 above)
```

---

## Quality Checklist

- [ ] Features sorted by importance (descending)
- [ ] All text is legible (12pt minimum)
- [ ] Value labels don't overlap with bars
- [ ] Colors differentiate importance levels
- [ ] Grid lines are subtle (not distracting)
- [ ] Warning about causation is prominent
- [ ] Title includes model name (Random Forest)
- [ ] Importance values sum to ~1.0
- [ ] Top feature annotation is clear

---

## Usage During Teaching

**When to Show:**
- Segment 3 (1:05): Brief introduction to feature importance
- Segment 6 (2:20): Deep dive during comparison (main usage)

**Teaching Script:**
> "After training our Random Forest, we can extract feature importance. This chart shows which features the model uses most for predictions. See capital-gain at the top? With importance 0.324, it's the single most influential feature - about one-third of the model's decision-making comes from investment income."

> "Age is second at 0.156, education third at 0.128. Together, the top 3 features account for 60% of the model's logic."

> "But CRITICAL WARNING: This does NOT mean capital-gain CAUSES high income in a causal sense. It means the model USES this feature heavily. If you manipulated capital-gain artificially, the real-world outcome might not change. Correlation, not causation!"

**Common Student Question:**
> "Why is 'fnlwgt' (final weight) in the top 10? What does it mean?"

**Answer:**
> "Good question! 'fnlwgt' is a census weighting variable - it tells you how many people in the population this person represents. It probably shouldn't be used for prediction at all (it's metadata, not a feature). This shows a limitation: feature importance tells you what the model uses, not what's actually meaningful. You still need domain knowledge!"

---

## Alternative Versions

**Version 1: Comparison Across Models**
- Show 3 side-by-side charts: Decision Tree, Random Forest, XGBoost
- Compare how different models rank features
- Highlight agreements and disagreements

**Version 2: Top 5 Only**
- Simplify to just top 5 features
- Larger bars and text for clarity
- Use in slides for quick reference

**Version 3: Grouped by Category**
- Group features: Demographics, Work-related, Financial
- Show total importance per category
- Stacked bar chart

---

## File Variants

- `feature_importance_rf.png` - Random Forest version
- `feature_importance_xgb.png` - XGBoost version
- `feature_importance_dt.png` - Decision Tree version
- `feature_importance_comparison.png` - All three side-by-side

---

## Version

Feature Importance Plot Specification v1.0 | January 24, 2026
