# Week 11 Generative AI Cheat Sheet

---

## Setup

```bash
pip install transformers diffusers accelerate
```

---

## Loading a small LLM (local)

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# GPU, Apple Silicon (MPS), or CPU — no code changes needed
DEVICE = 'cuda' if torch.cuda.is_available() else ('mps' if torch.backends.mps.is_available() else 'cpu')
MODEL = 'microsoft/Phi-3-mini-4k-instruct'  # or 'Qwen/Qwen2.5-0.5B-Instruct'

tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForCausalLM.from_pretrained(
    MODEL,
    dtype=torch.float16 if DEVICE in ('cuda', 'mps') else torch.float32,  # v5: 'dtype' (was 'torch_dtype')
    device_map='auto' if DEVICE == 'cuda' else None,
    # No trust_remote_code: transformers v5 has native Phi-3/Qwen support; the models'
    # old bundled code crashes on v5 (KeyError: 'type' in rope init).
)
if DEVICE != 'cuda':   # cuda placed by device_map='auto'; mps/cpu need an explicit move
    model = model.to(DEVICE)
```

---

## Generation function

```python
def generate(prompt, max_new_tokens=120, temperature=0.7, top_p=0.9):
    messages = [{'role': 'user', 'content': prompt}]
    # v5: apply_chat_template returns a BatchEncoding (not a tensor) — use return_dict=True
    # and unpack with generate(**inputs).
    inputs = tokenizer.apply_chat_template(
        messages,
        return_tensors='pt',
        add_generation_prompt=True,
        return_dict=True,
    ).to(DEVICE)
    
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            temperature=temperature,
            top_p=top_p,
            do_sample=temperature > 0,
            pad_token_id=tokenizer.eos_token_id,
        )
    
    return tokenizer.decode(outputs[0][inputs['input_ids'].shape[1]:], skip_special_tokens=True)
```

---

## Prompting patterns

### Zero-shot
```python
generate('Classify as positive or negative: "Great product!"')
```

### Few-shot
```python
prompt = '''Classify reviews. Examples:
"Love it!" -> POSITIVE
"Terrible." -> NEGATIVE

Now: "Eh, it's fine." ->'''
generate(prompt, max_new_tokens=10)
```

### Structured output (JSON)
```python
prompt = '''Extract product info as JSON.
Message: "I bought the iPhone 15 Pro for $999."
Return ONLY valid JSON with keys: product, price.'''
generate(prompt, max_new_tokens=60, temperature=0.1)  # low temp for determinism
```

### System prompt + user message
```python
messages = [
    {'role': 'system', 'content': 'You are a helpful assistant. Always respond in exactly 1 sentence.'},
    {'role': 'user', 'content': 'What is machine learning?'}
]
inputs = tokenizer.apply_chat_template(messages, return_tensors='pt', add_generation_prompt=True, return_dict=True).to(DEVICE)
# generate as before — model.generate(**inputs, ...)
```

---

## Temperature reference

| Temperature | Behavior | Use case |
|---|---|---|
| 0.0 | Deterministic, picks highest probability | Factual extraction, structured output |
| 0.3 | Mostly deterministic, slight variation | Standard Q&A, code |
| 0.7 | Default — creative but coherent | General chat, summarization |
| 1.0+ | Very creative, can go off-rails | Brainstorming, fiction |

---

## Stable Diffusion

```python
from diffusers import StableDiffusionPipeline
import torch

DEVICE = 'cuda' if torch.cuda.is_available() else ('mps' if torch.backends.mps.is_available() else 'cpu')

# 'sd-legacy' is HF's maintained mirror of SD v1.5. diffusers still uses `torch_dtype`
# (only transformers v5 renamed it). Use float16 ONLY on CUDA — on MPS/CPU, fp16 SD can
# produce black images, so use float32 there.
pipe = StableDiffusionPipeline.from_pretrained(
    'sd-legacy/stable-diffusion-v1-5',
    torch_dtype=torch.float16 if DEVICE == 'cuda' else torch.float32,
).to(DEVICE)

# Disable safety checker for speed (re-enable for production)
pipe.safety_checker = None
if DEVICE == 'mps':
    pipe.enable_attention_slicing()   # smooths MPS memory spikes

