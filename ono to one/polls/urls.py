from django.urls import path
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('person/', views.PersonList.as_view()),
    path('person/<int:pk>/', views.PersonDetail.as_view()),
    path('adhar/', views.AdharList.as_view()),
    path('adhar/<int:pk>/', views.AdharDetail.as_view()),
]



urlpatterns = format_suffix_patterns(urlpatterns)