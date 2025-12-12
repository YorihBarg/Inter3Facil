from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Aula(models.Model):
    trilha = models.CharField(max_length=100)
    titulo = models.CharField(max_length=150)
    conteudo = models.TextField()
    imagem = models.CharField(
        max_length=200,
        help_text="Ex: mestre/img/aula1.png"
    )

    def __str__(self):
        return self.titulo
    

class Progresso(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    avaliacao = models.IntegerField(null=True, blank=True)

    class Meta:
        unique_together = ("usuario", "aula")