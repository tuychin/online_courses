# Generated by Django 5.0 on 2023-12-22 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0009_alter_courses_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Цена в ₽'),
        ),
    ]
