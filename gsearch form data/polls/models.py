from django.db import models
from datetime import datetime
# Create your models here.
from django.db import models
#import datetime
# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=255)
    web = models.CharField(max_length=255)
    date_subscribed = models.DateTimeField(default=datetime.now())
    output = models.IntegerField()