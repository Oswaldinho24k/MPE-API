# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 18:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('egresados', '0007_auto_20161128_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='egresado',
            name='archivopsicologica',
            field=models.FileField(blank=True, null=True, upload_to='egresado/psico'),
        ),
        migrations.AlterField(
            model_name='egresado',
            name='carta',
            field=models.FileField(blank=True, null=True, upload_to='egresado/carta'),
        ),
        migrations.AlterField(
            model_name='egresado',
            name='certificado',
            field=models.FileField(blank=True, null=True, upload_to='egresado/certificado'),
        ),
        migrations.AlterField(
            model_name='egresado',
            name='compdomicilio',
            field=models.FileField(blank=True, null=True, upload_to='egresado/domicilio'),
        ),
        migrations.AlterField(
            model_name='egresado',
            name='curriculum',
            field=models.FileField(blank=True, null=True, upload_to='egresado/cv'),
        ),
        migrations.AlterField(
            model_name='egresado',
            name='egr',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='egresado',
            name='fcurp',
            field=models.FileField(blank=True, null=True, upload_to='egresado/curp'),
        ),
        migrations.AlterField(
            model_name='egresado',
            name='identificacion',
            field=models.FileField(blank=True, null=True, upload_to='egresado/identificación'),
        ),
        migrations.AlterField(
            model_name='egresado',
            name='titulo',
            field=models.FileField(blank=True, null=True, upload_to='egresado/titulo'),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='encuesta', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='estudio',
            name='egresado',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='expectativa',
            name='id_egresado',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='expectativa', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reporte',
            name='egresado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reportes', to=settings.AUTH_USER_MODEL),
        ),
    ]
