from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from productapp.models import Product, Category
from django.urls import reverse_lazy


class CategoryList(ListView):
    model = Category
    template_name = 'productapp/category_list.html'


class ProductList(ListView):
    model = Product
    template_name = 'productapp/product_list.html'
    context_object_name = 'products'


class ProductDetail(DetailView):
    model = Product
    template_name = 'productapp/product_detail.html'
    context_object_name = 'product'  # 'product' 'object'{}


class ProductCreate(CreateView):
    model = Product
    # form_class = BlogForm
    fields = ['name', 'category', 'description', 'price'] #form
    template_name = 'productapp/product_new.html'  # If not provided, searches for 'blog/blog_form.html'
    success_url = reverse_lazy('productapp:product_list') # reverse map a url -