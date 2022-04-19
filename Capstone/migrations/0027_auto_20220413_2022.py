# Generated by Django 3.1.5 on 2022-04-13 17:22

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Capstone', '0026_auto_20220413_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrcode',
            name='passenger',
            field=models.ForeignKey(blank='TRUE', null='TRUE', on_delete=django.db.models.deletion.CASCADE, related_name='code', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='route',
            name='time_dep',
            field=models.TimeField(default=datetime.datetime(2022, 4, 13, 17, 22, 31, 61203, tzinfo=utc), verbose_name='time dep'),
        ),
        migrations.AlterField(
            model_name='route',
            name='time_orig',
            field=models.TimeField(default=datetime.datetime(2022, 4, 13, 17, 22, 31, 61203, tzinfo=utc), verbose_name='time orig'),
        ),
    ]
