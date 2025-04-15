import os
import pandas as pd

for file in os.listdir('BTC_USDT'):
    if file.startswith('BTCUSDT_') and file.endswith('.csv'):
        path = os.path.join('BTC_USDT', file)

        try:
            df = pd.read_csv(path)
            df['Date'] = pd.to_datetime(df['Date'], format = '%Y%m%d%H%M%S', errors = 'coerce')
            df = df.dropna(subset = ['Date']).sort_values(by = 'Date')
            df['Date'] = df['Date'].dt.strftime('%Y%m%d%H%M%S')

            df.to_csv(path, index = False)
            print(f'Finish sorting file:{path}')

        except Exception as e:
            print(e)