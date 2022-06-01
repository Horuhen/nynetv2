from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.IntegerChoices):
        EMPLOYEE = 1
        ADMINISTRATOR = 2
        SUPERVISOR = 3

    avatar = models.ImageField(upload_to='users/%Y%m', default='/static/img/product_empty.png', null=True, blank=True,
                               verbose_name="Avatar")
    dni = models.PositiveIntegerField(verbose_name='Dni', unique=True, default=123456789)
    address = models.CharField(max_length=100, verbose_name='Address', default='aqui')
    role = models.IntegerField(choices=Role.choices, default=Role.EMPLOYEE, verbose_name="Role")

    def get_image(self):
        if self.avatar:
            return f"{'/media/'}{self.avatar}"

        return '/static/img/user_empty.png'
