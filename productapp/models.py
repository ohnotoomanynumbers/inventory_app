from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_category = models.CharField(max_length=200)
    product_description = models.CharField(max_length=500)
    product_price = models.FloatField(default=0)
    product_image = models.ImageField()