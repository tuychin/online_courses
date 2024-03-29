# Generated by Django 5.0 on 2023-12-27 17:06

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0003_alter_course_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='course',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 27, 20, 6, 33, 650904), verbose_name='Дата публикации (по МСК)'),
        ),
    ]
