from django.urls import path

from productapp import views

app_name = 'productapp'

urlpatterns=[
    path('', views.CategoryList.as_view(), name='category_list'), # localhost/product/
    path('<int:category_id>/', views.ProductList, name='product_list'), # localhost/product/1
    path('<int:question_id>/<int:product_id>', views.ProductDetail, name='product_detail'), # localhost/product/1/1

]
