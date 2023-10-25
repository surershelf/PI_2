
from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    genero = models.CharField(max_length=10)

# Create your models here.
