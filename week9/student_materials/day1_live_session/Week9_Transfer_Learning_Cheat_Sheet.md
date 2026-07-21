# Week 9 Transfer Learning Cheat Sheet

---

## Quick reference: load any pretrained model

```python
from keras.applications import MobileNetV2, ResNet50, EfficientNetB0
from keras.applications.mobilenet_v2 import preprocess_input as mobilenet_preprocess
from keras.applications.resnet50 import preprocess_input as resnet_preprocess
from keras.applications.efficientnet import preprocess_input as efficientnet_preprocess

# Load with frozen base
base = MobileNetV2(input_shape=(160, 160, 3), include_top=False, weights='imagenet')
base.trainable = False
```

---

## Phase 1 template: Frozen base + new head

```python
inputs = keras.Input(shape=(160, 160, 3))
x = preprocess_input(inputs)        # Critical — model-specific normalization
x = base(x, training=False)         # training=False keeps BN in inference mode
x = layers.GlobalAveragePooling2D()(x)
x = layers.Dropout(0.3)(x)
outputs = layers.Dense(num_classes, activation='softmax')(x)

model = keras.Model(inputs, outputs)
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train just the head
history = model.fit(train_ds, validation_data=test_ds, epochs=10)
```

**Result:** Usually 85-95% accuracy on small datasets in seconds-to-minutes.

---

## Phase 2 template: Fine-tune top layers + augmentation

```python
# Step 1: Unfreeze top N layers (keep bottom frozen)
base.trainable = True
N = 30  # number of top layers to fine-tune
for layer in base.layers[:-N]:
    layer.trainable = False

# Step 2: Add augmentation to the model
data_aug = keras.Sequential([
    layers.RandomFlip('horizontal'),
    layers.RandomRotation(0.1),
    layers.RandomZoom(0.1),
])

# Step 3: Rebuild with augmentation
inputs = keras.Input(shape=(160, 160, 3))
x = data_aug(inputs)
x = preprocess_input(x)
x = base(x, training=False)         # Keep BN in inference mode!
x = layers.GlobalAveragePooling2D()(x)
x = layers.Dropout(0.3)(x)
outputs = layers.Dense(num_classes, activation='softmax')(x)

model = keras.Model(inputs, outputs)

# Step 4: Compile with VERY LOW learning rate
model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=1e-5),  # 100× lower than default!
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Step 5: Train
history = model.fit(train_ds, validation_data=test_ds, epochs=10)
```

**Result:** Usually +1-5% over Phase 1.

---

## Loading data from folders

```python
train_ds = keras.utils.image_dataset_from_directory(
    'path/to/train',
    image_size=(160, 160),
    batch_size=32,
    label_mode='int',
    seed=42
)

# Folder structure expected:
# path/to/train/
#   classA/
#     img1.jpg
#     img2.jpg
#   classB/
#     ...

class_names = train_ds.class_names  # Inferred from folder names
```

---

## Choosing a backbone

| Backbone | Params | Speed | When to use |
|---|---|---|---|
| MobileNetV2 | ~3.5M | Fastest | Mobile, edge, fast iteration |
| EfficientNetB0 | ~5.3M | Fast | Balanced default |
| ResNet50 | ~25M | Medium | Server, traditional choice |
| EfficientNetB7 | ~66M | Slow | Maximum accuracy if compute allows |
| VGG16 | ~138M | Slow | Older; rarely needed today |

---

## Common preprocess_input requirements

| Backbone | Expected input range | Special notes |
|---|---|---|
| MobileNetV2 | `[-1, 1]` | `(x / 127.5) - 1` |
| ResNet50 | Caffe-style ZCA | Subtract ImageNet mean per channel |
| EfficientNet | `[0, 255]` | Layers handle normalization internally |
| VGG16 | Caffe-style | Subtract ImageNet mean |

**Always use the matching `preprocess_input` from the model's submodule.** Wrong preprocess = near-random accuracy.

---

## Augmentation recipes

**Mild (typical):**
```python
data_aug = keras.Sequential([
    layers.RandomFlip('horizontal'),
    layers.RandomRotation(0.1),
    layers.RandomZoom(0.1),
])
```

**Aggressive (for very small data):**
```python
data_aug = keras.Sequential([
    layers.RandomFlip('horizontal'),
    layers.RandomRotation(0.2),
    layers.RandomZoom(0.2),
    layers.RandomContrast(0.1),
    layers.RandomBrightness(0.1),
])
```

**For orientation-sensitive data (medical, X-ray):**
```python
data_aug = keras.Sequential([
    # NO RandomFlip — left/right matters
    layers.RandomRotation(0.05),  # very mild
    layers.RandomZoom(0.05),
])
```

---

## Saving and loading

```python
# Save the entire model (including augmentation layers and pretrained backbone)
model.save('my_transfer_model.keras')

# Load later
loaded = keras.models.load_model('my_transfer_model.keras')

# At inference time, augmentation auto-disables — outputs match what you'd see in production
```

---

## Common error → fix table

| Error | Likely cause | Fix |
|---|---|---|
| Accuracy at chance level | Forgot `preprocess_input` | Import and use the matching one |
| `AttributeError: 'NoneType'` | Functional API miswired | Check each `x = layer(x)` |
| `OOM error` | Batch too large | Reduce batch size or image size |
| Phase 2 accuracy plummets | LR too high | Use `Adam(learning_rate=1e-5)` |
| Different results each run | No random seed | `keras.utils.set_random_seed(42)` |
| Wrong `class_names` | Hidden folders or extra dirs | Clean directory; pass `class_names=[...]` |

---

## Inference recipe (after training)

```python
import numpy as np
from PIL import Image

img = Image.open('test_image.jpg').resize((160, 160))
img_array = np.array(img)[np.newaxis, ...]  # Add batch dim: (1, 160, 160, 3)

predictions = model.predict(img_array)
predicted_class_idx = np.argmax(predictions[0])
predicted_class = class_names[predicted_class_idx]
confidence = predictions[0][predicted_class_idx]

print(f'{predicted_class} ({confidence:.2%})')
```

---

## What's coming in Week 10

```python
# Sneak peek of the Week 10 pattern
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained('distilbert-base-uncased')
model = AutoModelForSequenceClassification.from_pretrained(
    'distilbert-base-uncased',
    num_labels=4
)
# ... fine-tune on text
```

Same `from_pretrained` pattern. Different framework (Hugging Face). Different architecture (transformer instead of CNN).

---

**Version:** Week 9 Cheat Sheet v1.0 | April 2026
