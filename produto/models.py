from django.db import models

from categoria.models import Categoria
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='produtos/')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0)
    quantidade = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.nome