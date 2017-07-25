# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 22:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20170707_1850'),
        ('sessions', '0001_initial'),
        ('cart', '0006_auto_20170722_1902'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cart',
            unique_together=set([('product', 'price', 'session')]),
        ),
    ]