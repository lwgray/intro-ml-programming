# Reusable prompt: set up Brev Launchables for a new course repo

Copy everything below the line into an LLM coding agent (Claude Code or similar)
opened **inside the new course repo**, after filling in the ALL-CAPS blanks in
the first block. The agent needs shell + file access to the repo; the reference
repo (this one) is public, so the agent can read it from GitHub.

---

## Task

Set up NVIDIA Brev Launchables for this course repository so that each teaching
unit (week/module) gets its own Launchable backed by a prebuilt Docker image
with all of that unit's datasets and models baked in — nothing downloads on
class day.

Fill-in parameters:

- Course repo: `OWNER/NEW-REPO` (GitHub, public, default branch `BRANCH`)
- Container mount path & volume name: `/NEW-REPO`
- Image prefix: `ghcr.io/OWNER/SHORTNAME-`
- Teaching units: describe them, or say "infer from the repo layout"
- Compute per unit: e.g. "units 1–4 CPU (4 vCPU/16 GB), units 5–8 NVIDIA L4",
  or "infer from the frameworks each unit uses"

## Reference implementation — copy this architecture

Study `https://github.com/lwgray/intro-ml-programming` (public), which adapted
NVIDIA's accelerated-computing-hub Brev architecture for a multi-week course.
Read these files and mirror their structure, renaming paths/env prefixes for
this course:

- `brev/` — shared entrypoint scripts (`entrypoint.bash` dispatches to
  base/jupyter/shell; base does one-time init; jupyter runs JupyterLab).
  Note what `entrypoint-base-user.bash` does with git — every line of that
  pull dance exists because something broke without it.
- `brev/images/dockerfile` — ONE dockerfile, multiple publishable targets
  (CPU base → per-part targets; GPU base → per-part targets). Layer order is
  deps → prefetch scripts → `COPY . /repo`, so notebook edits never re-download
  model weights.
- `brev/images/prefetch-*.py` — per-image scripts that bake every runtime
  download into image caches at build time.
- `week*/brev/docker-compose.yml` — one per unit; Brev consumes these by URL.
- `.github/workflows/build-brev-images.yml` — matrix build to ghcr.io.
- `docs/brev_setup.md` — the human-facing runbook to reproduce for this course.

## Method

1. **Inventory the repo.** Map the units and scan every notebook for runtime
   downloads: sklearn fetchers, `keras.datasets`, pretrained-weight loads
   (`weights='imagenet'`), `from_pretrained(...)`, `load_dataset(...)`,
   `hf_hub_download`, bare `read_csv(url)`, etc. Also collect every `import` to
   derive per-image requirements. List what ships in the repo itself vs. what
   downloads at runtime.
2. **Group images.** Aim for FEW shared images behind per-unit launchables
   (units sharing a dependency stack share an image; heavy model weights that
   only one unit needs get that unit its own image). Per-unit compose files
   differ only in image tag, working dir, and start-page notebook.
