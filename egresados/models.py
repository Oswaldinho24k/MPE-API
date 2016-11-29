from django.db import models
from accounts.models import Profile
from django.contrib.auth.models import User
#from empresas.models import Vacante

# Create your models here.

"""
Modelo de Datos de registro de Egresado para ser válido
"""
GENDER = (('m', 'Hombre'), ('M', 'Mujer'))
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
UNIVERSIDADES = (
	('U01','Instituto Tecnológico Sup. del Oriente del E. de Hidalgo (ITESA) (Apan)'),
	('U02','Universidad Politécnica Francisco I. Madero (UPFIM) (Francisco Madero)'),
	('U03','Universidad Tecnológica de la Huasteca Hidalguense (UTHH) (Huejutla)'),
	('U04','Instituto Tecnológico de Huejutla (Huejutla)'),
	('U05','Instituto Tecnológico Superior de Huichapan (ITESHU) (Huichapan)'),
	('U06','Universidad Tecnológica del Valle del Mezquital (UTVM) (Ixmiquilpan)'),
	('U07','Instituto Tecno. Sup. del Occ. del E. de Hidalgo (ITSOEH) (Mixquiahuala)'),
	('U08','Instituto Tecnológico de Pachuca (Pachuca)'),
	('U09','Universidad Pedagógica Nacional (UPN) (Pachuca - Tulancingo) '),
	('U10','Universidad Politécnica Metropolitana de Hidalgo (UPMH) (Pachuca)'),
	('U11','Universidad Autónoma del Estado de Hidalgo (UAEH) '),
	('U12','Universidad Tecnológica de Tula - Tepeji (UTTT) (Tula)'),
	('U13','Universidad Tecnológica de Tulancingo (Tulancingo)'),
	('U14','Universidad Politécnica de Tulancingo (UPT) (Tulancingo)'),
	('U15','Universidad Tec. de la Sierra Hidalguense (UTSH) (Zacualtipán de Ángeles)'),
	('U16','Universidad Politécnica de Pachuca (UPP) (Zempoala)'),
	('U17','Ateneo Universitario en Humanidades y Ciencias de la Salud (Pachuca)'),
	('U18','Centro Académico Bicentenario (CAB - UNAM) (Pachuca)'),
	('U19','Centro Universitario "Vasco de Quiroga" de Huejutla (CUVAQHSTJ) (Huejutla)'),
	('U20','Centro Universitario del Oriente de Hidalgo (CUOH) (Tulancingo) '),
	('U21','Centro Cultural Europeo de Estudios Universitarios de Hidalgo (Pachuca)'),
	('U22','Centro de Estudio Valores con Libertad (Tulancingo)'),
	('U23','Centro Universitario Antares (Pachuca)'),
	('U24','Centro de Estudios Superiores Iddea (Zimapan)'),
	('U25','Centro de Estudios Universitarios Henry Fayol (CEUHF) (Apan)'),
	('U26','Centro de Estudios Universitarios Leonardo de Vinci (Huejutla) '),
	('U27','Centro de Estudios Universitarios Moyocoyani (Actopan)  '),
	('U28','Centro de Posgrados Santander (La loma)'),
	('U29','Centro de Sistemas Computacionales (Ixmiquilpan) '),
	('U30','Centro Educativo Arje Tulancingo (Tulancingo)'),
	('U31','Centro Hidalguense de Estudios Superiores (CENHIES) (Pachuca)'),
	('U32','Centro Metropolitano de Arquitectura Sustentable (CMAS) (Tulancingo)'),
	('U33','Centro Universitario Continental (Pachuca)'),
	('U34','Centro Universitario Allende (CENUA) (Tula) '),
	('U35','Centro Universitario de desarrollo Intelectual (CUDI) (Pachuca)'),
	('U36','Centro Universitario de la Ciudad de México (Pachuca)'),
	('U37','Centro Universitario Hidalguense (CUH) (Pachuca)'),
	('U38','Centro Universitario Interamericano (CEUNI) (Tizayuca)'),
	('U39','Centro Universitario Siglo XXI (Pachuca)'),
	('U40','Centro Universitario Siglo XXI (Zacualtipan)'),
	('U41','Instituto Tecnológico Latinoamericano (ITLA) (Mineral de la Reforma - Tula)'),
	('U42','Tecnológico de Monterrey (ITESM) (Pachuca)'),
	('U43','Universidad Interamericana para el Desarrollo (UNID) (Pachuca - Tula)'),
	('U44','Universidad del Fútbol y Ciencias del Deporte (UFCD) (Tlaxiaca)'),
	('U45','Universidad La Salle Pachuca (Tlaxiaca)'),
	('U46','Universidad ETAC (Tulancingo)'),
	('U47','Universidad del Nuevo México (Tula)'),
	('U78','Instituto Carl Rogers Pachuca (Pachuca)'),
	('U49','Circulo de Estudios de Logoterapia y Análisis Existencial (CELAE) (Pachuca)'),
	('U50','Colegio Anahuac (Tula)'),
	('U51','Colegio de Estudios Superiores Hispanoamericano (Ixmiquilpan) '),
	('U52','Colegio Jorge Berganza (Tula)'),
	('U53','Colegio Libre de Hidalgo (Pachuca)'),
	('U54','Colegio Real Hidalgo (Pachuca)'),
	('U55','Colegio Superior de Odontología de Hidalgo (CSOH) (Pachuca)'),
	('U56','Colegio Vasconcelos Posgrado (Tezontepec)'),
	('U57','Grupo Educativo Virtud y Ciencia (Tula)'),
	('U58','Instituto de Administracion Publica del Estado de Hidalgo (IAPH) (Pachuca)'),
	('U59','Instituto de Ciencias y Estudios Superiores de Hidalgo (Huejutla) '),
	('U60','Instituto de Enseñanza Superior Alfonso Cravioto (Tula)'),
	('U61','Instituto de Estudios Superiores de Progreso de Obregón (IESPOH) (P. Obregon)'),
	('U62','Instituto de Estudios Superiores del Altiplano (IESA) (Tlanalapa)'),
	('U63','Instituto de Estudios Superiores Elise Freinet (Pachuca)'),
	('U64','Instituto de Estudios Superiores John F Kennedy (Pachuca)'),
	('U65','Instituto de Estudios Superiores Plata (IESP) (Pachuca)'),
	('U66','Instituto de Estudios Superiores Tiozihuatl (Huejutla) '),
	('U67','Instituto de Posgrado en Psicoterapia Cognitivo Conductual (IPPCC) (Mineral de la Reforma)'),
	('U68','Instituto Gastronomito Hidalguense (Pachuca)'),
	('U69','Instituto Mexicano de Terapias Breves (Pachuca)'),
	('U70','Instituto Tecnológico Cultural de Hidalgo (ITECH) (Pachuca)'),
	('U71','Instituto Tecnológico de Educación Superior (Tula)'),
	('U72','Instituto Universitario Conde de Guevara (IUCG) (Atotonilco)'),
	('U73','Instituto Universitario del Centro de México (Pachuca)'),
	('U74','Liceo Superior de Hidalgo (Pachuca)'),
	('U75','Pedro de Gante (Tula)'),
	('U76','Universidad Canadiense (Tula)'),
	('U77','Universidad Científica Latino Americana de Hidalgo (UCLAH) (Pachuca)'),
	('U78','Universidad Humanística Hidalgo (Pachuca)'),
	('U79','Universidad Iberomexicana de Hidalgo (Pachuca)'),
	('U80','Universidad INECUH (Tizayuca)'),
	('U81','Universidad Interactiva Milenio (Pachuca)'),
	('U82','Universidad Interamericana para el Desarrollo Campus Pachuca (Pachuca)'),
	('U83','Universidad Interamericana para el Desarrollo Campus Tula (Tula)'),
	('U84','Universidad Interglobal  (Pachuca)'),
	('U85','Universidad Madero Hidalgo Baluarte de la Verdad (Mineral de la Reforma)'),
	('U86','Universidad Privada Del Centro (Pachuca)'),
	('U87','Universidad Tecnológica Internacional (Tlaxcoapan)'),
	('U88','Universidad Tollancingo (Tula)')
		)
