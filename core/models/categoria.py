from django.db import models
from .editora import Editora


class Categoria(models.Model):
    descricao = models.CharField(max_length=100)
    editora = models.ForeignKey(Editora, on_delete=models.PROTECT, related_name="livros", null=True, blank=True)

    def __str__(self):
        return self.descricao
