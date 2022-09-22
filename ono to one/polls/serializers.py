from rest_framework import serializers
from .models import Adhar, Person#, Standards, Countries, Tag


class PersonSerializer(serializers.ModelSerializer):
  class Meta:
    model = Person
    fields = '__all__'

class AdharSerializer(serializers.ModelSerializer):
  class Meta:
    model = Adhar
    fields = '__all__'