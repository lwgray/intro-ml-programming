# Week 9 Glossary

---

## Core Concepts

**Pretrained model**
A model already trained on a large dataset (typically ImageNet for vision), made available with its learned weights. We reuse those weights instead of starting from random.

**Foundation model**
General term for a large pretrained model used as a starting point. ImageNet-pretrained CNNs are foundation models for vision; LLMs are foundation models for language (Week 11).

**Backbone (or Feature Extractor)**
The part of a transfer learning setup that converts images into feature vectors. Usually a pretrained CNN with its classifier head removed.

**Classifier head**
The new task-specific layers added on top of the backbone. Typically `GlobalAveragePooling2D + Dropout + Dense(num_classes, softmax)`.

**Feature extraction (Phase 1)**
Transfer learning regime: freeze entire pretrained base, train only a new classifier head. Fast, works with very small data.

**Fine-tuning (Phase 2)**
Transfer learning regime: also unfreeze the top layers of the base and train them with a low learning rate. Slower, can yield higher accuracy.

**Transfer learning**
The general practice of reusing knowledge from one task on another. Specifically (in this course): starting from pretrained model weights and adapting them.

**Frozen weights**
Layer weights that don't update during training. Set with `layer.trainable = False`. The forward pass still happens; only backprop is skipped for that layer.

**Trainable weights**
Layer weights that DO update during training. The default; opposite of frozen.

**Catastrophic forgetting**
What happens when you fine-tune with too high a learning rate — the pretrained features get destroyed. Why we use 1e-5 instead of 1e-3.

**Domain shift / Domain mismatch**
When your target data is significantly different from the source data (ImageNet for our case). Pretrained features transfer less well; may need more aggressive fine-tuning.

---

## Data Augmentation

**Data augmentation**
Random transformations applied to training images to create synthetic variety. Combats overfitting on small datasets.

**Keras preprocessing layers**
Built-in augmentation layers (`RandomFlip`, `RandomRotation`, `RandomZoom`, etc.) that auto-disable during inference.

**Inside-the-model vs outside-the-model augmentation**
- **Inside:** Augmentation layers inside `keras.Model`. Saves with the model, runs on GPU, auto-disables in inference. Modern practice.
- **Outside:** Augmentation in the data pipeline (`tf.data` pipeline). More control but more setup.

---

## Pretrained Model Vocabulary

**`keras.applications`**
Keras submodule providing pretrained CNN architectures (MobileNetV2, ResNet50, EfficientNet, etc.).

**`include_top=False`**
Argument to load the pretrained backbone WITHOUT its 1000-class ImageNet classifier head. Almost always what you want when transfer learning.

**`weights='imagenet'`**
Argument to load weights pretrained on ImageNet. Set to `None` to start from random initialization.

**`preprocess_input`**
Model-specific input normalization function. Different per architecture (MobileNetV2 expects `[-1, 1]`; ResNet50 expects caffe-style; EfficientNet expects `[0, 255]` and handles it internally). Always import from the matching submodule.

**`GlobalAveragePooling2D`**
Layer that reduces each feature map to a single value (its mean). Output shape: `(batch, num_filters)`. Modern alternative to `Flatten + Dense`.

---

## Modern CV Applications (concepts only)

**Object detection**
Detect MULTIPLE objects in an image with bounding boxes and class labels. Architectures: YOLO, Faster R-CNN, DETR. Library: `ultralytics`.

**Semantic segmentation**
Per-pixel classification: every pixel gets a class label. Architectures: U-Net, DeepLab. Use case: medical imaging.

**Instance segmentation**
Per-pixel + per-instance: distinguish individual instances of the same class. Architecture: Mask R-CNN.

**CLIP (Contrastive Language-Image Pretraining)**
OpenAI model that maps images and text into a shared embedding space. Enables zero-shot classification: classify into ANY classes specified in text. Foundation for text-to-image models (Week 11).

**Zero-shot classification**
Classifying into classes not seen during training. CLIP enables this for images by projecting images into a text-aligned embedding space.

---

## From Earlier Weeks (Still Relevant)

**`keras.Sequential`** / **functional API** (`keras.Model(inputs, outputs)`)
For transfer learning, prefer the functional API — it composes more cleanly with pretrained models than Sequential.

**`model.compile(optimizer, loss, metrics)`**
Required after changing `trainable` status. Always recompile.

**`model.fit(...)`**
Same as before. Pretrained models train the same way.

**`EarlyStopping`** / **`ModelCheckpoint`** (Week 7 callbacks)
Same callbacks work here. Especially useful with fine-tuning.

**`Dropout`** (Week 7)
Used in the classifier head, just like Week 8.

**Sparse categorical crossentropy**
Same loss as Weeks 6-8 for integer-label classification.

---

## Continuing into Week 10

**Hugging Face**
The dominant ecosystem for transformers and NLP models. Equivalent of `keras.applications` for transformer architectures.

**`from_pretrained`**
Hugging Face equivalent of `keras.applications.X(weights='imagenet')`. Loads a pretrained model.

**Tokenizer**
Converts text to integer token IDs (Week 10). Each model has a matching tokenizer.

**Transformer**
The architecture family that dominates modern NLP (Week 10). Built on attention.

---

## Common Misconceptions

**"Bigger pretrained model is always better."**
False. For small datasets, smaller models (MobileNet) often outperform giant ones (huge EfficientNet) because there's less to overfit.

**"Transfer learning only works for similar tasks."**
Mostly false. Even very different tasks often benefit from ImageNet pretraining because the low-level features (edges, textures) are universal.

**"Fine-tuning means unfreeze everything and retrain."**
False. Fine-tuning means selectively unfreezing TOP layers and training at LOW LR. Unfreezing everything with default LR causes catastrophic forgetting.

**"You need a GPU for transfer learning."**
For Phase 1 (frozen base): no — only the small head trains. For Phase 2: yes, practically.

---

**Version:** Week 9 Glossary v1.0 | April 2026
