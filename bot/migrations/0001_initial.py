# Generated by Django 5.0 on 2023-12-27 16:00

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'категории',
                'verbose_name_plural': 'категории',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=120, verbose_name='Название')),
                ('description', models.TextField(blank=True, default='', null=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображение')),
                ('course_url', models.URLField(default='', max_length=120, verbose_name='Ссылка')),
                ('price', models.IntegerField(default=0, verbose_name='Цена в ₽')),
                ('tags', models.CharField(blank=True, default='', max_length=120, null=True, verbose_name='Теги')),
                ('datetime', models.DateTimeField(default=datetime.datetime(2023, 12, 27, 19, 0, 35, 389520), verbose_name='Дата публикации (по МСК)')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bot.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'курс',
                'verbose_name_plural': 'курсы',
            },
        ),
    ]