CARRERAS = (
	('Aac','Abogacía'),
	('Ali','Accidentología Vial'),
	('Aor','Actuario'),
	('Adl','Administración de Servicios de Salud'),
	('Aau','Agrimensura'),
	('Aam','Agronomía'),
	('Asm','Análisis de Sistemas'),
	('Aag','Antropología'),
	('Aag','Archivología'),
	('Asu','Arquitectura'),
	('Adr','Arte dramático (Teatro)'),
	('Ast','Artes - Bellas Artes'),
	('Asc','Artes Plásticas'),
	('Ang','Asesoramiento de imagen'),
	('Aam','Astronomía'),
	('Arr','Azafata o comisario de a bordo'),
	('Bag','Bibliotecología'),
	('Bai','Bioquímica'),
	('Bor','Bioterio'),
	('Bag','Bromatología'),
	('Cai','Caligrafía Pública'),
	('Cln','Camarero Profesional'),
	('Con','Canto'),
	('Coo','Ceremonial y Protocolo'),
	('Cai','Ciencia Política'),
	('Cst','Ciencia y Tecnología de los alimentos'),
	('Csc','Ciencias Biológicas'),
	('Cae','Ciencias de la Atmósfera'),
	('Cni','Ciencias de la Computación'),
	('Cna','Ciencias de la Comunicación'),
	('Cnd','Ciencias de la Educación'),
	('Cor','Ciencias del Gobierno'),
	('Csc','Ciencias Físicas'),
	('Csa','Ciencias Geológicas'),
	('Csd','Ciencias Químicas'),
	('Cln','Cocinero Profesional'),
	('Cni','Comercialización'),
	('Cln','Comercio Internacional'),
	('Clc','Composición Musical'),
	('Crt','Constructor'),
	('Crd','Contador'),
	('Cai','Criminalistica'),
	('Dsv','Despachante de aeronaves'),
	('Dlr','Dirección Coral'),
	('Daf','Dirección de Fotografía'),
	('Dlt','Dirección Orquestal'),
	('Dst','Diseño de Historietas'),
	('Doi','Diseño de Imagen y Sonido'),
	('Dlt','Diseño de Indumentaria y textil'),
	('Dsr','Diseño de Interiores'),
	('Dpi','Diseño de Paisaje (Agronomía)'),
	('Dbw','Diseño de sitios web'),
	('Dpr','Diseño del Paisaje (Arquitectura)'),
	('Dlu','Diseño en Comunicación Visual'),
	('Doi','Diseño Gráfico'),
	('Dli','Diseño Industrial'),
	('Eag','Ecología'),
	('Esi','Economía y administración agrarias'),
	('Eni','Edición'),
	('Eai','Educación Física'),
	('Eia','Educación Inicial (preescolar)'),
	('Ear','Enfermería'),
	('Eoi','Escribano Público'),
	('Fac','Farmacia'),
	('Faf','Filosofía'),
	('Fau','Floricultura'),
	('Fag','Fonoaudiología'),
	('Gaf','Geografía'),
	('Gst','Gestión de Agroalimentos'),
	('Gsv','Gestión de Instituciones Educativas'),
	('Hap','Hemoterapia'),
	('Har','Historia'),
	('Har','Hotelería'),
	('Iai','Ingeniería Aeronáutica'),
	('Iar','Ingeniería Agraria'),
	('Ilt','Ingeniería Ambiental'),
	('Iai','Ingeniería Biomédica'),
	('Ilv','Ingeniería Civil'),
	('Ili','Ingeniería Comercial'),
	('Ist','Ingeniería de Alimentos'),
	('Ipi','Ingeniería Eléctrica'),
	('Idi','Ingeniería Electromecánica'),
	('Iai','Ingeniería Electrónica'),
	('Isn','Ingeniería en Comunicaciones'),
	('Iai','Ingeniería en Física Médica'),
	('Isl','Ingeniería en Materiales'),
	('Iol','Ingeniería en Petróleo'),
	('Ism','Ingeniería en Sistemas'),
	('Ilt','Ingeniería Forestal'),
	('Iai','Ingeniería Hidráulica'),
	('Ili','Ingeniería Industrial'),
	('Iai','Ingeniería Informática'),
	('Ini','Ingeniería Mecánica'),
	('Iki','Ingeniería Metalúrgica'),
	('Iai','Ingeniería naval y mecánica'),
	('Iae','Ingeniería Pesquera'),
	('Iai','Ingeniería Química'),
	('Ieo','Instructor del Método DeRose'),
	('Ioi','Instrumentador Quirúrgico'),
	('Jar','Jardinería'),
	('Kag','Kinesiología'),
	('Lae','Lengua Inglesa'),
	('Lsr','Letras'),
	('Lni','Licenciado en Administración'),
	('Ldd','Licenciado en Biodiversidad'),
	('Lam','Licenciado en Economía'),
	('Lai','Licenciado en Educación Física'),
	('Lsn','Licenciado en Sistemas de Información de las Organizaciones'),
	('Loa','Licenciatura / Profesorado en Piano'),
	('Lsu','Licenciatura en Alemán, Francés, Inglés, Italiano y Portugués'),
	('Llt','Licenciatura en Artes Visuales con orientación en: Escultura, Pintura, Grabado y Arte Textil'),
	('Lag','Licenciatura en Biotecnología'),
	('Lli','Licenciatura en Educación Especial'),
	('Lau','Licenciatura en Escultura'),
	('Laf','Licenciatura en Fotografía'),
	('Lai','Licenciatura en Genética'),
	('Llt','Licenciatura en Gerenciamiento Ambiental'),
	('Loa','Licenciatura en Grabado'),
	('Lsd','Licenciatura en Humanidades'),
	('Laa','Licenciatura en Lengua y Literatura Castellana'),
	('Lte','Licenciatura en Management'),
	('Lag','Licenciatura en Museología'),
	('Lss','Licenciatura en Ortesis y Prótesis'),
	('Lsn','Licenciatura en producción de bio-imágenes'),
	('Lai','Licenciatura en Seguridad Pública'),
	('Los','Licenciatura en Urbanismo'),
	('Mgi','Marketing'),
	('Mrd','Martillero Público, Corredor (Mobiliario e Inmobiliario), Administrador de Consorcios y Tasador'),
	('Msc','Matemáticas'),
	('Mai','Medicina'),
	('Mag','Meteorologia'),
	('Map','Musicoterapia'),
	('Noi','Notario público'),
	('Nni','Nutrición'),
	('Oac','Obstetricia'),
	('Oaf','Oceanografía'),
	('Oag','Odontología'),
	('Ooi','Óptico técnico'),
	('Ost','Organización de Eventos'),
	('Oni','Organización de la Producción'),
	('Pag','Paleontología'),
	('Pln','Panadero Profesional'),
	('Plb','Pastelero Profesional'),
	('Plt','Perfecionamiento Instrumental'),
	('Paa','Perfusionista en cirugía cardíaca'),
	('Pos','Periodismo'),
	('Pli','Piloto Comercial'),
	('Pau','Pintura'),
	('Pag','Podología'),
	('Pni','Procuración'),
	('Pai','Producción Radial y Televisiva'),
	('Psi','Profesional en Artes Culinarias'),
	('Pui','Profesorado en Educación General Básica'),
	('Plc','Profesorado en Educación Musical'),
	('Pag','Profesorado en Enseñanza Media y Superior en Psicología'),
	('Par','Profesorado en Guitarra'),
	('Pri','Profesorado en Informática'),
	('Pld','Profesorado Universitario para el Tercer ciclo de la de la EGB y la Educación Polimodal'),
	('Pag','Psicología'),
	('Pag','Psicopedagogía'),
	('Pdd','Publicidad'),
	('Rlu','Realización Audiovisual'),
	('Rsn','Recursos Humanos'),
	('Roa','Relaciones del Trabajo'),
	('Rsl','Relaciones Internacionales'),
	('Rml','Relaciones Públicas e Institucionales'),
	('Rni','Religión'),
	('Soi','Secretariado Ejecutivo'),
	('Sls','Sindicatura Concursal'),
	('Sdd','Sistemas de Seguridad'),
	('Svc','Sistemas Informáticos'),
	('Sag','Sociología'),
	('Tni','Tecnicatura en Prevención de Drogadicción'),
	('Tsl','Técnicatura en Producción de Medios Audiovisuales, Eventos y Espectáculos'),
	('Tas','Tecnico Ceramista'),
	('Tag','Técnico de Laboratorio Clínico e Histopatología'),
	('Tsc','Técnico en Análisis Clínicos'),
	('Tae','Técnico en Producción Lechera'),
	('Tsr','Técnico en Seguros'),
	('Tas','Técnico Mecánico Electricista'),
	('Tms','Técnico Mecánico Electricista'),
	('Toa','Técnico Museógrafo'),
	('Too','Técnico Radiólogo'),
	('Tsm','Técnico Superior en Cosméticos y Perfumes'),
	('Tsc','Técnico Superior en Cultivo y Obtención de Aromáticas'),
	('Tsl','Tecnico Universitario En Asuntos Municipales'),
	('Tlp','Técnico Universitario en Dinámica Grupal'),
	('Tbr','Técnico Universitario en Industria de la Madera.'),
	('Tar','Técnico Universitario en Minería'),
	('Tln','Terapia Ocupacional'),
	('Tli','Trabajo Social'),
	('Toi','Traductorado Público'),
	('Tsl','Traductorado Público en Idioma Inglés'),
	('Tos','Turismo'),
	('Var','Veterinaria'),
		)

