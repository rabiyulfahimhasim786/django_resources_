from django.db import models

# Create your models here.

class Currencies(models.Model):
    iso = models.IntegerField()
    description = models.CharField(max_length=10)
    
    def __str__(self):
        return self.description

class Standards(models.Model):
    rate = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.rate

class Countries(models.Model):
    Country = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.Country

# Create your models here.
