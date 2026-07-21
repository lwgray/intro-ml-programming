# Appendix J: Generative AI Cookbook

Recipes for common generative AI tasks. Use as starting points for student POCs.

---

## Recipe 1: Quick LLM inference (Phi-3-mini)

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# GPU, Apple Silicon (MPS), or CPU
DEVICE = 'cuda' if torch.cuda.is_available() else ('mps' if torch.backends.mps.is_available() else 'cpu')
MODEL = 'microsoft/Phi-3-mini-4k-instruct'

tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForCausalLM.from_pretrained(
    MODEL,
    dtype=torch.float16 if DEVICE in ('cuda', 'mps') else torch.float32,  # v5: 'dtype' (was 'torch_dtype')
    device_map='auto' if DEVICE == 'cuda' else None,
    # No trust_remote_code on v5 — native Phi-3/Qwen support; old bundled code crashes (KeyError: 'type').
)
if DEVICE != 'cuda':
    model = model.to(DEVICE)

def generate(prompt, max_new_tokens=120, temperature=0.7):
    messages = [{'role': 'user', 'content': prompt}]
    # v5: apply_chat_template returns a BatchEncoding — use return_dict=True + generate(**inputs).
    inputs = tokenizer.apply_chat_template(
        messages, return_tensors='pt', add_generation_prompt=True, return_dict=True
    ).to(DEVICE)
    with torch.no_grad():
        outputs = model.generate(
            **inputs, max_new_tokens=max_new_tokens, temperature=temperature,
            top_p=0.9, do_sample=temperature > 0,
            pad_token_id=tokenizer.eos_token_id,
        )
    return tokenizer.decode(outputs[0][inputs['input_ids'].shape[1]:], skip_special_tokens=True)

print(generate('Explain transformers in one sentence.'))
```

---

## Recipe 2: Structured JSON output

```python
prompt = '''Extract product info as JSON.

Message: "I bought the Nikon Z6 II for $1900 from B&H Photo."

Return ONLY valid JSON with keys: product, brand, price, vendor.'''

import json
result = generate(prompt, max_new_tokens=80, temperature=0.1)

# Parse and validate
try:
    data = json.loads(result)
    print(data)
except json.JSONDecodeError:
    print('LLM produced invalid JSON; retry or use a JSON-enforcement library')
```

For production: use `outlines` or `instructor` libraries to enforce JSON schema.

---

## Recipe 3: Stable Diffusion image generation

```python
from diffusers import StableDiffusionPipeline
import torch

DEVICE = 'cuda' if torch.cuda.is_available() else ('mps' if torch.backends.mps.is_available() else 'cpu')
# diffusers keeps `torch_dtype`. fp16 only on CUDA — on MPS/CPU it can produce black images.
pipe = StableDiffusionPipeline.from_pretrained(
    'sd-legacy/stable-diffusion-v1-5',
    torch_dtype=torch.float16 if DEVICE == 'cuda' else torch.float32,
).to(DEVICE)
pipe.safety_checker = None  # for class only
if DEVICE == 'mps':
    pipe.enable_attention_slicing()

image = pipe(
    'a cat wearing a top hat, photorealistic, 4k',
    negative_prompt='watermark, text, low quality',
    num_inference_steps=20,
    guidance_scale=7.5,
).images[0]
image.save('output.png')
```

---

## Recipe 4: Multi-model app (sentiment-aware response generator)

```python
from transformers import pipeline

sentiment = pipeline('sentiment-analysis')
# llm: load Phi-3 from Recipe 1

def respond_to_customer(message):
    mood = sentiment(message)[0]
    
    if mood['label'] == 'NEGATIVE':
        prompt = (
            f'A customer wrote: "{message}"\n\n'
            f'Write a brief, sincere apology. Maximum 3 sentences.'
        )
    else:
        prompt = (
            f'A customer wrote: "{message}"\n\n'
            f'Write a brief thank-you. Maximum 2 sentences.'
        )
    
    response = generate(prompt, max_new_tokens=100, temperature=0.5)
    return {
        'sentiment': mood['label'],
        'confidence': float(mood['score']),
        'response': response,
    }

# Usage
print(respond_to_customer('My order arrived broken!'))
```

---

## Recipe 5: NER-based extraction

```python
from transformers import pipeline

ner = pipeline('ner', aggregation_strategy='simple')

def extract_entities(text):
    results = ner(text)
    extracted = {}
    for r in results:
        ent_type = r['entity_group']
        extracted.setdefault(ent_type, []).append(r['word'])
    return extracted

print(extract_entities(
    'Sundar Pichai, CEO of Google, met with President Biden in Washington.'
))
```

---

## Recipe 6: Zero-shot classification

```python
zero_shot = pipeline('zero-shot-classification')