class Egresado(models.Model):

	egr = models.OneToOneField(User, null=True, blank=True)
	nombre = models.CharField(max_length=50, null=True, blank=True)
	apellidop = models.CharField(max_length=50, null=True, blank=True)
	apellidom = models.CharField(max_length=50, null=True, blank=True)
	edad = models.IntegerField(null=True, blank=True)
	#lugar = ???
	sexo = models.CharField(max_length=1, choices=GENDER, null=True, blank=True)
	curp = models.CharField(max_length=18, null=True, blank=True)
	municipio = models.CharField(max_length=4, choices=MUNICIPIOS, null=True, blank=True)
	calle = models.CharField(max_length=50, null=True, blank=True)
	numero = models.IntegerField(blank=True, null=True)
	colonia = models.CharField(max_length=50, null=True, blank=True)
	fechaentregatitulo = models.DateField(auto_now_add=True, null=True, blank=True)
	cp = models.IntegerField(null=True, blank=True)
	telefonofijo = models.IntegerField( null=True, blank=True)
	celular = models.IntegerField(null=True, blank=True)
	email = models.EmailField(null=True, blank=True)
	#nivel = ???
	universidad = models.CharField(max_length=3,choices=UNIVERSIDADES, null=True, blank=True)
	carrera = models.CharField(max_length=3, choices=CARRERAS, null=True, blank=True)
	#situacion = ???
	añoegreso = models.DateField(null=True, blank=True)
	fechaingresoprograma = models.DateField(auto_now=True, null=True, blank=True)
	#colocado = ???
	certificado = models.FileField(upload_to = "egresado/certificado", null=True, blank=True)
	identificacion = models.FileField(upload_to = "egresado/identificación", null=True, blank=True)
	compdomicilio = models.FileField(upload_to = "egresado/domicilio", null=True, blank=True)
	titulo = models.FileField(upload_to = "egresado/titulo", null=True, blank=True)
	fcurp = models.FileField(upload_to = "egresado/curp", null=True, blank=True)
	carta = models.FileField(upload_to = "egresado/carta", null=True, blank=True)
	fechatitulacion = models.DateField(auto_now_add=True, null=True, blank=True)
	promedio = models.DecimalField(decimal_places=2, max_digits=4, null=True, blank=True)
	becario = models.BooleanField("Es Becario",default= False)
	#modalidadtitulo = ???
	#empleoformal = ???
	#empleocual = ???
	#municipios = Repetido
	#sectores = #
	#compromiso = #
	#folio 
	#perfil
	rfc = models.CharField(max_length=13, null=True, blank=True)
	#status
	#motivobaja = ???
	#vacante = models.OneToOneField(Vacante, related_name='vacante', blank=True, null=True)
	curriculum = models.FileField(upload_to = "egresado/cv", null=True, blank=True)
	#psicologica ???
	archivopsicologica = models.FileField(upload_to = "egresado/psico", null=True, blank=True)
	notarjeta = models.CharField(max_length=16, blank=True, null=True)
	#noseguropopular = ???
	segpop = models.CharField(max_length=100, blank=True, null=True)
	#traslado = ???
	#etapa = 
	#horaps
	
	validada = models.BooleanField(default=False)
	#userid
	#visto
	#carpeta
	inicio = models.DateField(null=True, blank=True)
	concluye = models.DateField(null=True, blank=True)

	def __str__ (self):
		return self.nombre
