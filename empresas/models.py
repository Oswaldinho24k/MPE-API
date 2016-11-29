from django.db import models
from accounts.models import Profile
from egresados.models import Egresado
from django.contrib.auth.models import User

# Create your models here.

"""
Modelo de Cámara a las que pertenecen las empresas
"""
class Camara(models.Model):

	cam_nombre = models.CharField(max_length=100, null=True, blank=True)
	cam_siglas = models.CharField(max_length=10, null=True, blank=True)
	cam_repnombre = models.CharField(max_length=100, null=True, blank=True)
	cam_repcargo = models.CharField(max_length=100, null=True, blank=True)
	cam_repperiodo = models.CharField(max_length=100, null=True, blank=True)
	cam_calleynum = models.CharField(max_length=100, null=True, blank=True)
	cam_colonia = models.CharField(max_length=100, null=True, blank=True)
	cam_municipio = models.CharField(max_length=100, null=True, blank=True)
	cam_cp = models.CharField(max_length=5, null=True, blank=True)
	cam_telefono = models.CharField(max_length=10, null=True, blank=True)
	cam_paginaweb = models.CharField(max_length=100, null=True, blank=True)
	cam_contacto = models.CharField(max_length=100, null=True, blank=True)
	cam_cargocontacto = models.CharField(max_length=100, null=True, blank=True)
	cam_telcontacto = models.CharField(max_length=100, null=True, blank=True)
	cam_email = models.CharField(max_length=100, null=True, blank=True)
	cam_fecha_registro = models.CharField(max_length=100, null=True, blank=True)
	cam_validada = models.CharField(max_length=100, null=True, blank=True)

	def __str__(self):
		return self.cam_nombre

"""
Modelo que contiene todos los datos de registro necesarios para que una empresa sea Válida
"""

