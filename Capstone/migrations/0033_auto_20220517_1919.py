# Generated by Django 3.1.5 on 2022-05-17 16:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Capstone', '0032_auto_20220517_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='time_dep',
            field=models.TimeField(default=datetime.datetime(2022, 5, 17, 16, 19, 25, 994005, tzinfo=utc), verbose_name='time dep'),
        ),
        migrations.AlterField(
            model_name='route',
            name='time_orig',
            field=models.TimeField(default=datetime.datetime(2022, 5, 17, 16, 19, 25, 994005, tzinfo=utc), verbose_name='time orig'),
        ),
    ]
