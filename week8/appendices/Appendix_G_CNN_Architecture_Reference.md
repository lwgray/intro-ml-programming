# Appendix G: CNN Architecture Reference

Quick reference for all CNN-related Keras concepts from Week 8.

---

## Conv2D

```python
keras.layers.Conv2D(
    filters,         # number of output channels (= number of filters)
    kernel_size,     # tuple or int — filter dimensions (e.g., 3 or (3, 3))
    strides=1,       # how far the filter moves per step
    padding='valid', # 'valid' (no padding) or 'same' (preserve dimensions)
    activation=None, # often 'relu' is passed inline
)
```

**Examples:**
```python
Conv2D(32, 3)                                    # 32 filters, 3×3 kernel, no padding, no activation
Conv2D(32, 3, activation='relu', padding='same') # typical pattern
Conv2D(64, kernel_size=(5, 5), strides=2)        # 5×5 kernel, stride 2 (downsamples)
```

---

## MaxPooling2D

```python
keras.layers.MaxPooling2D(
    pool_size=2,    # 2×2 region (default)
    strides=None,   # default to pool_size — non-overlapping
    padding='valid',
)
```

**Common usage:**
```python
MaxPooling2D(2)        # halves spatial dimensions
MaxPooling2D((3, 3))   # 3×3 region (less common)
```

---

## AveragePooling2D

```python
keras.layers.AveragePooling2D(pool_size=2)
```

Average instead of max. Less common for classification.

---

## Flatten

```python
keras.layers.Flatten()
```

Reshapes (N, H, W, C) → (N, H×W×C). Used once before the classifier head.

---

## GlobalAveragePooling2D

```python
keras.layers.GlobalAveragePooling2D()
```

Reduces (N, H, W, C) → (N, C) by taking the mean over each feature map. Modern alternative to Flatten + Dense. Fewer parameters.

---

## Standard CNN architectures (reference)

### Small CNN (Fashion-MNIST)
```
Conv2D(32, 3) → MaxPool(2) → Conv2D(32, 3) → MaxPool(2) → Flatten → Dense(64) → Dropout(0.3) → Dense(10)
```
~111K parameters

### VGG-style (CIFAR-10)
```
Conv2D(32, 3) → Conv2D(32, 3) → MaxPool(2)
Conv2D(64, 3) → Conv2D(64, 3) → MaxPool(2)
Flatten → Dense(128) → Dropout(0.5) → Dense(10)
```
~550K parameters

### Modern with GAP
```
Conv2D(32, 3) → MaxPool(2)
Conv2D(64, 3) → MaxPool(2)
Conv2D(128, 3) → GlobalAveragePooling2D
Dense(10)
```
~150K parameters

---

## Output dimension formulas

For input dimension `H_in`, kernel `k`, stride `s`, padding `p`:

```
H_out = (H_in + 2p - k) / s + 1
```

**Common cases:**
- Conv2D(filters, 3, padding='same'): `H_out = H_in`
- Conv2D(filters, 3, padding='valid'): `H_out = H_in - 2`
- MaxPooling2D(2): `H_out = H_in / 2`

---

## Parameter count formulas

### Conv2D
```
params = (kernel_h × kernel_w × input_channels × num_filters) + num_filters
                                                                  ↑ biases
```

Example (our 2nd conv): Conv2D(32, 3) on (14, 14, 32) input = 3×3×32×32 + 32 = 9,248

### Dense
```
params = (input_size × output_size) + output_size
```

Example (our dense head): Dense(64) after Flatten of (7, 7, 32) = 1568 × 64 + 64 = 100,416

### Pooling, Flatten, GlobalAveragePooling2D, Dropout
Zero parameters.

---

## Common patterns

### Doubling filters with each block
```
Conv2D(32) → Pool → Conv2D(64) → Pool → Conv2D(128) → Pool
```
Standard pattern: each pool halves spatial dims; doubling filters keeps representation roughly constant.

### Using `padding='same'`
Default if you want to preserve spatial dimensions. Almost always paired with `stride=1`.

### When to use stride=2 instead of pooling
Some architectures (ResNet) use strided conv as downsampling. Slightly more parameters than pooling but more learnable.

---

## Pretrained models in `keras.applications` (preview Week 9)

```python
from keras.applications import (
    MobileNetV2,    # small, fast, mobile-friendly
    ResNet50,       # classic, robust
    EfficientNetB0, # modern, optimized
    VGG16,          # older, larger
    InceptionV3,    # complex architecture
)

# Common pattern
base = MobileNetV2(input_shape=(224, 224, 3), include_top=False, weights='imagenet')
```

`include_top=False` removes the ImageNet 1000-class classifier head. `weights='imagenet'` loads pretrained weights.

---

## Visualization recipes

### Plot first-layer filters
```python
filters, _ = model.layers[0].get_weights()
filters = (filters - filters.min()) / (filters.max() - filters.min())

fig, axes = plt.subplots(4, 8, figsize=(12, 6))
for i, ax in enumerate(axes.flat):
    if i < filters.shape[-1]:
        ax.imshow(filters[:, :, 0, i], cmap='gray')
    ax.axis('off')
plt.show()
```

### Plot feature maps
```python
feature_extractor = keras.Model(
    inputs=model.inputs,
    outputs=model.layers[N].output  # pick a layer index
)
feature_maps = feature_extractor.predict(image[np.newaxis, ...])

fig, axes = plt.subplots(4, 8, figsize=(12, 6))
for i, ax in enumerate(axes.flat):
    if i < feature_maps.shape[-1]:
        ax.imshow(feature_maps[0, :, :, i], cmap='viridis')
    ax.axis('off')
plt.show()
```

---

## Common errors → fixes

| Error | Cause | Fix |
|---|---|---|
| `expected min_ndim=4` | Channel dim missing | `np.expand_dims(X, -1)` |
| Negative output dim | Too many `valid` pools | `padding='same'` |
| OOM during training | Batch size too big | `batch_size=32` |
| Stuck at chance accuracy | Pixels not normalized | `X.astype('float32') / 255.0` |
| Loss NaN | LR too high | Default Adam (1e-3) usually fine |

---

## Architecture history (1-line summary)

- **LeNet (1998):** First practical CNN
- **AlexNet (2012):** Deep learning revolution starts
- **VGG (2014):** Depth via stacked 3×3 convs
- **ResNet (2015):** Skip connections, 100+ layers
- **EfficientNet (2019):** Optimized depth/width/resolution scaling

See `instructor_materials/deep_dives/Week8_DeepDive_Architecture_History.md` for instructor depth.
