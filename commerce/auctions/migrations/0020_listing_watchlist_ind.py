# Generated by Django 3.1.5 on 2021-04-24 17:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0019_auto_20210419_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='watchlist_ind',
            field=models.ForeignKey(blank='TRUE', null='TRUE', on_delete=django.db.models.deletion.CASCADE, related_name='my_watchlist', to=settings.AUTH_USER_MODEL),
            preserve_default='TRUE',
        ),
    ]