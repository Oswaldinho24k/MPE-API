from django.contrib.auth.models import User, Group
from accounts.models import Profile
from egresados.models import Egresado, Estudio, Encuesta, Expectativa, Reporte
from empresas.models import Camara, Empresa, Vacante
from rest_framework import viewsets
from api.serializers import UserSerializer, GroupSerializer, VacanteSerializer, EmpresaSerializer, ProfileSerializer, EgresadoSerializer

"""
API endpoints for the accounts app
"""
#Users endpoints
class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

#Gropus endpoints
class GroupViewSet(viewsets.ModelViewSet):
    
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

#Profiles Endpoints
class ProfileViewSet(viewsets.ModelViewSet):

	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer
  
"""
API endpoints for the Empresas app
"""
#Empresas endpoints
class EmpresaViewSet(viewsets.ModelViewSet):

    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

#Vacantes endpoints
class VacanteViewSet(viewsets.ModelViewSet):
 
    queryset=Vacante.objects.all()
    serializer_class = VacanteSerializer

"""
API endpoints for the Egresados app
"""
#Egresados endpoints
class EgresadoViewSet(viewsets.ModelViewSet):

	queryset = Egresado.objects.all()
	serializer_class = EgresadoSerializer

