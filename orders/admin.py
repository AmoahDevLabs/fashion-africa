from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


# def order_detail(obj):
#     url = reverse('orders:admin_order_detail', args=[obj.id])
#     return mark_safe(f'<a href="{url}">View</a>')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'status',
                    'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['first_name', 'address']
    inlines = [OrderItemInline]


admin.site.site_header = 'Quickie Sauce'
