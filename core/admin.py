from django.contrib import admin
from .models import Cart, Item, OrderedItem



# @admin.register(Item)

# @admin.register(OrderedItem)
class OrderedItemAdmin(admin.TabularInline):
    model= OrderedItem
    fields=[
        'item'
    ]
    

class ItemAdmin(admin.ModelAdmin):
    list_display=[
        'title',
        'price',
    ]
    
    inlines=[
        OrderedItemAdmin
    ]


admin.site.register(Cart)
# class CartAdmin(admin.ModelAdmin):
#     list_display=[
#         'user',
#         'items',
#         'ordered',
#         'placement_time',
#         'order_time',
#     ]
    

# Register your models here.
