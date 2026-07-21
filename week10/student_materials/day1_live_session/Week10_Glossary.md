# Week 10 Glossary

---

## Core Concepts

**Sequence**
Ordered data where position matters. Examples: text, time series, audio, DNA.

**Token**
A discrete unit of input. For text: usually a subword piece. Tokenizer converts text to tokens, then to integer IDs.

**Tokenization**
The process of converting text into tokens. Each pretrained model has its own tokenizer that must be paired with it.

**Token embedding**
A vector representation of a token. Each unique token in the vocabulary has its own learned embedding vector.

**Vocabulary**
The set of all tokens a tokenizer can produce. Typically 30K-50K tokens for English BERT-family models. Includes subword pieces.

**Attention**
A learnable mechanism where each token computes how much to attend to every other token, then mixes their values weighted by attention scores. The core innovation of transformers.

**Self-attention**
Attention where the same sequence acts as both queries and keys/values. Tokens attend to OTHER tokens in the SAME sequence.

**Cross-attention**
Attention where queries come from one sequence and keys/values from another. Used in encoder-decoder transformers (decoder cross-attends to encoder output).

**Q (Query)**
For each token: "What am I looking for?" Computed by projecting the token embedding through a learned linear layer.

**K (Key)**
For each token: "What do I offer?" Computed similarly to Q but with a different learned projection.

**V (Value)**
For each token: "Here's my actual content." Same idea — different learned projection.

**Multi-head attention**
Running attention multiple times in parallel with different learned Q/K/V projections. Each "head" can specialize in different relationships. Outputs are concatenated.

**Positional encoding**
Vector added to token embeddings to inject position information. Originally sine/cosine waves; modern variants use learned embeddings or rotary encoding (RoPE).

---

## Transformer Architectures

**Encoder-only transformer**
Family that uses only the encoder block of the original transformer. Outputs hidden states for each token. Best for understanding tasks. Examples: BERT, DistilBERT, RoBERTa, DeBERTa.

**Decoder-only transformer**
Family that uses only the decoder block. Generates tokens autoregressively (one at a time, conditioned on previous). Best for generation. Examples: GPT-2/3/4, Llama, Qwen, Phi.

**Encoder-decoder transformer**
Both encoder and decoder. Encoder reads input; decoder generates output. Best for sequence-to-sequence tasks. Examples: T5, BART.

**BERT (Bidirectional Encoder Representations from Transformers)**
The first major encoder-only transformer (2018). Trained by masked language modeling. Foundation for understanding tasks.

**DistilBERT**
A smaller (40% fewer params), faster (60% faster) version of BERT trained via knowledge distillation. Retains ~97% of BERT's accuracy.

**GPT (Generative Pre-trained Transformer)**
Family of decoder-only transformers. GPT-1 (2018), GPT-2 (2019), GPT-3 (2020), GPT-3.5/ChatGPT (2022), GPT-4 (2023+).

---

## Hugging Face Library

**`transformers` library**
The dominant Python library for transformer models. Contains thousands of pretrained models, tokenizers, and training utilities.

**`pipeline()`**
Highest-level inference API. Bundles tokenizer + model + post-processing. One line of code to use a pretrained model.

**`AutoTokenizer.from_pretrained(name)`**
Loads the tokenizer matching a given model. Always use the same name as the model.

**`AutoModel.from_pretrained(name)`**
Loads the base transformer model (no task-specific head). Outputs hidden states.

**`AutoModelForSequenceClassification.from_pretrained(name, num_labels=N)`**
Loads the base transformer with a fresh classification head sized for N classes. The head is randomly initialized; the base is pretrained.

**`AutoModelForXxx`** variants
- `AutoModelForTokenClassification`: NER, POS tagging
- `AutoModelForQuestionAnswering`: extractive QA
- `AutoModelForCausalLM`: language modeling / generation
- `AutoModelForSeq2SeqLM`: seq2seq generation (translation, summarization)

**`Trainer` API**
Hugging Face's high-level training utility. Analogous to `model.fit()` in Keras. Handles training loop, evaluation, logging, checkpoints.

**`TrainingArguments`**
Configuration object for Trainer — learning rate, epochs, batch size, eval strategy, etc.

**`from_pretrained` pattern**
The dominant pattern for loading pretrained models. Same as `keras.applications` from Week 9, just for transformers.

