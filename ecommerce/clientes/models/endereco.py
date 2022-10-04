from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models

from .user import User

class Endereco(models.Model):
    rua = models.CharField(max_length=255)
    numero = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)