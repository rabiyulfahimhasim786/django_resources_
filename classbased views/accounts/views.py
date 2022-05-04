from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.response import Response
from .serializers import CurrenciesSerializer, StandardsSerializer, CountriesSerializer, TagSerializer

from .models import Currencies, Standards, Countries, Tag

from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status

from django.template.response   import TemplateResponse


def new(request):
    return HttpResponse("Hello, world. You're at the accounts index.")

def index(request):
    return render(request, './index.html')

def main(request):
    return render(request, './main.html')

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

class CountryList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        countries = Countries.objects.all()
        serializer = CountriesSerializer(countries, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CountriesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CountryDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Countries.objects.get(pk=pk)
        except Countries.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        countries = self.get_object(pk)
        serializer = CountriesSerializer(countries)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        countries = self.get_object(pk)
        serializer = CountriesSerializer(countries, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StandardList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        standards = Standards.objects.all()
        serializer = StandardsSerializer(standards, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StandardsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StandardDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Standards.objects.get(pk=pk)
        except Standards.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        standards = self.get_object(pk)
        serializer = StandardsSerializer(standards)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        standards = self.get_object(pk)
        serializer = StandardsSerializer(standards, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TagList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        tag = Tag.objects.all()
        serializer = TagSerializer(tag, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TagDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Tag.objects.get(pk=pk)
        except Tag.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        standards = self.get_object(pk)
        serializer = TagSerializer(standards)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Tag = self.get_object(pk)
        serializer = TagSerializer(Tag, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

