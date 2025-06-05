# Ascendance

This repository provides a small Python script that automates mouse clicks based on image recognition.

## Usage

1. Install dependencies:
   ```bash
   pip install pyautogui
   ```
2. Place your reference images in the repository directory:
   - `forge.png` for the forge process.
   - `ring1.png`, `ring2.png`, `ring3.png`, `ring4.png` for the ring process.
3. Run the script:
   ```bash
   python3 ascendance.py
   ```
   When prompted with `Start Ascendance? (Y/N):`, press `Y` to start or `N` to abort.

The script holds down the **Shift** key, searches for the provided images on the screen, and clicks their centers when found.
