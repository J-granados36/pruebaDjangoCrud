from django.db import models

# Create your models here.

class Empleado(models.Model):
    codigo = models.CharField(primary_key=True,max_length=6)
    nombre = models.CharField( max_length=50)
    telefono = models.CharField(max_length=15)
    cedula = models.BigIntegerField()
    correo = models.CharField(max_length=30)
    
    def __str__(self):
        texto = "{0}({1})"
        return texto.format(self.nombre,self.telefono,self.cedula,self.correo)
    
    