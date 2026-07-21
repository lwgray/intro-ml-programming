# Appendix I: Hugging Face API Reference

Quick reference for `transformers` and `datasets` libraries.

---

## Install

```bash
pip install transformers datasets evaluate accelerate
```

---

## High-level inference: `pipeline`

```python
from transformers import pipeline

# Tasks with a pipeline() shortcut in transformers v5 (default models)
pipeline('sentiment-analysis')
pipeline('zero-shot-classification')
pipeline('ner', aggregation_strategy='simple')
pipeline('fill-mask')
pipeline('text-generation', model='gpt2')
pipeline('feature-extraction')  # embeddings
```

> ⚠️ **Removed in transformers v5:** `summarization`, `translation`, and `question-answering` no
> longer have a `pipeline` shortcut. Use the `AutoModel` classes below — `AutoModelForSeq2SeqLM`
> for summarization/translation, `AutoModelForQuestionAnswering` for extractive QA.

```python
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, AutoModelForQuestionAnswering

# Summarization / translation (T5 text-to-text: prefix selects the task)
t5_tok = AutoTokenizer.from_pretrained('google-t5/t5-small')
t5 = AutoModelForSeq2SeqLM.from_pretrained('google-t5/t5-small')
ids = t5.generate(**t5_tok('summarize: ' + text, return_tensors='pt',
                           truncation=True, max_length=512), max_new_tokens=60)
print(t5_tok.decode(ids[0], skip_special_tokens=True))

# Extractive QA (predict answer-span start/end tokens)
qa_tok = AutoTokenizer.from_pretrained('distilbert-base-cased-distilled-squad')
qa = AutoModelForQuestionAnswering.from_pretrained('distilbert-base-cased-distilled-squad')
inp = qa_tok(question, context, return_tensors='pt', truncation=True, max_length=384)
with torch.no_grad():
    out = qa(**inp)
start = out.start_logits.argmax(); end = out.end_logits[0, start:].argmax() + start + 1
print(qa_tok.decode(inp['input_ids'][0][start:end], skip_special_tokens=True))
```

---

## Auto classes (more flexible)

```python
from transformers import (
    AutoTokenizer,
    AutoModel,                              # raw model, no head
    AutoModelForSequenceClassification,     # text classification
    AutoModelForTokenClassification,        # NER
    AutoModelForQuestionAnswering,          # extractive QA
    AutoModelForCausalLM,                   # generation (GPT-style)
    AutoModelForSeq2SeqLM,                  # translation, summarization
    AutoModelForMaskedLM,                   # fill-mask (BERT MLM)
)
```

CRITICAL: same NAME for tokenizer and model.

```python
NAME = 'distilbert-base-uncased'
tokenizer = AutoTokenizer.from_pretrained(NAME)
model = AutoModelForSequenceClassification.from_pretrained(NAME, num_labels=4)
```

---

## Tokenization

```python
inputs = tokenizer(
    text_or_list_of_texts,
    return_tensors='pt',           # 'pt' for PyTorch, 'tf' for TF
    truncation=True,                # cut at max_length
    max_length=128,                 # max seq length
    padding='max_length',           # pad to max_length (consistent shapes)
    # OR:
    # padding=True,                 # pad to longest in batch
)
```

Returns:
- `input_ids`: token IDs
- `attention_mask`: 1 for real tokens, 0 for padding
- (sometimes) `token_type_ids`: for sentence-pair tasks

---

## Datasets library

```python
from datasets import load_dataset, Dataset

# Load standard dataset
ds = load_dataset('ag_news')
ds = load_dataset('imdb')
ds = load_dataset('emotion')

# Subset
small = ds['train'].select(range(2000))

# Custom data
my_ds = Dataset.from_dict({
    'text': [...],
    'label': [...]
})

# Train/test split
splits = my_ds.train_test_split(test_size=0.2, seed=42)

# Apply tokenization
tokenized = ds['train'].map(tokenize_fn, batched=True)
```

---

## Trainer API

```python
from transformers import Trainer, TrainingArguments

training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=3,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=32,
    learning_rate=5e-5,            # CRITICAL: low LR for fine-tuning
    eval_strategy='epoch',          # evaluate every epoch
    logging_steps=50,
    save_strategy='no',             # don't save checkpoints (or 'epoch'/'best')
    report_to='none',               # disable W&B/TensorBoard
)

def compute_metrics(eval_pred):
    predictions, labels = eval_pred
    preds = np.argmax(predictions, axis=1)
    return {'accuracy': (preds == labels).mean()}

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_tokenized,
    eval_dataset=test_tokenized,
    compute_metrics=compute_metrics,
)

trainer.train()
trainer.evaluate()
```

---

## Manual inference (without Trainer)

```python
import torch

inputs = tokenizer('Some text', return_tensors='pt', truncation=True, max_length=128)

# Move to GPU
if torch.cuda.is_available():
    inputs = {k: v.to('cuda') for k, v in inputs.items()}
    model.to('cuda')

model.eval()
with torch.no_grad():
    outputs = model(**inputs)

probs = torch.softmax(outputs.logits, dim=-1)[0].cpu().numpy()
predicted_class = probs.argmax()
```

---

## Save and load

```python
# Save
model.save_pretrained('./my_model')
tokenizer.save_pretrained('./my_model')

# Load
loaded_model = AutoModelForSequenceClassification.from_pretrained('./my_model')
loaded_tokenizer = AutoTokenizer.from_pretrained('./my_model')
```

---

## Attention extraction (for visualization)

```python
model = AutoModel.from_pretrained(NAME, output_attentions=True)
outputs = model(**inputs)

# attentions: tuple of length num_layers
# Each: tensor [batch, num_heads, seq_len, seq_len]
attention = outputs.attentions[5][0]  # last layer, first batch
tokens = tokenizer.convert_ids_to_tokens(inputs['input_ids'][0])
```

---

## Common model names

### Encoder-only
- `bert-base-uncased`, `bert-base-cased`
- `distilbert-base-uncased`
- `roberta-base`, `roberta-large`
- `microsoft/deberta-v3-base`

### Decoder-only
- `gpt2`, `gpt2-large`
- `microsoft/Phi-3-mini-4k-instruct`
- `Qwen/Qwen2.5-0.5B-Instruct`
- `meta-llama/Llama-3-8B-Instruct` (gated)

### Encoder-decoder
- `t5-small`, `t5-base`, `t5-large`
- `facebook/bart-base`, `facebook/bart-large`
- `Helsinki-NLP/opus-mt-en-fr` (translation)

---

## Common errors

| Error | Cause | Fix |
|---|---|---|
| Garbage output | Tokenizer/model mismatch | Use SAME name for both |
| `AttributeError: classifier` | Wrong AutoModel variant | Use `AutoModelForSequenceClassification` |
| Loss NaN | LR too high | `learning_rate=5e-5`, not 1e-3 |
| OOM | Batch too big | `per_device_train_batch_size=8` |
| `RuntimeError: stack expects equal size` | Inconsistent padding | `padding='max_length'` |
| `OSError: Can't load tokenizer` | Network issue | `huggingface-cli login` for gated models |

---

## See also

- `Week10_HuggingFace_Cheat_Sheet.md` — student-facing cheat sheet
- `HUGGINGFACE_TECHNICAL_SETUP.md` — environment setup
- `Section6_Live_Coding_Reference.md` — line-by-line code
