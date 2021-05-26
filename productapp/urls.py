from django.urls import path

from productapp import views

app_name = 'productapp'

urlpatterns=[
    path('', views.CategoryList.as_view(), name='category_list'),
    path('<int:category_id>/', views.ProductList, name='product_list'),
    path('<int:question_id>/<int:product_id>', views.ProductDetail, name='product_detail'),

]