from django.urls import path
from .views import order_create, payment_success

app_name = 'orders'


urlpatterns = [
    path('initiate_order/', order_create, name='order_create'),
    path('payment/success/', payment_success, name='payment_success'),
]
