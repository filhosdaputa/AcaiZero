# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 14:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caixa', '0002_auto_20170725_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='caixa',
            name='obs',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='caixa',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 26, 10, 19, 37, 974548)),
        ),
    ]
