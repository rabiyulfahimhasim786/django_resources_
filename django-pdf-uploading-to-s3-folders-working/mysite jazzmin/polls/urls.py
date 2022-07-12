
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
#from . import views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('table/', views.download_dir, name='download_dir'),
    path('json/', views.some_views, name='some_views'),
    path('tables/', views.bot_views, name='bot_views'),
    path('keyvalue/', views.botkv_views, name='botkv_views'),
    #path('currencies/', views.CurrencyList.as_view()),
    #path('currencies/<int:pk>/', views.CurrencyDetail.as_view()),
    path('dropbox/', views.DropboxList.as_view()),
    path('dropbox/<int:pk>/', views.DropboxDetail.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)