from django.contrib import admin

from .models import CourseCategories, Courses

admin.site.site_header = 'Онлайн курсы'
admin.site.site_title = 'Онлайн курсы'
admin.site.index_title = 'Панель администратора'

admin.site.register(CourseCategories)
admin.site.register(Courses)
