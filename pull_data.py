from binance.client import Client
from datetime import datetime, timezone
import csv

api_key = 'eW6Nv6jqbYtrjpFCU8jaP3fzRsymBtLPi8dBuxPHayBBBZVebrtDCnj8Dhw4kmH5'
api_secret = '1sMqGafas3VCh7vUDk1B4IsKsMBBRMNLuxEYqg8yFWKxQHOzop0V2GXOFVmEu2RM'

client = Client(api_key, api_secret)

# valid interval: '1m', '3m', '5m', '15m', '30m', '1h', '2h', '4h', '6h', '8h', '12h', '1d', '3d', '1w', '1M'
data = client.get_historical_klines('BTCUSDT', '1m', start_str = '1, Mar, 2020', end_str = '8, Apr, 2025')

for lines in data:
    del lines[5:]
    lines[0] = datetime.fromtimestamp(lines[0] / 1000, tz = timezone.utc).strftime('%Y%m%d %H%M%S')

with open('BTC_USDT/BTCUSDT_1Minute.csv', 'w', encoding = 'utf-8') as file:
    writer = csv.writer(file)

    for lines in data:
        writer.writerow(lines)