**`save_pretrained(path)`**
Saves a model or tokenizer to a directory. Reload with `from_pretrained(path)`.

---

## Tokenizer Internals

**`[CLS]` (BERT)**
Special token at the start of every sequence. Its hidden state is often used as a sentence-level representation for classification.

**`[SEP]` (BERT)**
Separator token. Marks end of sequence (or boundary between two sequences).

**`[MASK]` (BERT)**
Used during pretraining for masked language modeling. Tokens are randomly replaced with [MASK] and the model learns to predict them.

**`[PAD]`**
Padding token used when batching variable-length sequences. attention_mask tells model to ignore these.

**`##` prefix (BERT-family)**
Indicates a subword continuation. "playing" might tokenize as `play ##ing`.

**`<s>` and `</s>` (RoBERTa-family)**
Different special token format than BERT. Same idea, different syntax.

**Truncation**
Cutting off input that exceeds max_length. `truncation=True` is standard for fine-tuning.

**Padding**
Adding [PAD] tokens to make all sequences in a batch the same length. `padding='max_length'` pads to a fixed length; `padding=True` pads to longest in batch.

**`attention_mask`**
Binary tensor (1 for real tokens, 0 for padding) telling the model which positions to attend to.

---

## Tokenizer Algorithms (knowledge level only)

**WordPiece (BERT)**
Subword tokenization that starts with characters and merges frequent pairs. BERT and DistilBERT use this.

**BPE (Byte-Pair Encoding) (GPT)**
Similar idea, slightly different algorithm. GPT family uses this.

**SentencePiece (T5, multilingual models)**
Language-agnostic tokenizer. Used by T5, mBART, multilingual BERT.

For Week 10, you don't need to know these in depth — just that different models use different algorithms.

---

## Training Concepts (Mostly from Earlier Weeks)

**Learning rate**
Same idea from Week 7. Critical to use LOW LR (2e-5 to 5e-5) for fine-tuning transformers — like Week 9.

**Batch size**
Same idea from Week 6. Smaller for transformers due to memory. Common: 8-16 for fine-tuning.

**Epoch**
Same. For transformer fine-tuning, 3-5 epochs is typical.

**Loss**
For classification: cross-entropy (called `CrossEntropyLoss` in PyTorch, `sparse_categorical_crossentropy` in Keras).

**Optimizer**
AdamW (a slight variant of Adam) is the standard for transformers.

---

## What Came Before (Historical)

**RNN (Recurrent Neural Network)**
Pre-transformer architecture for sequences. Process tokens one at a time, maintaining hidden state. Replaced by transformers ~2018+.

**LSTM (Long Short-Term Memory)**
Variant of RNN with gating mechanisms to handle long-range dependencies better than vanilla RNN. Still substantially worse than transformers on most tasks.

**Vanishing gradient problem**
Why RNNs struggled with long sequences — gradients flowing back through time get exponentially small. Transformers don't have this problem because attention directly links any two positions.

---

## Looking Ahead to Week 11

**LLM (Large Language Model)**
A decoder-only transformer at scale (typically billions of parameters). GPT-3, Claude, Llama all qualify.

**Foundation model**
A general term for large pretrained models used as starting points. LLMs are foundation models for language; ImageNet-pretrained CNNs are foundation models for vision.

**Diffusion model**
Generative model for images. Different architecture from transformers (uses UNet). Coming Week 11.

**RLHF (Reinforcement Learning from Human Feedback)**
Training technique that uses human preference rankings to align LLM outputs. What turned GPT-3 into ChatGPT.

**Prompt engineering**
The empirical practice of crafting prompts to get desired LLM outputs.

---

## Common Misconceptions

**"Attention is just one mechanism."**
False. "Attention" is a family — self-attention, cross-attention, masked attention, multi-head attention. Different variants serve different roles.

**"Transformers replaced CNNs everywhere."**
Mostly false. CNNs still dominate production CV; ViTs (Vision Transformers) are an alternative but not a replacement. For text, yes — transformers replaced RNNs.

**"You need to understand attention math to use transformers."**
False. The intuition is enough. Hugging Face handles the math. The vast majority of practitioners never derive attention from scratch.

**"All transformers are large language models."**
False. DistilBERT (~67M params) is a transformer, not an LLM. LLMs specifically refer to large (billions+) decoder-only generative models.

---

**Version:** Week 10 Glossary v1.0 | April 2026
