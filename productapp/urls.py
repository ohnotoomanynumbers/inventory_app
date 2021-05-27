from django.urls import path

from productapp import views

app_name = 'productapp'

urlpatterns=[
    path('', views.CategoryList.as_view(), name='category_list'), # localhost/product/
    path('<int:category_id>/', views.ProductList.as_view(), name='product_list'), # localhost/product/1
    path('<int:category_id>/<int:product_id>', views.ProductDetail.as_view(), name='product_detail'), # localhost/product/1/1
    path('new/', views.ProductCreate.as_view(), name='product_new'),

]
