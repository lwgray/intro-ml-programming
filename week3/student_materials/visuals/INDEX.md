# Visual Materials Index

**Quick navigation for Week 3 visual materials**

---

## Quick Actions

### Generate All Visuals Now
```bash
python generate_all_visuals.py
```
**Time:** 2-3 minutes | **Output:** 8 PNG files

### Read Quick Start Guide
Start here if you're new: [`QUICK_START.md`](QUICK_START.md)

---

## File Organization

### 📖 Documentation Files

| File | Purpose | Read Time |
|------|---------|-----------|
| [`QUICK_START.md`](QUICK_START.md) | 5-minute guide to generate all visuals | 3 min |
| [`README_VISUAL_CREATION.md`](README_VISUAL_CREATION.md) | Comprehensive creation guide with troubleshooting | 15 min |
| [`TREE_VISUAL_README.md`](../TREE_VISUAL_README.md) | When to use each visual during teaching | 5 min |

### 🎨 Visual Specifications (8 files)

Each spec file contains exact dimensions, layouts, colors, and Python code.

| Priority | Visual | Spec File | Use Case |
|----------|--------|-----------|----------|
| 🔴 HIGH | Decision Tree Example | [`DECISION_TREE_EXAMPLE_SPEC.md`](DECISION_TREE_EXAMPLE_SPEC.md) | Introducing decision trees (0:10) |
| 🟡 MEDIUM | Tree Splitting | [`TREE_SPLITTING_ANIMATION_SPEC.md`](TREE_SPLITTING_ANIMATION_SPEC.md) | Explaining splitting logic (0:18) |
| 🔴 HIGH | Feature Importance | [`FEATURE_IMPORTANCE_PLOT_SPEC.md`](FEATURE_IMPORTANCE_PLOT_SPEC.md) | Interpreting importance (0:26) |
| 🔴 HIGH | Random Forest Ensemble | [`RANDOM_FOREST_ENSEMBLE_SPEC.md`](RANDOM_FOREST_ENSEMBLE_SPEC.md) | "Committee Decision" metaphor (0:42) |
| 🟡 MEDIUM | Bagging Illustration | [`BAGGING_ILLUSTRATION_SPEC.md`](BAGGING_ILLUSTRATION_SPEC.md) | Bagging process steps (0:52) |
| 🔴 HIGH | Boosting Illustration | [`BOOSTING_ILLUSTRATION_SPEC.md`](BOOSTING_ILLUSTRATION_SPEC.md) | "Learning from Mistakes" metaphor (1:32) |
| 🔴 HIGH | XGBoost Comparison | [`XGBOOST_COMPARISON_SPEC.md`](XGBOOST_COMPARISON_SPEC.md) | RF vs XGBoost tradeoffs (1:50) |
| 🔴 HIGH | Overfitting Trees | [`OVERFITTING_TREES_SPEC.md`](OVERFITTING_TREES_SPEC.md) | Overfitting warning (0:32) |

**Priority Legend:**
- 🔴 HIGH = Essential for teaching (create first)
- 🟡 MEDIUM = Nice to have (can describe verbally if needed)

### 🛠️ Generation Tools

| File | Purpose |
|------|---------|
| [`generate_all_visuals.py`](generate_all_visuals.py) | Master script - generates all 8 PNGs automatically |

---

## Teaching Timeline

When to display each visual during live session:

```
0:00 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2:00
     ↓          ↓          ↓          ↓          ↓
   0:10       0:32       0:52       1:32       1:50
   Tree       Overfit    Bagging    Boosting   Comparison
```

**Detailed Timeline:**
- **0:10** - `decision_tree_example.png` (with "20 Questions" metaphor)
- **0:18** - `tree_splitting_animation.png`
- **0:26** - `feature_importance_plot.png`
- **0:32** - `overfitting_trees.png`
- **0:42** - `random_forest_ensemble.png` (with "Committee Decision" metaphor)
- **0:52** - `bagging_illustration.png`
- **1:32** - `boosting_illustration.png` (with "Learning from Mistakes" metaphor)
- **1:50** - `xgboost_comparison.png`

---

## Common Workflows

### Workflow 1: First-Time Setup (10 minutes)

1. Install dependencies:
   ```bash
   pip install matplotlib numpy pandas scikit-learn xgboost
   ```

