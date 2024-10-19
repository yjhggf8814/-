from django.db import models

# Create your models here.
class Produkt(models.Model):
    title = models.CharField(max_length = 86)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    price = models.PositiveIntegerField()
    rating = models.PositiveSmallIntegerField()
    is_available = models.BooleanField(default= True)
    stock = models.IntegerField()
    sale = models.PositiveIntegerField()
