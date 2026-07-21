# Week 10 Pre-Class Study Guide
## Sequences, Attention & Transformers

**Time required:** 30 minutes
**Goal:** Arrive with attention intuition + Hugging Face account ready

✅ **Start here:** Read the **[From Words to Vectors primer](Week10_Words_To_Vectors_Primer.md)** first (~15 min). It's the on-ramp that turns today's material from a deep end into a gentle wade-in — do it before anything else.

---

## Where you are in the course

| Week | What you learned | Connection to Week 10 |
|---|---|---|
| 8 | CNNs from scratch | Same loss/optimization principles |
| 9 | Pretrained CNNs + transfer learning | Same `from_pretrained` pattern today |
| **10** | **Transformers + attention** | **NEW: sequences, attention, Hugging Face** |

Two big shifts this week:
1. **New architecture** — attention-based instead of convolutional
2. **New framework** — Hugging Face takes over from Keras for transformers

---

## What to do (~30 minutes)

### Part 1 (REQUIRED — do this first): Read the "From Words to Vectors" primer (~15 min)

**[From Words to Vectors primer](Week10_Words_To_Vectors_Primer.md)**

This is your on-ramp. It teaches the two steps everything today rests on — how text becomes **tokens**, and how tokens become **meaning-vectors (embeddings)** — and gives you a one-sentence picture of attention. Read it slowly; it's written to be easy.

By the end you'll be able to say, in plain English: what tokenization is (and what `[CLS]`/`[SEP]` are), what a word embedding is (**similar words → similar vectors**), and the one-line idea of attention.

### Part 2 (CRITICAL): Set up your Hugging Face account (~5 min)

**Sign up at:** https://huggingface.co (free, no credit card)

You need this for class. Some models (especially in Week 11) require accepting terms of service before download.

### Part 3 (Recommended): Hugging Face quick tour (~10 min)

**Hugging Face Quick Tour:** https://huggingface.co/docs/transformers/quicktour

Read the introduction and `pipeline` section. Try at least one code example if you can.

**Things to extract:**
- The `pipeline` API for inference
- The `AutoTokenizer` + `AutoModel` pairing pattern
- That thousands of pretrained models are available

### Part 4 (Optional reinforcement): Watch the 3Blue1Brown attention video

**3Blue1Brown — Attention in Transformers, Visually Explained:**
https://www.youtube.com/watch?v=eMlx5fFNoYc

The best visual explanation of attention anywhere — and it lands *much* better once you've read the primer, because you'll already know what tokens and embeddings are. **This is a bonus second pass, not a prerequisite.** Don't stress if parts feel fuzzy: **we rebuild attention from scratch, together, on the whiteboard in class.**

### Part 5 (Optional): Skim the original paper

**"Attention Is All You Need" (Vaswani et al., 2017):** https://arxiv.org/abs/1706.03762

Read the abstract and look at Figure 1 (the architecture diagram). **Don't try to read the math.** Just see what it looks like.

---

## A preview of where we're headed (skim — you do NOT need to master these beforehand)

*The primer above is your real on-ramp: tokens, embeddings, and the one-line idea of attention. The Q&A below is a **sneak peek** at what we build together in class. If some of it feels fuzzy right now, that's exactly right — that's what the 50-minute deep dive is for.*

### Q1: What is attention?
**Answer:** A learnable lookup mechanism. For each token, the network issues a query, every other token offers a key, the model computes match scores, then pulls in a weighted mix of values. The output is a weighted combination of value vectors, weighted by relevance.

### Q2: What's Q/K/V?
**Answer:** Three projections of the same input embedding, serving three roles:
- **Query (Q):** "What am I looking for?"
- **Key (K):** "What do I offer?"
- **Value (V):** "Here's my actual content."

For each token, we compute these three vectors via three learned linear projections.

### Q3: What's "self-attention"?
**Answer:** Tokens attending to OTHER tokens in the SAME sequence. Each token's output is a weighted combination of values from all tokens in the sequence (including itself).

### Q4: Why do transformers need positional encoding?
**Answer:** The attention mechanism is permutation-invariant — it would give the same output if you shuffled the words. Positional encodings (added to token embeddings) inject the order information that the architecture itself doesn't preserve.

