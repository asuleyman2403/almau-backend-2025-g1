from django.urls import path
from .views import get_product_list, get_product_item

urlpatterns = [
    path('', get_product_list),
    path('<int:pk>', get_product_item)
]

