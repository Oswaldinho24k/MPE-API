# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 07:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('egresados', '0002_encuesta_estudio_expectativa_reportes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reportes',
            new_name='Reporte',
        ),
    ]