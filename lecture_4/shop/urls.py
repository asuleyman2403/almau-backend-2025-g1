from django.urls import path
from .views import get_product_list, get_product_item, delete_product_item, get_main_page

urlpatterns = [
    path('', get_main_page, name='index_page'),
    path('products/', get_product_list, name='products_page'),
    path('products/<int:pk>/', get_product_item, name='product_details'),
    path('products/<int:pk>/delete/', delete_product_item, name='remove_product')
]

