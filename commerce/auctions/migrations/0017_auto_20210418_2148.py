# Generated by Django 3.1.5 on 2021-04-18 18:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_auto_20210418_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='watching',
            field=models.ManyToManyField(blank='TRUE', related_name='watchlist', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bid',
            name='bidder',
            field=models.ForeignKey(blank='TRUE', null='TRUE', on_delete=django.db.models.deletion.CASCADE, related_name='bidders', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bid',
            name='listing_bid',
            field=models.ForeignKey(blank='TRUE', null='TRUE', on_delete=django.db.models.deletion.CASCADE, related_name='listings_bidded', to='auctions.listing'),
        ),
    ]