from django.db import models

class TipoResiduo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class LocalColeta(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    descricao = models.TextField()
    tipo_residuo = models.ManyToManyField(TipoResiduo)

    def __str__(self):
        return self.nome

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=255)
    # Outros campos relevantes

    def __str__(self):
        return self.nome