"""
Modelo de Estudio Socioeconómico que el egresado debe completar
"""
class Estudio(models.Model):

	EDOC = (
	('C', 'Casado'), 
	('S', 'Soltero'), 
	)

	egresado = models.OneToOneField(User, blank=True, null=True)
	edo_civil = models.CharField(max_length=50,choices = EDOC, blank=True, null=True)
	dependientes = models.CharField(max_length=2, blank=True, null=True)
	situacionlaboral = models.CharField(max_length=20, blank=True, null=True)
	trabajo = models.CharField(max_length=30, blank=True, null=True)
	dependen_ti = models.BooleanField("Alguien depende de ti?", default=True)
	cuantos_depend = models.IntegerField("Cuantos dependen de ti", blank=True, null=True)
	ingreso_mensual = models.CharField(max_length=20, blank=True, null=True)
	transporte = models.BooleanField(default=True)
	vives_en = models.CharField(max_length=60, blank=True, null=True)
	cuantos_hermanos = models.CharField(max_length=20, blank=True, null=True)
	cuantos_papas = models.CharField(max_length=20, blank=True, null=True)
	cuantos_abuelos = models.CharField(max_length=20, blank=True, null=True)
	casa_techo = models.CharField(max_length=20, blank=True, null=True)
	casa_piso = models.CharField(max_length=20, blank=True, null=True)
	casa_pared = models.CharField(max_length=20, blank=True, null=True)
	numero_recamaras = models.CharField(max_length=20, blank=True, null=True)
	numero_banos = models.IntegerField(blank=True, null=True)
	numero_salas = models.IntegerField(blank=True, null=True)	
	numero_comedor = models.CharField(max_length=20, blank=True, null=True)
	numero_vehiculos =   models.IntegerField(blank=True, null=True)	
	numero_recamaras =  models.IntegerField(blank=True, null=True)
	gasto_mensual = models.CharField(max_length=20, blank=True, null=True)
	mayor_gasto = models.CharField(max_length=20, blank=True, null=True)
	otra_beca = models.BooleanField(default=True)

	def __str__(self):
		return self.id

