from django.contrib import admin

# Register your models here.
from .models import Currencies, Dropbox#, Standards, Countries, Tag

# Register your models here.
admin.site.register(Currencies)
admin.site.register(Dropbox)