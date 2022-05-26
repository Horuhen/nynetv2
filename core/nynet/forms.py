from django.forms import ModelForm, TextInput, Textarea, ClearableFileInput, NumberInput
from .models import Product, Invoice, Inventory


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
            'value': NumberInput(
                attrs={
                    'class': 'input'
                }
            )

        }


class InvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'


class InventoryForm(ModelForm):
    class Meta:
        model = Inventory
        fields = '__all__'
        widgets={
            'stock': NumberInput(
                attrs={
                    'class': 'input'
                }
            )
        }
