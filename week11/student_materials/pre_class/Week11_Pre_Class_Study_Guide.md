# Week 11 Pre-Class Study Guide
## Generative AI — LLMs and Diffusion (Course Finale)

**Time required:** 30 minutes
**Goal:** Arrive with intuition for LLMs + diffusion, and models pre-downloaded

⚠️ **Critical:** Download Phi-3-mini (or Qwen2.5-0.5B) BEFORE class. ~2GB; do not try to download during class.

---

## Where you are in the course

| Week | What you learned | Connection to Week 11 |
|---|---|---|
| 8-9 | CNN + transfer learning | Same `from_pretrained` pattern, scaled up |
| 10 | Encoder transformers (DistilBERT) | Today: decoder transformers (LLMs) |
| **11** | **LLMs + Diffusion** | **NEW: generative models, prompt engineering** |

This is the course finale for substantive ML content. Week 12 is the Copilot Workshop.

---

## What to do (30 minutes)

### Part 1 (CRITICAL): Download model weights (10 minutes)

You need to pre-download a small LLM before class. Pick ONE based on your machine:

**Option A: Phi-3-mini (recommended — more capable)**
- Size: ~2GB
- RAM needed: 8GB+ recommended
- Download:
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained('microsoft/Phi-3-mini-4k-instruct')
model = AutoModelForCausalLM.from_pretrained('microsoft/Phi-3-mini-4k-instruct')
print('Phi-3-mini downloaded')
```

**Option B: Qwen2.5-0.5B-Instruct (faster, smaller — good for older machines)**
- Size: ~500MB
- RAM needed: 4GB+
- Download:
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained('Qwen/Qwen2.5-0.5B-Instruct')
model = AutoModelForCausalLM.from_pretrained('Qwen/Qwen2.5-0.5B-Instruct')
print('Qwen-0.5B downloaded')
```

**Test it:**
```python
inputs = tokenizer.apply_chat_template(
    [{'role': 'user', 'content': 'Say hello.'}],
    return_tensors='pt',
    add_generation_prompt=True,
    return_dict=True,            # transformers v5 returns a BatchEncoding
)
outputs = model.generate(**inputs, max_new_tokens=20)
print(tokenizer.decode(outputs[0][inputs['input_ids'].shape[1]:], skip_special_tokens=True))
```

If you see a hello-like response, you're good.

### Part 2: Watch 3Blue1Brown LLM video (15 min)

**3Blue1Brown — Large Language Models, but how?**
https://www.youtube.com/watch?v=LPZh9BOjkQs

Watch through the section on "predicting the next token" and "attention's role in LLMs." Same series as the attention video from Week 10.

**Things to extract:**
- LLMs are decoder-only transformers
- Trained to predict the next token
- Scale + RLHF turn this into ChatGPT
- Tokens, context window, sampling parameters

### Part 3: Watch a diffusion explainer (10 min)

Any short visual explainer:
- AssemblyAI: "How Diffusion Models Work"
- 3Blue1Brown: "But what is diffusion?" (if available)
- DeepLearning.AI: "How Stable Diffusion works"

**Key concepts:**
- Forward process: add noise step by step
- Reverse process: train a model to undo noise
- Sampling: start with noise, denoise to image

### Part 4: Read Hugging Face Diffusers Quick Tour (5 min)

https://huggingface.co/docs/diffusers/quicktour

Just the introduction. Get familiar with `StableDiffusionPipeline`.

---

## Concepts to arrive with

### Q1: What's an LLM?
**Answer:** A decoder-only transformer trained at massive scale to predict the next token. At sufficient scale (billions of parameters, trillions of training tokens), this gives rise to emergent capabilities — reasoning, code generation, dialogue.

### Q2: What's RLHF and why does it matter?
**Answer:** Reinforcement Learning from Human Feedback. Pretraining gives you a smart but unaligned model. Instruction tuning teaches it to follow instructions. RLHF teaches it to be helpful, harmless, honest. **Pretraining made it smart; RLHF made it helpful.**

