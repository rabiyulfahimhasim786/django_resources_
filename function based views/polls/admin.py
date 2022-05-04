from django.contrib import admin

from .models import Currencies, Standards, Countries

# Register your models here.

admin.site.register(Currencies)
admin.site.register(Standards)
admin.site.register(Countries)