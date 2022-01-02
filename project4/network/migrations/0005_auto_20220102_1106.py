# Generated by Django 3.1.5 on 2022-01-02 09:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0004_auto_20220102_1015'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply_txt', models.CharField(blank='True', max_length=150)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('mypost_reply', models.ForeignKey(blank='TRUE', null='TRUE', on_delete=django.db.models.deletion.CASCADE, to='network.mypost')),
                ('owner', models.ForeignKey(blank='TRUE', null='TRUE', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
