# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-23 19:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_auto_20180422_1720'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='age',
        ),
        migrations.RemoveField(
            model_name='review',
            name='gender',
        ),
    ]
