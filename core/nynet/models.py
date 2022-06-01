from django.db import models
from django.forms import model_to_dict


class Update(models.Model):
    date_updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Product(Update):
    name = models.CharField(max_length=50, verbose_name='Name', unique=True)
    description = models.TextField(verbose_name='Description')
    image = models.ImageField(upload_to='products/%Y', verbose_name='Image')
    value = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Value')
    date_creation = models.DateTimeField(auto_now=True)

    def get_image(self):
        if self.image:
            return f"{'/media/'}{self.image}"

        return '/static/img/product_empty.png'

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        db_table = 'product'


class Inventory(Update):
    product = models.OneToOneField(Product, on_delete=models.DO_NOTHING, verbose_name='Name of product', unique=True)
    stock = models.PositiveIntegerField(default=0, verbose_name='Stock')

    def __str__(self):
        return f"{self.product}"

    class Meta:
        verbose_name = 'Inventory'
        verbose_name_plural = 'Inventories'
        db_table = 'inventory'


class Customer(Update):
    first_name = models.CharField(max_length=50, verbose_name='First name')
    last_name = models.CharField(max_length=50, verbose_name='Last name')
    dni = models.PositiveIntegerField(verbose_name='Dni', unique=True)
    address = models.CharField(max_length=100, verbose_name='Address')
    email = models.EmailField(verbose_name='Email')
    amount_invoices = models.PositiveIntegerField(verbose_name='Amount of invoices', default=0)

    def __str__(self):
        return f"{self.dni}"

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        db_table = 'customer'


class Invoice(models.Model):
    list_of_products = models.ManyToManyField(Inventory, verbose_name='Products')
    # employee = models.OneToOneField(Employee, on_delete=models.DO_NOTHING)
    customer = models.OneToOneField(Customer, on_delete=models.DO_NOTHING)
    date_creation = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} {self.date_creation}"

    class Meta:
        verbose_name = 'Invoice'
        verbose_name_plural = 'Invoices'
        db_table = 'invoice'
