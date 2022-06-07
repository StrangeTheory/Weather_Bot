import requests
import datetime
from config import tg_token, OW_token
from aiogram import bot, types
from aiogram.dispatcher import dispatcher
from aiogram.utils import executor

bot = Bot(token=tg_token)
dp = dispatcher(bot)

@dp.message_handler(commands=["start"])
async_def start_command(message: types.message):
    await message.reply("Привет! Напиши мне название города и я подскажу тебе прогноз!")


if __name__ == '__main__':
    executor.start_polling(dp)

