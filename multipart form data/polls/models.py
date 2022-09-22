from django.db import models

# Create your models here.
from django.db import models
 
class DropBox(models.Model):
    title = models.CharField(max_length=30)
    #document = models.FileField(max_length=30)
    document = models.FileField(upload_to='async-kv-table/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    class Meta:
        verbose_name_plural = 'Drop Boxes'