class Empresa(models.Model):

	MUNICIPIOS = (
		('Alan','Acatlán'),
		('Alan','Acaxochitlán'),
		('Apan','Actopan'),
		('Aide','Agua Blanca de Iturbide'),
		('Auba','Ajacuba'),
		('Acan','Alfajayucan'),
		('Aoya','Almoloya'),
		('Apan','Apan'),
		('Auia','Atitalaquia'),
		('Axco','Atlapexco'),
		('Aula','Atotonilco de Tula'),
		('Ande','Atotonilco el Grande'),
		('Cali','Calnali'),
		('Cnal','Cardonal'),
		('Cngo','Chapantongo'),
		('Ccan','Chapulhuacán'),
		('Ctla','Chilcuautla'),
		('Cosa','Cuautepec de Hinojosa'),
		('Enal','El Arenal'),
		('Elan','Eloxochitlán'),
		('Eata','Emiliano Zapata'),
		('Ecan','Epazoyucan'),
		('Fero','Francisco I. Madero'),
		('Hmpo','Huasca de Ocampo'),
		('Htla','Huautla'),
		('Hngo','Huazalingo'),
		('Htla','Huehuetla'),
		('Hyes','Huejutla de Reyes'),
		('Hpan','Huichapan'),
		('Ipan','Ixmiquilpan'),
		('Jzma','Jacala de Ledezma'),
		('Jcan','Jaltocán'),
		('Jlgo','Juárez Hidalgo'),
		('Lian','La Misión'),
		('Ltla','Lolotla'),
		('Mpec','Metepec'),
		('Mlan','Metztitlán'),
		('Mrma','Mineral de la Reforma'),
		('Mico','Mineral del Chico'),
		('Mnte','Mineral del Monte'),
		('Mrez','Mixquiahuala de Juárez'),
		('Mlla','Molango de Escamilla'),
		('Nres','Nicolás Flores'),
		('Nran','Nopala de Villagrán'),
		('Orez','Omitlán de Juárez'),
		('Poto','Pachuca de Soto'),
		('Pula','Pacula'),
		('Pres','Pisaflores'),
		('Pgan','Progreso de Obregón'),
		('Slan','San Agustín Metzquititlán'),
		('Saca','San Agustín Tlaxiaca'),
		('Spec','San Bartolo Tutotepec'),
		('Slan','San Felipe Orizatlán'),
		('Sdor','San Salvador'),
		('Saya','Santiago de Anaya'),
		('Srre','Santiago Tulantepec de Lugo Guerre'),
		('Scan','Singuilucan'),
		('Tllo','Tasquillo'),
		('Ttla','Tecozautla'),
		('Tria','Tenango de Doria'),
		('Tlco','Tepeapulco'),
		('Tero','Tepehuacán de Guerrero'),
		('Tmpo','Tepeji del Río de Ocampo'),
		('Tlan','Tepetitlán'),
		('Tngo','Tetepango'),
		('Tama','Tezontepec de Aldama'),
		('Tngo','Tianguistengo'),
		('Tuca','Tizayuca'),
		('Tpan','Tlahuelilpan'),
		('Tepa','Tlahuiltepa'),
		('Tapa','Tlanalapa'),
		('Tnol','Tlanchinol'),
		('Tpan','Tlaxcoapan'),
		('Tuca','Tolcayuca'),
		('Tnde','Tula de Allende'),
		('Tavo','Tulancingo de Bravo'),
		('Vpec','Villa de Tezontepec'),
		('Xpan','Xochiatipan'),
		('Xlan','Xochicoatlán'),
		('Yica','Yahualica'),
		('Zles','Zacualtipán de ?ngeles'),
		('Zrez','Zapotlán de Juárez'),
		('Zala','Zempoala'),
		('Zana','Zimapán')  
				)

	emp = models.OneToOneField(User, related_name='empresa', null=True, blank=True)
	emp_nombre = models.CharField(max_length=150, null=True, blank=True)
	emp_calle = models.CharField(max_length=150, null=True, blank=True)
	emp_colonia = models.CharField(max_length=150, null=True, blank=True)
	emp_municipio = models.CharField(max_length=4, choices=MUNICIPIOS, null=True, blank=True)
	emp_cp = models.CharField(max_length=5, null=True, blank=True)
	emp_direccionvisitas = models.CharField(max_length=150, null=True, blank=True)
	emp_tel = models.CharField(max_length=10, null=True, blank=True)
	emp_fax = models.CharField(max_length=20, null=True, blank=True)
	emp_email = models.EmailField(null=True, blank=True)
	emp_replegal = models.CharField(max_length=40, null=True, blank=True)
	emp_start_date = models.DateField(null=True, blank=True)
	emp_total_number_workes = models.IntegerField(null=True, blank=True)
	emp_giro = models.CharField(max_length=40, null=True, blank=True)
	emp_registry_date = models.DateField(null=True, blank=True)
	emp_name_project_manager = models.CharField(max_length=60, null=True, blank=True)
	emp_puesto = models.CharField(max_length=60, null=True, blank=True)
	emp_rfc = models.CharField(max_length=20, null=True, blank=True)
	emp_acteconomica = models.CharField(max_length=250, null=True, blank=True)
	emp_products_services = models.TextField(null=True, blank=True)
	emp_name_project = models.CharField(max_length=100, null=True, blank=True)
	emp_description = models.TextField(null=True, blank=True)
	emp_camara = models.ForeignKey(Camara, related_name='camara', null=True, blank=True)
	emp_size = models.CharField(max_length=10, null=True, blank=True)
	emp_clasificacion = models.CharField(max_length=10, null=True, blank=True)
	emp_sectores = models.IntegerField(null=True, blank=True)
	emp_sector = models.CharField(max_length=10, null=True, blank=True)
	emp_rango_trab = models.CharField(max_length=60, null=True, blank=True)
	emp_acceso = models.CharField(max_length=60, null=True, blank=True)
	emp_extension = models.CharField(max_length=60, null=True, blank=True)
	emp_rfc_imagen = models.FileField(upload_to="empresa/rfc",null=True, blank=True)
	emp_identificacion = models.FileField(upload_to="empresa/ide",null=True, blank=True)
	emp_identificacion_tutor =models.FileField(upload_to="empresa/idtutor",null=True, blank=True)
	emp_comprobante = models.FileField(upload_to="empresa/comprobante",null=True, blank=True)
	emp_carta =models.FileField(upload_to="empresa/carta",null=True, blank=True)
	emp_pagina = models.CharField(max_length=60, null=True, blank=True)
	emp_ubucacion =models.TextField(null=True, blank=True)
	emp_croquis = models.CharField(max_length=60, null=True, blank=True)
	emp_emailreproy = models.EmailField(null=True, blank=True)
	emp_validada = models.IntegerField(null=True, blank=True)
	emp_etapa = models.CharField(max_length=60, null=True, blank=True)
	emp_carpeta = models.IntegerField(null=True, blank=True)
	emp_administra = models.IntegerField(null=True, blank=True)
	emp_visto = models.IntegerField(null=True, blank=True)


	def __str__(self):
		return self.emp_nombre_completo

"""
Modelo de Vacantes que las empresas lanzarán al programa de mi primer empleo
"""

class Vacante(models.Model):
	empresa = models.ForeignKey(Empresa, blank=True, null=True)
	egresado = models.ManyToManyField(User, related_name='vacante', blank=True)
	puesto = models.CharField(max_length=80)
	activades = models.TextField(null=True, blank=True)
	dias = models.IntegerField(null=True, blank=True)
	horario_entrada = models.TimeField(blank=True, null=True)
	horario_entrada_sabado = models.TimeField(blank=True, null=True)
	horario_salida = models.TimeField(blank=True, null=True)
	horario_salida_sabado = models.TimeField(blank=True, null=True)
	fecha_alta = models.DateField(blank=True, null=True)
	fecha_asignado = models.DateField(blank=True, null=True)
	vacante_activa = models.BooleanField(default=True)

	def __str__(self):
		return self.puesto
