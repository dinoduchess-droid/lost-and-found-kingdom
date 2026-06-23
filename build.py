"""Build script to create EXE using PyInstaller."""

import os
import subprocess
import sys


def build_executable():
    """Build the game into a standalone executable."""
    
    # PyInstaller command
    cmd = [
        "pyinstaller",
        "--onefile",
        "--windowed",
        "--name", "LostAndFoundKingdom",
        "--add-data", "src:src",
        "src/main.py"
    ]
    
    print("Building Lost and Found Kingdom executable...")
    try:
        result = subprocess.run(cmd, check=True)
        print("\n✓ Build successful!")
        print("The executable is located in: dist/LostAndFoundKingdom.exe")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n✗ Build failed: {e}")
        return False


if __name__ == "__main__":
    success = build_executable()
    sys.exit(0 if success else 1)
