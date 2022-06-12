from django.urls import path
from .views import home, store, product, product_list_view, search

app_name = 'store'

urlpatterns = [
    path('', home, name='home'),
    path('store', store, name='store'),
    # path('find', search, name='search'),
    path('store/<slug:slug>', product, name='product'),
    path('<slug:category_slug>/', product_list_view, name='product_list_by_category'),
]
