# Visual Specification: XGBoost Comparison

## Purpose

Side-by-side performance comparison of Random Forest vs XGBoost on same dataset.

---

## Specifications

**Filename:** `xgboost_comparison.png`
**Dimensions:** 1200 x 800 pixels
**Format:** PNG, white background

---

## Visual Layout

```
┌────────────────────────────────────────────────────────────┐
│    Algorithm Comparison: Random Forest vs XGBoost          │
│              (Adult Income Dataset)                         │
├────────────────────────────────────────────────────────────┤
│                                                             │
│  METRIC            RANDOM FOREST    XGBOOST    WINNER      │
│  ────────────────────────────────────────────────────────  │
│  Accuracy          85.1%            86.7%      XGBoost ✓   │
│  Precision         72.4%            75.1%      XGBoost ✓   │
│  Recall            58.7%            63.2%      XGBoost ✓   │
│  F1-Score          65.0%            68.6%      XGBoost ✓   │
│  ────────────────────────────────────────────────────────  │
│  Training Time     2.3s             8.1s       RF ✓        │
│  Prediction Time   0.15s            0.42s      RF ✓        │
│  ────────────────────────────────────────────────────────  │
│                                                             │
│  [Bar chart showing metrics side-by-side]                  │
│                                                             │
└────────────────────────────────────────────────────────────┘
```

---

## Detailed Specifications

### Title
- Text: "Algorithm Comparison: Random Forest vs XGBoost"
- Subtitle: "(Adult Income Dataset)"
- Font: Bold, 22pt for title, 16pt for subtitle
- Color: #003366
- Position: Top center, 30px from edge

### Comparison Table

**Table Layout:**
- Header row: Bold, 14pt, dark gray background #E0E0E0
- Data rows: Regular, 13pt, alternating white and light gray #F8F8F8
- Border: 2px solid #666666
- Cell padding: 10px

**Columns:**
1. Metric (left-aligned)
2. Random Forest (center-aligned)
3. XGBoost (center-aligned)
4. Winner (center-aligned)

**Rows:**

| Metric | Random Forest | XGBoost | Winner |
|--------|---------------|---------|--------|
| **Accuracy** | 85.1% | **86.7%** | XGBoost ✓ |
| **Precision** | 72.4% | **75.1%** | XGBoost ✓ |
| **Recall** | 58.7% | **63.2%** | XGBoost ✓ |
| **F1-Score** | 65.0% | **68.6%** | XGBoost ✓ |
| *Separator line* | | | |
| **Training Time** | **2.3s** | 8.1s | RF ✓ |
| **Prediction Time** | **0.15s** | 0.42s | RF ✓ |

