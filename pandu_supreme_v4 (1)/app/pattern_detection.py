import numpy as np
import pandas as pd

def detect_patterns(df):
    signals = []
    if len(df) < 30:  # Not enough data
        return signals

    # Double Top/Bottom detection (very basic)
    highs = df['high'][-30:]
    lows = df['low'][-30:]
    if highs.max() == highs[-1] and highs.max() == highs[-15]:
        signals.append({'pattern': 'Double Top'})
    if lows.min() == lows[-1] and lows.min() == lows[-15]:
        signals.append({'pattern': 'Double Bottom'})
    # TODO: Add advanced logic for triangles, wedges
    return signals
