from django.urls import path

from core.nynet.views import ProductListView, ProductDatatableView, ProductCreateView, InvoiceDatatableView, \
    InvoiceCreateView, InventoryDatatableView, InventoryCreateView, ProductUpdateView, InvoiceUpdateView, \
    ProductDeleteView, InvoiceDeleteView, CustomerDeleteView, CustomerCreateView, CustomerUpdateView, \
    InventoryUpdateView, CustomerDatatableView, InventoryDeleteView

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
    path('invoices/edit/<int:pk>/', InvoiceUpdateView.as_view(), name='update_invoice'),
    path('invoices/delete/<int:pk>/', InvoiceDeleteView.as_view(), name='delete_invoice'),

    # Inventory
    path('inventories/datatable/', InventoryDatatableView.as_view(), name='datable_inventory'),
    path('inventories/add/', InventoryCreateView.as_view(), name='create_inventory'),
    path('inventories/edit/<int:pk>/', InventoryUpdateView.as_view(), name='update_inventory'),
    path('inventories/delete/<int:pk>/', InventoryDeleteView.as_view(), name='delete_inventory'),

    # Customer
    path('customers/datatable/', CustomerDatatableView.as_view(), name='datable_customer'),
    path('customers/add/', CustomerCreateView.as_view(), name='create_customer'),
    path('customers/edit/<int:pk>/', CustomerUpdateView.as_view(), name='update_customer'),
    path('customers/delete/<int:pk>/', CustomerDeleteView.as_view(), name='delete_customer'),

]
