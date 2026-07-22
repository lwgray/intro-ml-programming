Go to [brev.nvidia.com](https://brev.nvidia.com/), log in, and switch to the **John-Deere2-Brev** org (the `org-3GEO…` id is the same org). Launchables → Create Launchable. For week N:

1. **Code page:** "I have code files in a git repository" → paste `https://github.com/lwgray/intro-ml-programming/blob/main/weekN/README.md` → click "With container(s)" → Next.
    
2. **Container page:** Docker Compose → "I have an existing docker-compose.yaml file" → "Provide GitHub/GitLab URL" → paste `https://github.com/lwgray/intro-ml-programming/blob/main/weekN/brev/docker-compose.yml` → **Validate** → Next.
    
3. **Services page:** choose **"No, I don't want Jupyter"** (the container runs its own). Under Secure Links, rename the port 8888 link to `jupyter`. No other ports. → Next.
    
4. **Compute page:**
    
    |Weeks|Instance|Disk|
    |---|---|---|
    |1–7|CPU · 4 vCPU / 16 GB|64 GB|
    |8–10|GPU · NVIDIA L4 (T4 if unavailable)|128 GB|
    |11|GPU · NVIDIA L4|150 GB|
    
5. **Review page:** name it `intro-ml-weekN` → Create Launchable → View Deploy Page. **Save the deploy-page URL** — that's what students get.