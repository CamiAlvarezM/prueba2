from django.contrib import admin

# Register your models here.

from . models import Index, Info, Formulario, Galeria, We

admin.site.register(Index)
admin.site.register(Info)
admin.site.register(Formulario)
admin.site.register(Galeria)
admin.site.register(We)