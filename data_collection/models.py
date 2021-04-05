from django.db import models


class Product(models.Model):
    article = models.PositiveIntegerField()
    name = models.CharField(max_length=80)
    photo = models.ImageField(upload_to='product_picture/')
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    product = models.ForeignKey(Product, models.SET_NULL, blank=True, null=True)
    manufacturer = models.CharField(max_length=80)

    def __str__(self):
        return self.manufacturer

