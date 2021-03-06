# Generated by Django 3.1.4 on 2020-12-29 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('password', models.CharField(blank=True, max_length=20, verbose_name='Password')),
                ('designation', models.CharField(choices=[('USER', 'Just a User'), ('CONTRIBUTOR', 'Contributor'), ('EDITOR', 'Editor')], default='USER', max_length=20, verbose_name='designation')),
                ('date_registered', models.DateTimeField(verbose_name='Date Registered')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('purpose', models.CharField(choices=[('SUGGESTION', 'SUGGESTION'), ('COMPLAINT', 'COMPLAINT'), ('APPRECIATION', 'APPRECIATION'), ('REQUEST', 'REQUEST')], default='APPRECIATION', max_length=20, verbose_name='purpose')),
                ('date_registered', models.DateTimeField(verbose_name='Date Sent')),
                ('message', models.TextField(max_length=500, verbose_name='Message')),
                ('date', models.DateField(verbose_name='Date Messaged')),
                ('register', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myDBMSapp.register')),
            ],
        ),
    ]
