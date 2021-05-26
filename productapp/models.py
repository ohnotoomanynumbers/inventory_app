from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=200)
    category_id = models.IntegerField()


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_description = models.CharField(max_length=500)
    product_price = models.FloatField(default=0)
    product_image = models.ImageField(upload_to='media', height_field=None, max_length=100)