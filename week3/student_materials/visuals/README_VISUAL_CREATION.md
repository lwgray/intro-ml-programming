# Visual Creation Guide for Week 3

## Purpose

This document provides instructions for creating all visual materials for Week 3 (Trees and Ensembles). Each visual has a detailed specification file - this README tells you how to actually create them.

---

## Quick Start

**Have all PNG files already?** You're done! Use them directly during teaching.

**Need to create visuals?** Follow the methods below.

---

## Visual Files Inventory

| # | Filename | Specification File | Priority | Complexity |
|---|----------|-------------------|----------|------------|
| 1 | `decision_tree_example.png` | `DECISION_TREE_EXAMPLE_SPEC.md` | HIGH | Easy |
| 2 | `tree_splitting_animation.png` | `TREE_SPLITTING_ANIMATION_SPEC.md` | MEDIUM | Medium |
| 3 | `feature_importance_plot.png` | `FEATURE_IMPORTANCE_PLOT_SPEC.md` | HIGH | Easy |
| 4 | `random_forest_ensemble.png` | `RANDOM_FOREST_ENSEMBLE_SPEC.md` | HIGH | Medium |
| 5 | `bagging_illustration.png` | `BAGGING_ILLUSTRATION_SPEC.md` | MEDIUM | Medium |
| 6 | `boosting_illustration.png` | `BOOSTING_ILLUSTRATION_SPEC.md` | HIGH | Medium |
| 7 | `xgboost_comparison.png` | `XGBOOST_COMPARISON_SPEC.md` | HIGH | Easy |
| 8 | `overfitting_trees.png` | `OVERFITTING_TREES_SPEC.md` | HIGH | Hard |

**Priority:**
- HIGH = Essential for teaching (create these first)
- MEDIUM = Nice to have (can describe verbally if needed)

**Complexity:**
- Easy = Run provided code, generates immediately
- Medium = Requires some customization
- Hard = May need manual drawing or advanced coding

---

## Creation Methods

### Method 1: Python + Matplotlib (Recommended)

**Pros:**
- Fully automated
- Consistent quality
- Easy to modify
- Code provided in spec files

**Cons:**
- Requires Python environment
- Learning curve if not familiar with matplotlib

**Requirements:**
```bash
pip install matplotlib numpy pandas scikit-learn xgboost
# For tree visualization:
pip install graphviz
# System graphviz (macOS):
brew install graphviz
# Ubuntu:
sudo apt-get install graphviz
```

**Steps:**
1. Read the specification file (e.g., `DECISION_TREE_EXAMPLE_SPEC.md`)
2. Find the "Creation Code" section
3. Copy the Python code
4. Run in Jupyter notebook or Python script
5. PNG file generated automatically

**Example:**
```python
# From DECISION_TREE_EXAMPLE_SPEC.md
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

iris = load_iris()
X, y = iris.data, iris.target

tree = DecisionTreeClassifier(max_depth=3, random_state=42)
tree.fit(X, y)

plt.figure(figsize=(20, 10))
plot_tree(tree, feature_names=iris.feature_names,
          class_names=iris.target_names, filled=True, rounded=True)
plt.savefig('decision_tree_example.png', dpi=300, bbox_inches='tight')
plt.show()
```

---

### Method 2: PowerPoint or Google Slides (Manual)

**Pros:**
- No coding required
- Full creative control
- Easy to adjust on the fly

**Cons:**
- Time-consuming
- Harder to maintain consistency
- Manual work for each visual

**Steps:**
1. Open PowerPoint or Google Slides
2. Set slide size to match specifications (e.g., 1920x1080)
3. Read specification file for exact layout
4. Use shapes, text boxes, and SmartArt to create visual
5. Export as PNG

**Best for:**
- Simple diagrams (Random Forest ensemble, bagging illustration)
- Quick prototypes
- Last-minute changes

