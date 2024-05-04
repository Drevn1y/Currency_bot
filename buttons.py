from telebot import types


# ======================================================================================================================
def language():
    lg = types.ReplyKeyboardMarkup(resize_keyboard=True)
    ru = types.KeyboardButton('🇷🇺Русский')
    eng = types.KeyboardButton('🇺🇿English')

    lg.add(ru, eng)
    return lg


# ======================================================================================================================
def main():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    value = types.KeyboardButton('💰Курс валют')
    admin = types.KeyboardButton('📞Тех поддержка')
    donate = types.KeyboardButton('🎁Поддержать проект')
    lgs = types.KeyboardButton('🔄Сменить язык')

    kb.add(value, donate, admin, lgs)
    return kb


def main_eng():
    kb_eng = types.ReplyKeyboardMarkup(resize_keyboard=True)
    value_eng = types.KeyboardButton('💰Currency Exchange Rate')
    admin_eng = types.KeyboardButton('📞Support')
    donate = types.KeyboardButton('🎁Support the project')
    lgs_eng = types.KeyboardButton('🔄Change Language')

    kb_eng.add(value_eng, donate,  admin_eng, lgs_eng)
    return kb_eng


# ======================================================================================================================
def currency():
    currency_markup = types.InlineKeyboardMarkup(row_width=2)
    usd = types.InlineKeyboardButton(text='USD', callback_data='USD')
    eur = types.InlineKeyboardButton(text='EUR', callback_data='EUR')
    rub = types.InlineKeyboardButton(text='RUB', callback_data='RUB')

    currency_markup.add(usd, eur, rub)
    return currency_markup


# ======================================================================================================================
def donate():
    donate_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    click = types.KeyboardButton('Click')
    payme = types.KeyboardButton('Payme')
    donate_markup.add(click, payme)
    return donate_markup


def donate_inline():
    donate_markup = types.InlineKeyboardMarkup(row_width=2)
    button1 = types.InlineKeyboardButton(text='5 000 som', callback_data='5 000 som')
    button2 = types.InlineKeyboardButton(text='10 000 som', callback_data='10 000 som')
    button3 = types.InlineKeyboardButton(text='20 000 som', callback_data='20 000 som')

    donate_markup.add(button1, button2, button3)
    return donate_markup


# ======================================================================================================================
def back():
    back_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = types.KeyboardButton('🔙Назад')
    back_markup.add(back)
    return back_markup


def back_eng():
    back_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = types.KeyboardButton('🔙Back')
    back_markup.add(back)
    return back_markup


# ======================================================================================================================
