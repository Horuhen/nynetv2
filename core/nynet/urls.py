from django.urls import path

from core.nynet.views import ProductListView, ProductDatatableView, ProductCreateView, InvoiceDatatableView, \
    InvoiceCreateView, InventoryDatatableView, InventoryCreateView, ProductUpdateView, InvoiceUpdateView, \
    ProductDeleteView

app_name = 'nynet'

urlpatterns = [
    # Product
    path('products/list/', ProductListView.as_view(), name='product_list'),
    path('products/datatable/', ProductDatatableView.as_view(), name='datable_product'),
    path('products/add/', ProductCreateView.as_view(), name='create_product'),
    path('products/edit/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('products/delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),

    # Invoice
    path('invoices/datatable/', InvoiceDatatableView.as_view(), name='datable_invoice'),
    path('invoices/add/', InvoiceCreateView.as_view(), name='create_invoice'),
    path('invoices/edit/<int:pk>', InvoiceUpdateView.as_view(), name='update_invoice'),

    # Inventory
    path('inventories/datatable/', InventoryDatatableView.as_view(), name='datable_inventory'),
    path('inventories/add/', InventoryCreateView.as_view(), name='create_inventory'),
]