**Color Coding:**
- Better value in each row: Bold text, highlighted background #CCFFCC (light green)
- Winner column: Green checkmark ✓ (#00AA00)
- Metric names: Bold

### Bar Chart (Below Table)

**Grouped bar chart showing main metrics:**

**Layout:**
- X-axis: Metrics (Accuracy, Precision, Recall, F1)
- Y-axis: Percentage (0-100%)
- Two bars per metric:
  - Random Forest: Blue #3366CC
  - XGBoost: Green #00AA00
- Bar width: 0.35 (grouped)
- Grid lines: Horizontal, light gray, dashed

**Annotations:**
- Value labels on top of each bar (e.g., "86.7%")
- Font: Bold, 11pt
- Legend in top right corner

**Chart Title:**
"Performance Metrics Comparison"
- Font: Bold, 16pt
- Position: Above chart

### Summary Box (Bottom)

```
KEY TAKEAWAY:
XGBoost achieves 1.6% higher accuracy but takes 3.5x longer to train.
Choose based on your priorities: Speed (RF) vs Accuracy (XGBoost)
```
- Box: 800 x 80px
- Border: 3px solid #FF9900 (orange)
- Background: Light yellow #FFFACD
- Font: Bold, 14pt for "KEY TAKEAWAY", regular 12pt for text
- Icon: Lightbulb emoji or icon

---

## Color Scheme

- Random Forest bars: Blue #3366CC
- XGBoost bars: Green #00AA00
- Better values: Light green highlight #CCFFCC
- Table borders: Dark gray #666666
- Summary box: Orange border #FF9900, yellow background #FFFACD

---

## Creation Code

```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Data
metrics = ['Accuracy', 'Precision', 'Recall', 'F1-Score']
rf_scores = [85.1, 72.4, 58.7, 65.0]
xgb_scores = [86.7, 75.1, 63.2, 68.6]

# Create figure with table and chart
fig = plt.figure(figsize=(12, 8))

# Table
ax_table = plt.subplot(2, 1, 1)
ax_table.axis('tight')
ax_table.axis('off')

# Table data
table_data = [
    ['Metric', 'Random Forest', 'XGBoost', 'Winner'],
    ['Accuracy', '85.1%', '86.7%', 'XGBoost ✓'],
    ['Precision', '72.4%', '75.1%', 'XGBoost ✓'],
    ['Recall', '58.7%', '63.2%', 'XGBoost ✓'],
    ['F1-Score', '65.0%', '68.6%', 'XGBoost ✓'],
    ['─' * 15, '─' * 15, '─' * 15, '─' * 10],
    ['Training Time', '2.3s', '8.1s', 'RF ✓'],
    ['Prediction Time', '0.15s', '0.42s', 'RF ✓']
]

table = ax_table.table(cellText=table_data, cellLoc='center', loc='center',
                       colWidths=[0.3, 0.25, 0.25, 0.2])
table.auto_set_font_size(False)
table.set_fontsize(12)
table.scale(1, 2.5)

# Style header row
for i in range(4):
    table[(0, i)].set_facecolor('#E0E0E0')
    table[(0, i)].set_text_props(weight='bold', fontsize=13)

# Highlight better values
highlight_cells = [(1, 2), (2, 2), (3, 2), (4, 2), (6, 1), (7, 1)]
for row, col in highlight_cells:
    table[(row, col)].set_facecolor('#CCFFCC')
    table[(row, col)].set_text_props(weight='bold')

# Title
fig.text(0.5, 0.95, 'Algorithm Comparison: Random Forest vs XGBoost',
         ha='center', fontsize=22, fontweight='bold', color='#003366')
fig.text(0.5, 0.92, '(Adult Income Dataset)', ha='center',
         fontsize=16, color='#003366')

# Bar chart
ax_chart = plt.subplot(2, 1, 2)

x = np.arange(len(metrics))
width = 0.35

bars1 = ax_chart.bar(x - width/2, rf_scores, width, label='Random Forest',
                     color='#3366CC', edgecolor='black', linewidth=1.5)
bars2 = ax_chart.bar(x + width/2, xgb_scores, width, label='XGBoost',
                     color='#00AA00', edgecolor='black', linewidth=1.5)

# Add value labels
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax_chart.text(bar.get_x() + bar.get_width()/2., height + 1,
                     f'{height:.1f}%', ha='center', va='bottom',
                     fontsize=11, fontweight='bold')

ax_chart.set_xlabel('Metrics', fontsize=14, fontweight='bold')
ax_chart.set_ylabel('Percentage (%)', fontsize=14, fontweight='bold')
ax_chart.set_title('Performance Metrics Comparison', fontsize=16, fontweight='bold')
ax_chart.set_xticks(x)
ax_chart.set_xticklabels(metrics, fontsize=12)
ax_chart.set_ylim(0, 100)
ax_chart.legend(loc='upper right', fontsize=12)
ax_chart.grid(axis='y', alpha=0.3, linestyle='--')
ax_chart.set_axisbelow(True)

# Summary box
summary = ("KEY TAKEAWAY:\n"
           "XGBoost achieves 1.6% higher accuracy but takes 3.5x longer to train.\n"
           "Choose based on your priorities: Speed (RF) vs Accuracy (XGBoost)")
fig.text(0.5, 0.05, summary, ha='center', va='bottom', fontsize=12,
         bbox=dict(boxstyle='round,pad=0.8', facecolor='#FFFACD',
                  edgecolor='#FF9900', linewidth=3))

plt.tight_layout(rect=[0, 0.12, 1, 0.9])
plt.savefig('xgboost_comparison.png', dpi=150, bbox_inches='tight',
            facecolor='white', edgecolor='none')
plt.show()
```

---

## Usage

**When:** Segment 5 (1:50) - Discussing XGBoost performance

**Script:**
> "Let's compare Random Forest and XGBoost on the same dataset. Look at these numbers. XGBoost wins on all accuracy metrics - 86.7% vs 85.1% accuracy. But notice the training time: RF takes 2.3 seconds, XGBoost takes 8.1 seconds. Is 1.6% extra accuracy worth 3.5x longer training time? Depends on your use case!"

---

## Version

XGBoost Comparison Visual v1.0 | January 24, 2026
