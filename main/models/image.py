from django.db import models

class ImageField(models.Model):
    name = models.CharField(null=True, max_length=50)
    img = models.FileField(upload_to='media')
    type = models.CharField(null=True, max_length=100)
    
    def __str__(self):
        if self.name:
            return f"{self.name} - {self.img}"
        else:
            return f"Image: {self.img}" 