# Generated by Django 3.1.5 on 2022-03-10 19:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Capstone', '0006_auto_20220307_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='date_orig',
            field=models.DateTimeField(default=datetime.date(2022, 3, 10), verbose_name='date orig'),
        ),
        migrations.AlterField(
            model_name='route',
            name='time_dep',
            field=models.TimeField(default=datetime.datetime(2022, 3, 10, 19, 43, 2, 334949, tzinfo=utc), verbose_name='time dep'),
        ),
        migrations.AlterField(
            model_name='route',
            name='time_orig',
            field=models.TimeField(default=datetime.datetime(2022, 3, 10, 19, 43, 2, 334949, tzinfo=utc), verbose_name='time orig'),
        ),
    ]