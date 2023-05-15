import logging
import os

import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

logging.basicConfig(level=logging.INFO)

API_TOKEN = os.getenv("TOKEN")
bot = Bot(API_TOKEN)
storage = MemoryStorage()

dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
# async def suz(msg: types.Message):
#     await msg.answer("")



@dp.message_handler()
async def lubboy(msg: types.Message):
    unli = 'aouie'
    count = 0
    s = msg.text
    for i in s:
        if i in unli:
            count += 1
    if count >= 5:
        await bot.delete_message(msg.chat.id, msg.message_id)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)