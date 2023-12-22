# Generated by Django 5.0 on 2023-12-21 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0005_alter_course_options_alter_coursecategory_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.CharField(default='', max_length=180, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_url',
            field=models.URLField(default='', max_length=120, verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(default='', max_length=60, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='course',
            name='tags',
            field=models.CharField(default='', max_length=120, verbose_name='Теги'),
        ),
    ]
