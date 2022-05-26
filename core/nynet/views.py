from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView

from core.nynet.forms import ProductForm, InvoiceForm, InventoryForm
from core.nynet.models import Product, Invoice, Inventory


def home_view(request):
    context = {
    }
    return render(request, 'index.html', context)


# Product

class ProductListView(ListView):
    model = Product
    template_name = 'product/list-product.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'List of products'
        context['name'] = 'products'
        context['url'] = ""
        return context


class ProductDatatableView(ListView):
    model = Product
    template_name = 'product/datatable-product.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Datatable of products'
        context['name'] = 'products'
        return context


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/create-product.html'
    success_url = reverse_lazy('nynet:product_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create products'
        return context


# Invoice
class InvoiceDatatableView(ListView):
    model = Invoice
    template_name = 'invoice/datatable-invoice.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Datatable of invoices'
        context['name'] = 'invoices'
        return context


class InvoiceCreateView(CreateView):
    model = Invoice
    form_class = InvoiceForm
    template_name = 'invoice/create-invoice.html'
    success_url = reverse_lazy('nynet:datable_invoice')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create invoice'
        return context

# Inventory

class InventoryDatatableView(ListView):
    model = Inventory
    template_name = 'inventory/datatable-inventory.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Datatable of inventory'
        context['name'] = 'inventory'
        return context


class InventoryCreateView(CreateView):
    model = Inventory
    form_class = InventoryForm
    template_name = 'inventory/create-inventory.html'
    success_url = reverse_lazy('nynet:datable_inventory')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create inventory'
        return context
