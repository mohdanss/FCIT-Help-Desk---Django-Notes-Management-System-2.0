# Generated by Django 3.1.4 on 2021-01-04 12:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myDBMSapp', '0011_auto_20210104_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date_messaged',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 4, 17, 58, 23, 247302)),
        ),
        migrations.AlterField(
            model_name='register',
            name='date_registered',
            field=models.DateTimeField(null=True, verbose_name='Date Registered'),
        ),
    ]
