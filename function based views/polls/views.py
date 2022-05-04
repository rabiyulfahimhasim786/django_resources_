from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CurrenciesSerializer, StandardsSerializer, CountriesSerializer

from .models import Currencies, Standards, Countries

from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.


@api_view(['GET'])
def apiOverview(request):
  api_urls ={
    'List': '/task-list/',
    'Detail View': '/task-detail/<str:pk>/',
    'Create': '/task-create/',
    'Update':'/task-update/<str:pk>/',
    'Delete':'/task-delete/<str:pk>/',
    'Currencies': '/currencies-list/',
    'Countries': '/countries-list/',
    'Standards': '/standards-list/',
    'Currency': '/curreny-list/<str:pk>/',
    'Country': '/country-list/<str:pk>/',
    'Standard': '/standards-list/<str:pk>/',
  }
  return Response(api_urls)

@api_view(['GET'])
def currencyList(request):
  currencies = Currencies.objects.all()
  serializer = CurrenciesSerializer(currencies, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def standardList(request):
  standards = Standards.objects.all()
  serializer = StandardsSerializer(standards, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def countriesList(request):
  countries = Countries.objects.all()
  serializer = CountriesSerializer(countries, many=True)
  return Response(serializer.data)

@api_view(['POST'])
def currenciesCreate(request):  
  serializer = CurrenciesSerializer(data=request.data)
  
  if serializer.is_valid():
      serializer.save()

  return Response(serializer.data)

@api_view(['POST'])
def standardsCreate(request):  
  serializer = StandardsSerializer(data=request.data)
  
  if serializer.is_valid():
      serializer.save()

  return Response(serializer.data)

@api_view(['POST'])
def countriesCreate(request):  
  serializer = CountriesSerializer(data=request.data)
  
  if serializer.is_valid():
      serializer.save()

  return Response(serializer.data)

@api_view(['POST'])
def currenciesUpdate(request, pk): 
  currencies = Currencies.objects.get(id=pk)
  serializer = CurrenciesSerializer(instance=currencies, data=request.data)
  
  if serializer.is_valid():
      serializer.save()

  return Response(serializer.data) 

@api_view(['POST'])
def standardsUpdate(request, pk): 
  standards = Standards.objects.get(id=pk)
  serializer = StandardsSerializer(instance=standards, data=request.data)
  
  if serializer.is_valid():
      serializer.save()

  return Response(serializer.data) 

@api_view(['POST'])
def countriesUpdate(request, pk): 
  countries = Countries.objects.get(id=pk)
  serializer = CountriesSerializer(instance=countries, data=request.data)
  
  if serializer.is_valid():
      serializer.save()

  return Response(serializer.data)

@api_view(['DELETE'])
def currenciesDelete(request, pk): 
  currencies = Currencies.objects.get(id=pk)
  currencies.delete()

  return Response('Done')  

@api_view(['DELETE'])
def standardsDelete(request, pk): 
  standards = Standards.objects.get(id=pk)
  standards.delete()

  return Response('Done')  

@api_view(['DELETE'])
def countriesDelete(request, pk): 
  countries = Countries.objects.get(id=pk)
  countries.delete()

  return Response('Done')

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