3. **Build everything**: shared `brev/` scripts, the multi-target dockerfile,
   requirements files, prefetch scripts, per-unit compose files (each opening
   on that unit's main session notebook), the CI workflow, and a
   `docs/brev_setup.md` runbook with the per-unit Launchable creation
   click-path and an instance/disk table.
4. **Validate** what you can locally: every compose file through
   `docker compose config --quiet`, every prefetch script through a syntax
   check, notebooks still valid JSON if you edit any.

## Hard-won constraints — violating any of these caused a real failure

**Git/CI plumbing**
- The workflow's `actions/checkout` MUST set `persist-credentials: false`.
  Otherwise a short-lived CI token is baked into `.git/config` inside the
  image, and every `git pull` on an instance gets a 401 + credential prompt.
- The base entrypoint must, before pulling: force the origin URL to anonymous
  HTTPS, `git config --unset-all http.https://github.com/.extraheader`,
  `git config core.filemode false` (the image COPY chmods everything 0777,
  which git otherwise reports as local changes on every file and refuses to
  pull), and pull with `GIT_TERMINAL_PROMPT=0 ... --ff-only` with a non-fatal
  fallback. Keep `.git` in the image (do NOT dockerignore it) — this pull is
  how notebook fixes reach students without an image rebuild.
- `COPY --chmod=0777 . /NEW-REPO` so the created student user can write
  anywhere in the checkout.

**Jupyter behind Brev's proxy**
- In `jupyter-server-config.py`: empty token/password (auth is Brev's
  secure-link layer), `root_dir '/'`, PLUS `c.ServerApp.allow_origin = '*'`,
  `allow_remote_access = True`, `trust_xheaders = True`. Without allow_origin,
  JupyterLab's sandboxed HTML preview sends `/files/` requests with no Referer
  and Jupyter 403s them ("Blocking request from unknown origin").

**Prefetch correctness**
- Set cache env vars image-wide so notebooks need no modification:
  `SCIKIT_LEARN_DATA`, `SEABORN_DATA`, `KERAS_HOME`, `HF_HOME` under
  `/opt/caches`; `chmod -R a+rwX /opt/caches` after prefetching (the runtime
  user differs from the build user).
- Hugging Face repo ids must be namespaced (`fancyzhx/ag_news`,
  `stanfordnlp/imdb` — bare `ag_news`/`imdb` now raise HfUriError). If
  notebooks use bare ids, FIX THE NOTEBOOKS TOO or class-day fails identically.
  Also verify model repos still exist (e.g. Stable Diffusion 1.5 moved from
  `runwayml/` to `sd-legacy/stable-diffusion-v1-5`).
- Big LLMs: `snapshot_download` (no RAM cost in CI), with ignore_patterns for
  gguf/onnx. Diffusers pipelines: use `from_pretrained` instead — their repos
  carry tens of GB of .ckpt/variant files a blind snapshot would pull.
- Explicitly-named models: hard-fail the build on error. Bare `pipeline(task)`
  defaults: wrap in try/except and log (defaults change across versions).
- `pd.read_csv(url)` never caches — keep offline copies under `/opt/data` as
  outage insurance, and know the notebooks will still hit the network (tiny).
- Keras 3 on torch: set `KERAS_BACKEND=torch` BEFORE any prefetch import; CPU
  images install torch from the `download.pytorch.org/whl/cpu` index.
  Keras application weights are per-resolution for some nets (MobileNetV2) —
  prefetch each input_shape the notebooks use.

**Compose files**
- CPU units' compose must NOT contain the nvidia device reservation (it fails
  on non-GPU instances); GPU units keep it (`driver: nvidia, count: all,
  capabilities: [gpu]`, shm_size 1g). No nsight/TURN services, no docker.sock
  mount, single port 8888.
- Each compose: `base` one-shot service + `jupyter` service depending on it,
  named volume populated from the image, `pull_policy: missing`,
  `default_url` pointing at the unit's session notebook with
  `?file-browser-path=` set to the unit's materials dir. Watch for units with
  nonstandard folder layouts — verify each start notebook path actually exists.

**CI workflow**
- Matrix over image targets; `jlumbroso/free-disk-space` step first (stock
  runners have ~14 GB free; GPU images run 15–25 GB); push `latest` + sha
  tags; `workflow_dispatch` with a target filter input; auto-trigger only on
  `brev/**` paths (notebook edits don't need rebuilds — the boot pull covers
  them); no GHA layer cache for the big images (10 GB cache limit).

## What to hand back to the human

The full file tree you created, plus the runbook (`docs/brev_setup.md`)
containing the steps only a human can do:

1. Push to GitHub; repo must be PUBLIC (Brev fetches the compose by URL
   anonymously; the boot pull is anonymous too).
2. Watch the Actions run; the first build is the real integration test.
3. Make each ghcr package PUBLIC (Settings → Change visibility) — they default
   to private and Brev pulls anonymously; this is the most common silent
   failure (instance boot fails on image pull).
4. Create one Launchable per unit at brev.nvidia.com: Code page → repo README
   URL, "With container(s)"; Container page → Docker Compose → the unit's
   compose file URL → Validate; Services page → "No, I don't want Jupyter",
   rename the 8888 secure link to `jupyter`, no other ports; Compute page →
   per the instance/disk table; name it, create, save the deploy-page URL.
5. Smoke test the lightest and heaviest units: boot, confirm JupyterLab opens
   on the right notebook, run a data-loading cell and confirm NO download
   progress bars, delete the test instance.
6. Student guidance: stop (don't delete) instances between sessions — the
   volume keeps their edits; each unit is a separate instance, so export work
   before week's end.
