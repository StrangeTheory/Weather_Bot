from config import OW_token
from pprint import pprint
import requests
import datetime

def get_weather(city,OW_token):

    code_to_smile = {
        "Clear": "Ясно \U00002688",
        "Clouds": "Облачно \U00002681",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туманище \U0001F328"
    }


    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OW_token}&units=metric"
        )
        data = r.json()
        #pprint(data)

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

        print(f"Погода в городе: {city}\nТемпература: {cur_temp}C {wd}\n"
        f"Влажность: {humid}%\nВетер: {wind}м.c\n"
        f"Время восхода: {sunrise_time}\n"
        f"Время заката: {sunset_time}" )


    except Exception as ex:
        print(ex)
        print("Проверьте название города")



def main():
    city = input("Введите город: ")
    get_weather(city, OW_token)



if __name__ == '__main__':
    main()
