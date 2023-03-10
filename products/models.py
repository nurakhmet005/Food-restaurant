from django.db import models


class Product (models.Model):
    name = models.CharField("Имя", max_length=128)
    description = models.TextField(max_length=256, blank = True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return " %s" % self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class ProductImage (models.Model):
    product = models.ForeignKey(Product,  blank = True, null=True, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products_images/")
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Заказ %s" % self.id

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"
# Create your models here.
