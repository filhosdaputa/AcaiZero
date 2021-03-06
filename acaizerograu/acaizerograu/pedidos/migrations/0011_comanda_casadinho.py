# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 18:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('outros', '0009_casadinho'),
        ('pedidos', '0010_auto_20170721_1743'),
    ]

    operations = [
        migrations.CreateModel(
            name='comanda_casadinho',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tamanho', models.CharField(choices=[('P', 'Pequeno'), ('G', 'Grande')], max_length=1)),
                ('total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('itens', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='outros.casadinho')),
            ],
        ),
    ]
