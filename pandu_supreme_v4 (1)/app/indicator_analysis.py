import pandas as pd
import ta

def analyze_indicators(df):
    result = {}

    df = df.copy()
    df['rsi'] = ta.momentum.rsi(df['close'], window=14)
    df['macd'] = ta.trend.macd(df['close'])
    df['macd_signal'] = ta.trend.macd_signal(df['close'])
    df['macd_hist'] = ta.trend.macd_diff(df['close'])
    indicator = df.iloc[-1]

    # RSI
    if indicator.rsi > 70:
        result['rsi'] = 'Overbought'
    elif indicator.rsi < 30:
        result['rsi'] = 'Oversold'
    else:
        result['rsi'] = 'Neutral'

    # MACD
    if indicator.macd > indicator.macd_signal:
        result['macd'] = "Bullish Crossover"
    elif indicator.macd < indicator.macd_signal:
        result['macd'] = "Bearish Crossover"
    else:
        result['macd'] = "Neutral"

    # Bollinger Bands
    indicator['bb_high'] = indicator['close'] + 2*df['close'].rolling(20).std().iloc[-1]
    indicator['bb_low']  = indicator['close'] - 2*df['close'].rolling(20).std().iloc[-1]
    if indicator.close > indicator.bb_high:
        result['bollinger'] = "Breakout Up"
    elif indicator.close < indicator.bb_low:
        result['bollinger'] = "Breakout Down"
    else:
        result['bollinger'] = "Within Bands"

    # Volume Spike
    historical_vol = df['volume'][:-1]
    if indicator['volume'] > historical_vol.mean()*2:  # 2x mean
        result['volume'] = "Volume Spike"
    else:
        result['volume'] = "Normal"

    return result
