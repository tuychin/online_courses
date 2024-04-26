from django.contrib import admin

from .models import Category, Course

admin.site.site_header = "t.me/my_online_courses_bot"
admin.site.site_title = "Онлайн курсы"
admin.site.index_title = "Панель администратора"

admin.site.register(Category)
admin.site.register(Course)
