# Week 10 — Sequences, Attention & Transformers

This is the biggest, heaviest week of the course — and the payoff is the architecture behind every modern language model. Students learn why text broke CNNs and killed RNNs, spend a full 50 minutes on attention ("a search engine inside the network"), then cash the theory in with Hugging Face: three-line `pipeline()` calls and a live fine-tune of DistilBERT to ~90% on AG News. Same `from_pretrained` philosophy as Week 9's transfer learning — just for text instead of images.

## At a Glance

| | |
| --- | --- |
| **Topic** | Sequences, attention, and transformers — Q/K/V intuition, the Hugging Face ecosystem, and fine-tuning DistilBERT |
| **Datasets** | AG News (Day 1 fine-tune) · IMDB (post-class Part B option) |
| **Frameworks** | Hugging Face `transformers` (v5) + `datasets` (PyTorch under the hood) · BertViz for attention visualization |
| **Structure** | Pre-class (~30 min) - Day 1 live session (3 hr) - Day 2 guided deep dive (90-min lecture + 20-min notebook) - Post-class (~60–90 min) |
| **Compute** | Brev GPU tier — NVIDIA L4 22 GB (T4 floor, L40S stretch); CPU fallback workable but slow (Weeks 8–11) |

**Two logistics beats to know up front:** students need a **free Hugging Face account** before class (it's in the pre-class guide), and the wrap-up assigns a **~2 GB model pre-download (Phi-3-mini or Qwen2.5-0.5B) before Week 11** — the highest-dependency week of the course.

## What Students Learn

- **The sequence problem** — "Dog bites man" vs "Man bites dog": same words, different meaning; order matters, and CNNs (built for spatial data) don't natively respect it
- **Why RNNs/LSTMs died** — vanishing gradients and un-parallelizable sequential processing, and why 2017's "Attention Is All You Need" (Vaswani et al.) was the inflection point
- **The attention mechanism** — Query/Key/Value projections, the softmax-weighted lookup, self- vs cross-attention, multi-head attention, and positional encoding, all anchored to the "search engine inside the network" metaphor — plus real attention weights plotted live on a real sentence
- **The Hugging Face ecosystem** — `pipeline()` turns a pretrained transformer into a 3-line function call; the three transformer families (encoder / decoder / encoder-decoder) and how to map a task to a family
- **The `from_pretrained` pattern for text** — and the #1 rule: tokenizer and model MUST share the same name
- **Fine-tuning DistilBERT on AG News** — tokenization (`[CLS]`/`[SEP]`/`##` subwords), a fresh classification head (`num_labels=4`), the low-LR lesson (5e-5, straight from Week 9), and the Trainer API driving to ~90% accuracy in under a minute on GPU
- **Breadth across NLP tasks** — NER, fill-mask, and text generation via `pipeline()`; QA, translation, and summarization via the transformers-v5 pattern (`AutoModelForSeq2SeqLM` + `.generate()` — the same `from_pretrained` idea, a few more lines)

## Day 1 — Live Session (3 hours)

| Time | Segment | What happens |
| --- | --- | --- |
| 0:00–0:10 | Segment 1 — Week 9 Recap + The Sequence Problem | Acknowledge the difficulty out loud ("everyone is shaky on attention — that's normal"), bridge from Week 9's `from_pretrained` pattern, land "Dog bites man" vs "Man bites dog" |
| 0:10–0:25 | Segment 2 — The RNN/LSTM Funeral | The hidden-state chain, the two fatal flaws (vanishing gradients, no parallelism), and the 2017 "Attention Is All You Need" inflection point |
| 0:25–1:15 | Segment 3 — Attention Deep Dive | Q/K/V, the search-engine metaphor, multi-head, positional encoding, and a live attention heatmap on "The cat sat on the mat" |
| 1:15–1:30 | Segment 4 — Break | Students decompress + verify HF login and warm caches; instructor arms the Segment 6 backup checkpoint |
| 1:30–2:00 | Segment 5 — Hugging Face Fundamentals | Live `pipeline()` sentiment and zero-shot, summarization via T5 + `.generate()` (transformers v5), the three families, the tokenizer-pairing rule |
| 2:00–2:40 | Segment 6 — Live Coding: Fine-Tune DistilBERT | The magic moment: AG News, 4 classes, Trainer API, ~90% accuracy live, predictions on brand-new sentences, save/reload |
| 2:40–2:55 | Segment 7 — Pair Pipeline Exploration | Pairs pick ONE task (NER, fill-mask, generation, QA, translation, summarization) and probe its limits with custom inputs |
| 2:55–3:00 | Segment 8 — Wrap-up + Week 11 Hook | Three-point recap, post-class assignment, encoder-understands/decoder-generates hook, and the CRITICAL Week 11 model download reminder |

## Day 2 — "Inside the Transformer": SEE Attention, Meet the Decoder

A 90-minute whiteboard-driven story plus a 20-minute guided notebook that turns Day 1's recipe into real understanding: **see it → multiply it → place it**. Students visualize the meaning-space and watch live attention weights ("it" reaching back to "the mat"), meet multi-head attention as a committee of specialists, then place DistilBERT among the three architecture families — spending real time on the decoder, because a scaled-up decoder *is* an LLM (that's Week 11).

