# Generated by Django 3.2 on 2023-10-10 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20231010_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.PositiveSmallIntegerField(db_index=True, help_text='Укажите год произведения', verbose_name='Год произведения'),
        ),
    ]
