from login_bot import login_to_eo
from chart_reader import capture_chart
from ai_trader import analyze_chart
from trade_executor import execute_trade
import time

print("🚀 Launching EO Auto AI Trader...")

# 1. تسجيل الدخول
login_to_eo()

# 2. البدء في دورة التداول
while True:
    print("\n📸 Capturing chart...")
    chart = capture_chart()

    print("🧠 Analyzing...")
    signal = analyze_chart(chart)

    if signal:
        print(f"✅ Signal: {signal.upper()}")
        execute_trade(signal)
    else:
        print("⏸️ No valid signal found.")

    time.sleep(30)