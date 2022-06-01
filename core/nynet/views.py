from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from core.nynet.forms import ProductForm, InvoiceForm, InventoryForm, CustomerForm
from core.nynet.models import Product, Invoice, Inventory, Customer


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

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No action sent'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create products'
        context['action'] = 'add'
        context['list_url'] = reverse_lazy('nynet:product_list')
        return context


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/create-product.html'
    success_url = reverse_lazy('nynet:product_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No action sent'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update product'
        context['list_url'] = reverse_lazy('nynet:product_list')
        context['action'] = 'edit'
        return context


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'delete-ajax.html'
    success_url = reverse_lazy('nynet:product_list')
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
    
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
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No action sent'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create invoice'
        context['action'] = 'add'
        context['list_url'] = reverse_lazy('nynet:datable_invoice')
        return context


class InvoiceUpdateView(UpdateView):
    model = Invoice
    form_class = InvoiceForm
    template_name = 'invoice/create-invoice.html'
    success_url = reverse_lazy('nynet:datable_invoice')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No action sent'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update invoice'
        context['list_url'] = reverse_lazy('nynet:datable_invoice')
        context['action'] = 'edit'
        return context


class InvoiceDeleteView(DeleteView):
    model = Invoice
    template_name = 'delete-ajax.html'
    success_url = reverse_lazy('nynet:datable_invoice')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete invoice'
        context['name'] = 'invoice'
        context['list_url'] = reverse_lazy('nynet:datable_invoice')
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
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No action sent'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create inventory'
        context['action'] = 'add'
        context['list_url'] = reverse_lazy('nynet:datable_inventory')
        return context


class InventoryUpdateView(UpdateView):
    model = Inventory
    form_class = InventoryForm
    template_name = 'inventory/create-inventory.html'
    success_url = reverse_lazy('nynet:datable_inventory')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No action sent'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update invoice'
        context['action'] = 'edit'
        context['list_url'] = reverse_lazy('nynet:datable_inventory')
        return context


class InventoryDeleteView(DeleteView):
    model = Inventory
    template_name = 'delete-ajax.html'
    success_url = reverse_lazy('nynet:datable_inventory')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete inventory'
        context['name'] = 'inventory'
        context['list_url'] = reverse_lazy('nynet:datable_invoice')
        return context


# Customer

class CustomerDatatableView(ListView):
    model = Customer
    template_name = 'customer/datatable-customer.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Customer.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'No action sent'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Datatable of customer'
        context['name'] = 'customer'
        context['create_url'] = reverse_lazy('nynet:create_customer')
        context['action'] = 'searchdata'
        return context


class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer/create-customer.html'
    success_url = reverse_lazy('nynet:datable_customer')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}

        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No action sent'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create customer'
        context['list_url'] = reverse_lazy('nynet:datable_customer')
        context['action'] = 'add'
        return context


class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer/create-customer.html'
    success_url = reverse_lazy('nynet:datable_customer')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No action sent'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update customer'
        context['list_url'] = reverse_lazy('nynet:datable_customer')
        context['action'] = 'edit'
        return context


class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'delete-ajax.html'
    success_url = reverse_lazy('nynet:datable_customer')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete customer'
        context['name'] = 'customer'
        context['list_url'] = reverse_lazy('nynet:datable_customer')
        return context
