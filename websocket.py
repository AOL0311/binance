import asyncio
import websockets
import json
import numpy as np
from env import CryptoTradingEnv
from stable_baselines3 import DQN
from telegram import Bot

model = DQN('MlpPolicy', CryptoTradingEnv(), verbose = 0)
model.learn(total_timesteps = 5000)

# token, chat_id 已暫時清除
bot = Bot(token = '')
chat_id = ''

def send_telegram(message):
    bot.send_message(chat_id, text = message)

def place_order(action):
    if action == 0:
        send_telegram('[RL] Buy signal triggered.')
    elif action == 1:
        send_telegram('[RL] Sell signal triggered.')
    else:
        send_telegram('[RL] Hold - No trade triggered.')

price_buffer = []
async def websocket_binance(symbol = 'btcusdt'):
    uri = f'wss://stream.binance.com:9443/ws/{symbol}@kline_1m'

    async with websockets.connect(uri) as ws:
        print('Websocket connected.')
        while True:
            data = await ws.recv()
            parsed = json.loads(data)
            candle = parsed['k']
            if candle['x']:
                close_price = float(candle['c'])
                price_buffer.append(close_price)

                if len(price_buffer) > 10:
                    price_buffer.pop(0)

                    sma = np.mean(price_buffer)
                    state = CryptoTradingEnv.get_state(close_price, sma)
                    action, _ = model.predict(state)
                    place_order(action)

if __name__ == '__main__':
    try:
        asyncio.run(websocket_binance())
    except KeyboardInterrupt:
        print('Stop websocket.')
