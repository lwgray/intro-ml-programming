"""Bake the weeks 8-9 datasets and pretrained weights into the image.

The flowers/ 5-class subset ships in the repo itself; everything else lands in
the KERAS_HOME / HF_HOME caches set image-wide.
"""

from keras.datasets import cifar10, fashion_mnist, mnist

mnist.load_data()
fashion_mnist.load_data()  # weeks 8-9
cifar10.load_data()        # weeks 8-9

# Pretrained backbones: live session + phase 2 use MobileNetV2 at 160 and the
# default 224; pair programming compares ResNet50 and EfficientNetB0; Xception
# appears in the appendix. Keras weight files are per-resolution for MobileNetV2.
from keras.applications import EfficientNetB0, MobileNetV2, ResNet50, Xception

MobileNetV2(input_shape=(160, 160, 3), include_top=False, weights='imagenet')
MobileNetV2(input_shape=(224, 224, 3), include_top=False, weights='imagenet')
ResNet50(include_top=False, weights='imagenet')
EfficientNetB0(include_top=False, weights='imagenet')
Xception(include_top=False, weights='imagenet')

# Week 9 day 2 CLIP demo
from transformers import CLIPModel, CLIPProcessor

CLIPModel.from_pretrained('openai/clip-vit-base-patch32')
CLIPProcessor.from_pretrained('openai/clip-vit-base-patch32')

# Week 9 phase-2 companion downloads cats-vs-dogs parquet shards from this repo
from huggingface_hub import snapshot_download

snapshot_download('Bingsu/Cat_and_Dog', repo_type='dataset')

print('vision prefetch complete')
