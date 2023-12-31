# Generated by Django 5.0 on 2023-12-22 09:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0006_course_description_alter_course_course_url_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CourseCategory',
            new_name='CourseCategories',
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=60, verbose_name='Название')),
                ('description', models.TextField(default='', max_length=180, verbose_name='Описание')),
                ('course_url', models.URLField(default='', max_length=120, verbose_name='Ссылка')),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
                ('tags', models.CharField(default='', max_length=120, verbose_name='Теги')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.coursecategories', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'курс',
                'verbose_name_plural': 'курсы',
            },
        ),
        migrations.DeleteModel(
            name='Course',
        ),
    ]
