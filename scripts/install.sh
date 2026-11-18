#!/usr/bin/env bash
set -e

REPO="h45sh/engineering-aggregate"
TARGET_DIR="${HOME}/.agents/skills/engineering-aggregate"
GITHUB_URL="https://github.com/${REPO}.git"

echo "=== Installing engineering-aggregate from GitHub (${REPO}) ==="

mkdir -p "${HOME}/.agents/skills"

if [ -d "${TARGET_DIR}/.git" ]; then
  echo "Updating existing installation in ${TARGET_DIR}..."
  cd "${TARGET_DIR}"
  git pull --ff-only origin main
else
  echo "Cloning ${GITHUB_URL} into ${TARGET_DIR}..."
  rm -rf "${TARGET_DIR}"
  git clone --depth 1 "${GITHUB_URL}" "${TARGET_DIR}"
fi

# Link into active provider skills if directory exists
for dir in "${HOME}/.t3/userdata/providers/antigravity"/*/config/skills; do
  if [ -d "${dir}" ]; then
    echo "Linking skill into $(dirname "${dir}")..."
    ln -sfn "${TARGET_DIR}" "${dir}/engineering-aggregate"
  fi
done

echo "Running self-test..."
python3 "${TARGET_DIR}/scripts/agg.py" test

echo "✅ engineering-aggregate successfully installed and globally active!"
