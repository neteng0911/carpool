# Generated by Django 3.1.5 on 2022-01-03 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0005_auto_20220102_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='lists',
            field=models.ManyToManyField(blank='TRUE', related_name='replies', to='network.Mypost'),
        ),
    ]