from telegram import Bot
import asyncio

# token, chat_id 暫時移除
async def test():
    bot = Bot(token = '')
    chat_id = ''
    await bot.send_message(chat_id = chat_id, text = 'test')

asyncio.run(test())
