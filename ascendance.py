import sys
import pyautogui

CONFIDENCE = 0.9


def locate_and_click(image_path):
    location = pyautogui.locateOnScreen(image_path, confidence=CONFIDENCE)
    if location is None:
        print(f"Unable to locate {image_path} on screen.")
        return False
    center = pyautogui.center(location)
    pyautogui.click(center)
    return True


def main():
    response = input("Start Ascendance? (Y/N): ").strip().lower()
    if response != "y":
        print("Aborting.")
        return

    pyautogui.keyDown('shift')
    try:
        if not locate_and_click('forge.png'):
            return

        ring_images = [
            'ring1.png',
            'ring2.png',
            'ring3.png',
            'ring4.png',
        ]
        for img in ring_images:
            if locate_and_click(img):
                break
        else:
            print("Unable to locate any ring image on screen.")
    finally:
        pyautogui.keyUp('shift')


if __name__ == "__main__":
    main()
