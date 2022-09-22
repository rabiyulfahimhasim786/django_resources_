from django.urls import path

from . import views

from .views import DropBoxViewset
urlpatterns = [
    path('hello/', views.index, name='index'),
]

from rest_framework.routers import SimpleRouter
from .views import DropBoxViewset
router = SimpleRouter()
router.register('accounts', DropBoxViewset)
urlpatterns = router.urls