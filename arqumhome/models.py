from django.db import models
from django.contrib.auth.models import User


class InfoPerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    foto_perfil = models.ImageField(upload_to='fotos_perfil', blank=True)

    def __str__(self):
        return self.usuario


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


# class Archivos(models.Model):
