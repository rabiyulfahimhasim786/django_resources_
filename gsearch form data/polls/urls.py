from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('get/', views.getting, name='getting'),
    path('var/', views.variable, name='variable')
]