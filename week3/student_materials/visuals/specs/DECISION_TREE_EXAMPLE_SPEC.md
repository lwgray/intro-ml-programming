# Visual Specification: Decision Tree Example

## Purpose

Create a clear decision tree diagram showing binary splits on the Iris dataset with max_depth=3. This visual will be used when introducing the "20 Questions Game" metaphor.

---

## Specifications

**Filename:** `decision_tree_example.png`

**Dimensions:** 1920 x 1080 pixels (16:9 aspect ratio)

**Format:** PNG with transparent or white background

**Resolution:** 300 DPI (for print) or 72 DPI (screen only)

---

## Visual Elements

### Tree Structure

```
                        Root Node
                   [petal_width <= 0.8]
                   samples = 150
                   value = [50, 50, 50]
                   class = setosa
                          |
        ┌─────────────────┴─────────────────┐
       YES                                  NO
        |                                    |
        ▼                                    ▼
   [Leaf Node]                       [petal_width <= 1.75]
   class = setosa                    samples = 100
   samples = 50                      value = [0, 50, 50]
   value = [50, 0, 0]                class = versicolor
   (PURE)                                   |
                        ┌───────────────────┴───────────────┐
                       YES                                 NO
                        |                                   |
                        ▼                                   ▼
                 [petal_length <= 4.95]              [petal_length <= 4.85]
                 samples = 54                        samples = 46
                 value = [0, 49, 5]                  value = [0, 1, 45]
                 class = versicolor                  class = virginica
                        |                                   |
            ┌───────────┴──────────┐           ┌───────────┴──────────┐
           YES                    NO          YES                    NO
            |                      |           |                      |
            ▼                      ▼           ▼                      ▼
     [Leaf: versicolor]    [Leaf: virginica]  [Leaf: versicolor] [Leaf: virginica]
     samples = 48          samples = 6        samples = 3         samples = 43
     value = [0, 47, 1]    value = [0, 2, 4]  value = [0, 1, 2]   value = [0, 0, 43]
```

### Node Design

