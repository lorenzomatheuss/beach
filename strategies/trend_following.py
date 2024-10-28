# strategies/trend_following.py

import talib
import pandas as pd

def trend_following_strategy(df):
    """
    Implementação da estratégia de Trend Following usando Médias Móveis Simples (SMA).
    """
    df['SMA_short'] = talib.SMA(df['close'], timeperiod=9)
    df['SMA_long'] = talib.SMA(df['close'], timeperiod=21)

    df['buy_signal'] = (df['SMA_short'] > df['SMA_long']) & (df['SMA_short'].shift(1) <= df['SMA_long'].shift(1))
    df['sell_signal'] = (df['SMA_short'] < df['SMA_long']) & (df['SMA_short'].shift(1) >= df['SMA_long'].shift(1))

    return df
