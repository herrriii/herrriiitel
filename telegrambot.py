import telebot
import random

# Token
bot = telebot.TeleBot("759825642:AAERC44zGNqB9n3czBgQOtXHpOjcA3xElGI")

a = ["Подтверждаю", "Да", "Угу", "Конечно", "Ага"]
b = ["Hmm", "Интересно", "Что?", "Что ещё раз?", "Ого", "Omg"]
с = ["Не", "Не подтверждаю", "Не-а", "Нууу... нет", "К сожалениею, нет"]

# Start, joke
@bot.message_handler(commands=['start', "анектод", "Анектод"])
def welcome(message):
    bot.send_message(message.chat.id, "Царь позвал к себе Иванушку-дурака и говорит:\n"
                                      '– Если завтра не принесешь двух говорящих птиц – голову срублю.\n'
                                      'Иван принес филина и воробья. Царь говорит:\n'
                                      '– Ну, пусть что-нибудь скажут.\n'
                                      'Иван спрашивает:\n'
                                      '– Воробей, почем раньше водка в магазине была?\n'
                                      'Воробей:\n'
                                      '– Чирик.\n'
                                      'Иван филину:\n'
                                      '– А ты, филин, подтверди.\n'
                                      'Филин:\n'
                                      '– Подтверждаю.')


# Agree
@bot.message_handler(regexp="подтверди")
def answer(message):
    bot.send_message(message.from_user.id, random.choice(a))


# Agree2
@bot.message_handler(regexp="Да")
def answer(message):
    bot.send_message(message.from_user.id, random.choice(a))


# Don't agree
@bot.message_handler(regexp="не")
def answer(message):
    bot.send_message(message.from_user.id, random.choice(с))


# Reply
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, random.choice(b))


bot.polling(none_stop=True, interval=0)
