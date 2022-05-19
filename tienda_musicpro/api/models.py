from django.db import models
from django.utils import timezone

# Create your models here.

class Producto(models.Model) :
    serie_producto = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    codigo = models.CharField(max_length=15)
    marca = models.CharField(max_length=30)
    precio = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self) :
        return self.nombre