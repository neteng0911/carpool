# Generated by Django 3.1.5 on 2022-02-13 16:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Capstone', '0003_remove_route_passenger'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='passenger',
            field=models.ManyToManyField(blank='TRUE', related_name='routes', to=settings.AUTH_USER_MODEL),
        ),
    ]
