import pyautogui
import time

def capture_chart():
    print("📷 Taking screenshot...")
    time.sleep(2)
    screenshot = pyautogui.screenshot(region=(200, 200, 800, 600))
    path = "chart.png"
    screenshot.save(path)
    return path