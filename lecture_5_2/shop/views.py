from django.shortcuts import render, redirect
from .models import Product, Category
from .forms import ProductCreationForm, CategoryForm, ProductEditForm


def get_main_page(request):
    products = Product.objects.all()
    form = ProductCreationForm()
    return render(request, 'shop/index.html', {'products': products, 'form': form})


### CATEGORIES ###
def get_category_products(request, pk):
    products = Product.objects.filter(category_id=pk)
    category = Category.objects.get(id=pk)
    if request.method == 'GET':
        form = ProductCreationForm()
        return render(request, 'shop/category-products.html', {'form': form, 'products': products, 'category': category})
    if request.method == 'POST':
        form = ProductCreationForm(request.POST)
        if form.is_valid():
            title = form.data.get('title')
            description = form.data.get('description')
            amount = form.data.get('amount')
            price = form.data.get('price')
            category_id = pk
            product = Product(title=title, description=description, amount=amount, price=price, category_id=category_id)
            product.save()
        return redirect(to='category_products_page', pk=pk)

def get_categories_page(request):
    categories = Category.objects.all()
    if request.method == 'GET':
        form = CategoryForm()
        return render(request, 'shop/categories.html', {'categories': categories, 'form': form })
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = Category(name=form.data.get('name'))
            category.save()
            return redirect(to='categories_page')
        return render(request, 'shop/categories.html', {'categories': categories, 'form': form })

def edit_category(request, pk):
    category = Category.objects.get(id=pk)
    if request.method == 'GET':
        form = CategoryForm(data={'name': category.name})
        return render(request, 'shop/edit-category.html', {'category': category, 'form': form})
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category.name = form.data.get('name')
            category.save()
        return redirect(to='categories_page')

def delete_category(request, pk):
    category = Category.objects.get(id=pk)
    category.delete()
    return redirect(to='categories_page')


### PRODUCTS ###

def get_product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        form = ProductCreationForm()
        return render(request, 'shop/index.html', {'products': products, 'form': form})
    if request.method == 'POST':
        form = ProductCreationForm(request.POST)
        if form.is_valid():
            title = form.data.get('title')
            description = form.data.get('description')
            amount = form.data.get('amount')
            price = form.data.get('price')
            product = Product(title=title, description=description, amount=amount, price=price)
            product.save()
            return redirect(to='products_page')
        else:
            products = Product.objects.all()
            return render(request, 'shop/index.html', {'products': products, 'form': form})


def get_product_item(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'shop/product-details.html', {'product': product})


def delete_product_item(request, pk):
    try:
        product = Product.objects.get(id=pk)
        product.delete()
        return redirect('/products/')
    except Product.DoesNotExist as e:
        products = Product.objects.all()
        form = ProductCreationForm()
        error = 'Product does not exist'
        return render(request, 'shop/index.html', {'products': products, 'form': form, 'error': error})


def edit_product_item(request, pk):
    product = Product.objects.get(id=pk)
    title = product.title
    description = product.description
    amount = product.amount
    price = product.price
    category_id = product.category.id
    categories = Category.objects.all()

    if request.method == 'GET':
        form = ProductEditForm(data={'title': title, 'description': description, 'amount': amount, 'price': price, 'category_id': category_id})
        return render(request, 'shop/edit-product.html', {'product': product, 'form': form, 'categories': categories})
    if request.method == 'POST':
        form = ProductEditForm(request.POST)
        if form.is_valid():
            title = form.data.get('title')
            description = form.data.get('description')
            amount = form.data.get('amount')
            price = form.data.get('price')
            category_id = form.data.get('category_id')
            product.title = title
            product.description = description
            product.amount = amount
            product.price = price
            product.category_id = category_id
            product.save()
            return redirect(to='category_products_page', pk=category_id)
        else:
            products = Product.objects.all()
            return render(request, 'shop/index.html', {'products': products, 'form': form})