- Guided notebooks: [week10_day2_transformer_internals_guided.ipynb](student_materials/day2_guided_practice/week10_day2_transformer_internals_guided.ipynb) · [solutions](student_materials/day2_guided_practice/week10_day2_transformer_internals_guided_solutions.ipynb)

## Materials Map

### For Students

#### Pre-class (~30 min)

- [Pre-Class Study Guide](student_materials/pre_class/Week10_Pre_Class_Study_Guide.md) — includes the Hugging Face account setup
- [From Words to Vectors Primer](student_materials/pre_class/Week10_Words_To_Vectors_Primer.md) — the ~15-min on-ramp; read first

#### Day 1 live session

- [week10_live_session.ipynb](student_materials/day1_live_session/week10_live_session.ipynb) — the primary notebook (attention viz, pipelines, DistilBERT fine-tune)
- [Student Workbook](student_materials/day1_live_session/Week10_Student_Workbook.md) · [Hugging Face Cheat Sheet](student_materials/day1_live_session/Week10_HuggingFace_Cheat_Sheet.md) · [Glossary](student_materials/day1_live_session/Week10_Glossary.md)

#### Day 1 pair programming

- [week10_pair_programming.ipynb](student_materials/day1_pair_programming/week10_pair_programming.ipynb) — six scaffolded tasks; pick one, go deep (note: QA/translation/summarization use `AutoModel` + `.generate()`, not `pipeline()`, under transformers v5)

#### Day 2 guided practice

- [week10_day2_transformer_internals_guided.ipynb](student_materials/day2_guided_practice/week10_day2_transformer_internals_guided.ipynb) · [solutions](student_materials/day2_guided_practice/week10_day2_transformer_internals_guided_solutions.ipynb)

#### Post-class (~60–90 min)

- [week10_postclass_exercise.ipynb](student_materials/post_class/week10_postclass_exercise.ipynb) — Part A: build YOUR pipeline on your own data; Part B (stretch): fine-tune DistilBERT on custom labeled text (e.g., IMDB)
- [Solutions](student_materials/post_class/week10_postclass_solutions.ipynb) · [Self-Assessment](student_materials/post_class/Week10_Self_Assessment.md) (includes the Week 11 download checkbox)

#### Visuals

- [student_materials/visuals/](student_materials/visuals/) — attention heatmap, Q/K/V flow, multi-head, positional encoding, transformer family tree, and more (PNGs + specs)

#### Reference reading

- [Appendix I: Hugging Face API Reference](appendices/Appendix_I_HuggingFace_API_Reference.md)

## Where This Week Fits

- **Builds on:** Week 9 — transfer learning for vision (load a pretrained backbone → freeze → train a new head, 95%+ on ~500 images); today is the exact same `from_pretrained` philosophy, for text
- **Sets up:** Week 11 — encoders *understand*, decoders *generate*: scale a decoder up and that's ChatGPT. The finale covers LLMs + diffusion — and students must pre-download Phi-3-mini or Qwen2.5-0.5B (~2 GB) before class
