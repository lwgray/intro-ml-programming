# Week 11 Glossary

---

## LLM Concepts

**LLM (Large Language Model)**
A decoder-only transformer at scale (typically billions of parameters). Trained primarily by next-token prediction on massive text corpora. Examples: GPT-4, Claude, Llama 3, Phi-3, Qwen.

**Foundation model**
A general term for large pretrained models used as starting points for downstream tasks. LLMs are foundation models for language; CLIP is a foundation model for vision-language.

**Decoder-only transformer**
Transformer family that uses only the decoder block, with causal masking so each position only attends to earlier positions. Generates output autoregressively (one token at a time).

**Autoregressive generation**
Generating one token at a time, where each new token is conditioned on all previous tokens (including just-generated ones).

**Next-token prediction**
The training objective. Given the first N tokens, predict the (N+1)th. Compute cross-entropy loss against actual, backprop, update weights, repeat for trillions of tokens.

**Token**
A discrete unit of text. For BERT/GPT-family models, usually a subword. The tokenizer converts text → token IDs.

**Context window**
Maximum number of tokens the model can process at once. Phi-3-mini-4k: 4,000. GPT-4: 128K. Claude: 200K+.

**Emergent capabilities**
Capabilities that appear at scale but not at smaller sizes. Reasoning, code generation, multi-step tasks. Not explicitly trained for — they emerge from pretraining at sufficient scale.

---

## LLM Training Stack

**Pretraining**
Initial training on massive raw text. Predict next token. Output: smart but not aligned. Typically ~10 trillion tokens for a frontier model.

**Instruction tuning (SFT — Supervised Fine-Tuning)**
Fine-tuning on curated (instruction, response) pairs after pretraining. Output: model follows instructions instead of just continuing text.

**RLHF (Reinforcement Learning from Human Feedback)**
Final training stage. Humans rank model outputs from best to worst. Train a reward model on rankings. Use RL to push the LLM toward higher-ranked outputs. Output: helpful, harmless, honest.

**Alignment**
The general practice of making models produce outputs that match human preferences. RLHF is one approach; there are others (DPO, RLAIF).

**Fine-tuning**
Same idea from Weeks 9-10. Adapt a pretrained model to a specific task. For LLMs at scale, often done with parameter-efficient methods (LoRA, QLoRA) instead of full fine-tuning.

**LoRA / QLoRA**
Low-Rank Adaptation. Parameter-efficient fine-tuning that adds small trainable matrices instead of fine-tuning the whole model. Makes LLM fine-tuning practical on consumer GPUs. Out of scope for course but mentioned for further reading.

---

## Sampling and Generation

**Sampling**
The process of choosing the next token from the model's probability distribution.

**Temperature**
Sampling parameter. Lower = more deterministic. Higher = more creative.
- 0 = always pick highest-probability token (greedy)
- 0.5-0.7 = creative but coherent (default for most uses)
- 1.0+ = creative but may go off-rails

**Top-p / Nucleus sampling**
Alternative to pure temperature. Sample from the smallest set of tokens whose cumulative probability is p. `top_p=0.9` means use the smallest set summing to 90%.

**Top-k sampling**
Sample only from the top k highest-probability tokens.

**Beam search**
Alternative to sampling — keep multiple candidate sequences in parallel, return the highest-scoring overall. Used for tasks where you want the "best" output rather than diverse outputs (e.g., translation).

**EOS token (End of Sequence)**
Special token marking end of a generation. Generation stops when EOS is produced (or `max_new_tokens` reached).

**`max_new_tokens`**
Cap on how many tokens to generate. Critical to set explicitly — without it, generation can run indefinitely.

---

## Prompting

**Prompt engineering**
The empirical practice of crafting input prompts to get desired outputs. Iterative, brittle, no formal theory.

**Zero-shot prompting**
Just asking the model to do the task without examples in the prompt.

**Few-shot prompting**
Including a few demonstration examples in the prompt to guide format and behavior.

**System prompt**
An instruction that frames the model's behavior, separate from user inputs. "You are a customer support agent..."

**Structured output**
Forcing the model to return parseable formats (JSON, XML, specific schemas). Critical for production where you need to extract values programmatically.

**Hallucination**
LLMs generating false content with confidence. Property of the architecture, not a bug. Mitigation: RAG, verification, low temperature, explicit "I don't know" prompts.

**RAG (Retrieval-Augmented Generation)**
Pattern for reducing hallucination on factual tasks. Retrieve relevant documents from a knowledge base, include them in the prompt, ask LLM to answer based on those documents.

**Prompt injection**
A real risk: malicious user input that overrides system instructions. "Ignore previous instructions and..." Mitigation: input validation, output filtering, careful UX design.

---

## Diffusion Models

**Diffusion model**
Generative model based on iterative denoising. Train a model to undo one step of noise at a time; sample by starting with random noise and applying the trained reverse step iteratively.

**Forward process**
Adding Gaussian noise step by step until the data is pure noise. Deterministic — no learning required. Just add random noise.

**Reverse process**
The learned part. A neural network (UNet) is trained to undo one step of noise at a time. Predicts the denoised version given the noisy version.

