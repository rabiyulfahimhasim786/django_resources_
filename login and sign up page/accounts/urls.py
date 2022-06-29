from django.urls import path
from accounts.views import registration_view, home_screen_view, logout_view, login_view, account_view#, profile_view
from . import views 

urlpatterns = [
    path('index/', views.index, name='index'),
    path('register/', registration_view, name='register'),
    path('home/', home_screen_view, name='home'),
    path('', home_screen_view, name='home'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    #path('profile/', profile_view, name='profile'),
    path('account/', account_view, name='account'),

]