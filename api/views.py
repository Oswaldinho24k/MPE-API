from django.contrib.auth.models import User, Group
from accounts.models import Profile
from egresados.models import Egresado, Estudio, Encuesta, Expectativa, Reporte
from empresas.models import Camara, Empresa, Vacante
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from api.serializers import UserSerializer, GroupSerializer, VacanteSerializer, EmpresaSerializer, ProfileSerializer, EgresadoSerializer

"""
API endpoints for the accounts app
"""
#Users endpoints
class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    authentication_classes = (BasicAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated, )
#Gropus endpoints
class GroupViewSet(viewsets.ModelViewSet):
    
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    authentication_classes = (BasicAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated, )

#Profiles Endpoints
class ProfileViewSet(viewsets.ModelViewSet):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    authentication_classes = (BasicAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated, )

"""
API endpoints for the Empresas app
"""
#Empresas endpoints
class EmpresaViewSet(viewsets.ModelViewSet):

    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    authentication_classes = (BasicAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated, )
    

#Vacantes endpoints
class VacanteViewSet(viewsets.ModelViewSet):
 
    queryset=Vacante.objects.all()
    serializer_class = VacanteSerializer
    authentication_classes = (BasicAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated, )
    
"""
API endpoints for the Egresados app
"""
#Egresados endpoints
class EgresadoViewSet(viewsets.ModelViewSet):
    queryset = Egresado.objects.all()
    serializer_class = EgresadoSerializer
    authentication_classes = (BasicAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated, )
    
