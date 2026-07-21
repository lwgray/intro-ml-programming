# From Words to Vectors
### The 15-minute on-ramp to attention — read this *before* the 3Blue1Brown video

*You spent Weeks 8–9 on images. An image is **already numbers** — every pixel is a value from
0 to 255, so a neural network can start doing math on it immediately. Text isn't. "The cat sat"
is letters. Before a transformer can do* anything *with a sentence, we have to turn words into
numbers — and this happens in **two small steps**. Today's class quietly assumes you've already
met both. So let's meet them now, gently. Do this first, and nothing later will feel like magic.*

**Time:** ~15 minutes · **You need:** nothing but this page.

---

## The whole idea in one picture

```
   "The cat sat"
        │   STEP 1 — Tokenization:  chop text into pieces, give each a number (an ID)
        ▼
   [CLS]  the   cat   sat  [SEP]        →   IDs:  101  1996  4937  2938  102
        │   STEP 2 — Embedding:  turn each ID into a list of numbers that captures MEANING
        ▼
   a little stack of "meaning vectors", one per token   ←  THIS is what attention works on
```

Two steps: **text → tokens → IDs**, then **IDs → meaning-vectors.** That's it. The rest of
today's class is about what attention *does* with those vectors — but you can't understand that
until you've seen where the vectors come from. So:

---

## Step 1 — Tokenization: turning text into numbered pieces

A network can't consume the letters "cat." It needs a number. So the first job is to **chop the
text into pieces (tokens) and give each piece an ID number.**

**Analogy — a giant dictionary.** Imagine every word filed in a huge dictionary, and instead of
the word you just write down its page number. "the" → 1996, "cat" → 4937. Those numbers are
**token IDs**.

**But models don't store every word — they use *subword* pieces.** English has millions of
words (and typos, and names). So instead of one entry per word, the tokenizer keeps a fixed set
of ~30,000 **pieces** and snaps them together:

```
   "unbelievable"   →   "un"  +  "##believ"  +  "##able"
```

The `##` just means *"glue me onto the piece before me, no space."*

> **Analogy — Lego for words.** A small box of bricks can build almost anything. Subword pieces
> are the bricks: the model can spell a word it has *never seen* by snapping known pieces
> together. That's why it never chokes on a weird word.

**Two special pieces you'll see on screen today.** Every sentence gets wrapped with two
housekeeping tokens:
- **`[CLS]`** goes at the very **front**. Think of it as the model's **scratchpad / summary
  slot** — a place to accumulate "what is this whole sentence about." (When we classify a
  sentence later, we read the answer *out of* `[CLS]`.)
- **`[SEP]`** marks the **end** (or the boundary between two sentences).

So `"The cat sat"` actually becomes:

```
   [CLS]  the  cat  sat  [SEP]
    101  1996 4937 2938   102        (your exact middle IDs will vary by model — [CLS]=101, [SEP]=102 are standard)
```

> ⚠️ **When you see `[CLS]` and `[SEP]` on the attention heatmap in class, that's all they are** —
> the front scratchpad and the end marker. Not magic, not something you missed.

**Quick self-check (guess before you read on):** does the tokenizer treat **"cat"** and
**"cats"** as the *same* thing?
> *No — they're different tokens with different IDs. But — and this is Step 2 — their **meaning
> vectors** will end up very close together, because they mean almost the same thing.*

---

## Step 2 — Embeddings: turning IDs into *meaning*

Here's the problem with a token ID like `4937`: **the number itself is meaningless.** 4937 isn't
"twice as much" as 2938. It's just a name tag. We need each token to become something that
actually captures what the word *means*.

**The fix:** each token ID **looks up a vector** — a list of a few hundred numbers (768 of them
for DistilBERT) — from a big learned table.

```
   ID 4937  ("cat")   →   [ 0.21, -0.83, 0.05, 0.44, ... ]   (768 numbers)
```

That list is called a **word embedding**. Think of it as a **fingerprint for meaning**: a
long code that pins down where the word sits in "meaning space."

**The one property that makes it powerful — similar words get similar vectors.** The model
*learns* this table during training so that words used in similar ways land near each other:

```
   meaning space (cartoon — really it's 768-D):

        kitten                                     run
      cat                                        ran   running
        dog

                                    airplane
                                      rocket
```

`cat`, `kitten`, `dog` cluster together; `run`, `ran`, `running` cluster; `airplane`, `rocket`
are off in their own neighborhood. Nobody hand-placed these — **the network discovered them**,
exactly like a CNN in Week 8 discovered edge-detector filters that no one programmed in. Same
idea: *learn* the representation from data.

> **You don't need the math**, but here's the famous party trick that shows how much structure
> is in there: `king − man + woman ≈ queen`. The vectors literally do meaning-arithmetic. Wild,
> and totally fine to just enjoy.

