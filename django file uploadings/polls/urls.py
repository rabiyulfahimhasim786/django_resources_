from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('uploads/', views.simple_upload, name='simple_upload'),
    path('formupload/', views.model_form_upload, name='model_form_upload'),
    #path('new/', views.newest, name='newest'),
]