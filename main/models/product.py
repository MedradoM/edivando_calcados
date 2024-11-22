from django.db import models

from main.models.brand import Brand
from main.models.galery import Galery
from main.models.group import GroupModel

class Product(models.Model):
    PRODUCT_STATUS = {
        "SD": "Default",
        "SH": "Highlight",
    }
    title = models.CharField(max_length=300)
    value = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    description = models.TextField()
    galery = models.ForeignKey(Galery, blank=True, null=True, on_delete=models.CASCADE)
    group = models.ForeignKey(GroupModel, blank=True, null=True, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, blank=True, null=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=PRODUCT_STATUS, default="SD")
    
    def __str__(self):
        return self.title