#from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
# declare a new model with a name "Currencies"
class Currencies(models.Model):
    # fields of the model
    iso = models.IntegerField()
    description = models.CharField(max_length=10)
    # renames the instances of the model
        # with their title name
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