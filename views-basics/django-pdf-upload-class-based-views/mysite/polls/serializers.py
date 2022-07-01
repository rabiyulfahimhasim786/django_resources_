from rest_framework import serializers
from .models import Currencies, Dropbox#, Standards, Countries, Tag

class CurrenciesSerializer(serializers.ModelSerializer):
  class Meta:
    model = Currencies
    fields = '__all__'


class DropboxSerializer(serializers.ModelSerializer):
  class Meta:
    model = Dropbox
    fields = '__all__'