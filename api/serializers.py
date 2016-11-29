from django.contrib.auth.models import User, Group
from accounts.models import Profile
from egresados.models import Egresado, Estudio, Encuesta, Expectativa, Reporte
from empresas.models import Camara, Empresa, Vacante
from rest_framework import serializers

"""
Serializers for each model of the accounts app
"""
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Profile
		fields = ('user', 'name', 'email', 'photo', 'tipo')

"""
Serializers for each model of the Empresas app
"""

class EmpresaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Empresa
		fields = ('emp','emp_nombre')

class VacanteSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Vacante
		fields = ('empresa','egresado','puesto')

"""
Serializers for each model of the Egresados app
"""
class EgresadoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Egresado
		fields = ('egr','nombre', 'universidad', 'carrera' )

