#from django.urls import path

#from . import views

#urlpatterns = [
#    path('', views.index, name='index'),
#]

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
#from . import views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('currencies/', views.CurrencyList.as_view()),
    path('currencies/<int:pk>/', views.CurrencyDetail.as_view()),
    path('dropbox/', views.DropboxList.as_view()),
    path('dropbox/<int:pk>/', views.DropboxDetail.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)