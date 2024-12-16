from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True) # Cria uma chave única para o usuário
    nome = models.TextField(max_length=255)
    idade = models.IntegerField()