"""Bake the week 11 model weights (HF_HOME cache) into the image.

This is the whole point of the per-week launchable: Phi-3-mini + Stable
Diffusion 1.5 never download on class day. LLM weights are fetched with
snapshot_download (no RAM cost in CI); Stable Diffusion goes through
from_pretrained because its repo also carries ~25 GB of .ckpt/variant files a
blind snapshot would pull in.
"""

from huggingface_hub import snapshot_download

# Day 1 LLM + the day 2 lighter alternative
snapshot_download('microsoft/Phi-3-mini-4k-instruct',
                  ignore_patterns=['*.gguf', '*.onnx*', 'onnx/*'])
snapshot_download('Qwen/Qwen2.5-0.5B-Instruct',
                  ignore_patterns=['*.gguf', '*.onnx*', 'onnx/*'])

# Stable Diffusion 1.5 — the maintained sd-legacy mirror (runwayml is gone)
from diffusers import StableDiffusionPipeline

StableDiffusionPipeline.from_pretrained('sd-legacy/stable-diffusion-v1-5')

# Day 2 composing app pairs the generative models with a sentiment classifier
from transformers import pipeline

try:
    pipeline('sentiment-analysis')
except Exception as e:
    print(f'skipping pipeline(sentiment-analysis) prefetch: {e}')

print('week11 prefetch complete')