2. Generate all visuals:
   ```bash
   python generate_all_visuals.py
   ```

3. Verify output:
   ```bash
   ls -lh *.png
   ```
   Should see 8 PNG files

4. Test on projector (optional but recommended)

**Done!** Ready to teach.

### Workflow 2: Regenerate Single Visual (2 minutes)

1. Open the spec file (e.g., `DECISION_TREE_EXAMPLE_SPEC.md`)
2. Find "Creation Code" section
3. Copy code to Jupyter notebook or save as `.py` file
4. Run to generate that specific PNG

### Workflow 3: Customize Visual (5 minutes)

1. Open `generate_all_visuals.py`
2. Find the section for your visual (search for filename)
3. Modify code (colors, sizes, content)
4. Re-run script

**Example:** Change tree depth:
```python
# Find:
tree = DecisionTreeClassifier(max_depth=3, random_state=42)

# Change to:
tree = DecisionTreeClassifier(max_depth=5, random_state=42)
```

---

## Troubleshooting Quick Reference

### Error: "No module named 'matplotlib'"
```bash
pip install matplotlib
```

### Error: "graphviz not found"
**macOS:**
```bash
brew install graphviz && pip install graphviz
```

**Ubuntu:**
```bash
sudo apt-get install graphviz && pip install graphviz
```

### Visuals look pixelated
Increase DPI in code:
```python
plt.savefig('file.png', dpi=300)  # Instead of dpi=150
```

### Script fails partway through
Run individual sections - each visual is independent. Comment out failing sections and generate others.

---

## Integration with Other Materials

### Teaching Metaphors
See [`../tree_teaching_metaphor.md`](../tree_teaching_metaphor.md) for:
- "20 Questions Game" (Decision Trees)
- "Committee Decision" (Random Forests)
- "Learning from Mistakes" (XGBoost)

### PowerPoint Slides
Generate slides with:
```bash
cd ..
python create_slides.py
```

### Student Reference
Point students to [`../../appendices/Appendix_C_Tree_Ensemble_Guide.md`](../../appendices/Appendix_C_Tree_Ensemble_Guide.md)

---

## Visual Quality Standards

Before using in class, verify:
- ✅ Text readable from 10 feet away
- ✅ Colors distinguishable (colorblind-friendly)
- ✅ File format is PNG (not JPEG)
- ✅ File size < 5MB per image
- ✅ Resolution at least 150 DPI

---

## Expected Output Files

After running `generate_all_visuals.py`, you should have:

```
visuals/
├── decision_tree_example.png      (~500KB)
├── tree_splitting_animation.png   (~300KB)
├── feature_importance_plot.png    (~200KB)
├── random_forest_ensemble.png     (~400KB)
├── bagging_illustration.png       (~350KB)
├── boosting_illustration.png      (~400KB)
├── xgboost_comparison.png         (~250KB)
└── overfitting_trees.png          (~600KB)
```

**Total:** ~3MB of visual materials

---

## Alternative Creation Methods

### Option 1: Python (Automated) ⭐ Recommended
- Use `generate_all_visuals.py`
- Pros: Fast, consistent, easy to modify
- Cons: Requires Python environment

### Option 2: PowerPoint (Manual)
- Follow spec file layouts
- Pros: No coding, full control
- Cons: Time-consuming

### Option 3: Diagramming Tools
- Use draw.io, Lucidchart, or Canva
- Pros: Professional polish
- Cons: Requires account/software

### Option 4: Request Pre-Generated
- Ask course development team
- Pros: Zero effort
- Cons: Can't customize

---

## Need Help?

1. **Quick questions:** Check [`QUICK_START.md`](QUICK_START.md)
2. **Technical issues:** See [`README_VISUAL_CREATION.md`](README_VISUAL_CREATION.md) troubleshooting section
3. **Teaching integration:** Read [`../TREE_VISUAL_README.md`](../TREE_VISUAL_README.md)
4. **Content questions:** Reference [`../../appendices/Appendix_C_Tree_Ensemble_Guide.md`](../../appendices/Appendix_C_Tree_Ensemble_Guide.md)

---

## Version

Visual Materials Index v1.0 | January 24, 2026

**Ready to generate visuals?**

```bash
python generate_all_visuals.py
```

**Time:** 2-3 minutes | **Output:** 8 teaching-ready PNG files
