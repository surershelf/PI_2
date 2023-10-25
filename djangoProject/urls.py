from django.contrib import admin
from django.urls import path, include
from .views import hello
from login.views import *
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',pagina_principal, name='pagina_principal'),
    path('hello/',hello),
    path('login/', Login, name='login'),
    path('register/',Register, name='register'),
    
]
