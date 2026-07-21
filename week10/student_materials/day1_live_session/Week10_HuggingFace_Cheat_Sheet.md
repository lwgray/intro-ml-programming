# Week 10 Hugging Face Cheat Sheet

---

## Setup

```bash
pip install transformers datasets evaluate accelerate
```

---

## Easiest possible inference: `pipeline`

```python
from transformers import pipeline

# Sentiment analysis (3 lines!)
classifier = pipeline('sentiment-analysis')
result = classifier('I love this product!')
# [{'label': 'POSITIVE', 'score': 0.999...}]

# Other tasks that STILL have a one-line pipeline() shortcut in transformers v5
ner = pipeline('ner', aggregation_strategy='simple')
zero_shot = pipeline('zero-shot-classification')
generator = pipeline('text-generation', model='gpt2')
fill_mask = pipeline('fill-mask')
```

> ⚠️ **transformers v5 removed the `pipeline` shortcut for `summarization`, `translation`, and
> `question-answering`** (the seq2seq + extractive-QA tasks). Use the `AutoModel` API instead — see
> the next section.

---

## Summarization / Translation / QA (v5: no `pipeline` shortcut)

```python
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, AutoModelForQuestionAnswering

# --- Summarization & Translation: T5 is "text-to-text" (one model, task chosen by a prefix) ---
t5_tok = AutoTokenizer.from_pretrained('google-t5/t5-small')
t5 = AutoModelForSeq2SeqLM.from_pretrained('google-t5/t5-small')

def t5_run(prefixed_text, max_new_tokens=60):
    inp = t5_tok(prefixed_text, return_tensors='pt', truncation=True, max_length=512)
    out = t5.generate(**inp, max_new_tokens=max_new_tokens, num_beams=4)
    return t5_tok.decode(out[0], skip_special_tokens=True)

t5_run('summarize: ' + long_text)                          # summarization
t5_run('translate English to German: ' + 'Hello world.')   # translation

# --- Extractive QA: model predicts the start/end token of the answer span ---
qa_tok = AutoTokenizer.from_pretrained('distilbert-base-cased-distilled-squad')
qa_model = AutoModelForQuestionAnswering.from_pretrained('distilbert-base-cased-distilled-squad')

def answer(question, context):
    inp = qa_tok(question, context, return_tensors='pt', truncation=True, max_length=384)
    with torch.no_grad():
        out = qa_model(**inp)
    start = out.start_logits.argmax()
    end = out.end_logits[0, start:].argmax() + start + 1   # force end >= start (never empty)
    return qa_tok.decode(inp['input_ids'][0][start:end], skip_special_tokens=True)
```

---

## More flexible: AutoTokenizer + AutoModel

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# CRITICAL: same NAME for both
NAME = 'distilbert-base-uncased'
tokenizer = AutoTokenizer.from_pretrained(NAME)
model = AutoModelForSequenceClassification.from_pretrained(NAME, num_labels=4)

# Tokenize input
inputs = tokenizer(
    'Some text to classify',
    return_tensors='pt',  # 'pt' for PyTorch, 'tf' for TensorFlow
    truncation=True,
    max_length=128,
    padding='max_length'
)

# Inference
import torch
with torch.no_grad():
    outputs = model(**inputs)
predictions = outputs.logits.softmax(dim=-1)
```

---

## Variants of `AutoModelForXxx`

| Variant | Use case |
|---|---|
| `AutoModel` | Raw model, outputs hidden states (no task head) |
| `AutoModelForSequenceClassification` | Text classification |
| `AutoModelForTokenClassification` | NER, POS tagging |
| `AutoModelForQuestionAnswering` | Extractive QA |
| `AutoModelForCausalLM` | Generation (GPT-style) |
| `AutoModelForSeq2SeqLM` | Translation, summarization (T5/BART-style) |
| `AutoModelForMaskedLM` | Fill-mask (BERT pretraining task) |

---

## Fine-tuning template (Trainer API)

```python
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    Trainer,
    TrainingArguments,
    set_seed,
)
from datasets import load_dataset
import numpy as np

set_seed(42)

# 1. Load data
ds = load_dataset('ag_news')
train_ds = ds['train'].select(range(2000))
test_ds = ds['test'].select(range(500))

# 2. Tokenize
NAME = 'distilbert-base-uncased'
tokenizer = AutoTokenizer.from_pretrained(NAME)

def tokenize(ex):
    return tokenizer(ex['text'], truncation=True, max_length=128, padding='max_length')

train_tokenized = train_ds.map(tokenize, batched=True)
test_tokenized = test_ds.map(tokenize, batched=True)

# 3. Load model with classification head
model = AutoModelForSequenceClassification.from_pretrained(NAME, num_labels=4)

# 4. Configure training
training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=3,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=32,
    learning_rate=5e-5,        # CRITICAL: low LR
    eval_strategy='epoch',
    logging_steps=50,
    save_strategy='no',
    report_to='none',
    disable_tqdm=True,         # v5: plain-text progress (avoids a notebook callback bug + ipywidgets)
)

