# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 21:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0009_comanda_acaimix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comanda_acaimix',
            name='itens',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='outros.acaimix'),
        ),
    ]
