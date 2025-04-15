import os
import pandas as pd
import ta.trend
import ta.momentum

for file in os.listdir('BTC_USDT'):
    if file.startswith('BTCUSDT_') and file.endswith('.csv'):
        path = os.path.join('BTC_USDT', file)

        try:
            df = pd.read_csv(path)
            close = pd.to_numeric(df['Close'], errors = 'coerce')

            df['5EMA'] = ta.trend.EMAIndicator(close = close, window = 5).ema_indicator()
            df['10EMA'] = ta.trend.EMAIndicator(close = close, window = 10).ema_indicator()
            df['20EMA'] = ta.trend.EMAIndicator(close = close, window = 20).ema_indicator()
            df['RSI'] = ta.momentum.RSIIndicator(close = close, window = 14).rsi()

            MACD = ta.trend.MACD(close = close)
            df['MACD'] = MACD.macd()
            df['Signal'] = MACD.macd_signal()

            df.to_csv(path, index = False)
            print(f'Finish calculate file:{path}')

        except Exception as e:
            print(e)