"""
Modelo de Encuestas que el egresado debe rellenar
"""

class Encuesta(models.Model):
	user = models.OneToOneField(User, related_name='encuesta')
	fecha_captura = models.DateField(auto_now=True)
	aporte = models.CharField(max_length=150)
	#por que medio se entero sobre la empresa Supongo
	#facebook, twitter, periodico, tv, radio, escuela, amigo, empresa, otro medio, 
	viade_informacion =  models.CharField(max_length=100)
	act_desemp = models.CharField(max_length=100)
	capacitacion = models.CharField(max_length=200)
	apoyo_extra = models.TextField()
	propuesta = models.TextField()
	contratado = models.BooleanField(default=True)
	motivo_no_contratacion = models.TextField()
	fecha_contrato = models.DateField(auto_now=True)
	salario = models.FloatField()
	evaluacion_experiencia = models.CharField(max_length=200)
	expectativas = models.TextField()
	mejora_programa = models.TextField()
	mejora_empresa = models.TextField()
	mejora_institucion = models.TextField()
	conocimientos = models.TextField()
	entrevista = models.TextField()
	oferta = models.TextField()
	lugar = models.TextField()

	def __str__(self):
		return self.user

class Expectativa(models.Model):

	id_egresado = models.OneToOneField(User, related_name='expectativa')
	entrevista_lab = models.BooleanField(default=True)
	que_quieres = models.CharField(max_length=100)	
	que_esperas = models.CharField(max_length=100)
	uso_beca = models.CharField("Que haras con la beca?",max_length=100)
	aportacion = models.TextField(max_length=100)
	logro = models.TextField("Objetivo Profesional",max_length=100)
	logro_academico = models.CharField("Objetivo Academico",max_length=100)
	formacion = models.CharField("Objetivo Academico",max_length=20)
	eleccion_correcta = models.BooleanField(default=True)
	gasto_mensual = models.CharField(max_length=80)
	empleo_buscado = models.BooleanField("Buscaste empleo", default=True)
	tiempo_busqueda = models.CharField("Cuanto tiempo",max_length=80)
	medios_busqueda = models.CharField("Que medios usaste para buscar",max_length=80)

	def __str__(self):
		return self.id


"""
Modelo de reporte mensual
"""

class Reporte(models.Model):
	egresado = models.ForeignKey(User, related_name='reportes')
	numero = models.IntegerField()
	fecha = models.DateField()
	area = models.CharField(max_length=100)
	tutor = models.CharField(max_length=200)
	actividades = models.CharField(max_length=400)
	aporte = models.CharField(max_length=100)
	monto = models.CharField(max_length=10)
	capacitacion = models.BooleanField(default=True)
	#en_que = models.BooleanField(default=True)
	proyecto =models.CharField(max_length=200)
	recursos = models.BooleanField(default=True)
	experiencia = models.BooleanField(default=True)
	emp_puntualidad = models.BooleanField(default=True)
	emp_imagen = models.BooleanField(default=True)
	emp_actitud = models.BooleanField(default=True)
	emp_aprendio = models.BooleanField(default=True)
	emp_objetivos_cump = models.BooleanField(default=True)
	validado= models.BooleanField(default=True)
	fecha_validacion = models.DateField()
	pago = models.BooleanField(default=True)
	fecha_pago = models.DateField()

	def __str__(self):
		return self.fecha



