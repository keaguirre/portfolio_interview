from django.contrib import admin
from .models import Precio, Portafolio, Activo
# Register your models here.

admin.site.register(Precio)
admin.site.register(Portafolio)
admin.site.register(Activo)