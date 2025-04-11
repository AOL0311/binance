from datetime import datetime
import csv

File = 'BTC_USDT/BTCUSDT_1Week.csv'

def get_interval(time):
    return datetime.strptime(time[0], '%Y%m%d %H%M%S')

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