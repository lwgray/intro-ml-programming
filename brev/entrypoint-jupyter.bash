#! /bin/bash
#
# Entrypoint for the jupyter service. Runs as root, then switches to user.

set -euo pipefail

# Switch to user and run user-level entrypoint
exec gosu "${IML_TARGET_USER}" /intro-ml-programming/brev/entrypoint-jupyter-user.bash "$@"
