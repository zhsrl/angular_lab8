from django.urls import path
from requests import request

from api import views

from .views import CategoriesView, ProductListView, get_products_by_category

urlpatterns = [
    path('products/', ProductListView.as_view()),
    path('products/<int:id>', ProductListView.get_single),
    path('categories/', CategoriesView.as_view()),
    path('cate/<int:id>', views.get_products_by_category),
    path('categories/<int:id>', CategoriesView.get_single),
    path('categories/<int:id>/products', views.get_products_by_category)

]
