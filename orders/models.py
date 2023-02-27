from django.db import models
from products.models import Product


class Status (models.Model):
    name = models.CharField(max_length=24, blank = True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Статус %s" % self.name

    class Meta:
        verbose_name = "Статус заказа"
        verbose_name_plural = "Статусы заказа"


class Order (models.Model):
    total_amount = models.DecimalField("Сумма", max_digits=15, decimal_places=2, default=0) #total price for all products
    customer_name = models.CharField("Имя", max_length=128)
    cutomer_phone = models.CharField("Номер телефона", max_length=128, blank = True, null=False, default=None)
    customer_address = models.CharField("Адрес", max_length=128, blank = False, null=True, default=None)
    comments = models.TextField(max_length=256, blank = True, null=True, default=None)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Заказ %s %s" % (self.id, self.status.name)
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class ProductInOrder (models.Model):
    order = models.ForeignKey(Order, blank = True, null=True, default=None, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, blank = True, null=True, default=None, on_delete=models.CASCADE)
    number = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.product.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

# Create your models here.
