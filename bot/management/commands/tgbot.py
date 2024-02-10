from django.conf import settings
import telebot

from bot.models import Category, Course
from ._text import START_TEXT

bot = telebot.TeleBot(settings.TELEGRAM_TOKEN, parse_mode='markdown')

categories = Category.objects.all()

print(categories)


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.from_user.id, START_TEXT)


@bot.message_handler(commands=['categories'])
def handle_category(message):
    keyboard = telebot.types.InlineKeyboardMarkup()

    for category in categories:
        category_button = telebot.types.InlineKeyboardButton(text=category.name, callback_data=category.id)
        keyboard.add(category_button)

    bot.send_message(message.chat.id, 'Выберите категорию:', reply_markup=keyboard)


@bot.message_handler(commands=['search'])
def handle_search(message):
    bot.send_message(message.from_user.id, '')


@bot.message_handler()
def handle_unknown(message):
    bot.send_message(message.from_user.id, 'Я не знаю такую команду. Напишите /start.')


@bot.callback_query_handler(func=lambda call: True)
def handle_buttons_click(call):
    courses = Course.objects.filter(category_id=call.data)

    if courses:
        for course in courses:
            text = f'*{course.name}*\n\n{course.description if course.description else ""}' \
                   f'Цена: {course.price} ₽\n\nПодробнее: {course.course_url}'

            bot.send_message(call.message.chat.id, '\n\n------------------------------\n\n')

            if course.image:
                bot.send_photo(call.message.chat.id, course.image, caption=text)
            else:
                bot.send_message(call.message.chat.id, text, disable_web_page_preview=True)
    else:
        bot.send_message(call.message.chat.id, 'В этой категориии пока нет курсов :(')


bot.polling(none_stop=True, interval=0)
