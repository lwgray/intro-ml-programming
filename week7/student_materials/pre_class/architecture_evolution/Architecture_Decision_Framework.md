# Neural Network Architecture Decision Framework
**Quick Reference Sheet - Week 7 Pre-Class**

---

## Step 1: Data Type → Architecture Family

```
┌─────────────────────────────────────────────────────────────────────┐
│                   WHAT TYPE OF DATA DO YOU HAVE?                    │
└────────┬────────────────────────────┬────────────────┬──────────────┘
         │                            │                │
    ┌────▼─────┐                 ┌────▼────┐      ┌───▼────┐
    │  IMAGES  │                 │  TEXT/  │      │TABULAR │
    │ (Photos, │                 │SEQUENCE │      │ (CSV,  │
    │ Scans)   │                 │ (Words, │      │Struct) │
    └────┬─────┘                 │  Time)  │      └───┬────┘
         │                       └────┬────┘          │
         │                            │               │
         ▼                            ▼               ▼
    Use CNN                  Use TRANSFORMER      Use DENSE
                              or LSTM/GRU        (2-5 layers)
```

---

## Step 2: Architecture Selection Table

| **Data Type** | **Problem** | **1st Choice** | **2nd Choice** | **When to Switch** |
|---------------|-------------|----------------|----------------|--------------------|
| **Images** | Classification | CNN (ResNet-18) | VGG-16 | >100K images → ResNet-50 |
| **Images** | Object Detection | YOLO, Faster R-CNN | RetinaNet | Accuracy > speed → Faster R-CNN |
| **Text** | Classification | BERT (fine-tune) | LSTM/GRU | <10K examples → LSTM |
| **Text** | Generation | GPT-2/GPT-3 | LSTM | Limited compute → LSTM |
| **Text** | Translation | Transformer | LSTM seq2seq | Old approach (pre-2017) |
| **Time Series** | Forecasting | LSTM/GRU | 1D CNN | Simple patterns → Dense |
| **Tabular** | Classification/Reg | Dense (2-5 layers) | XGBoost | Try XGBoost first! |
| **Mixed** | Image + Features | Multi-input (CNN+Dense) | Ensemble | Complex → separate models |

---

## Step 3: Layer Count Heuristics

### Dense Networks
```
Simple Problem (few features, linear-ish)     → 2-3 layers
Medium Problem (moderate features)            → 4-6 layers
Complex Problem (many features, non-linear)   → 7-10 layers
Very Deep (>10 layers)                        → Add skip connections (ResNet-style)
```

### CNNs
```
Small Images (28×28 like MNIST)               → 5-10 layers
Medium Images (64×64 to 128×128)              → 10-20 layers (VGG-16 style)
Large Images (224×224+ like ImageNet)         → 20-50 layers (ResNet-50)
Very Large Models (>50 layers)                → MUST use skip connections (ResNet)
```

### RNN/LSTM
```
Short sequences (<50 steps)                   → 1-2 layers
Medium sequences (50-200 steps)               → 2-3 layers
Long sequences (>200 steps)                   → 3 layers or switch to Transformer
```

### Transformers
```
Standard BERT/GPT                             → 6-12 layers
Large models (GPT-3)                          → 24-96 layers
```

---

## Step 4: Neuron/Filter Count Heuristics

### Dense Layers (Neurons per Layer)
```
Powers of 2:  64, 128, 256, 512  (GPU-efficient)

Start:     128-256 neurons
Too simple? → Increase to 256-512
Overfitting? → Decrease to 64-128 or add Dropout
```

### CNN Filters (Number of Filters per Conv Layer)
```
Pattern: DOUBLE after each pooling layer

Example architecture:
Layer 1-2:   32 filters  (before pooling)
Layer 3-4:   64 filters  (after pooling)
Layer 5-6:   128 filters (after pooling)
Layer 7-8:   256 filters (after pooling)
Dense:       512 neurons
```

### CNN Filter Sizes
```
3×3:   Standard (modern best practice)
5×5:   First layer (capture larger initial patterns)
7×7:   Very first layer for large images (224×224+)
1×1:   Dimensionality reduction (advanced)

Rule: Stack 3×3 filters instead of one large filter
      (Two 3×3 = same receptive field as 5×5, fewer params)
```

---

## Step 5: Activation Function Selection

