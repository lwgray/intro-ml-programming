# Appendix H: keras.applications Reference

Quick reference for all `keras.applications` pretrained models.

---

## Available models (subset)

| Model | Params | Top-1 Acc | Best for |
|---|---|---|---|
| MobileNetV2 | ~3.5M | 71.3% | Mobile, edge, fast iteration |
| MobileNetV3Small | ~2.5M | 67.5% | Even smaller mobile |
| ResNet50 | ~25M | 76.0% | Classic, robust default |
| ResNet101 | ~44M | 77.0% | Higher accuracy version |
| ResNet152 | ~60M | 77.5% | Largest ResNet |
| VGG16 | ~138M | 71.3% | Older, larger; rarely used today |
| VGG19 | ~143M | 71.3% | Deeper VGG |
| EfficientNetB0 | ~5.3M | 77.1% | Modern default |
| EfficientNetB7 | ~66M | 84.3% | Maximum accuracy |
| InceptionV3 | ~24M | 77.9% | Complex but accurate |
| Xception | ~23M | 79.0% | Depthwise separable convs |
| DenseNet121 | ~8M | 75.0% | Dense connectivity pattern |

(Top-1 accuracies on ImageNet validation; subject to slight variation.)

---

## Loading pattern

```python
from keras.applications import MobileNetV2

base = MobileNetV2(
    input_shape=(160, 160, 3),  # any size; 224×224 is standard ImageNet
    include_top=False,           # remove ImageNet classifier head
    weights='imagenet',          # load pretrained weights
    pooling=None,                # 'avg' would add GlobalAveragePooling
)
```

---

## Required preprocess_input per model

```python
# MobileNetV2 / MobileNetV3
from keras.applications.mobilenet_v2 import preprocess_input
# Range: [-1, 1]; transforms via (x / 127.5) - 1

# ResNet50, ResNet101, ResNet152
from keras.applications.resnet50 import preprocess_input
# Range: caffe-style ZCA; subtracts ImageNet mean per channel

# EfficientNet (B0-B7)
from keras.applications.efficientnet import preprocess_input
# Range: [0, 255]; layers handle normalization internally

# VGG16, VGG19
from keras.applications.vgg16 import preprocess_input
# Range: caffe-style; subtracts ImageNet mean
```

⚠️ **Always use the matching `preprocess_input`.** Wrong preprocess = near-random accuracy.

---

## Standard transfer learning pattern

```python
# Phase 1: frozen base + new head
base = MobileNetV2(include_top=False, weights='imagenet', input_shape=(160, 160, 3))
base.trainable = False

inputs = keras.Input(shape=(160, 160, 3))
x = preprocess_input(inputs)
x = base(x, training=False)
x = keras.layers.GlobalAveragePooling2D()(x)
x = keras.layers.Dropout(0.3)(x)
outputs = keras.layers.Dense(num_classes, activation='softmax')(x)

model = keras.Model(inputs, outputs)
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(train_ds, validation_data=test_ds, epochs=10)
```

---

## Phase 2: fine-tuning

```python
# Unfreeze top N layers
base.trainable = True
for layer in base.layers[:-30]:  # unfreeze top 30
    layer.trainable = False

# Add augmentation, rebuild
data_aug = keras.Sequential([
    layers.RandomFlip('horizontal'),
    layers.RandomRotation(0.1),
    layers.RandomZoom(0.1),
])

inputs = keras.Input(shape=(160, 160, 3))
x = data_aug(inputs)
x = preprocess_input(x)
x = base(x, training=False)  # KEEP this False even when unfrozen
x = layers.GlobalAveragePooling2D()(x)
x = layers.Dropout(0.3)(x)
outputs = layers.Dense(num_classes, activation='softmax')(x)
model = keras.Model(inputs, outputs)

# CRITICAL: low LR
model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=1e-5),
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
model.fit(train_ds, validation_data=test_ds, epochs=10)
```

---

## Choosing a backbone

Decision tree:
1. **Mobile/edge deployment?** → MobileNetV2 or MobileNetV3
2. **Latency-critical inference?** → MobileNet or EfficientNetB0
3. **Server, no constraints, max accuracy?** → ResNet50 or EfficientNetB3+
4. **Research / experimentation?** → EfficientNet family (B0-B7 = small to large)
5. **Specific architecture mentioned in your project?** → Use whatever the team uses

---

## Common errors

| Error | Cause | Fix |
|---|---|---|
| Stuck at chance | Forgot `preprocess_input` | Import matching one |
| Phase 2 accuracy crashes | Default LR | `Adam(learning_rate=1e-5)` |
| Wrong input shape | Using wrong default | Set `input_shape=(N, N, 3)` explicitly |
| BatchNorm drift | Lost `training=False` | Always pass `training=False` to base model |
| Weights download fails | Network / firewall | Pre-cache; distribute via shared drive |

---

## Cache locations

By default, weights are cached at:
- Linux/Mac: `~/.keras/models/`
- Windows: `%USERPROFILE%\.keras\models\`

To pre-distribute: zip the cache directory and share. Students extract to their own `~/.keras/`.

---

## Domain-specific alternatives (worth knowing)

For specialized domains where ImageNet doesn't transfer well:
- **Medical imaging:** RadImageNet, MedNet
- **Satellite:** EarthNet, BigEarthNet pretrained models
- **Microscopy:** Specific microscopy pretrained models from Bioimaging
- **Document images:** LayoutLM, Donut

These aren't in `keras.applications` but are available on Hugging Face Hub.

---

## See also

- `Week9_Transfer_Learning_Cheat_Sheet.md` — student-facing cheat sheet
- `Section6_Live_Coding_Reference.md` — line-by-line code
- `Week9_DeepDive_FineTuning_Learning_Rate.md` — why low LR matters
