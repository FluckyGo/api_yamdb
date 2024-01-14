# Generated by Django 3.2 on 2023-10-10 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20231010_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.PositiveSmallIntegerField(verbose_name='Оценка произведения'),
        ),
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.PositiveSmallIntegerField(help_text='Укажите год произведения', verbose_name='Год произведения'),
        ),
    ]
