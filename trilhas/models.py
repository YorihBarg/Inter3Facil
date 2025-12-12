from django.db import models
from django.contrib.auth.models import User

class Avaliacao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    aula = models.CharField(max_length=20)  # aula1, aula2, aula3
    avaliacao = models.IntegerField(null=True, blank=True)  # 1 a 5

    class Meta:
        unique_together = ('usuario', 'aula')  # garante 1 avaliação por aula

    def __str__(self):
        return f"{self.usuario.username} - {self.aula}"