result = zero_shot(
    'I just bought tickets to see the Yankees play.',
    candidate_labels=['sports', 'politics', 'food', 'technology']
)

for label, score in zip(result['labels'], result['scores']):
    print(f'{label:12s}: {score:.3f}')
```

---

## Recipe 7: Image-to-prompt-to-image

Combine Week 9 (image classification) + Week 11 (SD).

```python
from transformers import pipeline

# Step 1: classify image
classifier = pipeline('image-classification', model='google/vit-base-patch16-224')

input_image = ... # Load image
classes = classifier(input_image)
top_class = classes[0]['label']

# Step 2: use class as Stable Diffusion prompt
generated = pipe(
    f'a {top_class}, in the style of Studio Ghibli',
    num_inference_steps=20,
).images[0]
generated.save('stylized.png')
```

---

## Recipe 8: Cluster description (combine K-Means with LLM)

```python
from sklearn.cluster import KMeans

# Step 1: cluster (Week 5 from course)
kmeans = KMeans(n_clusters=4, random_state=42)
labels = kmeans.fit_predict(your_data)

# Step 2: get representative samples per cluster
for cluster_id in range(4):
    samples = your_data[labels == cluster_id][:5]  # 5 representative
    
    prompt = f'''I have a cluster of customer purchases:
    {samples}
    
    Describe in 1 sentence what kind of customer this represents.'''
    
    description = generate(prompt, max_new_tokens=40)
    print(f'Cluster {cluster_id}: {description}')
```

---

## Recipe 9: Document summarization at scale

```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# transformers v5 removed the 'summarization' pipeline shortcut. Summarization is a seq2seq
# task — use AutoModelForSeq2SeqLM. T5 is "text-to-text": prefix the input with 'summarize: '.
sum_tok = AutoTokenizer.from_pretrained('google-t5/t5-small')
sum_model = AutoModelForSeq2SeqLM.from_pretrained('google-t5/t5-small')

def _summarize(text, max_new_tokens=100):
    inputs = sum_tok('summarize: ' + text, return_tensors='pt', truncation=True, max_length=512)
    ids = sum_model.generate(**inputs, max_new_tokens=max_new_tokens, num_beams=4)
    return sum_tok.decode(ids[0], skip_special_tokens=True)

def summarize_long_doc(text, chunk_size=1000):
    # Split into chunks
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    
    # Summarize each chunk
    summaries = [_summarize(chunk, max_new_tokens=100) for chunk in chunks]
    
    # Combine
    combined = ' '.join(summaries)
    
    # Summarize the combined summary
    if len(combined) > chunk_size:
        return _summarize(combined, max_new_tokens=200)
    return combined

print(summarize_long_doc(your_long_document))
```

---

## Recipe 10: Conversational system

```python
class ChatBot:
    def __init__(self):
        self.history = []
    
    def chat(self, user_message):
        self.history.append({'role': 'user', 'content': user_message})
        
        # v5: apply_chat_template returns a BatchEncoding — return_dict=True + generate(**inputs).
        inputs = tokenizer.apply_chat_template(
            self.history, return_tensors='pt', add_generation_prompt=True, return_dict=True
        ).to(DEVICE)
        
        with torch.no_grad():
            outputs = model.generate(
                **inputs, max_new_tokens=200, temperature=0.7,
                pad_token_id=tokenizer.eos_token_id,
            )
        response = tokenizer.decode(outputs[0][inputs['input_ids'].shape[1]:], skip_special_tokens=True)
        
        self.history.append({'role': 'assistant', 'content': response})
        return response

bot = ChatBot()
print(bot.chat('Hello!'))
print(bot.chat('What did I just say?'))
```

---

## Production patterns

### Always validate LLM JSON output
```python
import json
from pydantic import BaseModel

class ProductInfo(BaseModel):
    product: str
    price: float

result = generate(prompt)
try:
    data = ProductInfo.model_validate_json(result)
except Exception:
    # Retry, fallback, or manual review
    ...
```

### Cache LLM outputs
```python
from functools import lru_cache

@lru_cache(maxsize=1000)
def cached_generate(prompt):
    return generate(prompt)
```

### Rate limit
```python
from time import sleep
def safe_generate(prompt):
    sleep(0.1)  # rate limit
    return generate(prompt)
```

---

## See also

- `Week11_Generative_AI_Cheat_Sheet.md` — student-facing cheat sheet
- `GENERATIVE_AI_TECHNICAL_SETUP.md` — environment setup
- `Section6_Live_Coding_Reference.md` — line-by-line code
- `Week11_Continued_Learning_Resources.md` — what to study next
