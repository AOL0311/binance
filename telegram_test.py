from telegram import Bot
import asyncio

async def test():
    bot = Bot(token = '7683441276:AAFJsaLJpNzDf23Nh4pBnjrPIAvKI0-gu5w')
    chat_id = '6515758042'
    await bot.send_message(chat_id = chat_id, text = 'test')

asyncio.run(test())