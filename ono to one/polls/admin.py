from django.contrib import admin

# Register your models here.
from .models import Person, Adhar #

admin.site.register(Person)
admin.site.register(Adhar)
