from django.contrib import admin

# Register your models here.
from .models import Product, Category

admin.site.register(Product) # You might want to register categories as well :)
admin.site.register(Category)