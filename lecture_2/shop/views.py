from django.shortcuts import render
from .models import Product


def get_product_list(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def get_product_item(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product-details.html', {'product': product})
