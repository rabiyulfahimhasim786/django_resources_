#from django.shortcuts import render

# Create your views here.
#from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.response import Response
from .serializers import CurrenciesSerializer, DropboxSerializer#, StandardsSerializer, CountriesSerializer, TagSerializer

from .models import Currencies, Dropbox#, Standards, Countries, Tag

from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world.")


class CurrencyList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        currencies = Currencies.objects.all()
        serializer = CurrenciesSerializer(currencies, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CurrenciesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CurrencyDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Currencies.objects.get(pk=pk)
        except Currencies.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        currencies = self.get_object(pk)
        serializer = CurrenciesSerializer(currencies)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        currencies = self.get_object(pk)
        serializer = CurrenciesSerializer(currencies, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class DropboxList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        dropbox = Dropbox.objects.all()
        serializer = DropboxSerializer(dropbox, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DropboxSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DropboxDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Dropbox.objects.get(pk=pk)
        except Dropbox.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        dropbox = self.get_object(pk)
        serializer = DropboxSerializer(dropbox)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        dropbox = self.get_object(pk)
        serializer = DropboxSerializer(dropbox, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)