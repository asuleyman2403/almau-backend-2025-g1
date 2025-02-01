from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductCreationForm


def get_product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        form = ProductCreationForm()
        return render(request, 'index.html', {'products': products, 'form': form})
    if request.method == 'POST':
        form = ProductCreationForm(request.POST)
        if form.is_valid():
            title = form.data.get('title')
            description = form.data.get('description')
            amount = form.data.get('amount')
            price = form.data.get('price')
            product = Product(title=title, description=description, amount=amount, price=price)
            product.save()
            return redirect('/products/')
        else:
            products = Product.objects.all()
            return render(request, 'index.html', {'products': products, 'form': form})


def get_product_item(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product-details.html', {'product': product})


def delete_product_item(request, pk):
    try:
        product = Product.objects.get(id=pk)
        product.delete()
        return redirect('/products/')
    except Product.DoesNotExist as e:
        products = Product.objects.all()
        form = ProductCreationForm()
        error = 'Product does not exist'
        return render(request, 'index.html', {'products': products, 'form': form, 'error': error})
