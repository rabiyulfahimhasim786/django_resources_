from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world!")

from rest_framework import viewsets, parsers
from .models import DropBox
from .serializers import DropBoxSerializer
class DropBoxViewset(viewsets.ModelViewSet):
 
    queryset = DropBox.objects.all()
    serializer_class = DropBoxSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    http_method_names = ['get', 'post', 'patch', 'delete']