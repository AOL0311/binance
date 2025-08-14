from binance.client import Client
from datetime import datetime, timezone
import pandas as pd
import os

# key 暫時清除，後續寫入 env.py 中
api_key = ''
api_secret = ''

client = Client(api_key, api_secret)

# valid interval: '1M', '1w', '3d', '1d', '12h', '8h', '6h', '4h', '2h', '1h', '30m', '15m', '5m', '3m', '1m'
interval = ['1M', '1w', '3d', '1d', '12h', '8h', '6h', '4h', '2h', '1h']

for i in interval:
    data = client.get_historical_klines('BTCUSDT', i, start_str = '1, Mar, 2020', end_str = '18, Apr, 2025')

    for line in data:
        del line[5:]
        line[0] = datetime.fromtimestamp(line[0] / 1000, tz = timezone.utc).strftime('%Y%m%d%H%M%S')

    df = pd.DataFrame(data, columns = ['Date', 'Open', 'High', 'Low', 'Close'], index = None)

    if os.path.exists(f'BTC_USDT/BTCUSDT_{i}.csv'):
        df.to_csv(f'BTC_USDT/BTCUSDT_{i}.csv', mode = 'a', header = False, index = False)
    else:
        df.to_csv(f'BTC_USDT/BTCUSDT_{i}.csv', mode = 'w', header = True, index = False)

    print(f'Finish fetching time:{i} data.')
