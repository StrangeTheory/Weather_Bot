import requests
import datetime
from config import tg_token, OW_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=tg_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.message):
    await message.reply("Привет! Напиши мне название города и я подскажу тебе прогноз!")


if __name__ == '__main__':
    executor.start_polling(dp)

