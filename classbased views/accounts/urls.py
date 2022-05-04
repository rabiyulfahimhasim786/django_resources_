from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('new/', views.new, name='new'),
    path('', views.index, name='index'),
    path('main/', views.main, name='main'),
    path('currencies/', views.CurrencyList.as_view()),
    path('currencies/<int:pk>/', views.CurrencyDetail.as_view()),
    path('countries/', views.CountryList.as_view()),
    path('countries/<int:pk>/', views.CountryDetail.as_view()),
    path('standards/', views.StandardList.as_view()),
    path('standards/<int:pk>/', views.StandardDetail.as_view()),
    path('tag/', views.TagList.as_view()),
    path('tag/<int:pk>/', views.TagDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)