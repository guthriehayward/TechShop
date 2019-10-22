from django.db import models
from django.utils import timezone

class ProductCategory(models.Model):
    product_category = models.CharField(max_length = 255)
    category_summary = models.CharField(max_length = 255)
    category_slug = models.CharField(max_length = 255)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.product_category

class ProductManufacturer(models.Model):
    product_manufacturer = models.CharField(max_length=255)

    product_category = models.ForeignKey(ProductCategory, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
    manufacturer_summary = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Manufacturer"

    def __str__(self):
        return self.product_manufacturer

class Product(models.Model):
    productName = models.CharField(max_length = 255)
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    description = models.TextField(default="")
    uploadDate = models.DateTimeField("date uploaded", default=timezone.now)
    product_category = models.ForeignKey(ProductCategory, default=1, verbose_name = "Category", on_delete=models.SET_DEFAULT)
    product_manufacturer = models.ForeignKey(ProductManufacturer, default=1, verbose_name="Manufacturer", on_delete=models.SET_DEFAULT)
    product_slug = models.CharField(max_length=255, default=1)

    def __str__(self):
        return self.productName
