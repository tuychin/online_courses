# Generated by Django 5.0 on 2023-12-22 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0010_alter_courses_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='description',
            field=models.TextField(default='', null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='courses',
            name='tags',
            field=models.CharField(default='', max_length=120, null=True, verbose_name='Теги'),
        ),
    ]
