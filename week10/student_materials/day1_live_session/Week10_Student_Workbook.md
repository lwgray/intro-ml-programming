# Week 10 Student Workbook

Use alongside `week10_live_session.ipynb`. Fill in as you go.

⚠️ **Heads up:** This is the conceptually hardest week. Take notes. It's OK if some bits don't land on first pass.

---

## Setup

**Date:** ___________
**My HF account username:** ___________
**Did `pipeline('sentiment-analysis')` work?** Yes / No

---

## Section 1: Hugging Face `pipeline` API

### What is `pipeline`?
*One sentence:*
___________________________________________

### Tasks I tried in class:
- [ ] sentiment-analysis
- [ ] summarization
- [ ] zero-shot-classification
- [ ] (other): ___________

### What surprised you about how easy this was?
___________________________________________

---

## Section 2: Attention Mechanism (the big one)

### Q/K/V — fill in the analogy
| Letter | Meaning | Search engine analogy |
|---|---|---|
| Q | Query | "What am I ___________?" |
| K | Key | "What do I ___________?" |
| V | Value | "Here's my ___________" |

### Attention computation steps (fill in)
1. For each token, compute Q, K, V (three projections of the input embedding)
2. Compute Q · K for each pair → ___________
3. Apply ___________ to convert to probabilities
4. Compute weighted sum of ___________ values, weighted by attention scores
5. Output is the attention result for that token

### Why is "self-attention" called self?
___________________________________________

### What does multi-head attention do?
___________________________________________

### Why do we need positional encoding?
___________________________________________

---

## Section 3: The Three Transformer Families

| Family | Examples | Best for |
|---|---|---|
| Encoder-only | ___________, ___________, DistilBERT | ___________ tasks |
| Decoder-only | ___________, ___________, Llama | ___________ tasks |
| Encoder-decoder | ___________, BART | ___________ tasks |

### Today we used the ___________ family (DistilBERT).

### Next week we'll use the ___________ family (LLMs).

---

## Section 4: Fine-Tuning DistilBERT

### Architecture pattern
```
Input text
  ↓
Tokenizer (AutoTokenizer)
  ↓
Token IDs + attention mask
  ↓
Pretrained DistilBERT base
  ↓
Hidden states
  ↓
Classification head (Dense(num_labels))
  ↓
Logits → Softmax → Class probabilities
```

### Critical pairing rule
**Tokenizer name must match model name.** Use `AutoTokenizer.from_pretrained(NAME)` and `AutoModel*.from_pretrained(NAME)` with the same NAME.

### Fine-tuning learning rate (CRITICAL)
**Default Adam:** ___________
**For fine-tuning:** ___________ (___ × lower)

### Why low LR?
___________________________________________

### My results
- Training samples: ___________
- Test accuracy: ___________
- Training time: ___________

---

## Section 5: Tokenization Examples

### What does the tokenizer do to "machine learning is amazing"?

Tokens (write them down):
___________________________________________

### What does `[CLS]` mean? ___________
### What does `[SEP]` mean? ___________
### What do `##` prefixes mean? ___________

---

## Reflection

### What's the biggest concept I'm shaky on?
___________________________________________
___________________________________________

### What's the biggest concept I now understand?
___________________________________________
___________________________________________

### Connection to Week 9
*How is fine-tuning a transformer like fine-tuning a CNN?*
___________________________________________

*How is it different?*
___________________________________________

### Connection to Week 11
*What do you predict next week's class will cover?*
___________________________________________

---

## Pair Programming Notes

**Partner:** ___________
**Task we tried:** ___________

### What worked well
___________________________________________

### What didn't work well / surprised us
___________________________________________

### Production usefulness
*Would you trust this in production? Why or why not?*
___________________________________________

---

## Post-class checklist

- [ ] Reviewed live session notebook
- [ ] Started custom HF pipeline exercise
- [ ] Self-assessment filled in
- [ ] **Downloaded Phi-3-mini OR Qwen2.5-0.5B** (for Week 11)
- [ ] Identified 1-2 questions for office hours

---

## Reassurance

**It's normal to be confused after Week 10.** Attention is the hardest concept in this course. By Week 11, when you're using transformers in code, the intuition will solidify.

If you're feeling lost, the single best resource for self-study is Jay Alammar's "Illustrated Transformer": http://jalammar.github.io/illustrated-transformer/

See you in Week 11. Course finale.
