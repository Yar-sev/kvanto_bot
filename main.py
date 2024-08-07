import telebot
from telebot import types
import main_SQL
bot = telebot.TeleBot("6701177381:AAHOyJu-MZ2j8djqTT5rZlqiGIlJMOt0mA0")


namesur = None
pfdoo = None

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("Далее")
    markup.add(btn1)
    bot.send_message(message.chat.id, "Привет, ты попал на крупнейшую криптоплощадку Кванториума! Здесь ты можешь заработать Квантокоины, а после обменять их на ценные товары и/или услуги :>", reply_markup=markup)

@bot.message_handler()
def register(message):
    bot.send_message(message.chat.id, "Для того, чтобы начать, необходимо зарегистрироваться >>> Введи имя и фамилию:")
    bot.register_next_step_handler(message, age)

@bot.message_handler()
def age(message):
    global namesur
    namesur = message.text
    print(namesur)
    bot.send_message(message.chat.id, "Укажи свой номер сертификата ПФДО:")
    bot.register_next_step_handler(message, profile)

@bot.message_handler()
def profile(message):

    try:
        global pfdoo
        pfdoo = int(message.text)
        print(pfdoo)
        bot.send_message(message.chat.id, "Ты успешно зарегистрировался! Вот твой профиль:")
        main_SQL.user_database(id, namesur, pfdoo)
        bot.register_next_step_handler(message, anketa)

    except:
        bot.send_message(message.chat.id, "Введите корректный номер сертификата!")
        bot.register_next_step_handler(message, profile)

@bot.message_handler()
def anketa(message):
    bot.send_message(message.chat.id, "Тут должна быть ваша анкета")




bot.infinity_polling()