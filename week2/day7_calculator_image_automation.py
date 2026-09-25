import pyautogui
import time
import os
import subprocess


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "day7_assets")


def click_button(image_name):
    image_path = os.path.join(ASSETS_DIR, image_name)

    if not os.path.exists(image_path):
        print(f"Image not found: {image_path}")
        return False

    print(f"Searching for {image_name}...")

    try:
        position = pyautogui.locateCenterOnScreen(
            image_path,
            confidence=0.8
        )

        if position:
            print(f"Found {image_name} at {position}")
            pyautogui.click(position)
            time.sleep(0.7)
            return True

        print(f"{image_name} not found.")
        return False

    except pyautogui.ImageNotFoundException:
        print(f"{image_name} not found.")
        return False


# -----------------------------------------
# Start Calculator
# -----------------------------------------

print("Opening Calculator...")

subprocess.Popen("calc.exe")

time.sleep(3)


# -----------------------------------------
# Move mouse away from PowerShell
# -----------------------------------------

pyautogui.moveTo(100, 100)

time.sleep(1)


# -----------------------------------------
# Calculator calculation
# -----------------------------------------

print("Performing 7 + 5")

if not click_button("seven.png"):
    exit()

if not click_button("plus.png"):
    exit()

if not click_button("five.png"):
    exit()

if not click_button("equals.png"):
    exit()

print("Calculation completed!")
print("Expected result: 12")