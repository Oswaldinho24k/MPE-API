
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from django.conf import settings
from api import urls as apiUrls
#from accounts import urls as acUrls
#from egresados import urls as egUrls
#from empresas import urls as emUrls
from sedeco import urls as sedecoURLs



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(
        regex=r'^media/(?P<path>.*)$',
        view=serve,
        kwargs={'document_root':settings.MEDIA_ROOT}),
    #url(r'^accounts/', inlcude(acUrls)),
    #url(r'^empresas/', inlcude(acUrls)),
    #url(r'^egresados/', inlcude(acUrls))
    url(r'^api/', include(apiUrls)),
    url(r'^',
        include(sedecoURLs)),


]