### Q3: What's "next-token prediction at scale"?
**Answer:** The training objective. Read N tokens, predict the (N+1)th. Compare to actual next token. Update weights via gradient descent. Repeat for trillions of tokens. Out comes a model that can do tasks the trainers never explicitly designed for — emergent capabilities.

### Q4: How does a diffusion model work?
**Answer:**
- Forward: take an image, add Gaussian noise step by step until it's pure noise
- Reverse: train a model to undo ONE step at a time
- Sampling: start with random noise, apply the reverse step ~50 times, get a coherent image

### Q5: What's "latent diffusion"?
**Answer:** Running diffusion in a compressed latent space (~16K dimensions) instead of pixel space (millions). Stable Diffusion uses this — it's why SD runs on consumer hardware while pure-pixel diffusion would be impractical.

### Q6: What's the connection between Week 10 and Week 11?
**Answer:** Same `from_pretrained` pattern. Week 10's encoder transformers (DistilBERT) understand text. Week 11's decoder transformers (LLMs) generate text. Diffusion is a different paradigm — but text conditioning in diffusion uses cross-attention, same mechanism from Week 10.

---

## What you'll do in class

1. **Recap Week 10:** Encoder transformers vs decoder transformers
2. **LLMs intuitively:** Pretraining → Instruction tuning → RLHF
3. **Live prompting (30 min):** Phi-3-mini hands-on. Zero-shot, few-shot, JSON output, temperature
4. **Diffusion intuitively:** Forward/reverse process, latent diffusion
5. **Live image generation (30 min):** Stable Diffusion via `diffusers`. Prompt iteration, negative prompts
6. **Multimodal tour:** CLIP, vision-language, text-to-video, audio
7. **Course wrap-up:** From linear regression to image generation in 11 weeks

---

## Common student questions

**"Will I be able to run Stable Diffusion on my laptop?"**
On GPU: yes (~3-5 sec/image). On CPU: technically yes but slow (~30-60 sec/image at 256×256). Class will use the course GPU platform.

**"How much will this cost?"**
We're using OPEN-SOURCE models (free) running locally. No API charges. The instructor may demo a closed API (Claude, GPT) for comparison — that's instructor-only.

**"Will we learn how to fine-tune an LLM?"**
Conceptually yes, hands-on no. Full LLM fine-tuning needs serious infrastructure. We'll mention LoRA/QLoRA as further reading. The course focus is using LLMs effectively, not training them.

**"Is this the last week of new content?"**
Yes. Week 12 is the Copilot Workshop — applying everything to coding workflows.

---

## Things you absolutely cannot skip

1. **Download Phi-3-mini OR Qwen2.5-0.5B before class.** Don't try to download during class — 200 students hitting Hugging Face simultaneously will tank.
2. **Watch the 3B1B LLM video.** Same quality as the attention video.

---

## Pre-class checklist

- [ ] Phi-3-mini OR Qwen2.5-0.5B downloaded and tested
- [ ] HF account active
- [ ] Watched 3Blue1Brown LLM video
- [ ] Watched a diffusion explainer
- [ ] Skimmed Hugging Face Diffusers Quick Tour
- [ ] Course-provided GPU access verified

---

## Reading list (continued learning post-course)

After the course ends, if you want to go deeper:

**LLMs:**
- Karpathy "Let's build GPT" video — implement a tiny GPT from scratch
- Hugging Face course (free): https://huggingface.co/learn
- "The Annotated Transformer" (Harvard NLP)

**Diffusion:**
- Lilian Weng's blog post on diffusion (math-heavy but excellent)
- Hugging Face Diffusers documentation

**LLM applications:**
- LangChain documentation (LLM orchestration)
- LlamaIndex (RAG patterns)
- Anthropic's prompt engineering guide

---

**See you in class — course finale.** Bring your most ambitious questions about modern AI; we'll answer as many as time allows.
