from django.db import models

# Create your models here.
from django.db import models

class Precio(models.Model):
    dates = models.DateField()
    eeuu = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    europa = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    japon = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    em_asia = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    latam = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    high_yield = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    ig_corporate = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    emhc = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    latam_hy = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    uk = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    asia_desarrollada = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    emea = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    otros_rv = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    tesoro = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    mbs_cmbs_ambs = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    abs = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    mm_caja = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)

    def __str__(self):
        return f"Precio del {self.dates}"
    
class Portafolio(models.Model):
    fecha = models.DateField()
    activos = models.CharField(max_length=255)
    portafolio_1 = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    portafolio_2 = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)

    def __str__(self):
        return f"Datos de {self.activos} del {self.fecha}"