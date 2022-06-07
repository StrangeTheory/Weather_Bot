from config import OW_token
import requests

def get_weather(city,OW_token):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OW_token}"
        )
        data = r.json()
        print(data)

    except Exception as ex:
        print(ex)
        print("Проверьте название города")



def main():
    city = input("Введите город: ")
    get_weather(city, OW_token)



if __name__ == '__main__':
    main()
