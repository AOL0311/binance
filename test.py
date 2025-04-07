import os
from binance.client import Client

api_key = "eW6Nv6jqbYtrjpFCU8jaP3fzRsymBtLPi8dBuxPHayBBBZVebrtDCnj8Dhw4kmH5"
api_secert = "1sMqGafas3VCh7vUDk1B4IsKsMBBRMNLuxEYqg8yFWKxQHOzop0V2GXOFVmEu2RM"

client = Client(api_key, api_secert)
client.API_URL = 'https://api.binance.com/api'

# 查詢帳戶餘額
assets_list = ['USDT', 'ETH', 'BTC']
for i in assets_list:
    print(client.get_asset_balance(asset = i))
    
# 查詢最新價格
price_list = ['ETHUSDT', 'BTCUSDT', 'BNBUSDT']
for i in price_list:
    temp = client.get_symbol_ticker(symbol = i)
    print(f'{temp['symbol']}, price: {temp['price']:>15s}')