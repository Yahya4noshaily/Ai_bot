from config import AUTO_TRADE
from analyzer import analyze_chart
import time
import random

print("🔄 بدء تشغيل البوت...")
if not AUTO_TRADE:
    print("⏸️ البوت متوقف حاليًا حسب الإعدادات.")
    exit()

def get_chart():
    # محاكاة بيانات الشارت (في النسخة الحقيقية تتصل بـ WebSocket)
    return [{"close": random.uniform(1.12, 1.19)} for _ in range(30)]

while True:
    candles = get_chart()
    signal = analyze_chart(candles)
    if signal:
        print(f"✅ صفقة {signal.upper()} تم تنفيذها.")
        time.sleep(60)
    else:
        print("🔍 لا توجد توصية حالياً.")
        time.sleep(10)
