from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), #чтобы изменить адресс страницы, нужно просто поменять первое значение
    path('about', views.about, name='about'),
]
