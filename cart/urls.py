from django.urls import path
from .views import add_to_cart, cart_, checkout, update_cart, hx_menu_cart, hx_cart_total

app_name = 'cart'

urlpatterns = [
    path('', cart_, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('add_to_cart/<uuid:product_id>/', add_to_cart, name='add_to_cart'),
    path('update_cart/<uuid:product_id>/<str:action>/', update_cart, name='update_cart'),
    path('hx_menu_cart/', hx_menu_cart, name='hx_menu_cart'),
    path('hx_cart_total/', hx_cart_total, name='hx_cart_total'),
]
