from django.conf import settings
from django.db.models import Q

import telebot

from bot.models import Category, Course
from .consts import START_TEXT

bot = telebot.TeleBot(settings.TELEGRAM_TOKEN, parse_mode='markdown')

def send_course(course, chat_id):
    newline = '\n\n'
    text = f'*{course.name}*{newline}' \
           f'{course.description + newline if course.description else ""}' \
           f'Цена: {course.price} ₽{newline}' \
           f'Подробнее: {course.course_url}'

    if course.image:
        bot.send_photo(chat_id, course.image, caption=text)
    else:
        bot.send_message(chat_id, text, disable_web_page_preview=True)


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.from_user.id, START_TEXT)


@bot.message_handler(commands=['categories'])
def handle_category(message):
    categories = Category.objects.all()
    keyboard = telebot.types.InlineKeyboardMarkup()

    for category in categories:
        category_button = telebot.types.InlineKeyboardButton(text=category.name, callback_data=category.id)
        keyboard.add(category_button)

    bot.send_message(message.chat.id, 'Выберите категорию:', reply_markup=keyboard)


@bot.message_handler(commands=['search'])
def handle_search(message):
    keywords = ' '.join(message.text.split()[1:])

    if not keywords:
        bot.reply_to(message, 'Пожалуйста, укажите ключевые слова для поиска. '
                              'Например: /search программирование')
        return

    courses = Course.objects.filter(
        Q(name__icontains=keywords)
        | Q(description__icontains=keywords)
        | Q(tags__icontains=keywords)
    )

    if not courses:
        bot.reply_to(message, 'Ничего не найдено :(')
        return

    for course in courses:
        send_course(course, message.chat.id)


@bot.message_handler()
def handle_unknown(message):
    bot.reply_to(message, 'Я не знаю такую команду. Напишите /start.')


@bot.callback_query_handler(func=lambda call: True)
def handle_buttons_click(call):
    courses = Course.objects.filter(category_id=call.data)

    if not courses:
        bot.send_message(call.message.chat.id, 'В этой категориии пока нет курсов :(')
        return

    for course in courses:
        send_course(course, call.message.chat.id)


bot.polling(none_stop=True, interval=0)
