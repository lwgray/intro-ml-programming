# Visual Specification: Data Leakage Before/After Comparison

**Purpose:** Flowchart comparing WRONG (with leakage) vs CORRECT (no leakage) approaches with resulting accuracy differences.

**File name:** `data_leakage_examples.png`

**Usage:** Display when explaining data leakage impact (Segment 6, Minute 92)

---

## Visual Layout

**Dimensions:** 1400px × 900px
**Background:** White (#FFFFFF)
**Font:** Sans-serif

---

## Main Title

**Text:** "Data Leakage: The Impact on Model Performance"
**Position:** Top center, 30px from top
**Font size:** 30pt
**Font weight:** Bold
**Color:** Dark blue (#1f4788)

---

## Two-Column Layout

**Left Column:** ❌ WRONG (with leakage) - RED theme
**Right Column:** ✅ CORRECT (no leakage) - GREEN theme

**Divider:** Vertical dashed line (x = 700px), gray (#cccccc), 2px

---

## LEFT COLUMN: WRONG APPROACH

### Column Header

**Text:** "❌ WRONG: With Data Leakage"
**Position:** Centered at 350px horizontal, 90px from top
**Font size:** 24pt
**Font weight:** Bold
**Color:** Red (#e74c3c)
**Background box:**
- Width: 600px, Height: 50px
- Fill: Light red (#fadbd8)
- Border: 2px solid red (#e74c3c)

---

### Flowchart Boxes (Vertical flow)

**Starting Y position:** 180px
**Box spacing:** 100px vertical between boxes

#### Box 1: Complete Dataset
**Position:** (100, 180)
**Size:** 500px × 60px
**Border:** 2px solid black (#000000)
**Fill:** Light gray (#e0e0e0)
**Text:** "Complete Dataset (1000 samples)"
**Font size:** 14pt, centered

#### Arrow 1
**From:** Bottom of Box 1
**To:** Top of Box 2
**Style:** Solid black arrow, 3px
**Label:** "Step 1" (12pt, gray)

#### Box 2: Fit Scaler on ALL Data (LEAKAGE!)
**Position:** (100, 300)
**Size:** 500px × 80px
**Border:** 3px solid red (#e74c3c)
**Fill:** Light red (#fadbd8)
**Text:**
- Line 1: "scaler.fit(X)  # ALL DATA"
  - Font: Monospace, 12pt
  - Color: Black
- Line 2: "⚠️ LEAKAGE! Test data influences scaler"
  - Font size: 11pt, Italic
  - Color: Red (#c0392b)

**Warning icon:**
- Position: Top-right corner
- Icon: ⚠️ (24px)

#### Arrow 2
**From:** Bottom of Box 2
**To:** Top of Box 3
**Style:** Solid black arrow, 3px
**Label:** "Step 2" (12pt, gray)

#### Box 3: Scale Data
**Position:** (100, 420)
**Size:** 500px × 60px
**Border:** 2px solid black
**Fill:** Light gray (#e0e0e0)
**Text:** "X_scaled = scaler.transform(X)"
**Font:** Monospace, 12pt

#### Arrow 3
**From:** Bottom of Box 3
**To:** Top of Box 4
**Style:** Solid black arrow, 3px
**Label:** "Step 3" (12pt, gray)

#### Box 4: Split Data
**Position:** (100, 520)
**Size:** 500px × 60px
**Border:** 2px solid black
**Fill:** Light gray (#e0e0e0)
**Text:** "train_test_split(X_scaled, y)"
**Font:** Monospace, 12pt

#### Arrow 4
**From:** Bottom of Box 4
**To:** Top of Box 5
**Style:** Solid black arrow, 3px
**Label:** "Step 4" (12pt, gray)

#### Box 5: Train Model
**Position:** (100, 620)
**Size:** 500px × 60px
**Border:** 2px solid black
**Fill:** Light gray (#e0e0e0)
**Text:** "model.fit(X_train, y_train)"
**Font:** Monospace, 12pt

---

### Results Box (Left)

**Position:** (100, 720)
**Size:** 500px × 120px
**Border:** 3px solid red (#e74c3c)
**Fill:** Light red (#ffe6e6)
**Corner radius:** 8px

**Content:**
- Line 1: "Development Performance:"
  - Font size: 16pt, Bold
  - Color: Red (#c0392b)

- Line 2: "Training Accuracy: 0.98"
  - Font size: 18pt, Bold
  - Color: Black

- Line 3: "Test Accuracy: 0.97"
  - Font size: 18pt, Bold
  - Color: Black

- Line 4: "😊 \"Looks amazing!\""
  - Font size: 14pt
  - Color: Green (#27ae60)

**Arrow down (from results box):**
**To:** Production box below
**Style:** Thick red arrow, 4px
**Label:** "Deploy!" (14pt, bold)

---

### Production Reality Box (Left)

**Position:** (100, 860)
**Size:** 500px × 60px
**Border:** 3px solid dark red (#a93226)
**Fill:** Dark red (#e74c3c)

**Content:**
- Text: "Production Accuracy: 0.68  💀"
  - Font size: 20pt, Bold
  - Color: White (#FFFFFF)

**Annotation below:**
- Text: "29-point drop! Model failed!"
  - Font size: 12pt, Bold
  - Color: Dark red (#a93226)

---

## RIGHT COLUMN: CORRECT APPROACH

### Column Header

**Text:** "✅ CORRECT: No Data Leakage"
**Position:** Centered at 1050px horizontal, 90px from top
**Font size:** 24pt
**Font weight:** Bold
**Color:** Green (#27ae60)
**Background box:**
- Width: 600px, Height: 50px
- Fill: Light green (#d5f4e6)
- Border: 2px solid green (#27ae60)

---

### Flowchart Boxes (Vertical flow)

**Starting Y position:** 180px
**Box spacing:** 100px vertical between boxes

#### Box 1: Complete Dataset
**Position:** (800, 180)
**Size:** 500px × 60px
**Border:** 2px solid black
**Fill:** Light gray (#e0e0e0)
**Text:** "Complete Dataset (1000 samples)"
**Font size:** 14pt, centered

#### Arrow 1
**From:** Bottom of Box 1
**To:** Top of Box 2
**Style:** Solid black arrow, 3px
**Label:** "Step 1" (12pt, gray)

#### Box 2: Split Data FIRST
**Position:** (800, 300)
**Size:** 500px × 80px
**Border:** 3px solid green (#27ae60)
**Fill:** Light green (#d5f4e6)
**Text:**
- Line 1: "train_test_split(X, y)"
  - Font: Monospace, 12pt
  - Color: Black
- Line 2: "✓ Test set locked away!"
  - Font size: 11pt, Italic
  - Color: Green (#1e8449)

**Checkmark icon:**
- Position: Top-right corner
- Icon: ✓ (24px, green)

#### Arrow 2 (splits into two paths)
**From:** Bottom of Box 2
**To:** Two separate boxes (Train path and Test path)
**Style:** Solid black arrow that forks

#### Box 3a: Fit Scaler on TRAIN only
**Position:** (800, 420)
**Size:** 500px × 80px
**Border:** 2px solid green (#27ae60)
**Fill:** Light green (#d5f4e6)
**Text:**
- Line 1: "scaler.fit(X_train)  # TRAIN ONLY"
  - Font: Monospace, 12pt
  - Color: Black
- Line 2: "✓ No test contamination"
  - Font size: 11pt, Italic
  - Color: Green (#1e8449)

#### Arrow 3
**From:** Bottom of Box 3a
**To:** Top of Box 4
**Label:** "Apply to both"

#### Box 4: Scale Both Sets
**Position:** (800, 540)
**Size:** 500px × 60px
**Border:** 2px solid black
**Fill:** Light gray (#e0e0e0)
**Text:** "X_train_scaled, X_test_scaled"
**Font:** Monospace, 11pt

#### Arrow 4
**From:** Bottom of Box 4
**To:** Top of Box 5
**Style:** Solid black arrow, 3px

#### Box 5: Train Model
**Position:** (800, 640)
**Size:** 500px × 60px
**Border:** 2px solid black
**Fill:** Light gray (#e0e0e0)
**Text:** "model.fit(X_train_scaled, y_train)"
**Font:** Monospace, 12pt

---

### Results Box (Right)

**Position:** (800, 740)
**Size:** 500px × 120px
**Border:** 3px solid green (#27ae60)
**Fill:** Light green (#e6f7ee)
**Corner radius:** 8px

**Content:**
- Line 1: "Development Performance:"
  - Font size: 16pt, Bold
  - Color: Green (#1e8449)

- Line 2: "Training Accuracy: 0.95"
  - Font size: 18pt, Bold
  - Color: Black

- Line 3: "Test Accuracy: 0.83"
  - Font size: 18pt, Bold
  - Color: Black

- Line 4: "✓ Realistic estimate"
  - Font size: 14pt
  - Color: Green (#27ae60)

**Arrow down (from results box):**
**To:** Production box below
**Style:** Thick green arrow, 4px
**Label:** "Deploy!" (14pt, bold)

---

### Production Reality Box (Right)

**Position:** (800, 880)
**Size:** 500px × 60px
**Border:** 3px solid green (#1e8449)
**Fill:** Green (#27ae60)

**Content:**
- Text: "Production Accuracy: 0.81  ✅"
  - Font size: 20pt, Bold
  - Color: White (#FFFFFF)

**Annotation below:**
- Text: "2-point drop - expected variance!"
  - Font size: 12pt, Bold
  - Color: Green (#1e8449)

---

## Comparison Arrows & Annotations

### Comparison Arrow (between production boxes)

**Arrow:**
**From:** Left production box (0.68)
**To:** Right production box (0.81)
**Style:** Large curved arrow, 4px, dark blue (#1f4788)

**Label (on arrow):**
**Text:** "13-point improvement from fixing leakage!"
**Font size:** 14pt, Bold
**Color:** Dark blue (#1f4788)
**Background:** Yellow highlight (#fff59d)

---

## Bottom Summary Box

**Position:** Bottom center, spanning both columns, 20px from bottom

**Box:**
- Width: 1300px, Height: 80px
- Border: 3px solid dark blue (#1f4788)
- Fill: Light blue (#e3f2fd)

**Content:**
- Line 1: "⚠️ Key Lesson: Data Leakage Causes Production Failures"
  - Font size: 20pt, Bold
  - Color: Dark blue (#1f4788)

- Line 2: "Always split data FIRST, then preprocess. Use Pipeline to prevent leakage."
  - Font size: 16pt
  - Color: Black (#000000)

- Line 3: "Development accuracy that's \"too good\" is often leakage!"
  - Font size: 14pt
  - Color: Gray (#666666)

---

## Color Palette

| Element | Color | Hex Code |
|---------|-------|----------|
| Wrong path boxes | Light red | #fadbd8 |
| Wrong results | Red | #e74c3c |
| Wrong production | Dark red | #a93226 |
| Correct path boxes | Light green | #d5f4e6 |
| Correct results | Green | #27ae60 |
| Correct production | Green | #1e8449 |
| Warning | Yellow | #f39c12 |
| Checkmark | Green | #27ae60 |
| Title | Dark blue | #1f4788 |
| Comparison highlight | Yellow | #fff59d |

---

## Validation Checklist

- ✓ Left column shows WRONG approach with leakage
- ✓ Right column shows CORRECT approach
- ✓ Flowcharts show step-by-step process
- ✓ Leakage step highlighted with warning (left)
- ✓ Correct split highlighted with checkmark (right)
- ✓ Development scores shown (inflated left, realistic right)
- ✓ Production scores shown (failed left, successful right)
- ✓ Comparison arrow shows 13-point improvement
- ✓ Bottom summary box with key lesson
- ✓ Color coding: red = wrong, green = correct

---

**This visual dramatically shows the real-world impact of data leakage: inflated development scores that collapse in production vs realistic scores that hold up.**
