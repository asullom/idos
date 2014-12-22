from django.db import models

# Create your models here.


class Categoria(models.Model):

    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Producto(models.Model):

    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Cliente(models.Model):

    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='test_img', null=True, blank=True)
    dni = models.CharField(max_length=50, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, null=True, blank=True)
    productos = models.ManyToManyField(Producto, null=True, blank=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.nombre
