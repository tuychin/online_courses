from django.conf import settings

import telebot

bot = telebot.TeleBot(settings.TELEGRAM_TOKEN)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Привет':
        bot.send_message(message.from_user.id, 'Привет, чем я могу тебе помочь?')
    elif message.text == '/start':
        bot.send_message(message.from_user.id, 'Напиши Привет')
    else:
        bot.send_message(message.from_user.id, 'Я тебя не понимаю. Напиши /start.')


bot.polling(none_stop=True, interval=0)