**Internal Nodes (Decision Nodes):**
- Shape: Rounded rectangle
- Border: 3px solid, color #003366 (dark blue)
- Background: Light blue gradient (#CCE5FF to #E6F2FF)
- Text layout:
  ```
  [Feature <= Threshold]
  samples = N
  value = [class0, class1, class2]
  class = majority_class
  ```
- Font: Sans-serif, 14pt for question, 12pt for details

**Leaf Nodes (Predictions):**
- Shape: Ellipse/oval
- Border: 3px solid, color based on class:
  - Setosa: #00AA00 (green)
  - Versicolor: #FF6600 (orange)
  - Virginica: #9933FF (purple)
- Background: Same color as border, 30% opacity
- Text: Bold class name, 16pt, centered
- Additional info (samples, value) in smaller font below

### Edges (Branches)

- Style: Solid arrow lines
- Width: 2px
- Color: #666666 (medium gray)
- Labels:
  - "Yes" on left branches (light green background #CCFFCC)
  - "No" on right branches (light red background #FFCCCC)
  - Font: Bold, 12pt

### Color Scheme

**Primary Colors:**
- Decision nodes: Blue (#003366 border, #CCE5FF fill)
- Setosa leaves: Green (#00AA00)
- Versicolor leaves: Orange (#FF6600)
- Virginica leaves: Purple (#9933FF)

**Secondary Colors:**
- Yes labels: Light green (#CCFFCC background)
- No labels: Light red (#FFCCCC background)
- Edges: Gray (#666666)

### Labels and Annotations

**Title (Top of Image):**
- Text: "Decision Tree Example: Iris Classification (max_depth=3)"
- Font: Bold, 24pt, centered
- Color: #003366
- Position: 50px from top

**Legend (Bottom Right):**
```
Class Colors:
● Setosa (green)
● Versicolor (orange)
● Virginica (purple)

Node Information:
Feature <= Threshold → Split condition
samples = N → Number of training points
value = [a, b, c] → Count per class
class = X → Majority class
```
- Font: Regular, 10pt
- Background: White box with light gray border

---

## Creation Methods

### Option 1: Use sklearn's plot_tree (Recommended)

```python
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Load data
iris = load_iris()
X, y = iris.data, iris.target

# Train tree
tree = DecisionTreeClassifier(max_depth=3, random_state=42)
tree.fit(X, y)

# Plot
plt.figure(figsize=(20, 10))
plot_tree(
    tree,
    feature_names=iris.feature_names,
    class_names=iris.target_names,
    filled=True,              # Color by majority class
    rounded=True,             # Rounded boxes
    fontsize=12,
    proportion=False          # Show sample counts
)
plt.title("Decision Tree Example: Iris Classification (max_depth=3)",
          fontsize=24, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('decision_tree_example.png', dpi=300, bbox_inches='tight',
            facecolor='white', edgecolor='none')
plt.show()
```

### Option 2: Use graphviz

```python
from sklearn.tree import export_graphviz
import graphviz

# Train tree (same as above)

# Export to graphviz
dot_data = export_graphviz(
    tree,
    out_file=None,
    feature_names=iris.feature_names,
    class_names=iris.target_names,
    filled=True,
    rounded=True,
    special_characters=True
)

# Render
graph = graphviz.Source(dot_data)
graph.format = 'png'
graph.render('decision_tree_example', cleanup=True)
```

### Option 3: Manual Design (PowerPoint/Google Slides)

1. Create slide with dimensions 1920 x 1080
2. Use SmartArt "Hierarchy" diagram
3. Add rounded rectangles for nodes
4. Add arrows for edges
5. Fill in text manually following the layout above
6. Color code by class (green/orange/purple)
7. Export as PNG

---

## Quality Checklist

Before finalizing the image, verify:

- [ ] All text is legible (minimum 12pt font)
- [ ] Node borders are clearly visible (3px minimum)
- [ ] Colors are distinct (test with colorblind simulator)
- [ ] Title is prominent and centered
- [ ] Legend explains all symbols and colors
- [ ] No text overlap or crowding
- [ ] Image exports at correct dimensions (1920x1080)
- [ ] Background is white or transparent (not gray)
- [ ] File size is reasonable (<5MB for PNG)

---

## Usage During Teaching

**When to Show:**
- Segment 2 (0:20): During "20 Questions Game" metaphor introduction
- Segment 2 (0:40): During tree visualization walkthrough
- Segment 6 (2:05): When training decision tree on Adult Income (as reference)

**How to Use:**
1. Display on screen while drawing on whiteboard
2. Point to root node: "This is where all data starts - 150 iris flowers"
3. Trace one path: "Follow this path from top to bottom..."
4. Explain each node: "At each box, we ask a yes/no question"
5. Point to leaves: "Final predictions at the bottom"

**Teaching Script:**
> "This is a real decision tree trained on the Iris dataset. See how it starts at the top with all 150 flowers, then asks 'Is petal width <= 0.8?' If yes, go left - that's all setosa flowers (perfectly separated!). If no, go right and ask more questions. By depth 3, we've classified all flowers into the three species."

---

## Alternative Versions

Consider creating these variations:

**Version 1: Simplified (for introduction)**
- Only show depth 2 (fewer nodes, clearer)
- Use larger fonts (18pt for questions)
- Remove value arrays (just show class names)

**Version 2: Annotated (for detailed explanation)**
- Add arrows pointing to specific nodes with explanations
- Highlight one path from root to leaf in bold
- Add "Information Gain" values on splits

**Version 3: Comparison (overfitting example)**
- Side-by-side: max_depth=3 vs max_depth=None
- Show how deep tree creates many tiny leaves
- Label: "Good generalization" vs "Overfitting"

---

## File Naming Convention

- Primary version: `decision_tree_example.png`
- Simplified version: `decision_tree_simple.png`
- Annotated version: `decision_tree_annotated.png`
- Comparison version: `decision_tree_overfitting_comparison.png`

---

## Dependencies

**Python Libraries (if generating programmatically):**
```bash
pip install scikit-learn matplotlib graphviz
# For graphviz, also install system package:
# macOS: brew install graphviz
# Ubuntu: sudo apt-get install graphviz
# Windows: Download from graphviz.org
```

**Alternative Software:**
- PowerPoint (manual creation)
- Google Slides (manual creation)
- Draw.io (free diagram tool)
- Lucidchart (professional diagrams)

---

## Testing

**Test the visual by asking:**
1. Can you read all text from 10 feet away? (legibility test)
2. Can you trace a path from root to leaf? (clarity test)
3. Do colors differentiate classes? (color test)
4. Is the decision logic clear? (comprehension test)

**Student comprehension check:**
After showing the visual, ask:
- "What question does the root node ask?"
- "If petal width is 0.5, which path do we take?"
- "What does the tree predict for the left-most leaf?"

If students can't answer, the visual needs improvement.

---

## Version

Decision Tree Example Visual Specification v1.0 | January 24, 2026

**Ready to create the visual!** Use Option 1 (sklearn plot_tree) for fastest results.
