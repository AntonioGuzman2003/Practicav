from django.db import models
from server.model.CategoriaModel import CategoriaModel

class PostModel(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    picture = models.URLField(max_length=2000, default=None, blank=True, null=True)
    categoria = models.ForeignKey(CategoriaModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo