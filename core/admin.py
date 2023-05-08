from django.contrib import admin
from .models import Cart, Item, OrderedItem



# @admin.register(Item)

# @admin.register(OrderedItem)
class OrderedItemAdmin(admin.TabularInline):
    model= OrderedItem
    # fields=[
    #     'item'
    # ]
    

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    fields=[
        'title',
        'price',
    ]
    
    inlines=[
        OrderedItemAdmin
    ]


# admin.site.register(Cart)
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    fields=[
        'user',
        'items',
        'ordered',
        'placement_time',
        'order_time',
    ]
    

# Register your models here.
