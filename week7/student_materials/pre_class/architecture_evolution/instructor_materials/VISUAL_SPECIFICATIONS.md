# Visual Specifications: Neural Network Architecture Evolution

**Purpose:** Exact specifications for creating all diagrams, animations, and visuals for teaching/recording

**Module:** Week 7 Pre-Class - Architecture Evolution
**Created:** 2026-02-22

---

## Table of Contents

1. [Dense Networks Visuals (1-3)](#dense-networks-visuals)
2. [CNN Visuals (4-6)](#cnn-visuals)
3. [ResNet Visuals (7-8)](#resnet-visuals)
4. [RNN/LSTM Visuals (9-10)](#rnnlstm-visuals)
5. [Transformer Visuals (11-12)](#transformer-visuals)
6. [Master Diagrams (13-14)](#master-diagrams)
7. [Tool Recommendations](#tool-recommendations)
8. [Color Palette](#color-palette)
9. [Export Settings](#export-settings)

---

## Dense Networks Visuals

### Visual 1: Perceptron Diagram

**File Name:** `perceptron_diagram.png`

**Dimensions:** 1200×800px (3:2 aspect ratio, landscape)

**Style:** Clean technical diagram, white background

**Elements:**

```
[Input Layer]    [Neuron]        [Activation]    [Output]

  x₁ ────┐
         │
  x₂ ────┼──→ [  Σ  ] ──→ [sign()] ──→  y
         │
  x₃ ────┘

  (bias b)
```

**Detailed Spec:**

**Input Nodes (3 circles):**
- Position: Left side, vertically aligned
- Diameter: 60px
- Color: Light blue (#ADD8E6)
- Border: 3px solid dark gray (#333)
- Labels inside circles: "x₁", "x₂", "x₃" (16pt font)
- Spacing: 100px between centers

**Weights (arrows):**
- From each input to neuron
- Arrow style: Solid line, 3px width, dark gray (#333)
- Arrow head: 10px triangle
- Labels above arrows: "w₁", "w₂", "w₃" (14pt italic font)

**Bias:**
- Position: Below x₃, dashed line to neuron
- Label: "b" (14pt italic font)
- Dashed line: 2px width, gray (#666)

**Neuron (summation):**
- Position: Center of canvas
- Shape: Circle, diameter 100px
- Color: Orange (#FFA500)
- Border: 4px solid dark gray (#333)
- Symbol inside: "Σ" (summation, 36pt font, white)

**Activation Function:**
- Position: Right of neuron
- Shape: Rounded rectangle, 120px × 80px
- Color: Light gray (#E0E0E0)
- Border: 3px solid dark gray (#333)
- Label: "sign(·)" (18pt font)

**Output:**
- Position: Far right
- Shape: Circle, diameter 60px
- Color: Light green (#90EE90)
- Border: 3px solid dark gray (#333)
- Label: "y" (16pt font)

**Formula (bottom of diagram):**
```
y = sign(Σ wᵢxᵢ + b) = sign(w₁x₁ + w₂x₂ + w₃x₃ + b)
```
- Font: 16pt, centered
- Position: 50px from bottom

**Annotations:**
- Top-left corner: "Single-Layer Perceptron (1958)" (14pt, gray)
- Below formula: "Linear classifier - cannot learn XOR" (12pt italic, red)

---

### Visual 2: Multi-Layer Perceptron (MLP)

**File Name:** `mlp_diagram.png`

**Dimensions:** 1400×900px (landscape)

**Layers:**
- **Input:** 4 nodes
- **Hidden Layer 1:** 5 nodes
- **Hidden Layer 2:** 4 nodes
- **Output:** 3 nodes

**Detailed Spec:**

**Input Layer (4 circles):**
- Position: x=100px, y evenly spaced (150px apart)
- Diameter: 50px each
- Color: Light blue (#ADD8E6)
- Labels: "x₁", "x₂", "x₃", "x₄"

**Hidden Layer 1 (5 circles):**
- Position: x=400px, y evenly spaced
- Diameter: 50px each
- Color: Light orange (#FFD699)
- No labels (just nodes)

**Hidden Layer 2 (4 circles):**
- Position: x=700px, y evenly spaced
- Diameter: 50px each
- Color: Light orange (#FFD699)
- No labels

**Output Layer (3 circles):**
- Position: x=1000px, y evenly spaced
- Diameter: 50px each
- Color: Light green (#90EE90)
- Labels: "y₁", "y₂", "y₃"

**Connections:**
- **All-to-all (fully connected)** between adjacent layers
- Line style: Thin gray (#999), 1.5px width
- Example: Every input node connects to every hidden 1 node (4×5 = 20 connections)
- Use slight transparency (0.6 alpha) to avoid clutter

**Activation Function Labels:**
- Below Hidden Layer 1: "ReLU" in red box (14pt)
- Below Hidden Layer 2: "ReLU" in red box (14pt)
- Below Output Layer: "Softmax" in green box (14pt)

**Layer Labels (above layers):**
- Above Input: "Input Layer" (12pt)
- Above Hidden 1: "Hidden Layer 1" (12pt)
- Above Hidden 2: "Hidden Layer 2" (12pt)
- Above Output: "Output Layer" (12pt)

**Annotations:**
- Top center: "Multi-Layer Perceptron (Deep Neural Network)" (16pt bold)
- Bottom center: "Universal Approximator - Can learn XOR and non-linear patterns" (14pt italic, green)

---

### Visual 3: XOR Decision Boundary (Side-by-Side)

**File Name:** `xor_decision_boundary.png`

**Dimensions:** 1000×500px (2 plots side-by-side)

**Layout:** Two plots, each 450×450px, separated by 100px

**Plot 1: Perceptron Fails (Left)**

**Axes:**
- X-axis: x₁ (range 0 to 1)
- Y-axis: x₂ (range 0 to 1)
- Grid: Light gray, 0.1 increments
- Labels: 14pt font

**Data Points:**
```
(0, 0) → Class 0 (blue circle, diameter 30px)
(0, 1) → Class 1 (red square, 30px)
(1, 0) → Class 1 (red square, 30px)
(1, 1) → Class 0 (blue circle, diameter 30px)
```

**Decision Boundary (Perceptron):**
- Straight line (e.g., y = -x + 0.5)
- Color: Black, 3px dashed line
- **Crosses errors!** Line unavoidably misclassifies some points
- Red X marks on misclassified points

**Title:** "Perceptron: Cannot Separate XOR" (16pt, top)
**Subtitle:** "Linear boundary fails" (12pt, red)

---

**Plot 2: MLP Succeeds (Right)**

**Axes:** Same as Plot 1

**Data Points:** Same as Plot 1
```
(0, 0) → Blue circle
(0, 1) → Red square
(1, 0) → Red square
(1, 1) → Blue circle
```

**Decision Boundary (MLP):**
- Curved (non-linear) boundary
- Example: Parabolic or circular curve separating correctly
- Color: Black, 3px solid line
- **Cleanly separates!** All points correctly classified

**Background Shading (optional):**
- Region for Class 0: Light blue (alpha 0.2)
- Region for Class 1: Light red (alpha 0.2)
- Makes separation visually obvious

**Title:** "MLP: Non-Linear Boundary" (16pt, top)
**Subtitle:** "Solves XOR with hidden layers" (12pt, green)

---

## CNN Visuals

### Visual 4: Dense vs Conv Parameter Comparison

**File Name:** `dense_vs_conv_parameters.png`

**Dimensions:** 1600×700px (side-by-side comparison)

**Layout:** Two sections, 750px each, separated by 100px divider

**Section 1: Dense Layer (Left)**

**Input Image Grid:**
- 28×28 grid visualization (small squares)
- Each square: 5px × 5px (total 140×140px visual)
- Color: Grayscale gradient (simulate MNIST digit)
- Label above: "28×28 Image = 784 pixels" (14pt)

**Arrow Down:**
- 100px tall, 20px wide
- Label on arrow: "Every pixel connected to every neuron" (12pt)

**Hidden Layer:**
- 128 circles (show subset, e.g., 20 circles with "...")
- Each circle: 15px diameter, light orange
- Arrangement: Horizontal line
- Label: "128 neurons" (14pt)

**Spaghetti Diagram:**
- Many criss-crossing lines from grid to circles
- Color: Gray (#999), thin (1px), semi-transparent (0.3 alpha)
- Visual mess to show complexity

**Calculation Box (below):**
```
┌─────────────────────────┐
│ Parameters:             │
│ 784 × 128 = 100,352     │
│                         │
│ Plus biases: +128       │
│ Total: 100,480 params   │
└─────────────────────────┘
```
- Box: 300px × 150px, light gray background (#F0F0F0)
- Border: 2px solid black
- Text: 14pt, centered

---

**Section 2: Convolutional Layer (Right)**

**Input Image Grid:**
- Same 28×28 grid (140×140px visual)
- Label above: "28×28 Image" (14pt)

**Filter Sliding:**
- Show 3×3 filter (highlighted square on grid)
- Filter: 15×15px red outline, thick (3px border)
- Position: On top-left corner of grid
- Label: "3×3 Filter slides across image" (12pt, with arrow showing motion)

**Arrow Down:**
- Label: "Same 9 parameters reused 676 times" (12pt, green)

**Feature Maps:**
- Show 32 small grids (each 20×20px, representing output)
- Arrange in 4×8 grid
- Label: "32 Feature Maps" (14pt)

**Calculation Box (below):**
```
┌─────────────────────────┐
│ Parameters per filter:  │
│ 3 × 3 = 9               │
│                         │
│ 32 filters: 9 × 32      │
│ = 288 parameters        │
│                         │
│ Plus biases: +32        │
│ Total: 320 params       │
└─────────────────────────┘
```
- Box: 300px × 200px
- Highlight: "320 params" in green, bold

---

**Comparison Box (bottom center):**
```
┌──────────────────────────────────────┐
│  Dense:  100,480 parameters          │
│  Conv:        320 parameters         │
│  ─────────────────────────────       │
│  Reduction: 314× fewer!              │
│  ✓ Parameter sharing                 │
│  ✓ Translation invariance            │
└──────────────────────────────────────┘
```
- Box: 500px × 150px, yellow background (#FFF59D)
- Border: 4px solid green
- Font: 16pt bold

---

### Visual 5: Convolutional Filter Animation

**Option A: Animated GIF (Preferred)**

**File Name:** `conv_filter_animation.gif`

**Dimensions:** 1000×800px

**Frame Count:** 12 frames (3×4 grid positions)

**Input Image (5×5):**
```
[1 2 1 0 0]
[0 1 2 1 0]
[0 0 1 2 1]
[1 0 0 1 2]
[2 1 0 0 1]
```
- Display as grid: 250×250px (50px per cell)
- Numbers visible in each cell (24pt font)
- Grayscale shading based on value (0=white, 2=dark gray)

**3×3 Filter (Edge Detector):**
```
[-1 -1 -1]
[ 0  0  0]
[ 1  1  1]
```
- Display as 150×150px grid (50px per cell)
- Numbers visible (20pt font, white text)
- Color: Orange (#FFA500) overlay

**Animation Sequence:**

**Frame 1:** Filter at position (0, 0) - top-left
- Highlight 3×3 region of input being convolved
- Show calculation: sum of element-wise multiply
- Result: "4" appears in output position (0, 0)

**Frame 2:** Filter slides right (stride=1) to position (1, 0)
- Highlight new 3×3 region
- Calculation shown
- Result in output position (1, 0)

**Frames 3-12:** Continue sliding across (left-to-right, top-to-bottom)

**Output Feature Map (3×3):**
- Builds up as filter slides
- Display as 150×150px grid
- Filled cells shown in green

**Labels:**
- Top: "Convolutional Operation: Filter Sliding" (18pt bold)
- Left side: "Input (5×5)", "Filter (3×3)"
- Right side: "Output (3×3 Feature Map)"
- Bottom: "Stride=1, No Padding" (12pt)

**Frame Rate:** 2 frames per second (500ms per frame)

**Loop:** Infinite

---

**Option B: Static (3-Frame Summary)**

**File Name:** `conv_filter_static.png`

**Dimensions:** 1800×600px (3 panels horizontally)

**Panel 1: Start**
- Filter at position (0, 0)
- Label: "Start: Filter at top-left" (14pt)

**Panel 2: Middle**
- Filter at position (1, 1) - center
- Label: "Middle: Filter slides across" (14pt)

**Panel 3: End**
- Filter at position (2, 2) - bottom-right
- Complete output shown
- Label: "End: Complete feature map" (14pt)

---

### Visual 6: Feature Hierarchy (CNN Layers)

**File Name:** `feature_hierarchy.png`

**Dimensions:** 2000×600px (horizontal flow)

**Style:** Illustration showing progressive abstraction

**Elements (left to right):**

**Input Image:**
- Photo of cat (200×200px)
- Label below: "Input Image" (14pt)

**Arrow →**
- 100px long, 20px wide
- Label: "Layer 1" (12pt)

**Layer 1 Feature Maps (Edges):**
- Show 3 small images (100×100px each, arranged vertically):
  1. Vertical edges detected (white lines on black)
  2. Horizontal edges detected
  3. Diagonal edges detected
- Labels:
  - Above: "Low-Level Features" (14pt bold)
  - Below each: "Vertical", "Horizontal", "Diagonal" (10pt)

**Arrow →**
- Label: "Layer 2" (12pt)

**Layer 2 Feature Maps (Textures):**
- Show 3 small images (100×100px each):
  1. Fur texture pattern
  2. Whisker patterns
  3. Circular shapes (eyes region)
- Labels:
  - Above: "Mid-Level Features" (14pt bold)
  - Below each: "Fur", "Whiskers", "Curves" (10pt)

**Arrow →**
- Label: "Layer 3" (12pt)

**Layer 3 Feature Maps (Object Parts):**
- Show 3 small images (100×100px each):
  1. Eye detector
  2. Nose detector
  3. Ear detector
- Labels:
  - Above: "High-Level Features" (14pt bold)
  - Below each: "Eyes", "Nose", "Ears" (10pt)

**Arrow →**
- Label: "Layer 4" (12pt)

**Output:**
- Large label: "Cat" (36pt bold)
- Confidence: "95%" (24pt, green)
- Icon: Cat silhouette (100×100px)

**Bottom Annotation:**
```
Automatic feature hierarchy: Edges → Textures → Parts → Objects
Network learns these features through backpropagation (not hand-designed)!
```
- Font: 14pt italic, centered
- Color: Dark gray (#333)

---

## ResNet Visuals

### Visual 7: Gradient Flow Comparison

**File Name:** `gradient_flow_comparison.png`

**Dimensions:** 1600×900px (stacked vertically)

**Layout:** Two diagrams, 1600×400px each, separated by 100px

**Diagram 1: Standard Network (Top) - Vanishing Gradient**

**Forward Pass (left side):**
```
Input → [Layer 1] → [Layer 2] → ... → [Layer 10] → Output
         (ReLU)      (ReLU)             (ReLU)
```
- Boxes: 120×80px each, light blue (#ADD8E6)
- Arrows: 50px between boxes
- Label above: "Forward Pass" (14pt)

**Backward Pass (right side, same diagram):**
```
Output ←─────────────────────────────────────────── Input
       ← Gradient Flow
```
- Arrows: Pointing left (backward), red color (#FF6B6B)
- Gradient magnitudes shown above arrows (decreasing):
  - Layer 10: "1.0" (bold, green)
  - Layer 5: "0.01" (orange)
  - Layer 1: "0.0001" (red, bold, larger font)

**Visualization:**
- Arrow thickness decreases left-to-right
- Layer 10 arrow: 10px thick
- Layer 5 arrow: 3px thick
- Layer 1 arrow: 1px thick (nearly invisible)

**Annotation (red box, bottom):**
```
❌ Vanishing Gradient Problem
Gradients shrink exponentially
Early layers can't learn!
```

---

**Diagram 2: ResNet (Bottom) - Gradient Highway**

**Forward Pass:**
```
Input → [ResBlock1] → [ResBlock2] → ... → [ResBlock10] → Output
        ↓ skip ↓       ↓ skip ↓             ↓ skip ↓
```
- ResBlocks: 120×120px, light orange (#FFD699)
- Skip connections: Curved arrows arcing over blocks
  - Color: Green (#4CAF50), 4px thick, dashed
  - Arc from input of ResBlock to output

**Backward Pass:**
```
Output ←──────────── [Direct Gradient Path] ──────────── Input
       ← Gradient Highway (via skip connections)
```
- Main gradient path: Thick green arrow (15px) flowing along skip connections
- Secondary gradients through blocks: Thinner red arrows (5px)

**Gradient magnitudes (NOT vanishing!):**
- Layer 10: "1.0" (bold, green)
- Layer 5: "0.8" (green)
- Layer 1: "0.6" (green, bold) ← Still strong!

**Annotation (green box, bottom):**
```
✓ Skip Connections Provide Gradient Highway
Gradients flow directly backward
All layers receive strong gradient signal!
```

---

**Side-by-Side Comparison (bottom of image):**
```
┌─────────────────────────┬─────────────────────────┐
│   Standard Network      │      ResNet             │
├─────────────────────────┼─────────────────────────┤
│ ∂L/∂x = ∂F/∂x          │ ∂L/∂x = ∂F/∂x + 1      │
│ (can vanish)            │ (+1 ensures flow!)      │
└─────────────────────────┴─────────────────────────┘
```
- Box: 600px × 150px, centered
- Font: 18pt monospace

---

### Visual 8: Residual Block Diagram

**File Name:** `residual_block_diagram.png`

**Dimensions:** 1000×800px

**Style:** Technical flowchart

**Main Flow (left side, going down):**

```
    x (input)
    │
    ├──────────────────(skip connection)──────────┐
    │                                              │
    ↓                                              │
┌─────────┐                                        │
│ Conv3×3 │                                        │
│64 filters│                                       │
└─────────┘                                        │
    ↓                                              │
┌─────────┐                                        │
│  Batch  │                                        │
│  Norm   │                                        │
└─────────┘                                        │
    ↓                                              │
┌─────────┐                                        │
│  ReLU   │                                        │
└─────────┘                                        │
    ↓                                              │
┌─────────┐                                        │
│ Conv3×3 │                                        │
│64 filters│                                       │
└─────────┘                                        │
    ↓                                              │
┌─────────┐                                        │
│  Batch  │                                        │
│  Norm   │                                        │
└─────────┘                                        │
    │                                              │
    ↓     F(x)                                     │
    │                                              │
    └──────────────→ [  ADD  ] ←───────────────────┘
                         │
                         ↓
                     ┌─────────┐
                     │  ReLU   │
                     └─────────┘
                         │
                         ↓
                      y (output)
```

**Box Specifications:**
- Conv boxes: 150×60px, light blue (#ADD8E6), 3px border
- Batch Norm boxes: 150×50px, light yellow (#FFF9C4), 2px border
- ReLU boxes: 150×50px, light orange (#FFCCBC), 2px border
- ADD box: 100×100px circle, light green (#C8E6C9), 4px border

**Skip Connection:**
- Curved arrow (Bezier curve) from input x to ADD
- Color: Green (#4CAF50), 6px thick
- Dashed line style (10px dash, 5px gap)
- Arrow head: 20px triangle

**Arrows:**
- Main flow: Black, 4px thick, solid
- Labels: 12pt font, positioned next to arrows

**Formulas (bottom boxes):**

**Box 1 (left, 400×120px):**
```
┌─────────────────────────┐
│ Standard Block:         │
│ H(x) = F(x)            │
│ (learn full mapping)    │
└─────────────────────────┘
```

**Box 2 (right, 400×120px):**
```
┌─────────────────────────┐
│ Residual Block:         │
│ H(x) = F(x) + x        │
│ (learn residual)        │
└─────────────────────────┘
```

**Annotation (top):**
- "ResNet Residual Block" (20pt bold)
- "F(x) = learned residual, x = identity shortcut" (14pt italic)

---

## RNN/LSTM Visuals

### Visual 9: RNN Unrolled Through Time

**File Name:** `rnn_unrolled.png`

**Dimensions:** 1800×700px (wide horizontal)

**Layout:** 4 time steps shown horizontally

**Structure for each time step:**

```
     x_t
      ↓
    [RNN]
      ↓
     h_t ─────→ (to next time step)
      ↓
     y_t
```

**Detailed Spec:**

**Input Sequence (top row):**
- x₁="The", x₂="cat", x₃="sat", x₄="on"
- Position: 400px apart horizontally
- Style: Rounded rectangles, 100×50px
- Color: Light blue (#BBDEFB), 2px border
- Font: 16pt, centered

**RNN Cells (middle row):**
- 4 cells, aligned below inputs
- Shape: Rounded square, 120×120px
- Color: Light orange (#FFD699), 3px border
- Label inside: "RNN" (20pt bold)
- Small label below: "tanh" (12pt)

**Hidden States (arrows between cells):**
- Curved arrows from h_t to next cell's input
- Color: Purple (#9C27B0), 5px thick
- Label: "h₁", "h₂", "h₃", "h₄" (14pt bold, purple)
- Direction: Horizontal, right-pointing

**Outputs (bottom row):**
- y₁="cat", y₂="sat", y₃="on", y₄="the"
- Position: Aligned below RNN cells
- Style: Same as inputs (rounded rectangles)
- Color: Light green (#C8E6C9)

**Arrows:**
- Input to RNN: Black, 3px, downward
- RNN to hidden state: Purple, 5px, horizontal (loops back)
- RNN to output: Black, 3px, downward

**Weight Sharing Annotation:**
```
┌─────────────────────────────────────────┐
│ Same weights W_hh, W_xh, W_hy           │
│ shared across all time steps!           │
└─────────────────────────────────────────┘
```
- Box at bottom, 600px × 80px
- Yellow background (#FFF59D), 3px border
- Font: 16pt bold

**Formula (bottom-right):**
```
h_t = tanh(W_hh · h_{t-1} + W_xh · x_t + b)
```
- Font: 14pt monospace
- Box: 400px × 60px, light gray background

---

### Visual 10: LSTM Cell (Simplified)

**File Name:** `lstm_cell_simplified.png`

**Dimensions:** 1200×900px

**Style:** Conceptual diagram with conveyor belt metaphor

**Main Elements:**

**Cell State (Conveyor Belt):**
- Horizontal thick line across top third of diagram
- Color: Green (#4CAF50), 15px thick
- Arrows pointing right (→)
- Label above: "Cell State C_t (Memory Conveyor Belt)" (16pt bold)
- Formula: "C_t = f_t ⊙ C_{t-1} + i_t ⊙ C̃_t" (14pt)

**LSTM Cell Box (center):**
- Large rounded rectangle: 800×600px
- Color: Light orange (#FFE0B2), 4px border
- Label at top: "LSTM Cell" (24pt bold)

**Three Gates (inside cell box):**

**1. Forget Gate (left third):**
```
┌─────────────────┐
│  Forget Gate    │
│      f_t        │
│                 │
│   σ(W_f·[...])  │
│                 │
│  "What to       │
│   forget?"      │
└─────────────────┘
```
- Position: Left side of cell
- Size: 220×200px
- Color: Light red (#FFCDD2), 3px border
- Sigmoid symbol: σ (large, 36pt)
- Worker icon: 🗑️ (trash can, removing boxes from conveyor)

**2. Input Gate (center):**
```
┌─────────────────┐
│   Input Gate    │
│      i_t        │
│                 │
│   σ(W_i·[...])  │
│                 │
│  "What new      │
│   info to add?" │
└─────────────────┘
```
- Position: Center of cell
- Size: 220×200px
- Color: Light blue (#BBDEFB), 3px border
- Worker icon: 📦 (box, adding to conveyor)

**3. Output Gate (right third):**
```
┌─────────────────┐
│  Output Gate    │
│      o_t        │
│                 │
│   σ(W_o·[...])  │
│                 │
│  "What to       │
│   output?"      │
└─────────────────┘
```
- Position: Right side of cell
- Size: 220×200px
- Color: Light green (#C8E6C9), 3px border
- Worker icon: 📤 (outbox, shipping from conveyor)

**Inputs (bottom):**
- h_{t-1}: Previous hidden state (left arrow entering)
- x_t: Current input (center arrow entering)
- Both: Rounded rectangles, 100×50px, light gray

**Outputs (right side):**
- h_t: Hidden state (arrow exiting right)
- Label: 14pt, purple

**Metaphor Illustrations:**
- Small conveyor belt graphic at top (boxes moving right →)
- Worker stick figures at each gate
- Boxes labeled with "old info" and "new info"

**Formula Box (bottom):**
```
┌──────────────────────────────────────────────┐
│ Gates (Sigmoid: output 0 to 1):              │
│                                              │
│ Forget:  f_t = σ(W_f · [h_{t-1}, x_t])      │
│ Input:   i_t = σ(W_i · [h_{t-1}, x_t])      │
│ Output:  o_t = σ(W_o · [h_{t-1}, x_t])      │
│                                              │
│ Cell State Update (ADDITIVE):                │
│ C_t = f_t ⊙ C_{t-1} + i_t ⊙ C̃_t            │
│ (This preserves gradients!)                  │
└──────────────────────────────────────────────┘
```
- Box: 800px × 200px, light yellow background (#FFF9C4)
- Font: 13pt monospace

---

## Transformer Visuals

### Visual 11: Attention Matrix Heatmap

**File Name:** `attention_matrix_heatmap.png`

**Dimensions:** 1000×1000px (square)

**Data:**
- Sentence: "The cat sat on the mat"
- 6 words → 6×6 matrix

**Matrix:**

```
       The  cat  sat  on  the  mat
The   [0.1  0.1  0.1  0.1  0.5  0.1]
cat   [0.1  0.2  0.6  0.05 0.05 0.0]
sat   [0.05 0.7  0.1  0.1  0.05 0.0]
on    [0.05 0.1  0.1  0.1  0.05 0.6]
the   [0.4  0.1  0.05 0.05 0.1  0.3]
mat   [0.1  0.1  0.05 0.6  0.1  0.05]
```

**Heatmap Colors:**
- 0.0: White (#FFFFFF)
- 0.3: Light blue (#BBDEFB)
- 0.5: Medium blue (#42A5F5)
- 0.7: Dark blue (#1976D2)

**Grid:**
- 6×6 cells, each 140×140px
- Border: 2px gray (#BDBDBD)
- Values displayed in cells (18pt font, black or white depending on background)

**Axes:**
- X-axis (top): "Query (from)" - word labels (16pt)
- Y-axis (left): "Key (to)" - word labels (16pt)

**Annotations (arrows pointing to specific cells):**

**Arrow 1:**
- From cell [sat, cat] (value 0.7)
- Label: "'sat' pays attention to 'cat' (subject)" (14pt, red box)

**Arrow 2:**
- From cell [on, mat] (value 0.6)
- Label: "'on' pays attention to 'mat' (object)" (14pt, red box)

**Title (top):**
- "Self-Attention Matrix" (20pt bold)
- Subtitle: "Darker = Higher Attention Weight" (14pt italic)

**Formula (bottom):**
```
Attention(Q, K, V) = softmax(QK^T / √d_k) · V
```
- Font: 16pt monospace
- Box: 500px × 60px, light gray background

---

### Visual 12: RNN vs Transformer Processing

**File Name:** `rnn_vs_transformer_processing.png`

**Dimensions:** 1600×800px (side-by-side)

**Layout:** Two panels, 750px each

**Panel 1: RNN Sequential (Left)**

**Title:** "RNN: Sequential Processing" (18pt bold, red)

**Timeline Visualization:**
```
Time 1: Process "The"     → h₁  (wait...)
  ⏱️  ▮ (progress bar 25%)

Time 2: Process "cat"     → h₂  (wait for h₁...)
  ⏱️  ▮▮ (progress bar 50%)

Time 3: Process "sat"     → h₃  (wait for h₂...)
  ⏱️  ▮▮▮ (progress bar 75%)

Time 4: Process "on"      → h₄  (wait for h₃...)
  ⏱️  ▮▮▮▮ (progress bar 100%)
```

**Annotations:**
```
❌ Must compute sequentially
❌ Time step t must wait for t-1
❌ Cannot parallelize on GPU
❌ Total time: O(n) steps
```
- Red text, 14pt
- X marks in red (#F44336)

**GPU Utilization Bar:**
- Width: 600px, height: 40px
- Only 1 core lit up (out of many)
- Label: "GPU: 1/1000 cores active" (wasted potential)
- Color: Red gradient

---

**Panel 2: Transformer Parallel (Right)**

**Title:** "Transformer: Parallel Processing" (18pt bold, green)

**Parallel Visualization:**
```
All at once:
  "The" → [Embed + Pos] ─┐
  "cat" → [Embed + Pos] ─┼─→ [Multi-Head    → Output
  "sat" → [Embed + Pos] ─┤    Attention]       (all words
  "on"  → [Embed + Pos] ─┘                      at once)
```

**Attention Connections:**
- Show all-to-all connections between words
- Grid of lines connecting each word to every other word
- Color: Blue (#2196F3), semi-transparent (0.4 alpha)
- Label: "Self-Attention: All word pairs in parallel" (12pt)

**Annotations:**
```
✓ Process all positions simultaneously
✓ Attention computed for all pairs at once
✓ Fully parallelizable on GPU
✓ Total time: O(1) steps (constant!)
```
- Green text, 14pt
- Checkmarks in green (#4CAF50)

**GPU Utilization Bar:**
- Width: 600px, height: 40px
- All cores lit up (full bar)
- Label: "GPU: 1000/1000 cores active" (fully utilized)
- Color: Green gradient

---

**Comparison Box (bottom center):**
```
┌─────────────────────────┬─────────────────────────┐
│         RNN             │      Transformer        │
├─────────────────────────┼─────────────────────────┤
│ Time:    O(n)           │ Time:    O(1)           │
│ Memory:  O(n·d)         │ Memory:  O(n²·d)        │
│ Parallel: No ❌         │ Parallel: Yes ✓         │
│ Training: Slow          │ Training: Fast (10-100×)│
└─────────────────────────┴─────────────────────────┘
```
- Box: 800px × 200px
- Border: 4px solid black
- Font: 16pt

---

## Master Diagrams

### Visual 13: Historical Timeline Poster

**File Name:** `architecture_timeline_poster.pdf` (and .png)

**Dimensions:** 2400×1200px (24"×12" for printing, or landscape poster)

**Style:** Infographic timeline

**Timeline Structure:**

**Horizontal axis:** 1950 to 2025 (left to right)

**Milestones (bubbles on timeline):**

**Era 1: 1950s-1960s (Blue):**
- **1958:** Perceptron (Rosenblatt)
  - Icon: Single circle neuron
  - Label: "First neural network"
- **1969:** XOR limitation proven
  - Icon: Red X on perceptron
  - Label: "AI Winter begins"

**Era 2: 1980s (Yellow):**
- **1986:** Backpropagation
  - Icon: Network with arrows backward
  - Label: "Multi-layer training enabled"
- **1989:** LeNet (LeCun)
  - Icon: CNN diagram (small)
  - Label: "First successful CNN"

**Era 3: 1990s (Orange):**
- **1997:** LSTM
  - Icon: LSTM cell (simplified)
  - Label: "Solves RNN vanishing gradient"

**Era 4: 2010s - Deep Learning (Green):**
- **2012:** AlexNet
  - Icon: CNN + GPU
  - Label: "ImageNet breakthrough - 15% error"
  - Star icon ⭐ (revolutionary)
- **2014:** VGG
  - Icon: Stacked 3×3 filters
  - Label: "Systematic depth study"
- **2015:** ResNet
  - Icon: Skip connection diagram
  - Label: "152 layers - beat humans"
  - Star icon ⭐

**Era 5: 2017+ Transformer Era (Purple):**
- **2017:** Transformer
  - Icon: Attention mechanism
  - Label: "Attention Is All You Need"
  - Star icon ⭐
- **2018:** BERT / GPT
  - Icon: Language model
  - Label: "Pre-trained models"
- **2020:** GPT-3
  - Icon: 175B parameters
  - Label: "Foundation models"
- **2022:** ChatGPT
  - Icon: Chat interface
  - Label: "Conversational AI mainstream"

**Color Coding (Legend in top-right):**
```
Blue:   Dense Networks
Green:  CNNs
Orange: RNNs/LSTMs
Purple: Transformers
```

**Bottom Section: Problem → Solution Mapping:**

```
┌──────────────────────────────────────────────────────┐
│ Problem                → Solution                    │
├──────────────────────────────────────────────────────┤
│ Can't learn XOR        → Multi-layer + activation    │
│ Image spatial struct   → Convolutional layers        │
│ Vanishing gradients    → ReLU, then Skip connections │
│ Sequences              → RNNs, then LSTMs            │
│ Long sequences + speed → Transformers (attention)    │
└──────────────────────────────────────────────────────┘
```

**Annotations:**
- Major breakthroughs marked with ⭐
- "AI Winter" period shaded in gray (1969-1986)
- "Deep Learning Era" shaded in light green (2012+)

---

### Visual 14: Architecture Selection Flowchart

**File Name:** `architecture_decision_flowchart.pdf` (and .png)

**Dimensions:** 1600×1200px

**Style:** Decision tree / flowchart

**Start Node (top center):**
```
┌──────────────────────┐
│ START:               │
│ What type of data?   │
└──────────────────────┘
```
- Shape: Rounded rectangle, 300×80px
- Color: Light blue (#BBDEFB), 4px border
- Font: 18pt bold

**Level 1 Decision:**

```
         ┌─────────┐
    ┌────│ Images? │────┐
    │    └─────────┘    │
   Yes                  No
    │                    │
    ↓                    ↓
[Go to CNN]      [Go to Text/Tabular]
```

**Images Branch:**
```
┌──────────────────────┐
│ Spatial structure?   │
└──────────────────────┘
         │
    Yes ─┼─ No
         │     │
         ↓     ↓
      [CNN] [Dense]
         │
    How deep?
         │
    ┌────┼────┐
    │         │
  <10    50+ layers
layers      │
    │       ↓
    ↓   [ResNet]
 [VGG or   (skip
  simple    connections
  CNN]      required)
```

**Text/Sequences Branch:**
```
┌──────────────────────┐
│ Text or Sequences?   │
└──────────────────────┘
         │
    Yes ─┼─ No (Tabular)
         │         │
         ↓         ↓
   Sequence    [Dense]
    length?    or
         │     [XGBoost]
    ┌────┼────┐
    │         │
  <100    100+
  tokens   tokens
    │         │
    ↓         ↓
 [LSTM]   [Transformer]
 [GRU]    (if large data)
```

**Tabular Branch:**
```
┌──────────────────────┐
│ Tabular Data         │
└──────────────────────┘
         │
    Structure?
         │
    ┌────┼────┐
    │         │
 Simple   Complex
    │         │
    ↓         ↓
[Dense]   [XGBoost]
        (often better
         than NN!)
```

**Decision Boxes:**
- Shape: Diamonds, 200×100px
- Color: Light yellow (#FFF59D), 3px border

**Solution Boxes:**
- Shape: Rectangles with rounded corners, 250×100px
- Colors:
  - Dense: Light gray (#E0E0E0)
  - CNN: Light green (#C8E6C9)
  - ResNet: Dark green (#81C784)
  - LSTM: Light orange (#FFD699)
  - Transformer: Light purple (#E1BEE7)
  - XGBoost: Light brown (#BCAAA4)
- Border: 4px solid matching darker shade

**Arrows:**
- Width: 4px
- Color: Dark gray (#333)
- Labels on arrows: "Yes", "No", "<10", "50+" (12pt)

**Heuristics Box (bottom):**
```
┌──────────────────────────────────────────────────────┐
│ Additional Heuristics:                               │
│                                                      │
│ • Depth: Start shallow (2-3 layers), add if needed  │
│ • Neurons: Powers of 2 (64, 128, 256, 512)         │
│ • Activation: ReLU (hidden), Softmax/Sigmoid (out) │
│ • Overfitting: Use Dropout, early stopping         │
│ • Small data (<10K): Use simpler models (LSTM)     │
│ • Large data (>1M): Use complex (Transformer)      │
└──────────────────────────────────────────────────────┘
```
- Box: 1400px × 250px
- Yellow background (#FFF59D), 3px border
- Font: 14pt

---

## Tool Recommendations

### Diagramming Tools

**1. Draw.io (diagrams.net) - FREE ✅ RECOMMENDED**
- **Best for:** Architecture diagrams, flowcharts, technical schematics
- **Pros:** Free, web-based, neural network shape library available
- **Export:** PNG, SVG, PDF
- **Download:** https://www.diagrams.net/
- **Templates:** Search for "neural network" in template library

**Use for:** Visuals 1, 2, 7, 8, 9, 10, 14

---

**2. Microsoft PowerPoint / Keynote**
- **Best for:** Quick diagrams, combining text and shapes
- **Pros:** Familiar interface, good for presentations
- **Export:** PDF, PNG (File → Export)
- **Built-in:** Shapes library, SmartArt

**Use for:** Visuals 1, 2, 4, 12

---

**3. Excalidraw - FREE**
- **Best for:** Hand-drawn style diagrams (sketchy, informal)
- **Pros:** Simple, intuitive, web-based
- **Link:** https://excalidraw.com/
- **Export:** PNG, SVG

**Use for:** Informal versions of any diagram

---

**4. Canva - FREE (Pro for advanced)**
- **Best for:** Infographics, timelines, posters
- **Pros:** Beautiful templates, drag-and-drop
- **Link:** https://www.canva.com/
- **Templates:** Search "timeline infographic"

**Use for:** Visual 13 (Timeline Poster)

---

**5. Python (Matplotlib/Seaborn) - FREE**
- **Best for:** Plots, heatmaps, data-driven visualizations
- **Pros:** Precise control, programmable, publication-quality
- **Libraries:**
  ```python
  import matplotlib.pyplot as plt
  import seaborn as sns
  import numpy as np
  ```

**Use for:** Visuals 3, 6, 11

**Example code for Visual 11 (Attention Heatmap):**
```python
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Attention matrix
attention = np.array([
    [0.1, 0.1, 0.1, 0.1, 0.5, 0.1],
    [0.1, 0.2, 0.6, 0.05, 0.05, 0.0],
    [0.05, 0.7, 0.1, 0.1, 0.05, 0.0],
    [0.05, 0.1, 0.1, 0.1, 0.05, 0.6],
    [0.4, 0.1, 0.05, 0.05, 0.1, 0.3],
    [0.1, 0.1, 0.05, 0.6, 0.1, 0.05]
])

words = ["The", "cat", "sat", "on", "the", "mat"]

plt.figure(figsize=(10, 10))
sns.heatmap(attention, annot=True, fmt='.2f',
            xticklabels=words, yticklabels=words,
            cmap='Blues', cbar=True, square=True)
plt.xlabel('Key (to)', fontsize=14)
plt.ylabel('Query (from)', fontsize=14)
plt.title('Self-Attention Matrix', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('attention_matrix_heatmap.png', dpi=300)
plt.show()
```

---

### Animation Tools

**1. PowerPoint Animations**
- **Best for:** Simple step-by-step reveals
- **Export:** Save as GIF or MP4 (via screen recording)

**Use for:** Visual 5 (Conv Filter Animation)

---

**2. Matplotlib Animation**
- **Best for:** Data-driven animations
- **Library:** `matplotlib.animation.FuncAnimation`

**Example for Visual 5:**
```python
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate_conv_filter():
    # ... (code to animate filter sliding)
    pass

# Save as GIF
anim.save('conv_filter_animation.gif', writer='pillow', fps=2)
```

---

**3. Manim (3Blue1Brown's library) - Advanced**
- **Best for:** Mathematical animations (like 3Blue1Brown videos)
- **Pros:** Professional quality, beautiful
- **Cons:** Steep learning curve, Python coding required
- **Link:** https://www.manim.community/

**Use for:** Polished versions of all visuals (if time permits)

---

## Color Palette

**Consistent colors across all diagrams:**

### Architecture Family Colors
- **Dense Networks:** Blue (#2196F3)
- **CNNs:** Green (#4CAF50)
- **ResNet:** Dark Green (#388E3C)
- **RNNs/LSTMs:** Orange (#FF9800)
- **Transformers:** Purple (#9C27B0)

### Node/Element Colors
- **Input nodes:** Light blue (#ADD8E6)
- **Hidden layers:** Light orange (#FFD699)
- **Output nodes:** Light green (#90EE90)
- **Activation functions:** Light red (#FFCDD2)

### Annotation Colors
- **Success/Positive:** Green (#4CAF50)
- **Error/Negative:** Red (#F44336)
- **Warning:** Orange (#FF9800)
- **Info:** Blue (#2196F3)

### Background Colors
- **Diagrams:** White (#FFFFFF)
- **Boxes/Callouts:** Light gray (#F5F5F5) or light yellow (#FFF9C4)

---

## Export Settings

**For All Visuals:**

### PNG Export
- **Resolution:** 300 DPI (print quality)
- **Color mode:** RGB
- **Background:** White (not transparent)
- **File size:** Optimize for web (compress to <500KB if possible)

### PDF Export
- **For posters (Visual 13, 14):** Vector format (scalable)
- **Embed fonts:** Yes
- **Compress images:** Medium quality

### GIF Export (Animations)
- **Frame rate:** 2 fps (500ms per frame)
- **Loop:** Infinite
- **Optimize:** Reduce colors to 256 (smaller file size)

---

**End of Visual Specifications**

**Next Steps:**
1. Create diagrams following exact specifications above
2. Use recommended tools for each visual type
3. Export in specified formats
4. Save all files in `architecture_evolution/instructor_materials/visuals/` folder
5. Reference these visuals in teaching scripts

**Estimated Time to Create All 14 Visuals:** 3-4 hours
