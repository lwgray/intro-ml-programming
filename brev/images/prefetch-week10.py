"""Bake the week 10 models and datasets (HF_HOME cache) into the image."""

from datasets import load_dataset
from transformers import (
    AutoModel,
    AutoModelForCausalLM,
    AutoModelForQuestionAnswering,
    AutoModelForSeq2SeqLM,
    AutoTokenizer,
    pipeline,
)

# Models the notebooks name explicitly
for name in ['distilbert-base-uncased', 'gpt2', 't5-small', 'google-t5/t5-small',
             'distilbert-base-cased-distilled-squad']:
    AutoTokenizer.from_pretrained(name)

AutoModel.from_pretrained('distilbert-base-uncased')
AutoModelForCausalLM.from_pretrained('gpt2')
AutoModelForSeq2SeqLM.from_pretrained('t5-small')
AutoModelForSeq2SeqLM.from_pretrained('google-t5/t5-small')
AutoModelForQuestionAnswering.from_pretrained('distilbert-base-cased-distilled-squad')

# Default checkpoints behind the bare pipeline() calls in the pair-programming
# and post-class notebooks. Soft-fail: transformers v5 removed some no-model
# shortcuts, and a missing nicety shouldn't fail the image build.
for task in ['sentiment-analysis', 'fill-mask', 'ner', 'zero-shot-classification']:
    try:
        pipeline(task)
    except Exception as e:
        print(f'skipping pipeline({task!r}) prefetch: {e}')

# Datasets
load_dataset('ag_news')  # day 1 fine-tune
load_dataset('imdb')     # post-class

print('week10 prefetch complete')
