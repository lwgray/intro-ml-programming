# Week 11 — Generative AI: LLMs, Diffusion & the Course Finale

This is the finale — the week most students enrolled for. In one 3-hour session students learn how ChatGPT-style LLMs actually work (decoder-only transformers, next-token prediction, RLHF), prompt a real model live, learn how diffusion turns pure noise into images, and generate their own with Stable Diffusion — the two technologies behind the 2022 inflection that changed the public's relationship with AI. And then the whole 11-week arc snaps shut on one idea: from Week 1's linear regression to today's image generation, **it's all gradient descent on a loss function.**

## At a Glance

| | |
|---|---|
| **Topic** | Generative AI: large language models (decoder-only transformers, prompting patterns) + diffusion image generation, ending with the course finale wrap-up |
| **Datasets** | None — this week runs on pretrained models: `microsoft/Phi-3-mini-4k-instruct` (fallback: `Qwen/Qwen2.5-0.5B-Instruct`), `sd-legacy/stable-diffusion-v1-5`, and (Day 2) DistilBERT SST-2 sentiment as the "classic" pipeline stage |
| **Frameworks** | Hugging Face `transformers` + `diffusers`, PyTorch |
| **Structure** | Pre-class (~30 min, includes a **required** LLM pre-download) - Day 1 live session (3 hr) - Day 2 guided deep dive (90-min lecture + 20-min notebook) - Post-class portfolio project (1–3 hr) |
| **Compute** | Brev GPU tier — NVIDIA L4 22 GB (T4 floor, L40S stretch); GPU effectively REQUIRED for Stable Diffusion (Weeks 8–11) |

> ⚠️ **Model cautions:** Students must pre-download Phi-3-mini (~2GB) **before class** — flagged in Week 10 and in the pre-class guide; do not download during the session. Stable Diffusion 1.5 lives at `sd-legacy/stable-diffusion-v1-5` — the old `runwayml` repo is **gone**. Phi-3 and SD 1.5 together OOM on <8GB GPUs — free the LLM from GPU memory before loading Stable Diffusion.

## What Students Learn

- **Decoder-only transformers** — the same Q/K/V attention from Week 10 with one change (causal masking), why generation is autoregressive, and why ChatGPT streams word-by-word (not a UI trick)
- **The 3-stage training stack** — pretraining → supervised fine-tuning → RLHF, held together by the key phrase "Pretraining made it smart. RLHF made it helpful," plus emergent capabilities framed honestly (observed, not fully understood)
- **The four core prompting patterns**, live on Phi-3-mini — zero-shot, few-shot, structured JSON output, and temperature — plus the week's most important safety lesson: watching a confident **hallucination** and internalizing *verify outputs, use RAG for facts, humans review at high stakes*
- **Diffusion intuitively** — the forward noise process gives free training pairs; the model only learns to reverse one noising step; diffusion decomposes one impossible problem (noise → image) into ~1000 easy ones; latent diffusion and CLIP text conditioning reuse the *same* cross-attention from Week 10
- **Live image generation** with Stable Diffusion 1.5 — style prompting, negative prompts, and `guidance_scale` as practical control knobs, with student-suggested prompts generated on the spot
- **The multimodal frontier** — CLIP's shared image/text embedding space, zero-shot classification, vision-language models, and text-to-video/music/speech as "foundation models for every modality"
- **The course through-line** — Week 1's line-through-points and Week 11's images-from-static are the same move: define a loss, compute gradients, update weights, repeat

## Day 1 — Live Session (3 hours)

| Time | Segment | What happens |
|---|---|---|
| 0:00–0:15 | Segment 1: Recap + The Path to ChatGPT | Welcome to the finale; encoders *understand* → decoders *generate*; BERT → GPT-2 → GPT-3 → ChatGPT and the 2022 inflection (ChatGPT + Stable Diffusion within ~100 days) |
| 0:15–0:50 | Segment 2: LLMs Intuitively | Causal masking, autoregressive next-token prediction, emergence, the 3-stage training stack, and the open vs closed model landscape (no code) |
| 0:50–1:20 | Segment 3: Live Prompting Patterns | Phi-3-mini loads live via `from_pretrained`; zero-shot, few-shot, JSON output, temperature — and the hallucination demo (never skipped) |
| 1:20–1:35 | Segment 4: Break | Students rest; instructor runs the 🔒 critical task — free the LLM from GPU memory and pre-stage Stable Diffusion |
| 1:35–2:10 | Segment 5: Diffusion Intuitively | Forward/reverse process, free training pairs, iterative denoising, latent diffusion, CLIP text conditioning via cross-attention (no code) |
| 2:10–2:40 | Segment 6: Live Image Generation | Stable Diffusion 1.5 generates original images live — the visual wow moment — with prompt engineering, negative prompts, and `guidance_scale` |
| 2:40–2:55 | Segment 7: Multimodal Tour | Lightning tour: CLIP, zero-shot classification, VLMs, video/music/speech — the cut-first time buffer (keep CLIP) |
| 2:55–3:00 | Segment 8: Course Finale Wrap-Up | ⚠️ THE COURSE FINALE — Week 1 → Week 11 bookend, "it's all gradient descent on a loss function," Week 12 + portfolio foreshadow, **"Go build things."** Never shortchanged |

