# Generated by Django 3.1.4 on 2021-01-05 09:10

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myDBMSapp', '0014_auto_20210105_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='userMain',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='contact',
            name='date_messaged',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 5, 14, 10, 11, 125028)),
        ),
    ]
