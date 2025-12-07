#!/usr/bin/env python3
"""
Simple obstacle archiving utility - run this before milestone2 to clean data
"""

import shutil
from pathlib import Path
from datetime import datetime

def main():
    """Archive existing obstacle data to prevent mixing"""
    obstacle_dir = Path("data/obstacles")
    archive_base = Path("data/obstacles_archive")
    
    # Check if obstacle directory exists and has content
    if not obstacle_dir.exists() or not any(obstacle_dir.iterdir()):
        print("📁 No existing obstacle data found - nothing to archive")
        return
    
    # Create archive directory with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archive_path = archive_base / f"obstacles_{timestamp}"
    
    try:
        # Create archive directory
        archive_path.mkdir(parents=True, exist_ok=True)
        
        # Move obstacle directory to archive
        shutil.move(str(obstacle_dir), str(archive_path / "obstacles"))
        print(f"📦 Archived existing data to: {archive_path}")
        
        # Recreate empty obstacle directory
        obstacle_dir.mkdir(parents=True, exist_ok=True)
        print("✅ Clean obstacle directory ready for new data")
        
    except Exception as e:
        print(f"❌ Archive failed: {e}")

if __name__ == "__main__":
    main()