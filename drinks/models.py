from django.db import models

class Drinks (models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name + ' '+self.description
    
class Article (models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=250)
    description = models.TextField(max_length=20000)
    price = models.CharField(max_length=100)
    url = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.brand +' '+ self.model