# Generated by Django 3.1.4 on 2021-01-04 07:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myDBMSapp', '0006_auto_20210103_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date_messaged',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 4, 12, 19, 18, 796021)),
        ),
        migrations.AlterField(
            model_name='register',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='images/'),
        ),
    ]
