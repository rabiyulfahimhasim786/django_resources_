from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('imgtopdf/', views.imgtopdf, name='imgtopdf'),
    path('jpgtopng/', views.jpgtopng, name='jpgtopng'),
    path('png/', views.png, name='png'),
]