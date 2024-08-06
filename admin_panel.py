import telebot
from telebot import types
from main_SQL import *

bot = telebot.TeleBot("6701177381:AAHOyJu-MZ2j8djqTT5rZlqiGIlJMOt0mA0")


@bot.message_handler(commands=["start"])
def start(message):
    if user_db("user", message.chat.id) == True:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        user = (select_data("user", message.chat.id)[0][3])
        if user == "user":
            btn1 = types.KeyboardButton("профиль")
            btn2 = types.KeyboardButton("магазин")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id,
                         text="Привет, {0.first_name}!".format(
                             message.from_user), reply_markup=markup)
        elif user == 'admin':
            btn1 = types.KeyboardButton("профиль")
            btn2 = types.KeyboardButton("магазин")
            btn3 = types.KeyboardButton("панель администратора")
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id,
                         text="Привет, {0.first_name}!".format(
                             message.from_user), reply_markup=markup)
    else:
        bot.send_message(message.chat.id,
                         text="Привет, {0.first_name}!".format(
                             message.from_user))
        bot.send_message(message.chat.id, "Впишите ваш номер ПФДО")
        bot.register_next_step_handler(message, pfdo)
def pfdo(message):
    num = message.text
    if num.isdigit():
        pfdo0 = int(num)
        user_database(message.chat.id, message.from_user.first_name, pfdo0)
        start(message)
    else:
        bot.send_message(message.chat.id, "Неправильный ввод. Впишите ваш номер ПФДО")
        bot.register_next_step_handler(message, pfdo)

@bot.message_handler(content_types=['text'])
def message_handler(message):
    print(message.text)
    if message.text.lower() == "профиль":
        text = f"""пользователь по счёту - {select_data("user", message.chat.id)[0][0]}
имя - {select_data("user", message.chat.id)[0][4]} 
счёт - {select_data("user", message.chat.id)[0][2]} Квантокоинов"""
        bot.send_message(message.chat.id, text)
    elif message.text.lower() == "панель администратора":
        print(True)
        if select_data("user", message.chat.id)[0][3] == "admin":
            print(True)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("изменение магазина")
            btn2 = types.KeyboardButton("список пользователей")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, "панель администратора", reply_markup=markup)
        else:
            bot.send_message(message.chat.id, "У вас нет право доступа к панели")
    else:
        bot.send_message(message.chat.id, "нет такой команды")
bot.infinity_polling()