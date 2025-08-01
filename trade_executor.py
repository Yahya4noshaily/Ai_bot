import pyautogui
import json
import time

last_result = "none"
last_time = 0

def execute_trade(direction):
    global last_result, last_time
    with open("config.json") as f:
        config = json.load(f)

    if last_result == "loss":
        if time.time() - last_time < config["post_loss_pause"]:
            print("🛑 Post-loss pause active.")
            return

    if direction == "buy":
        pyautogui.click(x=1200, y=700)
    elif direction == "sell":
        pyautogui.click(x=1000, y=700)

    print(f"🚀 Executed {direction.upper()}")

    last_result = "win"
    last_time = time.time()