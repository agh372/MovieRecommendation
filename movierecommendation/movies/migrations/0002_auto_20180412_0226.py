# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-12 02:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='age',
            field=models.IntegerField(default=18),
            preserve_default=False,
        ),
    ]