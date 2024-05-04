import telebot
import requests
import datetime
import buttons as bt

TOKEN = '7093570623:AAEKcR6Qhh3m5gYGaqelXkg4T7QIRJxr2q4'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    user_id = message.from_user.id
    bot.send_message(user_id, f'Привет {message.from_user.first_name}', reply_markup=bt.main())


# ======================================================================================================================
@bot.message_handler(func=lambda message: message.text == '💰Курс валют')
def currency_message(message):
    user_id = message.from_user.id
    bot.send_message(user_id, 'Выберите курс валюты!', reply_markup=bt.currency())


@bot.callback_query_handler(func=lambda query: query.data == 'USD')
def USD_message(query):
    user_id = query.from_user.id
    currency = 'USD'
    date = datetime.date.today()

    api_key = f'https://cbu.uz/ru/arkhiv-kursov-valyut/json/{currency}/{date}/'

    result = requests.get(api_key)

    if result.status_code == 200:
        data = result.json()
        rate = data[0]['Rate']
        bot.send_message(user_id, f"Курс {currency} на сегодня: {rate} сум.", reply_markup=bt.back())
    else:
        print("Ошибка при получении данных с сервера.")


@bot.callback_query_handler(func=lambda query: query.data == 'RUB')
def RUB_message(query):
    user_id = query.from_user.id
    currency = 'RUB'
    date = datetime.date.today()

    api_key = f'https://cbu.uz/ru/arkhiv-kursov-valyut/json/{currency}/{date}/'

    result = requests.get(api_key)

    if result.status_code == 200:
        data = result.json()
        rate = data[0]['Rate']
        bot.send_message(user_id, f"Курс {currency} на сегодня: {rate} сум.", reply_markup=bt.back())
    else:
        print("Ошибка при получении данных с сервера.")


@bot.callback_query_handler(func=lambda query: query.data == 'EUR')
def USD_message(query):
    user_id = query.from_user.id
    currency = 'EUR'
    date = datetime.date.today()

    api_key = f'https://cbu.uz/ru/arkhiv-kursov-valyut/json/{currency}/{date}/'

    result = requests.get(api_key)

    if result.status_code == 200:
        data = result.json()
        rate = data[0]['Rate']
        bot.send_message(user_id, f"Курс {currency} на сегодня: {rate} сум.", reply_markup=bt.back())
    else:
        print("Ошибка при получении данных с сервера.")


# ======================================================================================================================
@bot.message_handler(func=lambda message: message.text == "🔙Назад")
def back_message(message):
    user_id = message.from_user.id
    bot.send_message(user_id, 'Возврат назад', reply_markup=bt.main())


# ======================================================================================================================
@bot.message_handler(func=lambda message: message.text == '🎁Поддержать проект')
def donate_message(message):
    user_id = message.from_user.id
    bot.send_message(user_id, 'В разработке в меню /start', reply_markup=bt.donate())


@bot.message_handler(func=lambda message: message.text == 'Click')
def click_message(message):
    user_id = message.from_user.id
    bot.send_message(user_id, 'Выберите сумму', reply_markup=bt.donate_inline())


@bot.callback_query_handler(lambda message: message.text == '5 000 som')
def click_5_message(message):
    user_id = message.from_user.id
    bot.send_message(user_id, 'Спасибо за вашу поддержку!', reply_markup=bt.back())


@bot.message_handler(func=lambda message: message.text == 'Payme')
def payme_message(message):
    user_id = message.from_user.id
    bot.send_message(user_id, 'В разработке в меню /start', reply_markup=telebot.types.ReplyKeyboardRemove())


# ======================================================================================================================
@bot.message_handler(func=lambda message: message.text == '📞Тех поддержка')
def support_message(message):
    user_id = message.from_user.id
    bot.send_message(user_id, '+998901234567', reply_markup=bt.back())


# ======================================================================================================================
@bot.message_handler(func=lambda message: message.text == '🔄Сменить язык')
def language_message(message):
    user_id = message.from_user.id
    bot.send_message(user_id, 'В разработке в меню /start', reply_markup=bt.language())


bot.polling(non_stop=True)
