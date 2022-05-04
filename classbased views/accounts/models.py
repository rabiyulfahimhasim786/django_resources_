from django.db import models

# Create your models here.

class Currencies(models.Model):
    iso = models.IntegerField()
    description = models.CharField(max_length=10)
    
    def __str__(self):
        return "%s %s" % (self.description, self.iso)

class Standards(models.Model):
    rate = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.rate

class Tag(models.Model):
    description = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.description

class Countries(models.Model):
    Country_name = models.CharField(max_length=100, null=True)
    Latitude = models.IntegerField()
    Langitude= models.IntegerField()
    currencies = models.ForeignKey(Currencies, null=True, on_delete = models.CASCADE)

    def __str__(self):
        return self.Country_name


class Meta:
        ordering = ['Country_name']
