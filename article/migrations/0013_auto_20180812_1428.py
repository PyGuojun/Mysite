# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-08-12 06:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0012_auto_20180812_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 12, 6, 28, 2, 7886, tzinfo=utc)),
        ),
    ]