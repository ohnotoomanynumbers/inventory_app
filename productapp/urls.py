from django.urls import path

from productapp import views

app_name = 'productapp'

urlpatterns=[
    path('', views.CategoryList.as_view(), name='category_list'),
    path('<int:category_id>/', views.ProductList, name='product_list'),
    path('<int:question_id>/results/', views.results, name='results'),

    path('<int:question_id>/vote/', views.vote, name='vote'),
]