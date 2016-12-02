from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.ListView.as_view()),
	url(r'^(?P<id>[0-9]+)/$', views.DetailView.as_view(), name='detalle')
]