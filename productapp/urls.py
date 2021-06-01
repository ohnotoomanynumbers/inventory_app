from django.urls import path, re_path

from productapp import views

app_name = 'productapp'

urlpatterns=[
    path('', views.product_list, name='product_list'), # localhost/product/
    re_path(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'), # localhost/product/1
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'), # localhost/product/1/1
    path('new/', views.ProductCreate.as_view(), name='product_new'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$/delete', views.ProductDelete.as_view(), name='product_del'),

]
