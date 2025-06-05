# Ascendance
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
   These should be located in the same folder as the Python scripts so the script can find them.
3. Launch the automation using `start.py` (opens a new terminal):
   ```bash
   python3 start.py
   ```
   The terminal will warn you to stash your equipped rings and amulet before proceeding and ask for confirmation. After confirming, you will be prompted `Ready to ascend!? (Y/N)`.
   If no terminal emulator is available, `start.py` will run `ascendance.py` directly in the current window.

The script holds down the **Shift** key, searches for the provided images on the screen, and clicks their centers when found.

The detection accuracy can be tuned in `ascendance.py` by adjusting the `CONFIDENCE` variable (default `0.9`).