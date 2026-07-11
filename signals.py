import ta


def generate_signal(df):
    """
    Generate BUY / SELL / HOLD signal
    """

    close = df["close"]

    rsi = ta.momentum.RSIIndicator(close=close, window=14).rsi()

    ema20 = ta.trend.EMAIndicator(close=close, window=20).ema_indicator()
    ema50 = ta.trend.EMAIndicator(close=close, window=50).ema_indicator()

    last_price = float(close.iloc[-1])

    last_rsi = float(rsi.iloc[-1])

    last_ema20 = float(ema20.iloc[-1])

    last_ema50 = float(ema50.iloc[-1])

    if last_rsi < 30 and last_ema20 > last_ema50:
        return {
            "signal": "BUY",
            "entry": round(last_price, 4),
            "tp": round(last_price * 1.03, 4),
            "sl": round(last_price * 0.98, 4),
            "confidence": 88,
        }

    if last_rsi > 70 and last_ema20 < last_ema50:
        return {
            "signal": "SELL",
            "entry": round(last_price, 4),
            "tp": round(last_price * 0.97, 4),
            "sl": round(last_price * 1.02, 4),
            "confidence": 86,
        }

    return {
        "signal": "HOLD",
        "entry": round(last_price, 4),
        "tp": None,
        "sl": None,
        "confidence": 0,
    }
