# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 19:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outros', '0013_acaicreme'),
    ]

    operations = [
        migrations.AddField(
            model_name='acaicreme',
            name='img',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
