from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy, resolve, reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
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
        context['create_url'] = reverse_lazy('nynet:create_product')
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
        context['create_url'] = reverse_lazy('nynet:create_product')
        context['update_url'] = reverse_lazy('nynet:update_product')
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


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/create-product.html'
    success_url = reverse_lazy('nynet:product_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update product'
        return context


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'delete.html'
    success_url = reverse_lazy('nynet:product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete product'
        context['name'] = 'product'
        context['list_url'] = reverse_lazy('nynet:product_list')
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
        context['create_url'] = reverse_lazy('nynet:create_invoice')
        context['update_url'] = 'nynet:update_invoice'
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


class InvoiceUpdateView(UpdateView):
    model = Invoice
    form_class = InvoiceForm
    template_name = 'invoice/create-invoice.html'
    success_url = reverse_lazy('nynet:datable_invoice')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update invoice'
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
        context['create_url'] = reverse_lazy('nynet:create_inventory')
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
