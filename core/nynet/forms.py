from django.forms import ModelForm, TextInput, Textarea, ClearableFileInput, NumberInput, EmailInput, Select, \
    DateTimeInput
from .models import Product, Invoice, Inventory, Customer


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'class': 'input',
                    'placeholder': 'Name of product',
                    'type': 'text',
                }
            ),
            'description': Textarea(
                attrs={
                    'class': 'textarea',
                    'placeholder': 'Description of product',
                }
            ),

            'image': ClearableFileInput(
                attrs={
                    'class': 'file-input',
                    'type': 'file',
                }
            ),
            'price': NumberInput(
                attrs={
                    'class': 'input'
                }
            )

        }
        exclude = ['user_updated', 'user_creation']

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class InvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'
        widgets = {
            'subtotal': NumberInput(
                attrs={
                    'class': 'input',
                    'readonly': '',
                    'name': 'subtotal',
                }
            ),
            'total': NumberInput(
                attrs={
                    'class': 'input',
                    'readonly': '',
                    'name': 'total',
                }
            ),
            'iva': NumberInput(
                attrs={
                    'class': 'input',
                    'name': 'iva',
                }
            ),
            'date_joined': DateTimeInput(
                attrs={
                    'type': 'date',
                    'name': 'date_joined',

                }
            ),
        }
        exclude = ['user_updated', 'user_creation']

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class InventoryForm(ModelForm):
    class Meta:
        model = Inventory
        fields = '__all__'
        widgets = {
            'stock': NumberInput(
                attrs={
                    'class': 'input'
                }
            )
        }
        exclude = ['user_updated', 'user_creation']

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            'first_name': TextInput(
                attrs={
                    'class': 'input',
                    'placeholder': 'First name',
                    'type': 'text',
                }
            ),
            'last_name': TextInput(
                attrs={
                    'class': 'input',
                    'placeholder': 'Last name',
                    'type': 'text',
                }
            ),
            'dni': NumberInput(
                attrs={
                    'class': 'input'
                }
            ),
            'address': TextInput(
                attrs={
                    'class': 'input',
                    'placeholder': 'Address',
                    'type': 'text',
                }
            ),
            'email': EmailInput(
                attrs={
                    'class': 'input',
                    'type': 'email',
                    'placeholder': 'Email',
                }
            ),
            'amount_invoices': NumberInput(
                attrs={
                    'class': 'input'
                }
            ),
        }
        exclude = ['user_updated', 'user_creation']

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
