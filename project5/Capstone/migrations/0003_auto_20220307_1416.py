# Generated by Django 3.1.5 on 2022-03-07 12:16

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Capstone', '0002_auto_20220307_1201'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comm_txt', models.CharField(blank='True', max_length=150)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
        migrations.AlterField(
            model_name='route',
            name='time_dep',
            field=models.TimeField(default=datetime.datetime(2022, 3, 7, 12, 16, 36, 668509, tzinfo=utc), verbose_name='time dep'),
        ),
        migrations.AlterField(
            model_name='route',
            name='time_orig',
            field=models.TimeField(default=datetime.datetime(2022, 3, 7, 12, 16, 36, 668509, tzinfo=utc), verbose_name='time orig'),
        ),
        migrations.DeleteModel(
            name='Reply',
        ),
        migrations.AddField(
            model_name='comment',
            name='lists',
            field=models.ManyToManyField(blank='TRUE', related_name='comments', to='Capstone.Route'),
        ),
        migrations.AddField(
            model_name='comment',
            name='owner',
            field=models.ForeignKey(blank='TRUE', null='TRUE', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='route_comm',
            field=models.ForeignKey(blank='TRUE', null='TRUE', on_delete=django.db.models.deletion.CASCADE, to='Capstone.route'),
        ),
    ]
