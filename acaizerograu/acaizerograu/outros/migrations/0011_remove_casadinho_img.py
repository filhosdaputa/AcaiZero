# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 18:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outros', '0010_casadinho_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='casadinho',
            name='img',
        ),
    ]
