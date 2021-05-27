from django.db import models

# Create your models here.
from django.urls import reverse_lazy


class Category(models.Model):
    category_name = models.CharField(max_length=200)
    category_id = models.IntegerField()

    def get_absolute_url(self):
        return reverse_lazy('productapp:category_list')


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_description = models.CharField(max_length=500)
    product_price = models.FloatField(default=0)
    product_image = models.ImageField(upload_to='media', height_field=None, max_length=100)


class User(models.Model):
    pass