# 5. Trainer
def compute_metrics(eval_pred):
    preds, labels = eval_pred
    return {'accuracy': (np.argmax(preds, axis=1) == labels).mean()}

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_tokenized,
    eval_dataset=test_tokenized,
    compute_metrics=compute_metrics,
)

# 6. Train
trainer.train()
trainer.evaluate()
```

---

## Loading datasets

```python
from datasets import load_dataset

# Standard datasets
ds = load_dataset('imdb')           # binary sentiment
ds = load_dataset('ag_news')        # 4-class news
ds = load_dataset('emotion')        # multi-class emotion

# Subset
small = ds['train'].select(range(1000))

# Custom data
from datasets import Dataset
my_ds = Dataset.from_dict({'text': [...], 'label': [...]})
train_test = my_ds.train_test_split(test_size=0.2, seed=42)
```

---

## Common model names

| Model | Family | Size | Use case |
|---|---|---|---|
| `distilbert-base-uncased` | encoder | 67M | Default for fast classification |
| `bert-base-uncased` | encoder | 110M | Standard BERT |
| `roberta-base` | encoder | 125M | Often better than BERT |
| `deberta-v3-base` | encoder | 184M | State-of-the-art encoder |
| `gpt2` | decoder | 124M | Default for text generation demos |
| `microsoft/Phi-3-mini-4k-instruct` | decoder | 3.8B | Small modern LLM (Week 11) |
| `Qwen/Qwen2.5-0.5B-Instruct` | decoder | 0.5B | Smallest usable LLM (Week 11) |
| `t5-base` | enc-dec | 220M | Translation, summarization |
| `facebook/bart-base` | enc-dec | 140M | Summarization |

---

## Key parameters explained

**`truncation=True`** — Cut inputs longer than max_length
**`max_length=128`** — Max tokens (most BERT-family allow up to 512)
**`padding='max_length'`** — Pad shorter inputs to max_length (consistent shape)
**`padding=True`** — Pad to longest in batch (variable shape)
**`return_tensors='pt'`** — Return PyTorch tensors

**`learning_rate=5e-5`** — Standard for fine-tuning. NEVER use 1e-3 (default Adam).
**`num_train_epochs=3`** — Standard for fine-tuning. More epochs → overfitting on small data.
**`per_device_train_batch_size=16`** — Reduce if OOM.

---

## Saving and loading

```python
# Save
model.save_pretrained('./my_model')
tokenizer.save_pretrained('./my_model')  # IMPORTANT: save both

# Load
loaded_model = AutoModelForSequenceClassification.from_pretrained('./my_model')
loaded_tokenizer = AutoTokenizer.from_pretrained('./my_model')
```

---

## Inference pattern (after fine-tuning)

```python
import torch

def predict(text, model, tokenizer, label_names):
    # Use the model's OWN device so inputs/weights match on CPU, CUDA, or Apple MPS.
    device = next(model.parameters()).device
    inputs = tokenizer(text, return_tensors='pt', truncation=True, max_length=128).to(device)
    model.eval()
    with torch.no_grad():
        outputs = model(**inputs)
    probs = torch.softmax(outputs.logits, dim=-1)[0].cpu().numpy()
    pred_idx = probs.argmax()
    return label_names[pred_idx], probs[pred_idx]

label, conf = predict('Some text', model, tokenizer, ['negative', 'positive'])
```

---

## Attention extraction (for visualization)

```python
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained('distilbert-base-uncased')
model = AutoModel.from_pretrained('distilbert-base-uncased', output_attentions=True)

inputs = tokenizer('The cat sat on the mat', return_tensors='pt')
outputs = model(**inputs)

# attentions: tuple length = num_layers
# Each: tensor [batch, num_heads, seq_len, seq_len]
attention = outputs.attentions[5][0]  # last layer, first batch
tokens = tokenizer.convert_ids_to_tokens(inputs['input_ids'][0])
```

---

## Common errors → fixes

| Error | Fix |
|---|---|
| Garbage output | Use matching tokenizer + model from same NAME |
| `AttributeError: classifier` | Use `AutoModelForSequenceClassification`, not `AutoModel` |
| Loss NaN | Lower LR (5e-5 → 2e-5) |
| OOM | Reduce batch_size or max_length |
| `tokenizer not found` | Check spelling; need internet for first download |
| Inconsistent shapes in batch | Ensure `padding='max_length'` consistently |

---

## What's coming in Week 11

```python
# Sneak peek of Week 11 — small LLM for generation
from transformers import pipeline
generator = pipeline(
    'text-generation',
    model='microsoft/Phi-3-mini-4k-instruct',
    device='cuda' if torch.cuda.is_available() else 'cpu',
)
out = generator('Explain transformers in one sentence:', max_new_tokens=80)
```

---

**Version:** Week 10 Cheat Sheet v1.0 | April 2026
