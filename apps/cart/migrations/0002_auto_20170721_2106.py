# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 21:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sessions', '0001_initial'),
        ('shop', '0002_auto_20170707_1850'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sessions.Session'),
        ),
        migrations.AlterUniqueTogether(
            name='cart',
            unique_together=set([('product', 'session')]),
        ),
    ]
