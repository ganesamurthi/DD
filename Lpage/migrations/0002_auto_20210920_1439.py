# Generated by Django 3.2.7 on 2021-09-20 09:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Lpage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='tiemstamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 9, 20, 9, 9, 50, 736815, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subscriber',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
