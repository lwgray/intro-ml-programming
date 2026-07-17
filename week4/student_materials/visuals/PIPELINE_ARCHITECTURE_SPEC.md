# Visual Specification: sklearn Pipeline Architecture Diagram

**Purpose:** Show the architecture of sklearn Pipeline with data flow from raw input to final predictions.

**File name:** `pipeline_architecture.png`

**Usage:** Display when introducing Pipeline solution (Segment 7, Minute 105)

---

## Visual Layout

**Dimensions:** 1200px × 800px
**Background:** White (#FFFFFF)
**Font:** Sans-serif

---

## Title

**Text:** "sklearn Pipeline Architecture"
**Position:** Top center, 30px from top
**Font size:** 30pt
**Font weight:** Bold
**Color:** Dark blue (#1f4788)

**Subtitle:**
**Text:** "Automatic Leakage Prevention"
**Position:** 75px from top
**Font size:** 18pt
**Color:** Green (#27ae60)

---

## Pipeline Container

**Main container box:**
**Position:** Centered, 150px from top
**Size:** 1000px × 500px
**Border:** 4px solid dark blue (#1f4788)
**Fill:** Light blue (#e8f4f8)
**Corner radius:** 10px
**Shadow:** 5px shadow, gray (#999999)

**Label (top-left of container):**
**Text:** "Pipeline"
**Font size:** 24pt, Bold
**Color:** White (#FFFFFF)
**Background:** Dark blue (#1f4788) tab (150px × 40px)

---

## Pipeline Steps (Left to Right Flow)

### Step Boxes

**Vertical alignment:** All boxes centered vertically in container (y = 300px)
**Horizontal spacing:** 30px between boxes
**Starting X position:** 100px

---

### Step 1: Imputer

**Box:**
- Position: (100, 260)
- Size: 150px × 80px
- Border: 2px solid blue (#3498db)
- Fill: White (#FFFFFF)
- Corner radius: 6px

**Icon (top of box):**
- Symbol: 🔢 or wrench icon
- Size: 24px

**Text:**
- Line 1: "SimpleImputer"
  - Font size: 14pt, Bold
  - Color: Blue (#2874a6)
- Line 2: "Fill missing values"
  - Font size: 10pt, Italic
  - Color: Gray (#666666)

**Method label (below box):**
- Text: "fit_transform(train)\ntransform(test)"
- Font size: 9pt
- Color: Gray (#666666)

---

### Arrow 1

**From:** Right edge of Imputer
**To:** Left edge of Scaler
**Style:** Thick arrow (4px), dark blue (#1f4788)

**Label above arrow:**
- Text: "Imputed data"
- Font size: 11pt
- Color: Dark blue (#1f4788)

---

### Step 2: StandardScaler

**Box:**
- Position: (280, 260)
- Size: 150px × 80px
- Border: 2px solid green (#27ae60)
- Fill: White (#FFFFFF)
- Corner radius: 6px

**Icon:**
- Symbol: 📏 or scale icon
- Size: 24px

**Text:**
- Line 1: "StandardScaler"
  - Font size: 14pt, Bold
  - Color: Green (#1e8449)
- Line 2: "Scale features"
  - Font size: 10pt, Italic
  - Color: Gray (#666666)

**Method label (below box):**
- Text: "fit_transform(train)\ntransform(test)"
- Font size: 9pt
- Color: Gray (#666666)

---

### Arrow 2

**From:** Right edge of Scaler
**To:** Left edge of Selector
**Style:** Thick arrow (4px), dark blue (#1f4788)

**Label above arrow:**
- Text: "Scaled data"
- Font size: 11pt
- Color: Dark blue (#1f4788)

---

### Step 3: SelectKBest

**Box:**
- Position: (460, 260)
- Size: 150px × 80px
- Border: 2px solid orange (#f39c12)
- Fill: White (#FFFFFF)
- Corner radius: 6px

**Icon:**
- Symbol: ⭐ or filter icon
- Size: 24px

**Text:**
- Line 1: "SelectKBest"
  - Font size: 14pt, Bold
  - Color: Orange (#d68910)
- Line 2: "Select features"
  - Font size: 10pt, Italic
  - Color: Gray (#666666)

**Method label (below box):**
- Text: "fit_transform(train)\ntransform(test)"
- Font size: 9pt
- Color: Gray (#666666)

---

### Arrow 3

**From:** Right edge of Selector
**To:** Left edge of Model
**Style:** Thick arrow (4px), dark blue (#1f4788)

**Label above arrow:**
- Text: "Selected features"
- Font size: 11pt
- Color: Dark blue (#1f4788)

---

### Step 4: Final Estimator (Model)

**Box:**
- Position: (640, 240)
- Size: 200px × 120px
- Border: 3px solid red (#e74c3c)
- Fill: Light red (#fadbd8)
- Corner radius: 6px

**Icon:**
- Symbol: 🤖 or brain icon
- Size: 32px

**Text:**
- Line 1: "RandomForest"
  - Font size: 16pt, Bold
  - Color: Red (#c0392b)
- Line 2: "Final Estimator"
  - Font size: 12pt, Italic
  - Color: Gray (#666666)

**Method label (below box):**
- Text: "fit(train)\npredict(test)"
- Font size: 10pt, Bold
- Color: Gray (#666666)

---

## Data Flow Visualization

### Input Data (Left)

**Position:** Left of Pipeline container, (30, 300)

**Box:**
- Size: 120px × 80px
- Border: 2px dashed gray (#999999)
- Fill: Light yellow (#fff9e6)

**Text:**
- Line 1: "X (raw data)"
  - Font size: 14pt, Bold
- Line 2: "Features with\nmissing values"
  - Font size: 10pt

**Arrow to Pipeline:**
- From: Right edge of input box
- To: Left edge of Pipeline container
- Style: Dashed arrow (3px), gray (#666666)
- Label: "Input" (11pt)

---

### Output Predictions (Right)

**Position:** Right of Pipeline container, (1050, 300)

**Box:**
- Size: 120px × 80px
- Border: 2px solid green (#27ae60)
- Fill: Light green (#d5f4e6)

**Text:**
- Line 1: "y_pred"
  - Font size: 14pt, Bold
  - Color: Green (#1e8449)
- Line 2: "Predictions"
  - Font size: 10pt

**Arrow from Pipeline:**
- From: Right edge of Model box
- To: Left edge of output box
- Style: Thick solid arrow (4px), green (#27ae60)
- Label: "Output" (11pt)

---

## ColumnTransformer (Optional Detail)

**Position:** Inside Pipeline container, top section (150, 170)

**Box:**
- Size: 400px × 60px
- Border: 2px dashed purple (#9b59b6)
- Fill: Light purple (#e8daef)

**Text:**
- Line 1: "ColumnTransformer (optional)"
  - Font size: 12pt, Bold
  - Color: Purple (#7d3c98)
- Line 2: "Apply different transformers to different columns"
  - Font size: 10pt, Italic

**Example inside:**
- "numeric → StandardScaler"
- "categorical → OneHotEncoder"
- Font size: 9pt

---

## Key Features Annotations

### Annotation 1: No Leakage

**Position:** Top right of Pipeline container
**Box:**
- Size: 250px × 60px
- Border: 2px solid green (#27ae60)
- Fill: Light green (#d5f4e6)

**Icon:** ✅ (large, 24px)

**Text:**
- Line 1: "✓ No Data Leakage"
  - Font size: 14pt, Bold, Green (#1e8449)
- Line 2: "Each step fits on training data only"
  - Font size: 10pt

---

### Annotation 2: Automatic

**Position:** Bottom right of Pipeline container
**Box:**
- Size: 250px × 60px
- Border: 2px solid blue (#3498db)
- Fill: Light blue (#d6eaf8)

**Icon:** ⚙️ (gear, 24px)

**Text:**
- Line 1: "⚙️ Automatic"
  - Font size: 14pt, Bold, Blue (#2874a6)
- Line 2: "Handles fit/transform correctly"
  - Font size: 10pt

---

## Bottom Code Example Box

**Position:** Bottom, centered, 700px from top

**Box:**
- Width: 1100px, Height: 120px
- Border: 2px solid gray (#cccccc)
- Fill: Light gray (#f5f5f5)
- Corner radius: 6px

**Title:**
- Text: "Example Code"
- Font size: 14pt, Bold
- Position: Top-left of box

**Code:**
```python
from sklearn.pipeline import Pipeline

pipeline = Pipeline([
    ('imputer', SimpleImputer()),
    ('scaler', StandardScaler()),
    ('selector', SelectKBest(k=10)),
    ('classifier', RandomForestClassifier())
])

pipeline.fit(X_train, y_train)      # Fits all steps
predictions = pipeline.predict(X_test)  # Applies all steps
```

**Font:** Monospace (Courier New), 11pt
**Syntax highlighting:**
- Keywords: Blue (#0066cc)
- Strings: Orange (#e67e22)
- Comments: Green (#27ae60)

---

## Execution Flow Annotation

### Training Flow (Above Pipeline)

**Position:** 180px from top, spanning pipeline steps

**Text with arrows:**
- "Training: fit_transform → fit_transform → fit_transform → fit"
- Font size: 11pt
- Color: Dark blue (#1f4788)
- Arrows point downward to each step

---

### Prediction Flow (Below Pipeline)

**Position:** 380px from top, spanning pipeline steps

**Text with arrows:**
- "Prediction: transform → transform → transform → predict"
- Font size: 11pt
- Color: Green (#27ae60)
- Arrows point upward from each step

---

## Color Palette

| Element | Color | Hex Code |
|---------|-------|----------|
| Pipeline container | Dark blue border | #1f4788 |
| Pipeline fill | Light blue | #e8f4f8 |
| Imputer | Blue | #3498db |
| Scaler | Green | #27ae60 |
| Selector | Orange | #f39c12 |
| Model | Red | #e74c3c |
| Model fill | Light red | #fadbd8 |
| Input | Light yellow | #fff9e6 |
| Output | Light green | #d5f4e6 |
| ColumnTransformer | Purple | #9b59b6 |
| Arrows | Dark blue | #1f4788 |
| Code background | Light gray | #f5f5f5 |

---

## Validation Checklist

- ✓ Pipeline container shown with clear border
- ✓ Four steps shown: Imputer → Scaler → Selector → Model
- ✓ Arrows show data flow left to right
- ✓ Each step labeled with fit_transform or fit/predict
- ✓ Input and output boxes shown
- ✓ No leakage annotation present
- ✓ Code example at bottom
- ✓ Training vs prediction flow differentiated
- ✓ Colors match specification
- ✓ ColumnTransformer mentioned (optional detail)

---

**This diagram clearly shows how Pipeline chains transformers and ensures no data leakage through proper fit/transform sequencing.**
