# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 17:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0007_auto_20170720_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comanda_acai',
            name='itens',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='outros.acai'),
        ),
    ]