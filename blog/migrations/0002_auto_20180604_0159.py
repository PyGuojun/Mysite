# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-06-04 01:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogArticle',
            new_name='BlogArticles',
        ),
    ]
