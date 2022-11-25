import telebot  # https://t.me/education_simple_calc_bot
from datetime import datetime as dt
from time import time

bot = telebot.TeleBot(
    "-------", parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Введите арифметическое выражение")


@bot.message_handler(func=lambda m: True)
def calc(message):

    digits = "1234567890()-+*/ "
    for i in message.text:
        if i not in digits:
            bot.reply_to(
                message, "В выражении присутствуют недопустимые символы, введите правильное арифметическое выражение")
            return
    bot.reply_to(message, f"{message.text} = {eval(message.text)}")
    data = f"{message.text} = {eval(message.text)}"
    time = dt.now().strftime('%H:%M')
    name = message.from_user.first_name
    with open('log.csv', 'a', encoding='utf-8') as file:
        file.write('{}; {} посчитал арифметическое выражение: {}\n'.format(
            time, name, data))
    file.close()


bot.infinity_polling()