## Day 2 — "From Demo to Product": Prompt Engineering + Composing Classic & Generative ML

Day 1 got a demo to work once — Day 2 turns that into engineering judgment. One continuous 90-minute story (whiteboard + live Qwen2.5-0.5B demos + constant ask-predict-reveal), then a 20-minute guided notebook. The spine is a chain of problems, each opening the next:

1. A demo isn't a product → clearer prompts get you far, but who sets the model's rules? (**system vs user roles**)
2. Clear instructions still won't match your exact format → show it examples (**in-context learning**, the deep *why* behind Day 1's few-shot)
3. A human-readable label isn't machine-readable data (**structured output**) → format's fixed but hard reasoning still flops (**chain-of-thought**)
4. None of it fixes the deepest problem: the model doesn't *know*, it predicts (**hallucination, mechanistically**) → so hand it the open book (**RAG** — which Day 1 only *named*)
5. The punchline the course was built to deliver: you own a reliable **classic** model AND a flexible **generative** one — the future is **composing** them (DistilBERT sentiment + Qwen in ONE pipeline), shipped responsibly (cost, latency, trust)

- Guided notebooks: [week11_day2_composing_ml_guided.ipynb](student_materials/day2_guided_practice/week11_day2_composing_ml_guided.ipynb) - [week11_day2_composing_ml_solutions.ipynb](student_materials/day2_guided_practice/week11_day2_composing_ml_solutions.ipynb)

## Materials Map

### For Students

- **Pre-class** (~30 min — do this **before** Day 1):
  - [Week11_Pre_Class_Study_Guide.md](student_materials/pre_class/Week11_Pre_Class_Study_Guide.md) — intuition primer + the **required** Phi-3-mini / Qwen pre-download (~2GB)
- **Day 1 live session:**
  - [week11_live_session.ipynb](student_materials/day1_live_session/week11_live_session.ipynb) — the primary notebook (LLM prompting + Stable Diffusion)
  - [Week11_Student_Workbook.md](student_materials/day1_live_session/Week11_Student_Workbook.md) - [Week11_Generative_AI_Cheat_Sheet.md](student_materials/day1_live_session/Week11_Generative_AI_Cheat_Sheet.md) - [Week11_Glossary.md](student_materials/day1_live_session/Week11_Glossary.md)
- **Day 1 pair programming:**
  - [week11_pair_programming.ipynb](student_materials/day1_pair_programming/week11_pair_programming.ipynb)
- **Day 2 guided practice:**
  - [week11_day2_composing_ml_guided.ipynb](student_materials/day2_guided_practice/week11_day2_composing_ml_guided.ipynb) (+ [solutions](student_materials/day2_guided_practice/week11_day2_composing_ml_solutions.ipynb))
- **Post-class** (1–3 hr — the portfolio piece):
  - [week11_postclass_exercise.ipynb](student_materials/post_class/week11_postclass_exercise.ipynb) (+ [solutions](student_materials/post_class/week11_postclass_solutions.ipynb)) — Final POC project: combine ≥2 models from the course into one working app
  - [Week11_Self_Assessment.md](student_materials/post_class/Week11_Self_Assessment.md) - [Week11_Continued_Learning_Resources.md](student_materials/post_class/Week11_Continued_Learning_Resources.md)
- **Reference reading:**
  - [Appendix J — Generative AI Cookbook](appendices/Appendix_J_Generative_AI_Cookbook.md)

## The Sentences Students Leave With

Every segment plants one line; together they are the week (and the course) in miniature:

- **"Encoders understand. Decoders generate."** — the bridge from Week 10 to Week 11 (Segment 1)
- **"Pretraining made it smart. RLHF made it helpful."** — the training stack in one breath (Segment 2)
- **The model is confidently wrong *by design*, not by error** — verify outputs, use RAG for facts, humans review at high stakes (Segment 3)
- **Diffusion decomposes one impossible problem (noise → image) into ~1000 easy ones (denoise one notch)** — (Segment 5)
- **"Foundation models for every modality"** — the same handful of ideas, applied everywhere (Segment 7)
- **"It's all gradient descent on a loss function."** — Week 1 to Week 11, the same move every time (Segment 8)
- **"Go build things."** — the last full sentence of the course (Segment 8)

## Where This Week Fits

- **Builds on:** Week 10 — encoder transformers (DistilBERT) that *understand* text; this week adds the decoder-only family that *generates*, reusing the same `from_pretrained` workflow from Weeks 9–10
- **Sets up:** Week 12 — the GitHub Copilot Workshop: take everything learned across the course and apply it with AI-assisted coding tools — plus the post-class portfolio piece (combine ≥2 models into one app of your own). **Go build things.**
