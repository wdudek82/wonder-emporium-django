# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-06 12:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20170707_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='_is_funny',
            field=models.BooleanField(default=False),
        ),
    ]
