from binance.client import Client
import pandas as pd
import btalib

api_key = 'eW6Nv6jqbYtrjpFCU8jaP3fzRsymBtLPi8dBuxPHayBBBZVebrtDCnj8Dhw4kmH5'
api_secert = '1sMqGafas3VCh7vUDk1B4IsKsMBBRMNLuxEYqg8yFWKxQHOzop0V2GXOFVmEu2RM'
client = Client(api_key, api_secert)

# valid interval: 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M
interval = ['1m', '3m', '5m', '15m', '30m', '1h', '2h', '4h', '6h', '8h', '12h', '1d', '3d', '1w', '1M']

for i in interval:
    time_stamp = client._get_earliest_valid_timestamp('BTCUSDT', i)

    bars = client.get_historical_klines('BTCUSDT', i, time_stamp, limit = 1000)

    for j in bars:
        del j[5:]
    
    with open(f'BTCUSDT/BTC_USDT_{i}.csv', 'w', encoding = 'utf-8', newline = '') as file:
        df = pd.DataFrame(bars, columns = ['Date', 'Open', 'High', 'Low', 'Close'])
        df['Close'] = pd.to_numeric(df['Close'])
        df.set_index(['Date'], inplace = True)
        df.index = pd.to_datetime(df.index, unit = 'ms')
        
        df['20sma'] = df['Close'].rolling(20).mean()
        df['sma'] = btalib.sma(df['Close'], period = 20).df
        
        rsi = btalib.rsi(df['Close'], period = 14)
        macd = btalib.macd(df['Close'], pfast = 20, pslow = 50, psignal = 13)
        
        df = df.join([rsi.df, macd.df])
        
        df.to_csv(file)