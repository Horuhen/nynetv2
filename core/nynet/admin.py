from django.contrib import admin

from core.nynet.models import Product, Invoice, Inventory


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'image', 'value']


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    fields = ["list_of_products",
              ]


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    fields = ['product', 'stock', ]
