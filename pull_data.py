from binance.client import Client
from datetime import datetime, timezone
import csv

api_key = 'eW6Nv6jqbYtrjpFCU8jaP3fzRsymBtLPi8dBuxPHayBBBZVebrtDCnj8Dhw4kmH5'
api_secret = '1sMqGafas3VCh7vUDk1B4IsKsMBBRMNLuxEYqg8yFWKxQHOzop0V2GXOFVmEu2RM'

client = Client(api_key, api_secret)

# valid interval: '1m', '3m', '5m', '15m', '30m', '1h', '2h', '4h', '6h', '8h', '12h', '1d', '3d', '1w', '1M'
interval = ['1d', '1w']
for i in interval:
    data = client.get_historical_klines('BTCUSDT', i, start_str = '1, Mar, 2020', end_str = '12, Apr, 2025')

    for lines in data:
        del lines[5:]
        lines[0] = datetime.fromtimestamp(lines[0] / 1000, tz = timezone.utc).strftime('%Y%m%d %H%M%S')

    if i == '1m':
        File = 'BTC_USDT/BTCUSDT_1Minute.csv'
    elif i == '3m':
        File = 'BTC_USDT/BTCUSDT_3Minute.csv'
    elif i == '5m':
        File = 'BTC_USDT/BTCUSDT_5Minute.csv'
    elif i == '15m':
        File = 'BTC_USDT/BTCUSDT_15Minute.csv'
    elif i == '30m':
        File = 'BTC_USDT/BTCUSDT_30Minute.csv'
    elif i == '1h':
        File = 'BTC_USDT/BTCUSDT_1Hour.csv'
    elif i == '2h':
        File = 'BTC_USDT/BTCUSDT_2Hour.csv'
    elif i == '4h':
        File = 'BTC_USDT/BTCUSDT_4Hour.csv'
    elif i == '6h':
        File = 'BTC_USDT/BTCUSDT_6Hour.csv'
    elif i == '8h':
        File = 'BTC_USDT/BTCUSDT_8Hour.csv'
    elif i == '12h':
        File = 'BTC_USDT/BTCUSDT_12Hour.csv'
    elif i == '1d':
        File = 'BTC_USDT/BTCUSDT_1Day.csv'
    elif i == '3d':
        File = 'BTC_USDT/BTCUSDT_3Day.csv'
    elif i == '1w':
        File = 'BTC_USDT/BTCUSDT_1Week.csv'
    elif i == '1M':
        File = 'BTC_USDT/BTCUSDT_1Month.csv'

    with open(File, 'a+', encoding = 'utf-8', newline = '') as file:
        writer = csv.writer(file)
        writer.writerows(data)