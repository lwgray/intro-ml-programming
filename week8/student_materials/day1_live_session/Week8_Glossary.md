# Week 8 Glossary

Quick reference for Week 8 vocabulary. Bookmark this for the rest of the DNN block.

---

## Core CNN Concepts

**Convolution**
Sliding a small filter across an image, computing a dot product at each position. The result is a feature map showing where the filter's pattern was detected.

**Filter (also: Kernel)**
A small grid of learnable weights (e.g., 3×3 or 5×5) that acts as a pattern detector. Each Conv2D layer learns multiple independent filters.

**Feature Map**
The output of one filter applied across the input. Same spatial extent as input (with `padding='same'`), with values indicating where the filter's pattern occurred.

**Stride**
How far the filter moves between positions. Stride 1 = touch every pixel. Stride 2 = skip every other position (also downsamples).

**Padding**
- `'valid'` (default): no padding; output is smaller than input
- `'same'`: zero-pad the input so output matches input spatial dimensions
Use `'same'` to preserve resolution; use `'valid'` when intentional shrinking is fine.

**Pooling**
Downsampling operation. **Max pooling** takes the maximum value in each region (most common). **Average pooling** takes the mean. Encodes translation invariance.

**Receptive field**
The region of input that influences a given output unit. Grows with depth — a unit in layer 3 "sees" a larger input region than a unit in layer 1.

**Parameter sharing**
The same filter weights are applied at every spatial position. One 3×3 filter has 9 weights regardless of image size. This is why CNNs are parameter-efficient compared to MLPs.

**Translation invariance**
The network gives similar outputs whether the object is at the left, right, or center of the image. Pooling and parameter sharing both contribute to this.

---

## Architecture Patterns

**CNN architecture pattern**
The standard layout: `Conv → ReLU → Pool → Conv → ReLU → Pool → ... → Flatten → Dense → Softmax`. The conv blocks extract spatial features; the dense head classifies based on those features.

**Conv block**
Conventional name for `Conv2D + ReLU + MaxPooling2D` (sometimes with BatchNormalization mixed in). Building unit of most CNNs.

**Channel dimension**
The 4th axis of a CNN input/feature map. For grayscale images: 1 channel. For RGB: 3 channels. For deeper feature maps: as many channels as the previous layer had filters.

**Flatten**
Layer that converts a multi-dimensional feature map into a flat 1D vector for the classifier head. Used once, near the end of a CNN.

**GlobalAveragePooling2D (GAP)**
Alternative to Flatten + Dense. Reduces each feature map to a single value (its mean). Output shape: `(batch, num_filters)`. More parameter-efficient than Flatten — used in modern architectures (ResNet, EfficientNet).

---

## Architecture History (high-level only)

**LeNet (1998, Yann LeCun)**
The first practical CNN. Recognized handwritten digits. Established the Conv → Pool → Conv → Pool → Dense pattern.

**AlexNet (2012, Krizhevsky et al.)**
Won ImageNet 2012 by a huge margin. Top-5 error 26% → 15%. Sparked the deep learning revolution.

**VGG (2014)**
Made the case for depth. 16-19 layers of stacked 3×3 conv blocks. Simple, uniform architecture.

**ResNet (2015, He et al.)**
Introduced skip connections (residual blocks). Made it possible to train networks with hundreds of layers. Still in production today.

**EfficientNet (2019, Tan & Le)**
Scaled depth, width, and resolution together. Excellent accuracy-per-parameter. Common choice for production deployment.

---

## Keras Layers and Functions

**`keras.layers.Conv2D(filters, kernel_size, ...)`**
The 2D convolution layer. `filters` is how many filters to learn; `kernel_size` is filter dimensions (e.g., 3 or `(3, 3)`).

**`keras.layers.MaxPooling2D(pool_size)`**
Max pooling layer. Default `pool_size=2` halves spatial dimensions.

**`keras.layers.AveragePooling2D(pool_size)`**
Average pooling alternative. Less common than max for classification.

**`keras.layers.Flatten()`**
Converts spatial feature maps to flat vector. Used before Dense in classification heads.

**`keras.layers.GlobalAveragePooling2D()`**
Global average pooling. Reduces each feature map to one value.

**`np.expand_dims(X, axis=-1)`**
Adds the channel dimension to a grayscale image array. Required for Conv2D input.

---

## From Earlier Weeks (Still Relevant)

**`keras.Sequential`**
Linear stack of layers (Week 6). Same API for CNNs.

**`model.compile(optimizer, loss, metrics)`**
Configure training (Week 6). Same for CNNs.

**`model.fit(X, y, epochs, batch_size, validation_split)`**
Train the model (Week 6). Same for CNNs.

**Dropout**
Regularization technique (Week 7). Used in CNN classifier heads.

**EarlyStopping**
Callback that stops training when validation stops improving (Week 7). Reused in Week 8.

**`sparse_categorical_crossentropy`**
Loss function for multi-class classification with integer labels (Week 6-7). Reused in Week 8.

**`adam`**
Adaptive optimizer (Week 6). Default optimizer for CNNs too.

---

## Continuing into Week 9

**Pretrained model**
A model already trained on a large dataset, used as a starting point for a new task. Coming Week 9.

**Transfer learning**
Reusing knowledge from one task on another. Specifically: starting from pretrained model weights and adapting them. Coming Week 9.

**ImageNet**
The 14-million-image dataset most pretrained CV models are trained on. Sets the standard for general visual features.

**Backbone / Feature extractor**
The pretrained part of a transfer learning setup that extracts features from images. Coming Week 9.

---

## Common Misconceptions (Already Addressed)

**"CNNs are black boxes."**
False. You can SEE what each filter learned. We did this in Section 4.

**"More layers always means better."**
False. Deeper networks need more data and can overfit. The right depth matches your data.

**"CNNs are only for images."**
Mostly true for classical CNNs, but 1D conv works for audio/time series, 3D conv for video. For text, transformers (Week 10) generally beat CNNs.

**"You should use the biggest model possible."**
False. Choose the smallest model that captures your task's complexity. Bigger costs more compute, more data, more inference latency.

---

**Version:** Week 8 Glossary v1.0 | April 2026
