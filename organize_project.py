import os
import shutil
import sys
import subprocess
from pathlib import Path

# ==========================================
# ⚙️ CONFIGURATION
# ==========================================
# Validate imports? (False = safer, won't touch code)
AUTO_FIX_SYSPATH = False 

# Move unknown files? (False = safer, leaves them where they are)
MOVE_UNKNOWN_TO_ARCHIVE = False

# ==========================================
# 🗺️ MAPPING
#Format: "Old_Name": ("New_Folder", "New_Name")
# ==========================================
MOVES = {
    # --- 1. EXPERIMENTS ---
    "run_milestone1.py":            ("experiments", "01_generate_tiling.py"),
    "run_milestone2_obstacle.py":   ("experiments", "02_generate_obstacles.py"),
    "test_manual_defects.py":       ("experiments", "03_run_healing_test.py"),
    "run_growth_experiment.py":     ("experiments", "04_run_growth.py"),
    "temperature_sweep_physics.py": ("experiments", "05_temperature_sweep.py"),

    # --- 2. VALIDATION ---
    "quick_verify_fixes.py":        ("validation", "quick_verify_fixes.py"),
    "verify_energy_consistency.py": ("validation", "verify_energy_consistency.py"),
    "debug_energy_consistency.py":  ("validation", "debug_energy_consistency.py"),
    "validate_energy_consistency.py": ("validation", "validate_energy_consistency.py"),
    "validate_week1_physics.py":    ("validation", "validate_week1_physics.py"),
    "test_neighborhood_radius.py":  ("validation", "calibrate_radius.py"),
    "verify_obstacles.py":          ("validation", "verify_obstacles.py"),
    "validate_robust_flip.py":      ("validation", "validate_robust_flip.py"),

    # --- 3. ANALYSIS ---
    "diagnose_energy_landscape_fixed.py": ("analysis", "plot_energy_landscape.py"),
    "analyze_temperature_results.py":     ("analysis", "analyze_temperature_results.py"),
    "analyze_growth_results.py":          ("analysis", "analyze_growth_results.py"),
    "debug_energy_distribution.py":       ("analysis", "debug_energy_distribution.py"),

    # --- 4. DEV TOOLS ---
    "debug_energy_model.py":           ("dev_tools", "debug_energy_model.py"),
    "debug_validation.py":             ("dev_tools", "debug_validation.py"),
    "diagnose_active_region_flips.py": ("dev_tools", "diagnose_active_region_flips.py"),
    "diagnose_flip_physics.py":        ("dev_tools", "diagnose_flip_physics.py"),
    "diagnose_temperature_effect.py":  ("dev_tools", "diagnose_temperature_effect.py"),
    "check_vertex_class.py":           ("dev_tools", "check_vertex_class.py"),
    "quick_label_check.py":            ("dev_tools", "quick_label_check.py"),
    "verify_label_persistence.py":     ("dev_tools", "verify_label_persistence.py"),
    "test_correct_flip.py":            ("dev_tools", "test_correct_flip.py"),
    "test_energy_sensitivity.py":      ("dev_tools", "test_energy_sensitivity.py"),
    "test_mc_quick.py":                ("dev_tools", "test_mc_quick.py"),
    "test_mc_temperature.py":          ("dev_tools", "test_mc_temperature.py"),
    "test_temperature_effect.py":      ("dev_tools", "test_temperature_effect.py"),
    "test_temperature_summary.py":     ("dev_tools", "test_temperature_summary.py"),
    "quick_control.py":                ("dev_tools", "quick_control.py"),
    "system_diagnostic.py":            ("dev_tools", "system_diagnostic.py"),

    # --- 5. ARCHIVE ---
    "diagnose_energy_landscape.py":    ("archive", "diagnose_energy_landscape.py"),
    "diagnose_mc_healing.py":          ("archive", "diagnose_mc_healing.py"),
    "test_growth_baseline.py":         ("archive", "test_growth_baseline.py"),
    "test_quick_growth.py":            ("archive", "test_quick_growth.py"),
    "run_week2.py":                    ("archive", "run_week2.py"),
    "archive_obstacles.py":            ("archive", "archive_obstacles.py"),
}

