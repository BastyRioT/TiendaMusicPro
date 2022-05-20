from django.db import models
from django.utils import timezone

categoria=[
    [0, "Ninguno"],
    [1, "Cuerdas"],
    [2, "Percusión"],
    [3, "Amplificadores"],
    [4, "Accesorios"] ]

class Producto(models.Model) :
    serie_producto = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    codigo = models.CharField(max_length=15)
    marca = models.CharField(max_length=30)
    precio = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)
    imagen = models.ImageField(upload_to='img', null=True)
    categoria = models.IntegerField(choices=categoria,null=True)

    def __str__(self) :
        return self.nombre