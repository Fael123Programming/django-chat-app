# Generated by Django 4.2.2 on 2023-06-22 16:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('room', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=1000000)),
                ('timestamp', models.DateTimeField(blank=True, default=datetime.datetime(2023, 6, 22, 16, 26, 59, 591576))),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
