from django.contrib import admin
from service.models import service
from service.models import mainpage
class serviceAdmin(admin.ModelAdmin):
    list_display = ('service_image','service_title','service_price','service_oldprice','service_rating','service_badge','service_desc')
admin.site.register(service,serviceAdmin)

class mainpageAdmin(admin.ModelAdmin):
    list_display = ('mainpage_image', 'mainpage_title', 'mainpage_desc')

admin.site.register(mainpage,mainpageAdmin)

