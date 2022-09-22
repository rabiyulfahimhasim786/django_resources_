from django.db import models

# Create your models here.
from django.db import models# Create your models here.
class Person(models.Model):
    name = models.TextField(max_length=100)
    email = models.EmailField()
    mobile = models.TextField(max_length=100)
    
class Adhar(models.Model):
    person = models.OneToOneField(Person,on_delete=models.CASCADE,primary_key=True,)
    signature = models.TextField()
    adhar_no = models.TextField(max_length=100)