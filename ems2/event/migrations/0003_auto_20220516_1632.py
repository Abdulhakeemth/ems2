# Generated by Django 3.0 on 2022-05-16 11:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20220516_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 16, 16, 32, 56, 951787)),
        ),
        migrations.AlterField(
            model_name='event',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 16, 16, 32, 56, 951787)),
        ),
        migrations.AlterField(
            model_name='eventticket',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 16, 16, 32, 56, 951787)),
        ),
    ]