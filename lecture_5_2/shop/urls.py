from django.urls import path
from .views import get_product_list, get_product_item, delete_product_item, get_main_page, edit_product_item, get_categories_page, edit_category, delete_category, get_category_products

urlpatterns = [
    path('', get_main_page, name='index_page'),

    path('categories/', get_categories_page, name='categories_page'), # GET List, POST
    path('categories/<int:pk>/edit', edit_category, name='edit_category'),
    path('categories/<int:pk>/delete', delete_category, name='delete_category'),
    path('categories/<int:pk>/products', get_category_products, name='category_products_page'),
    path('products/<int:pk>/delete/', delete_product_item, name='remove_product'),
    path('products/<int:pk>/edit/', edit_product_item, name='edit_product'),
    path('products/<int:pk>/', get_product_item, name='product_details'),
    path('products/', get_product_list, name='products_page'),
]