def create_in_place_wrapper(original_path, new_rel_path):
    """
    Creates a wrapper at the OLD location that points to the NEW location.
    Preserves commands like 'python scripts/old_name.py'
    """
    content = f"""#!/usr/bin/env python3
\"\"\"
LEGACY WRAPPER: Forwards to {new_rel_path}
\"\"\"
import os
import sys
import subprocess

# Path to the new script relative to the project root
NEW_SCRIPT = "scripts/{new_rel_path}"

def main():
    # Calculate absolute path to the project root
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir, ".."))
    script_path = os.path.join(project_root, NEW_SCRIPT)
    
    print(f"⏩ Forwarding execution to: {{NEW_SCRIPT}}")
    
    # Execute the new script, passing all arguments
    result = subprocess.run([sys.executable, script_path] + sys.argv[1:])
    sys.exit(result.returncode)

if __name__ == "__main__":
    main()
"""
    with open(original_path, 'w') as f:
        f.write(content)

def update_sys_path(file_path):
    """Only runs if AUTO_FIX_SYSPATH is True"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        new_lines = []
        modified = False
        
        for line in lines:
            if "sys.path.append('..')" in line:
                 new_lines.append("sys.path.append('../..') # Auto-updated\n")
                 modified = True
            else:
                new_lines.append(line)
            
        if modified:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.writelines(new_lines)
            print(f"    🔧 Updated sys.path in {file_path.name}")
    except Exception as e:
        print(f"    ⚠️ Failed to update sys.path: {e}")

def main():
    print("🧹 STARTING SAFE REORGANIZATION")
    print("=" * 60)
    
    base_scripts_dir = Path("scripts")
    if not base_scripts_dir.exists():
        print("❌ Error: 'scripts' directory not found.")
        return

    # 1. Create Directories
    print("\n1️⃣  Creating folders...")
    folders = ["experiments", "validation", "analysis", "dev_tools", "archive"]
    for folder in folders:
        target = base_scripts_dir / folder
        target.mkdir(exist_ok=True)
        (target / "__init__.py").touch()

    # 2. Move Files
    print("\n2️⃣  Moving files & Creating Wrappers...")
    
    for item in base_scripts_dir.iterdir():
        if item.is_dir() or item.name == "organize_project_safe.py":
            continue
            
        old_name = item.name
        
        if old_name in MOVES:
            target_folder, target_name = MOVES[old_name]
            
            src_path = item
            dest_folder_path = base_scripts_dir / target_folder
            dest_path = dest_folder_path / target_name
            
            # Move the actual file
            print(f"   Moving: {old_name} -> {target_folder}/{target_name}")
            shutil.move(str(src_path), str(dest_path))
            
            # Optional: Fix imports
            if AUTO_FIX_SYSPATH:
                update_sys_path(dest_path)
            
            # Create Wrapper in the ORIGINAL location
            # This ensures 'python scripts/old_name.py' still works
            create_in_place_wrapper(src_path, f"{target_folder}/{target_name}")
            
        else:
            if old_name not in ["__init__.py", "README.md", "execution order.txt"]:
                 if MOVE_UNKNOWN_TO_ARCHIVE and old_name.endswith(".py"):
                     print(f"   ⚠️  Unknown script '{old_name}' -> moving to archive/")
                     shutil.move(str(item), str(base_scripts_dir / "archive" / old_name))
                 elif old_name.endswith(".py"):
                     print(f"   ℹ️  Skipping unknown script: {old_name} (Safety Mode)")

    print("\n" + "="*60)
    print("✅ REORGANIZATION COMPLETE")
    print("="*60)
    print("New structure created.")
    print("Wrappers created in place, so your old commands still work.")
    print("\nTry running your main healing experiment (new path):")
    print("  python scripts/experiments/03_run_healing_test.py")
    print("\nOr use the old command (wrapper):")
    print("  python scripts/test_manual_defects.py")

if __name__ == "__main__":
    main()