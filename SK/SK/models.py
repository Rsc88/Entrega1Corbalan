from django.db import models
from django.db.models.fields import CharField


class Bibliografia(models.Model):
    nombre=CharField(max_length=(60))

class Libros(models.Model):
    nombres=CharField(max_length=(60))

class Peliculas(models.Model):
    nombres=CharField(max_length=(80))

class Otros(models.Model):
    clasificacion=CharField(max_length=(60))
                