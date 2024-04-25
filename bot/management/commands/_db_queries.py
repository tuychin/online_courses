from django.db.models import Q
from asgiref.sync import sync_to_async
from bot.models import Category, Course


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
