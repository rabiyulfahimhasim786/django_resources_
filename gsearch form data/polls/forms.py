from django.forms import ModelForm
from .models import Person

class SubscribeForm(ModelForm):
    class Meta:
        model = Person
        exclude = ('output', 'date_subscribed') 