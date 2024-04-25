import asyncio
import logging

from django.conf import settings
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandObject
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.enums import ParseMode
from aiogram.types import Message, InlineKeyboardButton, FSInputFile, CallbackQuery, LabeledPrice, PreCheckoutQuery

from bot.models import Course
from ._texts import START_TEXT, COURSE_TEXT, CATEGORIES_TEXT, COURSES_EMPTY_TEXT, SEARCH_NOT_FIND_TEXT,\
    SEARCH_WITHOUT_ARGS_TEXT, UNKNOWN_COMMAND_TEXT, PAYMENT_BUTTON_TEXT, INVOICE_DESCRIPTION_TEXT,\
    SUCCESSFUL_PAYMENT_TEXT
from ._db_queries import get_all_categories, get_courses_by_category_id, search_courses, get_course_by_id

logging.basicConfig(level=logging.INFO)

bot = Bot(token=settings.TELEGRAM_TOKEN, parse_mode=ParseMode.MARKDOWN)
dp = Dispatcher()


def get_price(price: int, product_name: str):
    """Возвращает объект цены для оплаты.

    Аргументы:
    price -- цена в рублях (не менее 80 рублей)
    product_name -- название продукта
    """
    return LabeledPrice(label=f"Купить: {product_name}", amount=price*100)


async def send_course(course: Course, message: Message):
    description = f"\n{course.description}\n" if course.description else ""
    text = COURSE_TEXT.format(name=course.name, description=description, url=course.course_url)

    builder = InlineKeyboardBuilder()
    course_button = InlineKeyboardButton(
        text=PAYMENT_BUTTON_TEXT.format(price=course.price),
        callback_data=f"course_{course.id}"
    )
    builder.row(course_button)

    if course.image:
        await message.answer_photo(FSInputFile(course.image.name), caption=text, reply_markup=builder.as_markup())
    else:
        await message.answer(text, reply_markup=builder.as_markup(), disable_web_page_preview=True)


async def category_button_handler(callback: CallbackQuery):
    category_id = callback.data.split("_")[1]
    courses = await get_courses_by_category_id(category_id)

    if not courses:
        await callback.message.answer(COURSES_EMPTY_TEXT)
        return

    for course in courses:
        await send_course(course, callback.message)


async def course_button_handler(callback: CallbackQuery):
    course_id = callback.data.split("_")[1]
    course: Course = await get_course_by_id(course_id)

    await callback.message.reply_invoice(
        title=course.name,
        description=INVOICE_DESCRIPTION_TEXT.format(name=course.name, price=course.price),
        provider_token=settings.PAYMENTS_TOKEN,
        currency="rub",
        is_flexible=False,
        prices=[get_price(price=course.price, product_name=course.name)],
        payload=callback.data
    )


@dp.message(Command("start"))
async def command_start_handler(message: Message):
    await message.answer(START_TEXT)


@dp.message(Command("categories"))
async def command_category_handler(message: Message):
    categories = await get_all_categories()
    builder = InlineKeyboardBuilder()

    for category in categories:
        category_button = InlineKeyboardButton(text=category.name, callback_data=f"category_{category.id}")
        builder.row(category_button)

    await message.answer(
        CATEGORIES_TEXT,
        reply_markup=builder.as_markup()
    )


@dp.message(Command("search"))
async def command_search_handler(message: Message, command: CommandObject):
    if command.args is None:
        await message.reply(SEARCH_WITHOUT_ARGS_TEXT)
        return

    courses = await search_courses(command.args)

    if not courses:
        await message.reply(SEARCH_NOT_FIND_TEXT)
        return

    for course in courses:
        await send_course(course, message)


@dp.callback_query()
async def buttons_click_handler(callback: CallbackQuery):
    handler_type = callback.data.split("_")[0]

    match handler_type:
        case "category":
            await category_button_handler(callback)
        case "course":
            await course_button_handler(callback)


@dp.pre_checkout_query(lambda query: True)
async def pre_checkout_query_handler(pre_checkout_q: PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)


@dp.message(F.successful_payment)
async def successful_payment_handler(message: Message):
    payment_info = message.successful_payment
    total_amount = payment_info.total_amount // 100
    currency = payment_info.currency
    course_id = payment_info.invoice_payload.split("_")[1]
    course: Course = await get_course_by_id(course_id)

    await message.answer(SUCCESSFUL_PAYMENT_TEXT.format(
        total_amount=total_amount,
        currency=currency,
        product_url=course.product_url
    ))


@dp.message()
async def command_unknown_handler(message: Message):
    await message.reply(UNKNOWN_COMMAND_TEXT)


async def start_bot():
    await dp.start_polling(bot)

asyncio.run(start_bot())
