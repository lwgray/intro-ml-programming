#! /bin/bash
#
# User-level entrypoint for the jupyter service. Sets up Jupyter and runs it.

set -euo pipefail

export HOME="${IML_TARGET_HOME}"

# Generate JupyterLab user settings (theme, execution timing)
/intro-ml-programming/brev/jupyter-generate-plugin-settings.bash

mkdir -p /intro-ml-programming/logs

# Set the preferred directory to the current working directory, which is set by Docker Compose.
ARGS="--ServerApp.preferred_dir=${PWD:-/}"

if [ -n "${1:-}" ]; then
  ARGS="--LabApp.default_url=${1}"
fi

exec python -m jupyter lab ${ARGS}
