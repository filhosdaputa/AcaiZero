# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 18:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outros', '0009_casadinho'),
    ]

    operations = [
        migrations.AddField(
            model_name='casadinho',
            name='img',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
