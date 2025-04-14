from datetime import datetime
import csv

def get_interval(time):
    return datetime.strptime(time[0], '%Y%m%d %H%M%S')

interval = ['1m', '3m', '5m', '15m', '30m', '1h', '2h', '4h', '6h', '8h', '12h', '1d', '3d', '1w', '1M']
for i in interval:
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

    datas = []
    with open(File, 'r', encoding = 'utf-8') as file:
        data = file.readlines()
        
        for line in data:
            line = line.replace('\n', '')
            line = line.split(',')
            
            datas.append(line)
    
    
    datas = sorted(datas, key = get_interval)

    for i in range(len(datas) - 1, 0, -1):
        if datas[i][0] == datas[i - 1][0]:
            del datas[i]
            
    with open(File, 'w', encoding = 'utf-8', newline = '') as file:
        writer = csv.writer(file)
        writer.writerows(datas)