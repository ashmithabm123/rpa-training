import pyautogui
import time

# Enable PyAutoGUI failsafe
pyautogui.FAILSAFE = True

# Wait before starting
time.sleep(2)

# Open Windows Run dialog
pyautogui.hotkey("win", "r")
time.sleep(2)

# Open Notepad
pyautogui.write("notepad", interval=0.05)
pyautogui.press("enter")
time.sleep(2)

# Select any existing content
pyautogui.hotkey("ctrl", "a")
time.sleep(1)

# Type paragraph
paragraph = (
    "PyAutoGUI is a Python library used for GUI automation. "
    "It can control the mouse and keyboard and interact with applications "
    "through their graphical user interface. "
    "This is useful in RPA for automating repetitive tasks."
)

pyautogui.write(paragraph, interval=0.03)

# Save the file
pyautogui.hotkey("ctrl", "shift", "s")
time.sleep(2)

# Enter file path
pyautogui.write(
    r"C:\Users\Admin\OneDrive - StayAhead (1)\Documents\training\week2\pyautogui_notepad.txt",
    interval=0.02
)

pyautogui.press("enter")
time.sleep(2)

# Handle possible overwrite confirmation
pyautogui.press("left")
pyautogui.press("enter")
time.sleep(2)

# Take screenshot
pyautogui.screenshot(
    r"C:\Users\Admin\OneDrive - StayAhead (1)\Documents\training\week2\notepad_screenshot.png"
)

print("Notepad automation completed successfully.") 