# Generate image
image = pipe(
    prompt='a cat wearing a top hat, photorealistic',
    negative_prompt='watermark, text, low quality',
    num_inference_steps=20,        # 20-50 typical
    guidance_scale=7.5,            # 7-9 typical
    height=512, width=512,         # 512×512 default
).images[0]
image.save('output.png')
```

### Stable Diffusion parameters

| Parameter | Typical | Effect |
|---|---|---|
| `num_inference_steps` | 20-50 | More = better quality but slower |
| `guidance_scale` | 7-9 | More = follows prompt more strictly |
| `height`, `width` | 512×512 | Larger = slower, more memory |
| `negative_prompt` | varies | What you DON'T want |
| `seed` | random | Reproducible outputs |

---

## Image generation prompt engineering

**Structure:** `subject, style, modifiers, quality terms`

**Examples:**
- Bad: `a city`
- Better: `a futuristic city, neon lights, cyberpunk style, photorealistic, 8k`
- Watercolor style: `a futuristic city, watercolor painting, soft pastels, dreamy`
- Photo-realistic: `..., photorealistic, sharp focus, professional photography`

**Negative prompts (common):**
- `watermark, text, signature` (clean output)
- `blurry, low quality, distorted` (sharpness)
- `extra limbs, deformed` (for character generation)

---

## Memory management

**Loading both LLM and Stable Diffusion will OOM on most GPUs.** Free memory between sections:

```python
import torch

# Free LLM before loading SD
import gc
del model
gc.collect()
if DEVICE == 'cuda':
    torch.cuda.empty_cache()
elif DEVICE == 'mps':
    torch.mps.empty_cache()

# Load SD
pipe = StableDiffusionPipeline.from_pretrained(...)
```

**Low-memory mode for SD:**
```python
pipe.enable_attention_slicing()  # ~30% slower but uses less memory
pipe.enable_model_cpu_offload()  # Move parts to CPU when not in use
```

---

## Hugging Face Inference API (fallback if local doesn't work)

```python
import os
import requests

HF_TOKEN = os.environ['HF_TOKEN']  # get from huggingface.co/settings/tokens

# Text generation
response = requests.post(
    'https://api-inference.huggingface.co/models/microsoft/Phi-3-mini-4k-instruct',
    headers={'Authorization': f'Bearer {HF_TOKEN}'},
    json={'inputs': 'Once upon a time'}
)
print(response.json())
```

Free tier rate-limited but works for individual exploration.

---

## Combining models (the post-class app pattern)

```python
from transformers import pipeline

sentiment = pipeline('sentiment-analysis')
ner = pipeline('ner', aggregation_strategy='simple')
# llm: load Phi-3 as above

def process_email(email_text):
    mood = sentiment(email_text)[0]
    entities = ner(email_text)
    
    if mood['label'] == 'NEGATIVE':
        prompt = f'Apologize for: {email_text}'
    else:
        prompt = f'Thank for: {email_text}'
    
    response = generate(prompt, max_new_tokens=100, temperature=0.4)
    
    return {
        'sentiment': mood,
        'entities': entities,
        'response': response,
    }
```

---

## Common errors → fixes

| Error | Likely cause | Fix |
|---|---|---|
| OOM (out of memory) | Model + batch too big | `dtype=torch.float16`, smaller batch, `enable_attention_slicing()` |
| Generation never stops | EOS token not handled | Set `pad_token_id=tokenizer.eos_token_id`, set `max_new_tokens` |
| Output incoherent | Temperature too high | Drop to 0.3-0.5 |
| Output boring/repetitive | Temperature too low | Raise to 0.5-0.7 |
| `KeyError: 'type'` loading Phi-3 | `trust_remote_code=True` pulls stale code | **Remove** `trust_remote_code` — v5 has native Phi-3/Qwen support |
| `AttributeError` / `.shape` in `generate` | v5 `apply_chat_template` returns a BatchEncoding | Use `return_dict=True` + `generate(**inputs)` |
| `Placeholder storage … MPS` | inputs on CPU, model on MPS | Put both on `DEVICE`; detect `mps` in `DEVICE` |
| Black image from SD on MPS | fp16 SD unstable on MPS | Use `torch_dtype=torch.float32` on MPS/CPU |
| Image generation slow | CPU or fp32 | Use GPU, fp16, smaller image, fewer inference steps |
| All images blocked by safety | Default filter aggressive | `pipe.safety_checker = None` (for class only) |

---

## Verification mindset

**Before trusting LLM output:**
- Did it hallucinate facts? (Look for specifics it couldn't know)
- Is the structured output valid JSON? (parse it, catch errors)
- Does it match the prompt's request?
- For high-stakes outputs, have a human review

**For diffusion images:**
- No quality control beyond "does it look right?"
- For production, have a content review process

---

## Production patterns (briefly)

1. **Validate structured outputs** with Pydantic / jsonschema
2. **Cache** common prompts/outputs
3. **Set timeouts** on API calls
4. **Monitor for drift** when API providers update
5. **Have fallbacks** when models are slow/down
6. **For closed APIs:** monitor cost, set per-user limits

---

## What's next (after this course)

- **LangChain / LlamaIndex:** orchestration libraries for LLM apps
- **RAG (Retrieval-Augmented Generation):** for fact-grounded responses
- **Fine-tuning with LoRA:** for custom LLM behavior
- **Function calling / tool use:** LLMs that can use external APIs
- **Agent frameworks:** AutoGen, CrewAI, Claude Agent SDK

---

**Version:** Week 11 Cheat Sheet v1.0 | April 2026
