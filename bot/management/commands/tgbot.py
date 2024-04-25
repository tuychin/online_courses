from django.conf import settings
from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandObject
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.enums import ParseMode
from aiogram.types import Message, InlineKeyboardButton, FSInputFile, CallbackQuery
import asyncio
import logging

from bot.models import Course
from ._texts import START_TEXT
from ._db_queries import get_all_categories, get_courses_by_category_id, search_courses

logging.basicConfig(level=logging.INFO)

bot = Bot(token=settings.TELEGRAM_TOKEN, parse_mode=ParseMode.MARKDOWN)
dp = Dispatcher()


async def send_course(course: Course, message: Message):
    newline = '\n\n'
    text = f'*{course.name}*{newline}' \
           f'{course.description + newline if course.description else ""}' \
           f'Цена: {course.price} ₽{newline}' \
           f'Подробнее: {course.course_url}'

    if course.image:
        print(f'TEST: {course.image.name}')
        await message.answer_photo(FSInputFile(course.image.name), caption=text)
    else:
        await message.answer(text, disable_web_page_preview=True)


@dp.message(Command('start'))
async def handle_start(message: Message):
    await message.answer(START_TEXT)


@dp.message(Command('categories'))
async def handle_category(message: Message):
    categories = await get_all_categories()
    builder = InlineKeyboardBuilder()

    for category in categories:
        category_button = InlineKeyboardButton(text=category.name, callback_data=str(category.id))
        builder.row(category_button)

    await message.answer(
        'Выберите категорию:',
        reply_markup=builder.as_markup()
    )


@dp.message(Command('search'))
async def handle_search(message: Message, command: CommandObject):
    if command.args is None:
        await message.reply('Пожалуйста, укажите ключевые слова для поиска. Например: /search программирование')
        return

    courses = await search_courses(command.args)

    if not courses:
        await message.reply('Ничего не найдено :(')
        return

    for course in courses:
        await send_course(course, message)


@dp.message()
async def handle_unknown(message: Message):
    await message.reply('Я не знаю такую команду. Напишите /start')


@dp.callback_query()
async def handle_buttons_click(callback: CallbackQuery):
    courses = await get_courses_by_category_id(callback.data)

    if not courses:
        await callback.message.answer('В этой категориии пока нет курсов :(')
        return

    for course in courses:
        await send_course(course, callback.message)


async def main():
    await dp.start_polling(bot)

asyncio.run(main())
