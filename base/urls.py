
from django.contrib import admin
from django.urls import path
from .views import ProductListCreate, ProductDetail , StudentsListCreate
from base import views

# urls.py


urlpatterns = [
    path('', views.index),
    path('products/', ProductListCreate.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('student/', StudentsListCreate.as_view(), name='student-detail'),


]
