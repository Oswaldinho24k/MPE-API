from django.db import models

# Create your models here.

class Profile(models.Model):

	EMPRESA = 'EM'
	EGRESADO = 'EG'
	TIPO = (
		(EMPRESA, 'Empresa'), 
		(EGRESADO, 'Egresado'), 
		)

	name = models.CharField(max_length=100, blank=True, null=True)
	email = models.EmailField(blank=True, null=True)
	password = models.CharField(max_length=100, blank=True, null=True)
	#photo = models.ImageField(upload_to="/accounts/photo", blank=True, null=True)
	tipo = models.CharField(max_length=2, choices=TIPO, default=EGRESADO, blank=True, null=True)

	def __str__(self):
		return self.name