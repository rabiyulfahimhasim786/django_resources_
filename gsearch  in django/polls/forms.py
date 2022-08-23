from django import forms
from .models import MyModel

class MyForm(forms.ModelForm):
  class Meta:
    model = MyModel
    fields ='__all__'
    #fields = ["fullname", "mobile_number",]
    #labels = {'fullname': "Name", "mobile_number": "Mobile Number",}