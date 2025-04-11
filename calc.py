import numpy as np
import csv

File = 'BTC_USDT/BTCUSDT_1Week.csv'

def calculate_rsi(prices, period = 14):
    gains = []
    losses = []

    for i in range(1, len(prices)):
        if prices[i] - prices[i - 1] > 0:
            gains.append(prices[i] - prices[i - 1])
            losses.append(0)
        else:
            losses.append(abs(prices[i] - prices[i - 1]))
            gains.append(0)

    avg_gain = np.mean(gains[-period:])
    avg_loss = np.mean(losses[-period:])

    return f'{100 - (100 / (1 + avg_gain / avg_loss if avg_loss != 0 else 0)):.8f}'

def calculate_ema(prices, period, previous_ema = None):
    alpha = 2 / (period + 1)

    if previous_ema is None:
        previous_ema = prices[0]

    ema_values = [previous_ema]
    for i in prices[1:]:
        current_ema = (i - ema_values[-1]) * alpha + ema_values[-1]
        ema_values.append(current_ema)

    return ema_values[-1]


def calculate_macd(prices, short_period = 12, long_period = 26, signal_period = 9):
    short_ema = [calculate_ema(prices[:i], short_period) for i in range(1, len(prices) + 1)]
    long_ema = [calculate_ema(prices[:i], long_period) for i in range(1, len(prices) + 1)]

    macd_values = [short_ema[i] - long_ema[i] for i in range(len(short_ema))]

    signal_values = [calculate_ema(macd_values[:i], signal_period) for i in range(1, len(macd_values) + 1)]
    
    return f'{macd_values[-1]:.8f}', f'{signal_values[-1]:.8f}'

datas = []
close_price = []
with open(File, 'r', encoding = 'utf-8') as file:
    data = file.readlines()
    
    for line in data:
        line = line.replace('\n', '')
        line = line.split(',')
    
        datas.append(line)
        close_price.append(float(line[4]))
        
        if len(close_price) >= 5:
            line.append(f'{sum(close_price[-5:]) / 5:.8f}')
        else:
            line.append(None)
            
        if len(close_price) >= 10:
            line.append(f'{sum(close_price[-10:]) / 10:.8f}')
        else:
            line.append(None)
            
        if len(close_price) >= 20:
            line.append(f'{sum(close_price[-20:]) / 20:.8f}')
        else:
            line.append(None)
            
        if len(close_price) >= 14:
            line.append(calculate_rsi(close_price))
        else:
            line.append(None)
            
        if len(close_price) >= 26:
            macd, signal = calculate_macd(close_price)
            line.append(macd)
            line.append(signal)
        else:
            line.append(None)
            line.append(None)

with open(File, 'w', encoding = 'utf-8', newline = '') as file:
    writer = csv.writer(file)
    writer.writerows(datas)