from crum import get_current_user
from django.db import models
from django.forms import model_to_dict
from django.conf import settings


class Update(models.Model):
    date_updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    user_creation = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING,
                                      related_name="user_creation", null=True, blank=True)
    user_updated = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name="user_updated",
                                     null=True, blank=True)

    class Meta:
        abstract = True


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name', unique=True)
    description = models.TextField(verbose_name='Description')
    image = models.ImageField(upload_to='products/%Y', verbose_name='Image')
    value = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Value')
    date_updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    user_creation = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING,
                                      related_name="user_creation_Pro", null=True, blank=True)
    user_updated = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING,
                                     related_name="user_updated_Pro", null=True, blank=True)

    def get_image(self):
        if self.image:
            return f"{'/media/'}{self.image}"

        return '/static/img/product_empty.png'
    
    def toJSON(self):
        item = model_to_dict(self)
        item['image'] = f"{'/media/'}{self.image}" 
        return item

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_updated = user
        super(Product, self).save()

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        db_table = 'product'


class Inventory(models.Model):
    product = models.OneToOneField(Product, on_delete=models.DO_NOTHING, verbose_name='Name of product', unique=True)
    stock = models.PositiveIntegerField(default=0, verbose_name='Stock')
    date_updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    user_creation = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING,
                                      related_name="user_creation_Inv", null=True, blank=True)
    user_updated = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING,
                                     related_name="user_updated_Inv", null=True, blank=True)

    def __str__(self):
        return f"{self.product}"

    def toJSON(self):
        item = model_to_dict(self)
        return item

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_updated = user
        super(Inventory, self).save()

    class Meta:
        verbose_name = 'Inventory'
        verbose_name_plural = 'Inventories'
        db_table = 'inventory'


class Customer(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='First name')
    last_name = models.CharField(max_length=50, verbose_name='Last name')
    dni = models.PositiveIntegerField(verbose_name='Dni', unique=True)
    address = models.CharField(max_length=100, verbose_name='Address')
    email = models.EmailField(verbose_name='Email')
    amount_invoices = models.PositiveIntegerField(verbose_name='Amount of invoices', default=0)
    date_updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    user_creation = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING,
                                      related_name="user_creation_Cus", null=True, blank=True)
    user_updated = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING,
                                     related_name="user_updated_Cus", null=True, blank=True)

    def __str__(self):
        return f"{self.dni}"

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_updated = user
        super(Customer, self).save()

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        db_table = 'customer'


class Invoice(models.Model):
    list_of_products = models.ManyToManyField(Inventory, verbose_name='Products')
    employee = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, verbose_name='Employee')
    customer = models.OneToOneField(Customer, on_delete=models.DO_NOTHING, verbose_name='Customer')
    date_updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    user_creation = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING,
                                      related_name="user_creation_Invo", null=True, blank=True)
    user_updated = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING,
                                     related_name="user_updated_Invo", null=True, blank=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_updated = user
        super(Invoice, self).save()

    def toJSON(self):
        item = model_to_dict(self)
        item['list_of_products'] = ''
        for i in self.list_of_products.all():
            item['list_of_products'] += f"{str(i)}, "
        print(item)
        return item

    def __str__(self):
        return f"{self.id} {self.date_creation}"

    class Meta:
        verbose_name = 'Invoice'
        verbose_name_plural = 'Invoices'
        db_table = 'invoice'
