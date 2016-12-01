from django.contrib.auth.models import User, Group
from accounts.models import Profile
from egresados.models import Egresado, Estudio, Encuesta, Expectativa, Reporte
from empresas.models import Camara, Empresa, Vacante
from rest_framework import viewsets

from api.serializers import UserSerializer, GroupSerializer, VacanteSerializer, EmpresaSerializer, ProfileSerializer, EgresadoSerializer

#Agregamos el login y permisos
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
#PErmisos
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response

"""
API endpoints for the accounts app
"""
#Users endpoints
class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    authentication_classes = (BasicAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated, )


    @list_route(methods=['post'],
        authentication_classes=[BasicAuthentication],
        permission_classes=[IsAuthenticated])
    def updatetoken(self, request, *args, **kwargs):
        # serializer = ProfileSerializer(instance=request.user, data=request.data)
        try:
            token = request.data['token']
            user = request.user
            user.profile.token = token
            user.profile.save()
            return Response({'Token actualizado':True})
        except:
            return Response({'Token actualizado': False})


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
    
