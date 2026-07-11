import requests
import pandas as pd

BASE_URL = "https://api.binance.com/api/v3/klines"

def get_klines(symbol, interval="15m", limit=200):
    url = BASE_URL
    params = {
        "symbol": symbol,
        "interval": interval,
        "limit": limit
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    df = pd.DataFrame(data)

    df = df.iloc[:, :6]

    df.columns = [
        "time",
        "open",
        "high",
        "low",
        "close",
        "volume",
    ]

    df["close"] = df["close"].astype(float)
    df["volume"] = df["volume"].astype(float)

    return df
