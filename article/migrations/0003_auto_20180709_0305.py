# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-07-09 03:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20180707_0812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 9, 3, 5, 17, 153264, tzinfo=utc)),
        ),
    ]