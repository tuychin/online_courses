from django.db.models import Q
from asgiref.sync import sync_to_async
from bot.models import Category, Course, Purchase


@sync_to_async
def get_all_categories():
    return list(Category.objects.all())


@sync_to_async
def get_courses_by_category_id(category_id: str):
    return list(Course.objects.filter(category_id=category_id))


@sync_to_async
def search_courses(text: str):
    return list(Course.objects.filter(
        Q(name__icontains=text)
        | Q(description__icontains=text)
        | Q(tags__icontains=text)
    ))


@sync_to_async
def get_course_by_id(course_id: str):
    return Course.objects.get(pk=course_id)


@sync_to_async
def add_purchase(
    user_login: str,
    product_id: int,
    product_name: str,
    product_url: str,
    product_paid: int,
    currency: str
):
    new_purchase = Purchase.objects.create(
        user_login=user_login,
        product_id=product_id,
        product_name=product_name,
        product_url=product_url,
        product_paid=product_paid,
        currency=currency
    )
    new_purchase.save()


@sync_to_async
def get_user_purchases(user_login: str):
    return list(Purchase.objects.filter(user_login=user_login))
