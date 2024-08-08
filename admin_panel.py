import telebot
from telebot import types
from main_SQL import *
from func_for_project import *
bot = telebot.TeleBot("6701177381:AAHOyJu-MZ2j8djqTT5rZlqiGIlJMOt0mA0")
Numprod = 0
def buttons(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    user = (select_data( message.chat.id)[0][3])
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
@bot.message_handler(commands=["start"])
def start(message):
    if user_db("user", message.chat.id) == True:
        buttons(message)
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
    if message.text.lower() == "профиль":
        text = f"""пользователь по счёту - {select_data( message.chat.id)[0][0]}
имя - {select_data( message.chat.id)[0][4]} 
счёт - {select_data(message.chat.id)[0][2]} Квантокоинов"""
        bot.send_message(message.chat.id, text)
    elif message.text.lower() == "панель администратора":
        if select_data("user", message.chat.id)[0][3] == "admin":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("изменение магазина")
            btn2 = types.KeyboardButton("список пользователей")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, "панель администратора", reply_markup=markup)
        else:
            bot.send_message(message.chat.id, "У вас нет право доступа к панели")
    elif message.text.lower() == "магазин":
        text = subnet()
        text = text + "\n" + "Введите номер товара/услуги для получения описания\nдля покупки - /buy \n для выхода введите - /exit "
        bot.send_message(message.chat.id, text)
        bot.register_next_step_handler(message, Store)
    else:
        bot.send_message(message.chat.id, "нет такой команды")
def Store(message):
    if message.text == "/exit":
        bot.register_next_step_handler(message, message_handler)
    elif message.text == "/buy":
        bot.send_message(message.chat.id, "напишите номер товара/услуги который хотите приобрести")
        bot.register_next_step_handler(message, buy)
    elif message.text.isdigit():
        if int(message.text) <= len(datafr("store", "products")) and int(message.text) > 0:
            data = product_def(message.text)
            bot.send_message(message.chat.id, data)
            bot.register_next_step_handler(message, Store)
        else:
            bot.send_message(message.chat.id, "неправильный ввод")
            bot.register_next_step_handler(message, Store)
    else:
        bot.send_message(message.chat.id, "неправильный ввод")
        bot.register_next_step_handler(message, Store)
def buy(message):
    if message.text != "/exit":
        data = product_def(message.text)
        if data != "нет такого товара" and data != "не правильный ввод":
            global Numprod
            Numprod = message.text
            bot.send_message(message.chat.id, data)
            bot.send_message(message.chat.id, "этот товар/услугу хотите приобрести?\n\nда/нет")

            bot.register_next_step_handler(message, buy1)
        else:
            bot.send_message(message.chat.id, data + "\n\nпопробуйте ещё раз")
            bot.register_next_step_handler(message, buy)
    else:
        bot.register_next_step_handler(message, message_handler)
def buy1(message):
    if message.text.lower() == 'да':
        data = datafr("store", "products")
        global Numprod
        cell = data[int(Numprod)-1][4]
        data0 = select_data(message.chat.id)
        if data0[0][2] >= cell:
            update_data("user", "users", message.chat.id, "score", select_data(message.chat.id)[2] - cell, "user_id")
        else:
            bot.send_message(message.chat.id, "не хватает квантокоинов")
    elif message.text.lower() == 'нет':
        bot.register_next_step_handler(message, message_handler)
    else:
        bot.send_message(message.chat.id, "неправильный ввод")
        bot.register_next_step_handler(message, buy1)
bot.infinity_polling()