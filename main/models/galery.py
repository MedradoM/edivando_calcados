from django.db import models

from main.models.image import ImageField

class Galery(models.Model):
    name = models.CharField(null=True, max_length=30)
    img = models.ManyToManyField(ImageField, blank=True)
    