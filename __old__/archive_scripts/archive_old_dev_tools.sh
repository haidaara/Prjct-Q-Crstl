#!/usr/bin/env bash
set -euo pipefail

# Archives old dev_tools scripts that are now redundant.
# Safe: moves to scripts/archive/dev_tools_legacy_<DATE>/
DATE="$(date +%Y%m%d)"
ARCH="scripts/archive/dev_tools_legacy_${DATE}"
mkdir -p "${ARCH}"

# List of old scripts commonly present (move if they exist)
CANDIDATES=(
  "scripts/dev_tools/test_mc_quick.py"
  "scripts/dev_tools/test_mc_temperature.py"
  "scripts/dev_tools/test_temperature_effect.py"
  "scripts/dev_tools/diagnose_temperature_effect.py"
  "scripts/dev_tools/test_temperature_summary.py"
  "scripts/dev_tools/test_energy_sensitivity.py"
  "scripts/dev_tools/quick_control.py"
  "scripts/dev_tools/quick_label_check.py"
  "scripts/dev_tools/verify_label_persistence.py"
  "scripts/dev_tools/check_vertex_class.py"
  "scripts/dev_tools/test_correct_flip.py"
  "scripts/dev_tools/diagnose_flip_physics.py"
  "scripts/dev_tools/calibrate_radius.py"
  "scripts/dev_tools/verify_obstacles.py"
  "scripts/dev_tools/debug_validation.py"
)

for f in "${CANDIDATES[@]}"; do
  if [[ -f "${f}" ]]; then
    mv "${f}" "${ARCH}/"
  fi
done

echo "✅ Archived old dev_tools to: ${ARCH}"
echo "Remaining dev tools should be:"
ls -1 scripts/dev_tools || true
