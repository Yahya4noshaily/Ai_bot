# تحليل الشارت باستخدام استراتيجيات ومؤشرات متعددة
def analyze_chart(candles):
    # مؤشرات تحليل بسيطة - MACD + RSI + EMA
    if len(candles) < 20:
        return None
    close_prices = [c['close'] for c in candles]
    ema10 = sum(close_prices[-10:]) / 10
    ema20 = sum(close_prices[-20:]) / 20
    rsi = 100 - (100 / (1 + sum([max(0, close_prices[i] - close_prices[i-1]) for i in range(1, 15)]) /
                            sum([max(0, close_prices[i-1] - close_prices[i]) for i in range(1, 15)])))
    macd = ema10 - ema20

    if macd > 0 and rsi > 55:
        return "buy"
    elif macd < 0 and rsi < 45:
        return "sell"
    return None
