#!/usr/bin/env python3
"""
🔍 STANDALONE OBSTACLE VERIFICATION SCRIPT
Run this anytime to verify obstacle creation results and check all fixes
"""

import json
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from src.obstacle.obstacle_creator import adjacency_intkeys_to_str


# Add project root to path to import modules
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

def main():
    """Run comprehensive verification on obstacle data"""
    print("🔍 OBSTACLE CREATION VERIFICATION")
    print("=" * 50)
    
    obstacle_dir = project_root / "data" / "obstacles"
    if not obstacle_dir.exists():
        print("❌ No obstacle data found - run Milestone 2 first")
        print("   Run: python run_milestone2_obstacle.py")
        return False
    
    verification_results = []
    
    # Check all pore files
    pore_files = list(obstacle_dir.glob("pores/*.json"))
    print(f"\n📁 Checking {len(pore_files)} pore configurations...")
    for pore_file in pore_files:
        with open(pore_file, 'r') as f:
            data = json.load(f)
        checks = verify_obstacle_data(data, pore_file.stem)
        verification_results.extend(checks)
        print(f"   {pore_file.stem}: {sum(1 for c in checks if c['status']=='PASS')}/{len(checks)} passed")
    
    # Check all fixed_defect files  
    defect_files = list(obstacle_dir.glob("fixed_defects/*.json"))
    print(f"\n📁 Checking {len(defect_files)} fixed defect configurations...")
    for defect_file in defect_files:
        with open(defect_file, 'r') as f:
            data = json.load(f)
        checks = verify_obstacle_data(data, defect_file.stem)
        verification_results.extend(checks)
        print(f"   {defect_file.stem}: {sum(1 for c in checks if c['status']=='PASS')}/{len(checks)} passed")
    
    # Generate comprehensive report
    return generate_verification_report(verification_results, obstacle_dir)

def verify_obstacle_data(obstacle_data, spec_name):
    """Verify key obstacle creation fixes"""
    checks = []
    
    # Check 1: Adjacency graph keys are strings (JSON compatibility)
    adj_keys = list(obstacle_data["adjacency_graph"].keys())
    check1 = {
        "test": "Adjacency graph keys are strings",
        "spec": spec_name,
        "status": "PASS" if adj_keys and all(isinstance(k, str) for k in adj_keys) else "FAIL",
        "details": f"Found {len(adj_keys)} adjacency entries"
    }
    checks.append(check1)
    
    # Check 2: Removed tiles have empty neighbor lists
    removed_tiles = [t for t in obstacle_data["tiles"] if t.get("removed", False)]
    check2 = {
        "test": "Removed tiles have empty neighbor lists", 
        "spec": spec_name,
        "status": "PASS" if all(len(t["neighbors"]) == 0 for t in removed_tiles) else "FAIL",
        "details": f"Checked {len(removed_tiles)} removed tiles"
    }
    checks.append(check2)
    
    # Check 3: Fixed defects are properly marked
    if "fixed_defects" in spec_name:
        fixed_tiles = [t for t in obstacle_data["tiles"] if t.get("immobile", False)]
        check3 = {
            "test": "Fixed defects marked as immobile",
            "spec": spec_name,
            "status": "PASS" if all(t.get("obstacle_type") == "fixed_defect" for t in fixed_tiles) else "FAIL",
            "details": f"Found {len(fixed_tiles)} fixed defects"
        }
        checks.append(check3)
    
    # Check 4: Pores have proper metadata
    if "pores" in spec_name:
        meta = obstacle_data.get("obstacle_metadata", {})
        check4 = {
            "test": "Pores have positions and radii",
            "spec": spec_name, 
            "status": "PASS" if meta.get("positions") and meta.get("radii") else "FAIL",
            "details": f"Positions: {len(meta.get('positions', []))}, Radii: {len(meta.get('radii', []))}"
        }
        checks.append(check4)
        
        # Additional pore check: positions and radii arrays match
        if meta.get("positions") and meta.get("radii"):
            check5 = {
                "test": "Pore positions and radii arrays match",
                "spec": spec_name,
                "status": "PASS" if len(meta["positions"]) == len(meta["radii"]) else "FAIL",
                "details": f"Positions: {len(meta['positions'])}, Radii: {len(meta['radii'])}"
            }
            checks.append(check5)
    
    # Check 6: No contradictory tile states (removed + immobile)
    contradictory_tiles = [t for t in obstacle_data["tiles"] if t.get("removed", False) and t.get("immobile", False)]
    check6 = {
        "test": "No contradictory tile states (removed + immobile)",
        "spec": spec_name,
        "status": "PASS" if len(contradictory_tiles) == 0 else "FAIL",
        "details": f"Found {len(contradictory_tiles)} contradictory tiles"
    }
    checks.append(check6)
    
    # Check 7: Obstacle metadata exists and is complete
    meta = obstacle_data.get("obstacle_metadata", {})
    check7 = {
        "test": "Obstacle metadata complete",
        "spec": spec_name,
        "status": "PASS" if meta and "type" in meta and "density" in meta else "FAIL",
        "details": f"Type: {meta.get('type')}, Density: {meta.get('density')}"
    }
    checks.append(check7)
    
    return checks