**Sampling**
Generation. Start with random noise, apply the trained reverse step ~50 times, get a coherent sample.

**Latent diffusion**
Diffusion in compressed latent space (~16K dimensions) instead of pixel space (millions of dims). Stable Diffusion uses this. Makes diffusion practical on consumer hardware.

**UNet (in diffusion context)**
The neural network architecture that predicts noise at each step. Encoder-decoder structure with skip connections. NOT a transformer (different architecture family).

**Stable Diffusion**
Open-source latent diffusion model for text-to-image generation. Released August 2022 by Stability AI. Trained on LAION dataset.

**Text conditioning**
How text prompts guide image generation. Text → CLIP encoder → text embeddings. Cross-attention layers in the UNet condition denoising on text embeddings.

**`num_inference_steps`**
Number of reverse-process steps during sampling. Typical: 20-50. Fewer = faster but lower quality.

**`guidance_scale`** (Classifier-Free Guidance)
Controls how strongly the prompt influences the output. 7-9 typical. 0 = ignore prompt. Higher = more prompt-adherence but can over-saturate.

**Negative prompt**
Specifies what NOT to include in the output. "watermark, blurry, low quality, text" is a common one.

**Inpainting**
Diffusion technique for filling in masked regions of an image. Conditional on existing pixels + mask.

**ControlNet**
Extension of diffusion for controlled generation — conditioning on additional inputs like edge maps, depth maps, poses.

---

## Multimodal Models

**CLIP (Contrastive Language-Image Pretraining)**
OpenAI model that maps images and text to a shared embedding space. Trained contrastively on image-text pairs from the web. Foundation for zero-shot image classification AND text-to-image conditioning.

**Zero-shot image classification**
Classifying images into ANY classes specified in text — no per-class training needed. CLIP enables this.

**VLM (Vision-Language Model)**
Models that take BOTH image and text input, output text. Examples: GPT-4V, Claude (with vision), LLaVA, Qwen-VL. Use cases: visual QA, image description.

**Multimodal embedding space**
Shared vector space where different modalities (image, text, audio) are mapped. Enables cross-modal operations: search images by text, find similar items, etc.

**Whisper**
OpenAI's open-source speech-to-text model. Multilingual, very high quality, free.

**Text-to-video**
Generating short video clips from text prompts. Examples: Sora (OpenAI), Veo (Google). Same diffusion idea applied to video tensors.

---

## Closed APIs vs Open Source

**Closed API**
LLMs accessed via paid HTTP API. OpenAI (GPT-3.5, GPT-4), Anthropic (Claude), Google (Gemini). Best capabilities but cost-per-call, ToS restrictions, vendor lock-in.

**Open source LLM**
Model weights freely available, run yourself. Llama (Meta), Mistral, Phi (Microsoft), Qwen (Alibaba), Gemma (Google). Free to run but you manage compute, lower capability than frontier.

**API key**
Authentication token for closed APIs. Must be kept secret. Don't commit to git.

**Rate limit**
Cap on API calls per time period. Free tiers have aggressive limits.

---

## Comparing Architectures

**Encoder-only transformer (Week 10)**
BERT family. Good for understanding tasks. Outputs hidden states for every token.

**Decoder-only transformer (Week 11)**
GPT family. Good for generation tasks. Generates tokens autoregressively.

**Encoder-decoder transformer**
T5/BART family. Good for sequence-to-sequence (translation, summarization). Encoder reads input; decoder generates output.

**Diffusion model**
Different paradigm from transformers. Different architecture (UNet). Different training (denoising). Best for image/video/audio generation.

**CNN (Week 8)**
Different paradigm. Spatial structure. Best for fixed-size images with classification or detection heads.

---

## Course-Wide Concepts

**Gradient descent**
Same algorithm used everywhere from Week 1 (linear regression) to Week 11 (LLMs). Compute gradient of loss with respect to parameters; step in the negative gradient direction.

**Loss function**
Mathematical quantity to minimize. MSE for regression, cross-entropy for classification, denoising loss for diffusion. **All use cases optimize a loss function via gradient descent.**

**Pretraining**
Across modalities: CNNs (ImageNet) → CLIP → BERT → LLMs → Stable Diffusion. The pattern of "train once on big data, adapt to specific tasks" is universal.

**Foundation model**
The general term for large pretrained models that serve as starting points. Universal pattern in modern ML.

---

## Common Misconceptions

**"LLMs know facts."**
False. They predict probable next tokens. Truthfulness is a happy side effect of training data, not guaranteed.

**"Diffusion models edit images."**
False. They generate from noise. Editing (inpainting, ControlNet) is a separate technique layered on top.

**"More parameters always = better."**
Mostly true for capabilities, but smaller models often suffice for specific tasks AND are cheaper to run.

**"Prompt engineering is a stable skill."**
False. Phrasing that works today may not work after a model update.

**"You need to understand transformer math to use LLMs."**
False. The intuition is enough for almost all practical work.

---

**Version:** Week 11 Glossary v1.0 | April 2026
