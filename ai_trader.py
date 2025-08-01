import cv2
import numpy as np

def analyze_chart(image_path):
    print("🧪 Reading chart...")
    img = cv2.imread(image_path)

    if img is None:
        print("❌ Failed to load image.")
        return None

    avg_color = img.mean(axis=0).mean(axis=0)
    red, green, blue = avg_color

    if green > red + 10:
        return "buy"
    elif red > green + 10:
        return "sell"
    else:
        return None