# Generated by Django 4.2.2 on 2023-06-22 16:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 6, 22, 16, 30, 35, 840440)),
        ),
    ]
