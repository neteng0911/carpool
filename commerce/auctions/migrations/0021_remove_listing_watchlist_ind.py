# Generated by Django 3.1.5 on 2021-04-24 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0020_listing_watchlist_ind'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='watchlist_ind',
        ),
    ]