**Tips:**
- Use snap-to-grid for alignment
- Copy color codes exactly (#003366 etc.)
- Export at high DPI (300 if available)

---

### Method 3: Dedicated Diagramming Tools

**Options:**
- **draw.io** (free, web-based) - Excellent for flowcharts and diagrams
- **Lucidchart** (paid, professional) - Best for complex diagrams
- **Canva** (free/paid) - Good for polished graphics
- **Figma** (free/paid) - Modern design tool

**Best for:**
- Ensemble diagrams (Random Forest, bagging, boosting)
- Decision tree simple representations
- Flowcharts

**Steps:**
1. Choose tool (draw.io recommended for free option)
2. Import template or start from scratch
3. Follow specification file for layout and colors
4. Export as PNG at specified dimensions

---

### Method 4: Generate from Actual Model (Live Data)

**Use for:**
- Feature importance plots (from trained models)
- Decision tree visualizations (from sklearn)
- Performance comparisons (from actual metrics)

**Steps:**
1. Train models on Adult Income dataset (or use provided data)
2. Extract relevant information (feature importance, metrics)
3. Use matplotlib to generate visual
4. Save as PNG

**Example (Feature Importance):**
```python
# After training Random Forest
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

importances = rf.feature_importances_
# Then use code from FEATURE_IMPORTANCE_PLOT_SPEC.md
```

---

## Step-by-Step Workflows

### Workflow A: Create All Visuals in One Session (Python)

**Time Required:** 2-3 hours

1. **Setup environment:**
   ```bash
   pip install matplotlib numpy pandas scikit-learn xgboost graphviz
   ```

2. **Create working directory:**
   ```bash
   mkdir week3_visuals
   cd week3_visuals
   ```

3. **For each visual:**
   - Open specification file
   - Copy "Creation Code" section
   - Save as `create_[visual_name].py`
   - Run: `python create_[visual_name].py`
   - Verify PNG created correctly

4. **Quality check:**
   - Open each PNG
   - Verify dimensions (should match spec)
   - Check text legibility
   - Confirm colors match spec

5. **Move to visuals directory:**
   ```bash
   mv *.png ../instructor_materials/visuals/
   ```

---

### Workflow B: Create Minimal Set (High Priority Only)

**Time Required:** 1 hour

**High priority visuals:**
1. decision_tree_example.png (Easy)
2. feature_importance_plot.png (Easy)
3. random_forest_ensemble.png (Medium)
4. boosting_illustration.png (Medium)
5. xgboost_comparison.png (Easy)
6. overfitting_trees.png (Hard)

**For others:** Draw on whiteboard during class or describe verbally.

---

### Workflow C: Use Pre-Made Templates

**If someone already created visuals:**
1. Download PNG files
2. Place in `instructor_materials/visuals/`
3. Verify they match specifications
4. Customize if needed (edit in PowerPoint or image editor)

---

## Customization Guide

### Changing Colors

All specification files use consistent color scheme:
- Primary: #003366 (dark blue)
- Decision trees: #00AA00 (green)
- Errors/warnings: #CC0000 (red)
- Highlights: #FFFACD (light yellow)

**To change:** Edit hex codes in Python code or manually in graphics software.

### Changing Dimensions

**For Python-generated visuals:**
```python
plt.figure(figsize=(width_inches, height_inches))
# e.g., figsize=(19.2, 10.8) for 1920x1080 at 100 DPI
```

**For manual creation:**
Set slide/canvas size to match pixels specified in spec file.

### Changing Data/Examples

**For real data visuals (feature importance, tree visualization):**
- Train on your own dataset
- Extract actual values
- Generate visual with real numbers

**For illustrative diagrams:**
- Edit example arrays in code
- Update labels manually in graphics software

---

## Quality Standards

Before finalizing any visual, check:

### Legibility
- [ ] Text readable from 10 feet away (minimum 12pt font)
- [ ] No overlapping labels
- [ ] Sufficient contrast (text on background)

### Accuracy
- [ ] Matches specification file
- [ ] Correct dimensions
- [ ] Color codes match
- [ ] All labels present

### Consistency
- [ ] Font family consistent across visuals
- [ ] Color scheme consistent
- [ ] Style (borders, shadows) consistent

### Technical
- [ ] File format: PNG
- [ ] File size: < 5MB per image
- [ ] Resolution: At least 72 DPI (150 DPI preferred)
- [ ] Background: White or transparent (not gray)

---

## Troubleshooting

### Issue: Python code doesn't run

**Error:** `ImportError: No module named 'matplotlib'`

**Solution:**
```bash
pip install matplotlib
# Or for Anaconda:
conda install matplotlib
```

---

### Issue: Tree visualization blank or not showing

**Error:** `graphviz not found`

**Solution:**
```bash
# macOS:
brew install graphviz
pip install graphviz

# Ubuntu:
sudo apt-get install graphviz
pip install graphviz

# Windows:
# Download from graphviz.org and install
# Then: pip install graphviz
```

**Alternative:** Use `tree.export_text()` instead of plot_tree()

---

### Issue: Generated image looks pixelated

**Solution:**
Increase DPI when saving:
```python
plt.savefig('image.png', dpi=300)  # Higher quality
# Instead of:
plt.savefig('image.png', dpi=72)   # Lower quality
```

---

### Issue: Colors look different than specification

**Solution:**
1. Verify hex codes match exactly: `#003366` not `#003365`
2. Check monitor color calibration
3. Save as PNG, not JPEG (JPEG compresses colors)
4. Use colorblind simulator to test accessibility

---

### Issue: Can't install graphviz on Windows

**Solution:**
1. Download installer from https://graphviz.org/download/
2. Install to `C:\Program Files\Graphviz`
3. Add to PATH: `C:\Program Files\Graphviz\bin`
4. Restart terminal
5. `pip install graphviz`

**Alternative:** Use sklearn's `plot_tree()` instead of graphviz

---

## Testing Visuals

### Test 1: Projection Test

1. Open visual on computer
2. Project onto screen (or simulate with small preview window)
3. View from back of room
4. Can you read all text? → Pass/Fail

### Test 2: Colorblind Test

1. Use colorblind simulator (online tools available)
2. View with deuteranopia filter (red-green colorblindness)
3. Can you still distinguish classes? → Pass/Fail

**Tools:**
- Coblis (online colorblind simulator)
- Chromatic Vision Simulator (mobile app)

### Test 3: Student Comprehension Test

1. Show visual to colleague (not familiar with content)
2. Ask: "What is this showing?"
3. If they get the main idea, it's clear → Pass

---

## Backup Plans

### If Visual Creation Fails

**Option A: Draw on Whiteboard**
- Most visuals can be simplified for whiteboard
- Decision trees: Draw manually with tree structure
- Ensembles: Sketch boxes and arrows
- Feature importance: Simple bar chart

**Option B: Describe Verbally with Metaphors**
- Random Forest → "Committee Decision" metaphor
- XGBoost → "Learning from Mistakes" metaphor
- Don't need visual if metaphor is strong

**Option C: Use Student Materials**
- Provide specification files to students
- Students can reference detailed text descriptions
- Visuals enhance but don't replace teaching

---

## Advanced: Automating Visual Generation

### Create Master Script

```python
# create_all_visuals.py
import subprocess
import os

visual_scripts = [
    'create_decision_tree.py',
    'create_feature_importance.py',
    'create_rf_ensemble.py',
    'create_boosting.py',
    'create_comparison.py',
    'create_overfitting.py'
]

for script in visual_scripts:
    print(f"Creating {script}...")
    subprocess.run(['python', script])
    print(f"✓ {script} complete")

print("\n✅ All visuals created!")
```

**Run once:**
```bash
python create_all_visuals.py
```

All 8 visuals generated automatically.

---

## Version Control

**Track changes to visuals:**

```bash
# In git repository
git add instructor_materials/visuals/*.png
git commit -m "Add Week 3 visual materials"

# Update a visual
python create_decision_tree.py  # Regenerate
git diff instructor_materials/visuals/decision_tree_example.png
git commit -m "Update decision tree visual with darker borders"
```

---

## Distribution

### For Instructors

**Include in instructor package:**
```
instructor_materials/
├── visuals/
│   ├── decision_tree_example.png
│   ├── feature_importance_plot.png
│   ├── random_forest_ensemble.png
│   ├── boosting_illustration.png
│   ├── xgboost_comparison.png
│   ├── overfitting_trees.png
│   ├── tree_splitting_animation.png
│   └── bagging_illustration.png
├── Week3_Live_Session_Slides.pptx
└── *_SPEC.md files
```

### For Students

**Provide selective visuals:**
- Feature importance example (for reference)
- Algorithm comparison table (for study)
- Do NOT provide all teaching visuals (keeps sessions engaging)

---

## Time Estimates

| Visual | Method | Time Required |
|--------|--------|---------------|
| Decision Tree Example | Python | 5 min |
| Tree Splitting | Python | 15 min |
| Feature Importance | Python | 5 min |
| Random Forest Ensemble | PowerPoint | 30 min |
| Bagging Illustration | Python | 20 min |
| Boosting Illustration | Python | 25 min |
| XGBoost Comparison | Python | 10 min |
| Overfitting Trees | Python | 20 min |

**Total (all Python):** ~2 hours
**Total (mixed approach):** ~2.5 hours

---

## Final Checklist

Before teaching session:

- [ ] All 8 PNG files created
- [ ] Files placed in `instructor_materials/visuals/`
- [ ] Tested on projector
- [ ] Verified legibility from back of room
- [ ] Checked colorblind accessibility
- [ ] Backed up files (cloud storage)
- [ ] Ready to use in PowerPoint slides (if applicable)
- [ ] Printed versions ready (optional backup)

---

## Support

**If you encounter issues:**

1. Check specification file for exact requirements
2. Review troubleshooting section above
3. Try alternative creation method (Python → PowerPoint or vice versa)
4. Simplify: Use whiteboard or verbal description
5. Contact course development team

**Remember:** Visuals enhance teaching but aren't mandatory. Strong metaphors and clear explanations work without visuals if needed!

---

## Version

Visual Creation Guide v1.0 | Week 3 | January 24, 2026

**Good luck creating your visuals! 🎨**
