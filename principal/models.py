from django.db import models

# Create your models here.

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='servicios/', null=True, blank=True)  # opcional
    orden = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre

class BlogPost(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='blog/', null=True, blank=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    orden = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo
