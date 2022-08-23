from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=255)
    web = models.CharField(max_length=255)
    #mobile_number = models.IntegerField()

    def __str__(self):
        return "%s %s" % (self.name, self.web)