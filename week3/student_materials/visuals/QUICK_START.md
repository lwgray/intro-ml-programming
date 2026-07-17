# Quick Start: Generate All Visuals in 5 Minutes

This guide gets you from zero to all 8 visual PNG files in about 5 minutes.

---

## Option 1: Automated Generation (Recommended)

### Step 1: Install Dependencies

```bash
pip install matplotlib numpy pandas scikit-learn xgboost
```

### Step 2: Run Generation Script

```bash
cd week3/instructor_materials/visuals
python generate_all_visuals.py
```

### Step 3: Verify Output

You should see:
```
[1/8] Creating decision_tree_example.png...
   ✓ decision_tree_example.png created
[2/8] Creating tree_splitting_animation.png...
   ✓ tree_splitting_animation.png created
...
[8/8] Creating overfitting_trees.png...
   ✓ overfitting_trees.png created

All visuals are ready for use in teaching!
```

**Done!** All 8 PNG files are in the current directory.

---

## Option 2: Manual Generation (Pick and Choose)

If you only need specific visuals, copy the code from the spec files:

### Example: Create Decision Tree Visual Only

1. Open `DECISION_TREE_EXAMPLE_SPEC.md`
2. Find the "Creation Code" section
3. Copy the Python code
4. Run it in Jupyter notebook or save as `create_tree.py` and run

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

**Result:** `decision_tree_example.png` created

---

## Option 3: PowerPoint Alternative (No Coding)

If you can't run Python, create visuals manually in PowerPoint:

1. Open PowerPoint
2. Set slide size to match spec (e.g., 1920x1080)
3. Read specification file (e.g., `RANDOM_FOREST_ENSEMBLE_SPEC.md`)
4. Recreate visual using shapes and text boxes
5. Export as PNG

**Best for:** Random Forest ensemble, bagging illustration

---

## Troubleshooting

### Error: "No module named 'matplotlib'"

**Fix:**
```bash
pip install matplotlib
```

### Error: "graphviz not found"

**Fix (macOS):**
```bash
brew install graphviz
pip install graphviz
```

**Fix (Ubuntu):**
```bash
sudo apt-get install graphviz
pip install graphviz
```

**Fix (Windows):**
1. Download from https://graphviz.org/download/
2. Install to `C:\Program Files\Graphviz`
3. Add to PATH: `C:\Program Files\Graphviz\bin`
4. Run: `pip install graphviz`

### Visuals Look Pixelated

Increase DPI in the code:
```python
plt.savefig('image.png', dpi=300)  # Higher quality
```

---

## File Inventory

After generation, you should have these 8 files:

| # | Filename | Size | When to Use |
|---|----------|------|-------------|
| 1 | `decision_tree_example.png` | ~500KB | 0:10 - Introducing decision trees |
| 2 | `tree_splitting_animation.png` | ~300KB | 0:18 - Explaining splitting logic |
| 3 | `feature_importance_plot.png` | ~200KB | 0:26 - Feature importance discussion |
| 4 | `random_forest_ensemble.png` | ~400KB | 0:42 - Random Forest introduction |
| 5 | `bagging_illustration.png` | ~350KB | 0:52 - Explaining bagging process |
| 6 | `boosting_illustration.png` | ~400KB | 1:32 - XGBoost sequential learning |
| 7 | `xgboost_comparison.png` | ~250KB | 1:50 - RF vs XGBoost tradeoffs |
| 8 | `overfitting_trees.png` | ~600KB | 0:32 - Overfitting warning |

---

## Integration with Slides

### Method 1: Insert into PowerPoint

1. Run `python create_slides.py` (generates base slides)
2. Open `Week3_Live_Session_Slides.pptx`
3. Insert PNG files at appropriate slides
4. Resize to fit

### Method 2: Use Directly (Projector)

1. Generate all PNGs
2. During teaching, open PNGs directly using Preview/Photos app
3. Switch between them at the right times

### Method 3: Embedded in Jupyter

```python
from IPython.display import Image, display
display(Image('decision_tree_example.png'))
```

---

## Quality Checklist

Before using in class, verify:

- [ ] All 8 files generated without errors
- [ ] Files are PNG format (not JPEG)
- [ ] Text is readable when projected
- [ ] Colors match specifications (can distinguish classes)
- [ ] File sizes are reasonable (< 5MB each)
- [ ] No distortion or pixelation

---

## Time Estimates

| Task | Time Required |
|------|---------------|
| Install dependencies (first time) | 2-5 min |
| Run automated script | 2-3 min |
| Manual verification | 1 min |
| **Total** | **5-10 min** |

---

## Support

**Problem:** Script fails with errors

**Solution:** Check individual spec files and run code snippets one by one to isolate the issue

**Problem:** Don't have Python environment

**Solution:** Use PowerPoint method or request pre-generated PNG files from course development team

**Problem:** Visuals don't match specifications exactly

**Solution:** That's okay! Specifications are guidelines. As long as the key concepts are clear, minor variations are acceptable.

---

## Next Steps

After generating visuals:

1. **Test on projector** - Verify readability from back of room
2. **Practice integration** - Know when to show each visual during teaching
3. **Prepare backups** - Have whiteboard diagrams ready if tech fails
4. **Review metaphors** - Read `tree_teaching_metaphor.md` to align visuals with verbal explanations

---

## Advanced: Customization

Want to modify visuals?

1. Open `generate_all_visuals.py`
2. Find the section for the visual you want to change
3. Modify colors, sizes, or content
4. Re-run the script

**Example:** Change Random Forest from 5 trees to 3 trees:
```python
# Find this line:
for i in range(5):  # Original: 5 trees

# Change to:
for i in range(3):  # Modified: 3 trees
```

---

## Version

Quick Start Guide v1.0 | Week 3 Visual Materials | January 24, 2026

**Ready to generate? Run this now:**

```bash
python generate_all_visuals.py
```
