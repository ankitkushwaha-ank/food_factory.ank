from django.contrib import admin
from contactenquery.models import contactenquery
class EnqueryAdmin(admin.ModelAdmin):
    list_display = ('name','email','message')

admin.site.register(contactenquery,EnqueryAdmin)

# Register your models here.
