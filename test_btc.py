import asyncio
from time import sleep
from binance import AsyncClient, BinanceSocketManager

async def main():
    client = await AsyncClient.create()
    manager = BinanceSocketManager(client, user_timeout = 30)
    socket = manager.trade_socket('BTCUSDT')
    
    async with socket as trade_socket:
        while True:
            sleep(5)
            res = await trade_socket.recv()
            print(f'BTC/USDT 當前價格:{res['p']}')
            
if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())