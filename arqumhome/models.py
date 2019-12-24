from django.db import models


class Cliente(models.Model):
    nombre_cliente = models.CharField(max_length=200)
    domicilio_real = models.CharField(max_length=200)
    domicilio_obra = models.CharField(max_length=200)
    correo = models.EmailField()
    telefono = models.CharField(max_length=200,
                                blank=True)
    fecha_alta_cliente = models.DateField()
    fecha_inicio_obra = models.CharField(max_length=8,
                                         blank=True)
    fecha_fin_obra = models.CharField(blank=True,
                                      max_length=8)
