from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):

	
	TIPO = (
		('EM', 'Empresa'), 
		('EG', 'Egresado'), 
		)
	user = models.OneToOneField(User, null=True, blank=True)
	name = models.CharField(max_length=100, blank=True, null=True)
	email = models.EmailField(blank=True, null=True)
	password = models.CharField(max_length=100, blank=True, null=True)
	photo = models.ImageField(upload_to="/account/photo", blank=True, null=True)
	tipo = models.CharField(max_length=2, choices=TIPO, blank=True, null=True)

	def __str__(self):
		return self.name