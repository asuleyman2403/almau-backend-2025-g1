from django.urls import path
from .views import login_page_view, register_page_view, handle_logout

urlpatterns = [
    path('login/', login_page_view, name='login_page'),
    path('register/', register_page_view, name='register_page'),
    path('logout/', handle_logout, name='logout')
]
