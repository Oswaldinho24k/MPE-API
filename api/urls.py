from django.conf.urls import url, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
#Accounts routes
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'profiles', views.ProfileViewSet)
#Empresas Routes
router.register(r'vacantes', views.VacanteViewSet)
router.register(r'empresas', views.EmpresaViewSet)
#Egresados Rotes
router.register(r'egresados', views.EgresadoViewSet)


# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]