**The payoff line — remember this one:**
> After these two steps, **"The cat sat" is a small stack of meaning-vectors, one per token.**
> When class says *"we take the input **embedding** and turn it into Q, K, and V"* — **the
> embedding is exactly this.** You've already met it.

---

## The bridge to attention (your friendly first picture)

Here is *all* attention is going to do, in one sentence — the thing the whole 50-minute class
builds up:

> **For each word's meaning-vector, attention looks at every other word's vector, decides which
> ones are relevant, and mixes them in.**

That's why, in "The cat sat on the mat, and *it* was soft," the word **"it"** can reach back and
absorb meaning from **"the mat."** Attention is a **learnable lookup** — a little search engine
inside the network. You don't need to know *how* yet; you just need the picture: *tokens became
vectors, and attention lets the vectors share information.*

---

## Now — and only now — watch the video

**3Blue1Brown — Attention in Transformers:** https://www.youtube.com/watch?v=eMlx5fFNoYc

It'll land far better now that you've met tokens, embeddings, and the one-sentence idea of
attention. And here's the important part:

> **Don't worry if pieces of it feel fuzzy. You are not expected to "get" attention from the
> video.** We rebuild it from scratch, together, on the whiteboard in class — with a running
> example and a live heatmap. The video is a *preview*, not a prerequisite. Come with questions.

---

## What you should be able to say before class (in plain English)

- [ ] **Tokenization:** text gets chopped into subword pieces, each with an ID number; `[CLS]`
  is the front scratchpad, `[SEP]` is the end marker.
- [ ] **Embedding:** each token ID becomes a vector (a few hundred numbers) that captures
  meaning; **similar words get similar vectors**, and the model *learned* that.
- [ ] **Attention (one sentence):** for each word, look at the other words, weight them by
  relevance, and mix them in — a learnable lookup.

If you can say those three, you're ready — and the "hardest week of the course" reputation won't
apply to you, because you're walking in on the *on-ramp*, not the deep end.

---
---

## ✂️ For the instructor — the 4-minute in-class version (drop in at the top of Segment 3)

*Segment 3 currently opens the attention derivation on "we take the same **input embedding** and
pass it through three learned linear layers" (Part 2) — three undefined primitives (embedding,
linear layer, projection) before the search-engine analogy in Part 4. Insert this short beat
**before Part 2** so the machinery arrives pre-anchored. It's the condensed, spoken version of
the primer above.*

**[DRAW ON WHITEBOARD as you talk — two steps, left to right.]**

**SAY:**
> "Before we build attention, 30 seconds on where the numbers even come from — because images
> were already numbers, but text isn't. Two steps."

**ASK STUDENTS (predict):**
> "A network needs numbers. How do you think we turn the word 'cat' into something a network can
> do math on?" **[WAIT — take a guess or two.]**

**SAY (Step 1 — tokenization):**
> "First we **tokenize** — chop the text into pieces and give each a number, an ID. And it's
> *subword* pieces — 'unbelievable' becomes 'un' + '##believ' + '##able', Lego bricks for words.
> Two housekeeping tokens ride along: **`[CLS]`** at the front — the model's summary scratchpad —
> and **`[SEP]`** at the end. *(Point ahead.)* When those show up on our heatmap in a few minutes,
> that's all they are."

**SAY (Step 2 — embeddings, the keeper):**
> "Second — and this is the one that matters for attention — each ID **looks up a vector**: a
> list of ~768 numbers that captures *meaning*. We call it a **word embedding**. The magic is
> that **similar words get similar vectors** — 'cat' and 'kitten' land right next to each other —
> and the model *learned* that, exactly like Week 8's CNN learned edge filters nobody coded. So
> our sentence is now a little stack of meaning-vectors, one per token. **That** stack is the
> 'input embedding' I'm about to turn into Q, K, and V."

**TRANSITION →**
> "Okay — we've got meaning-vectors. Now: attention is going to let each vector look at the
> others and pull in what's relevant. Let's build exactly how — it works like a search engine
> inside the network." *(→ into Part 2, now with the search-engine framing seeded up front.)*

*(Also add the one-liner before the heatmap in Part 8: "Those `[CLS]`/`[SEP]` on the axes — the
scratchpad and the end marker from our on-ramp; `[CLS]` often soaks up a lot of attention as a
'nothing-specific' resting spot.")*

---
*Draft v1 — serves two homes: (1) the pre-class on-ramp above, and (2) the 4-minute in-class
Seg-3 beat. Pair with the framing fixes to the pre-class study guide (reposition the 3B1B video
as reinforcement; remove the "class won't re-derive / hardest week, brace yourself" lines).*
