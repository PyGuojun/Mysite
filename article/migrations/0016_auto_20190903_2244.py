# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-09-03 14:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0015_auto_20190902_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 3, 14, 43, 59, 735128, tzinfo=utc)),
        ),
    ]
