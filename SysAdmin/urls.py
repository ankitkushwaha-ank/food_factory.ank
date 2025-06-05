from django.contrib import admin
from django.urls import path
from .views import *


from food_factory import views

urlpatterns = [
    path('', Adminlogin, name='admin_login'),
    path('dashboard/', AdminDasboard, name='admin_dashboard'),
    path('logout/', logout_view, name='admin_logout'),
    path('addmenu/', add_menu, name='add-food'),
    path('addnews/', add_news, name='add-news'),
    path('del_enq/<int:enqid>', del_enquiry, name='del-enq'),
    path('remove/<int:item_id>', remove_item, name='remove-food'),
    path('remove-news/<int:item_id>/', remove_news, name='remove-news'),

]