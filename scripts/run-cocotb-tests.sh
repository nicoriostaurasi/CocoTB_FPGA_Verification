#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-/work}"
ROOT="$(cd "$ROOT" && pwd)"

mapfile -t MAKEFILES < <(find "$ROOT" -name Makefile -type f | sort)

if [[ ${#MAKEFILES[@]} -eq 0 ]]; then
  echo "No Makefiles found under $ROOT" >&2
  exit 1
fi

FAILED=()

for makefile in "${MAKEFILES[@]}"; do
  test_dir="$(dirname "$makefile")"
  rel_dir="${test_dir#$ROOT/}"

  echo
  echo "==> $rel_dir"

  if ! make -C "$test_dir" clean icarus=sim; then
    FAILED+=("$rel_dir")
    continue
  fi

  if ! make -C "$test_dir" icarus=sim; then
    FAILED+=("$rel_dir")
  fi
done

echo
if [[ ${#FAILED[@]} -eq 0 ]]; then
  echo "All cocotb tests passed (${#MAKEFILES[@]} test directories)."
else
  echo "Failed cocotb test directories:" >&2
  printf ' - %s\n' "${FAILED[@]}" >&2
  exit 1
fi
