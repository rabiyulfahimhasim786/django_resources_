from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('json/', views.some_views, name='some_views'),
    path('tables/', views.bot_views, name='bot_views'),
    path('keyvalue/', views.botkv_views, name='botkv_views'),
    #botkv_views
]
