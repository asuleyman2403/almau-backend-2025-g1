from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import login

def login_page_view(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'user/login.html', {'form': form})
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=form.data.get('username'), password=form.data.get('password'))
            login(request, user)
            if user is not None:
                return redirect(to='index_page')
            else:
                form.add_error(field='username', error='Invalid password or login')
                return render(request, 'user/login.html', {'form': form})
        else:
            return render(request, 'user/login.html', {'form': form})


def register_page_view(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'user/register.html', {'form': form})
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_data = auth.authenticate(request, username=user.username, email=user.email, password=form.data.get('password'))
            print(auth_data, form.errors)
            if auth_data is not None:
                login(request, auth_data)
                return redirect(to='index_page')
        return render(request, 'user/register.html', {'form': form})


def handle_logout(request):
    auth.logout(request)
    return redirect('/auth/login')
