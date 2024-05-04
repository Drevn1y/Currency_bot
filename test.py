import requests
import datetime


currency = 'USD'
date = datetime.date.today()


api_key = f'https://cbu.uz/ru/arkhiv-kursov-valyut/json/{currency}/{date}/'


result = requests.get(api_key)


if result.status_code == 200:
    data = result.json()
    rate = data[0]['Rate']
    print(f"Курс {currency} на сегодня: {rate}")
else:
    print("Ошибка при получении данных с сервера.")
