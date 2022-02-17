from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('register/', user_register, name='register'),
    path('accounts/login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('add_url/', add_url, name='add_url'),
    path('<slug:key>', route_to_url, name='route'),
]