### Q5: What are the three families of transformers?
**Answer:**
- **Encoder-only (BERT family):** for understanding tasks (classification, NER, embedding)
- **Decoder-only (GPT family):** for generation tasks (text completion, dialogue)
- **Encoder-decoder (T5, BART):** for sequence-to-sequence tasks (translation, summarization)

### Q6: Why did transformers replace RNN/LSTM?
**Answer:** Two reasons:
1. **Long-range dependencies:** RNNs lose information across long sequences (vanishing gradient). Attention can directly link any two positions, regardless of distance.
2. **Parallelization:** RNNs process tokens sequentially — slow to train. Transformers process all positions in parallel — much faster on modern hardware.

---

## What you'll do in class

1. **Recap:** Quick review of Week 9 transfer learning (same `from_pretrained` pattern carries over)
2. **Brief funeral for RNN/LSTM:** What came before, why it failed, why we needed something better
3. **Attention deep dive (50 minutes):** The make-or-break segment. Q/K/V intuition with visualizations.
4. **Hugging Face fundamentals:** `pipeline`, `AutoTokenizer`, `AutoModelForSequenceClassification`
5. **Live coding:** Fine-tune DistilBERT on AG News (4-class news classification)
6. **Pair programming:** Explore different HF pipeline tasks
7. **Wrap-up:** Foreshadow Week 11 (generative AI)

---

## Common student questions before class

**"Will I need to install anything new?"**
Yes. The course platform should have `transformers` and `datasets` installed. If working locally: `pip install transformers datasets evaluate`.

**"Why are we switching from Keras to Hugging Face?"**
Hugging Face dominates the transformer ecosystem. Every modern transformer is published there first. For images, `keras.applications` is more idiomatic. For sequences, `transformers` is. Use the right tool.

**"Is the attention math going to be on a test?"**
No. We'll teach attention conceptually, not mathematically. You should be able to EXPLAIN what attention does — not derive it.

**"Will the class involve writing Q/K/V from scratch?"**
No. We use pretrained transformers via Hugging Face. You'll never have to implement attention by hand for this course.

**"What's the difference between BERT and GPT?"**
BERT is encoder-only (good for understanding). GPT is decoder-only (good for generating). DistilBERT is a smaller, faster BERT. Phi/Qwen are smaller, faster GPTs. We use DistilBERT today.

---

## Things you absolutely cannot skip

1. **Read the "From Words to Vectors" primer.** It's the on-ramp — everything today builds on it.
2. **Create your free Hugging Face account.** You'll need it for class.

---

## Pre-class checklist

- [ ] **Read the [From Words to Vectors primer](Week10_Words_To_Vectors_Primer.md)**
- [ ] **Created free Hugging Face account at huggingface.co**
- [ ] Can explain, in plain English: **tokenization**, **word embeddings** (similar words → similar vectors), and the **one-line idea of attention**
- [ ] Skimmed the Hugging Face Quick Tour
- [ ] Have `transformers` and `datasets` installable / installed
- [ ] *(Optional)* Watched the 3Blue1Brown attention video

---

## Setting up your environment (if working locally)

```bash
pip install transformers datasets evaluate accelerate
```

Quick test:
```python
from transformers import pipeline
classifier = pipeline('sentiment-analysis')
print(classifier('I love machine learning'))
# Should print: [{'label': 'POSITIVE', 'score': 0.999...}]
```

If that works, you're set.

---

## Optional deeper reading

- **The Illustrated Transformer (Jay Alammar):** http://jalammar.github.io/illustrated-transformer/ — Excellent visual walkthrough
- **The Annotated Transformer (Harvard NLP):** http://nlp.seas.harvard.edu/2018/04/03/attention.html — Code-level walkthrough (advanced)
- **BertViz GitHub:** https://github.com/jessevig/bertviz — Interactive attention visualization

---

**A note, not a warning:** Week 10 covers big ideas — but if you've read the primer, you're arriving on the **on-ramp, not the deep end.** We build every concept from scratch in class, with analogies and a live demo. Bring questions; that's the whole point.

See you in class.