| **Layer Type** | **Activation** | **Why** |
|----------------|----------------|---------|
| **Hidden layers (Dense)** | ReLU | Default. No vanishing gradient. |
| **Hidden layers (CNN)** | ReLU | Default. Fast, effective. |
| **Output (Binary class)** | Sigmoid | Outputs 0-1 probability. |
| **Output (Multi-class)** | Softmax | Outputs probability distribution. |
| **Output (Regression)** | Linear (none) | Continuous values (-∞ to +∞). |
| **LSTM/GRU gates** | Sigmoid, Tanh | Built-in, don't change. |

**Alternative Hidden Activations (Advanced):**
- **LeakyReLU:** If dying ReLU problem (many neurons output 0)
- **Swish/Mish:** Slightly better than ReLU (marginal gains, slower)
- **Tanh:** Old default (pre-2012), now rarely used

---

## Step 6: Common Patterns (Copy-Paste Architectures)

### Dense Network (Tabular Data)
```python
Input(features)
  → Dense(128, ReLU)
  → Dropout(0.3)
  → Dense(64, ReLU)
  → Dropout(0.3)
  → Dense(output_size, Sigmoid/Softmax)
```

### CNN for Images (28×28)
```python
Input(28, 28, channels)
  → Conv2D(32, 3×3, ReLU)
  → Conv2D(32, 3×3, ReLU)
  → MaxPool(2×2)
  → Conv2D(64, 3×3, ReLU)
  → Conv2D(64, 3×3, ReLU)
  → MaxPool(2×2)
  → Flatten()
  → Dense(128, ReLU)
  → Dropout(0.5)
  → Dense(output_size, Softmax)
```

### LSTM for Sequences
```python
Input(sequence_length, features)
  → LSTM(128, return_sequences=True)
  → LSTM(128)
  → Dense(64, ReLU)
  → Dense(output_size, Softmax/Sigmoid)
```

---

## Step 7: Debugging Guide (Model Not Working?)

### High Training Error (Underfitting)
```
Problem: Model can't learn training data
Solutions:
  ✓ Increase model capacity (more layers, more neurons)
  ✓ Train longer (more epochs)
  ✓ Decrease regularization (lower Dropout)
  ✓ Check learning rate (try 1e-3, 1e-4)
  ✓ Verify data is correct (labels match inputs?)
```

### High Validation Error (Overfitting)
```
Problem: Model memorizes training, fails on new data
Solutions:
  ✓ Add Dropout (0.3-0.5)
  ✓ Add L2 regularization (weight decay)
  ✓ Reduce model capacity (fewer layers, fewer neurons)
  ✓ Get more training data
  ✓ Data augmentation (images: rotate, flip, zoom)
  ✓ Early stopping (stop when validation plateaus)
```

### Training is Slow
```
Problem: Takes forever to train
Solutions:
  ✓ Use GPU (100× speedup)
  ✓ Reduce batch size if memory issue (16, 32, 64)
  ✓ Increase batch size if GPU underutilized (128, 256)
  ✓ Use smaller model (ResNet-18 instead of ResNet-50)
  ✓ Use simpler architecture (Dense instead of CNN if data allows)
```

### Loss is NaN or Exploding
```
Problem: Loss becomes NaN or shoots to infinity
Solutions:
  ✓ Lower learning rate (1e-4 instead of 1e-2)
  ✓ Gradient clipping (clip_norm=1.0)
  ✓ Check for bugs (infinite values in data?)
  ✓ Batch normalization (stabilizes training)
```

---

## Step 8: Quick Decision Flowchart

```
START: What problem are you solving?
   │
   ├─ IMAGES? ──────────────────┐
   │   │                        │
   │   ├─ <10K images ─────► ResNet-18 or VGG-16
   │   ├─ >100K images ────► ResNet-50 or EfficientNet
   │   └─ Need >50 layers ─► ResNet (skip connections REQUIRED)
   │
   ├─ TEXT/SEQUENCES? ──────────┐
   │   │                        │
   │   ├─ Modern NLP ───────► Transformer (BERT, GPT)
   │   ├─ <10K examples ───► LSTM/GRU (simpler)
   │   ├─ Time series ─────► LSTM/GRU
   │   └─ >500 tokens ─────► Transformer (better long-range)
   │
   ├─ TABULAR DATA? ────────────┐
   │   │                        │
   │   ├─ Start with ───────► Dense (2-5 layers)
   │   └─ Alternative ─────► XGBoost (often beats neural nets!)
   │
   └─ MIXED (IMAGE + TABULAR)? ─► Multi-input model (CNN + Dense branches)
```

