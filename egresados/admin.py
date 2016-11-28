from django.contrib import admin
from .models import Egresado, Estudio, Reporte, Encuesta, Expectativa

# Register your models here.
admin.site.register(Egresado)
admin.site.register(Estudio)
admin.site.register(Reporte)
admin.site.register(Encuesta)
admin.site.register(Expectativa)
