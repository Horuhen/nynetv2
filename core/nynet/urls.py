from django.urls import path

from core.nynet.views import ProductListView, ProductDatatableView, ProductCreateView, InvoiceDatatableView, \
    InvoiceCreateView, InventoryDatatableView, InventoryCreateView

app_name = 'nynet'

urlpatterns = [
    # Product
    path('products/list/', ProductListView.as_view(), name='product_list'),
    path('products/datatable/', ProductDatatableView.as_view(), name='datable_product'),
    path('products/add/', ProductCreateView.as_view(), name='create_product'),

    # Invoice
    path('invoices/datatable/', InvoiceDatatableView.as_view(), name='datable_invoice'),
    path('invoices/add/', InvoiceCreateView.as_view(), name='create_invoice'),

    # Inventory
    path('inventories/datatable/', InventoryDatatableView.as_view(), name='datable_inventory'),
    path('inventories/add/', InventoryCreateView.as_view(), name='create_inventory'),
]