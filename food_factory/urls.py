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
    path('admin/', include('SysAdmin.urls'), name='admin-login'),
    path('login/', views.user_login, name='user-login'),
    path('register/', views.register_user, name='user-register'),
    path('logout/', views.user_logout, name='user-logout'),
    path('order-sucess/', views.order_sucess, name='order-sucess'),
    path('track-order/', views.track_order, name='track-order'),
    # path('order-detail/', views.order_deatil, name='order-detail'),
    path('page-under-construction/', views.order_deatil, name='order-detail'),
    path('<path>/', views.page_not_found, name='error-page'),
    path('<path>/<ank>/', views.page_not_found1, name='error-page1'),
    # path('<pa>/<an>/<er>', views.page_not_found2, name='error-page11'),
    path('<path>/<ank>/<error>/<error1>', views.page_not_found3, name='error-page3'),
    path('page-in-progress/', views.page_in_progress, name='page-in-progress'),
    path('profile/', views.profile, name='profile-page'),
    path('food_added_to_cart/', views.food_added_to_cart, name='food_added_to_cart'),
    path('chatbot/', views.chatbot_response, name='chatbot'),
]

# Serving static files during development (only for DEBUG mode)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
