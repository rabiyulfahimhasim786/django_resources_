from rest_framework import serializers
from .models import Currencies, Standards, Countries, Tag

class CurrenciesSerializer(serializers.ModelSerializer):
  class Meta:
    model = Currencies
    fields = '__all__'

class StandardsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Standards
    fields = '__all__'

class CountriesSerializer(serializers.ModelSerializer):
  class Meta:
    model = Countries
    fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tag
    fields = '__all__'