from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from productapp.models import Product, Category
from django.urls import reverse_lazy


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'productapp/product_list.html', {'category': category,
                                                      'categories': categories,
                                                      'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    return render(request,
                  'productapp/product_detail.html', {'product': product})


class ProductCreate(CreateView):
    model = Product
    # form_class = BlogForm
    fields = ['product_name', 'product_category', 'product_description', 'product_price'] #form
    template_name = 'productapp/product_new.html'
    success_url = reverse_lazy('productapp:product_list') # reverse map a url -

class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('productapp:product_list')
