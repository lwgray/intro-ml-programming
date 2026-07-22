#! /bin/bash
#
# User-level entrypoint for the base service. Performs one-time initialization
# when a Launchable is deployed. The named Docker volume is populated from the
# image's baked-in copy of the repo automatically on first mount; this script
# only runs optional smoke tests.

set -euo pipefail

export HOME="${IML_TARGET_HOME}"

# Fast-forward the repo to the latest commit so notebook fixes reach students
# without an image rebuild. The volume was populated from the image's baked-in
# checkout; failures (no network, local edits) are non-fatal.
if [ -d /intro-ml-programming/.git ]; then
  git -C /intro-ml-programming remote set-url origin https://github.com/lwgray/intro-ml-programming.git 2>/dev/null || true
  # Drop any CI auth header baked in by actions/checkout — an expired token
  # makes anonymous pulls fail with a 401/credential prompt.
  git -C /intro-ml-programming config --unset-all http.https://github.com/.extraheader 2>/dev/null || true
  GIT_TERMINAL_PROMPT=0 git -C /intro-ml-programming pull --ff-only 2>&1 | tail -1 || echo "git pull skipped (offline or diverged); using baked-in materials"
fi

if [ -n "${IML_WEEK:-}" ] && [ -n "${IML_RUN_TESTS:-}" ]; then
  TEST_SCRIPT="/intro-ml-programming/${IML_WEEK}/brev/test.bash"
  LOG_DIR="/intro-ml-programming/logs"
  LOG_FILE="${LOG_DIR}/test.log"

  mkdir -p "${LOG_DIR}"

  if [ -f "${TEST_SCRIPT}" ]; then
    {
      echo ""
      echo "=========================================="
      echo "Test Run: $(date '+%Y-%m-%d %H:%M:%S %Z')"
      echo "Week: ${IML_WEEK}"
      echo "=========================================="
    } | tee -a "${LOG_FILE}"

    if bash "${TEST_SCRIPT}" ${IML_TEST_ARGS:-} 2>&1 | tee -a "${LOG_FILE}"; then
      echo "Tests completed successfully for: ${IML_WEEK}" | tee -a "${LOG_FILE}"
    else
      echo "Tests FAILED for: ${IML_WEEK}" | tee -a "${LOG_FILE}"
      exit 1
    fi
  else
    echo "No test script found at: ${TEST_SCRIPT}; skipping tests" | tee -a "${LOG_FILE}"
  fi
else
  echo "IML_RUN_TESTS is empty, skipping tests"
fi
