from django.db import models

# Create your models here.
class Order(models.Model):
    name = models.CharField(max_length=30,null=False)
    email = models.CharField(max_length=50,null=False)
    phone = models.CharField()
    food = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=250,null=True)
    Price = models.CharField()
    Quantity=models.PositiveIntegerField( null=True,default=1)
    Special_Instructions=models.TextField(null=True,default=None)
    order_type = models.CharField(max_length=20,default='delivery')
    payment_mode=models.CharField(max_length=20,default='cash')

