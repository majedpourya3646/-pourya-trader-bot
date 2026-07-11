from analysis import get_klines
from signals import generate_signal


def build_signal(symbol):

    df = get_klines(symbol)

    result = generate_signal(df)

    if result["signal"] == "HOLD":
        return (
            f"🪙 {symbol}\n\n"
            f"⏸ فعلاً سیگنال معتبری وجود ندارد."
        )

    return (
        f"🚨 SIGNAL\n\n"
        f"🪙 Coin : {symbol}\n"
        f"📈 Action : {result['signal']}\n\n"
        f"💰 Entry : {result['entry']}\n"
        f"🎯 TP : {result['tp']}\n"
        f"🛑 SL : {result['sl']}\n\n"
        f"⭐ Confidence : {result['confidence']}%"
    )
