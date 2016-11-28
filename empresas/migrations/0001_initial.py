# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-25 22:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_nombre_completo', models.CharField(blank=True, max_length=150, null=True)),
                ('emp_calle', models.CharField(blank=True, max_length=150, null=True)),
                ('emp_colonia', models.CharField(blank=True, max_length=150, null=True)),
                ('emp_municipio', models.CharField(blank=True, choices=[('Alán', 'Acatlán'), ('Alán', 'Acaxochitlán'), ('Apan', 'Actopan'), ('Aide', 'Agua Blanca de Iturbide'), ('Auba', 'Ajacuba'), ('Acan', 'Alfajayucan'), ('Aoya', 'Almoloya'), ('Apan', 'Apan'), ('Auia', 'Atitalaquia'), ('Axco', 'Atlapexco'), ('Aula', 'Atotonilco de Tula'), ('Ande', 'Atotonilco el Grande'), ('Cali', 'Calnali'), ('Cnal', 'Cardonal'), ('Cngo', 'Chapantongo'), ('Ccán', 'Chapulhuacán'), ('Ctla', 'Chilcuautla'), ('Cosa', 'Cuautepec de Hinojosa'), ('Enal', 'El Arenal'), ('Elán', 'Eloxochitlán'), ('Eata', 'Emiliano Zapata'), ('Ecan', 'Epazoyucan'), ('Fero', 'Francisco I. Madero'), ('Hmpo', 'Huasca de Ocampo'), ('Htla', 'Huautla'), ('Hngo', 'Huazalingo'), ('Htla', 'Huehuetla'), ('Hyes', 'Huejutla de Reyes'), ('Hpan', 'Huichapan'), ('Ipan', 'Ixmiquilpan'), ('Jzma', 'Jacala de Ledezma'), ('Jcán', 'Jaltocán'), ('Jlgo', 'Juárez Hidalgo'), ('Lión', 'La Misión'), ('Ltla', 'Lolotla'), ('Mpec', 'Metepec'), ('Mlán', 'Metztitlán'), ('Mrma', 'Mineral de la Reforma'), ('Mico', 'Mineral del Chico'), ('Mnte', 'Mineral del Monte'), ('Mrez', 'Mixquiahuala de Juárez'), ('Mlla', 'Molango de Escamilla'), ('Nres', 'Nicolás Flores'), ('Nrán', 'Nopala de Villagrán'), ('Orez', 'Omitlán de Juárez'), ('Poto', 'Pachuca de Soto'), ('Pula', 'Pacula'), ('Pres', 'Pisaflores'), ('Pgón', 'Progreso de Obregón'), ('Slán', 'San Agustín Metzquititlán'), ('Saca', 'San Agustín Tlaxiaca'), ('Spec', 'San Bartolo Tutotepec'), ('Slán', 'San Felipe Orizatlán'), ('Sdor', 'San Salvador'), ('Saya', 'Santiago de Anaya'), ('Srre', 'Santiago Tulantepec de Lugo Guerre'), ('Scan', 'Singuilucan'), ('Tllo', 'Tasquillo'), ('Ttla', 'Tecozautla'), ('Tria', 'Tenango de Doria'), ('Tlco', 'Tepeapulco'), ('Tero', 'Tepehuacán de Guerrero'), ('Tmpo', 'Tepeji del Río de Ocampo'), ('Tlán', 'Tepetitlán'), ('Tngo', 'Tetepango'), ('Tama', 'Tezontepec de Aldama'), ('Tngo', 'Tianguistengo'), ('Tuca', 'Tizayuca'), ('Tpan', 'Tlahuelilpan'), ('Tepa', 'Tlahuiltepa'), ('Tapa', 'Tlanalapa'), ('Tnol', 'Tlanchinol'), ('Tpan', 'Tlaxcoapan'), ('Tuca', 'Tolcayuca'), ('Tnde', 'Tula de Allende'), ('Tavo', 'Tulancingo de Bravo'), ('Vpec', 'Villa de Tezontepec'), ('Xpan', 'Xochiatipan'), ('Xlán', 'Xochicoatlán'), ('Yica', 'Yahualica'), ('Zles', 'Zacualtipán de ?ngeles'), ('Zrez', 'Zapotlán de Juárez'), ('Zala', 'Zempoala'), ('Zán', 'Zimapán')], max_length=1, null=True)),
                ('emp_cp', models.CharField(blank=True, max_length=5, null=True)),
                ('emp_direccionvisitas', models.CharField(blank=True, max_length=150, null=True)),
                ('emp_tel', models.CharField(blank=True, max_length=10, null=True)),
                ('emp_fax', models.CharField(blank=True, max_length=20, null=True)),
                ('emp_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('emp_replegal', models.CharField(blank=True, max_length=40, null=True)),
                ('emp_start_date', models.DateField(blank=True, null=True)),
                ('emp_total_number_workes', models.IntegerField(blank=True, null=True)),
                ('emp_giro', models.CharField(blank=True, max_length=40, null=True)),
                ('emp_registry_date', models.DateField(blank=True, null=True)),
                ('emp_name_project_manager', models.CharField(blank=True, max_length=60, null=True)),
                ('emp_puesto', models.CharField(blank=True, max_length=60, null=True)),
                ('emp_rfc', models.CharField(blank=True, max_length=20, null=True)),
                ('emp_acteconomica', models.CharField(blank=True, max_length=250, null=True)),
                ('emp_products_services', models.TextField(blank=True, null=True)),
                ('emp_name_project', models.CharField(blank=True, max_length=100, null=True)),
                ('emp_description', models.TextField(blank=True, null=True)),
                ('emp_size', models.CharField(blank=True, max_length=10, null=True)),
                ('emp_clasificacion', models.CharField(blank=True, max_length=10, null=True)),
                ('emp_sectores', models.IntegerField(blank=True, null=True)),
                ('emp_sector', models.CharField(blank=True, max_length=10, null=True)),
                ('emp_rango_trab', models.CharField(blank=True, max_length=60, null=True)),
                ('emp_acceso', models.CharField(blank=True, max_length=60, null=True)),
                ('emp_extension', models.CharField(blank=True, max_length=60, null=True)),
                ('emp_rfc_imagen', models.ImageField(blank=True, null=True, upload_to='rfc_imagen')),
                ('emp_identificacion', models.CharField(blank=True, max_length=60, null=True)),
                ('emp_identificacion_tutor', models.CharField(blank=True, max_length=60, null=True)),
                ('emp_comprobante', models.CharField(blank=True, max_length=60, null=True)),
                ('emp_carta', models.CharField(blank=True, max_length=60, null=True)),
                ('emp_pagina', models.CharField(blank=True, max_length=60, null=True)),
                ('emp_ubucacion', models.TextField(blank=True, null=True)),
                ('emp_croquis', models.CharField(blank=True, max_length=60, null=True)),
                ('emp_emailreproy', models.EmailField(blank=True, max_length=254, null=True)),
                ('emp_validada', models.IntegerField(blank=True, null=True)),
                ('emp_etapa', models.CharField(blank=True, max_length=60, null=True)),
                ('emp_carpeta', models.IntegerField(blank=True, null=True)),
                ('emp_administra', models.IntegerField(blank=True, null=True)),
                ('emp_visto', models.IntegerField(blank=True, null=True)),
                ('emp', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='empresa', to='accounts.Profile')),
            ],
        ),
    ]
