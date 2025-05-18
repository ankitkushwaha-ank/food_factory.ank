from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from food_factory import views

urlpatterns = [
    path('dj-admin/', admin.site.urls),
    path('', views.index_page, name='home'),
    path('home/', views.index_page, name='home_redirect'),
    path('menu/', views.menu_page, name='menu'),
    path('menu_detail/<slug>/', views.menu_detail, name='menu_detail'),
    path('promotions/', views.promotion_page, name='promotions'),
    path('contact/', views.contact_page, name='contact'),
    path('karaoke/', views.karaoke_page, name='karaoke'),
    path('form/', views.form_page, name='form'),
    path('add-to-cart/<int:item_id>/', views.addtocart, name='add_to_cart'),
    path('cart/', views.cart_page, name='cart_detail'),
    path('remove_all/', views.remove_all, name='remove-all'),
    path('remove/<int:item_id>/', views.remove_item, name='remove-item'),
    path('order/<slug>/', views.order_page, name='orderpage'),
    path('ordercart/', views.ordercart_page, name='order-cart'),
    path('submit-order/', views.ordersubmit, name='order-submit'),
    path('scroll/', views.scrollinfinite, name='scroll'),
    path('admin/', include('SysAdmin.urls'), name='admin-login'),
    path('login/', views.user_login, name='user-login'),
    path('register/', views.register_user, name='user-register'),
    path('logout/', views.user_logout, name='user-logout'),
]

# Serving static files during development (only for DEBUG mode)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
