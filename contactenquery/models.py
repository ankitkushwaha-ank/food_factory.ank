from django.db import models
from django.utils import timezone

# Create your models here.
class contactenquery(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    message=models.TextField()
    time = models.DateTimeField(default=timezone.now)
