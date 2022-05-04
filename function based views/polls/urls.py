from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', views.apiOverview, name="api-overview"), 
    path('currencies-list/', views.currencyList, name="currencies-list"),
    path('standards-list/', views.standardList, name="standards-list"),
    path('countries-list/', views.countriesList, name="countries-list"),
    path('currencies-list/post/', views.currenciesCreate, name="currencies-update"),
    path('standards-list/post/', views.standardsCreate, name="standards-update"),
    path('countries-list/post/', views.countriesCreate, name="countries-update"),
    path('currencies-list/update/<str:pk>/', views.currenciesUpdate, name="currencies-update"),
    path('standards-list/update/<str:pk>/', views.standardsUpdate, name="standards-update"),
    path('countries-list/update/<str:pk>/', views.countriesUpdate, name="countries-update"),
    path('currencies-list/delete/<str:pk>/', views.currenciesDelete, name="currencies-delete"),
    path('standards-list/delete/<str:pk>/', views.standardsDelete, name="standards-delete"),
    path('countries-list/delete/<str:pk>/', views.countriesDelete, name="countries-delete"),
    path('currencies/', views.CurrencyList.as_view()),
    path('currenies/<int:pk>/', views.CurrencyDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)