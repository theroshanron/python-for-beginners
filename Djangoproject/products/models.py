from django.db import models



class Product(models.Model):
    name = models.CharField(max_length=234)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2082)
    
    
