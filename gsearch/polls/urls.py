from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.my_form, name='my_form'),
    path('get/', views.getting, name='getting')
]