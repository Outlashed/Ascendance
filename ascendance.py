import sys
import time
from pathlib import Path
import pyautogui

CONFIDENCE = 0.9
SCRIPT_DIR = Path(__file__).resolve().parent


def locate_and_click(image_name, button='left'):
    image_path = SCRIPT_DIR / image_name
    location = pyautogui.locateOnScreen(str(image_path), confidence=CONFIDENCE)
    if location is None:
        print(f"Unable to locate {image_path} on screen.")
        return False
    center = pyautogui.center(location)
    pyautogui.click(center, button=button)
    return True


def main():
    print(
        "Put equipped rings and amulet in your stash before proceeding - If you wanna be ultra-safe: Take all your equipped gear off and put it in your stash first."
    )
    confirm = input("Confirm you've taken off your gear and put it in your stash: Y/N ").strip().lower()
    if confirm != "y":
        print("Since you said you didn't put your items in your stash, if your equipped gear gets ascended or the program bugs out; it's ON YOU.")
    else:
        print("Alright, you're safe - Let's proceed.")

    ready = input("Ready to ascend!? (Y/N): ").strip().lower()
    if ready != "y":
        print("No ascension feelsbadman")
        time.sleep(3)
        return

    pyautogui.keyDown("shift")
    try:
        ring_images = [
            "ring1.png",
            "ring2.png",
            "ring3.png",
            "ring4.png",
        ]
        while True:
            if not locate_and_click("forge.png"):
                break
            time.sleep(0.2)

            found = False
            for img in ring_images:
                if locate_and_click(img, button="right"):
                    found = True
                    break

            if not found:
                print("No more ring images found.")
                break

            time.sleep(0.2)
            if not locate_and_click("forge.png"):
                break
    finally:
        pyautogui.keyUp("shift")


if __name__ == "__main__":
    main()