def generate_verification_report(verification_results, obstacle_dir):
    """Generate comprehensive verification report"""
    total_checks = len(verification_results)
    passed_checks = sum(1 for r in verification_results if r["status"] == "PASS")
    failed_checks = sum(1 for r in verification_results if r["status"] == "FAIL")
    
    print(f"\n📊 VERIFICATION SUMMARY")
    print("=" * 50)
    print(f"   Total checks: {total_checks}")
    print(f"   ✅ PASSED: {passed_checks}")
    print(f"   ❌ FAILED: {failed_checks}")
    print(f"   📈 SUCCESS RATE: {passed_checks/total_checks*100:.1f}%")
    
    # Show detailed failures
    if failed_checks > 0:
        print(f"\n🚨 DETAILED FAILURES:")
        print("-" * 30)
        
        # Group by spec for better organization
        failed_by_spec = {}
        for check in verification_results:
            if check["status"] == "FAIL":
                spec = check["spec"]
                if spec not in failed_by_spec:
                    failed_by_spec[spec] = []
                failed_by_spec[spec].append(check)
        
        for spec, failures in failed_by_spec.items():
            print(f"\n   📂 {spec}:")
            for failure in failures:
                print(f"      • {failure['test']}")
                print(f"        Details: {failure['details']}")
    
    # Show key fixes that passed
    print(f"\n✅ KEY FIXES VERIFIED:")
    print("-" * 25)
    key_fixes = [
        "Adjacency graph keys are strings",
        "Removed tiles have empty neighbor lists", 
        "No contradictory tile states",
        "Obstacle metadata complete"
    ]
    
    for fix in key_fixes:
        fix_checks = [c for c in verification_results if c["test"] == fix]
        if fix_checks:
            passed = sum(1 for c in fix_checks if c["status"] == "PASS")
            total = len(fix_checks)
            status = "✅" if passed == total else "❌"
            print(f"   {status} {fix}: {passed}/{total}")
    
    # Save detailed report
    import time
    report = {
        "timestamp": time.time(),
        "total_checks": total_checks,
        "passed_checks": passed_checks,
        "failed_checks": failed_checks,
        "success_rate": passed_checks/total_checks*100,
        "results": verification_results
    }
    
    report_file = obstacle_dir / "verification_report.json"
    with open(report_file, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\n📄 Detailed report saved: {report_file}")
    
    # Return overall status
    if failed_checks == 0:
        print(f"\n🎉 ALL CHECKS PASSED! Obstacle creation is working correctly.")
        return True
    else:
        print(f"\n⚠️  Some checks failed. Review the issues above.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)