---

## Key Principles (Memorize These!)

### 1. **Match Architecture to Data Structure**
   - Spatial data (images) → CNN (parameter sharing)
   - Sequential data (text, time) → LSTM or Transformer
   - Unstructured (tabular) → Dense

### 2. **Start Simple, Increase Complexity**
   - Begin with small model (fewer layers, fewer neurons)
   - If underfitting → Increase capacity
   - If overfitting → Decrease capacity or regularize

### 3. **Skip Connections for Depth**
   - >20 layers → Helpful
   - >50 layers → REQUIRED (ResNet-style)
   - Reason: Gradient flow, prevent degradation

### 4. **Powers of 2 for Efficiency**
   - Neurons/Filters: 32, 64, 128, 256, 512
   - Batch sizes: 16, 32, 64, 128, 256
   - GPU hardware optimized for powers of 2

### 5. **ReLU is Default (Hidden Layers)**
   - Don't use Sigmoid in hidden layers (vanishing gradients!)
   - Output layer: Task-dependent (Sigmoid/Softmax/Linear)

### 6. **Transformers vs LSTM (Text)**
   - Modern (2017+): Transformer (faster training, better performance)
   - Legacy or limited compute: LSTM
   - Time series: LSTM still common

### 7. **Transfer Learning When Possible**
   - Images: Use pretrained ResNet, VGG, EfficientNet
   - Text: Use pretrained BERT, GPT-2
   - Fine-tune on your dataset (faster, better results)

---

## Validation Checklist

Before finalizing your architecture, ask:

- [ ] **Did I match architecture to data type?** (Images→CNN, Text→Transformer/LSTM, Tabular→Dense)
- [ ] **Is my model the right size for my dataset?** (Small data→small model, Large data→larger model)
- [ ] **Did I use ReLU in hidden layers?** (Not Sigmoid!)
- [ ] **Is my output activation correct?** (Binary→Sigmoid, Multi-class→Softmax, Regression→Linear)
- [ ] **If >20 layers, did I add skip connections?** (Prevent degradation)
- [ ] **Are neuron/filter counts powers of 2?** (GPU efficiency)
- [ ] **Did I consider transfer learning?** (Pretrained models often better)

---

## Common Mistakes (Avoid These!)

| ❌ **Mistake** | ✅ **Fix** |
|---------------|-----------|
| Using Sigmoid in hidden layers | Use ReLU in hidden layers |
| ResNet-152 on 1,000 images | Match model size to data (ResNet-18 for small data) |
| 30-layer CNN without skip connections | Add skip connections for >20 layers |
| LSTM for images | Use CNN for images (LSTM for sequences) |
| 1 hidden layer with 10,000 neurons | Prefer depth: 5 layers × 128 neurons |
| Inventing custom architecture first | Use proven architectures (ResNet, LSTM, BERT) |

---

## Resources

- **Full Study Guide:** Architecture_Evolution_Study_Guide.md (detailed explanations)
- **Video & Papers:** Further_Reading.md (curated learning materials)
- **Teaching Scripts:** instructor_materials/TEACHING_SCRIPT.md (lecture content)

---

## Quick Lookup: "I have ___, what architecture?"

| **I have...** | **Use this** |
|---------------|--------------|
| 10,000 images of cats/dogs | CNN (ResNet-18 or VGG-16) |
| 100,000 product reviews (text) | BERT (fine-tune pretrained) |
| Stock prices (time series) | LSTM or GRU |
| Customer demographics (CSV) | Dense network (2-5 layers) |
| Selfies + age/gender labels | Multi-input (CNN for image + Dense for labels) |
| Medical scans (X-rays) | CNN (ResNet-50 with transfer learning) |
| Sentences to translate | Transformer (seq2seq) |
| Audio waveforms | 1D CNN or Transformer (Wav2Vec) |
| Video clips (action recognition) | 3D CNN or CNN+LSTM |

---

**Print this sheet and keep it handy during Week 7-8!** 🎯
