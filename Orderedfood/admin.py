from django.contrib import admin
from Orderedfood.models import Order
class Food_order(admin.ModelAdmin):
    list_display = ('name','email','phone','food','Price','Quantity','Special_Instructions','order_type','payment_mode')
admin.site.register(Order,Food_order)

# Register your models here.
