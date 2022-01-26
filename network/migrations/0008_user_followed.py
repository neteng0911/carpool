# Generated by Django 3.1.5 on 2022-01-15 14:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0007_auto_20220112_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='followed',
            field=models.ForeignKey(blank='TRUE', null='TRUE', on_delete=django.db.models.deletion.CASCADE, related_name='followers', to=settings.AUTH_USER_MODEL),
            preserve_default='TRUE',
        ),
    ]