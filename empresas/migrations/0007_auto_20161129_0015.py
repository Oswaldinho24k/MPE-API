# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 00:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0006_auto_20161129_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacante',
            name='empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vacante', to='empresas.Empresa'),
        ),
    ]
