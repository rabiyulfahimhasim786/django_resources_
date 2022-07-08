from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gallery/', views.gallery, name='gallery'),
    path('photo/<str:pk>', views.viewphoto, name='photo'),
    path('add/', views.addphoto, name='add'),
    #path('h/', views.index, name='index'),
    #path(),
   # path(),
]