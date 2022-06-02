from django.contrib import admin

from core.nynet.models import Product, Invoice, Inventory, Customer


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'image', 'price']


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    fields = ["list_of_products",
              ]


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    fields = ['product', 'stock', ]


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'dni', 'address', 'email', 'amount_invoices', ]

