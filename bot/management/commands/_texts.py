START_TEXT = '''Я помогу выбрать онлайн-курс. Выберите команду:
/categories - меню категорий
/search - поиск (пример: /search программирование)
/purchases - мои покупки'''

COURSE_TEXT = '''*{name}*
{description}
*Подробнее:* {url}'''

CATEGORIES_TEXT = "Выберите категорию:"

COURSES_EMPTY_TEXT = "В этой категориии пока нет курсов\n(￢_￢)"

SEARCH_WITHOUT_ARGS_TEXT = '''Пожалуйста, укажите ключевые слова для поиска.
Например: /search программирование'''

SEARCH_NOT_FIND_TEXT = "Ничего не найдено\n(￢_￢)"

UNKNOWN_COMMAND_TEXT = "Неизвестная команда. Напишите /start"

PAYMENT_BUTTON_TEXT = "Купить за: {price} ₽"

INVOICE_DESCRIPTION_TEXT = '''Стоимость: {price} 🇷🇺RUB
Обработка платежа может занять до 3 минут, ожидайте\n( o˘◡˘o)
⚠️Если платеж не проходит, убедитесь, что ваша карта не просрочена⚠️

Помощь: @tuychin_r'''

SUCCESSFUL_PAYMENT_TEXT = '''Платеж на сумму {total_amount} {currency} прошел успешно!
*Ссылка на курс:* {product_url}'''

MY_PURCHASES_TEXT = '''*Мои покупки:*

{purchases}'''

MY_PURCHASES_EMPTY_TEXT = "У вас ещё нет ни одной покупки\n╮( ˘ ､ ˘ )╭"

PURCHASE_ITEM_TEXT = '''*{name}*
*Ссылка на курс:* {product_url}
*Оплачено:* {paid} {currency}'''
