# Week 10 Self-Assessment

Complete after the live session AND post-class HF pipeline exercise.

⚠️ **It's normal to be shaky on attention after Week 10.** That's the hardest week. By Week 11, when you're using transformers more, it'll solidify.

---

## Part 1: Conceptual Understanding (1=lost, 4=could teach it)

| Statement | 1-4 |
|---|---|
| I can explain "attention" in plain English | |
| I understand what Q, K, V represent | |
| I can describe the attention computation steps in order | |
| I understand multi-head attention conceptually | |
| I know why positional encoding exists | |
| I can distinguish encoder-only / decoder-only / encoder-decoder transformer families | |
| I understand the `from_pretrained` pattern (consistent with Week 9) | |
| I know that tokenizer must match model | |
| I can explain why we use a low learning rate when fine-tuning | |
| I understand why transformers replaced RNNs | |

---

## Part 2: Practical Skills

| Skill | Done? |
|---|---|
| Used `pipeline()` for at least 3 different tasks | ☐ |
| Loaded a pretrained model with `AutoModelForSequenceClassification` | ☐ |
| Tokenized data with matching `AutoTokenizer` | ☐ |
| Fine-tuned DistilBERT on AG News in live session | ☐ |
| Visualized attention weights on a real sentence | ☐ |
| Built a custom HF pipeline for personal text task (post-class) | ☐ |
| Fine-tuned DistilBERT on a custom dataset (post-class Part B) | ☐ |
| **Downloaded Phi-3-mini OR Qwen2.5-0.5B** for Week 11 | ☐ |

---

## Part 3: Reflection Questions

### 1. Live session results
- DistilBERT on AG News test accuracy: ___________
- Training time: ___________

### 2. Post-class custom data
- **Task:** ___________
- **Dataset:** ___________ (~N examples per class)
- **Test accuracy:** ___________

### 3. Where in the attention deep-dive did you get lost?
*Be honest. This helps you and instructors.*
___________________________________________

### 4. What's the most useful HF pipeline you found?
*One you could imagine using at work.*
___________________________________________

### 5. Why is transformer fine-tuning so much like CNN fine-tuning?
*One sentence — the cross-week pattern:*
___________________________________________

### 6. What surprised you most about Hugging Face?
___________________________________________

### 7. Pre-2017 alternative
*If you had to build today's text classifier in 2015, what would you have done?*
___________________________________________

### 8. Sleep recommendation
*Did you get enough sleep before the attention deep-dive?* Yes / No
*If no, plan accordingly for Week 11.*

---

## Part 4: Forward Look

### What's the relationship between today's DistilBERT and next week's GPT?
*One sentence:*
___________________________________________

### What do you predict "fine-tune an LLM" means?
___________________________________________

### Pre-class for Week 11
- [ ] Phi-3-mini OR Qwen2.5-0.5B downloaded?
- [ ] HF account active and tokenized?
- [ ] Read the Week 11 pre-class study guide?

---

## Part 5: Self-Score

Add up Part 1 conceptual scores (max 40):
- 36-40: Solid — ready for Week 11
- 28-35: Mostly there — this is honestly fine for Week 10. Re-read the Glossary.
- 20-27: Some gaps — re-watch 3B1B attention video; that's the highest-yield study
- < 20: Office hours strongly recommended — don't go into Week 11 confused

**My score:** ___________ / 40

---

## Continued resources for self-study

If you want to deepen your attention understanding:
1. **Jay Alammar — The Illustrated Transformer:** http://jalammar.github.io/illustrated-transformer/
2. **3Blue1Brown — Attention in Transformers** (re-watch, slowly)
3. **Hugging Face Course (free, self-paced):** https://huggingface.co/learn

---

## Reassurance

Attention is hard. Most ML practitioners take multiple passes to fully internalize it. By Week 11, when you're prompting LLMs, the conceptual foundation will solidify even if it didn't fully click in Week 10.

**See you in Week 11 — course finale.** Generative AI awaits.
