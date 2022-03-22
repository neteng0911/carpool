# Generated by Django 3.1.5 on 2022-03-22 17:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Capstone', '0012_auto_20220322_1904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route',
            name='fin',
        ),
        migrations.AlterField(
            model_name='route',
            name='time_dep',
            field=models.TimeField(default=datetime.datetime(2022, 3, 22, 17, 18, 11, 598870, tzinfo=utc), verbose_name='time dep'),
        ),
        migrations.AlterField(
            model_name='route',
            name='time_orig',
            field=models.TimeField(default=datetime.datetime(2022, 3, 22, 17, 18, 11, 598870, tzinfo=utc), verbose_name='time orig'),
        ),
    ]
