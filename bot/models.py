from django.db import models
import datetime


class Category(models.Model):
    class Meta:
        verbose_name = "категории"
        verbose_name_plural = "категории"

    name = models.CharField(max_length=60, verbose_name='Название')

    def __str__(self):
        return self.name


class Course(models.Model):
    class Meta:
        verbose_name = "курс"
        verbose_name_plural = "курсы"

    name = models.CharField(max_length=120, verbose_name='Название', default='')
    description = models.TextField(verbose_name='Описание', default='', null=True, blank=True)
    image = models.ImageField(verbose_name='Изображение', upload_to='images/', null=True, blank=True)
    course_url = models.URLField(max_length=120, verbose_name='Ссылка', default='')
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        on_delete=models.CASCADE,
    )
    price = models.IntegerField(verbose_name='Цена в ₽', default=0)
    tags = models.CharField(max_length=120, verbose_name='Теги', default='', null=True, blank=True)
    datetime = models.DateTimeField(verbose_name='Дата публикации (по МСК)', default=datetime.datetime.now())

    def __str__(self):
        return self.name
