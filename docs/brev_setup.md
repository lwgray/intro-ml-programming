# Brev Launchables for intro-ml-programming

One Launchable per week, backed by five prebuilt Docker images. Every dataset
and model a week needs is baked into its image at build time, so instances boot
warm — nothing downloads on class day.

Modeled on NVIDIA's [accelerated-computing-hub](https://github.com/NVIDIA/accelerated-computing-hub)
Brev architecture: each week has a `weekN/brev/docker-compose.yml` that Brev
consumes, shared entrypoint scripts live in [`brev/`](../brev/), and the images
are defined by the multi-target [`brev/images/dockerfile`](../brev/images/dockerfile).

## The five images

| Image (ghcr.io/lwgray/…) | Weeks | Base | Baked in |
|---|---|---|---|
| `intro-ml-part1` | 1–5 | CPU, python 3.12 | sklearn stack; California Housing, Boston, Adult (OpenML cache), titanic (seaborn cache), UCI offline copies in `/opt/data/uci` |
| `intro-ml-part2` | 6–7 | CPU + torch-cpu + Keras 3 | MNIST, Fashion-MNIST, CIFAR-10 (Keras cache) |
| `intro-ml-vision` | 8–9 | CUDA + torch + Keras 3 + transformers | Keras datasets; MobileNetV2/ResNet50/EfficientNetB0/Xception weights; CLIP; Bingsu/Cat_and_Dog. (The `flowers/` subset ships in the repo itself.) |
| `intro-ml-transformers` | 10 | CUDA + torch + transformers + datasets | DistilBERT (+SQuAD), GPT-2, T5-small, pipeline defaults; AG News, IMDB |
| `intro-ml-genai` | 11 | CUDA + torch + transformers + diffusers | Phi-3-mini-4k-instruct, Qwen2.5-0.5B-Instruct, Stable Diffusion 1.5 (`sd-legacy`), sentiment DistilBERT |

Caches are wired image-wide via `SCIKIT_LEARN_DATA`, `SEABORN_DATA`,
`KERAS_HOME`, and `HF_HOME` (all under `/opt/caches`), so notebooks need no
modification. Keras runs on the PyTorch backend (`KERAS_BACKEND=torch`).

## One-time setup

1. **Publish the images.** Push to `main` (or run the *Build Brev images*
   workflow from the Actions tab). The workflow builds all five targets and
   pushes to ghcr.io.
2. **Make the packages public.** ghcr packages are private by default and Brev
   pulls anonymously. For each of the five packages on GitHub → Profile →
   Packages → *(package)* → Package settings → Change visibility → Public.
   You only do this once per package.
3. Log in at [brev.nvidia.com](https://brev.nvidia.com) and select the course
   organization (**John-Deere2-Brev** — the id `org-3GEOHo3h2VY4OKS8zInjIuMsuGa`
   is the same org; pick whichever the org switcher shows).

## Creating each week's Launchable

Repeat once per week (11 total). Following the ACH click-path, with the
Nsight/TURN pieces removed:

**Code page**
- "I have code files in a git repository" → enter
  `https://github.com/lwgray/intro-ml-programming/blob/main/weekN/README.md`
  (shows as the Launchable description) → "With container(s)" → Next.

**Container page**
- Docker Compose → "I have an existing docker-compose.yaml file" →
  "Provide GitHub/GitLab URL" → enter
  `https://github.com/lwgray/intro-ml-programming/blob/main/weekN/brev/docker-compose.yml`
  → Validate → Next.

**Services page**
- "No, I don't want Jupyter" (the compose file runs its own JupyterLab).
- Under Secure Links, rename the port 8888 link to `jupyter`. No other ports.
- Next.

**Compute page**

| Weeks | Instance | Disk |
|---|---|---|
| 1–7 | CPU · 4 vCPU / 16 GB | 64 GB |
| 8–9 | GPU · NVIDIA L4 22 GB (T4 floor, L40S stretch) | 128 GB |
| 10 | GPU · NVIDIA L4 22 GB | 128 GB |
| 11 | GPU · NVIDIA L4 22 GB | 150 GB |

**Review page**
- Name it `intro-ml-weekN` → Create Launchable → View Deploy Page. Share that
  deploy link with students.

## How it behaves day to day

- **First boot of an instance** pulls the week's image (the big pull; ~2 min for
  CPU weeks, longer for week 11) and populates the `intro-ml-programming`
  volume from the image. JupyterLab opens on the week's day-1 live-session
  notebook.
- **Stop vs. delete:** stopping an instance keeps the volume — student edits
  survive and the next start is instant. Deleting the instance discards edits.
  Tell students: same instance all week; export anything you want to keep
  before the week ends (each week is a separate Launchable/instance).
- **Notebook fixes** land without a rebuild: the base service runs
  `git pull --ff-only` at every boot. Rebuild images only when dependencies,
  prefetch scripts, or entrypoints change (the workflow triggers itself on
  `brev/**` changes).
- **Smoke tests:** deploy with env `IML_RUN_TESTS=1` to run
  `weekN/brev/test.bash` (if present) during the base service; output lands in
  `/intro-ml-programming/logs/test.log`.

## Local development

```bash
# Build one image locally (from the repo root)
docker build -f brev/images/dockerfile --target part1 -t ghcr.io/lwgray/intro-ml-part1:latest .

# Run a week's stack locally
docker compose -f week1/brev/docker-compose.yml up
# JupyterLab: http://localhost:8888
```
