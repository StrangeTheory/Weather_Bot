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

@dp.message_handler()
async def get_weather(message: types.message):
    code_to_smile = {
        "Clear": "Ясно \U00002688",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туманище \U0001F328"
    }

    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={OW_token}&units=metric"
        )
        data = r.json()

        city = data["name"]
        cur_temp = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Посмотри в окно"

        humid = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        sunrise_time = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_time = datetime.datetime.fromtimestamp(data["sys"]["sunset"])

        await message.reply(f"Погода в городе: {city}\nТемпература: {cur_temp}C {wd}\n"
              f"Влажность: {humid}%\nВетер: {wind}м.c\n"
              f"Время восхода: {sunrise_time}\n"
              f"Время заката: {sunset_time}")


    except:
        await message.reply("\U00002620 Проверьте название города \U00002620")


if __name__ == '__main__':
    executor.start_polling(dp)

