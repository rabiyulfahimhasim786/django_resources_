from rest_framework import serializers
from .models import Currencies, Standards, Countries

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