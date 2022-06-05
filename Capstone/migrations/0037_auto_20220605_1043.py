# Generated by Django 3.1.5 on 2022-06-05 07:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Capstone', '0036_auto_20220522_2108'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='route',
            name='date_orig',
            field=models.DateTimeField(default=datetime.date(2022, 6, 5), verbose_name='date orig'),
        ),
        migrations.AlterField(
            model_name='route',
            name='time_dep',
            field=models.TimeField(default=datetime.datetime(2022, 6, 5, 7, 43, 14, 52414, tzinfo=utc), verbose_name='time dep'),
        ),
        migrations.AlterField(
            model_name='route',
            name='time_orig',
            field=models.TimeField(default=datetime.datetime(2022, 6, 5, 7, 43, 14, 52414, tzinfo=utc), verbose_name='time orig'),
        ),
    ]
