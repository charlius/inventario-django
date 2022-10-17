from django.db import models
from django.db.models import CharField

class categorias(models.Model):
    title = CharField(max_length=100)
