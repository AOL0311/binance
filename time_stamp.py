import os
from binance.client import Client
import csv
from datetime import datetime, timezone
import numpy as np

api_key = os.getenv('test_api_key')
api_secret = os.getenv('test_api_secret')
#api_key = 'eW6Nv6jqbYtrjpFCU8jaP3fzRsymBtLPi8dBuxPHayBBBZVebrtDCnj8Dhw4kmH5'
#api_secret = '1sMqGafas3VCh7vUDk1B4IsKsMBBRMNLuxEYqg8yFWKxQHOzop0V2GXOFVmEu2RM'

client = Client(api_key, api_secret)

# valid interval: '1m', '3m', '5m', '15m', '30m', '1h', '2h', '4h', '6h', '8h', '12h', '1d', '3d', '1w', '1M'
interval = ['1m']

# def calculate_rsi(prices, period = 14):
    # gains = []
    # losses = []

    # for i in range(1, len(prices)):
    #     if prices[i] - prices[i - 1] > 0:
    #         gains.append(prices[i] - prices[i - 1])
    #         losses.append(0)
    #     else:
    #         losses.append(abs(prices[i] - prices[i - 1]))
    #         gains.append(0)

    # avg_gain = np.mean(gains[-period:])
    # avg_loss = np.mean(losses[-period:])

    # return f'{100 - (100 / (1 + avg_gain / avg_loss if avg_loss != 0 else 0)):.8f}'

# def calculate_ema(prices, period, previous_ema = None):
    # alpha = 2 / (period + 1)

    # if previous_ema is None:
    #     previous_ema = prices[0]

    # ema_values = [previous_ema]
    # for i in prices[1:]:
    #     current_ema = (i - ema_values[-1]) * alpha + ema_values[-1]
    #     ema_values.append(current_ema)

    # return ema_values[-1]

def calculate_macd(prices, short_period = 12, long_period = 26, signal_period = 9):
    short_ema = [calculate_ema(prices[:i], short_period) for i in range(1, len(prices) + 1)]
    long_ema = [calculate_ema(prices[:i], long_period) for i in range(1, len(prices) + 1)]

#     macd_values = [short_ema[i] - long_ema[i] for i in range(len(short_ema))]

#     signal_values = [calculate_ema(macd_values[:i], signal_period) for i in range(1, len(macd_values) + 1)]
    
#     return f'{macd_values[-1]:.8f}', f'{signal_values[-1]:.8f}'

for i in interval:
    # time_stamp = client._get_earliest_valid_timestamp('BTCUSDT', i)

    data = client.get_historical_klines('BTCUSDT', i, start_str = '3, Apr, 2024', end_str = '1, Apr, 2025', limit = 1000)

    close_price = []
    for j in data:
        del j[5:]
        j[0] = datetime.fromtimestamp(j[0] / 1000, tz = timezone.utc).strftime('%Y%m%d %H:%M:%S')

        # close_price.append(float(j[4]))

        # if len(close_price) >= 5:
        #     j.append(f'{sum(close_price[-5:]) / 5:.8f}')
        # else:
        #     j.append(None)

        # if len(close_price) >= 10:
        #     j.append(f'{sum(close_price[-10:]) / 10:.8f}')
        # else:
        #     j.append(None)

        # if len(close_price) >= 20:
        #     j.append(f'{sum(close_price[-20:]) / 20:.8f}')
        # else:
        #     j.append(None)

        # if len(close_price) >= 14:
        #     j.append(calculate_rsi(close_price))
        # else:
        #     j.append(None)

        # if len(close_price) >= 26:
        #     macd, signal = calculate_macd(close_price)
        #     j.append(macd)
        #     j.append(signal)
        # else:
        #     j.append(None)
        #     j.append(None)
            
    if i == '1M':
        with open(f'BTCUSDT/BTC_USDT_month.csv', 'a+', encoding = 'utf-8', newline = '') as file:
            writer = csv.writer(file)
            # writer.writerow(['Date', 'Open', 'High', 'Low', 'Close', '5SMA', '10SMA', '20SMA', 'RSI', 'MACD', 'Signal'])

            for j in data:
                writer.writerow(j)
    else:
        with open(f'BTCUSDT/BTC_USDT_{i}.csv', 'a+', encoding = 'utf-8', newline = '') as file:
            writer = csv.writer(file)
            # writer.writerow(['Date', 'Open', 'High', 'Low', 'Close', '5SMA', '10SMA', '20SMA', 'RSI', 'MACD', 'Signal'])

        for j in data:
            writer.writerow(j)
