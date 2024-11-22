from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=50)
    img = models.FileField(upload_to="media")
    
    def __str__(self):
        return self.name
    
