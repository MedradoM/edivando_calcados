from django.db import models

from main.models.category import Category

class GroupModel(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name